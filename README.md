# SVG Studio AI

**Textile-aware SVG design studio + client-side multi-provider AI chat.**

Pure static — works on **GitHub Pages** with zero backend.  
Original liquid-glass SVG Studio + floating AI chat powered by a professional textile design system prompt (motifs, repeats, half-drop, colorways, validation).

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
- One-click “Load this SVG into studio”
- **Conversation auto-saves** in browser
- **Clear Chat** + **Download Chat** (.txt)
- System prompt tuned for textile design:
  - Motif hierarchy & composition
  - Repeat types (straight, half-drop, half-brick, tossed, mirror, ogee…)
  - Edge-wrap / seam integrity rules
  - Editable SVG hygiene & validation notes
  - Apparel / lawn / scarf / upholstery / wallpaper ready thinking

## Deploy to GitHub Pages

1. Repo is public: https://github.com/AdnanRaza88/svg-studio-ai
2. Replace `index.html` with the full static file (download from conversation if needed)
3. **Settings → Pages** → Branch `main` / root → Save
4. Live at: `https://adnanraza88.github.io/svg-studio-ai/`

## How to use the chat

1. Click 💬
2. Choose provider (Gemini recommended)
3. Paste API key → **Save**
4. Ask e.g.:
   - “Design a half-drop floral tile for lawn, soft indigo palette, 600×600”
   - “Optimize the current SVG for textile repeat”
   - “Suggest a secondary leaf motif that fits this flower”
5. Load returned SVG into the studio with one click
6. Export PNG/JPG/WebP/SVG as usual

Conversation is auto-saved. Use **Download Chat** to keep a text log.

### Recommended keys
- Gemini → https://aistudio.google.com/apikey
- Groq → https://console.groq.com

## Privacy

API keys stay in your browser. No backend, no tracking.

## License

MIT
