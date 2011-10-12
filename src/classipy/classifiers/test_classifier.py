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
      '''
      This method takes training from the training data and computes
      various probability variables pItemClass, pItem, pClass.
      '''
      # Calculating the items and their subsequent classes
      self.classFrequency = dict(zip(self.classes, [0.0]*len(self.classes)))

      # @todo: Optimization by replacing the object methods and properties
      for item in self.trainingData:
        if item.getData() not in self.itemsOverview:
          self.initializeItemOverview(item.getData())
          self.initializeItemProbabilities(item.getData())

        self.markItemOccurrence(item.getData(), item.getClass())

    def markItemOccurrence(self, item, iClass):
      '''
      This method marks occurence of a particular item, and updates
      the probabilities for that particular item.
      '''
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
      for tClass in self.itemsOverview[item]['class']:
        self.pItemClass[item][tClass] = self.itemsOverview[item]['class'][tClass] / self.itemsOverview[item]['count']
      self.pItem[item] = self.itemsOverview[item]['count'] / len(self.trainingData)

    def initializeItemOverview(self, item):
      '''
      This method is used to initialize the item overview for any item.
      It basically, creates a map with all the classes, and initial count
      set to 0.
      '''
      # Convert the classes list to a dictionary with classes as keys
      # of the dictionary having value 0.0 by default
      self.itemsOverview[item] = {"class":dict(zip(self.classes, [0.0]*len(self.classes))),
                                            "count":0.0}

    def initializeItemProbabilities(self, item):
      '''
      This method initializes the initial probability for an item.
      It returns a map with keys as classes and values as probabilities.
      All probabilities are default 0.
      '''
      # Convert the classes list to a dictionary with classes as keys
      # of the dictionary having value 0.0 by default
      self.pItemClass[item] = dict(zip(self.classes, [0.0]*len(self.classes)))

    def classifyItem(self, item):
      # Predict the various probabilities of a particular item
      # Returns each class and the confidence of the decision
      if item in self.pItem:
        return self.pItemClass[item]
      else:
        # @todo: Change the exception to a special class 'ItemNotFoundException'
        raise Exception("No previous information regarding " + item)
      pass

    def itemVerdict(self, item):
      # returns the final verdict, that is the final "class" of the item
      classes = self.classifyItem(item)
      # @todo: find a better way, but certainly assuming that no class has same probability
      tMax = -1.0

      rClass = None
      for tClass, tFrequency in classes.items():
        if tMax < tFrequency:
          tMax = tFrequency
          rClass = tClass
      return rClass

    def classifyAllItems(self, item_list):
      pass

    def __str__(self):
      return "[\n\tclass frequency: " + str(self.classFrequency) + ",\n\titems overview: " + str(self.itemsOverview) + "\n]"

    def __repr__(self):
      return "[\n\tclass frequency: " + str(self.classFrequency) + \
    ",\n\titems overview: " + str(self.itemsOverview) + \
    ",\n\tclasses: " + str(self.classes) + \
    ",\n\tp(item): " + str(self.pItem) + \
    ",\n\tp(item|class): " + str(self.pItemClass) + \
    ",\n\tp(class): " + str(self.pClass) + "\n"

