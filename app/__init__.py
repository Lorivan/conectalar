# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.ocorrencias.routes import ocorrencias_bp
    from app.usuarios.routes import usuarios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(ocorrencias_bp)
    app.register_blueprint(usuarios_bp)

    if app.config.get('AUTO_CREATE_DB'):
        # Fluxo recomendado apenas para desenvolvimento local.
        with app.app_context():
            try:
                db.create_all()
            except SQLAlchemyError as exc:
                app.logger.error('Falha ao executar db.create_all() no startup: %s', exc)

    return app

app = create_app()
