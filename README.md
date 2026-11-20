# Danny's Apps

Apps I build, delivered as websites on GitHub Pages. They work on iPhone, iPad and desktop browsers, and can be added to the Home Screen.

## Install

Open the hub page at `https://ynnadcor.github.io/dannys-apps/` in Safari, open an app, then Share → Add to Home Screen. Open it once while online; after that it works offline.

## Apps

| App | Source of truth | Website |
| --- | --- | --- |
| Engine Academy | `THECAR/learning-game/engine-academy.html` | `docs/engine-academy/` |

## Update Engine Academy

```
python tools/sync_engine_academy.py
git add -A && git commit -m "Engine Academy: <what changed>" && git push
```

The push updates the website through GitHub Pages. The sync script bumps the service-worker cache version, so phones load the new version the next time they open it online.

## Add another app

1. Put its web files in `docs/<app>/` (with `manifest.webmanifest`, icons and `sw.js` like Engine Academy).
2. Add a card for it on `docs/index.html`.

## Layout

- `docs/` is served by GitHub Pages (hub page and web apps).
- `tools/` holds the sync and icon scripts.

## iOS app build (turned off)

The repo still holds an iOS wrapper for Engine Academy, but its build is turned off: the GitHub Actions workflow `engine-academy-ios.yml` is disabled, so pushes no longer build an `.ipa` or update `docs/altstore-source.json`. The files are kept in case it is wanted again:

- `.github/workflows/engine-academy-ios.yml`: the build workflow. Turn it back on with `gh workflow enable engine-academy-ios.yml`.
- `apps/engine-academy/`: the XcodeGen spec and Swift wrapper.
- `docs/altstore-source.json` and `tools/update_source.py`: the SideStore/AltStore source and the script that updated it.
