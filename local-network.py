
import psutil
from rich import print, repr
from rich.table import Table
from rich.console import Console



import re

def get_size(val):
    return val/1024/1024/1024

def get_network():
    network = []
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        
        for address in interface_addresses:
            interface = {}
            interface['name']= interface_name
            interface['family'] = re.sub(r'AddressFamily.','', str(address.family) )
            interface['address'] = address.address
            interface['netmask'] = address.netmask
            interface['broadcast'] = address.broadcast
            interface['ptp'] = address.ptp

            network.append(interface)
    return network


def network_table():
    table = Table(title="Network")
    networtk = get_network()
    for i in networtk:
        if i['family'] == 'AF_INET':
            table.add_row(i['name'], i['address'],i['family'])

    return table

console = Console()
console.print(network_table())
# get IO statistics since boot
net_io = psutil.net_io_counters()
# print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
# print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")