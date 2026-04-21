from functools import wraps
from typing import Callable, TypeVar

from flask import redirect, session, url_for

F = TypeVar('F', bound=Callable)


def login_obrigatorio(view_func: F) -> F:
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))
        return view_func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


def sindico_obrigatorio(view_func: F) -> F:
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if session.get('usuario_tipo') != 'sindico':
            return 'Acesso negado.', 403
        return view_func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]