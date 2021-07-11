## 介绍
Kudu Connector 提供了对Kudu的读写支持。目前 Oceanus 提供的 `flink-connector-kudu` Connector 组件已支持 Upsert 方式插入数据。

## 使用范围
Kudu Connector 支持用作数据源表（Source，仅限于普通和维表 JOIN 的右表），也可以作为 Tuple 数据流的目的表（Sink），还可以作为 Upsert 数据流的目的表（Sink，需要包含主键）。

## 示例
### 用作数据源（Source）

```sql
CREATE TABLE `Data_Input` (
  `id` BIGINT,
  `name` STRING
) WITH (
  -- 指定Kudu连接参数
  'connector.type' = 'kudu',
  'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
  'kudu.table' = 'TableName1', -- 替换为Kudu中对应的表，如default.TestTable1
  'kudu.hash-columns' = 'id', -- 可选参数，Hash键
  'kudu.primary-key-columns' = 'id', -- 可选参数，主键
  'kudu.operation-timeout' = '10000', -- 可选参数，插入超时时间
  'kudu.max-buffer-size' = '2000', -- 可选参数，buffer大小
  'kudu.flush-interval' = '1000' -- 可选参数，刷新数据到kudu的时间间隔
)
```

### 用作数据目的（Tuple Sink）

```sql
CREATE TABLE `Data_Output` (
  `id` BIGINT,
  `name` STRING,
) WITH (
  -- 指定Kudu连接参数
  'connector.type' = 'kudu',
  'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
  'kudu.table' = 'TableName1', -- 替换为Kudu中对应的表，如default.TestTable1
  'kudu.hash-columns' = 'id', -- 可选参数，Hash键
  'kudu.primary-key-columns' = 'id', -- 可选参数，主键
  'kudu.operation-timeout' = '10000', -- 可选参数，插入超时时间
  'kudu.max-buffer-size' = '2000', -- 可选参数，buffer大小
  'kudu.flush-interval' = '1000' -- 可选参数，刷新数据到kudu的时间间隔
)
```

### 用作数据目的（Upsert Sink）

```sql
CREATE TABLE `Data_Output` (
  `id` BIGINT,
  `name` STRING,
) WITH (
  -- 指定Kudu连接参数
  'connector.type' = 'kudu',
  'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
  'kudu.table' = 'TableName1', -- 替换为Kudu中对应的表，如default.TestTable1
  'kudu.hash-columns' = 'id', -- 可选参数，Hash键
  'kudu.primary-key-columns' = 'id', -- 必选参数，主键。Upsert Sink需要包含主键。
  'kudu.operation-timeout' = '10000', -- 可选参数，插入超时时间
  'kudu.max-buffer-size' = '2000', -- 可选参数，buffer大小
  'kudu.flush-interval' = '1000' -- 可选参数，刷新数据到kudu的时间间隔
)
```

## 通用 WITH 参数

| 参数值                   | 必填 | 默认值 | 描述                                                         |
| :----------------------- | :--- | :----- | :----------------------------------------------------------- |
| connector.type           | 是   | 无     | 连接 Kudu 数据库时，需要填写 `'kudu'`                       |
| kudu.masters             | 是   | 无     | Kudu 数据库 MasterServer 的连接地址。端口默认为7051。若使用腾讯云的 Kudu 组件，master 地址和端口可以在 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr) 的【集群列表】>【集群服务】>【Kudu】>【操作】>【查看端口】中找到对应的 master server IP 和端口 |
| kudu.table               | 是   | 无     | 数据库表名                                                   |
| kudu.hash-columns        | 否   | 无     | Hash 键                                                     |
| kudu.primary-key-columns | 否   | 无     | 主键                                                       |
| kudu.replicas            | 否   | 无     | 副本数量                                                   |
| kudu.operation-timeout   | 否   | 30000  | 插入超时时间，单位为毫秒                                   |
| kudu.max-buffer-size     | 否   | 1000   | 默认为1000                                                 |
| kudu.flush-interval      | 否   | 1000   | 默认为1000                                                |
| kudu.ignore-not-found    | 否   | false  | 是否忽略未找到的数据                                      |
| kudu.ignore-duplicate    | 否   | false  | 是否忽略重复数据                                           |

## 注意事项
1. 若需要使用 Impala查询 Kudu 数据库的表时，需确认是否创建对应的外表。
2. 非 Impala-shell 创建的表，默认在 Impala 中没有对应的外表，需创建对应的 Kudu 外表才能查到记录。

