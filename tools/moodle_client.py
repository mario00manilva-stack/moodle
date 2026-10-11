#!/usr/bin/env python3
"""Cliente mínimo para la API REST de Moodle (web services).

Solo usa la librería estándar. Configuración por variables de entorno:
  MOODLE_URL    p. ej. https://formacion.veraqua.es
  MOODLE_TOKEN  token del servicio web (NUNCA se guarda en el repositorio)

Uso:
  python3 tools/moodle_client.py info               # datos del sitio y funciones permitidas al token
  python3 tools/moodle_client.py courses            # lista de cursos
  python3 tools/moodle_client.py contents <id>      # secciones y actividades de un curso
  python3 tools/moodle_client.py dump <id> [dir]    # vuelca la estructura del curso a JSON
  python3 tools/moodle_client.py call <wsfunction> [clave=valor ...]  # llamada genérica
"""
import json
import os
import sys
import urllib.parse
import urllib.request


class MoodleError(Exception):
    pass


class Moodle:
    def __init__(self, url=None, token=None):
        self.url = (url or os.environ.get("MOODLE_URL", "")).rstrip("/")
        self.token = token or os.environ.get("MOODLE_TOKEN", "")
        if not self.url or not self.token:
            raise MoodleError("Define MOODLE_URL y MOODLE_TOKEN")

    def call(self, wsfunction, **params):
        data = {"wstoken": self.token, "wsfunction": wsfunction, "moodlewsrestformat": "json"}
        data.update(flatten(params))
        req = urllib.request.Request(
            f"{self.url}/webservice/rest/server.php",
            data=urllib.parse.urlencode(data).encode(),
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.load(resp)
        if isinstance(result, dict) and "exception" in result:
            raise MoodleError(f"{result.get('errorcode')}: {result.get('message')}")
        return result

    def site_info(self):
        return self.call("core_webservice_get_site_info")

    def courses(self):
        return self.call("core_course_get_courses")

    def contents(self, courseid):
        return self.call("core_course_get_contents", courseid=int(courseid))


def flatten(value, prefix=""):
    """Convierte dicts/listas anidados al formato de Moodle: a[0][b]=c."""
    out = {}
    if isinstance(value, dict):
        for k, v in value.items():
            out.update(flatten(v, f"{prefix}[{k}]" if prefix else str(k)))
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            out.update(flatten(v, f"{prefix}[{i}]"))
    elif isinstance(value, bool):
        out[prefix] = int(value)
    else:
        out[prefix] = value
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    m = Moodle()
    cmd, args = argv[1], argv[2:]
    if cmd == "info":
        info = m.site_info()
        print(f"Sitio: {info['sitename']}  Moodle {info.get('release')}")
        print(f"Usuario: {info['username']} (id {info['userid']})")
        print("Funciones permitidas:")
        for f in sorted(fn["name"] for fn in info.get("functions", [])):
            print("  ", f)
    elif cmd == "courses":
        for c in m.courses():
            print(f"{c['id']:>5}  {c['shortname']:<25} {c['fullname']}")
    elif cmd == "contents":
        for s in m.contents(args[0]):
            print(f"[{s['section']}] {s['name']}")
            for mod in s.get("modules", []):
                print(f"     - {mod['modname']:<10} {mod['name']} (cmid {mod['id']})")
    elif cmd == "dump":
        outdir = args[1] if len(args) > 1 else "export"
        os.makedirs(outdir, exist_ok=True)
        path = os.path.join(outdir, f"course_{args[0]}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(m.contents(args[0]), fh, ensure_ascii=False, indent=2)
        print(path)
    elif cmd == "call":
        params = dict(a.split("=", 1) for a in args[1:])
        print(json.dumps(m.call(args[0], **params), ensure_ascii=False, indent=2))
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except MoodleError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
