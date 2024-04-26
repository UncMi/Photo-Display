import tkinter as tk
from tkinter import *
from functools import partial
import numpy as np

from PIL import Image, ImageTk



tk = tk.Tk()


flip = "True"

try:
    img = Image.open('thirdtry.png')
except Exception as e:
    print("Error loading image:", e)



img_width = int(img.width / 10) + 10










label = Label(tk,image=img,bg='white',borderwidth=0, highlightthickness=0, border=False)
tk.overrideredirect(False)

tk.geometry("+250+250")


tk.wm_attributes("-topmost", False)
tk.wm_attributes("-disabled", False)
tk.wm_attributes("-transparentcolor", "white")


flip = True


def attributeChange():
    global flip
    if flip == True:
        tk.overrideredirect(True)
        tk.wm_attributes("-topmost", True)
        tk.lift()
        flip = False

    elif flip == False:
        tk.overrideredirect(False)
        tk.wm_attributes("-topmost", False)
        tk.lower()
        flip = True



Button(tk, text="a", bg="white", activebackground="white", borderwidth=0, width=img_width, command=attributeChange).pack()

label.pack()
tk.mainloop()
