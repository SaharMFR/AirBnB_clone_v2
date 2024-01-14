#!/usr/bin/python3
"""
Fabric script (based on the file `1-pack_web_static.py`) distributes
an archive to my web servers , using the function `do_deploy`.
"""

from fabric.api import *
import os

env.hosts = ['35.175.129.78', '100.25.45.229']


def do_deploy(archive_path):
    """ Distributes an archive to my web servers """

    try:
        if os.path.exists(archive_path):
            path_list = archive_path.split("/")
            arg_save = path_list[1]
            path_list = path_list[1].split('.')
            arc_tgz = path_list[0]

            put(archive_path, '/tmp')
            uncompressed = '/data/web_static/releases/{}'.format(arc_tgz)
            tmp = '/tmp/{}'.format(arg_save)

            run('mkdir -p {}'.format(uncompressed))
            run('tar -xvzf {} -C {}'.format(tmp, uncompressed))
            run('rm {}'.format(tmp))
            run('mv {}/web_static/* {}'.format(uncompressed, uncompressed))
            run('rm -rf {}/web_static'.format(uncompressed))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(uncompressed))
            run('sudo service nginx restart')

            return True
        else:
            return False
    except Exception:
        return False
