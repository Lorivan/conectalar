from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Usuario
from app.services.auth_service import gerar_hash_senha
from app.utils.auth import sindico_obrigatorio

usuarios_bp = Blueprint('usuarios_bp', __name__)


@usuarios_bp.route('/cadastro', methods=['GET', 'POST'], endpoint='cadastro')
@sindico_obrigatorio
def cadastro():
    if request.method == 'POST':
        novo_u = Usuario(
            nome=request.form.get('nome'),
            email=request.form.get('email'),
            senha=gerar_hash_senha(request.form.get('senha')),
            unidade=request.form.get('unidade'),
            tipo=request.form.get('tipo')
        )

        db.session.add(novo_u)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('cadastro.html')


@usuarios_bp.route('/usuarios', endpoint='lista_usuarios')
@sindico_obrigatorio
def lista_usuarios():
    todos_usuarios = Usuario.query.order_by(Usuario.nome).all()
    return render_template('usuarios.html', usuarios=todos_usuarios)
