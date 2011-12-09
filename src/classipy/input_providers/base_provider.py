'''
Created on Sep 25, 2011

@author: dhruvbaldawa
'''
from abc import ABCMeta, abstractmethod
class baseProvider:
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    def __init__(self, data_stream):
        '''
        Constructor
        '''
        self.data_stream = data_stream
        self.classes = []
        self.data = []
        self.input_list = []

    @abstractmethod
    def get_classes(self):
        pass

    @abstractmethod
    def parse_data_stream(self):
        return self.data_stream
