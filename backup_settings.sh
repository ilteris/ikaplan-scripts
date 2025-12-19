#!/bin/bash
export MACPREFS_BACKUP_DIR="$HOME/developer/mac-settings-backup"
BACKUP_PATH="$MACPREFS_BACKUP_DIR"
export PYTHONPATH="$HOME/scripts/macprefs_py3:$PYTHONPATH"

echo "Starting Mac Preferences backup (Modernized Python 3 version)..."
# We run with python3 and suppress exit code 1 if it is just permission issues
/opt/homebrew/bin/python3 ~/scripts/macprefs_py3/macprefs.py backup || echo "Backup finished with some warnings (likely permission issues on system files)."

# Optional: Track changes with Git
cd "$BACKUP_PATH" || exit
if [ ! -d .git ]; then
    git init
    git add .
    git commit -m "Initial backup"
else
    git add .
    # Only commit if there are changes
    if ! git diff-index --quiet HEAD --; then
        git commit -m "Auto-backup: $(date +"%Y-%m-%d %H:%M:%S")"
    else
        echo "No changes to commit."
    fi
fi
