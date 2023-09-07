from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Item(Base):
    __tablename__ = 'item'

    artista = Column(String(50))
    descricao = Column(String(100),primary_key=True)
    formato = Column(String(50))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, artista: str, descricao: str, formato: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Item

        Arguments:
            artista: nome do artista.
            descricao: nome do item a ser cadastrado
            formato: formato do item
            data_insercao: data de quando o item foi inserido à base
        """
        self.artista = artista
        self.descricao = descricao
        self.formato = formato

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
