from pydantic import BaseModel
from typing import List
from model.item import Item

class ItemSchema(BaseModel):
    """ Define como um novo item a ser inserido deve ser representado"""
    artista: str = "Lady Gaga"
    descricao: str = "Joanne Urban Outfitters Pink Fluorescent"
    formato: str = "Vinil"


class ItemBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do item."""
    descricao: str = "Joanne Urban Outfitters Pink Fluorescent"


class ListagemItemsSchema(BaseModel):
    """ Define como uma listagem de items será retornada."""
    items:List[ItemSchema]


def apresenta_items(items: List[Item]):
    """ Retorna uma representação do item seguindo o schema definido em ItemViewSchema."""
    result = []
    for item in items:
        result.append({
            "artista": item.artista,
            "descricao": item.descricao,
            "formato": item.formato,
        })
    return {"items": result}


class ItemViewSchema(BaseModel):
    """ Define como um item será retornado: item"""
    artista: str = "Lady Gaga"
    descricao: str = "Joanne Urban Outfitters Pink Fluorescent"
    formato: str = "Vinil"


class ItemDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção."""
    mesage: str
    descricao: str

def apresenta_item(item: Item):
    """ Retorna uma representação do item seguindo o schema definido em ItemViewSchema."""
    return {
        "artista": item.artista,
        "descricao": item.descricao,
        "formato": item.formato,
    }
