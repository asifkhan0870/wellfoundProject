from sqlalchemy.orm import Session
from . import models, schemas

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(filename=document.filename, content=document.content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

def create_question(db: Session, question: schemas.QuestionCreate, answer: str):
    db_question = models.Question(pdf_id=question.pdf_id, question=question.question, answer=answer)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
