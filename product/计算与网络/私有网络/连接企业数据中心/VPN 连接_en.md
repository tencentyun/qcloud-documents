## Introduction
VPN Connection is a method you can use to connect peered IDC and VPC through public network encrypted tunnel. As shown below, Tencent Cloud VPC VPN Connection consists of the following components:
- VPN gateway: created VPC IPsec VPN gateway
- Customer gateway:  IPsec VPN service gateway for IDC
- VPN tunnel: encrypted IPsec VPN tunnel
![](//mccdn.qcloud.com/static/img/a654d376b4e4e13ae2bb65b13239cef2/image.png)

A VPN gateway can be established in the VPC. Each VPN gateway can establish multiple VPN tunnels. Each VPN tunnel can connect with one local IDC. It is important to note that **after establishing a VPN connection, you need to configure the routing policy in the routing table to achieve communication.**
 
## VPN Gateway
VPN gateway is an outbound gateway that establishes VPN connections in the VPC, which can be used with customer gateway (IPsec VPN service gateway for IDC). VPN gateway is mainly used to establish a secure and reliable encrypted network communication between Tencent Cloud VPC and external IDC. Implementing through virtual software and adopting duplicated hot backup strategy, Tencent Cloud VPN gateway can switch automatically when a single server suffers a failure, and will not affect the normal operation of the business.

According to the upper limit of bandwidth, VPN gateway is divided into five kinds of settings, namely: 5M, 10M, 20M, 50M and 100M. You can adjust the VPN gateway bandwidth setting at any time.

## Customer Gateway
Customer gateway refers to the IPsec VPN service gateway of IDC data center, which needs to be used with Tencent Cloud VPN gateway. A VPN gateway can establish encrypted VPN network tunnels with multiple customer gateways.

## VPN Tunnel
After the VPN gateway and the customer gateway are established, the VPN tunnel used for encrypted communication between VPC and external IDC can be established. Currently, VPN tunnels support IPsec encryption protocol, which can meet the needs of most VPN connections.

Because the VPN tunnels are operating in the operator's public network, the block or jitter of public network will affect the quality of VPN network. Therefore, the assurance of SLA service agreement is currently unavailable. If your business is sensitive to delay and jitter, it is recommended to access the VPC via Direct Connect. For more information, refer to [Direct Connect](https://cloud.tencent.com/product/dc.html).

The VPN tunnel on Tencent Cloud uses Internet Key Exchange (IKE) protocol to establish a session when implementing IPsec. IKE is provided with a self-protection mechanism that can securely authenticate identities, distribute keys and establish IPSec sessions on unsecured networks.

The establishment of VPN tunnel includes the following configuration information:
- Basic information
- Security Policy Database (SPD) policy
- IKE configuration (optional)
- IPsec configuration (optional)

The basic information, SPD policy, IKE configuration (optional) and IPsec configuration (optional) are described in detail below.

### Basic Information
Protocol type: IKE/IPsec
Pre-shared private key: The pre-shared private key is a Unicode string used to verify L2TP/IPSec connections. The local and peer must use the same pre-shared private key.

### Security Policy Database (SPD) Policy
The Security Policy Database (SPD) policy consists of a series of SPD rules, each of which is used to specify which segments of the VPC can communicate with which segments of the IDC.
- Each SPD policy corresponds to a local network segment and multiple peer network segments. The local network segment and the peer network segments cannot overlap.
- The local network segments of all policy collections cannot overlap.
- The multiple peer network segments of each local network segment cannot overlap.
- The peer network segment and the VPC network segment cannot overlap.

Here is a correct instance:

SPD policy 1 The local network segment is `10.0.0.0/24`, the peer network segment is `192.168.0.0/24`, `192.168.1.0/24`.
SPD policy 2 The local network segment is `10.0.1.0/24`, the peer network segment is `192.168.2.0/24`.
SPD policy 3 The local network segment is `10.0.2.0/24` the peer network segment is `192.168.2.0/24`.

![](//mccdn.qcloud.com/static/img/5b32174d312e31c5b5a9162a50456de8/image.png)
 
### IKE Configuration

| Configuration Item | Description |
|--|--|
| Version | IKE V1 |
| Authentication method | Default pre-shared private key |
| Authentication algorithm | Authentication algorithm, support MD5 and SHA1 |
| Negotiation mode | Support main mode and aggressive mode<br><br>The difference between the two is that the aggressive mode can send more information with fewer packets, which can establish connection quickly at the expense of sending the identity of security gateway in a clear way. When using aggressive mode, configuration parameters such as Diffie-Hellman and PFS can not be negotiated, so having a compatible configuration at both sides is critical |
| Local identity | Support IP address and Fully Qualified Domain Name (FQDN) |
| Peered identity | Support IP address and FQDN |
| DH group | Specify the DH group used during IKE. The security of key exchange increases with the expansion of DH group, but the exchange time also increases<br><br>Group1: DH group using 768-bit modular exponential (MODP) algorithm<br><br> Group2: DH group using 1024-bit MODP algorithm<br><br> Group5: DH group using 1536-bit MODP algorithm <br><br>Group14: DH group using 2048-bit MODP algorithm. Dynamic VPN is not supported for this option<br><br> Group24: DH group using 2048-bit MODP algorithm with a 256-bit prime order subgroup. Group VPN is not supported for this option |
| IKE SA Lifetime | Unit: second<br><br>Set the SA lifetime of IKE security proposal. Before the expiration of set lifetime, another SA will be negotiated in advance to replace the old SA. When the new SA has not been negotiated, the old SA will still be used. After the new SA is established, the new SA will be used immediately, and the old SA will be cleared automatically after its lifetime has expired |

###  Ipsec Information
| Configuration Item | Description |
|--|--|
| Encryption algorithm | Support 3DES, AES-128, AES-192, AES-256, DES |
| Authentication algorithm | Support MD5 and SHA1 |
| Message encapsulation mode | Tunnel |
| Security protocol | ESP |
| PFS | Support disable, dh-group1, dh-group2, dh-group5, dh-group14 and dh-group24 |
| IPsec SA lifetime (s) | Unit: second |
| IPsec SA lifetime (KB) | Unit: KB |

## Usage Constraints
For VPN connections, please note that:
- After the VPN parameters are configured, **you need to add the routing policy directed to VPN gateway in the routing table associated with subnet**, so that the network requests from CVM to peer network segment within the subnet can reach the customer gateway through VPN tunnel.
- After configuring the routing table, ** you need to ping the IP of peer network segment using the CVM of VPC to activate this VPN tunnel.**
- The stability of VPN connection depends on the public network quality of operators, so the assurance of SLA service agreement is currently unavailable.

| Resource | Limit | 
|---------|---------|
| Number of VPN gateways per VPC | 10 | 
| Number of customer gateways in a region | 20 | 
| Number of VPN tunnels per customer gateway | 1 | 
| Number of VPN tunnels in a region | 20 | 
| Number of SPDs per VPN tunnel | 10 | 
| Number of peered network segments per SPD | 50 | 

## Billing Method
- VPN tunnel and customer gateway are free of charge.
- VPN gateway will be charged by month. Its unit price already includes the cost of IDC bandwidth, so CVM does not need to purchase network bandwidth again. The specific expenses are shown in the following table:

| Configuration (Mbps) | Except North America (Toronto) | North America (Toronto) |
|---------|---------|
|5 |380 |480|
|10 |880 |1330|
|20 |1880 |2330|
|50 |4880 |	5330|
|100 |9880 |10330|

For more information regarding the prices of VPC services, refer to [VPC Price Overview](https://cloud.tencent.com/doc/product/215/3079).

## Instructions

## Quick Start
IPsec VPN can be fully customized in the console. You need to complete the following steps to make the VPN connection to take effect:
1) Create VPN gateway
2) Create customer gateway
3) Create VPN tunnel
4) Load the configuration file in its own IPsec VPN gateway
5) **Configure the routing table**
6) **Enable VPN tunnel**

Example:
Through IPsec VPN, connect the subnet A`192.168.1.0/24` in your VPC in **Guangzhou** ("TomVPC") with the subnet `10.0.1.0/24` in your IDC, and the public IP of the VPN gateway in IDC is `202.108.22.5`.
![](//mc.qcloudimg.com/static/img/0cfc46cf11e4d53164219b1c386509a1/1.png)

You need to complete the following steps:
#### Step 1: Create VPN gateway
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "VPN Gateway" tab in the left navigation bar.
3) Select the region of myVPC "**Guangzhou**" and the name of VPC `TomVPC` at the top of the list, then click "New".
4) Fill in the name of VPN gateway (e.g. TomVPNGw), select the appropriate bandwidth configuration and make the payment. Then, the VPN gateway is created. After that, the system will randomly assign a public IP to you, such as: `203.195.147.82`.

#### Step 2: Create customer gateway
Before creating a VPN tunnel, you need to create a customer gateway:
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "Customer Gateway" tab in the left navigation bar.
3) Select the region "**Guangzhou**" at the top of the list, then click "New".
4) Fill in the name of customer gateway (such as: TomVPNUserGw) and the public IP of VPN gateway of IDC `202.108.22.5`.
5) Click "Create" to view the new customer gateway in the customer gateway list.

#### Step 3: Create VPN tunnel
You need to complete the following steps to create a VPN tunnel:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "VPN Tunnel" tab in the left navigation bar.
3) Select the region of myVPC "**Guangzhou**" and the name of VPC `TomVPC` at the top of the list, then click "New".
4) Enter the name of tunnel (e.g. TomVPNConn), select the VPN gateway `TomVPNGw` and the customer gateway` TomVPNUserGw`, and enter the pre-shared key (e.g. `123456`).
5) Enter the SPD policy to limit that which local network segments can communicate with which peer network segments. The local network segment in this example is the network segment of subnet A `192.168.1.0 / 24`, and the peer network segment is` 10.0.1.0 / 24`. Then, click "Next".
6) Step 3: configure IKE parameters (optional). If you do not need advanced configurations, click "Next".
7) Step 4: configure IPsec parameters (optional). If you do not need these parameters, click "Finish" to complete the configuration.
8) Click to complete the creation of VPN tunnel, and download the configuration file.

#### Step 4: Load the configuration file in its own IPsec VPN gateway
To achieve interconnection of VPN tunnels, you need to load and configure the configuration files generated in Step 3 in your own IPsec VPN gateway.

#### Step 5: Modify routing table
After the completion of Step 4, we have successfully configured a VPN tunnel. However, since the traffic of subnet A have not been routed to the VPN gateway, the network segment in subnet A still can not communicate with the network segment in IDC. Now, you need to configure the routing settings:
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "Subnet" in the left navigation bar. Select the region of myVPC "**Guangzhou**" and the name of VPC `TomVPC` at the top of the list. Click the routing table ID associated with subnet A to enter the details page of the routing table.
3) Click "Edit" button, then click "New line". Enter the destination network segment (`10.0.1.0/24`), select the "VPN Gateway" for the next hop type, and then select the VPN gateway`TomVPNGw` you just created.
4) Click "Save" to complete the outbound routing settings of subnet that needs to achieve communication.

#### Step 6: Enable VPN tunnel
To activate the VPN tunnel, you need to ping the IP of peer network segment using the CVM of VPC. For example: use the CVM within the subnet A of `TomVPC` to `ping 10.0.1.1`

### Viewing the Monitoring Data
VPN tunnels and VPN gateways provide monitoring data viewing function.
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "VPN Gateway" or "VPN Tunnel" tab in the left navigation bar.
3) Click the icon in "Monitoring" column on the list page to view the monitoring data.

### Setting the Alarm
VPN tunnel provides alarm function:
1) Log in [Tencent Cloud Console](https://console.cloud.tencent.com/), click in the top navigation bar "Cloud Products" - "Monitor & Management" - ["Cloud Monitoring"](https://console.cloud.tencent.com/monitor/overview), and then select "My Alarms" - ["Alarm Policy"](https://console.cloud.tencent.com/monitor/policylist) in the left navigation bar, and click Add alarm policy.
2) Fill in the Alarm Policy Name, select "VPN Tunnel" in Policy Type, and then add the Condition of alarm trigger.
3) **Associate alarm objects**: select the alarm receiver group, and when it is saved, you can view the set alarm polices in Policy List.
4) **View the alarm information**: when any alarm conditions are triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation "My Alarms" - "Alarm List". For more information about alarms, refer to [Creating Alarms](https://cloud.tencent.com/doc/product/248/1073).

### Viewing the Details of VPN Gateway
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "VPN Gateway" tab in the left navigation bar.
3) Click "VPN Gateway ID" to enter the details page of VPN gateway to view the information of VPN gateway.

### Modifying the VPN tunnel configuration
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click "VPN Connection" - "VPN Tunnel" tab in the left navigation bar.
3) Click "VPN Gateway ID" to enter the details page of VPN gateway to view the information of VPN gateway.
4) You can modify the basic information and SPD policy in the basic information page, or you can modify the IKE and Ipsec configurations in "Advanced Configuration".
 

## API Overview
You can use API operations to configure and manage your VPN connections. Please refer to [Overview of All VPC APIs](https://cloud.tencent.com/doc/api/245/909).
