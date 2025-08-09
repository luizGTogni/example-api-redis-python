from src.main.server.server import app
from src.models.sqlite.settings.connection import sqlite_connection_handler
from src.models.redis.settings.connection import redis_connection_handler

if __name__ == "__main__":
    sqlite_connection_handler.connect()
    redis_connection_handler.connect()
    app.run(host="0.0.0.0", port=3000, debug=True)
