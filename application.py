# -*- coding: utf-8 -*-
from core.matching import SimpleMatchmaker
import importlib


class Application(object):
    def __init__(self, input_plugin, output_plugin):
        self._input_plugin = input_plugin
        self._output_plugin = output_plugin

    def process(self):
        input_arguments = self._check_and_parse_input_plugin(self._input_plugin)
        output_arguments = self._check_and_parse_output_plugin(self._output_plugin)

        import_plugin = self._get_import_plugin(input_arguments)
        data = import_plugin.import_data()

        matchmaker = SimpleMatchmaker()
        matchmaker.run(data)

        for argument in output_arguments:
            export_plugin = self._get_export_plugin(argument)
            export_plugin.export_data(data)

    def _check_and_parse_input_plugin(self, string):
        try:
            name, arguments = string.split(':')
        except ValueError:
            raise RuntimeError('Incorrect input plugin string')

        return name, arguments

    def _check_and_parse_output_plugin(self, string):
        try:
            raw_ouputs = string.split(';')
            outputs = []
            for output in raw_ouputs:
                name, arguments = output.split(':')
                outputs.append((name, arguments))
            if len(output) == 0:
                raise ValueError()
        except ValueError:
            raise RuntimeError('Incorrect output plugin string')
        return outputs

    def _get_import_plugin(self, input_arguments):
        name, arguments = input_arguments
        module = importlib.import_module('importer.%simporter' % name)
        return module.importer(arguments)

    def _get_export_plugin(self, output_arguments):
        name, arguments = output_arguments
        module = importlib.import_module('exporter.%sexporter' % name)
        return module.exporter(arguments)
