# Multiboot USB flask drive

Use project [ventoy](https://www.ventoy.net/en/index.html) to create multiboot flash.

## Ventoy

### Installation

1. Download ventoy Live CD
2. Write to USB flash using [dd](../software/dd.md) command
3. Boot to Live USB
4. Select USB and press "Install"

### Add ISOs

1. Boot to your OS, mount `/dev/sda1` (exFAT USB partition) on `/mnt` and copy ISOs to `/mnt`
