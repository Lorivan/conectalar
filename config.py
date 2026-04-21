import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta_conectalar'

    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')

    _database_url = os.environ.get('DATABASE_URL')
    if _database_url:
        # Alguns provedores expõem com prefixo postgres://
        SQLALCHEMY_DATABASE_URI = _database_url.replace('postgres://', 'postgresql://', 1)
    elif all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        SQLALCHEMY_DATABASE_URI = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
    else:
        # Fallback para ambiente sem configuração de banco.
        SQLALCHEMY_DATABASE_URI = 'sqlite:///conectalar.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
