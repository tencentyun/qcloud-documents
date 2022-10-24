## 操作场景

本文介绍通过 TDMQ 控制台创建一个专享集群，并通过开源 RabbitMQ 控制台创建 Vhost、Exchange 和 Queue 等资源的操作步骤，了解运行一个客户端之前所需要进行的资源准备。

## 操作步骤

### 步骤1：新建集群

1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)。
2. 在左侧导航栏选择 **rabbitmq** 下的集群管理，单击**新建集群**，进入购买页面。
3. 在购买页面，选择要购买的实例规格，单击**立即购买**，完成集群创建。
4. 单击集群的“ID”，进入基本信息页面，在**网络信息**模块，得到服务端的连接信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/04d5cad31290beb1445625c8bf373031.png)



### 步骤2：新建 Vhost

1. 单击刚刚创建好的集群的“ID”，进入基本信息页面。
2. 在**网络信息**模块，通过 **Web 控制台**中的访问地址和用户名密码登录开源 RabbitMQ 控制台。
3. 选择页签 **Admin** > **Virtual Hosts**，新建一个 Vhost。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b2c8ec0857bb5bdaf9adafa286adfc54.png)



### 步骤3：创建 user 并授权

1. 选择页签 **Admin** > **user**，新建一个 user。
   ![](https://qcloudimg.tencent-cloud.cn/raw/22bbaa24d4ef45d2654a47340dcae2d5.png)
2. 单击已经创建好的 user 名称，进入授权页面。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3abc8b667f6dc235f6798424602b5819.png)
3. 给创建好的 user 授予访问已创建好的 Vhost 权限。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b6480d63c579de5e05a84c1e96afe474.png)



### 步骤4：创建 Exchange

在页面顶部选择 **Exchanges**，单击 **Add a new exchange**，选择创建好的 Vhost，填写 exchange 名称，新建一个 exchange。

![](https://qcloudimg.tencent-cloud.cn/raw/96a030e68d04ba789864445825679e5b.png)



### 步骤5：创建 Queue

在页面顶部选择 **Queues** 页签，单击 **Add a new queue**，选择创建好的 Vhost，填写 queue 名称，新建一个 queue。

![](https://qcloudimg.tencent-cloud.cn/raw/c1c3fc32b12ceccd020e83a7837fdf4a.png)



### 步骤6：绑定路由关系

1. 在 **Queues** 页签下，单击创建好的 Queue 的名称，进入 Queue 详情页面。
   ![](https://qcloudimg.tencent-cloud.cn/raw/57b820d50ca66cf84c3c99692bee2a6b.png)
2. 在 **Binding** 栏，创建一条路由关系。
   ![](https://qcloudimg.tencent-cloud.cn/raw/293c5b9f7a4f1a286af2d59c09e8123b.png)

