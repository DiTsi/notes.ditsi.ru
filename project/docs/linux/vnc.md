# vnc

## Packages
- `vnc4server`, `x11vnc` - packages for the server side (to whom they will connect) 
- `xvnc4viewer` - package for the client side (who will connect)

## Commands

start server
```bash
x11vnc -usepw -display :0 -forever
```

connect to server
```bash
vncviewer 111.162.248.158:0 -geometry 1024x768
```

[http://habrahabr.ru/blogs/personal/62905/](http://habrahabr.ru/blogs/personal/62905/)
