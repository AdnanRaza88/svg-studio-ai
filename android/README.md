# SVG Studio AI — Android (Kotlin)

Light-theme textile design app. Jetpack Compose.

## Screens
- **Home** — dashboard
- **Studio** — upload SVG, preview, save locally
- **Chat** — Gemini + textile system prompt (motifs, half-drop, edge-wrap)
- **Patterns** — local saved designs with previews
- **Settings** — API key (device only)

## Build APK (local)
```bash
cd android
gradle wrapper --gradle-version 8.9
./gradlew assembleDebug
# APK: app/build/outputs/apk/debug/app-debug.apk
```

## GitHub Actions
Workflow **Build APK** builds debug APK on push to `android/**`.

## System prompt
Textile design engine (motifs, repeats, validation). Raw skill not shipped in APK.
