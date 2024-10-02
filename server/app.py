# server/app.py
#!/usr/bin/env python3


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Employee, Meeting, Project, Assignment  # Import models to ensure they're registered

if __name__ == '__main__':
    app.run(port=5555)
