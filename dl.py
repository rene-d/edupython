#! /usr/bin/env python3

"""
télécharge les exemples de https://edupython.tuxfamily.org
"""

import requests
import re
import pathlib
import black


sess = requests.Session()

codes = dict()

# lit la table des matières
r = sess.get("https://edupython.tuxfamily.org/sources/view.php")
for code, description in re.findall(
    rb"<a href=view.php\?code=(.+?)>(.+?)</a>", r.content
):
    codes[code.decode("iso-8859-1")] = description.decode("iso-8859-1")

# lit la liste des fichiers
r = sess.get("https://edupython.tuxfamily.org/sources/codes/")
for uri, file in re.findall(r'<a href="(.+?)">(.+?)</a>', r.text):

    dest_file = pathlib.Path("codes") / file
    if dest_file.exists():
        continue

    suffix = dest_file.suffix

    if suffix not in [".csv", ".txt", ".py"]:
        continue

    dest_file.parent.mkdir(exist_ok=True, parents=True)

    if suffix != ".py":
        c = sess.get("https://edupython.tuxfamily.org/sources/codes/" + uri)
        dest_file.write_text(c.content.decode("iso-8859-1"))

        print("téléchargé: {:<20}".format(file))
    else:
        # malheureusement le serveur est mal configuré et on ne peut pas
        # obtenir directement un .py (ou est-ce volontaire ?)

        file = file[:-3]
        uri = uri[:-3]

        url = "https://edupython.tuxfamily.org/sources/view.php?code=" + uri
        c = requests.get(url)

        code = c.content

        i = code.find(b'<pre class="brush: python;">')
        assert i != -1
        i += len(b'<pre class="brush: python;">')

        j = code.find(b"</pre>", i)
        assert j != -1

        # extrait le code source du document html
        source = code[i:j].decode("iso-8859-1").strip() + "\n"

        # ajoute un entête
        source = "# " + codes.get(file, "???") + "\n# " + url + "\n\n" + source

        # on peut reformater selon des standards modernes d'écriture...
        # try:
        #     s = black.format_str(source, mode=black.FileMode())
        #     source = s
        # except black.InvalidInput:
        #     pass

        # écrit le fichier
        dest_file.write_text(source)

        print("téléchargé: {:<20} {}".format(file, codes.get(file, "")))
