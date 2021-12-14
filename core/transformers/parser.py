from yaml import safe_load
from core.parser import Parser


class TransformationsParser(Parser):

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        super().__init__(filepath=filepath)

    @property
    def join_data(self):
        return self.all_data['transformations']['join']

    @property
    def writer_data(self):
        return self.all_data['transformations']['writer']

    @property
    def source(self):
        return self.join_data['table']

    @property
    def table(self):
        return self.join_data['from']

    @property
    def columns(self):
        columns = self.join_data['select']
        if columns:
            self.__columns = ','.join(columns)
        else:
            self.__columns = '*'
        return self.__columns

    @property
    def join_type(self):
        return self.join_data['how']

    @property
    def join_on(self):
        return self.join_data['with']

    @property
    def conditions(self):
        conditions = self.join_data.get('conditions', None)
        if conditions:
            self.__conditions = ' '.join(
                f'{k} {v}' for k, v in conditions.items()) or None
        else:
            self.__conditions = None
        return self.__conditions

    @property
    def output_path(self):
        return self.writer_data['output_path']

    @property
    def write_format(self):
        return self.writer_data['format']

    @property
    def writer_properties(self):
        exclude_keys = {'output_path', 'format'}
        return {x: self.writer_data[x] for x in self.writer_data if x not in exclude_keys}

    @property
    def transformations_order(self):
        return self.all_data.get('transformations_order', None)
