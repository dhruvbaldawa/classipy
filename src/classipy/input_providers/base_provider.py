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
    def __init__(self, dataStream):
        '''
        Constructor
        '''
        self.dataStream = dataStream
        self.classes = []
        self.data = []
        self.inputList = []
    
    @abstractmethod
    def getClasses(self):
        pass
    
    @abstractmethod
    def parseDataStream(self):
        return self.dataStream
        