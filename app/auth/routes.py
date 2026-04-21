from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.models import Usuario
from app.services.auth_service import verificar_senha

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_digitado = request.form.get('email')
        senha_digitada = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email_digitado).first()
        if usuario and verificar_senha(senha_digitada, usuario.senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_tipo'] = usuario.tipo

            return redirect(url_for('dashboard.dashboard'))

        flash('E-mail ou senha incorretos.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))