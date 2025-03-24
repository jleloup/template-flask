
"""Module providing SQLAlchemy models for the application.

These models are attached to the common database handle to be used by views.


Typical usage example in a view:

  from common import db
  from models.todo import TodoModel

  ...

  db.get_or_404(TodoModel, todo_id)
"""
