
| Resource | Restriction | Description |
|------|-----|-----|
| Physical Direct Connect / User | 10 | |
| Direct Connect Tunnel / Physical Direct Connect | 10 | |
| Direct Connect Gateway / Virtual Private Cloud | 1 | |
| Local IP Translation / Direct Connect Gateway | 100 | You can apply for higher quota. |
| Peer IP Translation / Direct Connect Gateway | 100 | You can apply for higher quota. |
| Number of IPs for Local Source IP Port Translation / Direct Connect Gateway | 20 | You can apply for higher quota. |
| Local Destination IP Port Translation / Direct Connect Gateway | 100 | You can apply for higher quota. |

As for **Direct Connect**, you need to understand:
- When the Direct Connect gateway is created, the IP translation and IP port translation contents are empty by default, where neither the IP translation or IP port translation is effective.
- Direct Connect tunnel supports BPG route and static route.

As for **IP translation**, you need to understand:
- The IP address pool can not be within the CIDR range of VPC to which the Direct Connect gateway belongs.
- ACL rules for multiple IP address pools should not overlap. Otherwise, this will cause network address translation conflicts.
- IPs between multiple IP address pools can not overlap.
- IP address pool only supports individual IP or consecutive IPs, and /24 network segment of consecutive IP should be consistent, that is, `192.168.0.1~192.168.0.6` is supported but `192.168.0.1~192.168.1.2` not.
- Address pool should not contain broadcast address (255.255.255.255), Class D address (224.0.0.0~239.255.255.255), or Class E address (240.0.0.0~255.255.255.254).
- The maximum address pools of 100 is supported for local source IP port translation, with 20 ACL rules at a maximum for each pool (the quota can be increased by making a ticket if needed)
- If you need to switch from IP translation to IP port translation, please clear the original IP translation rule, refresh the page and then you can edit the IP port translation rule.

As for **IP port translation**, you need to understand:
- The original IP must be within the CIDR range of VPC to which the Direct Connect gateway belongs
- The original IP port should be unique, that is, the same IP port within the VPC can only be mapped to one IP port
- The mapped IP port can not be within the CIDR range of VPC
- Mapped IP Port is unique and can not be replicated. That means multiple IP ports in a VPC can't be mapped to the same IP port
- Original IP or mapped IP should not be broadcast address (255.255.255.255), Class D address (224.0.0.0~239.255.255.255), Class E address (240.0.0.0~255.255.255.254)
- The maximum IP port mappings of 100 is supported for local destination IP port translation (the quota can be increased by making a ticket if needed)
- If both IP translation and IP port translation are configured, IP translation will be matched with first if any conflicts.
