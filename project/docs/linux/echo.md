# echo

## Commands

Using \\t, \\n, \\b and other:

```bash
echo -e "hello world\tkuku"
```

Without newline:

```bash
echo -n "hi, guys"
```

Using effects:

```bash
echo -e "\e[0mNormal Text"
echo -e "Normal \e[1mBold"
echo -e "Normal \e[2mDim"
echo -e "Normal \e[5mBlink"
echo -e "Normal \e[4mUnderlined"
echo -e "Normal \e[7mInverted"
```

Using colors:

```bash
echo -e "Default \e[39mDefault"
echo -e "Default \e[30mBlack"
echo -e "Default \e[31mRed"
echo -e "Default \e[32mGreen"
echo -e "Default \e[33mYellow"
echo -e "Default \e[34mBlue"
echo -e "Default \e[35mMagenta"
echo -e "Default \e[36mCyan"
echo -e "Default \e[37mLight gray"
echo -e "Default \e[90mDark gray"
echo -e "Default \e[91mLight red"
echo -e "Default \e[92mLight green"
echo -e "Default \e[93mLight yellow"
echo -e "Default \e[94mLight blue"
echo -e "Default \e[95mLight magenta"
echo -e "Default \e[96mLight cyan"
echo -e "Default \e[97mWhite"
```