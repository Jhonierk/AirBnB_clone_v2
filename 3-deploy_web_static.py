#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone
"""
from datetime import datetime
from fabric.api import *
from os.path import isfile

env.host = ["35.231.149.99", "3.80.36.203"]


def do_pack():
    """ function """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static_{}.tgz".format(now)
    command_tgz = "tar -cvzf {} web_static".format(name_file)
    if local(command_tgz) == 1:
        return None
    return name_file


def do_deploy(archive_path):
    """funtion """
    if isfile(archive_path) is False:
        return False

    try:

        name = archive_path.split("/")[1].split(".")[0]
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # path releases
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        # Uncompress the archive to the folder
        run(" tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(name, name))
        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(name))
        # move all files
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        # delete folder web_static
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))

    except Exception:
        return False
    return True


def deploy():
    """ that creates and distributes an archive to your web servers,
        using the function
    """
    archive_path = do_pack()

    if archive_path is None:
        return False
    return do_deploy(archive_path)
