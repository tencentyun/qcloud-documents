## 业务场景
通过 DataInLong 数据集成将业务数据源实时导入至 DLC iceberg 表的过程中，伴随着实时同步过程的推进，目标系统端会不断生成小文件。对于目标系统内已生成的小文件，基于周期合并的方式可避免由于小文件的累积造成目标系统 DLC 引擎查询效率恶化。
本文以 MySQL 实时同步至 DLC iceberg 表为例，介绍实时任务配置及小文件合并操作实践。	

## 操作步骤
### 创建目标表
1.  进入 [DLC 控制台](https://console.cloud.tencent.com/dlc)，根据以下语句创建 DLC 原生表（内表）， DLC 内表默认为 iceberg 表。
```
CREATE TABLE IF NOT EXISTS
 `db_name`.`new_table_name`(
`column_name1` column_type1,
`column_name2` column_type2
);
```
2. 修改表属性，并配置定时小文件合并。
```
ALTER TABLE `db_name`.`table_name` SET TBLPROPERTIES ('write.upsert.enabled'='true', 'format-version'='2', 'write.compact.enable' = 'true','write.compact.snapshot.interval'='20');
```
<table>
<thead>
<tr>
<th>参数说明参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>write.upsert.enabled</td>
<td>必选，支持流式 upsert 写入</td>
</tr>
<tr>
<td>format-version</td>
<td>必选，Iceberg 表版本，默认为 V1 表，实时导入目的表需要修改成 V2 表。</td>
</tr>
<tr>
<td>write.compact.enable    </td>
<td>开启小文件周期合并，推荐开启</td>
<td></td>
</tr>
<tr>
<td>write.compact.snapshot.interval</td>
<td>多少次 CheckPoint 进行一次小文件合并，设置为20表示20次，CheckPoint 执行一次小文件合并。实时数据导入任务的 CheckPoint 周期默认为1分钟。用户可以根据业务情况配置该参数</td>
</tr>
</tbody></table>
>? 实时导入数据会导致海量小文件产生，小文件会多了之后查询效率会恶化的非常严重，周期性的合并小文件能保证表的查询效率。小文件合并开启之后，实时导入任务会在指定次数的 CheckPoint 之后，下发一条合并指令到 DLC，该指令使用用户配置的 DLC 数据源的引擎执行。

### 配置项目空间
>? 若您使用的是 WeData 产品，配置项目空间操作请参见 [WeData-项目列表](https://cloud.tencent.com/document/product/1267/72614)。

1. 进入 [DataInLong 控制台](https://console.cloud.tencent.com/datainlong/projectlist)，单击**项目列表 > 新建**，新建项目空间。
![](https://qcloudimg.tencent-cloud.cn/raw/2ca4d56831f6d5c4143e487310fb04e1.png)
2. 配置项目空间信息
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>项目名称/标识</td>
<td>项目命名与唯一标识，其中唯一标识创建后不可修改</td>
</tr>
<tr>
<td>高级设置 - 项目成员</td>
<td>为此创建的项目中添加其他项目成员，创建者默认加入项目空间</td>
</tr>
<tr>
<td>成员角色</td>
<td>批量为项目成员配置角色（此处默认为前面添加的成员添加统一的角色，后续可<b>项目管理</b>模块修改）</td>
</tr>
</tbody></table>

### 配置集成资源组 [](id:配置集成资源组)
1. 进入 [DataInLong 控制台](https://console.cloud.tencent.com/datainlong/projectlist) 选择**集成资源**并单击**创建**，进入集成资源组购买页。
![](https://qcloudimg.tencent-cloud.cn/raw/02dcb0c5748c4ce2dc1c944f47bfe049.png)
>? 若您使用的是 WeData 产品，请点击进入 [WeData 控制台](https://console.cloud.tencent.com/wedata/fusion/executorResource)。
2. 购买集成资源组。
![](https://qcloudimg.tencent-cloud.cn/raw/88cb92b047b01a366fa76376655d497b.png)
>? 
>- 离线资源包与实时资源包可根据实际数据情况配置规格、以及数量。
>- 资源组网络建议选择 MySQL 和 DLC 所在网络；若 MySQL和 DLC 不在一个 VPC 环境，可为 VPC 配置开通公网，详细操作参见 [资源组配置公网](https://cloud.tencent.com/document/product/1580/81042)。
3. 购买完成后，返回控制台并关联资源组与项目空间。
>? 若在购买页面内已经关联资源组与项目空间，可忽略此步骤。
>
![](https://qcloudimg.tencent-cloud.cn/raw/449f19987e34a4a88ae978af2ab2fb3e.png)

### 配置数据源
1. 配置 MySQL 数据源。
进入**项目管理**模块，选择**数据源管理** > **新建数据源** > **选择 MySQL**。以 MySQL 数据源为例，数据连通性测试成功后，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/e0869e6003c8cc0294f37fd814b17895.png)
2. 配置 DLC 数据源。
进入**项目管理模块**，选择**数据源管理** > **新建数据源** > **选择 DLC**，配置数据源参数并在连通性测试成功后即可保存。
![](https://qcloudimg.tencent-cloud.cn/raw/7ab9a609127f690be3a7aaab3bb69e83.png)
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>JDBC URL</td>
<td>格式参考`：jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type=SparkSQLTask&amp;database_name=&amp;datasource_connection_name=DataLakeCatalog®ion=ap-beijing&amp;data_engine_name=test_engine`<br>若需要使用小文件合并，数据源的访问域名必须使用 dlc.internal.tencentcloudapi.com，task_type 必须使用 SparkSQLTask，data_engine_name 指定的引擎会用于实时同步后的小文件合并。<br>注意：小文件合并会使用此处配置的 DLC 数据引擎并在合并的时候占用部分资源，请合理配置资源，如果不启动小文件合并，该 DLC 引擎不会被使用</td>
</tr>
<tr>
<td>secretId/secretKey</td>
<td>填写拥有引擎和 SQL 执行权限的账号或者子账号的密钥。<br>可在 <a href="https://console.cloud.tencent.com/cam/capi" >API 密钥管理</a> 中查看</td>
</tr>
</tbody></table>

### 配置实时同步任务
1. 创建任务。
进入数据集成模块，创建**实时同步任务**，在弹出的提示框中输入任务名称和备注，选择**画布模式**或**表单模式**并单击完成。本介绍以画布模式为例。
![](https://qcloudimg.tencent-cloud.cn/raw/b881284b34a034a0201aea10a058cda8.png)
2. 编辑任务。
单击新建的实时同步任务名称，进入任务编辑界面，通过拖拽分别新建读取数据源和写入数据源，并通过连线指定数据流向：
![](https://qcloudimg.tencent-cloud.cn/raw/f8930c217349efbc0fb6a44c548e668f.png)
3. 配置 MySQL 节点。
双击画布中的 MySQL 节点，对读取数据源进行配置。如下图选择需要同步的数据库表，读取模式选择**全量模式**，完成后单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/ec8afbb49685b419c3f8b7adb566425c.png)
4. 配置 DLC 节点。
双击画布中的 DLC 节点，对 DLC 写入数据源进行配置。如下图选中需要写入的库表，根据业务需求选择写入模式，并指定唯一键。例子中指定唯一键为 ID 和 MySQL 的主键保持一致。
![](https://qcloudimg.tencent-cloud.cn/raw/0b0fcb7194b664992ed4fd75eceb3222.png)
下拉至底部，配置 MySQL 与 DLC 表字段映射，完成后单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/00e93ca66ef53b0c76c0ebb5dc945b90.png)
5. 任务保存与提交。
	- 配置完节点后，单击**任务数据**配置集成资源组。此资源组为 [配置集成资源组](#配置集成资源组) 步骤3中已关联至本空间的资源组。
![](https://qcloudimg.tencent-cloud.cn/raw/2f86051a5cf0eb6fa32223e1c71f3cb7.png)
	- 完成后单击**提交**按钮，并在弹窗口中勾选**立即启动**。
![](https://qcloudimg.tencent-cloud.cn/raw/511b04945c4d84cd225532d2d578ab96.png)
6. 查看并运维实时任务。
	- 提交任务后，可进入**实时运维**页面查看并监控任务状态。
![](https://qcloudimg.tencent-cloud.cn/raw/97cbebc9acd45b2c57229143898787ed.png)
	- 单击**运行监控**，可查看当前任务数据指标统计、以及配置监控告警等。

### 存量任务处理
1. 如果存量实时同步任务需要添加小文件合并功能，首先需按照步骤一修改表属性。
>? 
>- ALTER TABLE `db_name`.`new_table_name` SET TBLPROPERTIES ('write.compact.enable' = 'true', 'write.compact.snapshot.interval' = '20');其中合并周期参数‘write.compact.snapshot.interval’需要根据业务需求进行调整。
>- 如果存量表已经存在大量的小文件，推荐手动将小文件合并到一定数量之下后，再启动定时合并功能。

2. 将实时同步任务**停止**再**运行**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/e1ee7f7931ca15a7fd61a6c715046335.png)

## 附表：DLC 表属性配置的小文件合并参数说明
>? 在 DLC 设置表属性，所有参数的值都使用字符串。

|属性 |默认值 |类型 |描述信息|
|---------|---------|---------|---------|
|write.compact.enable|false|boolean |是否在实时同步的时候开启小文件合并|
|write.compact.snapshot.interval|5|integer|多少次 CheckPoint 进行一次小文件合并，wedata 默认一分钟进行一次 CheckPoint|
|write.compact.resource.name|default|string|执行小文件合并任务的 DLC 引擎，必须使用 Spark SQL 引擎，默认使用 DLC 数据源中配置的引擎|
|write.compact.max-concurrent-file-group-rewrites|1|integer|重写策略中同时重写的最大文件组数。每个文件组都将独立、异步地重写|
|write.compact.max-file-group-size-bytes|1024 * 1024 * 1024 * 100|long|单个组中压缩的最大数据量|
|write.compact.partial-progress.enabled|false|boolean|启用之后，在整个重写完成前可以对单个组进|
| write.compact.partial-progress.max-commits|10|integer|单次重写最大的可提交数|
|write.compact.target-file-size-bytes|512 * 1024 * 1024|integer|本次合并尝试生成的目标文件的大小。默认使用表属性："write.target-file-size-bytes   value"|
| write.compact.min-input-files|5|integer|单个文件组中的文件数大于该值才会产生合并操作|
|write.compact.delete-file-threshold|Integer.MAX_VALUE|integer|单个文件最少包含的 deletes 记录数，超过该值的必定会被合并|

详细说明可参考官网文档 [RewriteDataFiles](https://iceberg.apache.org/javadoc/0.14.0/org/apache/iceberg/actions/RewriteDataFiles.html#field.summary)。 


