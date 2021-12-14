from yaml import safe_load


class Parser:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    @property
    def all_data(self):
        with open(self.filepath, 'r') as f:
            data = safe_load(f)
        return data

    @property
    def source(self):
        return self.all_data['source']

    @property
    def table_schema(self):
        table_dict = dict()
        for table, columns in self.all_data['tables'].items():
            for column, schema in columns.items():
                table_dict.update({table: schema})
        return table_dict
