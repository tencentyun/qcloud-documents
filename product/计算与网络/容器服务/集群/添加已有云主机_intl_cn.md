## 添加已有云主机
### 概述
腾讯云容器服务支持新增节点到容器集群，同时也支持添加已有的云主机到集群内。
当前添加已有云主机到集群功能仅支持与集群在同一VPC内的主机，敬请期待基础网络和不同VPC内的云主机资源复用。

### 操作方法
1.在集群列表页中选择某集群的ID/节点名，点击【节点列表】，选择添加已有节点。

![Alt text](https://mc.qcloudimg.com/static/img/0cec75d91713f2b61f96dc8b6f70aa6d/Image+003.png)

2.选择需要添加到集群的云主机。

![Alt text](https://mc.qcloudimg.com/static/img/65e0be4baeed62090ac7e5c7111b8b3d/Image+004.png)

3.设置节点的登录方式，点击【完成】。

![Alt text](https://mc.qcloudimg.com/static/img/cd2e37ee6af64ad695a7780f4b7eb980/Image+005.png)

### 限制条件
1. 当前仅支持添加同一VPC下的云主机。
2. 添加存量的云主机到集群，将重装改云主机的操作系统。