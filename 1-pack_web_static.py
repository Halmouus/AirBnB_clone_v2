#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the
web_static folder"""
from fabric.api import local, task
from datetime import datetime

@task
def do_pack():
    """generates a .tgz archive from the contents
    of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path
    return None
