from main import client


def get_foam_in_time(_client, beg, end, foam_type):
    res = _client.query(f"SELECT * FROM `default`.NewTable WHERE ts BETWEEN {beg} AND {end} AND "
                        f"block_foam_type = \'{foam_type}\'")
    return res.result_rows


if __name__ == '__main__':
    foams = get_foam_in_time(client, 1669961644, 1671819940, 'SPG1620_01_1505-(')
    print(*('\t'.join(map(str, foam)) for foam in foams), sep='\n')
