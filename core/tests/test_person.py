# -*- coding: utf-8 -*-
import pytest
from core.person import Person, MatchingFlags


def test_if_person_has_no_name_or_phone_raise_error():
    try:
        Person(name='Joe', number=14)
        assert False
    except RuntimeError:
        assert True


def test_passing_non_flag_to_flags_raises_error():
    try:
        Person(name='Samuel', number=20, phone='123', flags=None)
        assert False, 'should not accept flags'
    except TypeError:
        assert True


def test_passing_valid_flag_works():
    person = Person(name='Deere', number=10, phone='911', flags=MatchingFlags.match_all)

    assert MatchingFlags.match_all in person.flags


@pytest.fixture
def person():
    return Person(name='John', number=1, phone='144', email='franz@fritz.at')


def test_adding_person_as_match_works(person):
    other = Person(name='Sepp', number=2, phone='133')

    person.add_match(other)

    assert other in person.matches


def test_adding_something_other_than_person_as_match_fails(person):
    other = object()

    try:
        person.add_match(other)
        assert False
    except TypeError:
        assert True
