import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_CONNECT_URL = 'clickhouse://default:@localhost/Kuznetsk'
engine = sa.create_engine(SQLALCHEMY_CONNECT_URL)
Base = declarative_base()


class Foam(Base, SerializerMixin):
    __tablename__ = 'foams'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    cell = sa.Column(sa.String, nullable=True)
    parent = sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String, nullable=True)
    ts = sa.Column(sa.Integer)
    value = sa.Column(sa.Integer)
    block_client_id = sa.Column(sa.Integer)
    block_foam_type = sa.Column(sa.String, nullable=True)
    block_place = sa.Column(sa.String, nullable=True)
    block_block_id = sa.Column(sa.Integer)
    block_batch_number = sa.Column(sa.Integer)
    block_recipe_num = sa.Column(sa.Integer)
    block_weight = sa.Column(sa.Integer)
    block_length = sa.Column(sa.Integer)
    block_wide_average = sa.Column(sa.Integer)
    block_height = sa.Column(sa.Integer)
