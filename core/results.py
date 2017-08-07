# -*- coding: utf-8 -*-


class Results(object):
    def __init__(self):
        self._marked_by_me = set()
        self._marked_me = set()
        self._matches = set()

    def clear(self):
        self._marked_by_me.clear()
        self._marked_me.clear()
        self._matches.clear()

    def add_marked_by_me(self, person):
        self._marked_by_me.add(person)

    def add_marked_me(self, person):
        self._marked_me.add(person)

    def add_match(self, person):
        self._matches.add(person)

    @property
    def marked_by_me(self):
        return self._marked_by_me

    @property
    def marked_me(self):
        return self._marked_me

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, data):
        self._matches = data
