'''
Created on Sep 26, 2011
@author: dhruvbaldawa
'''
class testClassifier(object):
    '''
    classdocs
    '''
    def __init__(self, training_data, classes):
        '''
        Constructor
        '''
        # The frequency of individual classes
        self.class_frequency = {}

        # The items overview with its frequency in each
        # of the classes
        self.items_overview = {}

        # List of all the classes
        self.classes = classes

        # The training data
        # training_data is a list of instances of trainingElement class
        self.training_data = training_data

        # Probabilities
        self.p_item_class = {}
        self.p_item = {}
        self.p_class = {}

        self.get_training()

    def get_training(self):
        '''
        This method takes training from the training data and computes
        various probability variables p_item_class, p_item, p_class.
        '''
        # Calculating the items and their subsequent classes
        self.class_frequency = dict(zip(self.classes, [0.0]*len(self.classes)))

        # @todo: Optimization by replacing the object methods and properties
        for item in self.training_data:
            if item.get_data() not in self.items_overview:
                self.initialize_item_overview(item.get_data())
                self.initialize_item_probabilities(item.get_data())

            self.mark_item_occurrence(item.get_data(), item.get_class())

    def mark_item_occurrence(self, item, iClass):
        '''
        This method marks occurence of a particular item, and updates
        the probabilities for that particular item.
        '''
        # Update the frequencies of the classes      
        self.items_overview[item]['class'][iClass] += 1.0
        self.items_overview[item]['count'] += 1.0
        self.class_frequency[iClass] += 1.0

        # Update the probabilities
        # p(class|item) = p(class) * p(item|class) / p(item)
        # p(class) = self.class_frequency / len(self.training_data)
        # p(item|class) = self.items_overview[item]['class'] / self.items_overview[item]['count']
        # p(item) = self.items_overview[item]['count'] / len(self.training_data)
        # @todo: Optimization
        self.p_class[iClass] = self.class_frequency[iClass] / len(self.training_data)
        for tClass in self.items_overview[item]['class']:
            self.p_item_class[item][tClass] = self.items_overview[item]['class'][tClass] / self.items_overview[item]['count']
        self.p_item[item] = self.items_overview[item]['count'] / len(self.training_data)

    def initialize_item_overview(self, item):
        '''
        This method is used to initialize the item overview for any item.
        It basically, creates a map with all the classes, and initial count
        set to 0.
        '''
        # Convert the classes list to a dictionary with classes as keys
        # of the dictionary having value 0.0 by default
        self.items_overview[item] = {"class":dict(zip(self.classes, [0.0]*len(self.classes))),
                                     "count":0.0}

    def initialize_item_probabilities(self, item):
        '''
        This method initializes the initial probability for an item.
        It returns a map with keys as classes and values as probabilities.
        All probabilities are default 0.
        '''
        # Convert the classes list to a dictionary with classes as keys
        # of the dictionary having value 0.0 by default
        self.p_item_class[item] = dict(zip(self.classes, [0.0]*len(self.classes)))

    def classify_item(self, item):
        # Predict the various probabilities of a particular item
        # Returns each class and the confidence of the decision
        if item in self.p_item:
            return self.p_item_class[item]
        else:
            # @todo: Change the exception to a special class 'ItemNotFoundException'
            raise Exception("No previous information regarding " + item)

    def item_verdict(self, item):
        # returns the final verdict, that is the final "class" of the item
        classes = self.classify_item(item)
        # @todo: find a better way, but certainly assuming that no class has same probability
        t_max = -1.0

        r_class = None
        for t_class, t_frequency in classes.items():
            if t_max < t_frequency:
                t_max = t_frequency
                r_class = t_class
        return r_class

    def classify_all_items(self, item_list):
        pass

    def __str__(self):
        return "[\n\tclass frequency: " + str(self.class_frequency) + \
            ",\n\titems overview: " + str(self.items_overview) + "\n]"

    def __repr__(self):
        return "[\n\tclass frequency: " + str(self.class_frequency) + \
            ",\n\titems overview: " + str(self.items_overview) + \
            ",\n\tclasses: " + str(self.classes) + \
            ",\n\tp(item): " + str(self.p_item) + \
            ",\n\tp(item|class): " + str(self.p_item_class) + \
            ",\n\tp(class): " + str(self.p_class) + "\n"

