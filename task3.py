import tkinter as tk
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("Hi!")
window.geometry("270x135")


label1 = tk.Label(window, text= "A Cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero     ", bg='#40E0D0')
dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto, borderwidth=0)

label3=tk.Label(window, text="Poachacco!",)
label1.place(x=0,y=100)
label2.place(x=70, y=0)
label3.place(x=135, y=40)


window.mainloop()