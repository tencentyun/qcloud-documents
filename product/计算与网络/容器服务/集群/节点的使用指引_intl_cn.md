节点是指一台已注册到集群内的云服务器，一个集群由 n 个节点组成。腾讯云容器服务支持新增节点到容器集群，同时也支持添加已有的节点到集群内。
>**注意：**
>当前添加已有节点功能仅支持与集群在同一 VPC (私有网络) 内的主机，敬请期待基础网络和不同 VPC 内的云主机资源复用。

## 前提条件
如果之前没有创建过集群，您需要先创建集群。有关如何创建集群的详细信息，参见 [新建集群](/doc/product/457/9091) 。

## 扩展节点
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的【集群】 ，在集群列表中单击右侧 【扩展节点】。
![](//mc.qcloudimg.com/static/img/630fefe69ca2d2bedd779246417f8c70/image.png)
2. 设置新建节点所属 **网络**、**机型** 和 **配置信息**。
![Alt text](https://mc.qcloudimg.com/static/img/74deca5e1fa716c6a0009c43be631870/image.png)
3. 新添加的节点将出现在节点列表中。
![](//mc.qcloudimg.com/static/img/1707fa09977298f255c293aa62b1cc10/image.png)

## 添加已有节点
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的【集群】 ，在集群列表中单击右侧 【添加已有节点】。
![](https://mc.qcloudimg.com/static/img/86909604c01b659736074e92aa83870b/image.png)
3. 在左侧可用节点列表栏选择要添加的节点，选择的节点 ID 将显示在右侧已选择栏。
![](//mc.qcloudimg.com/static/img/991fc9fe1e65e0ab3c80c49043ac639b/image.png)
4. 填写云主机配置。提供三种对应登录方式。
 - **设置密码**：请根据提示设置对应密码。
 - **立即关联密钥**：密钥对是通过一种算法生成的一对参数，是一种比常规密码更安全的登录云服务器的方式。详细参阅 [SSH 密钥](/doc/product/213/503) 。
 - **自动生成密码**：自动生成的密码将通过站内信发送给您。
![](//mc.qcloudimg.com/static/img/54696123752de29c95f72e4345de7afb/image.png)
5. 单击【完成】，新添加的节点将出现在节点列表中。
![](//mc.qcloudimg.com/static/img/0dbd5ce537c8f97f90545d40d45aeafb/image.png)
>**注意：**
>1. 当前仅支持添加同一 VPC 下的云主机。
>2. 添加存量的云主机到集群，将重装改云主机的操作系统。

## 查看节点信息
1. 在集群列表中，单击集群的 **ID/名称** （如 cls-098dghzt）。
![](//mc.qcloudimg.com/static/img/1e07d60a1a1da13cd500ab17a44f0b02/image.png)
2. 进入**节点列表**查看集群节点信息。
![](//mc.qcloudimg.com/static/img/ad5db6f3a9071235e614f856c3ef7083/image.png)

## 移出节点
1. 在集群列表中，单击集群的 **ID/名称** （如 cls-098dghzt）。
![](//mc.qcloudimg.com/static/img/1e07d60a1a1da13cd500ab17a44f0b02/image.png)
2. 进入**节点列表**页面，单击右侧【移出】。
![](//mc.qcloudimg.com/static/img/cbb99d53f194ec9121fe29d840081ab7/image.png)
3. 弹出提示页面，显示要移出的节点信息，单击【确定】删除节点。
![](//mc.qcloudimg.com/static/img/e9194e2947562271931fcc429e5788f8/image.png)
