from fastapi import FastAPI, UploadFile, File, HTTPException
from rag import add_document, query_document
from pypdf import PdfReader

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    text = ""

    # TXT files
    if file.filename.lower().endswith(".txt"):
        text = (await file.read()).decode("utf-8")

    # PDF files (text-based)
    elif file.filename.lower().endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    # Unsupported file types
    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload TXT or PDF files only."
        )

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the uploaded document."
        )

    add_document(text)
    return {"message": "Document uploaded and processed successfully"}

@app.get("/ask")
async def ask(question: str):
    answer = query_document(question)
    return {"answer": answer}
