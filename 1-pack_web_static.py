#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """ function """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static_{}.tgz".format(now)
    command_tgz = "tar -cvzf {} web_static".format(name_file)
    if local(command_tgz) == 1:
        return None
    return name_file
