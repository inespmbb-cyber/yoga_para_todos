from email.mime import base

from flask import Flask, render_template 

import sqlite3

from flask import request, redirect, url_for


app = Flask(__name__)


# Função para ligar à base de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Rota para a página principal (função index), onde listamos as posturas
@app.route('/')
def index():
    conn = get_db_connection()
    posturas = conn.execute('SELECT * FROM posturas').fetchall()
    conn.close()
    # Agora usamos o render_template para enviar os dados para o HTML
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
# Se a postura não for encontrada, mostramos uma mensagem de erro
        
    return render_template('detalhes.html', postura=postura) 
# Se a postura for encontrada, mostramos a página de detalhes, passando os dados 
# da postura para o HTML


# Rota para criar uma nova postura, onde o utilizador pode preencher um formulário
@app.route('/criar', methods=('GET', 'POST'))
def criar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        instrucoes = request.form['instrucoes']
        nivel = request.form['nivel']

        conn = get_db_connection()
        conn.execute('INSERT INTO posturas (titulo, descricao, instrucoes, nivel, categoria_id) VALUES (?, ?, ?, ?, ?)',
                     (titulo, descricao, instrucoes, nivel, 1)) # Categoria 1 por defeito para já
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('criar.html')

if __name__ == '__main__':
    app.run(debug=True)
# Este código é o backend (Python) da aplicação Flask. Ele define as rotas para 
# a página principal e para a página de detalhes de cada postura, além de se 
# conectar à base de dados SQLite para buscar as informações necessárias.
