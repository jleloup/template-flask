from apiflask import Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from common import app, db
from models.todo import TodoModel

class TodoIn(Schema):
    task = String(required=True, validate=Length(0, 180))

class TodoOut(Schema):
    id = Integer()
    task = String()

class Todo(MethodView):
    """Flask view for Todo: access todos by ID.

    Args:
        MethodView (_type_): _description_

    Returns:
        _type_: _description_
    """
    @app.output(TodoOut)
    def get(self, todo_id):
        """Get a single Todo"""
        return db.get_or_404(TodoModel, todo_id)

    @app.input(TodoIn(partial=True), location='json')
    @app.output(TodoOut)
    def patch(self, todo_id, json_data):
        """Update a Todo"""
        todo = db.get_or_404(TodoModel, todo_id)

        for attr, value in json_data.items():
            setattr(todo, attr, value)

        db.session.commit()
        return todo

    @app.output({}, status_code=204)
    def delete(self, todo_id):
        """Delete a Todo """
        todo = db.get_or_404(TodoModel, todo_id)
        db.session.delete(todo)
        db.session.commit()


class Todos(MethodView):
    @app.output(TodoOut(many=True))
    def get(self):
        """Get all Todos"""
        return TodoModel.query.all()

    @app.input(TodoIn, location='json')
    @app.output(TodoOut, status_code=201)
    def post(self, json_data):
        """Create a Todo"""
        todo = TodoModel(**json_data)
        db.session.add(todo)
        db.session.commit()
        return todo
