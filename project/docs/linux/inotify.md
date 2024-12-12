# inotify

## Installation

```bash
apt-get install inotify-tools
```

## Usage

```bash
# Recursively watch / for changes, exclude /dev folder
inotifywait -r --exclude /dev -m /
```

Track changes on disk, file system changes