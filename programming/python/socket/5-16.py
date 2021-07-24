import nmap
nm = nmap.PortScanner()

nm.scan("127.0.0.1", "22")
for host in nm.all_hosts(): # 127.0.0.1
    print("Host : {} {}".format(host, nm["127.0.0.1"].hostname())) # 127.0.0.1 localhost
    print("state: {}".format(nm["127.0.0.1"].state())) # up

for protocol in nm["127.0.0.1"].all_protocols():
    print(f"protocol: {protocol}") # tcp

local_port = list(nm["127.0.0.1"]["tcp"].keys()) # 22
local_port.sort()

for port in local_port:
    print(f"port : {port}") # 22
    print("state: {}".format(nm["127.0.0.1"][protocol][port]["state"])) #close or open

