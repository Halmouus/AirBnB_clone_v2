#!/usr/bin/python3
"""
Fabric script that distributes an archive to the
web servers using the function do_deploy
"""

from fabric.api import env, put, run
import os

env.user = 'ubuntu'
env.hosts = ['18.204.5.75', '52.3.244.101']


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers using the function do_deploy
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        dirname = f"/data/web_static/releases/{filename.split('.')[0]}"
        run(f"mkdir -p {dirname}")
        run(f"tar -xzf /tmp/{filename} -C {dirname}")
        run(f"rm /tmp/{filename}")
        slink = "/data/web_static/current"
        run(f"rm -rf {slink}")
        run(f"ln -s {dirname} {slink}")
        return True

    except Exception:
        return False
