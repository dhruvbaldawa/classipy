'''
Created on Sep 25, 2011
@author: dhruvbaldawa
'''
from classipy.input_providers.base_provider import baseProvider
from classipy.training_element import trainingElement
from sets import Set

class testProvider(baseProvider):
    '''
    A test provider class
    '''
    def __init__(self, dataStream):
        '''
        Constructor
        '''
        self.dataStream = dataStream
        self.parseDataStream()

    def getClasses(self):
        '''
        @return the list of all the classes from the provider
        '''
        return self.classes

    def parseDataStream(self):
        '''
        @return nothing
        '''
        # Creates a set for all the classes
        tClasses = Set()

        # Initialize data as list of input elements
        self.data = []

        # @todo: Optimization of the loop
        for item in self.dataStream:
            # Create an inputElement class and append it to the data list
            self.data.append(trainingElement(item["data"], item["class"]))
            # Add the class to the set
            tClasses.add(item["class"])

        # Convert the set to a list
        self.classes = list(tClasses)

    def __str__(self):
      return "[classes: " + str(self.classes) + ",\ndata: " + str(self.data) + "]"

    def __repr__(self):
      return "<classes: " + str(self.classes) + ",\ndata: " + str(self.data) + ">"
