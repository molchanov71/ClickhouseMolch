from __init__ import client


def get_distinct_foam_types(_client):
    res = _client.query('SELECT DISTINCT block_foam_type FROM `default`.NewTable')
    return {tpl[0] for tpl in res.result_rows}


if __name__ == '__main__':
    foam_types = get_distinct_foam_types(client)
    print(*foam_types, sep='\n')
