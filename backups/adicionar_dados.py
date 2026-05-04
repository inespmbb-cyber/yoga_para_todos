import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()


cur.execute("INSERT INTO posturas (titulo, descricao, instrucoes, nivel, categoria_id) VALUES (?, ?, ?, ?, ?)",
            ('Gato-Vaca (Marjaryasana)', 'Sequência para mobilidade da coluna.', 'Alterne entre arquear as costas e olhar para cima.', 'Iniciante', 1))


cur.execute("INSERT INTO posturas (titulo, descricao, instrucoes, nivel, categoria_id) VALUES (?, ?, ?, ?, ?)",
            ('Guerreiro II (Virabhadrasana II)', 'Fortalece as pernas.', 'Afaste as pernas e dobre o joelho.', 'Intermedio', 2))

conn.commit()
conn.close()
print("Sucesso total!")