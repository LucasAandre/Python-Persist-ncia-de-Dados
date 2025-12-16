import db

# 1. Criando a tabela de estudantes
db.criar_tabela_estudantes()

# 2. Criando a tabela de matrículas
db.criar_tabela_matriculas()

# 3. Criando estudantes
db.criar_estudante('Lucas', '1999-03-11')
db.criar_estudante('Pamela', '2003-02-02')

# 4. Listando os estudantes
db.listar_estudantes()
