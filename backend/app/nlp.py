from langchain.llm import OpenAI
from llama_index import Document, GPTSimpleVectorIndex
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_answer_from_document(document_text, question):
    documents = [Document(text=document_text)]
    index = GPTSimpleVectorIndex(documents)
    response = index.query(question)
    return response
