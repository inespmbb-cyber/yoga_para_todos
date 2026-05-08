import sqlite3
import os 
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'uma_chave_muito_secreta_padrao')
# A chave secreta é necessária para usar o flash, que é uma forma de mostrar
# mensagens

# Função para ligar à base de dados
def get_db_connection():
    # Define o caminho absoluto para o banco de dados na raiz do projeto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database.db')
    conn = sqlite3.connect(db_path)
    # Esta linha permite aceder aos dados como postura['titulo'] em vez de postura[0]
    conn.row_factory = sqlite3.Row 
    return conn

# Rota para a página principal, onde mostramos a lista de posturas. Se o utilizador
# usar o campo de pesquisa 'busca', procuramos por correspondências no título.
@app.route('/')
def index():
    busca = request.args.get('busca', '')
    nivel_filtro = request.args.get('nivel_filtro', '')
    evitar = request.args.get('evitar', '')
    
    conn = get_db_connection()
    
    # Base da query
    query = "SELECT * FROM posturas WHERE 1=1"
    params = []

    # Pesquisa por Título (mais robusta e insensível a maiúsculas/minúsculas)
    if busca:
        query += " AND LOWER(titulo) LIKE LOWER(?)"
        params.append(f'%{busca.lower()}%')
    
    # Filtro por Nível
    if nivel_filtro:
        query += " AND nivel = ?"
        params.append(nivel_filtro)

    # Filtro de Contraindicações (Evitar)
    if evitar:
        query += " AND (LOWER(contraindicacoes) NOT LIKE ? OR contraindicacoes IS NULL)"
        params.append(f'%{evitar.lower()}%')

    query += " ORDER BY titulo COLLATE NOCASE ASC"
    
    posturas = conn.execute(query, params).fetchall()
    conn.close()
    
    return render_template('index.html', posturas=posturas)


# Rota para a página de detalhes de uma postura, onde mostramos mais informações
# sobre a postura selecionada, usando o ID da postura na URL
@app.route('/postura/<int:postura_id>')
def detalhes(postura_id):
    conn = get_db_connection()
    # Procuramos a postura que tenha o ID que clicámos
    postura = conn.execute('SELECT * FROM posturas WHERE id = ?', (postura_id,)).fetchone()
    conn.close()
    
    if postura is None:
        return "Postura não encontrada!", 404 
# Se a postura não for encontrada, mostra uma mensagem de erro
        
    return render_template('detalhes.html', postura=postura) 
# Se a postura for encontrada, mostra a página de detalhes, passando os dados 
# da postura para o HTML


# Rota para criar uma nova postura, onde o utilizador pode preencher um formulário
@app.route('/criar', methods=('GET', 'POST'))
def criar():
    if request.method == 'POST':
        titulo = request.form.get('titulo', 'Sem Título').strip()
        nivel = request.form.get('nivel', 'Iniciante')
        fase_aula = request.form.get('fase_aula', 'Desenvolvimento')
        contraindicacoes = request.form.get('contraindicacoes', '')
        instrucoes = request.form.get('instrucoes', '') # Se estiver vazio, fica ''
        descricao = request.form.get('descricao')

        conn = get_db_connection()
        conn.execute('INSERT INTO posturas (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula) VALUES (?, ?, ?, ?, ?, ?)',
                     (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula))
        conn.commit()
        conn.close()
        flash('Postura criada com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('criar.html')


# Rota para editar uma postura existente, onde o utilizador pode atualizar 
# as informações de uma postura selecionada, usando o ID da postura 
# na URL e um formulário para editar os dados da postura
@app.route('/postura/<int:id>/editar', methods=('GET', 'POST'))
def editar(id):
    conn = get_db_connection()
    postura = conn.execute('SELECT * FROM posturas WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        descricao = request.form['descricao']
        instrucoes = request.form['instrucoes']
        nivel = request.form['nivel']
        contraindicacoes = request.form['contraindicacoes']
        fase_aula = request.form['fase_aula']

        conn.execute('''UPDATE posturas 
                SET titulo = ?, descricao = ?, instrucoes = ?, nivel = ?, 
                    contraindicacoes = ?, fase_aula = ? 
                WHERE id = ?''',
             (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula, id))
        conn.commit()
        conn.close()
        flash('Postura atualizada com sucesso!', 'info')
        return redirect(url_for('index'))

    conn.close()
    return render_template('editar.html', postura=postura)


# Rota para apagar uma postura, onde o utilizador pode remover postura
# selecionada, usando o ID da postura na URL e um formulário para confirmar a
# exclusão da postura
@app.route('/postura/<int:id>/apagar', methods=('POST',))
def apagar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posturas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Postura apagada com sucesso!', 'danger')
    return redirect(url_for('index'))

# Rota para gerar uma sequência inteligente, onde o utilizador pode escolher
# o tempo e o nível de dificuldade
@app.route('/gerar_sequencia_inteligente', methods=['POST'])
def gerar_sequencia_inteligente():
    tempo = int(request.form.get('tempo', 20))
    nivel = request.form.get('nivel')
    evitar = request.form.get('evitar', '').lower()

    n_posturas = int(tempo / 2)
    
    # Definir distribuição (ex: 20% Aquecimento, 60% Desenvolvimento, 20% Relaxamento)
    n_aq = max(1, int(n_posturas * 0.2))
    n_rel = max(1, int(n_posturas * 0.2))
    n_des = max(1, n_posturas - n_aq - n_rel)

    conn = get_db_connection()
    
    def buscar_fase(fase, limite):
        query = "SELECT * FROM posturas WHERE (nivel = ? OR nivel = 'Iniciante') AND fase_aula = ?"
        params = [nivel, fase]
        if evitar:
            query += " AND (LOWER(contraindicacoes) NOT LIKE ? OR contraindicacoes IS NULL)"
            params.append(f'%{evitar}%')
        query += " ORDER BY RANDOM() LIMIT ?"
        params.append(limite)
        return conn.execute(query, params).fetchall()

    # Procura posturas para cada fase de forma independente
    lista_aq = buscar_fase('Aquecimento', n_aq)
    lista_des = buscar_fase('Desenvolvimento', n_des)
    lista_rel = buscar_fase('Relaxamento', n_rel)

    # Junta as listas mantendo a ordem correta da aula
    sequencia = lista_aq + lista_des + lista_rel
    conn.close()

    # Se a sequência vier vazia, avisa o utilizador ou mostra erro
    if not sequencia:
        return "Nenhuma postura encontrada para estes filtros. Tenta mudar o nível ou remover limitações."

    return render_template('sequencia.html', sequencia=sequencia, tempo=tempo, nivel=nivel)

if __name__ == '__main__':
    app.run(debug=True)
# Este código é o backend (Python) da aplicação Flask. Ele define as rotas para 
# a página principal e para a página de detalhes de cada postura, além de
# conectar à base de dados SQLite para procurar as informações necessárias.
