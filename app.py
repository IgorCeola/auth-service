from fastapi import FastAPI
from controllers.auth_controller import router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Auth Service")

@app.on_event("startup")
def startup_event():
    Instrumentator().instrument(
        app, 
        exclude_paths=["/metrics"], 
    ).expose(app)

app.include_router(router)

@app.get("/")
def root():
    return {"mensagem": "Auth Service ativo, capitão!"}
