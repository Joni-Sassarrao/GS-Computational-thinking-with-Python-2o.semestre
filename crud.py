from database import collection
from bson import ObjectId
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
    cursor = collection.find({"habilidades": habilidade})
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
        else:
            pass
    return perfis_filtrados

async def criar_perfil(perfil: PerfilCreate):
    novo = perfil.dict()
    resultado = await collection.insert_one(novo)
    novo["id"] = str(resultado.inserted_id)
    return {
        "id": novo["id"],
        "mensagem": "Perfil criado com sucesso!"
    }

async def deletar_perfil(id: str):
    resultado = await collection.delete_one({"_id": ObjectId(id)})
    return {"removido": resultado.deleted_count > 0}