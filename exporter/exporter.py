from abc import ABCMeta, abstractmethod


def Exporter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def export_data(self, data):
        pass
