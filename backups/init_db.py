import sqlite3

connection = sqlite3.connect('database.db')

try:
    with open('schema.sql') as f:
        connection.executescript(f.read())
except FileNotFoundError:
    print("Erro: O ficheiro 'schema.sql' não foi encontrado. Certifique-se de que o ficheiro existe antes de executar este script.")
    exit(1)

cur = connection.cursor()


cur.execute("INSERT INTO categorias (nome) VALUES (?)", ('Flexibilidade',))
cur.execute("INSERT INTO categorias (nome) VALUES (?)", ('Força',))
cur.execute("INSERT INTO categorias (nome) VALUES (?)", ('Relaxamento',))


cur.execute("INSERT INTO posturas (titulo, descricao, instrucoes, nivel, categoria_id) VALUES (?, ?, ?, ?, ?)",
            ('Postura da Criança (Balasana)', 
             'Uma postura de descanso suave.', 
             'Ajoelhe-se no chão, toque os dedos grandes dos pés e sente-se nos calcanhares.', 
             'Iniciante', 
             3)
            )

cur.execute("INSERT INTO posturas (titulo, descricao, instrucoes, nivel, categoria_id) VALUES (?, ?, ?, ?, ?)",
            ('Cachorro Olhando para Baixo (Adho Mukha Svanasana)', 
             'Uma postura de alongamento integral.', 
             'Comece de quatro, levante os quadris em direção ao teto formando um V invertido.', 
             'Iniciante', 
             1)
            )

connection.commit()
connection.close()
print("Base de dados criada com sucesso!")