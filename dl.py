#! /usr/bin/env python3

"""
télécharge les exemples de https://amienspython.tuxfamily.org
"""

import requests
import re
import pathlib

BASE_URL = "http://amienspython.tuxfamily.org/sources/"

sess = requests.Session()

codes = dict()

# lit la table des matières
r = sess.get(BASE_URL + "view.php")
for code, description in re.findall(rb"<a href=view.php\?code=(.+?)>(.+?)</a>", r.content):
    codes[code.decode("iso-8859-1")] = description.decode("iso-8859-1")

# lit la liste des fichiers
r = sess.get(BASE_URL + "codes/")
for uri, file in re.findall(r'<a href="(.+?)">(.+?)</a>', r.text):

    dest_file = pathlib.Path("codes") / file
    if dest_file.exists():
        continue

    suffix = dest_file.suffix

    if suffix not in [".csv", ".txt", ".py"]:
        continue

    dest_file.parent.mkdir(exist_ok=True, parents=True)

    if suffix != ".py":
        c = sess.get(BASE_URL + "codes/" + uri)
        dest_file.write_text(c.content.decode("iso-8859-1"))

        print("téléchargé: {:<20}".format(file))
    else:
        url = BASE_URL + "codes/" + uri
        file = file[:-3]

        c = sess.get(url)

        code = c.content

        # Nota: les codes source sont stockés dans un pseudo-format UCS-2BE mal maitrisé
        # probablement un micmac de wchar_t et char

        # enlève le BOM
        if code[0:2] == b"\xff\xfe":
            code = code[2:]

        code = [c for c in code if c != 0]
        code = bytes(code)
        source = code.decode("iso-8859-1").strip() + "\n"

        # ajoute un entête
        source = "# " + codes.get(file, "???") + "\n# " + url + "\n\n" + source

        # écrit le fichier
        dest_file.write_text(source)

        print("téléchargé: {:<20} {}".format(file, codes.get(file, "")))
