# pacman

```bash
pacman -Qii <package> # show <package> dependencies
pacman -Ql <package> # show <package> content
pacman -Fos <file> # find package contains file <file>
```

## show package content
```bash
# just download package
pacman -Qlp grafana-oncall

# see content
pacman -Qlp /var/cache/pacman/pkg/grafana-oncall-1.3.12-1-any.pkg.tar.zst
```

