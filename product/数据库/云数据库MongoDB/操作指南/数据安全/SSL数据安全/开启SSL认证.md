## 操作场景
SSL（Secure Sockets Layer）认证是客户端到云数据库服务器端的认证，对用户和服务器进行认证。开通 SSL 加密，可获取 CA 证书，将 CA 证书上传在服务端。在客户端访问数据库时，将激活 SSL 协议，在客户端和数据库服务端之间建立一条 SSL 安全通道，实现数据信息加密传输，防止数据在传输过程中被截取、篡改、窃听，保证双方传递信息的安全性。 
>?SSL 认证当前在各地域逐步发布中，如需提前体验，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。

## 计费说明
开启 SSL，不收取任何费用，您可免费使用。

## 使用前须知
- 开启 SSL 过程中，需要重启实例，请在业务低峰期进行，或确保应用有重连功能。
- 开启 SSL 访问，保障数据访问及传输的安全，会显著增加 CPU 使用率，建议在有加密需求时才开通 SSL 加密。
- 开启 SSL 之后，证书过期前30天、15天、3天发送过期事件告警，请注意及时刷新 SSL 证书，否则无法通过 SSL 证书认证访问。

## 版本说明
- 新建实例：数据库版本4.0、4.2均支持开通 SSL 认证。
- 存量已有实例：数据库版本为3.6，需升级版本至4.0才支持开启 SSL 认证。

## 前提条件
- 数据库实例状态：运行中，无其他任务执行。
- 当前为业务低峰时刻，或客户端具有自动重连机制。

## 操作步骤
1. 登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)。
2. 在左侧导航栏 **MongoDB** 的下拉列表中，选择**副本集实例**或者**分片实例**。副本集实例与分片实例操作类似。
3. 在右侧实例列表页面上方，选择地域。
4. 在实例列表中，找到目标实例。
5. 在目标实例的**实例 ID / 名称**列，单击蓝色字体的实例 ID，进入**实例详情**页面。
6. 单击**数据安全**页签，再选择**访问加密**页签。
7. 在**开启 SSL** 后面，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/84853fe19aa340a98cc138f8d951ddb9.png" style="zoom: 25%;" />。
8. 在**提示**对话框，了解开启 SSL 的影响，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b46c6404a27d3b9a361484b34c0fb60a.png"  style="zoom:50%;">
9. 等待**开启 SSL**的状态为**已开启**，单击**下载证书**。
如果收到证书到期的告警信息，证书已经到期无效，请先单击**刷新证书**，更新证书文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/459637e4bd877c2fe738b54d4b909d72.png" style="zoom:67%;" />
10. 在页面左下角，获取证书 **MongoDB-CA.crt**。
11. 通过 Mongo Shell 方式连接数据库，请参见 [使用 Mongo Shell 通过 SSL 认证连接数据库](https://cloud.tencent.com/document/product/240/76360)。
通过多语言 SDK 连接数据库，请参见 [使用多语言 SDK 通过 SSL 认证连接数据库](https://cloud.tencent.com/document/product/240/76361)。

