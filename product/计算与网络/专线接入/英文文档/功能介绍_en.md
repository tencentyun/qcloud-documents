## 1. Physical Direct Connect

Physical Direct Connect refers to the physical connection between Tencent Cloud and local data center. You can establish a network connection between your data center and Tencent Cloud through a third-party ISP.

## 2. Direct Connect Tunnel

- Direct Connect tunnel is the network link segmentation of the physical Direct Connect.
- You can create the Direct Connect tunnels connected to different Direct Connect gateways to achieve the interconnection between the local data center and multiple VPCs.

## 3.	Direct Connect Gateway

Direct Connect gateway is the entry for establishing a Direct Connect tunnel between VPC and Direct Connect. VPC supports at most 2 Direct Connect gateways (One with NAT support and the other without NAT support). With Direct Connect gateway, Direct Connect tunnel to multiple physical Direct Connects can be established to implement a hybrid cloud deployment connecting to multi-locations.

## 4. Network Address Translation (NAT)

Network address translation is a solution for solving IP conflict at both ends of the Direct Connect when connecting hybrid cloud. You can configure network address translation rules on Direct Connect gateway. Network address translation (NAT) consists of IP translation and IP port translation.

### IP translation

IP translation refers to the original IP translation to the new IP to achieve network interconnection, which includes local IP translation and peer IP translation.

IP translation does not distinguish whether the access is initiated by the source or the destination. The mapped IP can either actively access to the peer, or be accessed actively from the peer.

#### Local IP translation

Refers to the original VPC IP mapping to new IP in VPC, and the latter is used to achieve the interconnection with the Direct Connect peer . You can configure more than one local IP translation rules and the network ACL for each local IP translation rule. The network ACL supports the configuration for source port, destination IP, and destination port. NAT rules will take effect only for network requests that meet ACL restriction requirements. The local IP translation does not impose any limit on the direction of network requests, which could be the active access of VPC to Direct Connect peer or vice versa.

![](//mccdn.qcloud.com/img5695b647a827a.png)

**Example:**
IP A 192.168.0.3 is mapped to IP B 10.100.0.3 within a VPC. The network packet source IP of the active access of IP A to Direct Connect peer will automatically change to 10.100.0.3. All network packets returned from the Direct Connect peer to 10.100.0.3 will be automatically redirected to IP A 192.168.0.3.

#### Peer IP translation

Refers to the original IP of user IDC mapping to new IP to achieve interconnection with the VPC IP with new IP. Unlike local IP translation, peer IP translation does not support network ACL restrictions. Therefore, once peer IP translation rules are configured, they will take effect and apply to all Direct Connect tunnels. For the peer IP translation, there is no restriction on the direction of network request, supporting both the active access of VPC to Direct Connect peer, and the active access of Direct Connect peer to VPC.

![](//mccdn.qcloud.com/img5695b66d18c7e.png)

**Example:**
IP D 10.0.0.3 of Direct Connect pee is mapped to IP C 172.16.0.3. The network packet source IP of the active access of IP D 10.0.0.3 to VPC will automatically change to IP C 172.16.0.3. All network packets returned from VPC to IP C 172.16.0.3 will be automatically redirected to Direct Connect peer IP D 10.0.0.3.
Note:
1) After configuring the local or the peer IP translation, the Direct Connect gateway will only send the routing of translated IP down to the Direct Connect peer, so the original IP without the local or the peer IP translation can not ping the Direct Connect peer successfully. But the Direct Connect gateway cannot replace the professional network firewall. If you need advanced network protection, please configure security group and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.
2) When the Direct Connect gateway is also configured with "Peer IP Translation", the **Destination IP** of the ACL rule for local source IP port translation should be **the mapping IP of peer IP translation**, instead of the original IP.


### IP Port Translation
IP port translation refers to the original IP port mapping to the new IP port to achieve network interconnection, which includes **local source IP port translation** and **local destination IP port translation**.

IP port translation has direction. The source IP port translation accesses externally and the destination IP port translation is accessed by the peer.

#### Local source IP port translation

Refers to the accesses to user IDC of Direct Connect peer using random port of random IP within specified IP pool when VPC IP access externally via the Direct Connect gateway. The local source IP port translation supports the configuration of ACL rules. Only the network access in accordance with ACL rules can be matched with the address pool forwarding rules. By configuring different ACL rules for an address pool, you can flexibly configure Network Address Translation rules for multiple third-party accesses.

![](//mccdn.qcloud.com/img5695b7459a76c.png)

The local source IP port translation only supports the network access request initiated by the VPC. If the Direct Connect peer needs to initiate active access to the IP port in VPC, it requires additional configuration for the local destination IP port translation. For the local source IP port translation, the network request initiated by VPC is for the stateful connection, so there is no need to consider the network return packet.

**Example:**
Suppose VPC with C network segment 172.16.0.0/16 connecting with the third-party banks A and B via Direct Connect, where the peer network segment of bank A is 10.0.0.0/28, requiring the interacted network segment 192.168.0.0/28, and the peer network segment of bank B is 10.1.0.0/28, requiring the interacted network segment 192.168.1.0/28. You can configure two local source IP port translations as follows:

Address Pool  A 192.168.0.1-192.168.0.15   ACL Rule A Source IP 172.16.0.0/16 Destination IP 10.0.0.0/28 Destination Port ALL
Address Pool B   192.168.1.1-192.168.1.15  ACL Rule B Source IP 172.16.0.0/16 Destination IP 10.1.0.0/28 Destination Port ALL

The VPC network request for active access to A or B will be translated into the random port of corresponding address pool based on ACL rule A or B to access the appropriate Direct Connect tunnel.

#### Local destination IP port translation
Local destination IP port translation refers to an approach for the active access of Direct Connect peer to VPC. By mapping the specified port of specified IP in the VPC to the new port of new IP, the Direct Connect peer can only communicate with the specified IP port in VPC by accessing to the mapped IP port, with other IP ports not exposed to the Direct Connect peer:

![](//mccdn.qcloud.com/img5695b8081dc51.png)

ACL rule is not applicable to the local destination IP port translation, so the IP port translation rule will be valid for all Direct Connect tunnels connected with the Direct Connect gateway. The local destination IP port translation will only be valid for the active access of Direct Connect tunnel peer to the VPC. If the VPC needs to have the active access to the Direct Connect peer, you can configure the local source IP port translation. For the local destination IP port translation, the network request is for the stateful connection, so there is no need to consider the network return packet.

**Example**
For VPC with C network segment 172.16.0.0/16, if you only want to open several ports for the active access of Direct Connect peer, you can make configuration as follows:
Mapping A: the original IP port 172.16.0.1:80, the mapped IP port 10.0.0.1:80
Mapping B: the original IP port 172.16.0.0:8080, the mapped IP port 10.0.0.1:8080
Then the Direct Connect peer can have the active access to Port 10.0.0.1:80 and 10.0.0.1:8080, to achieve the active access to Port 172.16.0.1:80 and 172.16.0.0:8080 in the VPC.

Note:
After configuring the local source or destination IP port translation, the Direct Connect gateway will only send the routing of translated IP port down to the Direct Connect peer, so the local IP port without relative configuration can not initiate requests actively or receive requests passively. But the Direct Connect gateway cannot replace the professional network firewall. If you need advanced network protection, please configure security group and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.
2) When both IP translation and IP port translation are configured, IP translation will be matched with first, and if there is no match, then IP port translation will be matched with.
3) When the Direct Connect gateway is also configured with "Peer IP Translation", the **Destination IP** of the ACL rule for local source IP port translation should be **the mapping IP of peer IP translation**, instead of the original IP.

