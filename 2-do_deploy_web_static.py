#!/usr/bin/python3
"""
Script that distributes an archive to your web servers,
using the function do_deploy
"""
import os.path
from fabric.api import *


#env.hosts = ['54.87.158.226', '34.229.186.174']
#env.user = 'ubuntu'
#env.key_filename = '~/.ssh/school'


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
        directory = "/data/web_static/releases/" /
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
    except Exception as e:
        print(e)
        return False
