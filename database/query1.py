from main import client


def get_distinct_foam_type(_client):
    res = _client.query('SELECT DISTINCT block_foam_type FROM `default`.NewTable')
    print(*(tpl[0] for tpl in res.result_rows), sep='\n')


if __name__ == '__main__':
    get_distinct_foam_type(client)
