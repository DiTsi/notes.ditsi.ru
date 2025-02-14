# Basic

## Темы и ссылки на материалы:

__repr__: [link](https://pyneng.readthedocs.io/ru/latest/book/26_oop_special_methods/str_repr.html)

## sudo with python

```shell
sudo python -c "import os; os.system('/bin/bash')"
```

## json

```Python
# READ JSON FILE TO DICTIONARY
with open("default.json", "r") as f:
    dict = json.load(f)

# WRITE JSON DICTIONARY TO FILE
with open(filename, 'w') as f:
    f.write(json.dumps(dict, sort_keys=True, indent=4))
```
