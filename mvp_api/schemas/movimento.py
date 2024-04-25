from pydantic import BaseModel
from typing import Optional, List
from model.movimento import Movimento


class MovimentoSchema(BaseModel):
    """ Define como um novo movimento a ser inserido deve ser representado
    """
    codigo: str = "Desenv0001"
    descr: str = "Em posição ereta, pés ligeiramente afastados, segurando halteres"
    foco: str = "Ombros"
    tipo: str = "Musculação"


class MovimentoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no código do movimento.
    """
    codigo: str = "Teste"


class ListagemMovimentosSchema(BaseModel):
    """ Define como uma listagem de movimentos será retornada.
    """
    movimentos:List[MovimentoSchema]


def apresenta_movimentos(movimentos: List[Movimento]):
    """ Retorna uma representação do movimento seguindo o schema definido em
        MovimentoViewSchema.
    """
    result = []
    for movimento in movimentos:
        result.append({
            "codigo": movimento.codigo,
            "descr": movimento.descr,
            "foco": movimento.foco,
            "tipo": movimento.tipo,
        })

    return {"movimentos": result}


class MovimentoViewSchema(BaseModel):
    """ Define como um movimento será retornado: movimento.
    """
    codigo: str = "Desenv0001"
    descr: str = "Em posição ereta, pés ligeiramente afastados, segurando halteres"
    foco: str = "Ombros"
    tipo: str = "Tonificação"
    
   
class MovimentoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    codigo: str

def apresenta_movimento(movimento: Movimento):
    """ Retorna uma representação do movimento seguindo o schema definido em
        MovimentoViewSchema.
    """
    return {
        "codigo": movimento.codigo,
        "descr": movimento.descr,
        "foco": movimento.foco,
        "tipo": movimento.tipo,
    }
