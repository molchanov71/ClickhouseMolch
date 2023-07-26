from src.database.query1 import *
from src.database.query2 import *


def main():
    print(*get_distinct_foam_types(client), sep='\n')
    print(*('\t'.join(map(str, foam)) for foam in
            get_foam_in_time(client, 1669961644, 1671819940, 'SPG1620_01_1505-(')), sep='\n')


if __name__ == '__main__':
    main()
