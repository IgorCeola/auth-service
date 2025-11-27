from fastapi import FastAPI
from controllers.auth_controller import router

app = FastAPI(title="Auth Service")

app.include_router(router)

@app.get("/")
def root():
    return {"mensagem": "Auth Service ativo, capitão!"}
