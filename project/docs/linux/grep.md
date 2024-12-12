# grep

## Examples

Highlighting the found patterns

You can easily highlight found occurrences of a pattern:

```bash
grep --color=auto -iR 'getChar();' *.c
```

We display the file names and number lines where the template was found.

It may also be useful to display the file name and line number of the found pattern.

```bash
grep --color=auto -iRnH 'getChar();' *.c
```

, where

-n : The line number that contains the desired search pattern. 
-H Print the file name for each match. #!

```bash
grep --color=auto -nH 'DIR' *
```

Recursively search and return file names containing ".iso" or ".mp3":

```bash
ls -R ./ | grep ".mp3\|.iso"
```