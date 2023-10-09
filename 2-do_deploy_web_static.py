#!/usr/bin/python3
"""
Fabric script that distributes an archive to the
web servers using the function do_deploy
"""

from fabric.api import env, put, run
from os.path import exists, splitext, basename

env.hosts = ['18.204.5.75', '52.3.244.101']


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers using the function do_deploy
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = basename(archive_path)
        dest = splitext(archive_name)[0]
        tmp = "/tmp/{}".format(archive_name)
        path = "/data/web_static/releases/{}".format(dest)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path))
        run('tar -xzf {}  -C {}'.format(tmp, path))
        run('rm {}'.format(tmp))
        run('mv {}/web_static/* {}/'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        return True

    except Exception:
        return False
