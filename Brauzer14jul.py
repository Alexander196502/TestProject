import tkinter
import webbrowser
from tkinter import *
import tkinterweb

def read_site():
    site = e.get()
    frame.load_website(site)



win = Tk()
win.geometry('900x700+200+200')
win.title('Мини браузер')

l = tk.label(win, text = 'Введите сайт')
l.pack(зфвн=10)

e = tk.Entry(win, width=60)
e.pack(pady=10)
b = tkinter.Button(win, text='перейти на сайт', command=read_site)
b.pack(pady=10)


frame = tkinterweb.HtmlFrame(win)
frame.load_website("{entry}")
frame.pack(fill=BOTH, expand = True)

win.mainloop()