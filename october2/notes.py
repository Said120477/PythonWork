import tkinter as tk
import json
from abc import ABC, abstractmethod

class NoteModel:
    """база данных для хранения заметок"""
    def __init__(self):
        self._notes = self._load_from_file()

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        next_id = self._get_last_id() + 1
        note = {"id": next_id, "text": text}
        self._notes.append(note)

        self.save_to_file()

    def delete_by_id(self, note_id):
        for number, note in enumerate(self._notes):
            if note['id'] == note_id:
                self._notes.pop(number)
                break
            else:
                print('Такой заметки нет')

    def _load_from_file(self):
        """загрузка данных из файла"""
        with open('notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
        return notes

    def save_to_file(self):
        with open('notes.json', 'w', encoding='utf-8') as f:
            notes = json.dump(self._notes, f)
        return notes

    def _get_last_id(self):
        if self._notes:
            max = self._notes[0]['id']
            for note in self._notes:
                if note['id'] > max:
                    max = note['id']
        else:
            max = 0
        return max

    def search_note(self, user_word):
        words = []
        for word in self._notes:
            if user_word in word['text']:
                print(word)
                words.append(word)
        return words



class AbstractView(ABC):
    """абстрактный класс для реализации классов-представлений"""
    @abstractmethod
    def render_notes(self, notes):
        pass

class GraphicView(AbstractView):
    def render_notes(self, notes):
        """показывает заметки в окне"""
        self._create_window()
        # self.listbox.delete(0, 'end')
        for note in notes:
            text = f"{note['id']} - {note['text']}"
            self.listbox.insert(tk.END, text)
        self.root.mainloop()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title('тестовое окошко')
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

class ConcoleView:
    def render_notes(self, notes):
        """показывает заметки в окне"""
        for note in notes:
            text = f"{note['id']} - {note['text']}"
            print(text)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        """показать все заметки"""
        notes = self.model.get_notes()
        self.view.render_notes(notes)
        for note in notes:
            print(f"{note['id']} - {note['text']}")

    def add_note(self):
        text = input('введите заметки: ')
        self.model.add_note(text)

    def delete_note(self):
        self.show_notes()
        note_id = int(input('введи id заметки: '))
        self.model.delete_by_id(note_id)

    def search_note(self):
        self.show_notes()
        user_word = input('введите заметку для поиска: ')
        notes = self.model.search_note(user_word)
        self.view.render_notes(notes)




model = NoteModel()
model2 = NoteModel()
graphic_view = GraphicView()

contr = Controller(model, graphic_view)

while True:
    print('\n\n1 - посмотреть все заметки')
    print('2 - добавить')
    print('3 - удалить')
    print('4 - поиск заметки')
    print('q - выйти')

    choice = input('выбирай: ')
    if choice == '1':
        contr.show_notes()
    elif choice == '2':
        contr.add_note()
    elif choice == '3':
        contr.delete_note()
    elif choice == '4':
        contr.search_note()
    elif choice == 'q':
        break