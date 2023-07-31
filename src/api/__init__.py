from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

from src.routes import *
from src.api.routes import *
