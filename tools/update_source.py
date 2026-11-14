"""Add a new build to docs/altstore-source.json (used by the iOS workflow).

Usage: python tools/update_source.py <app-id> <version> <build> <ipa-path> <download-url> "<notes>"
"""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "docs", "altstore-source.json")
KEEP = 5  # versions listed per app


def main():
    app_id, version, build, ipa, url, notes = sys.argv[1:7]
    src = json.load(open(PATH, encoding="utf-8"))
    app = next(a for a in src["apps"] if a["bundleIdentifier"] == app_id)
    entry = {
        "version": version,
        "buildVersion": build,
        "date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "localizedDescription": notes,
        "downloadURL": url,
        "size": os.path.getsize(ipa),
        "minOSVersion": "15.0",
    }
    app["versions"] = [entry] + [v for v in app.get("versions", []) if v["version"] != version][: KEEP - 1]
    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(src, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{app_id} {version} added ({entry['size']:,} bytes)")


if __name__ == "__main__":
    sys.exit(main())
