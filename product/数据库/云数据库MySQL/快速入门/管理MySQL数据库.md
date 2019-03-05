云数据库 MySQL 初始化完成后，在实例名右侧，单击【管理】链接，可以进入实例管理页面。
![](https://main.qcloudimg.com/raw/d1081af75c7108e07778a8cdd88bdc00.png)

云数据库 MySQL 实例管理页面内，您可以对数据库的实例详情查看及修改、实例监控告警管理、数据库管理、参数设置、安全组管理、备份管理以及数据库操作日志下载等。

### 实例详情
【实例详情】页能够对数据库的各种信息进行查看和操作，如下图所示，单击<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对实例的基本信息进行修改，其中外网地址默认是关闭状态，如您需要，请手动开启。
![](https://main.qcloudimg.com/raw/5891a3473b18b6248bdf2992487144d4.png)

### 实例监控
【实例监控】页提供了对当前数据库运行的众多核心指标的监控，分为访问、负载、查询缓存、表、Innodb、MyISAM 等六个维度的监控。
其中访问维度的监控数据项包括慢查询数、全表扫描数、查询数、更新数、删除数、插入数、覆盖数等 sql 操作的统计，总的请求数、当前连接数以及连接使用率等服务器服务指标。通过这些数据，能够实时了解当前数据库的操作总体情况。
负载维度包含的监控数据项有磁盘使用空间、磁盘占用空间、容量使用率，发送数据量以及接收数据量。这些数据能够反映数据库空间增长等一些指标，可以作为数据库升级的依据。

- 查询缓存维度包含了缓存命中率和缓存使用率，该指标能够反映数据库缓存的效率，当缓存命中率低时，就需要对业务的 SQL 操作进行分析。
- 表维度目前有临时表数量以及等待表锁次数两项指标。临时表数量太多，就说明可能有大量的数据表连接操作，当表数据量大时，会严重影响查询效率，此时就应该对查询进行优化。
- InnoDB 以及 MyISAM 的监控维度分别对上诉两个存储引擎的运行指标进行监控，从而使管理人员更清楚实际表（可能采取上诉两种引擎）的运行状况。

详细实例监控功能和告警功能的介绍，请参阅 [监控功能](https://cloud.tencent.com/document/product/236/8455) 和 [告警功能](https://cloud.tencent.com/document/product/236/8457)。

### 数据库操作
在【数据库管理】-【数据库列表】页面，您可以将 sql 文件导入到指定的数据库，如下表所示：

1. 单击【数据导入】进入数据导入页面。
   ![](https://main.qcloudimg.com/raw/e37eb9335ee79d0852829efcf5e8e45d.png)
2. 单击【新增文件】，选择本地 sql 文件，确认上传即可。

![](https://main.qcloudimg.com/raw/e82ead34a54034cf25f40b0698b9c33a.png)



### 参数设置

在【数据库管理】-【参数设置】页面，您可以对数据库的众多可修改参数进行设置和修改历史的查看，如下表所示，单击**参数运行值**旁边的<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对该参数值进行修改。更多关于参数模板的操作可参阅 [参数模板概述](https://cloud.tencent.com/document/product/236/8461)。
![](https://main.qcloudimg.com/raw/21715becbdc085c1ffff00bcff2786fb.png)

### 帐号管理
在【数据库管理】-【帐号管理】页面，您可以对系统默认的 root 帐户进行管理，如修改权限，重置密码等，也可以创建帐号，删除帐号。如下图所示：
![](https://main.qcloudimg.com/raw/58d42b6a85a21882735fef5caa4b1ad6.png)

### 安全组
在【安全组】页面，您可以对您的数据库进行安全组的配置操作，如下图所示，详细的安全组操作可参阅 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。
![](https://main.qcloudimg.com/raw/8983edaaad917bb4119880f042662275.png)

### 备份管理

在【备份管理】页面，您可以进行下载 binlog 和冷备操作，如下图所示，详细的备份介绍可参阅 [备份方式](https://cloud.tencent.com/document/product/236/7513)。
![](https://main.qcloudimg.com/raw/27c817ba8c4210ef84d738ddcb67e65b.png)

### 操作日志
在【操作日志】页面，您可以对慢查询及回档日志进行下载，如下图所示：
![](https://main.qcloudimg.com/raw/2ebfc2aad271f78d8f15510cec60b10f.png)

<span id = "biangengpeizhi"></span>
### 调整配置
在【实例列表】页面，您可以对数据库实例进行配置调整（扩缩容），支持实例升级与降级。入口如下图所示，详细操作可参考 [调整数据库实例规格](https://cloud.tencent.com/document/product/236/19707)。
![](https://main.qcloudimg.com/raw/6592b2ec71952933e0f1b12dd86de2b5.png)

### 回档
在【实例列表】页面，如下图所示，勾选所需要回档的实例，单击【回档】，借助于冷备和 binlog 可以将数据库回档至某个指定的时间，详细操作可参阅 [数据回档](https://cloud.tencent.com/document/product/236/7276)。
![](https://main.qcloudimg.com/raw/75631185a2331d3d9935d3b428a72b01.png)

<span id = "chongqi"></span>
### 重启
在【实例列表】页面，勾选需要重启的数据库实例，单击【重启】按钮对实例进行重启操作，支持批量重启（勾选多个实例），操作如下：
![](https://main.qcloudimg.com/raw/4ddb5e423d7681b41e169a8009f9253c.png)

>!
- 重启期间，实例将无法正常访问，已有的连接会断掉，请您做好准备，以免造成影响。
- 重启期间，如果业务写入量很大，脏页过多，会导致重启失败。重启失败后，实例回到重启之前状态，实例仍可访问。
- 请确保在业务低峰期重启，保证重启成功率，降低对业务的影响。
