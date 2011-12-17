'''
Created on 17-Dec-2011

@author: dhruv
'''
import unittest
from classipy.input_providers.test_provider import testProvider
from classipy.classifiers.test_classifier import testClassifier

class TestClassification(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSingleClassification(self):
        input_data = [{"data":"foo", "class":"yes"},
                      {"data":"bar", "class":"yes"},
                      {"data":"foo", "class":"no"},
                      {"data":"foo", "class":"no"},
                      {"data":"bar", "class":"yes"},
                      {"data":"bar", "class":"no"},
                      {"data":"monty", "class":"yes"},
                      {"data":"python", "class":"no"},
                      {"data":"monty", "class":"yes"},
                      {"data":"monty", "class":"no"},
                      {"data":"python", "class":"no"},
                      {"data":"python", "class":"no"},
                      {"data":"foo", "class":"yes"},
                      {"data":"foo", "class":"no"}]

        provider = testProvider(input_data)
        classifier = testClassifier(provider.data, provider.classes)

        self.assertEqual(classifier.item_verdict("foo"), "no", "Equality checking for 'foo'")
        self.assertEqual(classifier.item_verdict("bar"), "yes", "Equality checking for 'bar'")
        self.assertEqual(classifier.item_verdict("monty"), "yes", "Equality checking for 'monty'")
        self.assertEqual(classifier.item_verdict("python"), "no", "Equality checking for 'python'")
        self.assertRaises(Exception, classifier.item_verdict, "apple", "Exception checking for 'apple'")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
