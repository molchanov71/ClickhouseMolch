from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, HTMLResponse
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_CONNECT_URL = 'clickhouse://default:@localhost/Kuznetsk'
engine = sa.create_engine(SQLALCHEMY_CONNECT_URL)
Base = declarative_base()
app = FastAPI()


class Foam(Base, SerializerMixin):
    __tablename__ = 'table1'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    cell = sa.Column(sa.String)
    parent = sa.Column(sa.String)
    name = sa.Column(sa.String)
    ts = sa.Column(sa.Integer)
    value = sa.Column(sa.Integer)
    block_client_id = sa.Column(sa.Integer)
    block_foam_type = sa.Column(sa.String)
    block_place = sa.Column(sa.String)
    block_block_id = sa.Column(sa.Integer)
    block_batch_number = sa.Column(sa.Integer)
    block_recipe_num = sa.Column(sa.Integer)
    block_weight = sa.Column(sa.Integer)
    block_length = sa.Column(sa.Integer)
    block_wide_average = sa.Column(sa.Integer)
    block_height = sa.Column(sa.Integer)


Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()


@app.get('/')
def index():
    return HTMLResponse('It works!')


@app.get('/api/foams')
def get_foams(begin: int, end: int, type_: str):
    res = db.query(Foam).filter((begin <= Foam.ts) & (Foam.ts <= end) & (Foam.block_foam_type == type_)).all()
    return JSONResponse(content=res, status_code=status.HTTP_200_OK)


@app.post('/api/foams')
def add_foam(**params):
    foam = Foam(
        cell=params['cell'],
        parent=params['parent'],
        name=params['name'],
        ts=params['ts'],
        value=params['value'],
        block_client_id=params['block_client_id'],
        block_foam_type=params['block_foam_type'],
        block_place=params['block_place'],
        block_block_id=params['block_block_id'],
        block_batch_number=params['block_batch_number'],
        block_recipe_num=params['block_recipe_num'],
        block_weight=params['block_weight'],
        block_length=params['block_length'],
        block_height=params['block_height']
    )


if __name__ == '__main__':
    print(get_foams(1670000000, 1671000000, ' '))
