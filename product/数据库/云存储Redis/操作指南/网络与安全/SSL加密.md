## 操作场景
SSL（Secure Sockets Layer）认证是客户端到云数据库服务器端的认证，对用户和服务器进行认证。开通 SSL 加密，可获取 CA 证书，将 CA 证书上传在服务端。在客户端访问数据库时，将激活 SSL 协议，在客户端和数据库服务端之间建立一条 SSL 安全通道，实现数据信息加密传输，防止数据在传输过程中被截取、篡改、窃听，保证双方传递信息的安全性。
>?SSL 加密当前在各地域逐步发布中，如需提前体验，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。

## 计费说明
开启 SSL，不收取任何费用，您可免费使用。

## 使用前须知
- 开启 SSL 访问，保障数据访问及传输的安全，可能会略影响实例性能。建议仅在有加密需求时才开通 SSL 加密。
- 未开启免密登录， 同时支持 SSL 和非 SSL 两种连接数据库的方式；而开启免密功能之后，且开启了 SSL 加密，就仅能通过 SSL 加密访问数据库。 
- 开启 SSL 加密功能再关闭后，加密连接的客户端程序将无法正常连接。
- SSL 证书有效期为20年。

## 版本架构说明
- 版本说明
 - 新建实例：兼容版本4.0、5.0、6.0均支持直接开通 SSL 加密。如需使用6.0版本，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。
 - 存量已有实例：
   - 兼容版本为2.8，可根据需要升级兼容版本至4.0、5.0或6.0，才能开通 SSL 加密。具体操作，请参见 [版本升级](https://cloud.tencent.com/document/product/239/46457)。
   - 兼容版本为4.0、5.0、6.0，需升级代理版本至5.6.0才能支持。具体操作，请参见 [代理升级](https://cloud.tencent.com/document/product/239/74569)。
- 架构说明
标准架构与集群架构均支持 SSL 加密。

## 前提条件
- 数据库实例状态：运行中，无其他任务执行。
- 当前为业务低峰时刻，或客户端具有自动重连机制。

## 操作步骤
1. 登录 [Redis 控制台](https://console.cloud.tencent.com/redis)。
2. 在右侧实例列表页面上方，选择地域。
3. 在实例列表中，找到目标实例。
4. 在目标实例的**实例 ID / 名称**列，单击实例 ID，进入**实例详情**页面。
5. 单击 **SSL 加密**页签，在 **SSL 加密设置**下方，如果提示需升级版本，请单击**版本升级**，等到版本升级成功。
6. 在**加密状态**后面，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/84853fe19aa340a98cc138f8d951ddb9.png" style="zoom: 25%;" />，显示 **SSL 状态更新中**。
7. 等待**加密状态**显示为**已开通**，如下图所示。单击右上角的**下载证书**。
![](https://qcloudimg.tencent-cloud.cn/raw/914e99f788f4755a6ab08f9baf5aaff2.png)
8. 等待**开启 SSL** 的状态为**已开启**，单击**下载证书**。
9. 在页面左下角，将获取到的证书 **-crt.zip** 放在服务端，使用 SSL 加密方式访问数据库。
客户端 Java 代码连接示例，请参见 [Java 连接示例](https://cloud.tencent.com/document/product/239/30885)；客户端 Python 程序代码连接示例，请参见 [Python 连接示例](https://cloud.tencent.com/document/product/239/30887)。

## 相关 API

| API 接口 | 接口含义 | 
|---------|---------|
| [OpenSSL](https://cloud.tencent.com/document/api/239/81239) | 开启 SSL | 
| [CloseSSL](https://cloud.tencent.com/document/api/239/81240) | 关闭 SSL | 


