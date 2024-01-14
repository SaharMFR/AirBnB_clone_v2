#!/usr/bin/python3
"""
Fabric script that generates a `.tgz` archive from the content
of the `web_static` folder , using the function `do_pach`.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        date = (datetime.now()).strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(path))
        return path
    except Exception:
        return None
