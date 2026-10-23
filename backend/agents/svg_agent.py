"""
SVG Studio Agentic System (LangChain).

Tools:
  - generate_svg
  - optimize_svg
  - explain_svg
  - suggest_edits
"""

from __future__ import annotations

from typing import Any, Optional

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from backend.providers import get_llm


# ── Tools ───────────────────────────────────────────────────────────────────

@tool
def generate_svg(description: str, width: int = 200, height: int = 200) -> str:
    """Generate clean, modern SVG markup from a natural language description.
    Prefer gradients, soft shadows, and viewBox. Return ONLY the SVG code."""
    return (
        f"[Generate SVG request]\n"
        f"Description: {description}\n"
        f"Preferred size: {width}x{height}\n"
        f"Return a complete, valid <svg> element with xmlns and viewBox."
    )


@tool
def optimize_svg(svg_code: str) -> str:
    """Optimize / clean an existing SVG: remove unnecessary attributes,
    minify paths where possible, ensure proper viewBox, keep visual fidelity."""
    return (
        f"[Optimize request]\n"
        f"Original SVG:\n{svg_code}\n"
        f"Return the optimized SVG only."
    )


@tool
def explain_svg(svg_code: str) -> str:
    """Explain the structure, elements, paths, gradients and overall design
    of the given SVG in clear language."""
    return (
        f"[Explain request]\n"
        f"SVG to explain:\n{svg_code}\n"
        f"Provide a concise, structured explanation."
    )


@tool
def suggest_edits(svg_code: str, goal: str) -> str:
    """Suggest concrete code-level edits to reach a goal
    (e.g. 'make it blue', 'add a drop shadow', 'center the icon')."""
    return (
        f"[Suggest edits request]\n"
        f"Current SVG:\n{svg_code}\n"
        f"Goal: {goal}\n"
        f"Return the modified SVG and a short list of changes made."
    )


TOOLS = [generate_svg, optimize_svg, explain_svg, suggest_edits]


SYSTEM_PROMPT = """You are SVG Studio AI — an expert SVG designer and coding assistant embedded inside SVG Studio.

You help users:
- Generate beautiful, modern SVG icons and illustrations from descriptions
- Optimize and clean existing SVG code
- Explain complex path data, gradients, filters, and structure
- Suggest precise edits

Rules:
1. When generating or editing SVG, ALWAYS return a complete, valid <svg> element that includes xmlns="http://www.w3.org/2000/svg" and a sensible viewBox.
2. Prefer clean, modern aesthetics: soft gradients, rounded shapes, good contrast.
3. Keep code readable (pretty-printed) unless the user asks for minified.
4. If the user has a current SVG loaded, you will receive it in context — use it.
5. Be concise. Prefer code blocks over long prose.
6. Use the available tools when they help structure the work.
"""


def build_agent(
    provider: Optional[str] = None,
    model: Optional[str] = None,
) -> AgentExecutor:
    llm = get_llm(provider=provider, model=model)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(llm, TOOLS, prompt)
    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=6,
    )


def run_agent(
    message: str,
    *,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    svg_content: Optional[str] = None,
    history: Optional[list[dict[str, str]]] = None,
) -> dict[str, Any]:
    """
    Execute one turn of the agent.
    Returns {"output": str, "provider": str, "model": str}
    """
    agent = build_agent(provider=provider, model=model)

    enriched = message
    if svg_content and svg_content.strip():
        enriched = (
            f"Current SVG loaded in the studio:\n```svg\n{svg_content.strip()}\n```\n\n"
            f"User request: {message}"
        )

    chat_history = []
    if history:
        for turn in history[-8:]:
            role = turn.get("role", "user")
            content = turn.get("content", "")
            if role == "user":
                chat_history.append(HumanMessage(content=content))
            elif role == "assistant":
                chat_history.append(AIMessage(content=content))

    result = agent.invoke(
        {
            "input": enriched,
            "chat_history": chat_history,
        }
    )

    return {
        "output": result.get("output", ""),
        "provider": provider or "default",
        "model": model or "default",
    }
