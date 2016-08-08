
from ciscoconfparse import CiscoConfParse

def main():

    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')  
    crypto_maps = cisco_cfg.find_objects(r'^crypto map CRYPTO')
    for crypto_map in crypto_maps:
        print crypto_map.text     
        for child in crypto_map.children:
            print child.text 
    print

if __name__ == "__main__":
    main()
