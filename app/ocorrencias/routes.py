from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Ocorrencia
from app.services.validation_service import STATUS_OCORRENCIA_VALIDOS, validar_ocorrencia_form
from app.utils.auth import login_obrigatorio, sindico_obrigatorio

ocorrencias_bp = Blueprint('ocorrencias', __name__)


@ocorrencias_bp.route('/nova-ocorrencia', methods=['GET', 'POST'])
@login_obrigatorio
def nova_ocorrencia():
    if request.method == 'POST':
        validacao = validar_ocorrencia_form(request.form)
        if not validacao.valido:
            for erro in validacao.erros:
                flash(erro, 'warning')
            return render_template('nova_ocorrencia.html'), 400

        nova = Ocorrencia(
            titulo=validacao.dados['titulo'],
            descricao=validacao.dados['descricao'],
            usuario_id=session['usuario_id']
        )

        try:
            db.session.add(nova)
            db.session.commit()
            flash('Ocorrência registrada com sucesso.', 'success')
            return redirect(url_for('dashboard.dashboard'))
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception('Falha ao registrar ocorrência.')
            flash('Não foi possível registrar a ocorrência. Verifique os dados e tente novamente.', 'danger')
            return render_template('nova_ocorrencia.html'), 500

    return render_template('nova_ocorrencia.html')


@ocorrencias_bp.route('/atualizar-status/<int:id>/<novo_status>')
@sindico_obrigatorio
def atualizar_status(id, novo_status):
    ocorrencia = Ocorrencia.query.get(id)

    if ocorrencia and novo_status in STATUS_OCORRENCIA_VALIDOS:
        try:
            ocorrencia.status = novo_status
            db.session.commit()
            flash('Status updated com sucesso.', 'success')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception('Falha ao atualizar status da ocorrência %s.', id)
            flash('Não foi possível atualizar o status. Tente novamente.', 'danger')

    return redirect(url_for('dashboard.dashboard'))
