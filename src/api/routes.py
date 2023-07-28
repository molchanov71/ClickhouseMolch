from fastapi.responses import HTMLResponse
from api import app
from api.db import Foam, session


@app.get('/')
def index():
    res = session.query(Foam).filter(Foam.name == 'Температура').all()
    return HTMLResponse(str(tuple(str(type(foam)) for foam in res)))
