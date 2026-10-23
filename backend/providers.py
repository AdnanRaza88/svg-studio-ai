"""
Multi-provider LLM factory.
Supports: Gemini, OpenAI, Anthropic, Groq, Ollama (local).
"""

from __future__ import annotations

import os
from typing import Any, Optional

from langchain_core.language_models.chat_models import BaseChatModel


def get_llm(
    provider: Optional[str] = None,
    model: Optional[str] = None,
    temperature: float = 0.4,
) -> BaseChatModel:
    """
    Return a LangChain chat model for the requested provider.
    Falls back to DEFAULT_PROVIDER / DEFAULT_MODEL from env.
    """
    provider = (provider or os.getenv("DEFAULT_PROVIDER", "gemini")).lower().strip()
    model = model or os.getenv("DEFAULT_MODEL")

    if provider in ("gemini", "google"):
        from langchain_google_genai import ChatGoogleGenerativeAI

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is not set")
        return ChatGoogleGenerativeAI(
            model=model or "gemini-2.0-flash",
            google_api_key=api_key,
            temperature=temperature,
        )

    if provider in ("openai", "gpt"):
        from langchain_openai import ChatOpenAI

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        return ChatOpenAI(
            model=model or "gpt-4o-mini",
            api_key=api_key,
            temperature=temperature,
        )

    if provider in ("anthropic", "claude"):
        from langchain_anthropic import ChatAnthropic

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set")
        return ChatAnthropic(
            model=model or "claude-3-5-sonnet-20241022",
            api_key=api_key,
            temperature=temperature,
        )

    if provider == "groq":
        from langchain_groq import ChatGroq

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set")
        return ChatGroq(
            model=model or "llama-3.3-70b-versatile",
            api_key=api_key,
            temperature=temperature,
        )

    if provider in ("ollama", "local"):
        from langchain_ollama import ChatOllama

        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        return ChatOllama(
            model=model or "llama3.2",
            base_url=base_url,
            temperature=temperature,
        )

    raise ValueError(
        f"Unknown provider '{provider}'. "
        "Supported: gemini, openai, anthropic, groq, ollama"
    )


def list_available_providers() -> dict[str, Any]:
    """Return which providers have credentials configured."""
    return {
        "gemini": bool(os.getenv("GOOGLE_API_KEY")),
        "openai": bool(os.getenv("OPENAI_API_KEY")),
        "anthropic": bool(os.getenv("ANTHROPIC_API_KEY")),
        "groq": bool(os.getenv("GROQ_API_KEY")),
        "ollama": True,  # always available if Ollama is running
    }
