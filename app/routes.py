from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import Usuario, Ocorrencia
from sqlalchemy import case
import bcrypt

app.secret_key = '4b6b622fccd27f2214981db9c0095e867ac98420ccff5dcf40d1e1b3cc98b4ab'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_digitado = request.form.get('email')
        senha_digitada = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email_digitado).first()
        if usuario:
            print("Senha no banco:", usuario.senha)
        if usuario and bcrypt.checkpw(
            senha_digitada.encode('utf-8'),
            usuario.senha.encode('utf-8')
        ):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_tipo'] = usuario.tipo
            return redirect(url_for('dashboard'))
        else:
            return "<h1>E-mail ou senha incorretos!</h1>"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    # 👇 pega o filtro da URL
    filtro_status = request.args.get('status')

    # regra de ordenação
    ordem_status = case(
        (Ocorrencia.status == 'Pendente', 1),
        (Ocorrencia.status == 'Em Andamento', 2),
        (Ocorrencia.status == 'Resolvido', 3),
        else_=4
    )
    from sqlalchemy import func

    contadores = db.session.query(
        Ocorrencia.status,
        func.count(Ocorrencia.id)
    ).group_by(Ocorrencia.status).all()

    contagem = {
        'Pendente': 0,
        'Em Andamento': 0,
        'Resolvido': 0
    }

    for status, total in contadores:
        contagem[status] = total
    # começa a query
    query = Ocorrencia.query

    # aplica filtro se existir
    if filtro_status:
        query = query.filter(Ocorrencia.status == filtro_status)

    # mantém sua ordenação original
    todas_ocorrencias = query.order_by(
        ordem_status,
        Ocorrencia.id.desc()
    ).all()

    return render_template('dashboard.html',
                           ocorrencias=todas_ocorrencias,
                            contagem=contagem)
@app.route('/nova-ocorrencia', methods=['GET', 'POST'])
def nova_ocorrencia():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo_digitado = request.form.get('titulo')
        descricao_digitada = request.form.get('descricao')

        nova = Ocorrencia(
            titulo=titulo_digitado,
            descricao=descricao_digitada,
            usuario_id=session['usuario_id']
        )

        db.session.add(nova)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('nova_ocorrencia.html')


# --- NOVA ROTA: ALTERAR STATUS ---
@app.route('/atualizar-status/<int:id>/<novo_status>')
def atualizar_status(id, novo_status):
    # Proteção: Apenas síndicos podem alterar o status
    if session.get('usuario_tipo') != 'sindico':
        return "Acesso negado: Apenas a administração pode alterar status.", 403

    ocorrencia = Ocorrencia.query.get(id)
    if ocorrencia and novo_status in ['Pendente', 'Em Andamento', 'Resolvido']:
        ocorrencia.status = novo_status
        db.session.commit()

    return redirect(url_for('dashboard'))
import bcrypt

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if session.get('usuario_tipo') != 'sindico':
        return "Acesso negado: Apenas a administração pode cadastrar usuários.", 403

    if request.method == 'POST':
        senha_plana = request.form.get('senha')

        hash_senha = bcrypt.hashpw(
            senha_plana.encode('utf-8'),
            bcrypt.gensalt()
        )

        novo_u = Usuario(
            nome=request.form.get('nome'),
            email=request.form.get('email'),
            senha=hash_senha.decode('utf-8'),
            unidade=request.form.get('unidade'),
            tipo=request.form.get('tipo')
        )

        db.session.add(novo_u)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('cadastro.html')


@app.route('/usuarios')
def lista_usuarios():
    # Proteção: Apenas síndicos vêem a lista de moradores
    if session.get('usuario_tipo') != 'sindico':
        return "Acesso negado.", 403

    todos_usuarios = Usuario.query.order_by(Usuario.nome).all()
    return render_template('usuarios.html', usuarios=todos_usuarios)

@app.route('/logout')
def logout():
    session.clear()  # Limpa tudo ao sair
    return redirect(url_for('login'))