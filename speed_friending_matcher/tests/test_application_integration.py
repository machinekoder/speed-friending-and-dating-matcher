# -*- coding: utf-8 -*-
import os

import pytest
from speed_friending_matcher.application import Application

TEST_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def output_dir(tmpdir):
    return str(tmpdir.join(''))


def test_application_integration(output_dir):
    input_arguments = 'csv:{}/../../example/sample.csv'.format(TEST_PATH)
    output_arguments = 'todo:%s/todo.txt' % output_dir
    matchmaker = 'simple'

    app = Application(input_arguments, output_arguments, matchmaker)
    app.process()
