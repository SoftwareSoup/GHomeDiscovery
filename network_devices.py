# filename: network_devices
import os, subprocess, ipaddress

class NetworkList:
    def __init__(self):
        self.devices = []
    def discoverDevices(self, echo_requests = 1):
        subnet = ipaddress.ip_network(u'192.168.1.0/23', strict=False)
        for x in subnet.hosts():
            IP = str(x)
            output = subprocess.call(["ping", '-n', str(echo_requests), '-i', '1', IP])
            if output == 0:
                self.devices.append(IP)
                print(IP + " alive")
            print(IP + " checked" + str(output))
            # TODO resolve device names
            
    # iterate through all hostnames in the subnet mask
    def list_all_devices(self):
        retString = 'The current connected device '

        # Grammar
        if len(self.devices) > 1:
            retString += 's are: '
        else:
            retString += ' is: '

        # Append devices connected
        for s in self.devices:
            retString += s + ', '
        return(retString)
    
    def new_devices(self):
        print("new_devices")
        return("new_devices")
