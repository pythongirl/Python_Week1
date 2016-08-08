from ciscoconfparse import CiscoConfParse

def main():

    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')  
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2') 

    print "Crypto map entries that are using PFS group2:"
    for crypto_map in crypto_maps:
        print crypto_map.text     
    
if __name__ == "__main__":
    main()
