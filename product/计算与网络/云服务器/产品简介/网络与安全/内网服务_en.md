Cloud products on the Tencent Cloud can be accessed via [Internet access](/doc/product/213/5224) or accessed mutually via the Tencent Cloud private network. Private network services are Local Area Network (LAN) services, which are accessed mutually via private links. Tencent Cloud server rooms are interconnected by an underlying 10 Gigabit / Gigabit, providing high bandwidth, low latency within network communications services; and regions within the private network enjoy communications completely free of charge, helping you build a flexible network architecture.
> - Private network services contain user attributes; different users are isolated; that is, by default they cannot access another user's network through CVM services.
> - Private network services also have geographical attributes, and different geographical isolation; that is, by default, they cannot access the network through different accounts under cloud services.

## Private IP address

A private IP address is an IP that cannot access via the Internet; this is an implementation of private services by Tencent Cloud. You can use private IP addresses to implement communications between instances on the same network (basic networks or VPC). Each instance has a default network interface (ie, eth0) for assigning private IP addresses. Private IP addresses can be automatically assigned by Tencent and customized by users (only in [Private Network] environments). The combination of [Internet services](/doc/product/213/5224), and the Tencent cloud network architecture consists of the following two parts:

- Public network cards: Unanimously configured on the TGW interface layer, without CVM perception. When an instance is assigned a [Public IP address](/doc/product/213/5224), TGW automatically configures a public network interface for it.
- Private network card: Managed by Tencent Cloud, supports user configurations.

Therefore, when the user uses commands such as 'ifconfig' to view network interface information on the CVM, only the IP information of the private network can be viewed. For public network information, users need to log onto the [Tencent Cloud Console](https://console.cloud.tencent.com/) CVM list/details page to view. Please note that if you change the private network IP within an operating system, it will lead to an interruption of network communications.

Private IPs can be used for CLB load balancing, inter-network visits between CVM instances and between CVM instances and other cloud services, such as CDN and CDB.

## Private network DNS 
Private network DNS services are responsible for domain name resolutions; if a DNS configuration is wrong, the domain name cannot be accessed. Therefore, Tencent Cloud provides reliable private DNS servers in different regions. The specific configuration is as follows:
<table><tbody>
<tr><th>Network environment</th><th>Region</th><th>Private DNS server</th></tr>
<tr><td rowspan="7">Basic network</td><td>Guangzhou</td><td>10.225.30.181<br>10.225.30.223</td></tr>
<tr><td>Shanghai</td><td>10.236.158.114<br>10.236.158.106</td></tr>
<tr><td>Beijing</td><td>10.53.216.182<br>10.53.216.198</td></tr>
<tr><td>Shanghai Finance</td><td>10.48.18.9<br>10.48.18.82</td></tr>
<tr><td>North America</td><td>10.116.19.188<br>10.116.19.185</td></tr>
<tr><td>Hong Kong</td><td>10.243.28.52<br>10.225.30.178</td></tr>
<tr><td>Singapore</td><td>100.78.90.19<br>100.78.90.8</td></tr>
<tr><td>Private network</td><td>All regions</td><td>183.60.83.19<br>183.60.82.98</td></tr>
</tbody>
</table>
