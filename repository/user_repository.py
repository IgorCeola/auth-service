from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    def __init__(self):
        self.users = {} 

    def create_user(self, username: str, password: str):
        password_hash = pwd_context.hash(password)
        self.users[username] = password_hash

    def validate_user(self, username: str, password: str) -> bool:
        if username not in self.users:
            return False
        return pwd_context.verify(password, self.users[username])
