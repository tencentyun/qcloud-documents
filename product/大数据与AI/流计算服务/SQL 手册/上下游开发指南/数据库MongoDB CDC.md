## 介绍

MongoDB 的 CDC 源表（即 MongoDB 的流式源表），Connector 会自动跟踪 MongoDB 副本集或分片集群，以获取数据库和集合中的文档更改。

## 版本说明

| Flink 版本 | 说明     |
| :-------- | :------- |
| 1.11      | 支持     |
| 1.13      | 暂不支持 |

## 使用范围

MongoDB CDC 只支持作为源表，MongoDB 只支持3.6及以上版本，MongoDB 集群必须是副本集或者分片集群。

## 示例

```sql
CREATE TABLE `MongodbSourceTable` (
    _id VARCHAR,
    stringField VARCHAR,
    uuidField VARCHAR,
    md5Field VARCHAR,
    dateField TIMESTAMP,
    dateBefore1970 TIMESTAMP ,
    timestampField TIMESTAMP,
    booleanField BOOLEAN,
    decimal128Field DECIMAL(10,2),
    doubleField DOUBLE,
    int32field INTEGER,
    int64Field BIGINT,
    mapField MAP<STRING, STRING>,
    arrayField ARRAY<STRING>,
    doubleArrayField ARRAY<DOUBLE>,
    minKeyField VARCHAR,
    maxKeyField VARCHAR,
    regexField VARCHAR,
    undefinedField VARCHAR,
    nullField VARCHAR,
    binaryField BINARY,
    javascriptField VARCHAR,
    PRIMARY KEY (_id) NOT ENFORCED
) WITH (
    'connector' = 'mongodb-cdc',             -- 固定值 'mongodb-cdc'
    'hostname' = '172.28.0.136:27017',       -- MongoDB 数据库 IP 和端口对, 多对使用英文逗号分隔
    'username' = 'xxx',                      -- 数据库访问的用户名(拥有 changeStream 和 read 权限)
    'password' = 'xxxx',                     -- 数据库访问的密码
    'database-name' = 'column_type_test',    -- 需要同步的数据库
    'collection-name' = 'full_types'         -- 需要同步的数据 collection
);
```

## WITH 参数

| 参数                        | 说明                                                         | 是否必填 | 备注                                                         |
| :-------------------------- | :----------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| connector                   | 源表类型                                                     | 是       | 固定值为 `mongodb-cdc`                                       |
| hostname                    | MongoDB 数据库的 IP 端口对                                   | 是       | -                                                            |
| username                    | MongoDB 数据库服务的用户名                                   | 是       | -                                                            |
| password                    | MongoDB 数据库服务的密码                                     | 是       | -                                                            |
| database-name               | MongoDB 数据库名称                                           | 是       | -                                                            |
| collection-name             | MongoDB Collection 名称                                      | 是       | -                                                            |
| copy-existing               | 是否复制库中原有的数据，如果在复制期间对数据有更改，会在数据复制完成后应用更改 | 否       | 默认值为 true                                                |
| source-offset-token         | 从指定偏移量开始消费                                         | 否       | 例如 `source-offset-token = 8260DD1C8B000000012B02296E5A1004AFBC9601D3E24E8B84CC575B0AF19DE846645F6964006460DD1C8B395740A9F32B1CE20004` 日志中会打印 |
| source-pos-logging-interval | 打印 source 消费位置信息的间隔时间                           | 否       | 例如 `source-pos-logging-interval = 10 min`                  |
| mongodb.source.\*           | Mongodb-kafka 属性参数                                       | 否       | 详情请参见 [配置属性](https://docs.mongodb.com/kafka-connector/v1.4/kafka-source/)，需要加上"mongodb.source."前缀 |

## 类型映射

MongoDB 的 CDC 和 Flink 字段类型对应关系如下：

<div class="wy-table-responsive">
<table class="colwidths-auto docutils">
    <thead>
      <tr>
        <th class="text-left">BSON type<a href="https://docs.mongodb.com/manual/reference/bson-types/"></a></th>
        <th class="text-left">Flink SQL type<a href="{% link dev/table/types.md %}"></a></th>
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


## 注意事项

### 不支持的 MongoDB 数据类型

Document 类型或者值类型包含 Document 类型。

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
