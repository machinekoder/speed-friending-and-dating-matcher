# coding=utf-8
from abc import ABCMeta, abstractmethod


class Exporter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def export_data(self, data):
        pass
