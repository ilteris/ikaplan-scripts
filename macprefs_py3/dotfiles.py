from os import path, listdir
import logging as log
from config import get_dotfiles_backup_dir, get_dotfile_excludes, get_home_dir, get_user
from utils import copy_files, ensure_files_owned_by_user, copy_dir


def backup():
    log.info('Backing up dotfiles...')
    home_dir = get_home_dir()
    
    important_dot_dirs = [
        '.config', '.ssh', '.zsh', '.gnupg', 
        '.tmux', '.vim', '.local', '.oh-my-zsh', '.p10k.zsh'
    ]
    
    excludes = get_dotfile_excludes()
    
    files_to_copy = []
    dirs_to_copy = []
    
    for f in listdir(home_dir):
        if f[0] != '.':
            continue
        if f in excludes:
            continue
            
        full_path = path.join(home_dir, f)
        if path.isfile(full_path):
            files_to_copy.append(full_path)
        elif path.isdir(full_path) and f in important_dot_dirs:
            dirs_to_copy.append(f)

    dest = get_dotfiles_backup_dir()
    
    if files_to_copy:
        copy_files(files_to_copy, dest)
        
    for d in dirs_to_copy:
        src = path.join(home_dir, d)
        copy_dir(src, dest, excludes=excludes)


def restore():
    log.info('Restoring dotfiles...')
    source = get_dotfiles_backup_dir()
    dest = get_home_dir()
    copy_dir(source, dest)
