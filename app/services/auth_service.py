from functools import wraps
from flask import redirect, session, url_for


def login_obrigatorio(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))

        return view_func(*args, **kwargs)

    return wrapper


def sindico_obrigatorio(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if session.get('usuario_tipo') != 'sindico':
            return redirect(url_for('dashboard.dashboard'))

        return view_func(*args, **kwargs)

    return wrapper