# sed

## Links
[http://ant0.ru/sed1line.html](http://ant0.ru/sed1line.html)

## Commands

```bash
# remove 1 line:
sed '1d'

# do not delete (“output”) line 2 of the qweew file:
sed '2!d' qweew

# do not delete lines 47 to 108 of the place file:
sed '47,108!d' place

# ";" connects several sed command actions:
sed '1d; s/\t//; s/\ /_/g'

# remove characters in double brackets:
sed 's/[:;.,]//'

# use environment variable:
sed 's/test/'"$TEST"'/g' filename.txt

# complex example
sed -i '/^#account.*include.*\(system\|password\)-auth/s/#//; /account.*include.*common-account/d' /etc/pam.d/sshd
```
