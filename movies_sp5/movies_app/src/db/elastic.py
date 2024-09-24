from elasticsearch import AsyncElasticsearch, NotFoundError
from db.abstract import AsyncDataStorage

es: AsyncElasticsearch | None = None


# Функция понадобится при внедрении зависимостей
async def get_elastic() -> 'ElasticClient':
    return ElasticClient()


class ElasticClient(AsyncDataStorage):
    async def get_by_id(self, index: str, _id: str) -> dict | None:
        try:
            return await es.get(index=index, id=_id)
        except NotFoundError:
            return None

    async def search_by_query_with_pagination(self, index: str, body: dict, page_number: int | None = 1, page_size: int | None = 10) -> dict:
        _body = {
            'from': (page_number - 1) * page_size,
            'size': page_size,
        }
        _body |= body
        return await es.search(index=index, body=_body)
    async def index_document(self, index: str, id: str, body: dict):
            return await es.index(index=index, id=id, body=body)
