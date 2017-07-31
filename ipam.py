## ---------------------------------------------------------------------------
## A suite of functions to interact with Solarwinds IPAM API
## Requires IPAM 4.5 to function. We're currently on 4.3
## DEL - 2017-07-31
## ---------------------------------------------------------------------------

from __future__ import print_function
import jinja2
import csv
import sys
import os.path
import orionsdk
from ipamConfig import IPAM_HOST,IPAM_USER,IPAM_PW

def initialiseIPAM(IPAM_HOST,IPAM_USER,IPAM_PW):
    swis = orionsdk.SwisClient(IPAM_HOST,IPAM_USER,IPAM_PW)
    aliases = swis.invoke('IPAM.SubnetManagement', 'GetFirstAvailableIp', ['10.72.1.0','24'])
    print(aliases)

def getSubnet(IPAM_HOST,IPAM_USER,IPAM_PW):
    #get stuff
    print()

def createSubnet(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()

def reserveIP(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()

def getNextAvailableIP(IPAM_HOST,IPAM_USER,IPAM_PW):
    print()


if __name__ == "__main__":
    initialiseIPAM(IPAM_HOST,IPAM_USER,IPAM_PW)

    