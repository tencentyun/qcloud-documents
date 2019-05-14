节点网络与容器网络是集群的最基本属性。通过设置节点网络和容器网络可以规划集群的网络划分。
- 节点网络：将为集群内主机分配在节点网络地址范围内的 IP 地址，节点网络为腾讯云的私有网络，您可以选择私有网络中的子网用于集群的节点网络，更多私有网络介绍可看 [私有网络和子网](/doc/product/215/4927) 。
- 容器网络：将为集群内容器分配在容器网络地址范围内的 IP 地址，您可以自定义三大私有网段作为容器网络。

### 节点网络与容器网络的关系

- 节点网络和容器网络网段不能冲突
![Alt text](https://mc.qcloudimg.com/static/img/5203063dbc974a10c88e359e2d0001e7/%7BE7F54078-0576-4F44-A0B7-F54A087C7B1D%7D.png)
- 同一 VPC 内，不同集群容器网络网段不能冲突
![Alt text](https://mc.qcloudimg.com/static/img/b981fb679ef28fc6f380d133748b5727/%7BBD3BDC73-D210-4919-8F01-A04D4D6A7963%7D.png)
- 容器网络和 VPC 路由冲突时，优先在容器网络内转发
![Alt text](https://mc.qcloudimg.com/static/img/e16d6102276c066147ba195a9662cbbb/%7BF9702455-675D-4592-B554-CB9BFFF47B4C%7D.png)
### 容器网络与腾讯云其他资源通信
- 集群内容器与容器之间互通
- 集群内容器与节点直接互通
- 集群内容器与 [云数据库CDB](https://cloud.tencent.com/product/cdb-overview)、[云存储Redis](/doc/product/239/3205)、[云缓存Memcached](/doc/product/241/7489) 等资源直接互通

容器实例访问 VPC 内资源或者同集群容器时，能够直接访问，否则走 SNAT 。
![Alt text](https://mc.qcloudimg.com/static/img/4c0acc784a1d1442432f0100164164fb/%7BE2DCADA4-CCAF-4C81-8CD1-C51EF086978C%7D.png)


