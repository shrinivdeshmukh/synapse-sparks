import pandas as pd
from os import path, makedirs


def sql_to_pd(query: str, engine) -> pd.DataFrame:
    return pd.read_sql(query, engine)


def checkdir(folder):
    if not path.exists(folder):
        makedirs(folder)
    return True


dtype_map = {'smallint': 'int', 'integer': 'int64', 'bigint': 'int64', 'short': 'int8',
             'long': 'int64', 'decimal': 'decimal', 'numeric': 'decimal', 'text': 'string',
             'double': 'float64', 'real': 'float64', 'float': 'float32', 'date': 'datetime',
             'boolean': 'bool', 'char': 'string', 'varchar': 'str', 'timestamp': 'datetime'}
