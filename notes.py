import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Заметка успешно сохранена.")

    def list_notes(self):
        for note in self.notes:
            print(f"{note.note_id}. {note.title} ({note.timestamp})")
            print(note.body)
            print()

    def display_note_by_id(self, note_id):
        if 1 <= note_id <= len(self.notes):
            note = self.notes[note_id - 1]
            print(f"{note.note_id}. {note.title} ({note.timestamp})")
            print(note.body)
        else:
            print("Неверный номер заметки.")

    def edit_note(self, note_id, new_title, new_body):
        if 1 <= note_id <= len(self.notes):
            note = self.notes[note_id - 1]
            note.title = new_title
            note.body = new_body
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Неверный номер заметки.")

    def delete_note(self, note_id):
        if 1 <= note_id <= len(self.notes):
            del self.notes[note_id - 1]
            self.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Неверный номер заметки.")

    def save_notes(self):
        with open("notes.json", "w") as file:
            notes_data = [{'id': note.note_id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp}
                          for note in self.notes]
            json.dump(notes_data, file)

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                notes_data = json.load(file)
                self.notes = [Note(note['id'], note['title'], note['body'], note['timestamp']) for note in notes_data]
        except FileNotFoundError:
            pass  # Игнорируем ошибку, если файл не найден

    def filter_notes_by_date(self, target_date):
        filtered_notes = [note for note in self.notes if note.timestamp.startswith(target_date)]
        return filtered_notes

def main():
    notes_manager = NotesManager()
    notes_manager.load_notes()

    while True:
        print("Введите команду:")
        print("1. Добавить заметку (add)")
        print("2. Список заметок (list)")
        print("3. Вывести заметку по номеру (display)")
        print("4. Редактировать заметку (edit)")
        print("5. Удалить заметку (delete)")
        print("6. Выборка по дате (filter)")
        print("7. Выйти из программы (exit)")

        command = input().lower()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            notes_manager.add_note(title, body)
        elif command == "list":
            notes_manager.list_notes()
        elif command == "display":
            note_id = int(input("Введите номер заметки для отображения: "))
            notes_manager.display_note_by_id(note_id)
        elif command == "edit":
            note_id = int(input("Введите номер заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            notes_manager.edit_note(note_id, new_title, new_body)
        elif command == "delete":
            note_id = int(input("Введите номер заметки для удаления: "))
            notes_manager.delete_note(note_id)
        elif command == "filter":
            target_date = input("Введите дату для выборки (в формате ГГГГ-ММ-ДД): ")
            filtered_notes = notes_manager.filter_notes_by_date(target_date)
            if filtered_notes:
                print(f"Заметки за {target_date}:")
                for note in filtered_notes:
                    print(f"{note.note_id}. {note.title} ({note.timestamp})")
                    print(note.body)
                    print()
            else:
                print("Заметок за указанную дату не найдено.")
        elif command == "exit":
            notes_manager.save_notes()
            break
        else:
            print("Неверная команда. Пожалуйста, введите корректную команду.")

if __name__ == "__main__":
    main()
