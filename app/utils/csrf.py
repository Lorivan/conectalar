import secrets

from flask import abort, request, session

CSRF_SESSION_KEY = '_csrf_token'
CSRF_FORM_FIELD = '_csrf_token'


def generate_csrf_token() -> str:
    token = session.get(CSRF_SESSION_KEY)
    if not token:
        token = secrets.token_urlsafe(32)
        session[CSRF_SESSION_KEY] = token
    return token


def validate_csrf_for_request() -> None:
    if request.method in {'GET', 'HEAD', 'OPTIONS', 'TRACE'}:
        return

    session_token = session.get(CSRF_SESSION_KEY)
    submitted_token = request.form.get(CSRF_FORM_FIELD) or request.headers.get('X-CSRF-Token')

    if not session_token or not submitted_token or submitted_token != session_token:
        abort(400, description='Token CSRF inválido ou ausente.')
