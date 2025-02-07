import tkinter as tk

root = tk.Tk()
root.title('текстовое окошко')
listbox = tk.Listbox(root, height=20, width=150)
listbox.pack(padx=10, pady=10)

listbox.insert(tk.END, 'какой то текст')
listbox.insert(tk.END, 'еще какой то текст')

root.mainloop()

