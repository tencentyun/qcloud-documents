Routing table consists of default and custom routing rules, with each of them containing three parameters:

- Destination: Description of the destination network segment (only network segment format is supported. If you wish the destination to be an IP, you can set the mask to 32, for example: 172.16.1.1/32). The destination cannot be the IP segment within the VPC to which the routing table belongs.
- Next hop type: The next hop type for VPC supports "public network gateway", "VPN gateway", "Direct Connect gateway", etc. You need to create such a gateway, otherwise you cannot pull the next hop type;
- Next hop: Specify the next hop gateway to which you'll be redirected.

Each routing tables contains a default local route, which means the interconnection within VPC.

If there are multiple routing rules in a routing table, the order of priority of routing (from high to low) is as follows:

- Traffic within VPC: Match the traffic within VPC first
- Exact match routing: Match the traffic within non-VPC based on the exact-match routing rule
- Public IP: If match fails for all the routing rules, the Internet can be accessed through the public IP
