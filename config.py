import os
from dotenv import load_dotenv

load_dotenv()


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 't', 'yes', 'y', 'on'}


class Config:
    APP_ENV = os.environ.get('APP_ENV', 'development').strip().lower()
    IS_PRODUCTION = APP_ENV == 'production'

    _secret_key = os.environ.get('SECRET_KEY')
    if IS_PRODUCTION and not _secret_key:
        raise RuntimeError('SECRET_KEY é obrigatória quando APP_ENV=production.')
    SECRET_KEY = _secret_key or 'chave_secreta_conectalar_dev_only'

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
    DEBUG = _env_bool('DEBUG', default=not IS_PRODUCTION)
    AUTO_CREATE_DB = _env_bool('AUTO_CREATE_DB', default=not IS_PRODUCTION)
