# getent

tags: dns, resolve, nslookup, dig

getent hosts unix.stackexchange.com | awk '{ print $1 }'

