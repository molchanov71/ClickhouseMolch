import csv
import sqlite3


def main():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    with open('kuznetsk_raw_202307251556.csv', mode='r', encoding='utf8') as table:
        reader = csv.reader(table, delimiter=',')
        header = next(reader)
        cur.execute(f'CREATE TABLE t({", ".join(header)})')


if __name__ == '__main__':
    main()
