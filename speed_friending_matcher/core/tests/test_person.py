# -*- coding: utf-8 -*-
from speed_friending_matcher.core.person import Person, MatchingFlags


def test_if_person_has_no_name_or_phone_do_not_raise_error():
    try:
        Person(name='Joe', number=14, marked_numbers=set())
        assert True
    except RuntimeError:
        assert False


def test_passing_non_flag_to_flags_raises_error():
    try:
        Person(name='Samuel', number=20, phone='123', flags=None, marked_numbers=set())
        assert False, 'should not accept flags'
    except TypeError:
        assert True


def test_passing_valid_flag_works():
    person = Person(
        name='Deere',
        number=10,
        phone='911',
        flags=MatchingFlags.match_all,
        marked_numbers=set(),
    )

    assert MatchingFlags.match_all in person.flags


def test_passing_something_other_than_set_as_marked_numbers_raises_error():
    try:
        Person(name='Foo', number=1, phone='123457', marked_numbers=[1, 2, 3])
        assert False
    except TypeError:
        assert True
