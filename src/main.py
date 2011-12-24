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
    input_data = [{"data":"a perfect world", "class":"movie"},
                  {"data":"a perfect day", "class":"song"},
                  {"data":"my perfect woman", "class":"movie"},
                  {"data":"electric storm", "class":"song"},
                  {"data":"pretty woman", "class":"movie"},
                  {"data":"another rainy day", "class":"song"}]
    provider = testProvider(input_data)
    print provider
    classifier = testClassifier(provider.data, provider.classes)
    pp.pprint(classifier)
    pp.pprint("my name is anthony: " + str(classifier.classify_item("anthony hello negative message")))

