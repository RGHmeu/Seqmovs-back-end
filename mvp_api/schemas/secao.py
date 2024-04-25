from pydantic import BaseModel
from typing import Optional, List
from model.secao import Secao


class SecaoSchema(BaseModel):
    """ Define como uma nova seção a ser inserida deve ser representado
    """
    token: str = "1713637156311"
    latitude: str = "-22.9474304"
    longitude: str = "-43.1849472"
    


class SecaooBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no token.
    """
    codigo: str = "1613637156311"


class ListagemSecaoSchema(BaseModel):
    """ Define como uma listagem de seções que será retornada.
    """
    secoes:List[SecaoSchema]


def apresenta_secoes(secoes: List[Secao]):
    """ Retorna uma representação da seção seguindo o schema definido em
        SecaoViewSchema.
    """
    result = []
    for secao in secoes:
        result.append({
            "token": secao.token,
            "latitude": secao.latitude,
            "longitude": secao.longitude
         })

    return {"secoes": result}


class SecaoViewSchema(BaseModel):
    """ Define como uma secao será retornado: secao.
    """
    token: str = "1713637156311"
    latitude: str = "-22.9474304"
    longitude: str = "-43.1849472"

    
   
class SecaoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    codigo: str

def apresenta_secao(secao: Secao):
    """ Retorna uma representação da secao seguindo o schema definido em
        SecaoViewSchema.
    """
    return {
        "token": secao.token,
        "latitude": secao.latitude,
        "longitude": secao.longitude,
       }
