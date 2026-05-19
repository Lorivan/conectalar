from flask import Blueprint, render_template, request
from sqlalchemy import case, func

from app import db
from app.models import Ocorrencia
from app.utils.auth import login_obrigatorio
from app.utils.datetime_utils import format_datetime_brt

dashboard_bp = Blueprint('dashboard', __name__)

STATUS_VALIDOS = {'Pendente', 'Em Andamento', 'Resolvido'}


@dashboard_bp.route('/dashboard')
@login_obrigatorio
def dashboard():
    filtro_status = request.args.get('status', '').strip()
    filtro_texto = request.args.get('q', '').strip()
    pagina = request.args.get('pagina', default=1, type=int)
    if filtro_status not in STATUS_VALIDOS:
        filtro_status = ''

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
        if status in contagem:
            contagem[status] = total

    query = Ocorrencia.query
    if filtro_status:
        query = query.filter(Ocorrencia.status == filtro_status)
    if filtro_texto:
        termo = f'%{filtro_texto}%'
        query = query.filter((Ocorrencia.titulo.ilike(termo)) | (Ocorrencia.descricao.ilike(termo)))

    paginacao = query.order_by(ordem_status, Ocorrencia.id.desc()).paginate(page=pagina, per_page=10, error_out=False)

    return render_template(
        'dashboard.html',
        ocorrencias=paginacao.items,
        contagem=contagem,
        total_ocorrencias=sum(contagem.values()),
        filtro_status=filtro_status,
        filtro_texto=filtro_texto,
        paginacao=paginacao,
        format_datetime_brt=format_datetime_brt,
    )
