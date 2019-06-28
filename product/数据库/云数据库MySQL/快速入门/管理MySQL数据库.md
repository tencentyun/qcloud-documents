云数据库 MySQL 初始化完成后，在实例列表单击实例名，或在【操作】列单击【管理】，可以进入实例管理页面。
![](https://main.qcloudimg.com/raw/6b5ce84ac2728e387d79703267efdbb8.png)
云数据库 MySQL 实例管理页内，您可以对数据库的实例详情查看及修改、实例监控告警管理、数据库管理、参数设置、安全组管理、备份管理以及数据库操作日志下载等。

## 实例详情
【实例详情】页可查看和操作数据库的各种信息，如下图所示，单击<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对实例的基本信息进行修改，其中外网地址默认是关闭状态，如您需要，请手动开启。
![](https://main.qcloudimg.com/raw/553029f34aa0ca698104103365512a08.png)

## 实例监控
【实例监控】页提供了对当前数据库运行的众多核心指标的监控，分为访问、负载、查询缓存、表、InnoDB、MyISAM 等六个维度的监控。
- 访问维度的监控数据项包括慢查询数、全表扫描数、查询数、更新数、删除数、插入数、覆盖数等 SQL 操作的统计，总的请求数、当前连接数以及连接使用率等服务器服务指标。通过这些数据，能够实时了解当前数据库的操作总体情况。
- 负载维度包含的监控数据项有磁盘使用空间、磁盘占用空间、容量使用率，发送数据量以及接收数据量。这些数据能够反映数据库空间增长等一些指标，可以作为数据库升级的依据。
- 查询缓存维度包含了缓存命中率和缓存使用率，该指标能够反映数据库缓存的效率，当缓存命中率低时，就需要对业务的 SQL 操作进行分析。
- 表维度目前有临时表数量以及等待表锁次数两项指标。临时表数量太多，就说明可能有大量的数据表连接操作，当表数据量大时，会严重影响查询效率，此时就应该对查询进行优化。
- InnoDB 以及 MyISAM 的监控维度分别对上诉两个存储引擎的运行指标进行监控，从而使管理人员更清楚实际表（可能采取上诉两种引擎）的运行状况。

详细实例监控功能和告警功能的介绍，请参见 [监控功能](https://cloud.tencent.com/document/product/236/8455) 和 [告警功能](https://cloud.tencent.com/document/product/236/8457)。

## 数据库管理
### 数据库列表
在【数据库管理】>【数据库列表】页面，您可以将 SQL 文件导入到指定的数据库。
1. 单击【数据导入】进入数据导入页面。
![](https://main.qcloudimg.com/raw/bb8c82bec533459fa13923964f0cb363.png)
2. 单击【新增文件】，选择本地 SQL 文件，确认上传即可。
![](https://main.qcloudimg.com/raw/4f02597436ab9f2cbb32db7129f4118b.png)

### 参数设置
在【数据库管理】>【参数设置】页面，您可以对数据库的众多可修改参数进行设置和查看修改历史，如下表所示，单击【参数运行值】旁边的<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">可以对该参数值进行修改。更多关于参数模板的操作可参见 [参数模板概述](https://cloud.tencent.com/document/product/236/8461)。
![](https://main.qcloudimg.com/raw/05244ea4f056e01e49cceed6d23076bc.png)

### 帐号管理
在【数据库管理】>【帐号管理】页面，您可以对系统默认的 root 帐户进行管理，如修改权限，重置密码等，也可以创建帐号，删除帐号。如下图所示：
![](https://main.qcloudimg.com/raw/cf8b5965d294f57222db5d69f81a1cc8.png)

## 安全组
在【安全组】页面，您可以对您的数据库进行安全组的配置操作，如下图所示，详细的安全组操作可参见 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。
![](https://main.qcloudimg.com/raw/b873054664910f292c3e09ffaff342ae.png)

## 备份恢复
在【备份恢复】页面，您可以进行下载 binlog 和冷备操作，如下图所示，详细的备份介绍可参见 [备份方式](https://cloud.tencent.com/document/product/236/7513)。
![](https://main.qcloudimg.com/raw/b48b16c9b451c67dfe8e8657bbd65754.png)

## 操作日志
在【操作日志】页面，您可以对慢查询及回档日志进行下载。
![](https://main.qcloudimg.com/raw/dfb6bd7807ee80292f7a3892df790dd6.png)

## 调整配置
在【实例列表】页面，您可以对数据库实例进行配置调整（扩缩容），支持实例升级与降级。详细操作可参见 [调整数据库实例规格](https://cloud.tencent.com/document/product/236/19707)。
![](https://main.qcloudimg.com/raw/aa708f8d610e269e508de2d8ba86dc8b.png)

## 回档
在【实例列表】页面，勾选所需要回档的实例，选择【更多操作】>【回档】，借助于冷备和 binlog 可以将数据库回档至某个指定的时间，详细操作可参见 [数据回档](https://cloud.tencent.com/document/product/236/7276)。
![](https://main.qcloudimg.com/raw/87917ab8c89425e181699e4024f48a44.png)

## 重启
在【实例列表】页面，勾选需要重启的数据库实例，单击【重启】对实例进行重启操作，支持批量重启（勾选多个实例）。
> !
> - 重启期间，实例将无法正常访问，已有的连接会断掉，请您做好准备，以免造成影响。
> - 重启期间，如果业务写入量很大，脏页过多，会导致重启失败。重启失败后，实例回到重启之前状态，实例仍可访问。
> - 请确保在业务低峰期重启，保证重启成功率，降低对业务的影响。

![](https://main.qcloudimg.com/raw/f5f034a963843b54d6f40c9bb99e73da.png)


