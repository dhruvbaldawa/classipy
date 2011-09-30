'''
Created on Sep 30, 2011

@author: dhruvbaldawa
'''

class classifierElement(object):
    '''
    classdocs
    '''

    def __init__(self):
      '''
      Constructor
      '''
      self.cClass
      self.cData
      self.classes
      self.pClass = {}
      self.count = 0.0

    def initializeClasses(self, lClass, default = 0.0):
      self.classes = dict(zip(lClass, [default]*len(lClass)))
      self.pClasses = dict(zip(lClass, [0.0]*len(lClass)))

    def occurClass(self, dClass):
      self.classes[dClass] += 1.0
      pass
