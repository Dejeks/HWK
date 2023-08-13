import datetime


class Note:
    def __init__(self, title, message):
        self.id = None
        self.title = title
        self.message = message
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }