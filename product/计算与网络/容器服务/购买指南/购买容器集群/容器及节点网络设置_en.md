## Network Settings of Container and Node

Node network and container network are fundamental attributes of the cluster. You can plan the network segmentation of a cluster by setting up node network and container network.

- Node network: IP address within the node network address range will be assigned to the cluster CVM. A node network is a VPC of Tencent Cloud. You can choose the subnet in private network for the node network of the cluster. For more information on private network, please see [here](https://cloud.tencent.com/document/product/215/4927).
- Container network: IP address within the container network address range will be assigned to the cluster container. You can customize three private IP address ranges as the container network.

### Relationship Between Node Network and Container Network

- No conflict between IP address ranges of node network and container network is allowed
- No conflict between IP address ranges of different cluster containers is allowed in the same VPC.
 - When the container network and VPC route conflict, the container network is preferably adopted for forwarding.

### Connection Between Container Network and Other Resources of Tencent Cloud
- Connection between containers in the cluster
- Connection between cluster container and node
- Connection between cluster container and such resources as CDB, Redis, and Cloud Memcached


Container pod can access resources in VPC or containers in the same cluster. If not, use SNAT.


