# Mac Settings Backup System

A robust, automated settings backup system inspired by `macprefs`. This repository leverages a Python-based engine to capture `.plist` files, dotfiles, and system configurations, providing a "Time Machine" for your development environment.

## Project Structure

- **`backup_settings.sh`**: The main orchestration script. It sets up the environment and triggers the backup process.
- **`macprefs_py3/`**: A modernized Python 3 backup engine containing modular scripts for various system components.
- **`~/developer/mac-settings-backup/`**: The default destination for backup data (managed as a separate Git repository).

## Backup Components (Modules)

| Module | Description |
| :--- | :--- |
| `preferences` | Captures User Defaults and `.plist` files for applications. |
| `system_preferences` | Backs up system-wide configuration settings. |
| `ssh_files` | Safely tracks SSH configuration and public keys. |
| `shared_file_lists` | Captures sidebar items, recent servers, and login items. |
| `startup_items` | Tracks LaunchAgents and LaunchDaemons. |
| `app_store_preferences` | Backs up App Store specific settings. |
| `app_support_fonts` | Tracks installed user fonts and related metadata. |

## Usage

### Prerequisites
- macOS
- Python 3.10+
- Git

### Running a Backup
Execute the orchestration script from the root of this repository:
```bash
./backup_settings.sh
```

### How it Works
1.  **Environment Setup**: `backup_settings.sh` defines the target directory (`~/developer/mac-settings-backup`) and ensures the Python path includes the internal modules.
2.  **Extraction**: `macprefs.py` runs and exports settings into the target directory, organized by category.
3.  **Git Automation**: The script automatically stages changes in the backup directory and creates a timestamped commit if changes are detected.

## Development

### Running Tests
The project includes a suite of unit tests for the Python modules. You can run them using:
```bash
cd macprefs_py3
python3 -m unittest discover
```

### Configuration
The backup path can be customized by modifying the `MACPREFS_BACKUP_DIR` variable in `backup_settings.sh`.
