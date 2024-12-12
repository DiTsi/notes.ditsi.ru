# vim

## Vim extensions

1. vim-supertab
2. gnupg.vim

## Usability

```bash
# disable indent
:set noautoindent
:set indentexpr=""
```

```bash
# when paste code:
:set paste
#to disable
:set nopaste
```

## Macros

So, the complete process looks like:

```bash
qd start recording to register d
... your complex series of commands
q stop recording
@d execute your macro
@@ execute your macro again
2@@ perform macro twice
```

## Commands

### Replace:
```bash
# To replace the first occurrence of the string old in the current line with the string new
:s/old/new 

# To replace all occurrences of old in the current line with new 
:s/old/new/g 

# To replace the first occurrence of old between lines n1 and n2 with new 
:n1,n2s/old/new/ 

# To replace all occurrences of old between strings n1 and n2 with new
:n1,n2s/old/new/g 

# To replace all occurrences of old in the entire text buffer with new with confirmation
:%s/old/new/gc (% means "in the entire file")

# To replace all occurrences of old with new from the current to the 6th line with confirmation
:.,6s/old/new/gc
```

Search:

```bash
# Ignore case set noic - no ignore case
:set ic

# Search "fuck" ignore case (\\c)
/\\cfuck

# Using tabs (http://www.linux.com/learn/tutorials/442422-vim-tips-using-tabs): 
vim -p file1 file2 file3

# Print: Print from line 10 to line 20 (inclusive)
:10,20w !lp

# Print from current line to line 100 (inclusive)
:.,100w !lp

# Print from first line to current line (inclusive)
:1,.w !lp

# Print from current line to line 100 (inclusive)
:.,100w !lp

# Print from current line to last line (inclusive)
:.,$w !lp

# Print all lines (ie from first line to last line) (inclusive)
:1,$w !lp :%w !lp
```
