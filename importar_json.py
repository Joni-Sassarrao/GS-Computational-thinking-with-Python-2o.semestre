import json
from database import collection
import asyncio

async def importar():
    with open("perfis.json", encoding="utf-8") as f:
        dados = json.load(f)
    await collection.delete_many({})
    await collection.insert_many(dados)
    print("Perfis inseridos com sucesso!")

asyncio.run(importar())
