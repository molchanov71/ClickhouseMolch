from . import client


def query_get_distinct_foam_types(loc):
    res = client.query(f'SELECT DISTINCT block_foam_type FROM {loc}.foams WHERE NOT block_foam_type = \'\'').result_rows
    return [tpl[0] for tpl in res]


def query_get_foams_by_time(loc, beg, end, foam_type):
    res = client.query(f"SELECT * FROM Kuznetsk.foams WHERE ts BETWEEN {beg} AND {end} AND "
                       f"block_foam_type = \'{foam_type}\'").result_rows
    if not res:
        return [{
            'cell': '',
            'parent': '',
            'name': '',
            'ts': '',
            'value': '',
            'block_client_id': '',
            'block_foam_type': '',
            'block_place': '',
            'block_block_id': '',
            'block_batch_number': '',
            'block_recipe_num': '',
            'block_weight': '',
            'block_length': '',
            'block_wide_average': '',
            'block_height': ''
        }]
    return res


def query_get_distinct_ts(loc):
    res = client.query(f'SELECT DISTINCT ts FROM {loc}.foams').result_rows
    return [tpl[0] for tpl in res]
