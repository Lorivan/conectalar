from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import Usuario, Ocorrencia

app.secret_key = 'chave_secreta_conectalar'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_digitado = request.form.get('email')
        senha_digitada = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email_digitado).first()

        if usuario and usuario.senha == senha_digitada:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_tipo'] = usuario.tipo  # <-- NOVO: Guarda se é síndico ou morador
            return redirect(url_for('dashboard'))
        else:
            return "<h1>E-mail ou senha incorretos! Volte e tente novamente.</h1>"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    # Busca todas as ocorrências
    todas_ocorrencias = Ocorrencia.query.order_by(Ocorrencia.data_criacao.desc()).all()

    return render_template('dashboard.html', ocorrencias=todas_ocorrencias)


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


@app.route('/logout')
def logout():
    session.clear()  # Limpa tudo ao sair
    return redirect(url_for('login'))