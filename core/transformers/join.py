from core.transformers.parser import TransformationsParser
import pandas as pd
from core.extractors.rdbms.reader import Reader


def transform(df: pd.DataFrame, parser: TransformationsParser) -> pd.DataFrame:
    reader = Reader(parser=parser)
    other_df = reader.read()
    joined_df = df.join(other=other_df, lsuffix='_left', how=parser.join_type)
    return joined_df
