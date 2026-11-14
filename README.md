# Danny's Apps

Apps I build for my iPhone and iPad. Each app is a web app that also ships as an iOS app.

## Install

- **Web app (no expiry):** open the hub page at `https://ynnadcor.github.io/dannys-apps/` in Safari, open an app, then Share → Add to Home Screen.
- **SideStore / AltStore:** add this source:
  `https://raw.githubusercontent.com/ynnadcor/dannys-apps/main/docs/altstore-source.json`

## Apps

| App | Source of truth | Web | iOS project |
| --- | --- | --- | --- |
| Engine Academy | `THECAR/learning-game/engine-academy.html` | `docs/engine-academy/` | `apps/engine-academy/` |

## Update Engine Academy

```
python tools/sync_engine_academy.py
git add -A && git commit -m "Engine Academy: <what changed>" && git push
```

The push rebuilds the iOS app in GitHub Actions (`.github/workflows/engine-academy-ios.yml`), publishes the unsigned `.ipa` as a release, and adds it to `docs/altstore-source.json`. SideStore/AltStore show it as an update.

## Add another app

1. Put its web files in `docs/<app>/` (with `manifest.webmanifest`, icons and `sw.js` like Engine Academy).
2. Copy `apps/engine-academy/` to `apps/<app>/` and change the names and bundle ID in `project.yml`.
3. Copy the workflow, change the paths and names.
4. Add an entry for it in `docs/altstore-source.json` and a card on `docs/index.html`.

## Layout

- `docs/` is served by GitHub Pages (hub page, web apps, the source file).
- `apps/` holds the iOS wrappers (XcodeGen specs and Swift). The workflow copies the app's `docs/` folder into the bundle, so the iOS app runs offline.
- `tools/` holds the sync, icon and source-update scripts.
