#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the 
# web_static folder of your AirBnB Clone repo, using the function do_pack.

from fabric.api import local
from datetime import datetime


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
