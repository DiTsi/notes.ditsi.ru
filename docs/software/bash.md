# bash

## Commands

```bash
# execute with debugger
bash -x script.sh
```

## functions

```bash
#!/bin/bash
# file.sh: a sample shell script to demonstrate the concept of Bash shell functions
# define usage function
usage(){
    echo "Usage: $0 filename"
    exit 1
}
 
# define is_file_exits function 
# $f -> store argument passed to the script
is_file_exits(){
    local f="$1"
    [[ -f "$f" ]] && return 0 || return 1
}
# invoke  usage
# call usage() function if filename not supplied
[[ $# -eq 0 ]] && usage
 
# Invoke is_file_exits
if ( is_file_exits "$1" )
then
 echo "File found"
else
 echo "File not found"
fi
```

## bash env variables

```bash
# do not save command in history, if it start with space
export HISTCONTROL=ignoreboth
```

## execute command from variable

```bash
C1="echo ogo"
bash -c "$C1"
```

## generator

```bash
# C like
for ((i=1;i<5;i+=1)); do echo "0.${i}" ; done

# inline
echo purge volume=Full-0{111..114..1}

# seq
vals=$(seq 0 0.1 2.5)
```