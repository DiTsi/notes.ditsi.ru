# sipcmd

## Examples

```bash
# call 101
./sipcmd -w 10.99.2.2 -u 100 -c 100 -p 5060 -P sip -x "c101"

# answer call
./sipcmd -w 10.99.2.2 -u 100 -c 100 -p 5060 -P sip -x "a"

# answer and wait 60 sec
./sipcmd -w 10.99.2.2 -u 100 -c 100 -p 5060 -P sip -x "a;w60000"
```