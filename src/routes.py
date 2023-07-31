from fastapi.responses import FileResponse
from api import app


@app.get('/')
def index():
    return FileResponse('src/index.html')
