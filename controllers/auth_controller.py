from fastapi import APIRouter, HTTPException
from usecases.auth_usecase import AuthUseCase
from repository.user_repository import UserRepository

router = APIRouter()

repo = UserRepository()
usecase = AuthUseCase(repo)

@router.post("/register")
def register(data: dict):
    return usecase.register_user(data["username"], data["password"])

@router.post("/login")
def login(data: dict):
    result = usecase.login_user(data["username"], data["password"])
    if "erro" in result:
        raise HTTPException(status_code=401, detail=result["erro"])
    return result

# @router.post("/verify")
# def verify_token(data: dict):
#     from jose import jwt, JWTError
#     token = data.get("token")
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return {"valid": True, "username": payload.get("sub")}
#     except JWTError:
#         return {"valid": False}
