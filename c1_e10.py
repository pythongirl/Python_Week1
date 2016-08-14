# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
'''

from ciscoconfparse import CiscoConfParse

def main():

    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')  
    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES') 

    print "\nThe entry(s) not using AES is/are:"
    for crypto_map in crypto_maps:
        print crypto_map.text     

    print "\nCorresponding transform set for the entry:"
    for child in crypto_map.children:
        if "transform" in child.text:
            print child
    
if __name__ == "__main__":
    main()

