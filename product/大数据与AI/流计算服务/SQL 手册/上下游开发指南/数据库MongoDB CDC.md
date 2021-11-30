## 介绍

MongoDB 的 CDC 源表（即 MongoDB 的流式源表），Connector 会自动跟踪 MongoDB 副本集或分片集群，以获取数据库和集合中的文档更改。

## 版本说明

| Flink 版本 | 说明   |
| :-------- | :----- |
| 1.11      | 不支持 |
| 1.13      | 支持   |

## 使用范围

MongoDB CDC 只支持作为源表，MongoDB CDC 支持4.0、4.2、5.0版本，MongoDB 集群必须是副本集或者分片集群。

## DDL 定义

```sql
-- register a MongoDB table 'products' in Flink SQL
CREATE TABLE mongo_cdc_source_table (
  _id STRING, // must be declared
  name STRING,
  weight DECIMAL(10,3),
  tags ARRAY<STRING>, -- array
  price ROW<amount DECIMAL(10,2), currency STRING>, -- embedded document
  suppliers ARRAY<ROW<name STRING, address STRING>>, -- embedded documents
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb-cdc',
  'hosts' = 'localhost:27017,localhost:27018,localhost:27019',
  'username' = 'flinkuser',
  'password' = 'flinkpw',
  'database' = 'inventory',
  'collection' = 'products'
);
```

## WITH 参数

| 参数                      | 说明                                                         | 是否必填 | 备注                      |
| :------------------------ | :----------------------------------------------------------- | :------- | :------------------------ |
| connector                 | 源表类型                                                     | 是       | 固定值为 `mongodb-cdc`    |
| hosts                     | MongoDB 数据库的 IP 端口对                                   | 是       | -                         |
| username                  | MongoDB 数据库服务的用户名                                   | 是       | -                         |
| password                  | MongoDB 数据库服务的密码                                     | 是       | -                         |
| database                  | MongoDB 数据库名称                                           | 是       | -                         |
| collection                | MongoDB Collection 名称                                      | 是       | -                         |
| connection.options        | MongoDB 的 [连接选项](https://docs.mongodb.com/manual/reference/connection-string/#std-label-connections-connection-options)。有多个时，使用&连接，例如 `relicaSet=test&connectTimeoutMS=300000` | 否       | -    |
| errors.tolerance          | 是否忽略错误记录，接受 none 或者 all。如果设置为 all， 忽略错误记录 | 否       | none                      |
| errors.log.enable         | 是否需要把错误操作打印到日志文件                             | 否       | 默认值为 true             |
| copy.existing     | 是否复制库中原有的数据，如果在复制期间对数据有更改，会在数据复制完成后应用更改 | 否       | 默认值为 true|
| copy.existing.pipeline    | 当复制原有数据的时候，可以通过这个参数设置筛选条件。例如`[{"$match": {"closed": "false"}}]`，只会复制 closed 为 false 的 记录。用法参考 [$match (aggregation)](https://docs.mongodb.com/manual/reference/operator/aggregation/match/) | 否       | -                         |
| copy.existing.max.threads | 执行数据复制时要使用的线程数                               | 否       | 默认值为 Processors Count |
| copy.existing.queue.size  | 复制数据时要使用的队列的最大大小                           | 否       | 默认值为16000            |
| poll.max.batch.size       | 每次拉取数据的最大数量。默认情况下，1.5秒的拉取间隔下，最多拉取1000条变更数据 | 否       | 默认值为1000             |
| poll.await.time.ms    | 拉取数据的时间间隔。默认情况下，1.5秒的拉取间隔下，最多拉取1000条变更数据 | 否       | 默认值为1500 |
| heartbeat.interval.ms     | 发送心跳消息时间间隔，以毫秒为单位。使用0禁用              | 否       | 默认值为0                |

>? Note：当数据流变化慢的时候，建议把 heartbeat.interval.ms 设置为一个合适的值，心跳会推送 resumeToken，防止当 Flink job 从 checkpoint 或者 savepoint 恢复的时候，resumeToken 已经过期。 

## 类型映射

<div class="wy-table-responsive">
<table class="colwidths-auto docutils">
    <thead>
      <tr>
        <th class="text-left">MongoDB 字段类型<a href="https://docs.mongodb.com/manual/reference/bson-types/"></a></th>
        <th class="text-left">Flink 字段类型<a href="{% link dev/table/types.md %}"></a></th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>-</td>
      <td>TINYINT</td>
    </tr>
    <tr>
      <td>-</td>
      <td>SMALLINT</td>
    </tr>
    <tr>
      <td>
        Int<br>
      <td>INT</td>
    </tr>
    <tr>
      <td>Long</td>
      <td>BIGINT</td>
    </tr>
    <tr>
      <td>-</td>
      <td>FLOAT</td>
    </tr>
    <tr>
      <td>Double</td>
      <td>DOUBLE</td>
    </tr>
    <tr>
      <td>Decimal128</td>
      <td>DECIMAL(p, s)</td>
    </tr>
    <tr>
      <td>Boolean</td>
      <td>BOOLEAN</td>
    </tr>
    <tr>
      <td>Date</br>Timestamp</td>
      <td>DATE</td>
    </tr>
    <tr>
      <td>Date</br>Timestamp</td>
      <td>TIME</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>TIMESTAMP(3)</br>TIMESTAMP_LTZ(3)</td>
    </tr>
    <tr>
      <td>Timestamp</td>
      <td>TIMESTAMP(0)</br>TIMESTAMP_LTZ(0)
      </td>
    </tr>
    <tr>
      <td>
        String<br>
        ObjectId<br>
        UUID<br>
        Symbol<br>
        MD5<br>
        JavaScript</br>
        Regex</td>
      <td>STRING</td>
    </tr>
    <tr>
      <td>BinData</td>
      <td>BYTES</td>
    </tr>
    <tr>
      <td>Object</td>
      <td>ROW</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>ARRAY</td>
    </tr>
    <tr>
      <td>DBPointer</td>
      <td>ROW&lt;$ref STRING, $id STRING&gt;</td>
    </tr>
    <tr>
      <td>
        <a href="https://docs.mongodb.com/manual/reference/geojson/">GeoJSON</a>
      </td>
      <td>
        Point : ROW&lt;type STRING, coordinates ARRAY&lt;DOUBLE&gt;&gt;</br>
        Line  : ROW&lt;type STRING, coordinates ARRAY&lt;ARRAY&lt; DOUBLE&gt;&gt;&gt;</br>
        ...
      </td>
    </tr>
    </tbody>
</table>
</div>


## 代码示例

```sql
CREATE TABLE mongo_cdc_source_table (
  _id STRING, // must be declared
  name STRING,
  weight DECIMAL(10,3),
  tags ARRAY<STRING>, -- array
  price ROW<amount DECIMAL(10,2), currency STRING>, -- embedded document
  suppliers ARRAY<ROW<name STRING, address STRING>>, -- embedded documents
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb-cdc',
  'hosts' = 'localhost:27017,localhost:27018,localhost:27019',
  'username' = 'flinkuser',
  'password' = 'flinkpw',
  'database' = 'inventory',
  'collection' = 'products'
);
CREATE TABLE `print_table` (
  `id` STRING,
  `name` STRING,
  `currency` STRING
) WITH (
 'connector' = 'print'
);
insert into print_table select _id, name, price.currency from mongo_cdc_source_table;
```

## 注意事项

### 用户权限

MongoDB 的 User 必须有 changeStream 和 read 权限。

```
use admin;  
db.createUser(
 {
   user: "flinkuser",
   pwd: "flinkpw",
   roles: [
      { role: "read", db: "admin" },
      { role: "readAnyDatabase", db: "admin" }
   ]
 }
);
```

### 并行度

任务的并行度只支持为1。
