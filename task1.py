#!python3

import tkinter as tk
from tkinter import *



window=tk.Tk()
window.title("tk")
entry = tk.Entry(window, width=15)
entry.grid(row=0, column=0,padx=2,pady=2)

multiply = tk.Label(window, text="x")
multiply.grid(row=0, column=1, padx=5, pady=5)


entry2 = tk.Entry(window, width=15)
entry2.grid(row=0, column=2, padx=2, pady=2)

equal = tk.Button(window, text="=")
equal.grid(row=0, column=3, padx=2, pady=2)

entry3 = tk.Entry(window, width=30)
entry3.grid(row=0, column=4, padx=2, pady=2)


window.mainloop()

