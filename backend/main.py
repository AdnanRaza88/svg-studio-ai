"""
SVG Studio AI — FastAPI backend with LangChain agent.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend.agents.svg_agent import run_agent
from backend.providers import list_available_providers

load_dotenv()

app = FastAPI(
    title="SVG Studio AI",
    description="Agentic SVG assistant powered by LangChain + multi-provider LLMs",
    version="1.0.0",
)

origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROOT = Path(__file__).resolve().parent.parent
if (ROOT / "index.html").exists():
    app.mount("/static", StaticFiles(directory=str(ROOT)), name="static")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    provider: Optional[str] = None
    model: Optional[str] = None
    svg_content: Optional[str] = None
    history: Optional[list[dict[str, str]]] = None


class ChatResponse(BaseModel):
    output: str
    provider: str
    model: str


@app.get("/")
async def root():
    index = ROOT / "index.html"
    if index.exists():
        return FileResponse(index)
    return {"status": "ok", "docs": "/docs"}


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "providers": list_available_providers(),
    }


@app.get("/api/providers")
async def providers():
    return list_available_providers()


@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        result = run_agent(
            req.message,
            provider=req.provider,
            model=req.model,
            svg_content=req.svg_content,
            history=req.history,
        )
        return ChatResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
