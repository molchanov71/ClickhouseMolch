from datetime import datetime as dt
from fastapi import Body
from fastapi.responses import FileResponse, JSONResponse
from . import app
from .load import load
from .queries import *

FORMAT_LINE = '%d.%m.%Y %H:%M:%S'


@app.get('/api/foams/types')
def get_foam_types(location):
    types = query_get_distinct_foam_types(location)
    return JSONResponse(types)


@app.get('/api/foams/by_time')
def get_foams_by_time(location, begin, end, foam_type):
    begin = dt.strptime(begin, FORMAT_LINE).timestamp()
    end = dt.strptime(end, FORMAT_LINE).timestamp()
    res = query_get_foams_by_time(location, begin, end, foam_type)
    return res


@app.get('/api/datetimes')
def get_datetimes(location):
    timestamps = query_get_distinct_ts(location)
    datetimes = sorted({pydt.strftime(FORMAT_LINE) for pydt in map(dt.fromtimestamp, timestamps)})
    return JSONResponse(datetimes)


@app.post('/api/foams/sort')
def sort_foams(data=Body()):
    location = data['location']
    begin = data['begin']
    end = data['end']
    foam = data['foam']
    foams_table = get_foams_by_time(location, begin, end, foam)
    return load(foams_table)


@app.get('/')
def index():
    return FileResponse('src/index.html')
