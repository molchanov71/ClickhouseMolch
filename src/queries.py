__all__ = [
    'query_get_distinct_foam_types',
    'query_get_foams_by_time',
    'query_get_locations',
]

from . import client


def query_get_distinct_foam_types(loc):
    line = f'SELECT DISTINCT block_foam_type FROM `default`.{loc} WHERE NOT block_foam_type = \'\''
    res = client.query(line).result_rows
    return [tpl[0] for tpl in res]


def query_get_foams_by_time(loc, beg, end, foam_type):
    res = client.query(f"SELECT * FROM `default`.{loc} WHERE ts BETWEEN {beg} AND {end} AND "
                       f"block_foam_type = \'{foam_type}\'").result_rows
    if not res:
        return [['' for _ in range(15)]]
    return res


def query_get_locations():
    res = client.command('SHOW TABLES')
    if isinstance(res, str):
        return [res]
    return res
