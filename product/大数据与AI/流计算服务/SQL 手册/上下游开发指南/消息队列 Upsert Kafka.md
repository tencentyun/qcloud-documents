## 介绍

Upsert Kafka 连接器支持以 upsert 方式从 Kafka topic 中读取数据并将数据写入 Kafka topic。

作为 Source，Upsert Kafka 连接器生产 changelog 流，其中每条数据记录代表一个更新或删除事件。更准确地说，数据记录中的 value 被解释为同一 key 的最后一个 value 的 UPDATE，如果有这个 key（如果不存在相应的 key，则该更新被视为 INSERT）。用表来类比，changelog 流中的数据记录被解释为 UPSERT，也称为 INSERT/UPDATE，因为任何具有相同 key 的现有行都被覆盖。另外，value 为空的消息将会被视作为 DELETE 消息。

作为 Sink，Upsert Kafka 连接器可以消费 changelog 流。它会将 INSERT/UPDATE_AFTER 数据作为正常的 Kafka 消息写入，并将 DELETE 数据以 value 为空的 Kafka 消息写入（表示对应 key 的消息被删除）。Flink 将根据主键列的值对数据进行分区，从而保证主键上的消息有序，因此同一主键上的更新/删除消息将落在同一分区中。


## 版本说明

| Flink 版本 | 说明   |
| :-------- | :----- |
| 1.11      | 不支持 |
| 1.13      | 支持   |

## DDL 定义

```sql
CREATE TABLE kafka_upsert_sink_table (
  id INT,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  -- 定义 Upsert Kafka 参数
  'connector' = 'upsert-kafka',  -- 选择 connector
  'topic' = 'topic',  -- 替换为您要消费的 Topic
  'properties.bootstrap.servers' = '...',  -- 替换为您的 Kafka 连接地址
  'key.format' = 'json',  -- 定义 key 数据格式
  'value.format' = 'json'  -- 定义value 数据格式
);
```

>?Upsert Kafka 确保在 DDL 中定义主键。

## WITH 参数

<table class="table table-bordered">
    <thead>
      <tr>
      <th class="text-left" style="width: 25%">参数</th>
      <th class="text-center" style="width: 10%">是否必选</th>
      <th class="text-center" style="width: 10%">默认值</th>
      <th class="text-center" style="width: 10%">数据类型</th>
      <th class="text-center" style="width: 50%">描述</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><h5>connector</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>指定要使用的连接器，Upsert Kafka 连接器使用：<code>'upsert-kafka'</code>。</td>
    </tr>
    <tr>
      <td><h5>topic</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>用于读取和写入的 Kafka topic 名称。</td>
    </tr>
    <tr>
      <td><h5>properties.bootstrap.servers</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>以逗号分隔的 Kafka brokers 列表。</td>
    </tr>
    <tr>
      <td><h5>properties.*</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>
         该选项可以传递任意的 Kafka 参数。选项的后缀名必须匹配定义在 <a href="https://kafka.apache.org/documentation/#configuration">Kafka 参数文档</a> 中的参数名。
         Flink 会自动移除选项名中的 "properties." 前缀，并将转换后的键名以及值传入 KafkaClient。例如，您可以通过 <code>'properties.allow.auto.create.topics' = 'false'</code>
         来禁止自动创建 topic。 但是，某些选项，例如<code>'key.deserializer'</code> 和 <code>'value.deserializer'</code> 是不允许通过该方式传递参数，因为 Flink 会重写这些参数的值。
      </td>
    </tr>
    <tr>
      <td><h5>key.format</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>用于对 Kafka 消息中 key 部分序列化和反序列化的格式。key 字段由 PRIMARY KEY 语法指定。支持的格式包括 <code>'csv'</code>、<code>'json'</code>、<code>'avro'</code>。
      </td>
    </tr>
    <tr>
      <td><h5>key.fields-prefix</h5></td>
      <td>optional</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>为<code>'key.fields'</code>的所有字段定义自定义前缀，以避免与<code>'value.fields'</code>字段名称冲突。默认情况下，前缀为空。如果定义了自定义前缀，则
        表 schema 和 <code>'key.fields'</code> 将使用前缀名称。构建<code>'key.fields'</code>格式的数据类型时候，将删除前缀并使用key format中非前缀名称。请注意，此选项要求 <code>'value.fields-include'</code>
        必须设置为 <code>'EXCEPT_KEY'</code>。
      </td>
    </tr>
    <tr>
      <td><h5>value.format</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>用于对 Kafka 消息中 value 部分序列化和反序列化的格式。支持的格式包括 <code>'csv'</code>、<code>'json'</code>、<code>'avro'</code>。
      </td>
    </tr>
    <tr>
       <td><h5>value.fields-include</h5></td>
       <td>必选</td>
       <td style="word-wrap: break-word;"><code>'ALL'</code></td>
       <td>String</td>
       <td>控制哪些字段应该出现在 value 中。可取值：
       <ul>
         <li><code>ALL</code>：消息的 value 部分将包含 schema 中所有的字段，包括定义为主键的字段。</li>
         <li><code>EXCEPT_KEY</code>：记录的 value 部分包含 schema 的所有字段，定义为主键的字段除外。</li>
       </ul>
       </td>
    </tr>
    <tr>
      <td><h5>sink.parallelism</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>Integer</td>
      <td>定义 upsert-kafka sink 算子的并行度。默认情况下，由框架确定并行度，与上游链接算子的并行度保持一致。</td>
    </tr>
    <tr>
      <td><h5>sink.buffer-flush.max-rows</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">0</td>
      <td>Integer</td>
      <td>缓存刷新前，最多能缓存多少条记录。当 sink 收到很多同 key 上的更新时，缓存将保留同 key 的最后一条记录，因此 sink 缓存能帮助减少发往 Kafka topic 的数据量，以及避免发送潜在的 tombstone 消息。
      可以通过设置为 '0' 来禁用它。默认，该选项是未开启的。注意，如果要开启 sink 缓存，需要同时设置 <code>'sink.buffer-flush.max-rows'</code>
      和 <code>'sink.buffer-flush.interval'</code> 两个选项为大于零的值。</td>
    </tr>
    <tr>
      <td><h5>sink.buffer-flush.interval</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">0</td>
      <td>Duration</td>
      <td>缓存刷新的间隔时间，超过该时间后异步线程将刷新缓存数据。当 sink 收到很多同 key 上的更新时，缓存将保留同 key 的最后一条记录，因此 sink 缓存能帮助减少发往 Kafka topic 的数据量，以及避免发送潜在的 tombstone 消息。
        可以通过设置为 '0' 来禁用它。默认，该选项是未开启的。注意，如果要开启 sink 缓存，需要同时设置 <code>'sink.buffer-flush.max-rows'</code>
        和 <code>'sink.buffer-flush.interval'</code> 两个选项为大于零的值。</td>
    </tbody>
</table>


## 代码示例

```sql
CREATE TABLE `kafka_json_source_table` (
  `id` INT,
  `name` STRING
) WITH (
  -- 定义 Kafka 参数
  'connector' = 'kafka',
  'topic' = 'Data-Input',  -- 替换为您要消费的 Topic
  'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets / timestamp 的任何一种
  'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址
  'properties.group.id' = 'testGroup', -- 必选参数, 一定要指定 Group ID

  -- 定义数据格式 (JSON 格式)
  'format' = 'json',
  'json.fail-on-missing-field' = 'false',  -- 如果设置为 false, 则遇到缺失字段不会报错。
  'json.ignore-parse-errors' = 'true'    -- 如果设置为 true，则忽略任何解析报错。
);

CREATE TABLE kafka_upsert_sink_table (
  id INT,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  -- 定义 Upsert Kafka 参数
  'connector' = 'upsert-kafka',  -- 选择 connector
  'topic' = 'topic',  -- 替换为您要消费的 Topic
  'properties.bootstrap.servers' = '...',  -- 替换为您的 Kafka 连接地址
  'key.format' = 'json',  -- 定义 key 数据格式
  'value.format' = 'json'  -- 定义value 数据格式
);

-- 计算 pv、uv 并插入到 upsert-kafka sink
INSERT INTO kafka_upsert_sink_table
SELECT * FROM kafka_json_source_table;
```

## SASL 认证授权
### SASL/PLAIN 用户名密码认证授权

1. 参考 [消息队列 CKafka - 配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)，设置 Topic 按用户名密码访问的 SASL_PLAINTEXT 认证方式。
2. 参考 [消息队列 CKafka - 添加路由策略](https://cloud.tencent.com/document/product/597/36348)，选择 SASL_PLAINTEXT 接入方式，并以该接入方式下的网络地址访问 Topic。
3. 作业配置 with 参数。
```
CREATE TABLE `YourTable` (
...
) WITH (
  ...
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="ckafka-xxxxxxxx#YourUserName" password="YourPassword";',
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN',
  ...
);
```

>? `username` 是`实例 ID` + `#` + `刚配置的用户名`，`password` 是刚配置的用户密码。

### SASL/GSSAPI Kerberos 认证授权
腾讯云 CKafka 暂时不支持 Kerberos 认证，您的自建 Kafka 如果开启了 Kerberos 认证，可参考如下步骤配置作业。
1. 获取您的自建 Kafka 集群的 Kerberos 配置文件，如果您基于腾讯云 EMR 集群自建，获取 krb5.conf、emr.keytab 文件，路径如下。
```
/etc/krb5.conf
/var/krb5kdc/emr.keytab
```
2. 对步骤1中获取的文件打 jar 包。
```
jar cvf kafka-xxx.jar krb5.conf emr.keytab
```
3. 校验 jar 的结构（可以通过 vim 命令查看 vim kafka-xxx.jar），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```
META-INF/
META-INF/MANIFEST.MF
emr.keytab
krb5.conf
```
4. 在 [程序包管理](https://console.cloud.tencent.com/oceanus/resource) 页面上传 jar 包，并在作业参数配置里引用该程序包。
5. 获取 kerberos principal，用于作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
klist -kt /var/krb5kdc/emr.keytab

# 输出如下所示，选取第一个即可：hadoop/172.28.28.51@EMR-OQPO48B9
KVNO Timestamp     Principal
---- ------------------- ------------------------------------------------------
  2 08/09/2021 15:34:40 hadoop/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 hadoop/VM-28-51-centos@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/VM-28-51-centos@EMR-OQPO48B9 
```
6. 作业 with 参数配置。
```
CREATE TABLE `YourTable` (
...
) WITH (
  ...
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'GSSAPI',
  'properties.sasl.kerberos.service.name' = 'hadoop',
  ...
);
```
>? 参数 `properties.sasl.kerberos.service.name` 的值必须与您选取的 principal 匹配，如果您选择的为 `hadoop/${IP}@EMR-OQPO48B9`，那么取值为 hadoop。
>
7. 作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
security.kerberos.login.principal: hadoop/172.28.2.13@EMR-4K3VR5FD
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: krb5.conf
security.kerberos.login.contexts: KafkaClient
fs.hdfs.hadoop.security.authentication: kerberos
```
