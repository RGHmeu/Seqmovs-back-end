from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Movimento
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="MVP API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
movimento_tag = Tag(name="Movimento", description="Adição, visualização e remoção de movimentos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/movimento', tags=[movimento_tag],
          responses={"200": MovimentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_movimento(form: MovimentoSchema):
    """Adiciona um novo Movimento à base de dados

    Retorna uma representação dos movimentos.
    """
    movimento = Movimento(
        codigo=form.codigo,
        descr=form.descr,
        foco=form.foco,
        tipo=form.tipo)
    logger.debug(f"Adicionando movimento de codigo: '{movimento.codigo}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando movimento
        session.add(movimento)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado movimento de nome: '{movimento.codigo}'")
        return apresenta_movimento(movimento), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Movimento de mesmo código já salvo na base :/"
        logger.warning(f"Erro ao adicionar movimento '{movimento.codigo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar movimento '{movimento.codigo}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/movimentos', tags=[movimento_tag],
         responses={"200": ListagemMovimentosSchema, "404": ErrorSchema})
def get_movimentos():
    """Faz a busca por todos os movimentos cadastrados

    Retorna uma representação da listagem de movimentos.
    """
    logger.debug(f"Coletando movimentos")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    movimentos = session.query(Movimento).all()

    if not movimentos:
        # se não há produtos cadastrados
        return {"movimentos": []}, 200
    else:
        logger.debug(f"%d movimentos econtrados" % len(movimentos))
        # retorna a representação de movimento
        print(movimentos)
        return apresenta_movimentos(movimentos), 200


@app.get('/movimento', tags=[movimento_tag],
         responses={"200": MovimentoViewSchema, "404": ErrorSchema})
def get_movimento(query: MovimentoBuscaSchema):
    """Faz a busca por um Movimento a partir do codigo do movimento

    Retorna uma representação dos movimentos.
    """
    movimento_codigo = query.codigo
    logger.debug(f"Coletando dados sobre movimento #{movimento_codigo}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    movimento = session.query(Movimento).filter(Movimento.codigo == movimento_codigo).first()

    if not movimento:
        # se o movimento não foi encontrado
        error_msg = "Movimento não encontrado na base :/"
        logger.warning(f"Erro ao buscar movimento '{movimento.codigo}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Movimento econtrado: '{movimento.codigo}'")
        # retorna a representação de movimento
        return apresenta_movimento(movimento), 200


@app.delete('/movimento', tags=[movimento_tag],
            responses={"200": MovimentoDelSchema, "404": ErrorSchema})
def del_movimento(query: MovimentoBuscaSchema):
    """Deleta um Movimento a partir do codigo de movimento informado

    Retorna uma mensagem de confirmação da remoção.
    """
    movimento_codigo = unquote(unquote(query.codigo))
    print(movimento_codigo)
    logger.debug(f"Deletando dados sobre movimento #{movimento_codigo}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Movimento).filter(Movimento.codigo == movimento_codigo).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado movimento #{movimento_codigo}")
        return {"mesage": "Movimento removido", "codigo": movimento_codigo}
    else:
        # se o produto não foi encontrado
        error_msg = "Movimento não encontrado na base :/"
        logger.warning(f"Erro ao deletar movimento #'{movimento_codigo}', {error_msg}")
        return {"mesage": error_msg}, 404

