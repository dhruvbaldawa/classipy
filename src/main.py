'''
Created on Sep 25, 2011
@author: dhruvbaldawa
'''
from classipy.input_providers.test_provider import testProvider
from classipy.classifiers.test_classifier import testClassifier
import pprint

if __name__ == '__main__':
    """
    t_input = "bar"
    ans_"class":{}
    for item in p_class:
        ans_class[item] = (p_item[t_input][item]/len(input_list)) * (p_class[item]/len(input_list))
    
    print ans_class
    """

    pp = pprint.PrettyPrinter()
    input_data = [{"data":"foo", "class":"yes"}, {"data":"bar", "class":"yes"}, {"data":"foo", "class":"no"}, {"data":"foo", "class":"no"}, {"data":"bar", "class":"yes"}, {"data":"bar", "class":"no"}, {"data":"monty", "class":"yes"}, {"data":"python", "class":"no"}, {"data":"monty", "class":"yes"}, {"data":"monty", "class":"no"}, {"data":"python", "class":"no"}, {"data":"python", "class":"no"}, {"data":"foo", "class":"yes"}, {"data":"foo", "class":"no"}]
    provider = testProvider(input_data)
    classifier = testClassifier(provider.data, provider.classes)
    pp.pprint(classifier)
