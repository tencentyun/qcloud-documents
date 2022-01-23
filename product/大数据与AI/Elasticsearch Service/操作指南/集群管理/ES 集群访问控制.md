ES 集群部署在逻辑隔离的私有网络 VPC 中，我们提供了丰富的能力来切实保证云上资源的安全性，包括：
- 对腾讯云帐户下资源的 CAM 访问管理（参见 [CAM 访问控制配置](https://cloud.tencent.com/document/product/845/19550)）
- ES 集群访问密码/ES 集群用户登录认证
- 设置 Kibana 和 Cerebro 外网访问 IP 黑白名单，或限制 Kibana 和 Cerebro 仅能通过内网访问
- 对 ES 集群有限开启外网访问和设置 IP 白名单
- 提供的基于角色的访问控制（RBAC）

## 设置 ES 集群访问密码
在创建腾讯云 ES 集群时，会要求用户设置默认用户 elastic 的密码，该帐号和密码用于 Kibana 页面登录，若集群已开启 [ES 集群用户登录认证](https://cloud.tencent.com/document/product/845/42868)，则此用户名和密码还会用于 ES 集群的登录认证，提供进一步的安全防护，详情如下：
![](https://main.qcloudimg.com/raw/a6bf26dc63191403fe0a9e5b7a69d663.png)

## 重置 ES 集群访问密码
用户需要调整 ES 集群访问密码时，可以通过集群详情页的密码重置功能对 ES 集群 elastic 账号的密码进行重置，操作页面如下：
![密码重置](https://main.qcloudimg.com/raw/ddc3819595b60656c21c8f93349f31f0.png)

## 设置 Kibana 公网访问 IP 黑白名单
由于 Kibana 页面是默认通过公网访问，在进行密码校验的基础上，ES 还为 Kibana 访问提供了 IP 黑白名单功能，进一步保障用户集群的访问安全性。

Kibana 公网访问白名单默认为127.0.0.1，表示不允许所有 IPv4 和 IPv6 地址访问，此时单击 kibana 访问入口时，会弹窗引导用户去进行白名单设置，如下图。
![](https://qcloudimg.tencent-cloud.cn/raw/2cac2b9b82c12b64b5da98d63d9d298f.png)
在集群的**可视化配置**界面可以设置 Kibana 公网访问 IP 黑白名单：
- 配置规则：支持多个 IP，IP 之间以英文逗号分隔，格式为192.168.0.1,192.168.0.0/24，最多支持50个。
- 黑白名单设置：客户可以设置任意一个，如果黑白名单都配置，以白名单为准。

![](https://qcloudimg.tencent-cloud.cn/raw/6ca6bf3b9b7417f9291207494903f550.png)

## 限制 Kibana 仅能通过内网访问
如果用户担心公网访问安全性，也可以关闭外网访问，设置仅允许内网访问。
![](https://qcloudimg.tencent-cloud.cn/raw/84f663cc32800d8a40ed6853e4ccbfb4.png)

## 有限开启 ES 集群外网访问和设置 IP 白名单

基于安全考虑，ES 集群外网访问是默认关闭的，对于已开启 [ES 集群用户登录认证](https://cloud.tencent.com/document/product/845/42868) 的集群，允许用户基于使用便捷性的需要开启外网访问，但必须同时设置 IP 白名单以提供安全防护。
![](https://main.qcloudimg.com/raw/9a5888a6532da74b4a8def5f78fead62.png)

## 基于角色的访问控制（RBAC）

对于已开启 [ES 集群用户登录认证](https://cloud.tencent.com/document/product/845/42868) 的集群，用户将获得更多安全管理功能。白金版还可以进一步支持基于文档、字段级别的细粒度访问控制，详情请参考 Elastic 官网文档 [基于角色的访问控制](https://www.elastic.co/guide/en/elasticsearch/reference/current/authorization.html)。

### 角色管理

用户可以在 Kibana 的 **Management > Security > Roles** 中创建、修改和删除具有不同权限组合的角色，详情如下：
![](https://main.qcloudimg.com/raw/22af168b4bab7271f2b6ca4f76a3cd48.jpg)

### 用户管理

用户可以在 Kibana 的 **Management > Security > Users** 中创建、修改（信息修改、密码修改等）和删除具有多个角色的用户，详情如下：

> ! ES 内置用户 elastic 的密码只能在官网控制台进行重置。
> 
![](https://main.qcloudimg.com/raw/81241d5ba1c5cb6303fde291d931d7bd.png)

更多相关安全功能使用可以参考：
- [保护您在 Elastic Stack 中的数据](https://www.elastic.co/what-is/elastic-stack-security) 
- [Kibana XPACK SECURITY](https://www.elastic.co/guide/en/kibana/current/xpack-security.html)
- [ES SECURITY API](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api.html)
