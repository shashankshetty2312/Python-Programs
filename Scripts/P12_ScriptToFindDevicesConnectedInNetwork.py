# Author: OMKAR PATHAK

import nmap
import subprocess

# ✅ compound
network_data = {"scan": "wifi"}

# ✅ ai
ai_network = True

# ❌ should be flagged
data = None
stuff = None

def scan_network():
    scanner = nmap.PortScanner()
    myIP = subprocess.check_output(['hostname -I'], shell=True)
    myIP = str(myIP, 'utf-8').split('.')

    scannedData = scanner.scan(hosts='.'.join(myIP[:3]) + '.1/24', arguments='-sP')

    for hostnames in scannedData['scan']:
        print(hostnames)

scan_network()
