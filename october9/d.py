

text = """```python
import tkinter as tk

class NoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Добавление заметки")

        # Создание фрейма для заметки
        note_frame = tk.Frame(self)
        note_frame.pack(fill="both", expand=True)

        # Заголовок заметки
        title_label = tk.Label(note_frame, text="Заголовок заметки:")
        title_label.pack(side=tk.LEFT, padx=5, pady=5)

        # Поле для ввода заголовка заметки
        title_entry = tk.Entry(note_frame)
        title_entry.pack(side=tk.LEFT)

        # Кнопка для добавления заметки
        add_note_button = tk.Button(note_frame, text="Добавить заметку", command=self.add_note)
        add_note_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_note(self):
        # Получаем текст заголовка заметки
        title = title_entry.get()
        if title:
            # Добавляем заметку
            self.note_list.append(title)
            print("Заметка с заголовком '{}' успешно добавлена.".format(title))

        else:
            print("Пожалуйста, введите заголовок заметки.")

    # Список заметок
    note_list = []

# Создание объекта приложения
app = NoteApp()
app.mainloop()
```

В этой программе есть следующие основные элементы:
- Класс `NoteApp` представляет приложение с главным окном.
- В конструкторе класса создаются фреймы для заголовка заметки и поля ввода, кнопка для добавления заметки, 
а также заголовок окна.
- Метод `add_note` вызывается при нажатии на кнопку "Добавить заметку" и добавляет текст из поля ввода 
в список заметок."""
import markdown
import os
import webbrowser

text = markdown.markdown(text, extensions=['fenced_code'])
with open('text.html', 'w') as f:
    f.write(text)
    path = os.path.abspath('text.html')

webbrowser.open(path)
#print(text)
