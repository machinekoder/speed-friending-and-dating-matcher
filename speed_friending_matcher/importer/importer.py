# coding=utf-8
from abc import ABCMeta, abstractmethod


class Importer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def import_data(self):
        pass
