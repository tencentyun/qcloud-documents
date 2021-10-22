## 介绍
Elasticsearch Connector 提供了对 Elasticsearch  写入支持。目前 Oceanus 提供了  `flink-connector-elasticsearch6` 和 `flink-connector-elasticsearch7` 两个版本的内置 Connector 包，分别为 Elasticsearch 6.x 和 7.x 版本提供支持。

如果您希望连接其他版本的 Elasticsearch，请通过附加**自定义程序包**的方式，上传相应的 Elasticsearch Sink 的 JAR 包。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
Elasticsearch 只支持写入，可以作为 Tuple 数据流的目的表（Sink），也可以作为 Upsert 数据流的目的表（Sink，自动以文档 `_id` 字段生成主键，并更新之前的文档版本）。

如果希望将 JDBC 数据库的变动记录，将其作为流式源表消费，可以使用 [Debezium](https://debezium.io/documentation/reference/1.2/tutorial.html)、[Canal](https://github.com/alibaba/canal) 等，对 JDBC 据库的变更进行捕获和订阅，然后 Flink 即可对这些变更事件进行进一步的处理。可参见 [Kafka](https://cloud.tencent.com/document/product/849/48310)。

## 示例
### 用作 Elasticsearch 6 数据目的（Sink）
当写入 Elasticsearch 6.x 版本时，需要在作业内置 Connector 中选择 `flink-connector-elasticsearch6`。
```sql
CREATE TABLE `Data-Input` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    'connector' = 'elasticsearch-6',       -- 输出到 Elasticsearch 6
    'username' = '$username',              -- 选填 用户名
    'password' = '$password',              -- 选填 密码
    'hosts' = 'http://10.28.28.94:9200',   -- Elasticsearch 的连接地址
    'index' = 'my-index',                  -- Elasticsearch 的 Index 名
    'document-type' = '_doc',              -- Elasticsearch 的 Document 类型
    'sink.bulk-flush.max-actions' = '1',   -- 每条数据都刷新
    'format' = 'json'                      -- 输出数据格式，目前只支持 'json'
);
```

### 用作 Elasticsearch 7 数据目的（Sink）
当写入 Elasticsearch 7.x 版本时，需要在作业内置 Connector 中选择 `flink-connector-elasticsearch7`。
```sql
CREATE TABLE `Data-Output` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    'connector' = 'elasticsearch-7',       -- 输出到 Elasticsearch 7
    'username' = '$username',              -- 选填 用户名
    'password' = '$password',              -- 选填 密码
    'hosts' = 'http://10.28.28.94:9200',   -- Elasticsearch 的连接地址
    'index' = 'my-index',                  -- Elasticsearch 的 Index 名
    'sink.bulk-flush.max-actions' = '1',   -- 每条数据都刷新
    'format' = 'json'                      -- 输出数据格式，目前只支持 'json'
);
```

## 通用 WITH 参数
<table>
<thead>
<tr>
<th align="left">参数值</th>
<th align="center">必填</th>
<th align="center">默认值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">connector</td>
<td align="center">是</td>
<td align="center">无</td>
<td align="left">当写入 Elasticsearch 6.x 版本时，取值<code>elasticsearch-6</code>。当写入 Elasticsearch 7.x 及以上版本时，取值<code>elasticsearch-7</code>。</td>
</tr>
<tr>
<td align="left">username</td>
<td align="center">否</td>
<td align="center">无</td>
<td align="left">用户名。</td>
</tr>
<tr>
<td align="left">password</td>
<td align="center">否</td>
<td align="center">无</td>
<td align="left">密码。</td>
</tr>
<tr>
<td align="left">hosts</td>
<td align="center">是</td>
<td align="center">无</td>
<td align="left">Elasticsearch 的连接地址。</td>
</tr>
<tr>
<td align="left">index</td>
<td align="center">是</td>
<td align="center">无</td>
<td align="left">数据要写入的 Index。支持固定 Index（例如 <code>'myIndex'</code>），也支持动态 Index（例如<code>'index-{log_ts\|yyyy-MM-dd}'</code>）。</td>
</tr>
<tr>
<td align="left">document-type</td>
<td align="center">6.x 版本：必填<br>7.x 版本：不需要</td>
<td align="center">无</td>
<td align="left">Elasticsearch 文档的 Type 信息。当选择 <code>elasticsearch-7</code> 时，不能填写这个字段，否则会报错。</td>
</tr>
<tr>
<td align="left">document-id.key-delimiter</td>
<td align="center">否</td>
<td align="center">_</td>
<td align="left">为复合键生成 _id 时的分隔符 (默认是 "_")。例如有 a、b、c 三个主键，某条数据的 a 字段为 "1"，b 字段为 "2"，c 字段为 "3"，使用默认分隔符，则最终写入 Elasticsearch 的 _id 是 "1_2_3"。</td>
</tr>
<tr>
<td align="left">failure-handler</td>
<td align="center">否</td>
<td align="center">fail</td>
<td align="left">指定请求 Elasticsearch 失败时，错误处理策略。选项为：<li><code>fail</code>：抛出一个异常。</li><li><code>ignore</code>：忽略错误，直接继续。</li><li><code>retry-rejected</code>：重试写入该条记录。<br>另外也支持自定义错误处理器，这里可以填写用户自己编写的 Handler 的类全名（需要上传自定义程序包）。</li></td>
</tr>
<tr>
<td align="left">sink.flush-on-checkpoint</td>
<td align="center">否</td>
<td align="center">true</td>
<td align="left">Flink 进行快照时，是否等待现有记录完全写入 Elasticsearch 。如果设置为 false，则可能造成恢复时部分数据丢失或者重复等异常情况，但快照速度会提升。</td>
</tr>
<tr>
<td align="left">sink.bulk-flush.max-actions</td>
<td align="center">否</td>
<td align="center">1000</td>
<td align="left">批量写入的最大条数。设置为 <code>0</code> 则禁用批量功能。</td>
</tr>
<tr>
<td align="left">sink.bulk-flush.max-size</td>
<td align="center">否</td>
<td align="center">2mb</td>
<td align="left">批量写入缓存的最大容量，必须以 <code>mb</code> 为单位。设置为 <code>0</code> 则禁用批量功能。</td>
</tr>
<tr>
<td align="left">sink.bulk-flush.interval</td>
<td align="center">否</td>
<td align="center">1s</td>
<td align="left">批量写入的刷新周期。设置为<code>0</code>则禁用批量功能。</td>
</tr>
<tr>
<td align="left">sink.bulk-flush.backoff.strategy</td>
<td align="center">否</td>
<td align="center">DISABLED</td>
<td align="left">批量写入时，失败重试的策略。<li><code>DISABLED</code>：不重试。</li><li><code>CONSTANT</code>：等待 <code>sink.bulk-flush.backoff.delay</code> 选项设置的毫秒后重试。</li><li><code>EXPONENTIAL</code>：一开始等待 <code>sink.bulk-flush.backoff.delay</code> 选项设置的毫秒后重试，每次失败后将指数增加下次的等待时间。</li></td>
</tr>
<tr>
<td align="left">sink.bulk-flush.backoff.max-retries</td>
<td align="center">否</td>
<td align="center">8</td>
<td align="left">批量写入时，最多失败重试的次数。</td>
</tr>
<tr>
<td align="left">sink.bulk-flush.backoff.delay</td>
<td align="center">否</td>
<td align="center">50ms</td>
<td align="left">批量写入失败时，每次重试之间的等待间隔（对于 CONSTANT 策略而言）或间隔的初始基数（对于 EXPONENTIAL 策略而言）。</td>
</tr>
<tr>
<td align="left">connection.max-retry-timeout</td>
<td align="center">否</td>
<td align="center">无</td>
<td align="left">重试请求的最大超时时间。</td>
</tr>
<tr>
<td align="left">connection.path-prefix</td>
<td align="center">否</td>
<td align="center">无</td>
<td align="left">指定每个 REST 请求的前缀，例如 <code>'/v1'</code>。通常不需要设置该选项。</td>
</tr>
<tr>
<td align="left">format</td>
<td align="center">否</td>
<td align="center">json</td>
<td align="left">指定输出的格式，默认是内置的 <code>json</code> 格式，可以使用 前文（Kafka）描述过的 JSON 格式选项，例如 <code>json.fail-on-missing-field</code>、<code>json.ignore-parse-errors</code>、<code>json.timestamp-format.standard</code> 等。</td>
</tr>
</tbody></table>
