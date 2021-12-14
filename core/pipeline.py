from core.extractors import ReadParser
from core.transformers import TransformationsParser
from core.registry import ModuleRegistry
import pandas as pd


class Pipeline:

    def __init__(self, filepath: str) -> None:
        self.rparser = ReadParser(filepath=filepath)
        self.tparser = TransformationsParser(filepath=filepath)
        self.registry = ModuleRegistry()

    def read(self) -> pd.DataFrame:
        source = self.rparser.source.split('/')[0]
        reader_mod = self.registry.get_reader(source)
        reader = reader_mod.Reader(parser=self.rparser)
        df = reader.read()
        return df

    def transform(self, df: pd.DataFrame):
        if not self.tparser.transformations_order:
            return pd.DataFrame()
        for transformation in self.tparser.transformations_order:
            transformer = self.registry.get_transformer(transformation)
            df = transformer.transform(df, parser=self.tparser)
        return df

    def run(self) -> pd.DataFrame:
        df = self.read()
        result_df = self.transform(df)
        return result_df
