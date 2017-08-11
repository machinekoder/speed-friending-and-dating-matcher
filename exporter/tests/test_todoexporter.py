# -*- coding: utf-8 -*-
import pytest
import people_testdata


@pytest.fixture
def expected_output():
    data = '''
============================
Send to Tobi, tobi@gmail.com, 0123456789 the following message:

Hi Tobi, here are your contacts with people you can reach out to
(people that marked you with an "x" and you marked them with an "x"):

You marked:
3, Mark, mark@mark.com, 0987654321
4, Luisa, 0049123456789

You got marked by:
2, Sara Mustermann, 123456789

Your matches:


You can also find all other contacts here: http://goo.gl/123xyz
or on meetup here: https://www.meetup.com/speed-friending-events/members/
'''
    return data


@pytest.fixture
def testdata():
    return people_testdata.testdata()


@pytest.fixture
def exporter(tmpdir):
    from exporter.todoexporter import TodoExporter
    todo_file = tmpdir.join('todos.txt')
    return TodoExporter(filename=str(todo_file))


def test_creating_todo_string_from_person_object_returns_correct_string(testdata, exporter, expected_output):
    output = exporter._create_person_todo_string(testdata[0])

    assert output == expected_output


def test_writing_output_to_file_works_as_expected(testdata, exporter, expected_output):
    exporter.export_data(testdata)

    with open(exporter._filename, 'rt') as todo_file:
        written = todo_file.read()
        assert expected_output in written
