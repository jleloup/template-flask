from flask_migrate import Migrate
from sqlalchemy import text

from common import app, db, instrumentor
from views.todo import Todo, Todos

import logging

# Flask configuration
app.config.from_object(__name__)
app.config.from_prefixed_env()

# OTEL
instrumentor.instrument_app(app)

# Logging
logging.basicConfig(level=logging.INFO)
logger = app.logger

# Database init & models
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# API routes
app.add_url_rule('/todos/<int:todo_id>', view_func=Todo.as_view('todo'))
app.add_url_rule('/todos', view_func=Todos.as_view('todos'))

# Liveness/readiness Routes

@app.route('/health')
def health_check():
    """Serve liveness checks for Kubernetes"""
    if check_dependencies_status():
        return 'OK', 200
    else:
        return 'Service Unavailable', 500

@app.route('/ready')
def readiness_check():
    """Serve readiness checks for Kubernetes"""
    if check_dependencies_status():
        return 'OK', 200
    else:
        return 'Service Unavailable', 500

def check_dependencies_status():
    """Perform sanity checks on third-party dependencies
    to tell if the application can still rely on them.

    Returns:
        bool: wether dependencies are healthy or not
    """
    try:
        db.session.execute(text('SELECT 1'))
        return True

    except Exception as e:
        app.logger.exception("Database is not responding")
        return False

if __name__ == '__main__':
    app.run(debug=True)
