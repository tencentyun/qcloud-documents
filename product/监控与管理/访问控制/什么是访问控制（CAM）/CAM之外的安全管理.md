## 概述
通过访问管理 CAM，可以控制子用户通过腾讯云控制台或者云 API 执行的操作。除此之外，云上产品也有一些资源操作保护的措施，本文仅提供部分示例供您参考。

## 示例

#### 云服务器 CVM

为保证实例的安全可靠，腾讯云提供两种加密登录方式： [密码登录](https://cloud.tencent.com/doc/product/213/6093) 和 [SSH 密钥对登录](https://cloud.tencent.com/document/product/213/6092)，其中在配置 Linux 云服务器时您可以选择 SSH 密钥作为云服务器加密登录方式。

根据云服务器操作系统的不同，您可以参考以下文档，在创建云服务器时选择不同的加密登录方式。

- [自定义配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/10516)
- [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517)

#### 云数据库 MySQL

在云数据库 MySQL 中，需要使用与数据库关联的用户名称和密码来登录。

同时在云数据库 MySQL 实例详情中，选择**数据库管理** > **帐号管理**，您可以创建和管理用于登录该数据库的帐号。

关于云数据库 MySQL 帐号管理的详细说明，请参考 [云数据库 MySQL - 创建帐号](https://cloud.tencent.com/document/product/236/35794)。

#### 安全组

在访问云服务器 CVM 和云数据库 MySQL 时，可以通过配置安全组来指定可以访问的端口和 IP 等。

关于安全组的详细说明，请参考 [云服务器 - 安全组概述](https://cloud.tencent.com/document/product/213/12452)。

## 总结
如上所述的控制能力并不是 CAM 的一部分，CAM 支持您控制腾讯云产品的方法包括创建或终止 CVM 实例、修改安全组规则等。CAM 可以帮助您控制通过云 API 向腾讯云发起的任务执行请求，或者是在腾讯云控制台的操作。但是，CAM不会帮助您管理诸如登录操作系统 (CVM)、云数据库 MySQL 等任务的安全性。
