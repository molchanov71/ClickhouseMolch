import numpy as np
import pandas as pd
from __init__ import client
from database.query2 import get_foam_in_time


def load(_client, _path):
    data = get_foam_in_time(client, 1669961644, 1671819940, 'SPG1620_01_1505-(')
    df = pd.DataFrame(np.array(data))
    df.columns = ['cell', 'parent', 'name', 'ts', 'value', 'block_client_id', 'block_foam_type', 'block_place',
                  'block_block_id', 'block_batch_number', 'block_recipe_num', 'block_weight', 'block_length',
                  'block_wide_average', 'block_height']
    writer = pd.ExcelWriter(_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='book 1')
    writer.close()


if __name__ == '__main__':
    path = 'xlsx/res.xlsx'
    load(client, path)
