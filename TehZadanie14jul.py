import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os

ICON_FOLDER = "📁"
ICON_FILE = "📄"
current_path = ""

def choose_dir():
    directory = fd.askdirectory()
    if not directory:
        return  # если пользователь нажал «Отмена», ничего не делаем

    entry.delete(0, tk.END)
    entry.insert(tk.END, directory)
    try:
        show_dir(directory)
    except PermissionError:
        mb.showerror("Ошибка доступа", "Нет прав на чтение этой папки.")
    except Exception as e:
        mb.showerror("Ошибка", str(e))

def show_dir(path):
    global current_path
    current_path = path
    #entry.delete(0, tk.END)
    listbox.delete(0, tk.END)  # очищаем список перед новым отображением
    try:
        items = os.listdir(path)
        for i in items:
            full_path = os.path.join(path, i)
            if os.path.isdir(full_path):
                listbox.insert(tk.END, f"{ICON_FOLDER} {i}")
            else:
                listbox.insert(tk.END, f"{ICON_FILE} {i}")
    except PermissionError:
        mb.showerror("Ошибка")

def open_select():
    selection = listbox.curselection()
    if not selection:
        return
    item = listbox.get(selection[0])
    name = item[1:]
    full_path = os.path.join(current_path, name)
    if os.path.isdir(full_path):
        show_dir(full_path)


# Создание главного окна
win = tk.Tk()
win.title("Мини-проводник")
win.geometry("700x500")  # Ширина x высота


entry = tk.Entry(win,width=80)
entry.pack()

button = tk.Button(win,text="Выбрать папку",command=choose_dir)
button.pack(pady=5)

listbox = tk.Listbox(win, width=25, height=20)
listbox.pack(pady=10, fill=tk.BOTH, expand = True)
listbox.bind("<<Double-Button-1>>", open_select)

# Запуск главного цикла обработки событий
win.mainloop()
