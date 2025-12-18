from sqlalchemy import create_engine # Ela cria o Engine, que é o “motor” de conexão com o banco (PostgreSQL, SQLite, etc.)
from sqlalchemy.orm import declarative_base, sessionmaker

'''
declarative_base: cria uma classe base que você vai usar para definir seus models/tabelas (ex.: class Aluno(Base): ...).

sessionmaker: cria uma “fábrica de sessões”, ou seja, um gerador de objetos Session para você executar consultas e 
comandos (SELECT/INSERT/UPDATE/DELETE).
'''

DATABASE_URL = 'postgresql://usuario:senha@localhost/escola' # Sim, o meu usuário é usuário e a minha senha é senha

'''
postgresql:// → diz que o banco é PostgreSQL

usuario:senha@ → usuário e senha do banco

localhost → o banco está rodando na sua máquina

/escola → nome do banco de dados é escola
'''

engine = create_engine(DATABASE_URL) # Esse engine mantém as configurações e cria conexões reais com o banco quando necessário.
SessionLocal = sessionmaker(bind=engine) # bind=engine significa: “toda sessão criada por aqui vai usar esse engine”.

Base = declarative_base() # Cria a classe base para seus modelos ORM.
