## 概述
在您在腾讯云购买创建 Doris 集群后，从 [集群列表](https://console.cloud.tencent.com/cdwdoris) 页面单击**集群 ID/名称** 可以进入集群详情页。其中网络信息部分提供两个访问地址：tcp & http，分别对应了两种不同的客户端。其中 tcp 地址适合 JDBC 类客户端，最适合也最常用的就是 mysql。而 HTTP 客户端用于通过各类 HTTP 客户端调用 Doris 集群的 REST API 进行各种操作。下面分别进行描述。
![](https://qcloudimg.tencent-cloud.cn/raw/13469c304ee79c967eda96fc6fd1964c.png)

## Mysql / JDBC 类客户端
Doris 采用 MySQL 协议，高度兼容 MySQL 语法，支持标准 SQL，用户可以通过各类客户端工具来访问 Doris，并支持与 BI 工具的无缝对接。借助 MySQL 协议，用户使用任意 MySQL 的 ODBC/JDBC以及MySQL 的客户端，都可以直接访问 Doris。当然，其中最好用的是 MySQL 的客户端。
![](https://qcloudimg.tencent-cloud.cn/raw/c2e787d644c7e8c96c0cbbe1f0b4af73.png)

>! 只要支持 Mysql JDBC 协议的客户端都可使用，不过可能存在 Doris 返回信息没有被此客户端原样展示的情况。这种现象一般没有问题，但在有些情况下可能存在部分信息没有被展示出来，造成对操作结果的误判。例如，执行 broker load 之后返回信息中的 warning 信息很重要，在某些客户端中就没被展示出来，可能会让用户误以为没有 warning（即没有被过滤的数据）。

## HTTP 客户端
HTTP 客户端提供比较丰富的功能，包括数据操作和集群管控的功能。分为 Playgroud，System，Log，QueryProfile，Session，Configuration 几个大的功能页。HTTP 客户端需输入用户名和密码登录，进入后界面示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5c688161c53bb6c1cbc751db9a58e8cf.png)
Playgroud 中提供一个了 SQL 查询编辑器，用于执行各种sql命令。左侧以树形结构展示所有数据库和其下的表。双击表名可查看表的元数据和数据样例，单击`Data Import`后可从本地上传数据到表中。
System 页面可查看 Doris 集群各种系统信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6f9ab8384670325841034e976c926890.png)
Log 页面提供了 FE 日志级别管理的功能和 FE 日志的展示。
![](https://qcloudimg.tencent-cloud.cn/raw/21eb42a44ebeec4d9e950f5eaf337867.png)
QueryProfile 页面展示了记录到Profile的 SQL，并且可查看 SQL 整体以及其中各个 Instance 的执行计划及各类运行数据。
Session 页面展示了当前活动的所有会话的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b44d5f4f4df3838d8f092a3846f83225.png)
Configuration 页面可查看 FE 的所有配置信息，在配置值一列中提供了过滤功能。
![](https://qcloudimg.tencent-cloud.cn/raw/7bdcb99174bbe42265e9a1c39f14843d.png)
**HTTP 客户端实际是基于Doris JDBC 和 Rest API能力 实现的 Web UI 界面**，如果您需要更多基于命令行的Doris的管理能力，可以参考 [Doris Rest Api](https://doris.apache.org/zh-CN/docs/admin-manual/http-actions/fe/connection-action)。

