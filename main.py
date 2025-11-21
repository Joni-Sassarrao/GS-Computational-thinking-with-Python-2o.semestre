from fastapi import FastAPI
from routes.perfils import router as perfis_router

app = FastAPI(title="GS - Python")

app.include_router(perfis_router)
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API Global Solution!"}