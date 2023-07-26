import clickhouse_connect


def main():
    client = clickhouse_connect.get_client(host='localhost', port=8123)
    res = client.query('SELECT DISTINCT block_foam_type FROM `default`.NewTable')
    print(*(tpl[0] for tpl in res.result_rows), sep='\n')


if __name__ == '__main__':
    main()
