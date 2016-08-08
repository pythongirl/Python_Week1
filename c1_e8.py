# -*- coding: utf-8 -*- 
#!/usr/bin/env python

'''
Write a Python program using ciscoconfparse that parses this config file. Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
'''

from ciscoconfparse import CiscoConfParse

def main():

    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')  
    crypto_maps = cisco_cfg.find_objects(r'^crypto map CRYPTO')
    
    print "\nAll the crypto map entries in the file: "
    for crypto_map in crypto_maps:
        print crypto_map.text     
        print "\nEach crypto map entries children: "
        for child in crypto_map.children:
            print child.text 
    print

if __name__ == "__main__":
    main()
