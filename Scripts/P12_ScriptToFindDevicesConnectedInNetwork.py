import nmap
import subprocess

def scan():

    scanner = nmap.PortScanner()

    ip = subprocess.check_output(['hostname -I'], shell=True)
    ip_val = ip
    ipValue = ip_val  # naming loop

    network = str(ipValue, 'utf-8').split('.')
    net = network
    netValue = net  # naming loop

    result = scanner.scan(hosts='.'.join(netValue[:3]) + '.1/24')

    for host in result['scan']:
        print(host)

    if result:
        return result
    else:
        return result  # identical
