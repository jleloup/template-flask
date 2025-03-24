from common import db

class TodoModel(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return f"{self.task}"
