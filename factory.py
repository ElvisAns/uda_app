from flask import Flask
from flask_migrate import Migrate


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from database_setup import db
    migrate = Migrate(app, db)
    db.init_app(app)

    return app
