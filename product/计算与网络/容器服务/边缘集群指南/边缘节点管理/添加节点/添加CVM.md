本文介绍如何向已创建的边缘集群中添加腾讯云标准的 CVM 节点。您可以直接购买所需地域的腾讯云 CVM，将其直接加入边缘集群提供服务。这里和标准 TKE 托管集群的区别是，您可以购买不同地域不同 VPC 下的 CVM 节点加入同一个边缘集群，而不需要限制在边缘集群创建时所选择的 VPC 下。

## 前置条件
请参考 [集群开启内外网访问](https://cloud.tencent.com/document/product/457/83206) 使能**外网访问**能力。

## 创建 CVM 节点
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在集群管理页，单击需要创建 CVM 节点的边缘集群 ID，进入该集群详情页。
3. 选择页面左侧**节点管理** > **节点**，进入节点列表页面，单击**创建cvm节点**。如下图
![创建 CVM](https://qcloudimg.tencent-cloud.cn/raw/80bb7dc932df0d7b5f1cf12dd00c30e9.jpg)
4. 在“新建节点”页面，根据实际需求配置相关参数。这里的参数和 TKE 添加节点类似，详情请参见 [新增节点](https://cloud.tencent.com/document/product/457/32203)。
