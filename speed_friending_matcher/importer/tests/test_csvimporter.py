# coding=utf-8
import pytest
from speed_friending_matcher.importer.csvimporter import CsvImporter
from speed_friending_matcher.core.person import MatchingFlags


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


@pytest.fixture
def csv_file_with_nobody_interested_in(tmpdir):
    data = '''#;Name;Email;Phone;All;Interested
1;Tobi;tobi@gmail.com;123456789;0;
'''
    csv_file = tmpdir.join('test.csv')
    csv_file.write(data)
    return str(csv_file)


def test_importing_correct_csv_data_works(correct_csv_file):
    importer = CsvImporter(filename=correct_csv_file)

    data = importer.import_data()

    assert len(data) == 5
    person = data[0]
    assert person.name == 'Tobi'
    assert person.email == 'tobi@gmail.com'
    assert person.phone == '123456789'
    assert person.number == 1
    assert person.flags == MatchingFlags.no_flags
    assert person.marked_numbers == {2, 3}
    person = data[1]
    assert person.flags == MatchingFlags.match_all


def test_importing_csv_file_without_header_raises_error(csv_file_without_header):
    importer = CsvImporter(filename=csv_file_without_header)

    with pytest.raises(ValueError):
        importer.import_data()


def test_importing_csv_file_with_incomplete_field_raises_error(
    csv_file_with_incomplete_field
):
    importer = CsvImporter(filename=csv_file_with_incomplete_field)

    with pytest.raises(ValueError):
        importer.import_data()


def test_importing_csv_file_with_empty_interested_in_field_does_not_throw_error(
    csv_file_with_nobody_interested_in
):
    importer = CsvImporter(filename=csv_file_with_nobody_interested_in)

    data = importer.import_data()

    assert len(data) == 1
    person = data[0]
    assert person.marked_numbers == set()
