# -*- coding: utf-8 -*-
import pytest
from core.person import Person


@pytest.fixture
def testdata():
    data = []
    tobi = Person(name='Tobi', number=1, email='tobi@gmail.com', phone='0123456789', marked_numbers=set())
    sara = Person(name='Sara Mustermann', number=2, email='', phone='123456789', marked_numbers=set())
    mark = Person(name='Mark', number=3, email='mark@mark.com', phone='0987654321', marked_numbers=set())
    luisa = Person(name='Luisa', number=4, email='', phone='0049123456789', marked_numbers=set())
    tobi.results.add_marked_by_me(mark)
    tobi.results.add_marked_by_me(luisa)
    tobi.results.add_marked_me(sara)
    data.append(tobi)
    data.append(sara)
    data.append(mark)
    data.append(luisa)
    return data
