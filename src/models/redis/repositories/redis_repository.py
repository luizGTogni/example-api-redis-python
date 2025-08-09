from redis import Redis
from .interfaces.redis_repository import IRedisRepository

class RedisRepository(IRedisRepository):
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: str, expire_seconds: int = -1) -> None:
        self.__redis_conn.set(key, value, ex=expire_seconds)

    def get_key(self, key: str) -> str:
        value = self.__redis_conn.get(key)

        if not value:
            return None

        return value.decode("utf-8")

    def insert_hash(self, key: str, field: str, value: str, expire_seconds: int = -1) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, time=expire_seconds)

    def get_hash(self, key: str, field: str) -> str:
        value = self.__redis_conn.hget(key, field)

        if not value:
            return None

        return value.decode("utf-8")
