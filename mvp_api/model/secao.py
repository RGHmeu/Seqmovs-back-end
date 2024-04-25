from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Secao(Base):
    __tablename__ = 'secao'

    token = Column(String(13), primary_key=True)
    latitude = Column(String(11))
    longitude = Column(String(11))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, token:String, latitude:String, longitude:String,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Secao

        Arguments:
            token: identificação da seção do usuário
            latidude: coordenada da geolocalização do usuário
            longitude: coordenada da geolocalização do usuário
            data_insercao: data de quando a seção começou
        """
        self.token = token
        self.latitude = latitude
        self.longitude = longitude
 
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


