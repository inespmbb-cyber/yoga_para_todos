from flask import Flask, render_template 

import sqlite3


app = Flask(__name__)

# Função para ligar à base de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posturas = conn.execute('SELECT * FROM posturas').fetchall()
    conn.close()
    # Agora usamos o render_template para enviar os dados para o HTML
    return render_template('index.html', posturas=posturas)

if __name__ == '__main__':
    app.run(debug=True)