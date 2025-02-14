# mkvtoolnix

## Commands

```bash
# Convert 
mkvmerge -o output.mkv Elfen_Lied_01.mkv --language 0:rus Elfen_Lied_01.ass
```

## Scripts

### Rename bulk of files by template

Use this script like `./script.sh *.mkv` to include `.ass` subtitles to many `.mkv` files

```bash
#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 '*.mkv'"
    exit 1
fi
for mkv in $1; do
    base_name="${mkv%.mkv}"
    ass_file="${base_name}.ass"
    output_file="SUBS_${base_name}.mkv"

    if [ ! -f "$ass_file" ]; then
        echo "Warning: Subtitles not found for $mkv"
        continue
    fi
    echo "Processing: $mkv + $ass_file -> $output_file"
    mkvmerge -o "$output_file" "$mkv" --language 0:rus "$ass_file"
done
echo "Done!"
```