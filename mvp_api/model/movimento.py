from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Movimento(Base):
    __tablename__ = 'movimento'

    codigo = Column(String(32), primary_key=True)
    descr = Column(String(140))
    foco = Column(String(32))
    tipo = Column(String(32))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, codigo:str, descr:str, foco:str, tipo:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Movimento

        Arguments:
            codigo: codigo do movimento.
            descr: descrição do movimento
            foco: parte do corpo trabalhada pelo movimento
            tipo: tipo de trabalho muscular
            data_insercao: data de quando o produto foi inserido à base
        """
        self.codigo = codigo
        self.descr = descr
        self.foco = foco
        self.tipo = tipo

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


