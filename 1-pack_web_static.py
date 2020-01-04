#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive
from contents of the web static
"""


import tarfile
import os
from datetime import datetime


def do_pack():
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    if not os.path.exists("versions/"):
        os.mkdir("versions/")

    with tarfile.open("versions/" + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))

    if os.path.exists("versions/" + filename):
        return "versions/" + filename

    return None
