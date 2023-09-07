from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session, Item
from logger import logger
from schemas import *
from flask_cors import CORS, cross_origin

info = Info(title="HAUS WISHLIST API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
item_tag = Tag(name="Item", description="Adição, visualização e remoção de items de desejo à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/item', tags=[item_tag], responses={"200": ItemViewSchema, "400": ErrorSchema})
def add_item(form: ItemSchema):
    """Adiciona um novo Item à base de dados e Retorna uma representação dos items e comentários associados."""
    item = Item(
        artista=form.artista,
        descricao=form.descricao,
        formato=form.formato,)
    logger.debug(f"Adicionando item com a descricao: '{item.descricao}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando item
        session.add(item)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado item com a descricao: '{item.descricao}'")
        return apresenta_item(item), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar item '{item.descricao}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/items', tags=[item_tag], responses={"200": ListagemItemsSchema, "404": ErrorSchema})
def get_items():
    """Faz a busca por todos os Items cadastrados e retorna uma representação da listagem de items."""
    logger.debug(f"Coletando items ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    items = session.query(Item).all()

    if not items:
        # se não há items cadastrados
        return {"items": []}, 200
    else:
        logger.debug(f"%d items encontrados" % len(items))
        # retorna a representação de item
        print(items)
        return apresenta_items(items), 200


@app.get('/item', tags=[item_tag], responses={"200": ItemViewSchema, "404": ErrorSchema})
def get_item(query: ItemBuscaSchema):
    """Faz a busca por um Item a partir dda descricao do item e retorna uma representação dos items."""
    item_descricao = query.descricao
    logger.debug(f"Coletando dados sobre item #{item_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    item = session.query(Item).filter(Item.descricao == item_descricao).first()

    if not item:
        # se o item não foi encontrado
        error_msg = "Item não encontrado na base :/"
        logger.warning(f"Erro ao buscar item '{item_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Item encontrado: '{item.descricao}'")
        # retorna a representação de item
        return apresenta_item(item), 200


@app.delete('/item', tags=[item_tag], responses={"200": ItemDelSchema, "404": ErrorSchema})
def del_item(query: ItemBuscaSchema):
    """Deleta um Item a partir da descricao de item informado e retorna uma mensagem de confirmação da remoção."""
    item_descricao = (query.descricao)
    print(item_descricao)
    logger.debug(f"Deletando dados sobre item #{item_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Item).filter(Item.descricao == item_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado item #{item_descricao}")
        return {"mesage": "Item removido", "id": item_descricao}
    else:
        # se o item não foi encontrado
        error_msg = "Item não encontrado na base :/"
        logger.warning(f"Erro ao deletar item #'{item_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404
