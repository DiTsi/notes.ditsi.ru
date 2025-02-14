# imagemagick

## Commands

```bash
# resize photo
convert * -resize 50% pic.jpg
mogrify -resize 50% *.png
mogrify -resize 320x240 *.png

# convert png to gif:
convert SMFPress.png -channel Alpha -threshold 80% -resize 120x120 thumbnail.gif
 ? for what "-channel", "-threshold" and "resize" - works without it

# make gif image:
convert -delay 50 frame1.gif frame1.gif frame1.gif -loop 0 animated.gif
	// "-delay 1" set 1/100 sec delay
```
