本文介绍通过 [Oceanus](https://cloud.tencent.com/product/oceanus) ETL 方式将外部数据源实时导入到云数据仓库 ClickHouse，支持的外部数据源有如下：

<table>
<thread>
<tr>
<th >产品名</th>
<th >作为流数据源</th>
<th >作为批流数据源</th>
<th >作为维表</th>
</tr>
</thread>
<tbody>
<tr>
<td >消息队列 Kafka</td>
<td >支持 </td>
<td >-</td>
<td >-</td>
</tr>
<tr>
<td >消息队列 CMQ</td>
<td >支持 </td>
<td >-</td>
<td >-</td>
</tr>
<tr>
<td >日志消费 CLS</td>
<td >支持 </td>
<td >-</td>
<td >-</td>
</tr>
<tr>
<td >数据库 Redis</td>
<td >-</td>
<td >-</td>
<td >支持（Flink-1.11）</td>
</tr>
<tr>
<td >数据库 PostgreSQL CDC</td>
<td >支持</td>
<td >支持</td>
<td >支持</td>
</tr>
<tr>
<td >数据库 MySQL CDC</td>
<td >支持</td>
<td >支持</td>
<td >支持</td>
</tr>
<tr>
<td >数据库 MongoDB CDC</td>
<td >支持</td>
<td >-</td>
<td >-</td>
</tr>
<tr>
<td >数据仓库 Kudu</td>
<td >-</td>
<td >支持</td>
<td >-</td>
</tr>
<tr>
<td >数据仓库 Hive</td>
<td >支持</td>
<td >-</td>
<td >支持</td>
</tr>
<tr>
<td >数据仓库 Hbase</td>
<td >-</td>
<td >支持</td>
<td >支持</td>
</tr>
<tr>
<td >数据仓库 ClickHouse</td>
<td >-</td>
<td >支持</td>
<td >支持</td>
</tr>
<tr>
<td >数据仓库 PostgreSQL</td>
<td >-</td>
<td >支持</td>
<td >支持</td>
</tr>
<tr>
<td >Oracle（JDBC）</td>
<td >-</td>
<td >支持</td>
<td >支持</td>
</tr>
</tbody>
</table>

## 前提条件
1. 已开通 [Oceanus 服务](https://cloud.tencent.com/product/oceanus)。
2. Oceanus 集群和云数据 ClickHouse 集群须在同一个 VPC 下。
3. 流计算作业 ETL 作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 操作步骤
1. 登录云数据仓库 ClickHouse ，创建目标表。
 - 若您的任务有 update 和 delete 操作，可以通过[ CollapsingMergeTree](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/collapsingmergetree/) 来实现。
```
CREATE TABLE test.test ON CLUSTER default_cluster
(
    `id` Int32,
    `Sign` Int8
)
ENGINE = CollapsingMergeTree(Sign)
ORDER BY id
```

 - 若您的任务中不需要 update，可以通过 [MergeTree](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/) 来实现。
```
CREATE TABLE test.test ON CLUSTER default_cluster
(
    `id` Int32
)
ENGINE = MergeTree()
ORDER BY id
```

2. 发布 ETL 作业，详细请参见 [ETL 作业开发](https://cloud.tencent.com/document/product/849/57854)。
 1. 登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job)，单击左侧导航**作业管理**，进入作业管理页面。
 2. 单击**新建作业**，作业类型选中 ETL 作业，输入作业名称，并选择一个运行中的集群，新建的 ETL 作业将运行于此集群，单击**确定**后即成功创建作业。
![](https://qcloudimg.tencent-cloud.cn/raw/0b970f550619b6d1544240924cfb56c9.png)
 3. 流计算服务委托授权。
![](https://qcloudimg.tencent-cloud.cn/raw/41542923204713538b3e39faf7c1bc3d.png)
 4. 创建数据源表和目的表，并完成字段映射。
 5. 发布运行 ETL 作业。
 6. 查看作业运行情况。
作业发布并启动运行后，将变为操作中的状态，成功启动后将变为运行中的状态。作业运行中时，可以通过监控、日志、Flink UI 等功能查看作业运行的情况。

3. **登录云数据仓库 ClickHouse，并查询数据**。
```
select * from  test.test ;
```
