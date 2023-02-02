## 介绍
CLS（Cloud Log Service）日志服务，可以作为 Oceanus 的数据源（Source），用户可以将 CLS 日志主题，通过 CLS Kafka协议消费 功能，将日志导出到 Oceanus，参与后续流计算。

## 版本说明

| Flink 版本 | 说明 |
| :--------- | :--- |
| 1.11       | 支持 |
| 1.13       | 支持 |
| 1.14       | 不支持 |

## 使用范围
CLS 支持用作数据源表（Source）。

## 配置网络
建立 CLS Source 表前，需要配置网络信息，具体步骤如下：
1. 打开 [CLS 日志主题](https://console.cloud.tencent.com/cls/topic?region=ap-guangzhou) 页面中选择**日志主题 > 创建日志主题**，创建日志主题。
![](https://main.qcloudimg.com/raw/cfff31fc07d67bc51056788d90a6baf2.png)
2. 日志主题创建成功后，在列表页单击新建日志主题的**日志主题名称/ID** 进入到详情页面。
![](https://main.qcloudimg.com/raw/eb910d7411bf3bb131772b589ae9a680.png)
3. 在详情页，切换到**Kafka协议消费**页签，打开Kafka协议消费的功能。
![](https://qcloudimg.tencent-cloud.cn/raw/9af8eedc5ec40a774a5905258cd595fe.png)
开启后的状态如下：
![](https://qcloudimg.tencent-cloud.cn/raw/7d83a3fe21b5d3ebc72d58470df12faa.png)
详情请参考 [Kafka 协议消费](https://cloud.tencent.com/document/product/614/72651)
4. 在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/cluster) 中，单击**集群名称/ID**，在集群详情页**集群信息**中，单击 **VPC** 网络。
>?由于 Oceanus VPC 的网络安全严格性，需要用户找到 CLS 团队拿到 Kafka VIP 的另外几个 IP 和端口一起配置到 VPC 下的 NAT 网关中。
>
![](https://main.qcloudimg.com/raw/5b32339416ed805f85cefd8c31d2344f.png)
在 VPC **网络资源**中，需自行配置 NAT 网关。
![](https://main.qcloudimg.com/raw/9bf28a875a22449b061c1446c2547119.png)
在 NAT 网关中新增路由策略。
- 目的端：ping CLS 开放出的地址域名获取 IP 填写（IP 地址为上文提到的从 CLS 团队中提供的地址）。
- 下一跳类型：选择 NAT 网关。
![](https://main.qcloudimg.com/raw/7f78c8bd464fd33a1439b77a52240c87.png)
5. NAT 网关配置完成后，即可使用 CLS 的Kafka 协议消费功能。与消费 Kafka 方式一样，若有参数不清楚的地方，可参考 [消息队列 Kafka](https://cloud.tencent.com/document/product/849/48310)。


## 数据加工
消费 CLS Kafka 数据之前可以对原始数据进行加工处理。
1. 数据加工官网：[CLS 数据加工](https://cloud.tencent.com/document/product/614/63923)
2. 数据加工示例：[加工示例](https://cloud.tencent.com/document/product/614/63924)

## DDL 定义
```sql 
-- 建表语句如下
CREATE TABLE `nginx_source` (
  -- 日志中字段
  `@metadata` STRING,
  `@timestamp` TIMESTAMP,
  `agent` STRING,
  `ecs` STRING,
  `host` STRING,
  `input` STRING,
  `log` STRING,
  `message` STRING,
  `partition_id` BIGINT METADATA
  FROM
    'partition' VIRTUAL,
    -- kafka分区
    `ts` TIMESTAMP(3) METADATA
  FROM
    'timestamp'
) WITH (
  'connector' = 'kafka',
  -- cls kafka协议消费控制台给出的的主题名称，例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX,可在控制台复制
  'topic' = '您的消费主题',
  -- 服务地址+端口，外网端口9096，内网端口9095,列子是内网消费，请根据您的实际情况填写
  'properties.bootstrap.servers' = 'kafkaconsumer-${region}.cls.tencentyun.com:9095',
  -- 请替换为您的消费组名称   
  'properties.group.id' = '您的消费组名称',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'json',
  'json.fail-on-missing-field' = 'false',
  'json.ignore-parse-errors' = 'true',
  -- 用户名是日志集合ID，例如ca5cXXXXdd2e-4ac0af12-92d4b677d2c6
  -- 密码是用户的SecretId#SecretKey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。建议使用子账号密钥,为子账号授权时,遵循最小权限原则,即子账号的访问策略中的action、resource都配置为最小范围,可以满足操作即可,注意jaas.config最后有;分号,不填写会报错.
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="${logsetID}" password="${SecretId}#${SecretKey}";',
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN'
);
```

## 注意事项
前提条件及相关限制请参见  [Kafka 协议消费](https://cloud.tencent.com/document/product/614/72651)。
