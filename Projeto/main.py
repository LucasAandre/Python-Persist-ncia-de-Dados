from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # Cria as tabelas no PostgreSQL, caso não existam

app = FastAPI()

def get_db():
    db = SessionLocal() # Cria uma sessão ativa com o banco
    try:
        yield db # yield é tipo um return, mas não encerra a função por aí, como o return faz
    
    finally:
        db.close()

'''
O que acontece passo a passo

1️⃣ db = SessionLocal()
→ cria uma sessão com o banco

2️⃣ yield db
→ entrega a sessão para o endpoint

⏸️ a função PAUSA aqui

3️⃣ Endpoint executa (SELECT, INSERT, etc.)

4️⃣ Quando o endpoint termina (com sucesso ou erro)
→ o FastAPI retoma a função

5️⃣ Entra no finally
→ db.close() fecha a conexão
'''

# Criando os endpoints:

# Registrando um estudante
@app.post('/estudantes/', response_model = schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump()) # Um objeto com as iformações que estão vindo do navegador
    # db_student = models.Estudante(name='Lucas', birth_date=date(1999, 3, 11)) --> Caso eu quisesse colocar sem ler dados do navegador
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Lendo meu banco de dados
@app.get('/estudantes/', response_model = List[schemas.StudentResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all() # SELECT * FROM Estudante
    return students

# DESAFIO: criar endpoints para matrículas e para excluir entradas do banco de dados
