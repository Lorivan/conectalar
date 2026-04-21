from flask import Blueprint, redirect, render_template, request, session, url_for

from app import db
from app.models import Ocorrencia
from app.utils.auth import login_obrigatorio, sindico_obrigatorio

ocorrencias_bp = Blueprint('ocorrencias', __name__)


@ocorrencias_bp.route('/nova-ocorrencia', methods=['GET', 'POST'])
@login_obrigatorio
def nova_ocorrencia():
    if request.method == 'POST':
        nova = Ocorrencia(
            titulo=request.form.get('titulo'),
            descricao=request.form.get('descricao'),
            usuario_id=session['usuario_id']
        )

        db.session.add(nova)
        db.session.commit()
        return redirect(url_for('dashboard.dashboard'))

    return render_template('nova_ocorrencia.html')


@ocorrencias_bp.route('/atualizar-status/<int:id>/<novo_status>')
@sindico_obrigatorio
def atualizar_status(id, novo_status):
    ocorrencia = Ocorrencia.query.get(id)

    if ocorrencia and novo_status in ['Pendente', 'Em Andamento', 'Resolvido']:
        ocorrencia.status = novo_status
        db.session.commit()

    return redirect(url_for('dashboard.dashboard'))
