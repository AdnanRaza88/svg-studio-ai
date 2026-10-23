# SVG Studio AI

**Preview, edit & convert SVG files — with an integrated agentic AI chatbot.**

A modern, liquid-glass UI SVG tool (original client-side studio) enhanced with a LangChain-powered multi-provider AI agent. The agent understands SVG, can generate code, suggest improvements, explain markup, and help with conversion workflows.

## Features

### Core Studio (unchanged behavior)
- Drag & drop or paste SVG code
- Live preview with zoom controls
- Export to PNG / JPG / WebP / SVG at custom scales
- Background color control for JPG
- Beautiful liquid-morphism glass UI

### AI Chatbot (new)
- **Agentic system** built with LangChain
- Multi-provider support:
  - **Remote**: Google Gemini, OpenAI, Anthropic, Groq
  - **Local**: Ollama (any local model)
- Context-aware: the agent can see the currently loaded SVG
- Tools: generate SVG from description, optimize existing SVG, explain code, suggest edits
- Provider & model switcher in the UI

## Quick Start

### 1. Clone
```bash
git clone https://github.com/AdnanRaza88/svg-studio-ai.git
cd svg-studio-ai
```

### 2. Backend setup
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add at least one API key
```

### 3. Run
```bash
# Terminal 1 – API
uvicorn backend.main:app --reload --port 8000

# Then open http://localhost:8000  (serves index.html + API)
```

## Environment Variables

See `.env.example`. You only need keys for the providers you want to use.

```env
# At least one required
GOOGLE_API_KEY=...          # Gemini
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GROQ_API_KEY=...

# Local
OLLAMA_BASE_URL=http://localhost:11434

# Default provider when UI does not specify
DEFAULT_PROVIDER=gemini
DEFAULT_MODEL=gemini-2.0-flash
```

## Project Structure

```
svg-studio-ai/
├── index.html              # Full SVG Studio + Chat UI (original design preserved + chat panel)
├── backend/
│   ├── main.py             # FastAPI app + LangChain agent
│   ├── agents/
│   │   └── svg_agent.py    # Agentic system, tools, multi-provider factory
│   └── providers.py        # LLM provider factory (Gemini, OpenAI, Anthropic, Groq, Ollama)
├── requirements.txt
├── .env.example
└── README.md
```

## Agentic Capabilities

The agent has these tools available:

| Tool | Description |
|------|-------------|
| `generate_svg` | Create SVG markup from a natural-language description |
| `optimize_svg` | Clean / minify / improve an existing SVG |
| `explain_svg` | Explain structure, paths, gradients, etc. |
| `suggest_edits` | Propose concrete changes to the current SVG |

The current SVG content (if loaded in the studio) is automatically injected into the agent context.

## API

```
POST /api/chat
{
  "message": "Make a purple circle with a gradient",
  "provider": "gemini",          # optional
  "model": "gemini-2.0-flash",   # optional
  "svg_content": "<svg>...</svg>", # optional – current canvas
  "history": [...]               # optional chat history
}
```

## License

MIT

---

Original pure-frontend SVG Studio design preserved and extended.  
Built with LangChain + FastAPI for production-ready multi-provider agents.
