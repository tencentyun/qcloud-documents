Tencent Cloud DNSPod is a world-leading domain name resolution platform with 65 cloud cluster nodes in China and 12 cloud cluster nodes outside China. Each server is able to perform up to 10 million resolutions per second. We provide domain name resolution service for over 6.5 million domain names, process more than 21 billion DNS requests every day, and successfully prevent over 2,000 DNS attacks every month.

Multiple nodes in each cluster can provide users with nearby access points for DNS requests and implement complete remote disaster recovery mechanism.

Meanwhile, resolutions within clusters can achieve synchronization within seconds. When a record is modified on WEB, it will be immediately (1-5 seconds) synchronized to all backend DNS clusters and take effect within seconds at DNSPod. (Recursive DNS is controlled by TTL configuration, thus the actual effective time for end users depends on the TTL value configured in domain name resolution record)

Different service packages use different clusters for resolution, and the corresponding DNS addresses for different clusters are also different:

| DNS Service Package | DNS Address | Remark |
|---|---|---|
| Free DNS Address | f1g1ns1.dnspod.net/f1g1ns2.dnspod.net | 10 corresponding codes |
| Individual Professional | ns3.dnsv2.com/ns4.dnsv2.com | 12 corresponding nodes |
| Enterprise Basic | ns3.dnsv3.com/ns4.dnsv3.com | 14 corresponding nodes |
| Enterprise Standard | ns3.dnsv4.com/ns4.dnsv4.com | 18 corresponding nodes |
| Enterprise Ultimate | ns3.dnsv5.com/ns4.dnsv5.com | 22 corresponding nodes |

