Security has always been our major concern. By listing security as the top priority of the product design, Tencent Cloud requires its products fully isolated and provides multiple security protections with its basic network. Container service is a typical example. It adopts [Tencent Cloud's Private Network VPC](/doc/product/215/535) with more network features as its underlying network. This document mainly introduces the best practices of the security group under the container services to help you select an appropriate security group policy.

## Security Group
Security Group is a virtual firewall that allows state-based packet filtering. As an important network security isolation tool, it is used to set network access control for one CVM or multiple CVMs. For more information about security groups, please see [Security Group](/doc/product/213/5221).

## Principles on Security Group Selection with Container Services
1. In a container cluster, the service pods are deployed with the distributed method. In such case, different service pods are deployed on the combination of cluster nodes. It is recommended to bind the CVMs under the same cluster to the same security group and no other CVMs should be added to this security group for this cluster.
2. Security groups only grant the minimum permission externally.
3. It is required to open the following container service rules to the Internet:
 - Open the container pod network and cluster node network to Internet.
 When a service access reaches the CVM nodes, the request will be forwarded to any pod of the service upon the iptables rules set by the Kube-proxy module. As the service pods may be located on another node, cross-node access will occur at this time. The access destination IP serves as the service pod IP and node IP (or the bridge IP of Cluster cbr0 on nodes). It is required to open the container pod network and cluster node network to Internet on correspond nodes.
 - Container network and node network need to be opened for accesses across different clusters in the same VPC
 - Port 22 in SSH login node
 - Ports on Node 30000 - 32767
 In the access path, it is required to forward data packets to NodeIP: NodePort of the container cluster via the load balancer, where NodeIP is the CVM IP of any node in the cluster, and NodePort is assigned by the container cluster by default when creating the service. The range of NodePort is between 30000 and 32768.
 The following figure shows an example of the public network access service:
![Public Network Load Balancer Access](https://mc.qcloudimg.com/static/img/497412acf075bdf5d098b4f0ff36bbad/image.png)

## Suggestions
It is recommended to configure security groups for the cluster with the security group templates provided by the container services. The detailed security group configuration rules are as follows:

Inbound Rules:

| Protocol | Port | IP Range | Allowed | Description |
|:--------:|:---------:|:-------:|:--------:|:---------:|
| TCP | 30000-32768	| 0.0.0.0/0	| Yes | Permit Port 30000-32768 to be accessed by all IPs via TCP |
| UDP |	30000-32768	| 0.0.0.0/0	| Yes | Permit Port 30000-32768 to be accessed by all IPs via UDP |
| ALL | traffic	ALL |	10.0.0.0/8 | Yes | Open the private network IP range of 10.0.0.0/8 to Internet |
| ALL | traffic	ALL	| 172.16.0.0/12 |	Yes | Open the private network IP range of 172.16.0.0/12 to Internet |
| ALL | traffic ALL	| 192.168.0.0/16	| Yes | Open the private network IP range of 192.168.0.0/16 to Internet |
| TCP | 22 |	0.0.0.0/0 |	Yes | Permit Port 22 to be accessed by all IPs |
| ALL | traffic	ALL |	0.0.0.0/0	| No | No existing rules have been met, so it is denied |

Outbound Rules

| Protocol | Port | IP Range | Allowed | Description |
|:--------:|:---------:|:-------:|:--------:|:---------:|
| ALL | traffic	ALL | 0.0.0.0/0 | Yes | Open all rules to Internet |


With this rule configured for container nodes, services in the cluster can be accessed via different access methods.
For more information on methods of accessing services in clusters, see [Configuration of Service Access Methods](/doc/product/457/9098).

