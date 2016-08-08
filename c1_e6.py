#!/usr/bin/env python

'''
Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
'''
import json
import yaml

#List with at least a dict with 2 key value pairs
my_list = [0, 1, 2, 3, 4, 5, 6, 'switches', 'routers', {'ip': '1.1.1.1', 'attrib': ['cpu', 'memory', 'capacity'], 'os': 'veos'}]
print "My list is: ", my_list


#Write this list out to a file using YAML format
with open ('test_class1_yaml.yaml', 'w') as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
#print "Yaml format is: ", (yaml.dump(my_list, default_flow_style=False))


#Write this list out to a file using JSON format
with open ('test_class1_json.json', 'w') as f:
    f.write(json.dumps(my_list))
#print "JSON format is: ", (json.dumps(my_list))

#
