from abc import ABCMeta, abstractmethod


def Importer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def import_data(self):
        pass
