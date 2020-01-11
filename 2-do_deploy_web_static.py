#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.user = 'ubuntu'
env.hosts = ['34.73.191.78', '35.243.240.10']


def do_pack():
    """Convert web_static into .tgz file"""
    time = datetime.now()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
            time.year,
            time.month,
            time.day,
            time.hour,
            time.minute,
            time.second
    )
    local('mkdir -p versions')
    if local('tar -cvzf ' + file + ' web_static').succeeded:
        return file
    return None

def do_deploy(archive_path):
    """
    Deployment on servers
    """
    if isfile(archive_path):
        source_name = basename(archive_path)
        source_path = join(sep, 'tmp', source_name)
        dest_name = splitext(source_name)[0]
        dest_path = join(sep, 'data', 'web_static', 'releases', dest_name)
        put(archive_path, source_path)
        run('mkdir -p {}'.format(
            quote(dest_path)
        ))
        run('tar -xzf {} -C {}'.format(
            quote(source_path),
            quote(dest_path)
        ))
        run('rm -f {}'.format(
            quote(source_path)
        ))
        run('mv {} {}'.format(
            join(quote(join(dest_path, 'web_static')), '*'),
            quote(join(dest_path, ''))
        ))
        run('rm -rf {}'.format(
            quote(join(dest_path, 'web_static'))
        ))
        run('rm -rf {}'.format(
            quote(join(sep, 'data', 'web_static', 'current'))
        ))
        run('ln -s {} {}'.format(
            quote(dest_path),
            quote(join(sep, 'data', 'web_static', 'current'))
        ))
        return True
    return False
