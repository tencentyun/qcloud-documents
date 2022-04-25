## 介绍
消息队列 TDMQ RabbitMQ（TDMQ for RabbitMQ，以下简称 RMQ）是一款腾讯自主研发的消息队列服务，支持 AMQP 0-9-1 协议，完全兼容开源 RabbitMQ 的各个组件，可以用作数据目的（Sink）。用户可以通过 Flink 算子把流数据导入到 RMQ 的某个 Queue 中。



## 版本说明

| Flink 版本 | 说明 |
| :--------- | :--- |
| 1.11       | 支持 |
| 1.13       | 支持 |
| 1.14       | 不支持 |

## 使用范围
RMQ 支持用作数据目的表（Sink），暂不支持 Upsert 数据流。

## DDL 定义

### 用作数据目的（Sink）

#### JSON 格式输出

```sql
CREATE TABLE `rmq_sink_json_table` (
    `id` int,
    `name` STRING
) WITH (
	  'connector' = 'rabbitmq', 					 			-- 必须为 'rabbitmq'
    'host' = 'xxxx',    											-- rabbitmq host
    'port' = 'xxxx',			 		      					-- rabbitmq 端口
    'vhost' = '/',				   									-- 虚拟主机
    'username' = 'xxxx',         		 							-- 用户名
    'password' = 'xxxx',     									-- 用户密码
    'exchange' = 'exchange',             		 	-- 交换机名
  	'routing-key' = 'Key',										-- 绑定 Key
  	'format' = 'json',												-- 定义数据格式（JSON 格式）
    'json.fail-on-missing-field' = 'false',	  -- 如果设置为 false, 则遇到缺失字段不会报错
    'json.ignore-parse-errors' = 'true'       -- 如果设置为 true，则忽略任何解析报错
);
```

#### CSV 格式输出

```sql
CREATE TABLE `rmq_sink_csv_table` (
    `id` int,
    `name` STRING
) WITH (
	  'connector' = 'rabbitmq', 					 			-- 必须为 'rabbitmq'
    'host' = 'xxxx',    											-- rabbitmq host
    'port' = 'xxxx',			 		      					-- rabbitmq 端口
    'vhost' = '/',				   									-- 虚拟主机
    'username' = 'xxxx',         		 							-- 用户名
    'password' = 'xxxx',     									-- 用户密码
    'exchange' = 'exchange',             		 	-- 交换机名
  	'routing-key' = 'Key',										-- 绑定 Key
  	'format' = 'csv'													-- 定义数据格式（CSV 格式）
);
```

## WITH 参数

### 通用 WITH 参数

| 参数值                    | 必填 |  默认值  |                             描述                             |
| :------------------------ | :--: | :------: | :----------------------------------------------------------: |
| connector                 |  是  |    无    |                  必须指定为 `'rabbitmq'`。                   |
| host                      |  是  |    无    |                       队列所在 host。                        |
| port                      |  是  |   5672   |                       rabbitmq 端口。                        |
| vhost                     |  是  |    /     |                          虚拟主机。                          |
| username                  |  是  |  guest   |                           角色名。                           |
| password                  |  是  |  guest   |                          角色密码。                          |
| queue                     |  否  |    无    |                           队列名。                           |
| exchange                  |  是  |    无    |                          交换机名。                          |
| routing-key               |  否  |    无    |                       交换机绑定 Key。                        |
| delivery-mode             |  否  |    1     |            消息是否持久化，1：非持久化 2：持久化。             |
| expiration                |  否  | 86400000 |            消息过期时间，默认一天（单位：毫秒）。            |
| network-recovery-interval |  否  |   30s    |                        网络恢复间隔。                        |
| automatic-recovery        |  否  |   true   |              rabbitmq 自动连接，默认自动连接。               |
| topology-recovery         |  否  |   true   |              rabbitmq 拓扑恢复，默认自动恢复。               |
| connection-timeout        |  否  |   30s    |                   连接超时时间，默认30s。                    |
| requested-frame-max       |  否  |    0     |   最初请求的最大通信帧大小，以字节为单位。0意味着无限制。    |
| requested-heartbeat       |  否  |   60s    |                        请求心跳超时。                        |
| prefetch-count            |  否  |    0     | 服务器发送的消息的最大数量，0 意味着无限制。（仅 1.13 支持） |
| delivery-timeout          |  否  |   30s    |              提交队列超时时间。（仅 1.13 支持）              |
| format                    |  是  |    无    |     RMQ 消息的输入输出格式。目前支持`'csv'`、`'json'`。      |

### JSON 格式 WITH 参数

| 参数值                         | 必填 | 默认值 | 描述                                                         |
| ------------------------------ | ---- | ------ | ------------------------------------------------------------ |
| json.fail-on-missing-field     | 否   | false  | 如果为 true，则遇到缺失字段时，会让作业失败。如果为 false（默认值），则只会把缺失字段设置为 null 并继续处理。 |
| json.ignore-parse-errors       | 否   | false  | 如果为 true，则遇到解析异常时，会把这个字段设置为 null 并继续处理。如果为 false，则会让作业失败。 |
| json.timestamp-format.standard | 否   | SQL    | 指定 JSON 时间戳字段的格式，默认是 SQL（格式是`yyyy-MM-dd HH:mm:ss.s{可选精度}`）。也可以选择 ISO-8601，格式是 `yyyy-MM-ddTHH:mm:ss.s{可选精度}`。 |

### CSV 格式 WITH 参数

| 参数值                      | 必填 | 默认值     | 描述                                                         |
| :-------------------------- | ---- | ---------- | ------------------------------------------------------------ |
| csv.field-delimiter         | 否   | ,          | 指定 CSV 字段分隔符，默认是半角逗号。                        |
| csv.line-delimiter          | 否   | U&'\\000A' | 指定 CSV 的行分隔符，默认是换行符`\n`，SQL 中必须用`U&'\000A'`表示。如果需要使用回车符`\r`，SQL 中必须使用`U&'\000D'`表示。（仅 1.11 支持） |
| csv.disable-quote-character | 否   | false      | 禁止字段包围引号。如果为 true，则 'csv.quote-character' 选项不可用。 |
| csv.quote-character         | 否   | ''         | 字段包围引号，引号内部的作为整体看待。默认是`''`。           |
| csv.ignore-parse-errors     | 否   | false      | 忽略处理错误。对于无法解析的字段，会输出为 null。            |
| csv.allow-comments          | 否   | false      | 忽略 # 开头的注释行，并输出为空行（请务必将 csv.ignore-parse-errors 设为 true）。 |
| csv.array-element-delimiter | 否   | ;          | 数组元素的分隔符，默认是`;`。                                |
| csv.escape-character        | 否   | 无         | 指定转义符，默认禁用转义。                                   |
| csv.null-literal            | 否   | 无         | 将指定的字符串看作 null 值。                                 |

## 代码示例

```sql
-- 提示：请将参数替换成所属集群的信息
CREATE TABLE `rabbitmq_source_json_table` (`id` INT, `name` STRING) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:mysql://host:port/database?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai',
  'table-name' = 'source_table_name',
  'username' = 'username',
  'password' = 'password'
);

CREATE TABLE `rabbitmq_sink_json_table` (`id` INT, `name` STRING) WITH (
  'connector' = 'rabbitmq',
  'host' = 'host',
  'port' = 'port',
  'vhost' = 'vhost',
  'username' = 'username',
  'password' = 'password',
  'queue' = 'queue-name',
  'exchange'='exchange',
  'routing-key'='key',
  'format' = 'json'
);
insert into rabbitmq_sink_json_table select * from rabbitmq_source_json_table;
```

>! RMQ 作为数据目的表（Sink）使用的时候，需要注意往 RMQ 写入数据时有小概率会重复写入。
