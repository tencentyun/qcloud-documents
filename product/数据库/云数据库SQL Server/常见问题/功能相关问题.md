### SQL Server 是什么？
SQL Server 是微软公司推出的关系型数据库，SQL Server 具有可扩展、高性能等特点，可以对数据进行查询、搜索、同步、报告和分析之类的数据库。到目前为止，SQL Server 已经发布多个版本，每个版本都有其独特的特点。
云数据库现已支持 SQL Server 2008 R2 SP3、2012 SP3、2016 SP1，该版本允许使用 Microsoft .NET 和 Visual Studio 开发的自定义应用程序，在面向服务的架构（SOA）和通过 Microsoft BizTalk Server 进行的业务流程中使用数据等许多新的特性和关键的改进，使得它成为至今为止的最强大和最全面的 SQL Server 版本之一。您可以在云上轻松设置、操作和扩展 SQL Server 部署，让您能够轻松应对业务需求的快速变化。

### 云数据库 SQL Server 产品架构是怎样的？
云数据库 SQL Server 由一主一镜像的 SQL Server 数据库组成，跨机架部署，每个库对应一组监控 Agent，通过心跳对数据库进行实时监控。独立部署的两组决策，调度集群和配置集群组成，作为集群的管理调度中心，主要管理数据库节点组、接入网关集群、HDFS 的的正常运行。Hadoop 分布式文件系统（HDFS）提供数据灾备服务，提供冷备数据。接入网关集群，对外提供唯一的 IP，如果数据节点发送切换，IP 不会改变。

### 云数据库 SQL Server 如何创建实例并连接到数据库？
您可以通过 SQL Server 的管理控制台页面来完成管理数据库相关工作。
具体操作方法参见 [创建并连接数据库](https://cloud.tencent.com/document/product/238/7516)。

### 云数据库 SQL Server 实例帐号如何管理？
云数据库 SQL Server 禁止通过 Microsoft SQL Server Management 执行创建、删除数据库、创建、删除或修改账号操作，支持在 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver) > 实例详情页 > 【帐号管理】，创建、删除帐号或修改帐号权限。
目前仅支持用户使用“读写”、“只读”权限，如果需要更高级别的权限，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请（不提供 sa 账号）。

### 云数据库 SQL Server 实例如何监控？
云数据库 SQL Server 支持 SQL Server 常见的25种参数，您可以通过配置 SSMS 的计数器，额外统计其他参数，详情参见 [监控告警](https://cloud.tencent.com/document/product/238/7524)。
目前支持通过腾讯云云监控对以下监控指标进行告警，您可以在【[云监控](https://console.cloud.tencent.com/monitor/overview)】>【告警配置】>【告警策略】里面配置告警。
- CPU 利用率
- 连接数
- 输入流量
- 输出流量
- IOPS
- 存储空间

### 云数据库 SQL Server 实例如何回档？
云数据库 SQL Server 的全量备份和日志备份保存7天，因此可以回档到7天内的任意时刻。
具体操作方法参见 [数据库实例回档](https://cloud.tencent.com/document/product/238/7522)。

### 云数据库 SQL Server 实例如何备份？
云数据库 SQL Server 控制台中可以通过下载的备份文件将数据库恢复到其他实例（如自建实例）上。
具体操作方法参见 [数据库实例备份](https://cloud.tencent.com/document/product/238/7523)。


### 云数据库 SQL Server 如何迁移数据？
云数据库 SQL Server 支持 [云服务器自建 SQL Server 迁移数据](https://cloud.tencent.com/document/product/238/32585) 和 [COS 迁移 SQL Server 数据](https://cloud.tencent.com/document/product/238/19103)。

### 云数据库 SQL Server 升级流程是怎样的？
升级操作指将现有云数据库 SQL Server 实例的规格升级到更高规格。
1. 在 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver) 中选择选择相应的实例，在【操作】列，单击【升级】。
2. 在弹出的升级页，根据需要选择目标规格，并支付费用，成功后系统将自动升级实例规格。
升级费用 =（目标规格单价 - 原规格单价）x 剩余到期时间

>?
>- 只能向更大规格实例进行升级，不支持降级。
>- 升级过程中，不能取消本次升级操作。


### SQL Server 中 Windows 客户端上传工具如何使用？
1. 将“Windows 客户端上传工具”下载至本地后，将其解压到任意文件夹（文件夹路径请勿包涵中文），解压后获得 “bin” 和 “etc” 文件目录。
2. 为保证用户的数据安全，在上传备份之前，需要编辑配置文件 etc\conf.json，填写用户自己的 API 密钥（secretId 和secretKey），请务必保存好自己的 API 密钥，切勿泄漏。为保证传输过程的稳定性，此工具已经支持断点续传功能。
**conf.json 文件请存储为“UTF8 无 BOM 格式”（Windows 下建议用 notepad++ 转换编码）。**
![](https://main.qcloudimg.com/raw/b79bd31b582f82c00ce36d81856bc2b5.png)
3. 打开 Windows 命令行，进入解压后的“Windows 客户端上传工具”目录，调用 bin 目录下的 upload-tool.exe 完成上传操作。upload-tool.exe 有两个参数 –r 和 –p。–p 表示备份文件在本地的绝对路径；–r 表示中转存储所处的地域（请选择您的腾讯云数据库所在地域）。
![](https://main.qcloudimg.com/raw/012b37a5b851138c1dbd464344c05db2.png)

**地域对照（标识区分大小写）**

| 地域 | -r 参数 | 
|:---------:|:---------:|
| 广州 | gz | 
| 上海 | sh | 
| 香港 | hk | 
| 上海金融 | shjr | 
| 北京 | bj | 
| 深圳金融 | szjr | 



