# -*- coding: utf-8 -*-
import pytest
from . import people_testdata
from openpyxl import load_workbook


@pytest.fixture
def testdata():
    return people_testdata.testdata()


@pytest.fixture
def exporter(tmpdir):
    from speed_friending_matcher.exporter.onexlsxexporter import OneXlsxExporter

    test_file = tmpdir.join('test.xlsx')
    return OneXlsxExporter(filename=str(test_file))


def test_exporting_test_data_works_as_expected(exporter, testdata):
    exporter.export_data(testdata)

    workbook = load_workbook(exporter._filename)
    assert len(workbook.worksheets) == 1
    worksheet = workbook.worksheets[0]
    assert worksheet.title == 'Contacts'
    assert worksheet['A2'].value == 1
    assert worksheet['A3'].value == 2
    assert worksheet['B3'].value == 'Sara Mustermann'
    assert worksheet['C2'].value == 'tobi@gmail.com'
    assert worksheet['D3'].value == '123456789'
    assert worksheet['D4'].value is None
    assert worksheet['E5'].value == 'all'
    assert worksheet['E4'].value == 'not all'
    assert worksheet['H2'].value == 'x'
    assert worksheet['F2'].value is None
