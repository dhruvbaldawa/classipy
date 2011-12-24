from collections import Counter
from math import log

# @todo: methods to change the laplace smoothing constant

class NaiveBayesianClassifier:


    def __init__(self, documents, classes):
        """
        @param documents: is a list of lists.
        @param classes: is the list of classes for corresponding documents
        ["text1","text2","text3",..]
        ["class1","class1","class2",..]
        """
        # Vocabulary of all the words 
        self.vocabulary = []
        # The list of various training documents
        self.documents = documents
        # The list of classes corresponding to documents
        self.classes = classes
        # Important !!! each document should have a class
        assert len(self.documents) == len(self.classes)

        # Initialization of variables
        # A dict with class as key and value as list of all documents of that class
        self.class_lists = {}
        # Prior probabilities of each class
        self.prior = {}
        # Conditional probability of a term t given a class c
        self.cond_prob = {}
        # Laplace Smoothing constant
        self.K = 1

    def train(self):
        """
        Performs the training for the classifier given the documents list
        @todo: support for persistent data
        @todo: support for incremental addition to the training set
        """
        # Extract the vocabulary from the documents
        self.vocabulary = self.extract_vocabulary(self.documents)
        N = len(self.documents)

        # Combine classes and its documents
        for i in range(N):
            if self.classes[i] not in self.class_lists.keys():
                self.class_lists[self.classes[i]] = []

            self.class_lists[self.classes[i]].append(self.documents[i])

        # Perform the training
        for class_, items in self.class_lists.iteritems():
            # Calculate the prior probability of the class
            Nc = len(items)
            self.prior[class_] = Nc / float(N)

            # Tokenize the items and count the number of occurrences
            tokens = self.tokenize(items)
            counter = Counter()

            # Its magic !! Calculates frequencies for all the tokens
            counter.update(tokens)

            # Calculate the conditional probabilities
            for token, value in counter.iteritems():
                if not self.cond_prob.has_key(token):
                    x = self.class_lists.keys()
                    K = self.K
                    # Initialize the conditional probability for all the classes
                    self.cond_prob[token] = dict(
                                                 zip(x,
                                                    [K / float(len(tokens) + K * len(self.vocabulary))]*len(x)))
                # Calculate the conditional probability.
                self.cond_prob[token][class_] = (value + K) / float((len(tokens) + K * len(self.vocabulary)))

    def predict(self, document):
        """
        Performs the prediction given document
        """
        # Tokenize the document
        tokens = self.tokenize(document)

        # Remove the tokens not in the vocabulary
        # @todo: Optimize this !
        for token in tokens:
            if token not in self.vocabulary:
                tokens.remove(token)

        # Initialization for finding scores !
        # @todo: return scores
        # @todo: return probabilities
        score = {}
        max_score = float("-inf")
        max_class = None

        # Calculate scores for all the classes and find the best
        for class_ in self.class_lists.keys():
            score[class_] = log(self.prior[class_])

            for token in tokens:
                score[class_] += log(self.cond_prob[token][class_])

            if score[class_] > max_score:
                max_score = score[class_]
                max_class = class_

        return max_class

    def extract_vocabulary(self, document):
        """
        @param document: the document to extract vocabularies from
        @return: a list of vocabulary elements 
        """
        if type(document) == list:
            # process the list
            s = set()
            t_document = document[:]
            for item in t_document:
                s = s.union(self._extract_vocabulary_single(item))
            return list(s)

        elif type(document) == str:
            return self._extract_vocabulary_single(document)

        else:
            raise TypeError
        pass

    def _extract_vocabulary_single(self, in_string):
        """
        @param string: the string to extract vocabulary from
        @return: the list of vocabulary elements
        """
        token_list = set(in_string.lower().split())
        return list(token_list)

    def tokenize(self, input_):
        """
        Tokenize the given string/lift
        @todo: perform stemming and other processing
        """
        if type(input_) == str:
            return self._tokenize_single(input_)

        elif type(input_) == list:
            l = []
            for item in input_:
                l.extend(self._tokenize_single(item))
            return l

        else:
            raise TypeError

    def _tokenize_single(self, input_):
        """
        Tokenize the given input string
        """
        return input_.lower().split()
