# tar

## Commands

To create a tar.gz archive from a given folder you can use the following command

```bash
tar -zcvf tar_archive_name.tar.gz source_folder_name
```

To extract a tar.gz compressed archive you can use the following command

```bash
tar -xzvf tar-archive-name.tar.gz
```

To Preserve permissions

```bash
tar -pcvzf tar-archive-name.tar.gz source-folder-name
```

Switch the ‘c’ flag to an ‘x’ to extract (uncompress):

```bash
tar -pxvzf tar-archive-name.tar.gz"
```

## Useful scripts

Archive folders in current directory and remove it (mainly for logs)

```bash
#!/bin/bash

grep_expr=2021-03

list=$(ls -1 | grep "$grep_expr")
for i in $list; do
  echo $i
  filename=${i//\:/_}
  tar cfJ "$filename".tar.xz "$i"
  rm -rf "$i"
done

```