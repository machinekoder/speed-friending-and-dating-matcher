# -*- coding: utf-8 -*-
import pytest
from . import people_testdata


@pytest.fixture
def expected_output():
    data = '''\
Following cliques have been found:

TEAM 1: 3 friends
1, Tobi, tobi@gmail.com, 0123456789
2, Sara Mustermann, 123456789
3, Mark, mark@mark.com, 0987654321
'''
    return data


@pytest.fixture
def testdata():
    basedata = people_testdata.testdata()
    tobi, sara, mark, luisa = basedata
    tobi.results.clique = {sara, mark}
    sara.results.clique = {tobi, mark}
    mark.results.clique = {tobi, sara}
    luisa.results.clique = {tobi}
    return basedata


@pytest.fixture
def exporter(tmpdir):
    from speed_friending_matcher.exporter.cliqueexporter import CliqueExporter

    todo_file = tmpdir.join('clique.txt')
    return CliqueExporter(output_filename=str(todo_file))


def test_writing_output_to_file_works_as_expected(testdata, exporter, expected_output):
    exporter.export_data(testdata)

    with open(exporter._filename, 'rt') as f:
        written = f.read()
        assert written == expected_output
