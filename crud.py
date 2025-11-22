from fastapi import HTTPException
from bson import ObjectId, errors
from database import collection
from schemas import PerfilCreate

async def listar_perfis():
    perfis = []
    async for p in collection.find():
        p["id"] = str(p["_id"])
        del p["_id"]
        perfis.append(p)
    return perfis

async def buscar_por_area(area: str):
    cursor = collection.find({"area": area})
    perfis = []
    async for p in cursor:
        p["id"] = str(p["_id"])
        del p["_id"]
        perfis.append(p)
    return perfis

async def buscar_por_habilidade(habilidade: str):
    cursor = collection.find({"habilidadesTecnicas": habilidade})
    perfis = []
    async for p in cursor:
        p["id"] = str(p["_id"])
        del p["_id"]
        perfis.append(p)
    return perfis

async def filtrar_por_cargo(cargo: str):
    perfis_filtrados = []
    async for perfil in collection.find():
        if perfil.get("cargo", "").lower() == cargo.lower():
            perfil["id"] = str(perfil["_id"])
            del perfil["_id"]
            perfis_filtrados.append(perfil)
    return perfis_filtrados

async def criar_perfil(perfil: PerfilCreate):
    novo = perfil.dict()
    resultado = await collection.insert_one(novo)
    perfil_criado = await collection.find_one({"_id": resultado.inserted_id})
    perfil_criado["id"] = str(perfil_criado["_id"])
    del perfil_criado["_id"]
    return perfil_criado

async def deletar_perfil(id: str):
    try:
        obj_id = ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido. Use um ObjectId válido.")

    resultado = await collection.delete_one({"_id": obj_id})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Perfil não encontrado.")

    return {"mensagem": "Perfil deletado com sucesso!"}