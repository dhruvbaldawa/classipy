'''
Created on Sep 26, 2011
@author: dhruvbaldawa
'''
class testClassifier(object):
    '''
    classdocs
    '''
    def __init__(self, trainingData, classes):
      '''
      Constructor
      '''
      # The frequency of individual classes
      self.classFrequency = {}

      # The items overview with its frequency in each
      # of the classes
      self.itemsOverview = {}

      # List of all the classes
      self.classes = classes

      # The training data
      # trainingData is a list of instances of trainingElement class
      self.trainingData = trainingData

      # Probabilities
      self.pItemClass = {}
      self.pItem = {}
      self.pClass = {}

      self.getTraining()

    def getTraining(self):
      # Calculating the items and their subsequent classes
      self.classFrequency = dict(zip(self.classes, [0.0]*len(self.classes)))

      # @todo: Optimization by replacing the object methods and properties
      for item in self.trainingData:
        if item.getData() not in self.itemsOverview:
          self.initializeItemOverview(item.getData())
          self.initializeItemProbabilities(item.getData())

        self.markItemOccurrence(item.getData(), item.getClass())

    def markItemOccurrence(self, item, iClass):
      # Update the frequencies of the classes      
      self.itemsOverview[item]['class'][iClass] += 1.0
      self.itemsOverview[item]['count'] += 1.0
      self.classFrequency[iClass] += 1.0

      # Update the probabilities
      # p(class|item) = p(class) * p(item|class) / p(item)
      # p(class) = self.classFrequency / len(self.trainingData)
      # p(item|class) = self.itemsOverview[item]['class'] / self.itemsOverview[item]['count']
      # p(item) = self.itemsOverview[item]['count'] / len(self.trainingData)
      # @todo: Optimization
      self.pClass[iClass] = self.classFrequency[iClass] / len(self.trainingData)
      self.pItemClass[item][iClass] = self.itemsOverview[item]['class'][iClass] / self.itemsOverview[item]['count']
      self.pItem[item] = self.itemsOverview[item]['count'] / len(self.trainingData)

    def initializeItemOverview(self, item):
      # Convert the classes list to a dictionary with classes as keys
      # of the dictionary having value 0.0 by default
      self.itemsOverview[item] = {"class":dict(zip(self.classes, [0.0]*len(self.classes))),
                                            "count":0.0}

    def initializeItemProbabilities(self, item):
      # Convert the classes list to a dictionary with classes as keys
      # of the dictionary having value 0.0 by default
      self.pItemClass[item] = dict(zip(self.classes, [0.0]*len(self.classes)))

    def itemVerdict(self, item):
      pass

    def allVerdict(self):
      pass

    def classifiedItem(self, item):
      pass

    def classifiedItems(self):
      pass

    def __str__(self):
      return "[class frequency: " + str(self.classFrequency) + ",\nitems overview: " + str(self.itemsOverview) + "]"

    def __repr__(self):
      return "<class frequency: " + str(self.classFrequency) + \
    ",\n\titems overview: " + str(self.itemsOverview) + \
    ",\n\tclasses: " + str(self.classes) + \
    ",\n\tp(item): " + str(self.pItem) + \
    ",\n\tp(item|class): " + str(self.pItemClass) + \
    ",\n\tp(class): " + str(self.pClass) + ">"
