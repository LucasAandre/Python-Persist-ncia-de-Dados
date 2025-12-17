import db

# 1. Criando a tabela de estudantes
db.criar_tabela_estudantes()

# 2. Criando a tabela de matrículas
db.criar_tabela_matriculas()

# 3. Criando estudantes
#db.criar_estudante('Sofia', '2012-09-08')
#db.criar_estudante('Gabrielle', '2011-09-19')

# 4. Listando os estudantes
db.listar_estudantes()

# 5. Criando matrículas
#db.criar_matricula(5, 'Arte')
#db.criar_matricula(6, 'Eletricidade Básica')
#db.criar_matricula(3, 'Cálculo 1')
#db.criar_matricula(4, 'Eletromagnetismo')

# 6. Listar as matrículas
print()
db.listar_matriculas()

# 7. Relacionar tabelas
print()
db.relacionar_tabelas()
