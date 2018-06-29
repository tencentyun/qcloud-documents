Private network services are LAN services. Cloud services can access each other via internal linkages. The cloud products on the Tencent Cloud can access each other via [Internet Access](/doc/product/213/5224) or via the private network of Tencent Cloud. Interconnected with megabyte/gigabyte underlying networks, Tencent Cloud's data centers can enable communication via private network featured by large bandwidth and low latency, which is free of charge in the same region, giving you the flexibility to build a network architecture.

## Private IP address
### Overview
Private IP addresses are IP addresses that cannot be accessed through Internet. Tencent Cloud's private network services are realized based on them. Each instance has a default network interface (eth0) for the assignment of private IPs. Private IP addresses can be automatically assigned by Tencent Cloud, or defined by users (only under the [VPC](/doc/product/215/4927)).
>**Note:**
>Changing the private IP by yourself within the operating system may cause private network interruption.

### Attribute
 - Private network services are user-sensitive. Different users are isolated from each other, which means that the cloud services of the other user cannot be accessed via the private network by default.
 - Private network services are also region-sensitive. Different regions are isolated from each other, which means that the cloud services under the same account in a different region cannot be accessed via the private network by default.

### Application Scenarios
A private IP can be used for access between CLBs, CVMs, or access between CVMs and other cloud services (such as CDN and CDB) via a private network.

### Address Assignment
Each CVM instance will be given a default private IP address when activated. The private IP varies with [Network Environment](/doc/product/213/5227):
 - Basic network: The private IP address is assigned by Tencent Cloud automatically and cannot be changed.
 - VPC: The initial private IP address is assigned by Tencent Cloud randomly in VPC IP address range, and users can define the private IP address for the CVM instance within the `10.[0 - 255].0.0/8`, `172.[0 - 31].0.0/16` and `192.168.0.0/16` IP address ranges. The specific value range is determined by the VPC where the instance locates. For more information, please see [VPC and Subnet](/doc/product/215/4927).

## Private Network DNS 
### DNS Server Address
Private network DNS service is used for domain name resolution. If DNS configuration is incorrect, the domain name will become inaccessible.
Tencent Cloud provides reliable private network DNS servers in different regions. Specific configurations are shown below:
<table><tbody>
<tr><th>Network Environment</th><th>Region</th><th>Private Network DNS Server</th></tr>
<tr><td rowspan="13">Basic network</td><td>Guangzhou</td><td>10.225.30.181<br>10.225.30.223</td></tr>
<tr><td>Shanghai</td><td>10.236.158.114<br>10.236.158.106</td></tr>
<tr><td>Beijing</td><td>10.53.216.182<br>10.53.216.198</td></tr>
<tr><td>Shanghai Finance</td><td>10.48.46.77<br>10.48.46.27</td></tr>
<tr><td>Shenzhen Finance Zone</td><td>100.83.224.91<br>100.83.224.88</td></tr>
<tr><td>North America</td><td>10.116.19.188<br>10.116.19.185</td></tr>
<tr><td>Hong Kong</td><td>10.243.28.52<br>10.225.30.178</td></tr>
<tr><td>Singapore</td><td>100.78.90.19<br>100.78.90.8</td></tr>
<tr><td>Guangzhou Open Zone</td><td>10.59.218.18<br>10.112.65.51</td></tr>
<tr><td>Chengdu</td><td>100.88.222.14<br>100.88.222.16</td></tr>
<tr><td>Silicon Valley</td><td>100.102.22.21<br>100.102.22.30</td></tr>
<tr><td>Frankfurt</td><td>100.120.52.60<br>100.120.52.61</td></tr>
<tr><td>Seoul</td><td>10.165.180.53<br>10.165.180.62</td></tr>
<tr><td>VPC</td><td>All regions</td><td>183.60.83.19<br>183.60.82.98</td></tr>
</tbody>
</table>