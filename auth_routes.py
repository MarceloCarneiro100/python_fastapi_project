from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar() -> dict[str, str | bool]:
    """
    Esta é a rota padrão de autenticação do nosso sistema.
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação.", "autenticado": False}