import logging as log
import os
from config import get_fonts_dir, get_fonts_backup_dir, get_app_support_dir, get_app_support_backup_dir
from utils import copy_dir


def backup():
    # Backup targeted Application Support
    targeted_apps = [
        'com.mitchellh.ghostty',
        'com.lwouis.alt-tab-macos',
        'Rectangle',
    ]

    log.info('Backing up targeted Application Support...')
    app_support_src = get_app_support_dir()
    app_support_dest = get_app_support_backup_dir()

    for app in targeted_apps:
        src = os.path.join(app_support_src, app)
        if os.path.exists(src):
            # For nested paths, we need to create the parent directory in backup
            rel_parent = os.path.dirname(app)
            
            if rel_parent:
                dest_subdir = os.path.join(app_support_dest, rel_parent)
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                copy_dir(src, dest_subdir)
            else:
                copy_dir(src, app_support_dest)
        else:
            log.debug('App Support directory not found: ' + src)


def restore():
    log.info('Restoring targeted Application Support...')
    if os.path.exists(get_app_support_backup_dir()):
        copy_dir(get_app_support_backup_dir(), get_app_support_dir())
