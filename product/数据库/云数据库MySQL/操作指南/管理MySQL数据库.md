本文介绍云数据库 MySQL 控制台的实例列表页和管理页相关操作，指导您轻松管理 MySQL 数据库。

## 实例列表页
在 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例列表页可查看实例相关信息，以及管理实例。
![](https://main.qcloudimg.com/raw/f4baf638c4f58335e0ee9754f8d4c426.png)

| 功能 | 介绍 | 
|---------|---------|
| 调整配置 | 在实例列表，在操作列点击更多，可对数据库实例进行配置调整（扩缩容），支持实例升级与降级，详细介绍请参见 [调整数据库实例规格](https://cloud.tencent.com/document/product/236/19707)。 | 
| 回档 | 在实例列表，勾选需要回档的实例，选择**更多操作** > **回档**，借助于冷备和 binlog 可以将数据库回档至某个指定的时间，详细介绍请参见 [数据回档](https://cloud.tencent.com/document/product/236/7276)。|
| 重启 | 在实例列表，勾选需要重启的实例，单击**重启**对实例进行重启操作，支持批量重启（勾选多个实例）。<li>重启期间，实例将无法正常访问，已有的连接会断掉，请您做好准备，以免造成影响。<li>重启期间，如果业务写入量很大，脏页过多，会导致重启失败。重启失败后，实例回到重启之前状态，实例仍可访问。<li>请确保在业务低峰期重启，保证重启成功率，降低对业务的影响。</li>|

## 实例管理页
登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，初始化完成后，在实例列表，单击实例 ID 或在**操作**列的**管理**，可以进入实例管理页面。您可以进行实例详情查看、实例监控、数据库管理等操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5d632169d396b919b9d16dc538290959.png)

| 功能 | 介绍 | 
|---------|---------|
| 实例详情 | 在实例详情页面，您可以查看和操作数据库的各种信息，单击<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对实例的基本信息进行修改，其中外网地址默认是关闭状态，如有需要，请单击外网地址处的**开启**进行开启。 | 
|实例监控 | 在实例监控页面，您可以查看当前数据库运行的众多核心指标的监控，分为访问、负载、查询缓存、表、InnoDB、MyISAM 等维度的监控，详细介绍请参见 [监控功能](https://cloud.tencent.com/document/product/236/8455) 和 [告警功能](https://cloud.tencent.com/document/product/236/8457)。|
| 数据库管理 | <li>**数据库列表**<br>在数据库列表页面，您可以将 SQL 文件导入到指定的数据库，详细介绍请参见 [导入 SQL 文件](https://cloud.tencent.com/document/product/236/8466)。<li>**参数设置**<br>在参数设置页面，您可以对数据库的众多可修改参数进行设置和查看修改历史，单击**参数运行值**旁边的<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对该参数值进行修改，详细介绍请参见 [参数模板](https://cloud.tencent.com/document/product/236/30304)。<li>**帐号管理**<br>在帐号管理页面，您可以对系统默认的 root 帐号进行管理，如修改权限，重置密码等，也可以创建帐号，删除帐号，详细介绍请参见 [帐号管理](https://cloud.tencent.com/document/product/236/35794)。|
| 安全组 | 在安全组页面，您可以对您的数据库进行安全组的配置操作，详细介绍请参见 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。|
| 备份恢复 | 在备份恢复页面，您可以进行下载 binlog 和冷备操作，详细介绍请参见 [备份数据库](https://cloud.tencent.com/document/product/236/35172)。|
| 操作日志 | 在操作日志页面，您可以查看和下载慢查询日志、错误日志、回档日志，详细介绍请参见 [操作日志](https://cloud.tencent.com/document/product/236/39348)。|
| 只读实例 | 在只读实例页面，您可以创建一个或多个只读实例，以支持用户的读写分离和一主多从应用场景，可显著提高用户数据库的读负载能力，详细介绍请参见 [只读实例](https://cloud.tencent.com/document/product/236/7270)。|
| 数据库代理 |用于代理应用服务端访问数据库时的请求，提供自动读写分离、连接池、连接保持等高级功能，具有高可用、高性能、可运维、简单易用等特点。详细介绍请参见 [数据库代理](https://cloud.tencent.com/document/product/236/54652)。|
| 数据加密 |启用数据加密功能的实例，不支持使用物理备份恢复至其他主机上的自建数据库，详细介绍请参见 [数据加密](https://cloud.tencent.com/document/product/236/48863)。|
| 连接检查 | 在连接检查页面，您可以检测云数据库可能存在的连接访问问题，并根据提供的解决方法处理访问问题，以确保您的云数据库能够正常访问，详细介绍请参见 [一键连接检查工具](https://cloud.tencent.com/document/product/236/33206)。|

