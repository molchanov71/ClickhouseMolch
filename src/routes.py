from datetime import datetime as dt
from fastapi import Body
from fastapi.responses import FileResponse, JSONResponse
from . import app
from .load import load
from .queries import *

FORMAT_LINE_SRC = '%Y-%m-%dT%H:%M'


@app.get('/api/foams/types')
def get_foam_types(location):
    types = query_get_distinct_foam_types(location)
    return JSONResponse(types)


@app.get('/api/foams/by_time')
def get_foams_by_time(location, begin, end, foam_type):
    begin = dt.strptime(begin, FORMAT_LINE_SRC).timestamp()
    end = dt.strptime(end, FORMAT_LINE_SRC).timestamp()
    res = query_get_foams_by_time(location, begin, end, foam_type)
    return JSONResponse(res)


@app.post('/api/foams/sort')
def sort_foams(data=Body()):
    location = data['location']
    begin = data['begin']
    end = data['end']
    foam = data['foam']
    foams_table = get_foams_by_time(location, begin, end, foam)
    return load(foams_table)


@app.get('/api/locations')
def get_locations():
    locations_list = query_get_locations()
    return JSONResponse(locations_list)


@app.get('/')
def index():
    return FileResponse('src/index.html')
