from pydantic import BaseModel
from datetime import datetime

class DocumentBase(BaseModel):
    filename: str

class DocumentCreate(DocumentBase):
    content: str

class Document(DocumentBase):
    id: int
    upload_date: datetime

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    pdf_id: int
    question: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    answer: str

    class Config:
        orm_mode = True
