import importlib


class ModuleRegistry:
    def __init__(self):
        pass

    def get_transformer(self, modname):
        try:
            mod_name = f'core.transformers.{modname}'
            mod = importlib.import_module(mod_name)
            return mod
        except Exception as e:
            raise e

    def get_sink(self, modname):
        try:
            mod_name = f'core.sink.{modname}'
            mod = importlib.import_module(mod_name)
            return mod
        except Exception as e:
            raise e

    def get_reader(self, modname):
        try:
            mod_name = f'core.extractors.{modname}.reader'
            mod = importlib.import_module(mod_name)
            return mod
        except Exception as e:
            raise e
