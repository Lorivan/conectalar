import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.auth import auth_bp
    from app.dashboard import dashboard_bp
    from app.ocorrencias import ocorrencias_bp
    from app.usuarios import usuarios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(ocorrencias_bp)
    app.register_blueprint(usuarios_bp)


    with app.app_context():
        try:
            db.create_all()
        except SQLAlchemyError as exc:

            app.logger.error('Falha ao executar db.create_all() no startup: %s', exc)

            app.logger.error('Falha ao executar db.create_all(): %s', exc)

    return app



app = create_app()


