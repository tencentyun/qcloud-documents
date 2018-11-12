Node network and container network are the most fundamental attributes of a cluster. You can implement the network segmentation of a cluster by setting node network and container network.
- Node network: The system assigns the IP addresses within the node network address range to the CVMs in the cluster. A node network is a Tencent Cloud VPC. You can choose a subnet in the VPC as the node network of the cluster. For more information, please see [Private Network and Subnet](/doc/product/215/4927).
- Container network: The system assigns the IP addresses within the container network address range to the containers in the cluster. You can customize three private IP address ranges as the container network.

### Relationship between node network and container network

- IP address ranges of node network and container network cannot conflict with each other.
- IP address ranges of the container networks of different clusters in the same VPC cannot conflict with each other.
- In case of a conflict between container network and VPC routing, the container network is preferably adopted for forwarding.

### Communication between container network and other Tencent Cloud resources
- Containers in a cluster are interconnected with each other.
- Containers in a cluster are directly interconnected with nodes.
- Containers in a cluster are interconnected with [Cloud Databese](https://cloud.tencent.com/product/cdb-overview), [Cloud Redis](/doc/product/239/3205) and [Cloud Memcached](/doc/product/241/7489).

Container pod can directly access resources within a VPC or containers in the same cluster. If not, access via SNAT.



