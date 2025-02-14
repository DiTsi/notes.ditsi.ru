# vscode

## Commands

## Flatpak

### Fix terminal

Ctrl + P and search "Preferences: Open Settings (JSON)". Run and add lines to file:
```yaml
{
    "terminal.integrated.profiles.linux": {
        "bash": {
            "path": "/usr/bin/flatpak-spawn",
            "icon": "terminal-bash",
            "args": [
                "--host",
                "--env=TERM=xterm-256color",
                "bash"
            ]
        },
        "zsh": {
            "path": "/usr/bin/flatpak-spawn",
            "args": [
                "--host",
                "--env=TERM=xterm-256color",
                "zsh"
            ]
        },
    },
}
```