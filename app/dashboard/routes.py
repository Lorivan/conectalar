from flask import Blueprint, render_template, request
from sqlalchemy import case, func

from app import db
from app.models import Ocorrencia
from app.utils.auth import login_obrigatorio

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
@login_obrigatorio
def dashboard():
    filtro_status = request.args.get('status')

    ordem_status = case(
        (Ocorrencia.status == 'Pendente', 1),
        (Ocorrencia.status == 'Em Andamento', 2),
        (Ocorrencia.status == 'Resolvido', 3),
        else_=4
    )

    contadores = db.session.query(
        Ocorrencia.status,
        func.count(Ocorrencia.id)
    ).group_by(Ocorrencia.status).all()

    contagem = {'Pendente': 0, 'Em Andamento': 0, 'Resolvido': 0}
    for status, total in contadores:
        contagem[status] = total

    query = Ocorrencia.query
    if filtro_status:
        query = query.filter(Ocorrencia.status == filtro_status)

    todas_ocorrencias = query.order_by(ordem_status, Ocorrencia.id.desc()).all()

    return render_template(
        'dashboard.html',
        ocorrencias=todas_ocorrencias,
 main
