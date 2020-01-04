#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""


from fabric.api import env
from fabric.api import put
from fabric.api import run
import os
import ntpath


env.user = "ubuntu"
env.hosts = ["35.196.230.188", "34.73.178.142"]


def deploy():
    var = do_pack()
    if not var:
        return False
    return do_deploy(var)


def do_pack():
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    if not os.path.exists("versions/"):
        os.mkdir("versions/")

    with tarfile.open("versions/" + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))

    if os.path.exists("versions/" + filename):
        return "versions/" + filename

    return None


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        file = ntpath.basename(archive_path)
        folder = file[:-4]
        run("mkdir -p /data/web_static/releases/" + folder)
        run("tar -xzf /tmp/" + file + " -C /data/web_static/releases/" +
            folder)
        run("rm /tmp/" + file)
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/" + folder +
            "/web_static/ /data/web_static/current")
        return True
    except Exception:
        return False
