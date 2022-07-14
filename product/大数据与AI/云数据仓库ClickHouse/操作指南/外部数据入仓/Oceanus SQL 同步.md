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
3. 流计算作业 ETL 作业需运行于流计算独享集群，若还没有集群，请参见 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 操作步骤
1. 登录云数据仓库 ClickHouse ，创建目标表：
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

 - 若您到任务中不需要 update，可以通过 [MergeTree](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/) 来实现。
```
CREATE TABLE test.test ON CLUSTER default_cluster
(
    `id` Int32
)
ENGINE = MergeTree()
ORDER BY id
```

2. 在 Oceanus 控制台发布 SQL 作业，详细操作请参见[ SQL作业开发](https://cloud.tencent.com/document/product/849/48287)。
	1.  登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job)，单击左侧导航**作业管理**，进入作业管理页面。
	2.  单击**新建作业**，作业类型选中 SQL 作业，输入作业名称，并选择一个运行中的集群。
![](https://qcloudimg.tencent-cloud.cn/raw/e5c62c59358b1bd756505fe61d587a65.png)
	3. 获取流计算服务委托授权。
![](https://qcloudimg.tencent-cloud.cn/raw/41542923204713538b3e39faf7c1bc3d.png)
	4. 编写 SQL 语句，并完成字段映射。
授权完成后，可在开发调试的代码编辑框中输入 SQL 语句，可无需另外准备数据快速创建作业。示例语句具体执行的内容如下：
<dx-tabs>
::: Source 端
MySQL-CDC Source（学生信息作为 cdc 源表）：
```
CREATE TABLE `student` (
 `id` INT NOT NULL,
 PRIMARY KEY (`ID`) NOT ENFORCED
) WITH (
 'connector' = 'mysql-cdc',
 -- 必须为 'mysql-cdc'
 'hostname' = 'YoursIp',
 -- 数据库的 IP
 'port' = '3306',
 -- 数据库的访问端口
 'username' = '用户名',
 -- 数据库访问的用户名（需要提供 SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, SELECT, RELOAD 权限）
 'password' = 'YoursPassword,
-- 数据库访问的密码
'database-name' = 'mysqltestdb',
-- 需要同步的数据库
'table-name' = 'student' -- 需要同步的数据表名
);
```
:::
::: Sink 端
- 当任务中无 update 时：
```
CREATE TABLE clickhouse_sink (
`id` INT
) WITH (
  -- 指定数据库连接参数
  'connector' = 'clickhouse',                       -- 指定使用clickhouse连接器
  'url' = 'clickhouse://xxx:8123',        -- 指定集群地址，可以通过ClickHouse集群界面查看
  -- 如果ClickHouse集群未配置账号密码可以不指定
  --'username' = 'root',                            -- ClickHouse集群用户名
  --'password' = 'root',                            -- ClickHouse集群的密码
  'database-name' = 'test',                           -- 数据写入目的数据库
  'table-name' = 'test',                           -- 数据写入目的数据表
  'sink.batch-size' = '1000'                        -- 触发批量写的条数
);
```
- 当任务中包含 update 和 delete 操作：
```
CREATE TABLE clickhouse_upsert_sink_table (
`id` INT
 PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  -- 指定数据库连接参数
  'connector' = 'clickhouse',                     -- 指定使用clickhouse连接器
  'url' = 'clickhouse://xxx:8123',      -- 指定集群地址，可以通过ClickHouse集群界面查看
  -- 如果ClickHouse集群未配置账号密码可以不指定
  --'username' = 'root',                          -- ClickHouse集群用户名
  --'password' = 'root',                          -- ClickHouse集群的密码
  'database-name' = 'test',                         -- 数据写入目的数据库
  'table-name' = 'test',                         -- 数据写入目的数据表
  'table.collapsing.field' = 'Sign',              -- CollapsingMergeTree 类型列字段的名称
  'sink.batch-size' = '1000'                      -- 触发批量写的条数
);
```
 OCeanus ClickHouse_Sink 参数
<table>
<thread><tr><th >参数值</th><th >必填</th><th >默认值</th><th >描述</th></tr></thread>
<tbody>
<tr>
<td >connector</td>
<td >是</td>
<td >-</td>
<td >当要使用 ClickHouse 作为数据目的（Sink）需要填写，取值 clickhouse</td>
</tr>
<tr>
<td >url</td>
<td >是</td>
<td >-</td>
<td >ClickHouse 集群连接 url，可以通过集群界面查看，举例 'clickhouse://127.1.1.1:8123'</td>
</tr><tr>
<td >username</td>
<td >否</td>
<td >-</td>
<td >ClickHouse 集群用户名</td>
</tr><tr>
<td >password</td>
<td >否</td>
<td >-</td>
<td >ClickHouse 集群密码</td>
</tr><tr>
<td >database-name</td>
<td >是</td>
<td >-</td>
<td >ClickHouse 集群数据库</td>
</tr><tr>
<td >table-name</td>
<td >是</td>
<td >-</td>
<td >ClickHouse 集群数据表</td>
</tr><tr>
<td >sink.batch-size</td>
<td >否</td>
<td >1000</td>
<td >connector batch 写入的条数</td>
</tr><tr>
<td >sink.flush-interval</td>
<td >否</td>
<td >1000 （单位：ms）</td>
<td >connector 异步线程刷新写入 ClickHouse 间隔</td>
</tr><tr>
<td >table.collapsing.field</td>
<td >否</td>
<td >-</td>
<td >CollapsingMergeTree 类型列字段的名称</td>
</tr><tr>
<td >sink.max-retries</td>
<td >否</td>
<td >3</td>
<td >写入失败时的重试次数</td>
</tr><tr>
<td >local.read-write</td>
<td >否</td>
<td >false</td>
<td >是否写入本地表。默认 false 不开启写入本地表策略</td>
</tr><tr>
<td >table.local-nodes</td>
<td >否</td>
<td >-</td>
<td >local node 列表，举例 '127.1.1.10:8123,127.1.2.13:8123'（需要使用 http port）</td>
</tr><tr>
<td >sink.partition-strategy</td>
<td >否</td>
<td >balenced</td>
<td >数据分发策略，支持 balanced/shuffle/hash。当设置 sink.write-local 为 true 时启用。取值为 hash 时需要配合 sink.partition-key 使用。取值说明：balanced 轮询模式写入 shuffle 随机挑选节点写入 hash 根据 partition-key hash 值选择节点写入</td>
</tr><tr>
<td >sink.partition-key</td>
<td >否</td>
<td >-</td>
<td >当设置 sink.write-loal 为 true 且 sink.partition-strategy 为 hash 时需要设置，值为所定义表中的字段</td>
</tr><tr>
<td >scan.fetch-size</td>
<td >否</td>
<td >100</td>
<td >每次从数据库读取时，批量获取的行数</td>
</tr><tr>
<td >scan.by-part.enabled</td>
<td >否</td>
<td >false</td>
<td >是否启用读ClickHouse 表 part。若启用，必须先在所有节点上使用命令'STOP MERGES'和'STOP TTL MERGES'停止表的后台merge和基于TTL的数据删除操作，否则读取的数据会不正确</td>
</tr><tr>
<td >scan.part.modification-time.lower-bound</td>
<td >否</td>
<td >-</td>
<td >用于根据 modification_time 过滤 ClickHouse 表 part 的最小时间（包含），格式 yyyy-MM-dd HH:mm:ss</td>
</tr><tr>
<td >scan.part.modification-time.upper-bound</td>
<td >否</td>
<td >-</td>
<td >用于根据 modification_time 过滤 ClickHouse 表 part 的最大时间（不包含），格式 yyyy-MM-dd HH:mm:ss</td>
</tr><tr>
<td >lookup.cache.max-rows</td>
<td >否</td>
<td >无</td>
<td >查询缓存（Lookup Cache）中最多缓存的数据条数</td>
</tr><tr>
<td >lookup.cache.ttl</td>
<td >否</td>
<td >无</td>
<td >查询缓存中每条记录最长的缓存时间</td>
</tr><tr>
<td >lookup.max-retries</td>
<td >否</td>
<td >3</td>
<td >数据库查询失败时，最多重试的次数</td>
</tr>
</tbody>
</table>

>! 定义 WITH 参数时，通常只需要填写必填参数即可。当您启用**非必填参数**时，请您一定要明确参数含义以及可能对数据写入产生的影响。
:::
</dx-tabs>
	5. 进行逻辑运算。
此示例中，只进行了简单的 Join 没有进行复杂的运算。详细运算逻辑可参见 Oceanus 运算符和内置函数 或者 Flink 官网 Flink SQL 开发。
```
INSERT INTO
  clickhouse_sink
SELECT
  id
FROM
  student
```
	6. 发布运行 SQL 作业。
4. 登录 云数据仓库ClickHouse，并查看数据。
```
select * from  test.test ;
```
