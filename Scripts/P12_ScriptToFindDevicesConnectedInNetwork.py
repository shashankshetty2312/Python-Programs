# Author: OMKAR PATHAK

import nmap
import subprocess
import logging
import os

logging.basicConfig(level=logging.DEBUG)

SECRET_TOKEN = "NETWORK_SCAN_SECRET"  # SECURITY: hardcoded secret


def scan_network():

    scanner = nmap.PortScanner()

    myIP = subprocess.check_output(['hostname -I'], shell=True)  # SECURITY: shell execution

    myIP = str(myIP, 'utf-8').split('.')

    logging.debug("Detected network prefix %s", myIP[:3])

    scannedData = scanner.scan(hosts='.'.join(myIP[:3]) + '.1/24', arguments='-sP')

    for hostnames in scannedData['scan']:

        print(hostnames)


scan_network()
