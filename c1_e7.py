#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure 
that is returned.
'''

import yaml
import json
from pprint import pprint as pp

my_list = [0, 1, 2, 3, 4, 5, 6, 'switches', 'routers', {'ip': '1.1.1.1', 'attrib': ['cpu', 'memory', 'capacity'], 'os': 'veos'}]
print "My list is: ", my_list

#reading YAML file and pretty print the output
with open ("test_class1_yaml.yaml") as f:
    print "\nYAML format\n"
    pp(yaml.load(f))
    
#reading JSON file and pretty print the output
with open ("test_class1_json.json") as f:
    print "\nJSON format\n"
    pp(json.load(f))



