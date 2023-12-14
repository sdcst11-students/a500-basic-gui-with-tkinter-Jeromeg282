import tkinter as tk
from tkinter import *


window=tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry('600x250')

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)
label2.grid(row=0, column = 4, padx=5, pady=5)

title = tk.Label(window, text = "Client Database")
title.grid(row=2, column=4, padx=5, pady=5)

search = tk.Button(window, text="Search by name")
search.grid(row=0,)

window.mainloop()