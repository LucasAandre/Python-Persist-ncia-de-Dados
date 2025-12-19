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

# Lendo minha tabela estudantes
@app.get('/estudantes/', response_model = List[schemas.StudentResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all() # SELECT * FROM Estudante
    return students

# DESAFIO 1: criar endpoints para matrículas e para excluir entradas do banco de dados
# DESAFIO 2: ler e extrair os dados das minhas tabelas
# Postar no LinkedIn: imagine um banco com diversos dados ricos em informações para a sua empresa...

# SOLUÇÃO 1: Registrando uma matrícula
@app.post('/matriculas/', response_model = schemas.EnrollmentResponse)
def create_enrollment(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    db_enrollment = models.Matricula(**enrollment.model_dump())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

# SOLUÇÃO 1: Lendo minha tabela matriculas
@app.get('/matriculas/', response_model = List[schemas.EnrollmentResponse])
def read_enrollments(db: Session = Depends(get_db)):
    enrollments = db.query(models.Matricula).all()
    return enrollments

# SOLUÇÃO 1: Deletando estudantes (auxílio do ChatGPT)
@app.delete('/estudantes/{student_id}')
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Estudante).filter(models.Estudante.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail='Estudante não encontrado')
        # raise interrompe a execução da função e dispara uma exceção (erro), enquanto return encerra a função retornando um valor.
    
    db.delete(student)
    db.commit()

    return {
        'message': 'Estudante deletado com sucesso!',
        'student_id': student_id
    }

# SOLUÇÃO 1: Deletando matrículas
@app.delete('/matriculas/{enrollment_id}')
def delete_enrollmente(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(models.Matricula).filter(models.Matricula.id == enrollment_id).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail='Matrícula não encontrada')
    
    db.delete(enrollment)
    db.commit()

    return {
        'message': 'Matrícula deletada com sucesso!',
        'enrollment_id': enrollment_id
    }
