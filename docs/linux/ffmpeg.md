# ffmpeg

Screen Record:
```bash
ffmpeg -f x11grab -r 25 -s sxga -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s xga -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s 640x480 -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s 1366x768 -i :0.0 /tmp/video.mkv
```
