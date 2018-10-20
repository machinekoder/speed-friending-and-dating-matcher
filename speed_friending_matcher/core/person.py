# -*- coding: utf-8 -*-
from aenum import Flag
from .results import Results


class MatchingFlags(Flag):
    no_flags = 0
    match_all = 1


class Person(object):
    def __init__(
        self,
        name,
        number,
        marked_numbers,
        flags=MatchingFlags.no_flags,
        email=None,
        phone=None,
    ):
        if type(flags) is not MatchingFlags:
            raise TypeError('Must use MatchingOptions')

        if type(marked_numbers) is not set:
            raise TypeError('marked_numbers must be a set')

        self._number = number
        self._name = name
        self._email = email
        self._phone = phone
        self._flags = flags
        self._marked_numbers = marked_numbers
        self._matches = set()
        self._results = Results()

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @property
    def matches(self):
        return self._matches

    @property
    def marked_numbers(self):
        return self._marked_numbers

    @property
    def flags(self):
        return self._flags

    @property
    def results(self):
        return self._results

    def __repr__(self):
        return 'Person (name: %s, number: %s, marked_numbers: %s)' % (
            self._name,
            self._number,
            self._marked_numbers,
        )
