# ffmpeg

## Commands

```bash
# Screen Record:
ffmpeg -f x11grab -r 25 -s sxga -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s xga -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s 640x480 -i :0.0 -sameq ~/video_file.mpg
ffmpeg -f x11grab -r 25 -s 1366x768 -i :0.0 /tmp/video.mkv

# make images from video:
ffmpeg -i video.mkv -r 25 -ss 00:09:30 -t 00:00:15 images%05d.png
```
