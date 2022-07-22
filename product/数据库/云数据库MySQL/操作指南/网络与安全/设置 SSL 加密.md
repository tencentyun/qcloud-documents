## SSL 加密概述
SSL（Secure Sockets Layer）认证是客户端到云数据库服务器端的认证，对用户和服务器进行认证。开通 SSL 加密，可获取 CA 证书，将 CA 证书上传在服务端。在客户端访问数据库时，将激活 SSL 协议，在客户端和数据库服务端之间建立一条 SSL 安全通道，实现数据信息加密传输，防止数据在传输过程中被截取、篡改、窃听，保证双方传递信息的安全性。

SSL 协议要求建立在可靠的传输层协议（TCP）之上，其优势在于它是与应用层协议独立无关的，高层的应用层协议（例如：HTTP、FTP、TELNET 等）能透明地建立于 SSL 协议之上。SSL 协议在应用层协议通信之前就已经完成加密算法、通信密钥的协商及服务器认证工作，在此之后应用层协议所传送的数据都会被加密，从而保证通信的私密性。

## 背景
使用非加密方式连接数据库时，在网络中传输的所有信息都是明文，因此存在被非法用户窃听、篡改、冒充的三大风险；而 SSL 协议是为解决这三大风险而设计的，理论上可达到：
- 信息是加密传播，第三方无法窃听。
- 具有校验机制，一旦被篡改，通信双方会立刻发现。
- 配备身份证书，防止身份被冒充。

云数据库 MySQL 支持通过开启 SSL 加密来增强链路安全性，并支持下载和安装 SSL CA 证书到需要的应用服务。
>!SSL 加密不保护数据本身，是确保来往于数据库和服务器之间的流量安全，在传输层对网络连接进行加密，能够提升通信数据的安全性和完整性，但会同时增加网络连接响应时间。

## 前提条件
- 实例版本为 MySQL 5.6/5.7/8.0。
- 实例架构为双节点/三节点。
- 实例引擎为 InooDB/RocksDB。

## 开启 SSL 加密
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb/instance)，在实例列表，单击实例 ID 或操作列的**管理**，进入实例管理页面。
2. 在实例管理页面的**数据安全**页下，选择 **SSL** 页。
![](https://qcloudimg.tencent-cloud.cn/raw/cacf74d49df9fd1d3ecf68e9b056295b.png)
3. 此功能状态默认为未打开，将开关调为开启，然后单击**确定**，开启 SSL 加密。
 - 主实例开启 SSL 窗口如下：
 ![](https://qcloudimg.tencent-cloud.cn/raw/496e876d660522078f06062fbc6d836d.png)
>!开启 SSL 过程中，会重启您的数据库实例以加载 SSL 证书，请确保业务具备重连机制。
>
 - RO 实例开启 SSL 界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/a6fe527d8e4199a3d0f9c49b04f50ab3.png)
>!配置 RO 实例 SSL 功能会同步配置所属 RO 组中其他 RO 实例。
>
4. 单击**下载**，下载 SSL CA 证书。
下载的文件为压缩包（TencentDB-CA-Chain.zip），包含如下三个文件：
 - p7b 文件：用于 Windows 系统中导入 CA 证书。
 - jks 文件：Java 中的 truststore 证书存储文件，密码统一为 tencentdb，用于 Java 程序中导入 CA 证书链。
 - pem 文件：用于其他系统或应用中导入 CA 证书。
 
## 配置 SSL CA 证书
开启 SSL 加密后，使用客户端连接云数据库时需要配置 SSL CA 证书。以下以 Navicat 为例，为您介绍 SSL CA 证书安装方法。其它应用或者客户端请参见对应产品的使用说明。
1. 打开 Navicat。
2. 在对应数据库上单击鼠标右键，选择**编辑连接**。
![](https://qcloudimg.tencent-cloud.cn/raw/b2616fec8f18bef820c74a2236787332.png)
3. 选择 SSL 页签，选择.pem 格式 CA 证书的路径。完成下图设置后单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/df0f9ff3b6478cad06e54f456d9f76c3.png)
>?如果出现 connection is being used 报错，可能由于之前的会话未断开，请关闭 Navicat 后重试。
>
4. 双击对应数据库，测试能否正常连接。
![](https://qcloudimg.tencent-cloud.cn/raw/c39f48b8fb1659588fc8d89e7970acb5.png)

## 关闭 SSL 加密
1. 登录[ MySQL 控制台](https://console.cloud.tencent.com/cdb/instance)，在实例列表，单击实例 ID 或操作列的**管理**，进入实例管理页面。
2. 在实例管理页面的**数据安全**页下，选择 **SSL** 页。
3. 单击已开通前面的开关按钮，在弹出的提示框中单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/2e7dc23dc0d2ddabf2411ba9f33fc1c9.png)
>?关闭 SSL 过程中，会重启您的数据库实例以卸载 SSL 证书，请确保业务具备重连机制。

## 连接开启 SSL 连接加密的实例
使用 SSL 连接加密的方式连接数据库 SQL 如下：
```
mysql -P <端口号> -h <IP 地址>  -u <用户名> -p<密码> --ssl-ca<ca证书>
```
