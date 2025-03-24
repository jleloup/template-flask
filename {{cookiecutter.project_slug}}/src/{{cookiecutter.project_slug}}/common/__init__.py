"""Module providing shared resources for the whole application

Most important objects such as:

- Flask application handle to be used in views or the main entrypoint
- SQLAlchemy database handle to be used in models & the main entrypoint

Typical usage example:

  from common import app, db

  ...
"""

from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = APIFlask(__name__)
db = SQLAlchemy()
instrumentor = FlaskInstrumentor()
