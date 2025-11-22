from database import collection

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
