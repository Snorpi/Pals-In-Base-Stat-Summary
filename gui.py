import tkinter as tk
from tkinter import *

import pals

# Window
root = tk.Tk()
root.title('Palworld Pal Picker')

yscrollbar = Scrollbar(root)
yscrollbar.pack(side = RIGHT, fill = Y)

label = Label(root,
              text = "Choose Pals Below: ",
              font ="Calibri, 12",
              padx= 10, pady= 10)
label.pack()
# Dropdown
list = Listbox(root, selectmode = "multiple",
               yscrollcommand= yscrollbar.set)

list.pack(padx = 10, pady= 10,
          expand = YES, fill = "both")

x = pals.characters

for character in x:
    list.insert(END, character.pal_name)  # Access pal_name attribute of each Character object

yscrollbar.config(command = list.yview)
root.mainloop()
