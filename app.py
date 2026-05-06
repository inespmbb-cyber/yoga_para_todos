import sqlite3
import random
import os 
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'uma_chave_muito_secreta_padrao')
# A chave secreta é necessária para usar o flash, que é uma forma de mostrar
# mensagens

# Função para ligar à base de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Rota para a página principal, onde mostramos a lista de posturas. Se o utilizador
# usar o campo de pesquisa, filtramos as posturas para mostrar apenas aquelas que
# não contenham a palavra escrita no campo de contra-indicações.
@app.route('/')
def index():
    evitar = request.args.get('evitar')
    conn = get_db_connection()
    
    if evitar:
        # Procuramos posturas que NÃO contenham a palavra escrita
        # Usamos LOWER para a pesquisa não ser sensível a maiúsculas
        query = "SELECT * FROM posturas WHERE contraindicacoes NOT LIKE ? OR contraindicacoes IS NULL"
        posturas = conn.execute(query, ('%' + evitar + '%',)).fetchall()
    else:
        posturas = conn.execute('SELECT * FROM posturas').fetchall()
        
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
        titulo = request.form.get('titulo', 'Sem Título')
        nivel = request.form.get('nivel', 'Iniciante')
        descricao = request.form.get('descricao', '')
        fase_aula = request.form.get('fase_aula', 'Desenvolvimento')
        contraindicacoes = request.form.get('contraindicacoes', '')
        instrucoes = request.form.get('instrucoes', '') # Se estiver vazio, fica ''
        desc_curta = request.form.get('desc_curta', '')

        conn = get_db_connection()
        conn.execute('INSERT INTO posturas (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula, categoria_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (titulo, descricao, instrucoes, nivel, contraindicacoes, fase_aula, 1)) # Categoria 1 por defeito para já
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
        titulo = request.form['titulo']
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

@app.route('/gerar_sequencia')
def gerar_sequencia():
    conn = get_db_connection()
    
    # Procuramos posturas para cada fase
    aquecimento = conn.execute("SELECT * FROM posturas WHERE fase_aula = 'Aquecimento'").fetchall()
    desenvolvimento = conn.execute("SELECT * FROM posturas WHERE fase_aula = 'Desenvolvimento'").fetchall()
    relaxamento = conn.execute("SELECT * FROM posturas WHERE fase_aula = 'Relaxamento'").fetchall()
    
    conn.close()

    # Verificamos se temos pelo menos uma de cada para não dar erro
    if not aquecimento or not desenvolvimento or not relaxamento:
        flash('Precisas de ter pelo menos uma postura em cada fase (Aquecimento, Desenvolvimento e Relaxamento) para gerar uma sequência!', 'warning')
        return redirect(url_for('index'))

    # Seleção aleatória
    sequencia = [
        random.choice(aquecimento),
        random.choice(desenvolvimento),
        random.choice(relaxamento)
    ]
    
    return render_template('sequencia.html', sequencia=sequencia)

if __name__ == '__main__':
    app.run(debug=True)
# Este código é o backend (Python) da aplicação Flask. Ele define as rotas para 
# a página principal e para a página de detalhes de cada postura, além de
# conectar à base de dados SQLite para procurar as informações necessárias.
