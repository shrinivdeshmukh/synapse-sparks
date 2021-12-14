from .connector import Connector
from core.extractors import ReadParser
from os import getenv
from typing import Optional
from core.utils import sql_to_pd
import pandas as pd
from core.utils import dtype_map


class Reader(Connector):

    def __init__(self, parser: ReadParser) -> None:
        self.url = getenv('DB_URL', 'sqlite://testdb')
        self.parser = parser
        super().__init__(self.url)

    def read(self) -> pd.DataFrame:
        df = sql_to_pd(self.build_query(), self.engine)
        df = self.impose_schema(df)
        return df

    def build_query(self) -> str:
        query = f'SELECT {self.parser.columns} FROM {self.parser.table} {self.parser.conditions}'
        return query

    def impose_schema(self, df: pd.DataFrame) -> pd.DataFrame:
        python_schema_dict = dict()
        for column in self.parser.table_schema[self.parser.table]:
            python_schema_dict.update(
                {column['name']: dtype_map[column['type']]})
        dtype_df = df.astype(dtype=python_schema_dict)
        return dtype_df
