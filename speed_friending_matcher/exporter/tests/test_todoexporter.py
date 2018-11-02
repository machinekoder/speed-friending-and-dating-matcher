# -*- coding: utf-8 -*-
import pytest
from . import people_testdata


@pytest.fixture
def expected_output1():
    data = '''\
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


Your cliques:


You can also find all other contacts here: http://goo.gl/123xyz
or on meetup here: https://www.meetup.com/speed-friending-events/members/

'''
    return data


@pytest.fixture
def expected_output2():
    data = '''\
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


Your cliques:
TEAM 1: 4 friends
1, Tobi, tobi@gmail.com, 0123456789
2, Sara Mustermann, 123456789
3, Mark, mark@mark.com, 0987654321
4, Luisa, 0049123456789

TEAM 2: 3 friends
1, Tobi, tobi@gmail.com, 0123456789
2, Sara Mustermann, 123456789
3, Mark, mark@mark.com, 0987654321


You can also find all other contacts here: http://goo.gl/123xyz
or on meetup here: https://www.meetup.com/speed-friending-events/members/

'''
    return data


@pytest.fixture
def testdata():
    basedata = people_testdata.testdata()
    tobi, sara, mark, luisa = basedata
    tobi.results.clique = {sara, luisa, mark}
    mark.results.clique = {tobi, sara}
    return basedata


@pytest.fixture
def exporter(tmpdir):
    from speed_friending_matcher.exporter.todoexporter import TodoExporter

    todo_file = tmpdir.join('todos.txt')
    return TodoExporter(output_filename=str(todo_file))


def test_creating_todo_string_from_person_object_returns_correct_string(
    testdata, exporter, expected_output1
):
    output = exporter._create_person_todo_string(testdata[0], [])

    assert output == expected_output1


def test_writing_output_to_file_works_as_expected(testdata, exporter, expected_output2):
    exporter.export_data(testdata)

    with open(exporter._filename, 'rt') as todo_file:
        written = todo_file.read()

    separator = '============================'
    written = written.split(separator)
    assert (separator + written[1]) == expected_output2
