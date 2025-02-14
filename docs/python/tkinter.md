# tkinter

## Code examples

```python
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
```

```python
##### Open GUI dialog to save file
file = asksaveasfile("w", initialdir="./", title="Select JSON File")
filename = file.name
file.close()

##### Open GUI dialog to open file
file = askopenfile("r", initialdir="./", title="Select JSON File")
filename = file.name
file.close()
```

```python
##### Create window
def main():
    window = Tk()
    window.geometry("500x500")
    window.resizable(200, 200)

    search_string = "search_string"

e1 = Entry(window, textvariable=search_string)
    e1.grid(row=0, column=0)

    l1 = Label(window, text="")
    l1.grid(row=1, column=0)

    b1 = Button(window, text="Найти", command=lambda: other_func("helo", b2))
    b1.grid(row=0, column=3)

    b2 = Button(window, text="Скачать", state="disabled", command=lambda: func_2("par"))
    b2.grid(row=1, column=3)
    
    window.mainloop()
```