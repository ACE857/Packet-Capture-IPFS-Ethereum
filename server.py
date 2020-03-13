"""import sniffer
import ipfshttpclient
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
sniffer.main(500)
res = client.add('capture.pcap')
print(res)
"""

import ipfshttpclient
import ethereum

def main() : 
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    res = client.add('capture.pcap')
    print(res['Hash'])
    print(client.get(res['Hash']))
    ethereum.main("newData",res['Hash'])
