## Network Settings of Container and Node

Node network and container network are fundamental attributes of the cluster. You can plan the network segmentation of a cluster by setting up node network and container network.

- Node network: IP address within the node network address range will be assigned to the cluster CVM. A node network is a VPC of Tencent Cloud. You can choose the subnet in private network for the node network of the cluster. For more information on private network, please see [here](https://www.qcloud.com/document/product/215/4927).
- Container network: IP address within the container network address range will be assigned to the cluster container. You can customize three private IP address ranges as the container network.

### Relationship Between Node Network and Container Network

- No conflict between IP address ranges of node network and container network is allowed

![Alt text](https://mc.qcloudimg.com/static/img/5203063dbc974a10c88e359e2d0001e7/%7BE7F54078-0576-4F44-A0B7-F54A087C7B1D%7D.png)

- No conflict between IP address ranges of different cluster containers is allowed in the same VPC.

![Alt text](https://mc.qcloudimg.com/static/img/b981fb679ef28fc6f380d133748b5727/%7BBD3BDC73-D210-4919-8F01-A04D4D6A7963%7D.png)

 - When the container network and VPC route conflict, the container network is preferably adopted for forwarding.

![Alt text](https://mc.qcloudimg.com/static/img/e16d6102276c066147ba195a9662cbbb/%7BF9702455-675D-4592-B554-CB9BFFF47B4C%7D.png)
### Connection Between Container Network and Other Resources of Tencent Cloud
- Connection between containers in the cluster
- Connection between cluster container and node
- Connection between cluster container and such resources as CDB, Redis, and Cloud Memcached


Container pod can access resources in VPC or containers in the same cluster. If not, use SNAT.
![Alt text](https://mc.qcloudimg.com/static/img/4c0acc784a1d1442432f0100164164fb/%7BE2DCADA4-CCAF-4C81-8CD1-C51EF086978C%7D.png)

