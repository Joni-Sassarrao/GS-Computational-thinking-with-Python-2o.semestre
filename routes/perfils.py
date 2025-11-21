from fastapi import APIRouter
from crud import listar_perfis, buscar_por_area, buscar_por_habilidade, filtrar_por_cargo

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