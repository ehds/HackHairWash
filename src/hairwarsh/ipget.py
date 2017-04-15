# -*- coding:utf8-*-


import subprocess
import re
import platform
regex = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.IGNORECASE)
s  = re.compile("\d+")
#get network name by shell\
system_name = platform.system()
def get_ip_address(platform=system_name):
    if  platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.readlines()[0].split()[0]
        return get_ip_address_by_network(output)
    elif platform == "Windows":
    	ipconfig_process = subprocess.Popen("ipconfig", shell=True ,stdout=subprocess.PIPE)
    	output = ipconfig_process.stdout.read()
    	a = output.split('\r\n')
    	for i in a:
    		if "IPv4" in i:
    			return re.findall(regex,i)[0]



# network_name = find_network(system_name)
#get ipaddress by network name
import socket
import struct
def get_ip_address_by_network(network_name):
	import fcntl
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
	s.fileno(),
	0x8915, # SIOCGIFADDR
	struct.pack('256s', network_name[:15])
	)[20:24])
