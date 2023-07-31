from fastapi import FastAPI

app = FastAPI()

from src.routes import *
from src.api.routes import *
