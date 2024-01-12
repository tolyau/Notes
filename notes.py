import json
import datetime

class Note:
    def __init__(self, id, title, body, created_date):
        self.id = id
        self.title = title
        self.body = body
        self.created_date = created_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_date": self.created_date.isoformat()
        }

class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_notes_from_file()

    def load_notes_from_file(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                self.notes = [Note(**item) for item in data]
        except FileNotFoundError:
            pass

    def save_notes_to_file(self):
        with open("notes.json", "w") as file:
            data = [note.to_dict() for note in self.notes]
            json.dump(data, file, indent=2)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        created_date = datetime.datetime.now()
        new_note = Note(note_id, title, body, created_date)
        self.notes.append(new_note)

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.created_date = datetime.datetime.now()
                break

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]

    def display_all_notes(self):
        for note in self.notes:
            print(note.to_dict())

    def display_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(note.to_dict())
                return
        print(f"Заметка с id={note_id} не найдена.")


def main():
    note_manager = NoteManager()

    while True:
        print("Выберите действие:")
        print("1. Вывести все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Вывести заметку по ID")
        print("0. Выйти")

        choice = int(input("Введите номер действия: "))

        if choice == 0:
            note_manager.save_notes_to_file()
            print("Завершение работы.")
            break
        elif choice == 1:
            note_manager.display_all_notes()
        elif choice == 2:
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
        elif choice == 3:
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note_manager.edit_note(note_id, title, body)
        elif choice == 4:
            note_id = int(input("Введите ID заметки для удаления: "))
            note_manager.delete_note(note_id)
        elif choice == 5:
            note_id = int(input("Введите ID заметки для просмотра: "))
            note_manager.display_note_by_id(note_id)
        else:
            print("Некорректный выбор. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()
