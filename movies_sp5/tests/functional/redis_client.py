import pytest_asyncio
from redis import Redis
from settings import redis_settings


@pytest_asyncio.fixture(scope='session')
async def redis_client():
    client = Redis(
        host=redis_settings.REDIS_HOST, port=redis_settings.REDIS_PORT)
    yield client
    client.close()


@pytest_asyncio.fixture(scope='session')
async def flush_cache(redis_client: Redis):
    async def inner():
        result = redis_client.flushdb()
        return result
    return inner
