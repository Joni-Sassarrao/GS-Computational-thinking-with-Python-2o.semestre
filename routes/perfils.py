from fastapi import APIRouter
from schemas import PerfilCreate
from crud import (
    listar_perfis,
    buscar_por_area,
    buscar_por_habilidade,
    filtrar_por_cargo,
    criar_perfil,
    deletar_perfil
)
router = APIRouter(prefix="/perfis")

@router.get("/")
async def get_perfis():
    return await listar_perfis()

@router.get("/area/{area}")
async def get_por_area(area: str):
    return await buscar_por_area(area)

@router.get("/habilidade/{habilidade}")
async def get_por_habilidade(habilidade: str):
    return await buscar_por_habilidade(habilidade)

@router.get("/cargo/{cargo}")
async def get_por_cargo(cargo: str):
    return await filtrar_por_cargo(cargo)

@router.post("/")
async def post_perfil(perfil: PerfilCreate):
    return await criar_perfil(perfil)

@router.delete("/{id}")
async def delete_perfil(id: str):
    return await deletar_perfil(id)