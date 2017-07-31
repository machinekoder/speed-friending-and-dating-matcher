# -*- coding: utf-8 -*-
from aenum import Flag


class MatchingFlags(Flag):
    no_flags = 0
    match_all = 1


class Person(object):
    def __init__(self, name, number, flags=MatchingFlags.no_flags, email=None, phone=None):
        if not email and not phone:
            raise RuntimeError('%s has no email or phone' % name)

        if type(flags) is not MatchingFlags:
            raise TypeError('Must use MatchingOptions')

        self._name = name
        self._email = email
        self._phone = phone
        self._flags = flags
        self._interested_in = set()
        self._matches = set()

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
    def match_all(self):
        return self._match_all

    def add_match(self, person):
        if not type(person) is Person:
            raise TypeError('Can only match a person')

        self.matches.add(person)

    def clear_matches(self):
        self.matches.clear()

    @property
    def matches(self):
        return self._matches

    def add_interest(self, person):
        if not type(person) is Person:
            raise TypeError('Can only match a person')

        self._interested_in.add(person)

    def clear_interests(self):
        self._interested_in.clear()

    @property
    def interested_in(self):
        return self._interested_in

    @property
    def flags(self):
        return self._flags
