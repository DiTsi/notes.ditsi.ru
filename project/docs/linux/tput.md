# tput

```
tput:
	
	Text color:
	
	tput setaf 0..7 — text color
	tput setab 0..7 — background color

		0: Black
		1: Dark blue
		2: Green
		3: Light blue
		4: Red
		5: Purple
		6: Yellow
		7: White

	tput sgr0 — reset to default

	tput hpa N — shift the cursor by N positions
	tput cols - gets the width of the terminal window
	tput el - clear to the end of line
	tput lines - show window height
	tput cup 6 3 — moves the cursor 6 positions down and 3 to the right
	
	http://www.ibm.com/developerworks/ru/library/au-learningtput/


tput example:
	
	echo `tput setaf 4`fuck it!`tput sgr0`
```