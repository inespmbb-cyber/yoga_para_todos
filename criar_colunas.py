import sqlite3

def adicionar_colunas():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Tenta criar a coluna contraindicacoes
    try:
        cursor.execute('ALTER TABLE posturas ADD COLUMN contraindicacoes TEXT;')
        print("✅ Coluna 'contraindicacoes' criada!")
    except sqlite3.OperationalError:
        print("ℹ️ A coluna 'contraindicacoes' já existe.")

    # Tenta criar a coluna fase_aula
    try:
        cursor.execute('ALTER TABLE posturas ADD COLUMN fase_aula TEXT;')
        print("✅ Coluna 'fase_aula' criada!")
    except sqlite3.OperationalError:
        print("ℹ️ A coluna 'fase_aula' já existe.")

    conn.commit()
    conn.close()
    print("\nVerificação concluída. Podes voltar ao app.py!")

if __name__ == "__main__":
    adicionar_colunas()