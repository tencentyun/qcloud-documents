Node network and container network are the most fundamental attributes of a cluster. You can implement the network segmentation of a cluster by setting node network and container network.
- Node network: The system assigns the IP addresses within the node network address range to the CVMs in the cluster. A node network is a Tencent Cloud VPC. You can choose a subnet in the VPC as the node network of the cluster. For more information, please see [Private Network and Subnet](/doc/product/215/4927).
- Container network: The system assigns the IP addresses within the container network address range to the containers in the cluster. You can customize three private IP address ranges as the container network.

### Relationship between node network and container network

- IP address ranges of node network and container network cannot conflict with each other.
![Alt text](https://mc.qcloudimg.com/static/img/5203063dbc974a10c88e359e2d0001e7/%7BE7F54078-0576-4F44-A0B7-F54A087C7B1D%7D.png)
- IP address ranges of the container networks of different clusters in the same VPC cannot conflict with each other.
![Alt text](https://mc.qcloudimg.com/static/img/b981fb679ef28fc6f380d133748b5727/%7BBD3BDC73-D210-4919-8F01-A04D4D6A7963%7D.png)
- In case of a conflict between container network and VPC routing, the container network is preferably adopted for forwarding.
![Alt text](https://mc.qcloudimg.com/static/img/e16d6102276c066147ba195a9662cbbb/%7BF9702455-675D-4592-B554-CB9BFFF47B4C%7D.png)
### Communication between container network and other Tencent Cloud resources
- Containers in a cluster are interconnected with each other.
- Containers in a cluster are directly interconnected with nodes.
- Containers in a cluster are interconnected with [Cloud Databese](https://cloud.tencent.com/product/cdb-overview), [Cloud Redis](/doc/product/239/3205) and [Cloud Memcached](/doc/product/241/7489).

Container pod can directly access resources within a VPC or containers in the same cluster. If not, access via SNAT.
![Alt text](https://mc.qcloudimg.com/static/img/4c0acc784a1d1442432f0100164164fb/%7BE2DCADA4-CCAF-4C81-8CD1-C51EF086978C%7D.png)



