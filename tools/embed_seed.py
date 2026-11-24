"""Incrusta la biblioteca de ejercicios en index.html.

Lee data/exercises/*.json y data/media/musculos.json, cambia cada
"/_blob/<id>" por la ruta del archivo en assets/ y escribe el resultado
entre los marcadores SEED_LIB de index.html.

Una copia nueva de la app usa ese bloque para llenar su biblioteca la
primera vez que se abre. Las imágenes se cargan desde assets/, que se
publica junto a index.html.

Uso (desde la carpeta del repositorio):
    python3 tools/embed_seed.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- SEED_LIB:start -->", "<!-- SEED_LIB:end -->"

assets = {p.stem: p.name for p in (ROOT / "assets").iterdir() if p.is_file()}
missing = set()


def local(url):
    m = re.fullmatch(r"/_blob/([0-9a-f]{32})", url or "")
    if not m:
        return url
    if m.group(1) not in assets:
        missing.add(m.group(1))
        return url
    return "assets/" + assets[m.group(1)]


exercises = {}
for f in sorted((ROOT / "data" / "exercises").glob("*.json")):
    x = json.loads(f.read_text(encoding="utf-8"))
    x.pop("creadoPor", None)
    x["imagenes"] = [local(u) for u in x.get("imagenes") or []]
    exercises[f.stem] = x

media = json.loads((ROOT / "data" / "media" / "musculos.json").read_text(encoding="utf-8"))
for v in media.values():
    if isinstance(v, dict) and "url" in v:
        v["url"] = local(v["url"])

if missing:
    sys.exit("Faltan imágenes en assets/: " + ", ".join(sorted(missing)))

payload = json.dumps({"exercises": exercises, "media": media}, ensure_ascii=False, separators=(",", ":"))
payload = payload.replace("<", "\\u003c")
block = f'{START}\n<script type="application/json" id="seed-lib">{payload}</script>\n{END}'

html_path = ROOT / "index.html"
html = html_path.read_text(encoding="utf-8")
if START in html:
    html = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, html, flags=re.S)
else:
    anchor = '<div id="app"'
    html = html.replace(anchor, block + "\n" + anchor, 1)
html_path.write_text(html, encoding="utf-8")
print(f"{len(exercises)} ejercicios y {len(media)} músculos incrustados ({len(payload) // 1024} KB)")
