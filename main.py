import os
import sys


def main():
    return os.system('uvicorn src.api:app --reload --port 8080')


if __name__ == '__main__':
    sys.exit(main())
