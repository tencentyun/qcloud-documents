## 1. Physical Direct Connect

Physical Direct Connect is a physical line used to connect Tencent Cloud with local IDCs. You can establish a network connection between your IDC and Tencent Cloud Direct Connect network access point through a third-party network service provider.

## 2. Direct Connect tunnel

- Direct Connect tunnel is the network link segmentation of the physical Direct Connect.
- You can create Direct Connect tunnels connected to different Direct Connect gateways to achieve interconnection between local IDCs and multiple VPCs.

## 3. Direct Connect gateway

Direct Connect gateway is the entry for establishing Direct Connect tunnels between VPCs and physical Direct Connects. A VPC supports at most 2 Direct Connect gateways (one supports NAT and the other not). Direct Connect tunnels can be established between a Direct Connect gateway and multiple physical Direct Connects to deploy a hybrid cloud connected with multiple regions.

## 4. Network Address Translation (NAT)

NAT is used to solve the conflict between IPs at the two ends of a Direct Connect during the establishment of hybrid cloud connection. You can configure NAT rules on the direct connect gateway. NAT is divided into IP translation and IP port translation.

### IP translation

IP translation means to convert the original IP to a new IP to achieve network interconnection, which includes **local IP translation** and **peer IP translation**.

IP translation does not distinguish whether the access is initiated by the source or the destination. The mapped IP can either access or be accessed by the peer.

#### Local IP translation

Refers to mapping the original VPC IP to a new IP to achieve interconnection with the Direct Connect peer. You can configure more than one local IP translation rules and the network ACL for each local IP translation rule. The network ACL supports configuring source port, destination IP, and destination port. NAT rules are only valid for the network requests meeting the ACL restrictions. The local IP translation does not impose any limit on the direction of network requests, which can be the active access of VPC to Direct Connect peer or vice versa.

![](https://main.qcloudimg.com/raw/08fd80670fef1446546f38924ae8f4b5.png)

**Example:**
If IP A 192.168.0.3 in a VPC is mapped to IP B 10.100.0.3, the network packet source IP of the active access of IP A to the Direct Connect peer is automatically changed to 10.100.0.3, and all network packets accessing 10.100.0.3 from the Direct Connect peer is automatically directed to IP A 192.168.0.3.

#### Peer IP translation

Refers to mapping the original IP of user's IDC to a new IP to achieve interconnection with the VPC IP. Unlike local IP translation, peer IP translation does not support network ACL restrictions. Therefore, the peer IP translation rules will be valid for all Direct Connect tunnel peers once configured. The peer IP translation does not impose any limit on the direction of network requests, which can be the active access of VPC to Direct Connect peer or vice versa.

![](https://main.qcloudimg.com/raw/7fa1066f5cdd2d0e80fd502ebe823aba.png)

**Example:**
If the peer IP D 10.0.0.3 of a Direct Connect is mapped to IP C 172.16.0.3, the network packet source IP of the active access of IP D 10.0.0.3 to VPC is automatically changed to IP C 172.16.0.3, and all network packets accessing IP C 172.16.0.3 from VPC is automatically directed to the Direct Connect peer IP D 10.0.0.3.

<font color="red">Note</font>:
1. After the local or peer IP translation is configured, the Direct Connect gateway only sends the routing of translated IP to the Direct Connect peer, so the Direct Connect peer cannot be pinged via the original IP without being configured with local or peer IP translation. However, the Direct Connect gateway cannot be used as a professional network firewall. If you need a higher level of network protection, configure security groups and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.
2. If the Direct Connect gateway is also configured with peer IP translation, the **destination IP** in the ACL rule of the local source IP port translation should be the **mapping IP of the peer IP translation**, instead of the original IP.


### IP Port translation
IP port translation means to map the original IP port to a new IP to achieve network interconnection, which includes **local source IP port translation** and **local destination IP port translation**.

IP port translation has a direction. The source IP port translation is used to make outgoing access, and the destination IP port translation is used for the active access by the peer.

#### Local source IP port translation

Refers to accessing a user IDC of the Direct Connect peer using the random port of a random IP within the specified IP pool during the outgoing access of a VPC IP via the Direct Connect gateway. The local source IP port translation supports configuring ACL rules. Only the network access conforming to ACL rules can match the address pool forwarding rules. By configuring different ACL rules for an address pool, you can flexibly configure NAT rules for multiple third-party access.

![](https://main.qcloudimg.com/raw/c67a4d3dc064d3e96f6c63a0cdb4e5dc.png)

The local source IP port translation only supports the network access request initiated by the VPC. To actively access the IP port in the VPC, the Direct Connect peer needs to configure the local destination IP port translation. For the local source IP port translation, the network request initiated by the VPC is stateful, without considering the network response packet.

**Example:**
The VPC C IP address range 172.16.0.0/16 connects the third-party banks A and B via the Direct Connect. The peer IP address range of bank A is 10.0.0.0/28, requiring the connected IP address range 192.168.0.0/28, and the peer IP address range of bank B is 10.1.0.0/28, requiring the connected IP address range 192.168.1.0/28. You can configure two local source IP port translation rules as follows:

Address pool A 192.168.0.1-192.168.0.15; ACL rule A; Source IP 172.16.0.0/16; Destination IP 10.0.0.0/28; Destination port ALL
Address pool B 192.168.1.1-192.168.1.15; ACL rule B; Source IP 172.16.0.0/16; Destination IP 10.1.0.0/28; Destination port ALL

The VPC network request for active access to A or B will be translated into the random port of corresponding address pool based on ACL rule A or B to access the appropriate Direct Connect tunnel.

#### Local destination IP port translation
Refers to an approach for the active access of Direct Connect peer to VPC. By mapping the specified port of the specified IP in the VPC to the new IP and port, the Direct Connect peer can only communicate with the specified IP port in the VPC by accessing to the mapped IP port. Other IP ports will not be exposed to the Direct Connect peer.

![](https://main.qcloudimg.com/raw/780545de2940ed777027e2d3e3273ddd.png)

ACL rule is not applicable to the local destination IP port translation, so the IP port translation rule will be valid for all Direct Connect tunnels connected with the Direct Connect gateway. The local destination IP port translation is only valid for the active access of Direct Connect tunnel peer to the VPC. If the VPC needs to make an active access to the Direct Connect peer, the local source IP port translation can be configured. For the local destination IP port translation, the network request is stateful, without considering the network response packet.

**Example**
For the VPC C IP address range 172.16.0.0/16, if you only want to enable several ports for the active access of Direct Connect peer, you can configure as follows:
Mapping A; Original IP port 172.16.0.1:80; Mapped IP port 10.0.0.1:80
Mapping B; Original IP port 172.16.0.0:8080; Mapped IP port 10.0.0.1:8080
The Direct Connect peer can access the ports 10.0.0.1:80 and 10.0.0.1:8080 to achieve the active access to the ports 172.16.0.1:80 and 172.16.0.0:8080 in the VPC.

<font color="red">Note</font>:
1. After the local source or destination IP port translation is configured, the Direct Connect gateway only sends the routing of translated IP port to the Direct Connect peer, so the local IP port without being configured with the local source or destination IP port translation cannot initiate requests actively or receive requests passively. However, the Direct Connect gateway cannot be used as a professional network firewall. If you need a higher level of network protection, configure security groups and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.
2. When both IP translation and IP port translation are configured, it will match IP translation first. If there is no match for the IP translation, it will match IP port translation.
3. If the Direct Connect gateway is also configured with peer IP translation, the **destination IP** in the ACL rule of the local source IP port translation should be the **mapping IP of the peer IP translation**, instead of the original IP.

