from typing import Type
import pandas as pd
from core.utils import checkdir
from os.path import dirname
from core.transformers.parser import TransformationsParser

supported_formats = ['csv', 'json']


def transform(df: pd.DataFrame, parser: TransformationsParser) -> bool:

    if not parser.write_format in supported_formats:
        raise AttributeError(
            f'Only {supported_formats} formats are supported!')
    checkdir(dirname(parser.output_path))
    format = f'to_{parser.write_format.lower()}'
    df_writer = getattr(df, format)
    df_writer(parser.output_path, **parser.writer_properties)
    return True
