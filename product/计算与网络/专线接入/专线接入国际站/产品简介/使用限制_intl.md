
| Resource | Limit | Description |
|------|-----|-----|
| Physical Direct Connect/user | 10 | You can apply for higher quota |
| Direct Connect tunnel/Physical Direct Connect | 20 |  |
| Direct Connect gateway/VPC | 1 |  |
| Local IP translation/Direct Connect gateway | 100 | You can apply for higher quota |
| Peer IP translation/Direct Connect gateway | 100 | You can apply for higher quota |
| Number of IPs for local source IP port translation/Direct Connect gateway | 20 | You can apply for higher quota |
| Local destination IP port translation/Direct Connect gateway | 100 | You can apply for higher quota |

Notes about **Direct Connect**:
- When a Direct Connect gateway is created, the contents of IP translation and IP port translation are left empty by default. In this case, neither of them takes effect.
- Direct Connect tunnels support BPG routing and static routing.

Notes about **IP translation**:
- IP address pools cannot fall within the CIDR range of the VPC in which the Direct Connect gateway resides.
- ACL rules for multiple IP address pools cannot overlap to avoid conflicts in network address translation.
- IPs among multiple IP address pools cannot overlap.
- IP address pools only support single IP or consecutive IPs, and /24 IP address range of consecutive IPs should be consistent. For example, `192.168.0.1-192.168.0.6` is supported, but `192.168.0.1-192.168.1.2` not.
- Address pools should not contain broadcasting address (255.255.255.255), Class D address (224.0.0.0-239.255.255.255), or Class E address (240.0.0.0-255.255.255.254).
- The local source IP port translation supports a maximum of 100 IP address pools, and each of them supports a maximum of 20 ACL rules. (Submit a ticket to apply for higher quota if needed.)
- To switch from IP translation to IP port translation, remove the original IP translation rules and refresh the page to edit IP port translation rules.

Notes about **IP port translation**:
- The original IP must fall within the CIDR range of VPC in which the Direct Connect gateway resides.
- The original IP port must be unique. In other words, an IP port in a VPC can only be mapped to one IP port.
- The mapped IP port cannot fall within the CIDR range of the VPC.
- The mapped IP port must be unique. In other words, multiple IP ports in a VPC cannot be mapped to one IP port.
- Original IP or mapped IP should not be broadcasting address (255.255.255.255), Class D address (224.0.0.0-239.255.255.255), Class E address (240.0.0.0-255.255.255.254).
- The local destination IP port translation supports a maximum of 100 IP port mappings. (Submit a ticket to apply for higher quota if needed.)
- If both IP translation and IP port translation are configured, IP translation takes priority in case of any conflict.

