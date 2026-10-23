# SVG Studio AI

**Preview, edit & convert SVG files + client-side AI chatbot.**

Pure static site — works on **GitHub Pages** with zero backend.  
Original liquid-glass SVG Studio + floating AI chat that talks directly to Gemini / OpenAI / Anthropic / Groq.

## Features

### Core Studio
- Drag & drop or paste SVG
- Live preview + zoom
- Export PNG / JPG / WebP / SVG at any scale
- Beautiful liquid-morphism glass UI

### AI Chat (client-side only)
- **No server required**
- Providers: **Gemini**, **OpenAI**, **Anthropic**, **Groq**
- Paste your own API key (stored only in `localStorage`)
- Context-aware: sees the currently loaded SVG
- One-click “Load this SVG into studio” when the model returns code
- Agentic-style system prompt (generate / optimize / explain / edit)

## Deploy to GitHub Pages (1 minute)

1. This repo is already public.
2. Go to **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: `main` / folder: `/ (root)`
5. Save → wait ~30–60 seconds

Your site will be live at:

```
https://adnanraza88.github.io/svg-studio-ai/
```

## Local use

Just open `index.html` in any modern browser, or:

```bash
npx serve .
# or python -m http.server 5500
```

## How the chat works

1. Click the 💬 button (bottom-right)
2. Choose provider
3. Paste API key → click **Save** (saved only in your browser)
4. Ask anything: “make a purple gradient circle”, “optimize this SVG”, “explain the paths”…
5. When the AI returns SVG code, click **Load this SVG into studio**

### Recommended free keys
- **Gemini** → [aistudio.google.com](https://aistudio.google.com/apikey) (best CORS support)
- **Groq** → [console.groq.com](https://console.groq.com)

## Privacy

- API keys never leave your browser except to the provider you chose.
- No analytics, no backend, no tracking.

## License

MIT

---

Original pure-frontend SVG Studio design preserved and extended with a fully client-side multi-provider AI agent.
