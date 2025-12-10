import sqlite3

clientes = [
    ('Neymar', '1992-02-05'),
    ('Nelvis', '1999-03-11'),
    ('Valktro', '2010-06-03'),
    ('Oslwaldiney', '2018-12-27')
]

conexao = sqlite3.connect('banco_teste.db')
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nascimento DATE
        )
    '''
)

cursor.executemany('INSERT INTO clientes (nome, nascimento) VALUES (?, ?)', clientes)

conexao.commit()

cursor.execute('SELECT * FROM clientes')
exibir = cursor.fetchall()
print(exibir)

print('\n')

cursor.execute(
    '''
        UPDATE clientes SET nascimento = ? WHERE nome = ?
    ''',
    ('2010-06-30', 'Valktro')
)

cursor.execute('SELECT * FROM clientes')
print(exibir)

conexao.commit()
conexao.close()
