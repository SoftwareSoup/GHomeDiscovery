# filename: network_devices
import os, subprocess, ipaddress

class NetworkList:
    def __init__(self):
        self.devices = []
        self.deviceNames = []
    def discoverDevices(self, echo_requests = 1):
        subnet = ipaddress.ip_network(u'192.168.1.0/23', strict=False)
        for x in subnet.hosts():
            IP = str(x)
            if '192.168.0' in IP:
                continue
            output = subprocess.call(["ping", '-n', str(echo_requests), '-i', '1', '-w', '1', IP])
            if output == 0:
                self.devices.append(IP)
                print(IP + " alive")                
            # TODO resolve device names
        for x in self.devices:
            output = subprocess.Popen(["ping", '-n', str(echo_requests), '-a', '-w', '1', x], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
            print(output)
            if '[' not in output:
                self.deviceNames.append('Unknown Device')
                continue
            newString = ""
            for index, char in enumerate(output):
                if index <= 9:
                    continue
                if char == ' ' or index > 23:
                    break;
                newString += char
            if newString != "":
                self.deviceNames.append(newString)
    # iterate through all hostnames in the subnet mask
    def list_all_devices(self):
        retString = 'The current connected device '

        # Grammar
        if len(self.deviceNames) > 1:
            retString += 's are: '
        else:
            retString += ' is: '

        # Append devices connected
        for s in self.deviceNames:
            retString += s + ', '
        return(retString)
    
    def new_devices(self):
        print("new_devices")
        return("new_devices")
