import numpy as np
import pandas as pd


def load(data, path='./src/xlsx/res.xlsx'):
    df = pd.DataFrame(np.array(data))
    df.columns = ['cell', 'parent', 'name', 'ts', 'value', 'block_client_id', 'block_foam_type', 'block_place',
                  'block_block_id', 'block_batch_number', 'block_recipe_num', 'block_weight', 'block_length',
                  'block_wide_average', 'block_height']
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='book 1')
    writer.close()


if __name__ == '__main__':
    table_path = 'xlsx/res.xlsx'
    load(table_path)
