import clickhouse_connect
from fastapi import FastAPI

client = clickhouse_connect.get_client(host='localhost', port=8123)
app = FastAPI()

from .routes import *
