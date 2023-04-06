#!/usr/bin/python3
"""
Script that deploys web_static
"""
import os.path
from fabric.api import *
from datetime import datetime


env.hosts = ['54.87.158.226', '34.229.186.174']
env.user = 'ubuntu'
# env.key_filename = '~/.ssh/school'


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


def do_deploy(archive_path):
    """Distribute archive to the servers"""
    # check if archive exitst
    if not os.path.exists(archive_path):
        return False

    try:
        # upload archived file
        put(archive_path, "/tmp/")

        # uncompress archived files
        filename = os.path.basename(archive_path)
        directory = "/data/web_static/releases/" \
            + os.path.splitext(filename)[0] + "/"
        # print("Directory: {}".format(directory))
        run("mkdir -p {}".format(directory))
        run("tar -xzf /tmp/{} -C {} --strip-components=1"
            .format(filename, directory))

        # delete archive from server
        run("rm /tmp/{}".format(filename))

        # delete symbolic link
        run("rm -rf /data/web_static/current")

        # Recreate symbolic link
        run("ln -s {} /data/web_static/current"
            .format(directory))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
