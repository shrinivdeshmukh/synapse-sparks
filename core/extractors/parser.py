import yaml
from core.parser import Parser


class ReadParser(Parser):
    def __init__(self, filepath: str):
        self.filepath = filepath
        super().__init__(filepath=filepath)

    @property
    def data(self):
        with open(self.filepath, 'r') as f:
            self.__data = yaml.safe_load(f)
        return self.__data['reader']

    @property
    def table(self):
        return self.data['table']

    @property
    def columns(self):
        columns = self.data['columns']
        if columns:
            self.__columns = ','.join(columns)
        else:
            self.__columns = '*'
        return self.__columns

    @property
    def conditions(self):
        conditions = self.data['conditions']
        if conditions:
            self.__conditions = ' '.join(
                f'{k} {v}' for k, v in conditions.items()) or None
        else:
            self.__conditions = None
        return self.__conditions
