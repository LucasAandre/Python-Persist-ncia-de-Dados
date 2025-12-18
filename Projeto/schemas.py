from pydantic import BaseModel
from datetime import date

# Matrícula = Enrollment

class StudentBase(BaseModel):
    name: str
    birth_date: date

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True # Podemos ler os campos do estudante diretamente do nosso modelo

class EnrollmentBase(BaseModel):
    student_id: int
    discipline_name: str

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentResponse(EnrollmentBase):
    id: int
    class Config:
        from_attributes = True
    
