# AI-Powered Document Question Answering System (RAG)

This project is a full-stack Generative AI application that enables users to upload documents and ask natural language questions.  
It uses a Retrieval-Augmented Generation (RAG) architecture to retrieve relevant content from documents and generate context-aware answers.

## Tech Stack
- Backend: Python, FastAPI
- AI / LLM Concepts: Transformer-based embeddings, RAG pipeline
- Vector Database: FAISS
- Document Processing: TXT and text-based PDF
- Tools: Git, REST APIs

## Features
- Upload TXT and PDF documents
- Semantic search using vector embeddings
- Context-based question answering
- Clean REST API design
- Graceful error handling for unsupported files

## Architecture Overview
1. Document ingestion and text extraction
2. Embedding generation using transformer models
3. Vector similarity search with FAISS
4. Context-aware response generation

## How to Run
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
