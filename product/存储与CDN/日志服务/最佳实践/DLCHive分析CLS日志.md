## 概述
当您需要将日志服务 CLS 中的日志投递到 Hive 进行 OLAP 计算时，可以参考本文进行实践。您可以通过腾讯云数据湖计算 DLC（Data Lake Compute，DLC）提供的数据分析与计算服务，完成对日志的离线计算和分析。示意图如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/49cfebe438708b45edd6001625b55ab0.png)

## 操作步骤

### CLS 日志投递至 COS

#### 创建投递任务
1. 登录日志服务控制台，选择左侧导航栏中的 **投递任务管理 > [投递至 COS](https://console.cloud.tencent.com/cls/shipper/cos)**。
2. 在“投递至 COS” 页面中，单击**添加投递配置**，在弹出的“投递至 COS”窗口中，配置并创建投递任务。
如下配置项需要注意：
<table>
<thead>
<tr>
<th width="15%"><strong>配置项</strong></th>
<th><strong>注意事项</strong></th>
</tr>
</thead>
<tbody><tr>
<td>目录前缀</td>
<td>日志文件会投递到对象存储桶的该目录下。在数据仓库模型中，一般对应为 table  location 的地址。</td>
</tr>
<tr>
<td>分区格式</td>
<td>投递任务可按照创建时间进行自动分区，分区格式建议按照 hive 分区表格式指定。<br>例如，按天分区可以设置为 <code>/dt=%Y%m%d/test</code>，其中 <code>dt=</code> 代表分区字段，<code>%Y%m%d</code> 代表年月日，<code>test</code> 代表日志文件前缀，因投递文件默认是以下划线<code>(_)</code>开头，大数据计算引擎会将这类文件忽略，导致查询不到数据，故需增加一个前缀，实际分区目录名称为 <code>dt=20220424</code>。</td>
</tr>
<tr>
<td>投递间隔时间</td>
<td>可在5 - 15分钟范围内选择，建议选择<strong>15分钟，250MB，</strong>这样文件数量会比较少，查询性能更佳。</td>
</tr>
<tr>
<td>投递格式</td>
<td>推荐 JSON 格式。</td>
</tr>
</tbody></table>
在“基本配置”步骤中，配置示例如下图所示：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/98b9f0db88658ab9b6c582713f67ef66.png"/><br>
在“高级配置”步骤中，配置示例如下图所示：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/afcae67004ee7e28a2ae965d6890a5f8.png"/><br>


#### 查看投递任务结果


通常在启动投递任务15分钟后，可以在对象存储控制台查看到日志数据，如果在 log_data 日志集设置了按天分区，则目录结构类似下图，分区目录下包含具体的日志文件。
![](https://qcloudimg.tencent-cloud.cn/raw/8422e00e0d7543384686805199b205db.png)
对象存储控制台日志数据如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/4e388ef2b3287bfe4582e41146d2afd2.png" width="918px"/>



### DLC（Hive）分析

#### DLC 创建外部表并映射到对象存储日志目录
日志数据投递至对象存储后，即可通过 DLC 控制台 → 数据探索功能创建外部表，建表语句可参考如下 SQL 示例，**需特别注意分区字段以及 location 字段要与目录结构保持一致。**

DLC 创建外表向导提供高级选项，可以帮助您推断数据文件表结构自动快捷生成 SQL，因为是采样推断所以需要您进一步根据 SQL 判断表字段是否合理，例如以下案例，__TIMESTAMP__ 字段推断出为 int，但可能 bigint 才够用。

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS `DataLakeCatalog`.`test`.`log_data` (
  `__FILENAME__` string,
  `__SOURCE__` string,
  `__TIMESTAMP__` bigint,
  `appId` string,
  `caller` string,
  `consumeTime` string,
  `data` string,
  `datacontenttype` string,
  `deliveryStatus` string,
  `errorResponse` string,
  `eventRuleId` string,
  `eventbusId` string,
  `eventbusType` string,
  `id` string,
  `logTime` string,
  `region` string,
  `requestId` string,
  `retryNum` string,
  `source` string,
  `sourceType` string,
  `specversion` string,
  `status` string,
  `subject` string,
  `tags` string,
  `targetId` string,
  `targetSource` string,
  `time` string,
  `type` string,
  `uin` string
) PARTITIONED BY (`dt` string) ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' STORED AS TEXTFILE LOCATION 'cosn://coreywei-1253240642/log_data/'
```
- 如果是按分区投递，location 需要指向 `cosn://coreywei-1253240642/log_data/` 目录，而不是 `cosn://coreywei-1253240642/log_data/20220423/` 目录。
- 使用推断功能，需要将目录指向数据文件所在的子目录即：`cosn://coreywei-1253240642/log_data/20220423/` 目录，推断完成后在 SQL 中 location 修改回` cosn://coreywei-1253240642/log_data/` 目录即可。
- 适当分区会提升性能，但分区总数建议不超过1万。


#### 添加分区
分区表需要在添加分区数据后，才能通过 select 语句获取数据。您可以通过如下两种方式添加分区：

<dx-tabs>
::: 历史分区添加
该方案可一次性加载所有分区数据，运行较慢，适用首次加载较多分区场景。
```sql
msck repair table DataLakeCatalog.test.log_data;
```

:::
::: 增量分区添加
在加载完历史分区之后，增量分区还会定期增加。例如，每天新增一个分区，则可以通过该方案进行增量添加。
```sql
alter table DataLakeCatalog.test.log_data add partition(dt='20220424')
```

:::
</dx-tabs>


#### 分析数据
添加完分区后，即可通过 DLC 进行数据开发或分析。
```sql
select dt,count(1) from `DataLakeCatalog`.`test`.`log_data` group by dt;
```
结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/236bb86c500187f7885b0859d09435c2.png" width="918px"/>



