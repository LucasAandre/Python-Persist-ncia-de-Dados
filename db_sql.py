import sqlite3

# Conecta (ou cria) um banco de dados no arquivo local
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# Cria uma tabela de exemplo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER
               )

''')

# Insere registro
cursor.execute('INSERT INTO usuarios(nome, idade) VALUES (?, ?)', ('Lucas', 26))
conexao.commit() # Salva as alterações

# Consulta e exibe os dados
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall()) # [(1, 'Lucas', 26)]

conexao.close()
