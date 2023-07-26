from main import client


def get_foam_in_time(_client):
    ts_min = _client.query('SELECT MIN(ts) FROM `default`.NewTable').first_item['min(ts)']
    ts_max = _client.query('SELECT MAX(ts) FROM `default`.NewTable').first_item['max(ts)']

    ts_begin = int(input(f"Введите начальную отметку (От {ts_min} до {ts_max}): "))
    while ts_begin not in range(ts_min, ts_max + 1):
        print('Начальная отметка не находится в заданном промежутке, попробуйте ещё раз!')
        ts_begin = int(input(f"Введите начальную отметку (От {ts_min} до {ts_max}): "))

    ts_end = int(input(f"Введите конечную отметку (От {ts_min} до {ts_max}): "))
    while ts_end < ts_begin or ts_end not in range(ts_min, ts_max + 1):
        if ts_end < ts_begin:
            print('Конечная отметка не может быть раньше начальной!')
        else:
            print('Конечная отметка не находится в заданном промежутке, попробуйте ещё раз!')
        ts_end = int(input(f"Введите конечную отметку (От {ts_min} до {ts_max}): "))

    foam_types = tuple(tpl[0] for tpl in
                       _client.query('SELECT DISTINCT block_foam_type FROM `default`.NewTable').result_rows)
    foam_type = input(f"Введите тип пены (Варианты: {', '.join(foam_types)}): ")
    while foam_type not in foam_types:
        print('Такого типа пены нет, попробуйте ещё раз!')
        foam_type = input(f"Введите тип пены (Варианты: {', '.join(foam_types)}): ")

    query_text = f"SELECT * FROM `default`.NewTable WHERE (ts BETWEEN {ts_begin} AND {ts_end}) AND " \
                 f"block_foam_type = '{foam_type}'"
    res = _client.query(query_text)
    print(*('\t'.join(map(str, i)) for i in res.result_rows), sep='\n')


if __name__ == '__main__':
    get_foam_in_time(client)
