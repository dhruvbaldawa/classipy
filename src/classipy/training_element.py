'''
Created on Sep 25, 2011
@author: dhruvbaldawa
'''

class trainingElement(object):
    '''
    This is the input training data element class.
    '''
    def __init__(self, data, dClass):
        '''
        @param data: the data element
        @param dClass: the class of current data
        @return: nothing
        '''
        self.data = data
        self.dClass = dClass
    
    # 
    def getData(self):
        '''
        @return: the data in the element
        '''
        return self.data
    
    def getClass(self):
        '''
        @return: the class of data element
        '''
        return self.dClass
    
    def __str__(self):
        return "{data: %s,\n class: %s}" % (self.data, self.dClass)
    
    def __repr__(self):
        return "{data: %s,class: %s}" % (self.data, self.dClass)