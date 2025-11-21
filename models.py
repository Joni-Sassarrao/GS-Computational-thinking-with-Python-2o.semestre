from pydantic import BaseModel
from typing import List, Optional

class Idioma(BaseModel):
    idioma: str
    nivel: str

class Experiencia(BaseModel):
    empresa: str
    cargo: str
    inicio: str
    fim: str
    descricao: str

class Formacao(BaseModel):
    curso: str
    instituicao: str
    ano: int

class Projeto(BaseModel):
    titulo: str
    link: str
    descricao: str

class Perfil(BaseModel):
    id: Optional[str] = None
    nome: str
    cargo: str
    localizacao: str
    area: str
    habilidadesTecnicas: List[str]
    softSkills: List[str]
    experiencias: List[Experiencia]
    formacao: List[Formacao]
    projetos: List[Projeto]
    certificacoes: List[str]
    idiomas: List[Idioma]
    areaInteresses: List[str]