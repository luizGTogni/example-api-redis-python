from src.models.sqlite.settings.connection import sqlite_connection_handler
from src.models.redis.settings.connection import redis_connection_handler
from src.models.sqlite.repositories.products_repository import ProductsRepository
from src.models.redis.repositories.redis_repository import RedisRepository
from src.controllers.product_creator import ProductCreatorController
from src.views.product_creator import ProductCreatorView
from src.views.interfaces.view import IView


def product_creator_composer() -> IView:
    sqlite_conn = sqlite_connection_handler.get_connection()
    redis_conn = redis_connection_handler.get_connection()
    sqlite_repository = ProductsRepository(conn=sqlite_conn)
    redis_repository = RedisRepository(redis_conn=redis_conn)
    controller = ProductCreatorController(
        sqlite_repository=sqlite_repository,
        redis_repository=redis_repository
    )
    view = ProductCreatorView(products_controller=controller)

    return view
