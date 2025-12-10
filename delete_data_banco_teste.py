import sqlite3

conexao = sqlite3.connect('banco_teste.db')
cursor = conexao.cursor()

cursor.execute(
    '''
        DELETE FROM clientes WHERE id >= ?
    ''',
    (5,) # Sem a vírgula seria apenas um número e não uma tupla. Não funcionaria.
)

conexao.commit()
conexao.close()
