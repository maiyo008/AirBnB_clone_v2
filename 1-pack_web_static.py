#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents
of the web_static folder of AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress web_static folder to a .tgz archive"""
    local("mkdir -p versions")
    now = datetime.utcnow()
    tar_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.day
    )
    result = local("tar -czvf {} web_static". format(tar_file))

    if result.succeeded:
        return tar_file
    else:
        return None
