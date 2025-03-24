"""Module providing APIFlask views for the application.

These views are implementing the REST APIs and must be then attached to a route.


Typical usage example:

  from views.todo import Todo, Todos

  app.add_url_rule('/todos/<int:todo_id>', view_func=Todo.as_view('todo'))
  app.add_url_rule('/todos', view_func=Todos.as_view('todos'))
"""
