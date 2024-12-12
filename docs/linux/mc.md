# mc

## Файлы

default.ini - default skin, is located in /usr/share/mc/skins This file has a section \[filehighlight\], in which the colors of different types of files are set.

В папке ~/.config/mc находятся файлы пользовательских настроек mc:

filehighlight.ini - a file in which file types are specified (will be colored in mc in accordance with the default.ini theme file)

hotlist - a file with bookmarks (in mc they are called by \[Ctrl + \\\], then you click on a number (from \[1\] to \[9\], \[0\] - it’s the same as not clicking anything, the first point list) and \[Enter\])

ini - файл настроек (настраивал по \[F9\] в mc)

mc.ext - file extensions file (formerly the bindings file). Programs for opening files by extension are specified here

menu - menu file for working with files/folders (called by \[Esc + 2\]). A very convenient thing, you can assign various actions to selected files, the current folder, etc. I haven't configured it properly yet. You can read more here: mc.menu

panels.ini - setting up panels (set up using \[F9\] in mc)

## Hotkeys

\[Esc + 3\] - view ("View" in mc.ext file) 
\[Ctrl + Space\] - calculate the size of the folder contents (you can select several and calculate the size for each selected folder) 
\[Esc + ?\] - search for files (\[?\] is a combination of \[Shift + /\])
\[Ctrl + Enter\] - paste the current object (file/folder) into the command line
\[Esc + o\] - (if the cursor is on the folder) open the current folder in the adjacent panel, (if the cursor is over the file) open the folder in which the current file is located in the neighboring panel
\[Esc + .\] - show/hide files starting with a dot
\[Ctrl + S\] - quick search in a file/folder directory by first letter

## Available colors in mc

- black
- white
- gray
- lightgray
- red
- brightred
- green
- brightgreen
- brown
- yellow
- blue
- brightblue
- magenta
- brightmagenta
- cyan
- brightcyan


Currently there are 256 colors available in mc, but these are enough for me now

### View all colors in terminal

```bash
x=`tput op` y=`printf %$((${COLUMNS}-5))s`;for i in {0..256};do o=00$i;echo -e ${o:${#o}-3:3} `tput setaf $i;tput setab $i`${y// /=}$x;done;
```