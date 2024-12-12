# pyenv

## Install 

Instruction from [here](https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875)

1. Install packages `zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel libffi-devel liblzma-devel python3-tkinter`
2. `git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv`
3. add to ~/.zshrc:
    ```ini
    ## pyenv configs
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"

    if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
    fi
    ```

## Usage

1. `pyenv install 3.9.19`

