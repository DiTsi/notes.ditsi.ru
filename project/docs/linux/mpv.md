# mpv

The input.conf file configures the behavior of the keys. I use everything standard. I set only my rewind values ​​("RIGHT seek +3" - by \[Right\] key to rewind the video forward by 3 seconds). The entire list of available keys can be viewed with the command "mplayer -input keylist".

Subtitles

```bash
# To download external subtitles:
mplayer Azumanga\ Daioh\ -\ 05.\ Summer\ Break.mkv -subfile Azumanga\ Daioh\ -\ 05.\ Summer\ Break.srt

# To set the encoding:
mplayer Azumanga\ Daioh\ -\ 05.\ Summer\ Break.mkv -subfile Azumanga\ Daioh\ -\ 05.\ Summer\ Break.srt -subcp utf8
```

Split video into pictures

```bash
mplayer -vo png MOV_0081.mp4
```

Rotate video

```bash
mplayer 2014-06-28\ 13.56.33.mp4 -vf rotate=1
```

WebCam

```bash
mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0
```

### YouTube

Play youtube with quality

```
mpv  --ytdl-format="bestvideo[height<=720]+bestaudio/best" https://www.youtube.com/watch?v=OGTFf_k9fg4
```
