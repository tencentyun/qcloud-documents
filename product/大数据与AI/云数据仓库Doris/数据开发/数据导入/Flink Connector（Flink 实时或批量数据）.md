## 基于 Flink Connector 实现数据实时或批量导入 Doris
>? 本文档适用于 flink-doris-connector 1.1.0之后的版本，1.1.0之前的版本参考 [这里](https://doris.apache.org/zh-CN/docs/0.15/extending-doris/flink-doris-connector/)。

### 基本介绍
Flink Doris Connector 支持通过 Flink 操作（读取、插入、修改、删除） Doris 中存储的数据。不只是导入。由于 Flink 是批流一体的计算引擎，因此实时的增量数据和存量的批量数据都可通过 Flink Doris Connector 导入 Doris。
代码库地址：`https://github.com/apache/doris-flink-connector`
本质是将 `Doris` 表映射为 `DataStream` 或者 `Table`。

>! 
>- 修改和删除只支持在 Unique Key 模型上。
>-n 目前的删除是支持 Flink CDC 的方式接入数据实现自动删除，如果是其他数据接入的方式删除需要自己实现。Flink CDC 的数据删除使用方式参照本文档最后一节。

### 版本兼容

| Connector Version | Flink Version | Doris Version | Java Version | Scala Version |
| --------- | ----- | ------ | ---- | ----- |
| 1.0.3     | 1.11+ | 0.15+  | 8    | 2.11,2.12 |
| 1.1.0     | 1.14+ | 1.0+   | 8    | 2.11,2.12 |
| 1.2.0     | 1.15+ | 1.0+   | 8    | -         |

### 使用方法
Flink 读写 Doris 数据主要有两种方式：
* SQL
* DataStream

### 参数配置
Flink Doris Connector Sink 的内部实现是通过 `Stream Load` 服务向 Doris 写入数据, 同时也支持 `Stream Load` 请求参数的配置设置，具体参数可参考`Stream Load手册`，配置方法如下：
* SQL 使用 `WITH` 参数 `sink.properties.` 配置
* DataStream 使用方法 `DorisExecutionOptions.builder().setStreamLoadProp(Properties)` 配置

### SQL
* Source（Doris 表作为数据源）
```sql
CREATE TABLE flink_doris_source (
    name STRING,
    age INT,
    price DECIMAL(5,2),
    sale DOUBLE
    ) 
    WITH (
      'connector' = 'doris',
      'fenodes' = 'FE_IP:8030',
      'table.identifier' = 'database.table',
      'username' = 'root',
      'password' = 'password'
);
```
* Sink（Doris 表作为导入目标表）
```sql
-- enable checkpoint
SET 'execution.checkpointing.interval' = '10s';
CREATE TABLE flink_doris_sink (
    name STRING,
    age INT,
    price DECIMAL(5,2),
    sale DOUBLE
    ) 
    WITH (
      'connector' = 'doris',
      'fenodes' = 'FE_IP:8030',
      'table.identifier' = 'db.table',
      'username' = 'root',
      'password' = 'password',
      'sink.label-prefix' = 'doris_label'
);
```

* Insert
```sql
INSERT INTO flink_doris_sink select name,age,price,sale from flink_doris_source
```

### DataStream
* Source
```java
DorisOptions.Builder builder = DorisOptions.builder()
        .setFenodes("FE_IP:8030")
        .setTableIdentifier("db.table")
        .setUsername("root")
        .setPassword("password");

DorisSource<List<?>> dorisSource = DorisSourceBuilder.<List<?>>builder()
        .setDorisOptions(builder.build())
        .setDorisReadOptions(DorisReadOptions.builder().build())
        .setDeserializer(new SimpleListDeserializationSchema())
        .build();

env.fromSource(dorisSource, WatermarkStrategy.noWatermarks(), "doris source").print();
```

* Sink
**String 数据流**
```java
// enable checkpoint
env.enableCheckpointing(10000);

DorisSink.Builder<String> builder = DorisSink.builder();
DorisOptions.Builder dorisBuilder = DorisOptions.builder();
dorisBuilder.setFenodes("FE_IP:8030")
        .setTableIdentifier("db.table")
        .setUsername("root")
        .setPassword("password");


DorisExecutionOptions.Builder  executionBuilder = DorisExecutionOptions.builder();
executionBuilder.setLabelPrefix("label-doris"); //streamload label prefix

builder.setDorisReadOptions(DorisReadOptions.builder().build())
        .setDorisExecutionOptions(executionBuilder.build())
        .setSerializer(new SimpleStringSerializer()) //serialize according to string 
        .setDorisOptions(dorisBuilder.build());


//mock string source
List<Tuple2<String, Integer>> data = new ArrayList<>();
data.add(new Tuple2<>("doris",1));
DataStreamSource<Tuple2<String, Integer>> source = env.fromCollection(data);

source.map((MapFunction<Tuple2<String, Integer>, String>) t -> t.f0 + "\t" + t.f1)
      .sinkTo(builder.build());
```
**RowData 数据流**
```java
// enable checkpoint
env.enableCheckpointing(10000);

//doris sink option
DorisSink.Builder<RowData> builder = DorisSink.builder();
DorisOptions.Builder dorisBuilder = DorisOptions.builder();
dorisBuilder.setFenodes("FE_IP:8030")
        .setTableIdentifier("db.table")
        .setUsername("root")
        .setPassword("password");

// json format to streamload
Properties properties = new Properties();
properties.setProperty("format", "json");
properties.setProperty("read_json_by_line", "true");
DorisExecutionOptions.Builder  executionBuilder = DorisExecutionOptions.builder();
executionBuilder.setLabelPrefix("label-doris") //streamload label prefix
                .setStreamLoadProp(properties); //streamload params

//flink rowdata‘s schema
String[] fields = {"city", "longitude", "latitude"};
DataType[] types = {DataTypes.VARCHAR(256), DataTypes.DOUBLE(), DataTypes.DOUBLE()};

builder.setDorisReadOptions(DorisReadOptions.builder().build())
        .setDorisExecutionOptions(executionBuilder.build())
        .setSerializer(RowDataSerializer.builder()    //serialize according to rowdata 
                           .setFieldNames(fields)
                           .setType("json")           //json format
                           .setFieldType(types).build())
        .setDorisOptions(dorisBuilder.build());

//mock rowdata source
DataStream<RowData> source = env.fromElements("")
    .map(new MapFunction<String, RowData>() {
        @Override
        public RowData map(String value) throws Exception {
            GenericRowData genericRowData = new GenericRowData(3);
            genericRowData.setField(0, StringData.fromString("beijing"));
            genericRowData.setField(1, 116.405419);
            genericRowData.setField(2, 39.916927);
            return genericRowData;
        }
    });

source.sinkTo(builder.build());
```

### 配置
#### 通用配置项

| Key                              | Default Value      | Required | Comment                                                      |
| -------------------------------- | ------------------ | -------- | ------------------------------------------------------------ |
| fenodes                          | --                 | Y        | Doris FE HTTP 地址                                           |
| table.identifier                 | --                 | Y        | Doris 表名，如：db.tbl                                       |
| username                         | --                 | Y        | 访问 Doris 的用户名                                          |
| password                         | --                 | Y        | 访问 Doris 的密码                                            |
| doris.request.retries            | 3                  | N        | 向 Doris 发送请求的重试次数                                  |
| doris.request.connect.timeout.ms | 30000              | N        | 向 Doris 发送请求的连接超时时间                              |
| doris.request.read.timeout.ms    | 30000              | N        | 向 Doris 发送请求的读取超时时间                              |
| doris.request.query.timeout.s    | 3600               | N        | 查询 Doris 的超时时间，默认值为1小时，-1表示无超时限制       |
| doris.request.tablet.size        | Integer. MAX_VALUE | N        | 一个 Partition 对应的 Doris Tablet 个数。 此数值设置越小，则会生成越多的 Partition。从而提升 Flink 侧的并行度，但同时会对 Doris 造成更大的压力 |
| doris.batch.size                 | 1024               | N        | 一次从 BE 读取数据的最大行数。增大此数值可减少 Flink 与 Doris 之间建立连接的次数。 从而减轻网络延迟所带来的额外时间开销 |
| doris.exec.mem.limit             | 2147483648         | N        | 单个查询的内存限制。默认为 2GB，单位为字节                   |
| doris.deserialize.arrow.async    | FALSE              | N        | 是否支持异步转换 Arrow 格式到 flink-doris-connector 迭代所需的 RowBatch |
| doris.deserialize.queue.size     | 64                 | N        | 异步转换 Arrow 格式的内部处理队列，当 doris.deserialize.arrow.async 为 true 时生效 |
| doris.read.field                 | --                 | N        | 读取 Doris 表的列名列表，多列之间使用逗号分隔                |
| doris.filter.query               | --                 | N        | 过滤读取数据的表达式，此表达式透传给 Doris。Doris 使用此表达式完成源端数据过滤 |
| sink.label-prefix                | --                 | Y        | Stream load 导入使用的 label 前缀。2pc 场景下要求全局唯一 ，用来保证 Flink 的 EOS 语义 |
| sink.properties.*                | --                 | N        | Stream Load 的导入参数。<br>例如:  'sink.properties.column_separator' = ', ' 定义列分隔符，  'sink.properties.escape_delimiters' = 'true' 特殊字符作为分隔符，'\x01'会被转换为二进制的0x01 <br>JSON 格式导入<br/>'sink.properties.format' = 'json' 'sink.properties.read_json_by_line' = 'true' |
| sink.enable-delete               | TRUE               | N        | 是否启用删除。此选项需要 Doris 表开启批量删除功能(Doris0.15+版本默认开启)，只支持 Unique 模型 |
| sink.enable-2pc                  | TRUE               | N        | 是否开启两阶段提交(2pc)，默认为 true，保证 Exactly-Once 语义|


### Doris 和 Flink 列类型映射关系

| Doris Type | Flink Type                       |
| ---------- | -------------------------------- |
| NULL_TYPE  | NULL              |
| BOOLEAN    | BOOLEAN       |
| TINYINT    | TINYINT              |
| SMALLINT   | SMALLINT              |
| INT        | INT            |
| BIGINT     | BIGINT               |
| FLOAT      | FLOAT              |
| DOUBLE     | DOUBLE            |
| DATE       | DATE |
| DATETIME   | TIMESTAMP |
| DECIMAL    | DECIMAL                      |
| CHAR       | STRING             |
| LARGEINT   | STRING             |
| VARCHAR    | STRING            |
| DECIMALV2  | DECIMAL                      |
| TIME       | DOUBLE             |
| HLL        | Unsupported datatype             |

### 使用 Flink CDC 接入 Doris 示例（支持 Insert / Update / Delete 事件）
```sql
CREATE TABLE cdc_mysql_source (
  id int
  ,name VARCHAR
  ,PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector' = 'mysql-cdc',
 'hostname' = '127.0.0.1',
 'port' = '3306',
 'username' = 'root',
 'password' = 'password',
 'database-name' = 'database',
 'table-name' = 'table'
);

-- 支持删除事件同步(sink.enable-delete='true'),需要 Doris 表开启批量删除功能
CREATE TABLE doris_sink (
id INT,
name STRING
) 
WITH (
  'connector' = 'doris',
  'fenodes' = '127.0.0.1:8030',
  'table.identifier' = 'database.table',
  'username' = 'root',
  'password' = '',
  'sink.properties.format' = 'json',
  'sink.properties.read_json_by_line' = 'true',
  'sink.enable-delete' = 'true',
  'sink.label-prefix' = 'doris_label'
);

insert into doris_sink select id,name from cdc_mysql_source;
```

### Java 示例
`samples/doris-demo/fink-demo/` 下提供了 Java 版本的示例，可供参考，查看点击 [这里](https://github.com/apache/incubator-doris/tree/master/samples/doris-demo/flink-demo)。

## 最佳实践
### 应用场景
使用 Flink Doris Connector 最适合的场景就是实时/批量同步源数据（从 Mysql，Oracle，PostgreSQL 等）到 Doris，使用 Flink 对 Doris 中的数据和其他数据源进行联合分析，也可以使用 Flink Doris Connector。

### 其他
- Flink Doris Connector 主要是依赖 Checkpoint 进行流式写入，所以 Checkpoint 的间隔即为数据的可见延迟时间。
- 为了保证 Flink 的 Exactly Once 语义，Flink Doris Connector 默认开启两阶段提交，Doris 在1.1版本后默认开启两阶段提交。1.0可通过修改 BE 参数开启，可参考 [Stream load（本地文件）](https://cloud.tencent.com/document/product/1387/70832)。

### 常见问题
1. **Bitmap 类型写入**
```sql
CREATE TABLE bitmap_sink (
dt int,
page string,
user_id int 
)
WITH (
  'connector' = 'doris',
  'fenodes' = '127.0.0.1:8030',
  'table.identifier' = 'test.bitmap_test',
  'username' = 'root',
  'password' = '',
  'sink.label-prefix' = 'doris_label',
  'sink.properties.columns' = 'dt,page,user_id,user_id=to_bitmap(user_id)'
)
```
2. **errCode = 2, detailMessage = Label [label_0_1] has already been used, relate to txn [19650]**
Exactly-Once 场景下，Flink Job 重启时必须从最新的 Checkpoint/Savepoint 启动，否则会报如上错误。
不要求 Exactly-Once 时，也可通过关闭2PC 提交（sink.enable-2pc=false） 或更换不同的 sink.label-prefix 解决。




