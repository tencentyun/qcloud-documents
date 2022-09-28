腾讯云 ES 目前已经提供了多可用区部署，即支持同地域跨机房的高可用容灾方案，满足了绝大多数客户的需求。但是依然会有部分客户希望进一步提升容灾级别，能够做到跨地域容灾。随着腾讯云 ES 双网卡功能的发布，使得跨地域容灾成为可能。接下来将介绍下腾讯云 ES 实现跨地域容灾的详细步骤。
>? 由于腾讯云 ES 集群的证书是相互独立的，因此在搭建 CCR 环境之前，请先 [提交工单](https://console.cloud.tencent.com/workorder/category)，腾讯云助手会将两个集群证书设置为一致。

## 对等连接
1. 首先将北京和上海的两个 vpc 建立对等连接，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bfd6bbf34b42e99e295887bb61bde458.png)
>! 如果两个 vpc 的网段有冲突则不能建立对等连接。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1ccd733ec92df72539e577e3541c6193.png)
2. vpc 之间建立好对等连接后需要配置下路由表。 
一定要在本端和对端都配置相关路由，才能通过对等连接通信，且需要绑定对应云服务器的子网。
其中路由策略配置如下： 
路由表通过路由策略来实现流量走向控制，路由策略由目的端、下一跳类型和下一跳组成：
    - 目的端：目的端即为您要转发到的目标网段。目的网段描述仅支持网段格式，如果您希望目的端为单个 IP，可设置掩码为32（如172.16.1.1/32）。另外，目的端不能为路由表所在私有网络内的 IP 段，原因是 Local 路由已表示此私有网络内默认内网互通。
    - 下一跳类型：私有网络的数据包的出口。私有网络下一跳类型支持 “NAT 网关”、“对等连接”、“VPN 网关”、“专线网关”、“云服务器”等类型。
    - 下一跳：指定具体跳转到的下一跳实例（使用下一跳 ID 标识），如私有网络内的某个具体 NAT 网关。
3. 在本地端(北京)新增目的端的路由策略。 
![](https://qcloudimg.tencent-cloud.cn/raw/596540e430f3fc0f5509aead7a345c40.png)
4. 在目的端（上海）同样执行上面的操作。 
5. 对等连接建立好，且路由表配置完成后，我们进入到北京的云服务器中尝试连接上海的云服务器。
从北京的 cvm 上ping 上海的 cvm： 
![](https://qcloudimg.tencent-cloud.cn/raw/2a86e5055b387773f92f545b26713de7.png)

## 搭建 CCR
下面我们就分别在北京和上海使用对应的 vpc [购买两个 ES 集群](https://buy.cloud.tencent.com/es)。 
上海集群：
![](https://qcloudimg.tencent-cloud.cn/raw/c49fe6b1e3ec45e75d01f075dc34192e.png)
北京集群：
![](https://qcloudimg.tencent-cloud.cn/raw/cd9be0d47a66004b1090d6e047270e59.png)
我们将北京的 ES 集群作为 **Leader Cluster**，把上海的 ES 集群作为 **Follower Cluster**。
### 设置 Remote Cluster
1. 登录到上海的 kibana 进行 CCR 的相关配置。
将北京的 ES 集群设置为 Remote Cluster：
![](https://qcloudimg.tencent-cloud.cn/raw/0839d9aa631740eafec6b1d51d10ed38.png)
2. Connected 表示已经连接上远端的 ES 集群了：
![](https://qcloudimg.tencent-cloud.cn/raw/05d379aae599c8385e956f847a8240bd.png)


### 创建 Follower Index
1. 首先需要先在 Leader Cluster 即北京 ES 集群中创建一个索引：
![](https://qcloudimg.tencent-cloud.cn/raw/f3adc021f006f4b63eee005bc77dbb3e.png)
2. 在上海的集群中继续创建 Follower Index：
![](https://qcloudimg.tencent-cloud.cn/raw/410486692f16501b32f4c0cb3c14c7e6.png)
3. 在 Follower 上海集群的 kibana 中进行如下配置：
![](https://qcloudimg.tencent-cloud.cn/raw/5eb2fbaf4ac7592679a35379160bea8f.png)
4. 主要是配置前面设置的 Remote Cluster的name，以及 Leader Index 和本地集群需要 Follower的index。 
配置完成后得到如下的列表： 
![](https://qcloudimg.tencent-cloud.cn/raw/8cba351c0de9e820cca4e25d1d10665a.png)
5. 查看索引管理，发现已经在上海的集群中创建了一个 follower index：
![](https://qcloudimg.tencent-cloud.cn/raw/23e1fb396f88b6f2d7aa9d988f051af2.png)

这时候索引里还没有任何数据，doc 数量是0。下面我们在北京的 Leader 集群中写入几条数据，再看上海的 Follower 集群是否能够同步到。 

### 数据同步
1. 首先我们在北京集群的 kibana 中写入如下几条数据： 
![](https://qcloudimg.tencent-cloud.cn/raw/2794efbf3944ce4fc3aabbb88ae730cd.png)
2. 查看 Leader 北京的集群的 index manager：
![](https://qcloudimg.tencent-cloud.cn/raw/df6ea8f461327ebcc20f5d120ca0a876.png)
3. 发现四条数据都写入了。目前的 doc 数量是4。
4. 下面我们再去 Follower 上海集群的 kibana 上查看 Index Manager。 
![](https://qcloudimg.tencent-cloud.cn/raw/0e293b2eeffe3ee3782b3858c34b409d.png)
5. 发现上海的 Follower 集群中的 Follower 索引 wurong_sh_index 也包含了4条 doc 数据。说明我们已经完成了跨地域跨集群的复制了。 

至此，我们完成了跨地域复制的数据同步。
>? 由于是跨地域打通了网络，如果出现下面的 Not connected 状态，可能会出现网络不稳定的情况，会导致数据的复制有一定的延迟。 
>
![](https://qcloudimg.tencent-cloud.cn/raw/3b95492f6329657dfdc8e7ac862426c0.png)
