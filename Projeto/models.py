from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    ) # index cria um índice para busca; autoincrement gera o ID automaticamente

    name = Column(
        String(100),
        nullable=False,
    ) # nullable=False significa que não quero aceitar valores nulos

    birth_date = Column(
        Date,
        nullable=False
    )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey('estudantes.id')
    )

    discipline_name = Column(
        String(100),
        nullable=False
    )
