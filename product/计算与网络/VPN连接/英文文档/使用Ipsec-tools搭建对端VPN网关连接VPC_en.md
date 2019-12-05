Tencent Cloud VPC can be used to connect customer IDC through encrypted VPN tunnels by simply setting VPN gateway and peer gateway on the VPC and user IDC. If you currently don't want to use hardware VPN devices from Cisco, Juniper, H3C and other manufacturers, you can use open source software on the server to build the peer gateway. This document shows how to connect with Tencent Cloud VPC via open source software to establish hybrid cloud scenarios by installing Ipsec-tools on CentOS.

## 1. Environment Description
![](//mccdn.qcloud.com/img56c6836ccfc95.png)

As shown above, the left shows your VPC built on Tencent Cloud. To connect your VPC with customer IDC on the right, you can use the public network to establish an encrypted Ipsec VPN tunnel between the two to ensure safe and reliable transmission of data.

First, you need to set up your VPC on Tencent Cloud, and then you can perform the subnet layout, purchase VPN gateway, and set up the VPC routing of IDC network to be interconnected according to your need. (Note: please select the VPN gateway you purchased in "next hop" of routing settings.) For detailed procedures to create the VPC shown on the left, please refer to [Creating VPC and Subnet](http://cloud.tencent.com/doc/product/215/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%8F%8A%E5%AD%90%E7%BD%91), [Adding Cloud Services to VPC](http://cloud.tencent.com/doc/product/215/%E5%90%91%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E4%B8%AD%E6%B7%BB%E5%8A%A0%E4%BA%91%E6%9C%8D%E5%8A%A1), [Associating Subnets and Routing Tables](http://cloud.tencent.com/doc/product/215/%E5%85%B3%E8%81%94%E5%AD%90%E7%BD%91%E8%B7%AF%E7%94%B1), [Modifying Default Routing Table](http://cloud.tencent.com/doc/product/215/%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E8%B7%AF%E7%94%B1%E8%A1%A8) and [Creating VPN Gateway](http://cloud.tencent.com/doc/product/215/%E5%88%9B%E5%BB%BAVPN%E7%BD%91%E5%85%B3).

If you need to use the VPN hardware devices to build peer VPN gateway in IDC, please refer to available device list [here](http://cloud.tencent.com/help/VPN%E9%80%9A%E9%81%93%E5%BB%BA%E7%AB%8B%E7%9B%AE%E5%89%8D%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E8%AE%BE%E5%A4%87).

If you currently don't want to use any hardware VPN devices from other manufacturers, you can use the Ipsec-tools open source tool to set up a VPN gateway in IDC data center as described in the following section.

## 2. Installing Ipsec-tools
CentOS 6.4 is taken as an example to illustrate the system environment requirements:
Linux version 2.6.32-431.23.3.el6.x86_64
(mockbuild@c6b8.bsys.dev.centos.org) (gcc version 4.4.7 20120313 
(Red Hat 4.4.7-4) (GCC) ) #1 SMP Thu Jul 31 17:20:51 UTC 2014

Choose from packet ipsec-tools-0.8.0-25.3.x86_64.rpm or packet ipsec-tools-0.8.0-25.3.i686.rpm depending on the system platform. Download at:

ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/aevseev/CentOS_CentOS-6/x86_64/ipsec-tools-0.8.0-25.3.x86_64.rpm

ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/aevseev/CentOS_CentOS-6/i686/ipsec-tools-0.8.0-25.3.i686.rpm

After the download, you may install it using the following command:

```
rpm -ivh ipsec-tools-0.8.0-25.3.x86_64.rpm
```
Or:
```
rpm -ivh ipsec-tools-0.8.0-25.3.i686.rpm
```

After the installation, you may check the installation results using the following command:

```
racoon -V
```
![](//mccdn.qcloud.com/img56c68a299aed9.png)

## 3. Configuring Ipsec-tools
The files to be configured include:

IPSec policy configuration file: /etc/racoon/setkey.conf
Key configuration file: /etc/racoon/psk.txt
IKE configuration file: /etc/racoon/racoon.conf

### 3.1. Configuring Ipsec Policies
Use the following command to open the configuration file:

```
vi /etc/racoon/setkey.conf
```

Set up as follows:

Assuming that the CIDR of your VPC is 10.100.2.0/24, the IP address of the VPN gateway on the VPC is 112.\*.\*.251,  the CIDR of your IDC is 172.16.2.0/24 and the IP address of the local VPN device is 112.\*.\*.152, please configure as follows:
![](//mccdn.qcloud.com/img56c68be5ba93c.png)

### 3.2. Configuring Key
Use the following command to open the configuration file:

```
vi /etc/racoon/psk.txt
```
Again, assuming that the IP address of the VPN gateway on the VPC is 112.\*.\*.251 and the pre-shared key is "test", psk.txt will be configured as follows:

![](//mccdn.qcloud.com/img56c68ca34b349.png)

Execute the following command:

```
chmod 600 psk.txt   
chown root psk.txt
```

### 3.3. Configuring IKE
Use the following command to open the configuration file:

```
vi /etc/racoon/racoon.conf
```

Again, assuming that the IP address of the VPN gateway on the VPC is 112.\*.\*.251 and the IP address of the local VPN device is 112.\*.\*.152, racoon.conf will be configured as follows:

![](//mccdn.qcloud.com/img56c68dc067617.png)

## 4. Starting Ipsec-tools

Execute the following command to start Ipsec-tools:

```
echo 1 > /proc/sys/net/ipv4/ip_forward
/usr/sbin/setkey -f /etc/racoon/setkey.conf
/usr/sbin/racoon -f /etc/racoon/racoon.conf
```

To ensure that the Ipsec service could be automatically started after rebooting, you need to write these three commands to the /etc/rc.local file.

## 5. Checking tunnel status
Use the following command to see if the negotiation of tunnel SA has been negotiated:


```
setkey -D
```

![](//mccdn.qcloud.com/img56c68edfa569d.png)

On your IDC network, you need to route the CIDR messages of which the destination IP address is your VPC to your peer VPN gateway, i.e. the machine with Ipsec-tools configuration described earlier.

Ping your VPC sub-machine IP on the machine in the IDC to check if the communication has been established.

## 6. Others
If VPC and IDC cannot achieve encrypted communication after configuration, you can check by following the steps below:

1) Check whether the VPC gateway IP is accessible
Ping the public IP address of VPN gateway purchased on Tencent Cloud to check whether it is accessible.

2) Check whether routing is missing
Use the following command to check whether there is routing or default routing to the VPC segment.

```
route -n
```

3) Check whether there is a firewall filtering policy
Use the following command to check whether there is a firewall filtering out IKE or private network communication messages.

```
iptables   -nvL
```

4) Check the firewall NAT policy
Check whether the NAT is performed for private network communication messages, making them unable to match Ipsec policies.

```
iptables    -t    nat   -nvL
```

