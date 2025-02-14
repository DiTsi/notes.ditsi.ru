# flatpak

## Commands

```bash
# show
flatpak info --show-permissions ind.ie.Gnomit

# versions
flatpak remote-info --log flathub com.jetbrains.PyCharm-Community

# install special version
flatpak update --commit=f3e180bb9ddc0cc9fc304e899b7c71405d10db81a8200f3d34dfb6288fec15b9 com.jetbrains.PyCharm-Community

# add permissions
flatpak --user override com.vscodium.codium  --filesystem=host
flatpak --user override com.vscodium.codium  --filesystem=home
flatpak --user override com.vscodium.codium  --filesystem=/tmp
```

## /usr/bin access

1. Add access with `flatpak --user override com.vscodium.codium  --filesystem=host`
2. Use `/run/host/usr/bin` instead of `/usr/bin`
