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
    def __init__(self, data_stream):
        '''
        Constructor
        '''
        self.data_stream = data_stream
        self.parse_data_stream()

    def get_classes(self):
        '''
        @return the list of all the classes from the provider
        '''
        return self.classes

    def parse_data_stream(self):
        '''
        @return nothing
        '''
        # Creates a set for all the classes
        t_classes = Set()

        # Initialize data as list of input elements
        self.data = []

        # @todo: Optimization of the loop
        for item in self.data_stream:
            # @todo: Use lists automatically, if provided and don't tokenize
            # Tokenize the string
            token_list = self.tokenize(item["data"])

            for token in token_list:
                # Create an inputElement class and append it to the data list
                self.data.append(trainingElement(token, item["class"]))
            # Add the class to the set
            t_classes.add(item["class"])

        # Convert the set to a list
        self.classes = list(t_classes)

    def tokenize(self, data):
        token_list = data.lower().split()
        return token_list

    def __str__(self):
        return "[classes: " + str(self.classes) + ",\ndata: " + str(self.data) + "]"

    def __repr__(self):
        return "<classes: " + str(self.classes) + ",\ndata: " + str(self.data) + ">"
