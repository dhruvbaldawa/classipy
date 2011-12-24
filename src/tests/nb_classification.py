'''
Created on 17-Dec-2011

@author: dhruv
'''
import unittest
from classipy.input_providers.test_provider import testProvider
from classipy.classifiers.nb_classifier import NaiveBayesianClassifier

class TestClassification(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSingleClassification(self):
        input_data = {"foo":"yes",
                      "bar":"yes",
                      "foo":"no",
                      "foo":"no",
                      "bar":"yes",
                      "bar":"no",
                      "monty":"yes",
                      "python":"no",
                      "monty":"yes",
                      "monty":"no",
                      "python":"no",
                      "python":"no",
                      "foo":"yes",
                      "foo":"no"}

        document = ["foo", "bar", "foo", "foo", "bar", "bar", "monty",
                    "python", "monty", "monty", "python", "python",
                    "foo", "foo"]
        classes = ["yes", "yes", "no", "no", "yes", "no", "yes", "no", "yes", "no",
                   "no", "no", "yes", "no"]

        classifier = NaiveBayesianClassifier(document, classes)
        classifier.train()
        self.assertEqual(classifier.predict("foo"), "no", "Equality checking for 'foo'")
        self.assertEqual(classifier.predict("bar"), "yes", "Equality checking for 'bar'")
        self.assertEqual(classifier.predict("monty"), "yes", "Equality checking for 'monty'")
        self.assertEqual(classifier.predict("python"), "no", "Equality checking for 'python'")

    def testMovieSongClassification(self):
        input_data = {"a perfect world":"movie",
                      "a perfect day":"song",
                      "my perfect woman":"movie",
                      "electric storm":"song",
                      "pretty woman":"movie",
                      "another rainy day":"song"}

        classifier = NaiveBayesianClassifier(input_data.keys(), input_data.values())
        classifier.train()

        self.assertEqual(classifier.predict("perfect storm"), "song")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
