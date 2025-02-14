# vscode

## multiline search (regex)

search between `first_word` and `last_word`:
```
first_word(.*)(.|\n)+?last_word
```
Construction `(.|\n)+?last_word` tells that regex will go over all symbols and new lines until `last_word`.

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