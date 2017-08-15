## ---------------------------------------------------------------------------
## A suite of functions to interact with Solarwinds IPAM API
## Requires IPAM 4.5 to function. We're currently on 4.3
## DEL - 2017-07-31
## ---------------------------------------------------------------------------

from __future__ import print_function
import csv
import sys
import os.path
import orionsdk
import ipaddress
from ipamConfig import IPAM_HOST,IPAM_USER,IPAM_PW,SITE_CSV

def initialiseIPAM(IPAM_HOST,IPAM_USER,IPAM_PW):
    swis = orionsdk.SwisClient(IPAM_HOST,IPAM_USER,IPAM_PW)
    #aliases = swis.invoke('IPAM.SubnetManagement', 'GetFirstAvailableIp', ['10.72.1.0','24'])
    #print(aliases)

def getSubnet(IPAM_HOST,IPAM_USER,IPAM_PW):
    #get stuff
    print()

def createSubnet(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()

def reserveIP(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()

def getNextAvailableIP(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()

def buildValuesAccess(SITE_CSV):
    f = open(SITE_CSV, 'rt')
    try:
        reader = csv.DictReader(f)
        for dict_row in reader:
            siteCode = dict_row['siteCode']
            hostName = str(siteCode).upper() + "-FLOOR" +
            #siteSubnet = ipaddr.IPNetwork("10.73.1.0")
            subnetString = '10.' + dict_row['secondOctet'] + '.0.0'
            subnetString = unicode(subnetString,"utf-8")
            octets =subnetString.split(".")
            siteSubnet = ipaddress.ip_network(subnetString)
            vlan2Subnet = octets[0] + "." + octets[1] + ".1.0"
            vlan3Subnet = octets[0] + "." + octets[1] + ".2.0"
            vlan4Subnet = octets[0] + "." + octets[1] + ".3.0"
            vlan5Subnet = octets[0] + "." + octets[1] + ".4.0"
            vlan6Subnet = octets[0] + "." + octets[1] + ".5.0"
            vlan7Subnet = octets[0] + "." + octets[1] + ".6.0"
            vlan8Subnet = octets[0] + "." + octets[1] + ".7.0"

            for vlan in range(2,8):


            print (siteCode,siteSubnet,vlan2Subnet)

            #outputtext = template.render(dict_row)

            #config_filename = CONFIGS_DIR + dict_row['hostName'] + '-config'
            #with open(config_filename, 'w') as config_file:
            #    config_file.write(outputtext)
            #print("wrote file: %s" % config_filename)

    finally:
        f.close()

if __name__ == "__main__":
    initialiseIPAM(IPAM_HOST,IPAM_USER,IPAM_PW)
    buildValuesAccess(SITE_CSV)

