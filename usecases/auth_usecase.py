from jose import jwt
from config.settings import SECRET_KEY, ALGORITHM

class AuthUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, password):
        self.user_repository.create_user(username, password)
        return {"mensagem": "Usuário registrado com sucesso"}

    def login_user(self, username, password):
        valid = self.user_repository.validate_user(username, password)
        if not valid:
            return {"erro": "Usuário ou senha inválidos"}
        token = jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
