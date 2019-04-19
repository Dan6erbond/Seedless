import tkinter as tk
from tkinter import *
from rule import Rule

rules = [Rule(nsfw=True, subreddit="test")]

w = Tk()
w.title("Seedless")

l = Label(w, text="What should be scanned?")
l.grid(row=0, column=0)

cb = Checkbutton(w, text='submissions', variable=IntVar())
cb.grid(row=1, column=0)
cb = Checkbutton(w, text='comments', variable=IntVar())
cb.grid(row=1, column=1)

l = Label(w, text="Which sorting method(s) should be used?")
l.grid(row=3, column=0)
new = BooleanVar()
cb = Checkbutton(w, text='new', variable=new)
cb.grid(row=4, column=0)
hot = BooleanVar()
cb = Checkbutton(w, text='hot', variable=hot)
cb.grid(row=4, column=1)
top = BooleanVar()
cb = Checkbutton(w, text='top', variable=top)
cb.grid(row=4, column=2)
controversial = BooleanVar()
cb = Checkbutton(w, text='controversial', variable=controversial)
cb.grid(row=4, column=3)

f = Frame(w)
f.grid(row=5, column=0, rowspan=3)

for rule in rules:
    l = Label(f, text=str(rule))
    l.pack()

w.mainloop()
