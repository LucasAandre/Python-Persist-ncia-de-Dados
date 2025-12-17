import sqlite3

def conectar():
    conn = sqlite3.connect('escola.db')
    return conn

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS estudantes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                nascimento DATE
            )
        '''
    )
    conn.commit()
    conn.close()

def criar_tabela_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS matriculas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_disciplina TEXT,
                id_estudante INTEGER,
                FOREIGN KEY (id_estudante) REFERENCES estudantes(id)
            )
        '''
    )
    conn.commit()
    conn.close()

def criar_estudante(nome, nascimento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estudantes (nome, nascimento) VALUES (?, ?)', (nome, nascimento))
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estudantes')
    estudantes = cursor.fetchall()
    
    for estudante in estudantes:
        print(estudante)
    
    conn.commit()
    conn.close()

def criar_matricula(id_estudante, nome_disciplina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        '''
            INSERT INTO matriculas (id_estudante, nome_disciplina)
            VALUES (?, ?)
        ''',
        (id_estudante, nome_disciplina)
    )
    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM matriculas')
    matriculas = cursor.fetchall()

    for matricula in matriculas:
        print(matricula)
    
    conn.commit()
    conn.close()

def relacionar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT e.nome, m.nome_disciplina 
            FROM estudantes as e JOIN matriculas as m
            on e.id = m.id_estudante ORDER BY e.nome
        '''
    )
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)

    conn.commit()
    conn.close()
