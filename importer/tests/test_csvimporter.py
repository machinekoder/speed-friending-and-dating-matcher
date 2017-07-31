import pytest
from importer.csvimporter import CsvImporter


@pytest.fixture
def correct_csv_file(tmpdir):
    data = '''#;Name;Email;Phone;All;Interested
1;Tobi;tobi@gmail.com;123456789;0;2,3
2;Luisa;;49123456789;1;5,1
3;Mark;mark@mark.com;987654321;0;2,4,5
4;Sara Mustermann;;123456789;1;1,2,3
5;Olli G;olli@hotmail.com;;1;1
'''
    csv_file = tmpdir.join('test.csv')
    csv_file.write(data)
    return str(csv_file)


@pytest.fixture
def csv_file_without_header(tmpdir):
    data = '''1;Tobi;tobi@gmail.com;123456789;0;2,3
2;Luisa;;49123456789;1;5,1
'''
    csv_file = tmpdir.join('test.csv')
    csv_file.write(data)
    return str(csv_file)


@pytest.fixture
def csv_file_with_incomplete_field(tmpdir):
    data = '''#;Name;Email;Phone;All;Interested
1;Tobi;tobi@gmail.com;123456789;0;2,3
5;Olli G;olli@hotmail.com;
'''
    csv_file = tmpdir.join('test.csv')
    csv_file.write(data)
    return str(csv_file)


def test_importing_correct_csv_data_works(correct_csv_file):
    importer = CsvImporter(filename=correct_csv_file)

    data = importer.import_data()

    assert len(data) == 5
    assert data[0].name == 'Tobi'


def test_importing_csv_file_without_header_raises_error(csv_file_without_header):
    importer = CsvImporter(filename=csv_file_without_header)

    try:
        importer.import_data()
        assert False
    except ValueError:
        assert True


def test_importing_csv_file_with_incomplete_field_raises_error(csv_file_with_incomplete_field):
    importer = CsvImporter(filename=csv_file_with_incomplete_field)

    try:
        importer.import_data()
        assert False
    except ValueError:
        assert True
