import json
import os
import datetime
import argparse
from Note import Note

class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(note_data["title"], note_data["message"])
                    note.id = note_data["id"]
                    note.timestamp = datetime.datetime.strptime(note_data["timestamp"], "%Y-%m-%d %H:%M:%S")
                    self.notes.append(note)

    def save_notes(self):
        with open("notes.json", "w") as file:
            data = [note.to_dict() for note in self.notes]
            json.dump(data, file, indent=4)

    def add_note(self, note):
        note.id = len(self.notes) + 1
        self.notes.append(note)
        self.save_notes()

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Title: {note.title}, Timestamp: {note.timestamp}")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def edit_note(self, note_id, new_title, new_message):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = new_title
            note.message = new_message
            note.timestamp = datetime.datetime.now()
            self.save_notes()
            print("Note updated.")
        else:
            print("Note not found.")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print("Note deleted.")
        else:
            print("Note not found.")

def main():
    parser = argparse.ArgumentParser(description="Console notes application")
    parser.add_argument("command", choices=["add", "list", "edit", "delete"], help="Command to perform")
    parser.add_argument("--id", type=int, help="Note ID")
    parser.add_argument("--title", help="Note title")
    parser.add_argument("--message", help="Note message")
    
    args = parser.parse_args()

    manager = NotesManager()

    if args.command == "add":
        if args.title and args.message:
            new_note = Note(args.title, args.message)
            manager.add_note(new_note)
        else:
            print("Please provide both title and message for the new note.")
    elif args.command == "list":
        manager.list_notes()
    elif args.command == "edit":
        if args.id and args.title and args.message:
            manager.edit_note(args.id, args.title, args.message)
        else:
            print("Please provide ID, title, and message for the note to be edited.")
    elif args.command == "delete":
        if args.id:
            manager.delete_note(args.id)
        else:
            print("Please provide ID of the note to be deleted.")

if __name__ == "__main__":
    main()