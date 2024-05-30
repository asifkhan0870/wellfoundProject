from fastapi import FastAPI, File, UploadFile, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, nlp
from .database import SessionLocal, engine
import shutil
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/", response_model=schemas.Document)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text_content = nlp.extract_text_from_pdf(file_path)
    document = schemas.DocumentCreate(filename=file.filename, content=text_content)
    return crud.create_document(db=db, document=document)

@app.post("/ask/", response_model=schemas.Question)
async def ask_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    document = crud.get_document(db, question.pdf_id)
    if document:
        answer = nlp.get_answer_from_document(document.content, question.question)
        return crud.create_question(db=db, question=question, answer=answer)
    else:
        raise HTTPException(status_code=404, detail="Document not found")
