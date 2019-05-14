## Product Overview
Direct Connect provides a fast and secure approach to connect Tencent Cloud with local data centers. Users can have access to Tencent Cloud computing resources in multiple regions in one go using a physical direct connection line, to achieve a flexible and reliable hybrid cloud deployment.

## Components
Direct Connect consists of three parts: physical Direct Connect, Direct Connect tunnel and Direct Connect gateway.
1) **Physical Direct Connect**: The physical line to connect Tencent Cloud with local data centers, which can be established by users upon communication with the ISP, or by Tencent Cloud. Physical Direct Connect supports connection via dual-line hot backup, dual-line connection point power supply, and complete isolation of network tunnel.
2) **Direct Connect tunnel**: The network link segmentation of the physical Direct Connect. Users can create the Direct Connect tunnels connected to different Direct Connect gateways to achieve the interconnection between local data center and multiple VPCs.
3) **Direct Connect gateway**: The Direct Connect traffic entry for VPC, by which you can connect multiple Direct Connect tunnels with different IDCs. Cluster-based Direct Connect gateway can meet the finance-level network interconnection requirements without SPOF (single point of failure) risk in the full path.

Direct Connect gateway serves as the bridge connecting VPC to the physical Direct Connect, and you can create a Direct Connect tunnel associated with a Direct Connect gateway in the physical Direct Connect. The Direct Connect gateway can connect with Direct Connect tunnels from more than one physical Direct Connects to link with multiple local data centers. You can create only one Direct Connect gateway for each VPC in the Direct Connect gateway console. The created gateway can link with the requests for Direct Connect tunnels from different physical Direct Connects.

## Difference between Direct Connect and VPN Connection
- **[VPN Connection](https://cloud.tencent.com/doc/product/215/4956)** uses the public network and IPsec protocol to establish an encrypted network connection between your data center and VPC. You can purchase, enable and configure the VPN gateway in a few minutes. But the VPN connection may be interrupted due to Internet jitter, block or other public network quality problems. If users' services have low requirement for the network connection quality, it is a highly cost-effective choice for fast deployment.
- **Direct Connect** provides you with a dedicated Direct Connect network connection solution, which needs relatively longer construction time, but can provide the network connection services with high quality and reliability. If users' services have low requirement for the network quality and security, you may choose this solution for deployment.

## Direct Connect NAT
Tencent Cloud Direct Connect NAT (Network Address Translation) is a method to convert private IPs into other IPs for hybrid cloud connection, including IP translation and IP port translation. Direct Connect NAT can be used in the following two scenarios:
- IP conflict between the two ends of Direct Connect.
- To shield the actual local or peer network segment from being exposed to the other one.

## IP Translation
IP translation refers to the original IP translation to the new IP to achieve network interconnection, which includes **local IP translation** and **peer IP translation**. IP translation does not distinguish whether the access is initiated by the source or the destination. The new IP can either access or be accessed by the peer.

### Local IP Translation
Refers to the original VPC IP mapping to the new IP to achieve interconnection with the user IDC with new IP.
In the local IP translation, the original IP refers to the IP in VPC, and the mapped IP ***cannot*** be within the VPC CIDR range.
![](//mccdn.qcloud.com/static/img/89b1432e10828610a7287f1c5a150ec9/image.png)

**Example:**
When VPC IP A  `192.168.0.3` is mapped to IP B   `10.100.0.3`, the network packet source IP of the active access of IP A to Direct Connect peer will be automatically changed to `10.100.0.3`. All network packets returned from the Direct Connect peer to `10.100.0.3` will be automatically directed to IP A `192.168.0.3`.

**Note:**
- You can configure more than one local IP translation rules and the network ACL for each local IP translation rule. The network ACL supports the configuration for source port, destination IP, and destination port. NAT rules will take effect only for network requests that meet ACL restriction requirements.
- The local IP translation does not impose any limit on the direction of network requests, which could be the active access of VPC to Direct Connect peer or vice versa.

### Peer IP Translation
Refers to the original IP of user IDC mapping to new IP to achieve interconnection with the VPC IP with new IP. In the peer IP translation, the original IP refers to the IP of user IDC, and the mapped IP ***cannot*** be within the VPC CIDR range.
![](//mccdn.qcloud.com/static/img/a3cbf4c2a9b0c3ac3664b2a20d1768fd/image.png)

**Example:**
When Direct Connect peer IP D  `10.0.0.3` is mapped to IP C   `172.16.0.3`, the network packet source IP of the active access of `10.0.0.3` to VPC will be automatically changed to IP C `172.16.0.3`. All network packets returned from VPC to IP C `172.16.0.3` will be automatically directed to Direct Connect peer IP D `10.0.0.3`.

![](//mccdn.qcloud.com/static/img/cfdd11f873c0db9a0027088e955e46b7/image.png)

**Note:**
- The mapped IPs for local IP translation and peer IP translation cannot overlap, otherwise exceptions may occur during network access.
- When there is conflict between the user IDC IP and VPC IP, it is necessary to configure ***both*** the local IP translation and peer IP translation. Such IP conflict cannot be resolved by only configuring the peer IP translation.
- After the local or peer IP translation is configured, the Direct Connect gateway will only send the routing of translated IP to the Direct Connect peer, so the Direct Connect peer cannot be pinged via original IP for the local or peer IP translation. But the Direct Connect gateway cannot replace the professional network firewall. If you need advanced network protection, please configure security group and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.


## IP Port Translation
IP port translation refers to the original IP port mapping to the new IP port to achieve network interconnection,  which includes **local source IP port translation** and **local destination IP port translation**.
IP port translation has direction. The source IP port translation accesses externally and the destination IP port translation is accessed by the peer.

### Local Source IP Port Translation
Refers to the accesses to user IDC of Direct Connect peer using random port of random IP within specified IP pool when VPC IP access externally via the Direct Connect gateway:
![](//mccdn.qcloud.com/static/img/4c4131dadd5b8c120f1f16c31cca46df/image.png)

**Example:**

The VPC C network segment `172.16.0.0/16` connects the third-party bank A and B via Direct Connect, where the peer network segment of bank A is `10.0.0.0/28`, requiring the connected network segment `192.168.0.0/28`, and the peer network segment of bank B is `10.1.0.0/28`, requiring the connected network segment `192.168.1.0/28`. You can configure two local source IP port translation rules as follows:

- Address pool A:  `192.168.0.1-192.168.0.15`
- ACL rule A: source IP `172.16.0.0/16`, destination IP `10.0.0.0/28`, destination port `ALL`
- Address pool B:  `192.168.1.1-192.168.1.15`
- ACL rule B: source IP `172.16.0.0/16`, destination IP `10.1.0.0/28`, destination port `ALL`

The VPC network request for active access to A or B will be translated into the random port of corresponding address pool based on ACL rule A or B to access the appropriate Direct Connect tunnel.

**Note:**

- The local source IP port translation only supports the network access request initiated by the VPC. If the Direct Connect peer needs to initiate active access to the IP port in VPC, it requires additional configuration for the local destination IP port translation.
- For the local source IP port translation, the network request initiated by VPC is for the stateful connection, so there is no need to consider the network return packet.
- The local source IP port translation supports the configuration of ACL rules. Only the network access in accordance with ACL rules can be matched with the address pool forwarding rules. By configuring different ACL rules for an address pool, you can flexibly configure NAT rules for multiple third-party access.

### Local Destination IP Port Translation
Refers to an approach for the active access of Direct Connect peer to VPC. By mapping the specified port of specified IP in the VPC to the new IP and port, the Direct Connect peer can only communicate with the specified IP port in VPC by accessing to the mapped IP port. Other IP ports will not be exposed to the Direct Connect peer:

![](//mccdn.qcloud.com/static/img/f5569c546acb766908cf99d7c7e15798/image.png)

**Example:**
For the VPC C network segment `172.16.0.0/16`, if you only want to open several ports for the active access of Direct Connect peer, you can configure as follows:
- Mapping A: the original IP port `172.16.0.1:80`, the mapped IP port `10.0.0.1:80`
- Mapping B: the original IP port `172.16.0.0:8080`, the mapped IP port `10.0.0.1:8080`

The Direct Connect peer can access Port `10.0.0.1:80` and` 10.0.0.1:8080` to achieve the active access to Port `172.16.0.1:80` and `172.16.0.0:8080` in the VPC.

**Note:**

- After the local source or destination IP port translation is configured, the Direct Connect gateway will only send the routing of translated IP port to the Direct Connect peer, so the local IP port cannot initiate requests actively or receive requests passively. But the Direct Connect gateway cannot replace the professional network firewall. If you need advanced network protection, please configure security group and network ACL policies in the VPC, and deploy professional physical network firewall devices in your IDC.
- When both IP translation and IP port translation are configured, it will match IP translation first. If there is no match for IP translation, it will match IP port translation.
- ACL rule is not applicable to the local destination IP port translation, so the IP port translation rule will be valid for all Direct Connect tunnels connected with the Direct Connect gateway.
- The local destination IP port translation will only be valid for the active access of Direct Connect tunnel peer to the VPC. If the VPC needs to have the active access to the Direct Connect peer, you can configure the local source IP port translation.
- For the local destination IP port translation, the network request is for the stateful connection, so there is no need to consider the network return packet.
- In the local destination IP port translation, you can set an individual IP or a set of consecutive IPs as the IP pool for destination address translation.
- In the local destination IP port translation, the original IP port specified is the IP in VPC, and the mapped IP port is the translated IP port to which the peer initiates the active access. When setting the port mapping rule, you also need to specify whether the network protocol is TCP or UDP.



## Usage Constraints
The following are what you need to know about **Direct Connect**:
- When the Direct Connect gateway is created, the IP translation and IP port translation contents are left empty by default. In this case, neither the IP translation nor IP port translation is effective.
- Direct Connect tunnel supports BPG route and static route.

The following are what you need to know about **IP translation**:
- The IP address pool cannot be within the CIDR range of VPC to which the Direct Connect gateway belongs.
- ACL rules for multiple IP address pools cannot overlap. Otherwise, this will cause network address translation conflicts.
- IPs between multiple IP address pools cannot overlap.
- IP address pool only supports individual IP or consecutive IPs, and /24 network segment of consecutive IPs should be consistent. `192.168.0.1~192.168.0.6` is supported, but `192.168.0.1~192.168.1.2` not.
- Address pool should not contain broadcast address (255.255.255.255), Class D address (224.0.0.0~239.255.255.255), or Class E address (240.0.0.0~255.255.255.254).
- The local source IP port translation supports a maximum of 100 IP address pools, and each address pool supports a maximum of 20 ACL rules. (You can submit a ticket to apply for a higher quota if needed.)
- If you need to switch from IP translation to IP port translation, please clear the original IP translation rule and refresh the page to edit the IP port translation rule.

The following are what you need to know about **IP port translation**:
- The original IP must be within the CIDR range of VPC to which the Direct Connect gateway belongs.
- The original IP port should be unique. In other words, the same IP port within the VPC can only be mapped to one IP port.
- The mapped IP port cannot be within the CIDR range of VPC.
- Mapped IP Port should be unique. In other words, multiple IP ports in a VPC cannot be mapped to the same IP port.
- Original IP or mapped IP should not be broadcast address (255.255.255.255), Class D address (224.0.0.0~239.255.255.255), Class E address (240.0.0.0~255.255.255.254)
- The local destination IP port translation supports a maximum of 100 IP port mappings. (You can submit a ticket to apply for a higher quota if needed.)
- When configuring IP translation and IP port translation, it will match IP translation first if any conflicts occur.

| Resource | Limit | Description |
|------|-----|-----|
| Physical Direct Connect / User | 10 | |
| Direct Connect tunnel / Physical Direct Connect | 10 | |
| Direct Connect gateway (NAT supported) / Virtual Private Cloud | 1 | |
| Direct Connect gateway (NAT not supported) / Virtual Private Cloud | 1 | |
| Local IP translation / Direct Connect gateway | 100 | You can apply for higher quota. |
| Peer IP translation / Direct Connect gateway | 100 | You can apply for higher quota. |
| Number of IPs for local source IP port translation / Direct Connect gateway | 20 | You can apply for higher quota. |
| Local destination IP port translation / Direct Connect gateway | 100 | You can apply for higher quota. |

## Billing Method

The physical Direct Connect can be established by Tencent Cloud or by users.
- In the first mode, Tencent Cloud will initiate the request to the ISP for the establishment of Direct Connect and assume the responsibilities for its O&M and management;
- In the second mode, users will initiate the request to the ISP for the establishment of Direct Connect. The ISP shall take the responsibilities for its the O&M and management. Tencent Cloud is responsible for the connection debugging of Direct Connect as well as the O&M and management for the devices of Tencent Cloud. The fee charged by Direct Connect varies depending on the mode.

For the price details of Direct Connect, please contact the Direct Connect manager or customer service.

## Expiration
The physical Direct Connect only supports the annual prepaid payment mode for ISP reasons. The Direct Connect manager will contact you 1 month before your physical Direct Connect expires for the use of Direct Connect next year, and you need to confirm in advance whether to continue using it:
- If not, the Direct Connect will enter into the termination process when the validity period expires. The Direct Connect and corresponding Direct Connect tunnels will be deleted;
- If yes, please renew it before expiration, otherwise the network service will be suspended after it expires;
- If you do not top up for the renewal of suspended Direct Connect within 1 month, the Direct Connect will enter into the termination process. The Direct Connect and corresponding Direct Connect tunnels will be deleted.
You need to notify whether to continue using the Direct Connect service by email, which serves as the basis for reference.

## Operation Instruction
If you need the Direct Connect to connect your data center and the VPC on Tencent Cloud, please perform the steps as follows:
Step 1: Creating the physical Direct Connect
Step 2: Creating the Direct Connect tunnel
Step 3: Creating the Direct Connect tunnel for Direct Connect gateway, thus connecting your data center to your VPC.
(Optional) Step 4: Configuring the Direct Connect NAT
Step 5: Configuring the routing table associated with the subnets requiring communication.

These steps are described in detail below:
### Step 1: Creating the Physical Direct Connect
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Direct Connect" - "Physical Direct Connect" tab, and then click "New" button.
2) You need to carefully verify the region where the local data center is located, Direct Connect ISPs and the bandwidth of your physical Direct Connect, as these parameters cannot be changed once confirmed. After entering the basic information for the application of the physical Direct Connect, you will be provided with the recommended price based on the region of your local data center. You do not need to pay it during application.
3) After clicking "OK", you can find your Direct Connect application record on the "Application Record" page of the Direct Connect console. Our Direct Connect manager will contact you within 1 business day for the details of the Direct Connect. After it's approved, the status of the application record will change to "Payment Pending". If Tencent Cloud is deemed incapable of meeting your requirements for the applied Direct Connect after communication, the manager will change the status to "Application Refused".

The payment may be different depending on the establishment mode, the region where the local data center is located, and the bandwidth of Direct Connect. Once the payment is confirmed and paid, Tencent Cloud will carry out the Direct Connect construction based on the information you submitted, and if there is any parameter error found during its construction, you should bear the full cost incurred therefrom. The physical Direct Connect cannot be deleted during construction. After construction is completed, its status will change to "Running" on its console.

![](//mccdn.qcloud.com/img567fa85e57aa3.png)

### Step 2: Creating the Direct Connect Tunnel
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then click "Direct Connect Gateway" tab.
2) Click the "New" button to enter the Direct Connect creation page.
3) Enter the name, VPC and address mapping mode, and select whether to enable the network address translation function. (**This function is only available in the beta test currently**. Please activate it by a ticket or your customer manager.)
4) Click OK to confirm the information and complete the creation of the Direct Connect gateway.

### Step 3: Creating the Direct Connect Tunnel
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click "Direct Connect"- "Direct Connect Tunnel" tab.
2) You can only create the Direct Connect tunnel for a physical Direct Connect in "Running" status to establish a network link in the physical Direct Connect. Click the "New" button to enter the Direct Connect tunnel creation page.

Direct Connect tunnel supports BPG route and static route. BGP ASN and BGP key are required for BPG route.
The Vlan ID and Peer IP are configured automatically.

After the Direct Connect tunnel is created, it will take 1-2 business days to deploy network changes, during which please contact our Direct Connect manager for any questions you may have.

### (Optional) Step 4: Configuring the Direct Connect NAT
You can configure the gateway's network address translation on the Direct Connect gateway page. Such translation can be divided into IP translation and IP port translation.
#### IP Translation Configuration
IP translation refers to the original IP translation to the new IP to achieve network interconnection, which includes local IP translation and peer IP translation. IP translation does not distinguish whether the access is initiated by the source or the destination. The new IP can either access or be accessed by the peer. The specific procedure is as follows:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then click "Direct Connect" - "Direct Connect Gateway" tab.
2) Click the ID of the Direct Connect gateway to enter its details page.
3) Edit the rules for "Local IP Translation".

- Adding: In the top-left corner of the IP mapping page, click the "New" blue button and enter the original IP, mapped IP and note. ACL rule for the new local IP translation rule is ALL PASS by default, which means the local IP translation is valid for all Direct Connect tunnels. You can edit the ACL rule for the local ACL translation to change the applicable scope of the local IP translation.
- Deleting: Click "Delete" to the right of the IP translation rule and click OK to confirm the deletion. When the IP translation rule is deleted, all the ACL rules under it will also be deleted.
- Modifying: Click the "Modify IP Mapping" to the left of the IP translation rule to edit the original IP, mapped IP and note of the local IP translation rule. The modified IP translation takes effect immediately after clicking OK.

4) Configure the network ACL rules for local IP translation.
ACL rules support TCP and UDP protocol. The local IP mapping ACL rules support the source port, destination IP, and destination port. If the port and the IP are left blank, it means ALL. When ALL is selected for the protocol, both the port and the IP will default to ALL.
- Adding: Click "Edit ACL Rule" to the right of the IP mapping rule and click "Add" next to the existing ACL rules.
- Deleting: Click "Edit ACL Rule" to the right of a IP mapping rule for editing. Click "Delete" and OK to delete the ACL rule. You can also click the "Delete" button next to the ACL rule to delete it.
- Modifying: Click "Edit ACL Rule" to the right of a IP mapping rule to modify a ACL rule. You can also click the "Modify" button next to the ACL rule to modify it.


#### IP Port Translation Configuration
IP port translation refers to the original IP port mapping to the new IP port to achieve network interconnection, which includes **local source IP port translation** and **local destination IP port translation**. The specific procedure is as follows:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then click "Direct Connect" - "Direct Connect Gateway" tab.
2) Click the ID of the Direct Connect gateway to enter its details page.
3) On the Direct Connect gateway details page, click "Source IP Port Translation". There are two steps for configuring source IP port translation:

**Step 1: Configuring the local IP port translation address pool**
- Adding: Click "New" in the mapped IP pool page, enter the mapped IP pool (IP or IP segment is supported) and note (optional); ACL rule for the new IP pool is ALL DROP by default, and you need to edit the ACL rule to enable network translation;
- Deleting: Click "Delete" to the right of the IP address pool to delete the address pool. Deleting an address pool will delete the ACL rules associated with the address pool automatically.
- Modifying: Click "Modify Mapped IP Pool" to the right of the IP address pool to edit the IPs and note of the mapped IP pool.

**Step 2: Configuring the network ACL rule for the IP address pool**
ACL rules support configuration protocol (TCP or UDP), source IP, source port, destination IP, and destination port.
- Adding: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "New Line" at the bottom of the rule to add a new ACL rule.
- Deleting: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "Delete" to the right most of an ACL rule to delete it. You can also delete an ACL rule by expand it and click "Delete" to the right most of it.
- Modifying: Click "Edit ACL Rule" to the right of the IP address pool for editing. You can also modify an ACL rule by expand it and click "Modify" to the right most of it.

4) Configuring the local destination IP port translation.
On the Direct Connect gateway details page, click "Local Destination IP Port Translation" tab.
Adding: Click "Add" on the IP port mapping page to add a new IP port mapping.
Deleting: Click "Delete" to the right of the line where the IP port mapping is located to delete the mapping.
Modifying: Click "Modify IP Port Mapping" to the right of the line where the IP port mapping is located to modify the mapping and note of this IP port mapping.

### Step 5: Configuring the routing table associated with the subnets requiring communication
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2)	Click "Routing Table" in the left navigation bar and click the routing table ID associated with the subnet requiring communication to enter its details page.
3)	Click the "Edit" and "New line", enter the destination network segment, and select "Direct Connect" as the next hop type; then select the gateway name for next hop.
4)	Click "Save".

### Step 6: Setting the alarm
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products" - "Monitor & Management" - ["Cloud Monitoring"](https://console.qcloud .com/monitor/overview) in the top navigation bar, and then select "My Alarms" - ["Alarm Policy"](https://console.cloud.tencent.com/monitor/policylist) in the left navigation bar, and click Add Alarm Policy.
2)	Fill in the Policy Name, select "Physical Direct Connect" or "Direct Connect Tunnel" in Policy Type, and then add the Hit Condition.
3)	**Associate alarm objects**: select the alarm receiver group. You can view the set alarm policy in the policy list after you click "Complete".
4)	**View the alarm information**: when the alarm is triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation "My Alarms" - "Alarm List". For more information about alarms, refer to [Creating Alarms](https://cloud.tencent.com/doc/product/248/1073).

## API Overview
You can use the command line or APIs to configure and manage the Direct Connect gateway. Please refer to [Overview of All VPC APIs](https://cloud.tencent.com/doc/product/215/4954).

