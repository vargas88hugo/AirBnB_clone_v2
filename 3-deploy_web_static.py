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


def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        file = ntpath.basename(archive_path)
        folder = file[:-4]
        run("mkdir -p /data/web_static/releases/" + folder)
        run("tar -xzf /tmp/" + file + " -C /data/web_static/releases/" + folder)
        run("rm /tmp/" + file)
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/" + folder +
            " /data/web_static/current")
        return True
    except Exception:
        return False
