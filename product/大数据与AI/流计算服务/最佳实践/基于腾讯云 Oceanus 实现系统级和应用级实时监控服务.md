本方案结合腾讯云 Ckafka、流计算 Oceanus、腾讯云数据库 Elasticsearch、腾讯云 Prometheus 等，通过 Filebeat 实时监控系统日志和应用日志，将监控数据传输到腾讯云 Ckafka，再将 Kafka 中数据接入流计算 Oceanus，经过简单的业务逻辑处理输出到云数据库 Elasticsearch，利用云 Promethus 监控系统指标，利用云 Grafana 实现对 Oceanus 作业的个性化业务数据监控。
![](https://main.qcloudimg.com/raw/ca2f709f5a38530886d2e1cd81460f88.png)
## 方案架构  

![](https://main.qcloudimg.com/raw/9e979491e1f4a15333ac90bb27029c19.png)

## 前置准备
在使用前，请确保已购买并创建相应的大数据组件。

### 创建私有网络 VPC  
私有网络是一块您在腾讯云上自定义的逻辑隔离网络空间，在构建 Ckafka、Oceanus、Elasticsearch 集群等服务时选择的网络必须保持一致，网络才能互通。需要使用对等连接、NAT 网关等方式打通网络。具体创建步骤可参考 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

### 创建 Ckafka 实例  
**私有网络和子网选择之前创建的网络和子网**。Kafka 建议选择最新的2.4.1版本，和 Filebeat 采集工具兼容性较好。购买完成后，再创建 Kafka topic（`topic-app-info`）。
![](https://main.qcloudimg.com/raw/87fd37c2028d7cf250bedc56176a2823.png)

### 创建 Oceanus 集群  
流计算 Oceanus 服务兼容原生的 Flink 任务。在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job) 中**集群管理 > 新建集群**创建集群，选择地域、可用区、VPC、日志、存储、设置初始密码等。**VPC 及子网选择刚创建好的网络**，具体创建步骤可参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。创建完后 Flink 的集群如下：  
![](https://main.qcloudimg.com/raw/eff6eb6c2e2fe90516c22c55fbc4ef91.png)

### 创建 Elasticsearch 实例
进入 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，单击**新建**，**需选择之前创建好的私有网络和子网**，并设置账户和密码，具体操作可参考 [创建集群](https://cloud.tencent.com/document/product/845/19536)。
![](https://main.qcloudimg.com/raw/ea6da7dd1c272f12d04e8e4bf3d80e7a.png)

### 创建云监控 Prometheus 实例
为了展示自定义系统指标，需购买 Promethus 服务。若只需要自定业务指标，可以省略此步骤。

进入腾讯云监控页面，单击左侧 [Prometheus 监控](https://console.cloud.tencent.com/monitor/prometheus)，单击**新建**，**选择之前的私有网络和子网**，并设置实例名称和 Grafana 密码，具体操作可参考 [创建实例](https://cloud.tencent.com/document/product/1416/55982)。
![](https://main.qcloudimg.com/raw/097011cc05edc7e12393196a36863256.png)

### 创建独立 Grafana 资源
独立的 Grafana 在灰度发布中，需在 [Grafana 管理页面](https://console.cloud.tencent.com/monitor/grafana) 进行单独购买实现业务监控指标的展示。购买时仍需选择与其他资源同一 VPC 网络。

### 安装配置 Filebeat  
Filebeat 是一款轻量级日志数据采集的工具，通过监控指定位置的文件收集信息。在该 VPC 下给需要监控主机信息和应用信息的 CVM 上安装 Filebeat。
- 方式一：下载 Filebeat 并安装 [Filebeat 下载地址](https://www.elastic.co/cn/downloads/beats/filebeat)。
- 方式二：采用 **Elasticsearch 管理页面 > beats 管理**中提供的 Filebeat。本示例中采用了方式一。
下载到 CVM 中并配置 Filebeat，在 filebeat.yml 文件中提添加如下配置项：  
```shell
# 监控日志文件配置
- type: log
  enabled: true
  paths:
    - /tmp/test.log
    #- c:\programdata\elasticsearch\logs\*
```
```shell
# 监控数据输出项配置
output.kafka:
  version: 2.0.0                         # kafka版本号
  hosts: ["xx.xx.xx.xx:xxxx"]            # 请填写实际的IP地址+端口
  topic: 'topic-app-info'                  # 请填写实际的topic
```

请根据实际业务需求配置相对应的 filebeat.yml 文件，参考 [Filebeat 官方文档](https://www.elastic.co/guide/en/beats/filebeat/current/configuring-howto-filebeat.html)。

>!示例选用2.4.1的 Ckafka 版本，这里配置 version: 2.0.0。版本对应不上可能出现`ERROR   [kafka] kafka/client.go:341     Kafka (topic=topic-app-info): dropping invalid message`错误。

## 方案实现  
接下来通过案例介绍如何通过流计算 Oceanus 实现个性化监控。

### Filebeat 数据传输  
1. 进入到 Filebeat 根目录下，并启动 Filebeat 进行数据采集。示例中采集了 top 命令中显示的 CPU、内存等信息，也可以采集 jar 应用的日志、JVM 使用情况、监听端口等，详情可参考 [Filebeat 官网](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html)。
```python
# filebeat启动
./filebeat -e -c filebeat.yml

# 监控系统信息写入test.log文件
top -d 10 >>/tmp/test.log
```
2. 进入 Ckafka 页面，单击**消息查询**，查询对应 topic 消息，验证是否采集到数据。  
![](https://main.qcloudimg.com/raw/b9155994a4e68b14fdd4bc9b19d2bda6.png)
filebeat 采集到的数据格式：
```json
{
	"@timestamp": "2021-08-30T10:22:52.888Z",
	"@metadata": {
		"beat": "filebeat",
		"type": "_doc",
		"version": "7.14.0"
	},
	"input": {
		"type": "log"
	},
	"host": {
		"ip": ["xx.xx.xx.xx", "xx::xx:xx:xx:xx"],
		"mac": ["xx:xx:xx:xx:xx:xx"],
		"hostname": "xx.xx.xx.xx",
		"architecture": "x86_64",
		"os": {
			"type": "linux",
			"platform": "centos",
			"version": "7(Core)",
			"family": "redhat",
			"name": "CentOSLinux",
			"kernel": "3.10.0-1062.9.1.el7.x86_64",
			"codename": "Core"
		},
		"id": "0ea734564f9a4e2881b866b82d679dfc",
		"name": "xx.xx.xx.xx",
		"containerized": false
	},
	"agent": {
		"name": "xx.xx.xx.xx",
		"type": "filebeat",
		"version": "7.14.0",
		"hostname": "xx.xx.xx.xx",
		"ephemeral_id": "6c0922a6-17af-4474-9e88-1fc3b1c3b1a9",
		"id": "6b23463c-0654-4f8b-83a9-84ec75721311"
	},
	"ecs": {
		"version": "1.10.0"
	},
	"log": {
		"offset": 2449931,
		"file": {
			"path": "/tmp/test.log"
		}
	},
	"message": "(B[m16root0-20000S0.00.00:00.00kworker/1:0H(B[m[39;49m[K"
}
```

### SQL 作业编写
在流计算 Oceanus 中，对 Kafka 接入的数据进行加工处理，并存入 Elasticsearch 中。

#### 1. 定义 source
按照 Filebeat 中 json 消息的格式，构造 Flink Source。

```sql 
 CREATE TABLE DataInput (
     `@timestamp` VARCHAR,
     `host`       ROW<id VARCHAR,ip ARRAY<VARCHAR>>,
     `log`        ROW<`offset` INTEGER,file ROW<path VARCHAR>>,
     `message`    VARCHAR
 ) WITH (
     'connector' = 'kafka',   -- 可选 'kafka','kafka-0.11'. 注意选择对应的内置  Connector
     'topic' = 'topic-app-info',  -- 替换为您要消费的 Topic
     'scan.startup.mode' = 'earliest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets 的任何一种
     'properties.bootstrap.servers' = '10.0.0.29:9092',  -- 替换为您的 Kafka 连接地址
     'properties.group.id' = 'oceanus_group2',  -- 必选参数, 一定要指定 Group ID
     -- 定义数据格式 (JSON 格式)
     'format' = 'json',
     'json.ignore-parse-errors' = 'true',     -- 忽略 JSON 结构解析异常
     'json.fail-on-missing-field' = 'false'   -- 如果设置为 true, 则遇到缺失字段会报错 设置为 false 则缺失字段设置为 null
 );
```

#### 2. 定义 sink
```sql
CREATE TABLE es_output (
    `id` VARCHAR,
    `ip` ARRAY<VARCHAR>,
    `path` VARCHAR,
    `num` INTEGER,
    `message` VARCHAR,
    `createTime` VARCHAR
) WITH (
    'connector.type' = 'elasticsearch', -- 输出到 Elasticsearch
    'connector.version' = '6',          -- 指定 Elasticsearch 的版本, 例如 '6', '7'. 
    'connector.hosts' = 'http://10.0.0.175:9200',  -- Elasticsearch 的连接地址
    'connector.index' = 'oceanus_test2',       -- Elasticsearch 的 Index 名
    'connector.document-type' = '_doc',  -- Elasticsearch 的 Document 类型
    'connector.username' = 'elastic',  
    'connector.password' = 'yourpassword', 
    'update-mode' = 'upsert',            -- 可选无主键的 'append' 模式，或有主键的 'upsert' 模式     
    'connector.key-delimiter' = '$',     -- 可选参数, 复合主键的连接字符 (默认是 _ 符号, 例如 key1_key2_key3)
    'connector.key-null-literal' = 'n/a',  -- 主键为 null 时的替代字符串，默认是 'null'
    'connector.failure-handler' = 'retry-rejected',   -- 可选的错误处理。可选择 'fail' （抛出异常）、'ignore'（忽略任何错误）、'retry-rejected'（重试）

    'connector.flush-on-checkpoint' = 'true',   -- 可选参数, 快照时不允许批量写入（flush）, 默认为 true
    'connector.bulk-flush.max-actions' = '42',  -- 可选参数, 每批次最多的条数
    'connector.bulk-flush.max-size' = '42 mb',  -- 可选参数, 每批次的累计最大大小 (只支持 mb)
    'connector.bulk-flush.interval' = '60000',  -- 可选参数, 批量写入的间隔 (ms)
    'connector.connection-max-retry-timeout' = '1000',     -- 每次请求的最大超时时间 (ms)
    --'connector.connection-path-prefix' = '/v1'          -- 可选字段, 每次请求时附加的路径前缀                                                        
    'format.type' = 'json'        -- 输出数据格式, 目前只支持 'json'
);
```

#### 3. 业务逻辑
```sql
INSERT INTO es_output
SELECT 
host.id as `id`,
host.ip as `ip`,
log.file.path as `path`,
log.`offset` as `num`,
message,
`@timestamp` as `createTime`
from DataInput;
```

#### 4. 作业参数  
内置 connector：选择`flink-connector-elasticsearch6`和`flink-connector-kafka`。
>?需根据实际版本选择。

#### 5. ES 数据查询  
在 ES 控制台的 Kibana 页面查询数据，或者进入某台相同子网的 CVM 下，使用以下命令进行查询：
```shell
# 查询索引  username:password请替换为实际账号密码
curl -XGET -u username:password http://xx.xx.xx.xx:xxxx/oceanus_test2/_search -H 'Content-Type: application/json' -d'
{
    "query": { "match_all": {}},
    "size":  10
}
'
```
更多访问方式请参考 [访问 ES 集群](https://cloud.tencent.com/document/product/845/42868)。

### 系统指标监控  
本章节主要实现系统信息监控，对 Flink 作业运行状况进行监控告警。

Prometheus 是一个非常灵活的时序数据库，通常用于监控数据的存储、计算和告警。流计算 Oceanus 建议用户使用腾讯云监控提供的 Prometheus 服务，以免去部署、运维开销；同时它还支持腾讯云的通知模板，可以通过短信、电话、邮件、企业微信机器人等方式，将告警信息轻松触达不同的接收方。

#### 监控配置（Oceanus 作业监控）
除了 Oceanus 控制台自带的监控信息，还可以配置目前已经支持了任务级细粒度监控、作业级监控和集群 Flink 作业列表监控。

1. Oceanus 作业详情页面，单击**作业参数**，在**高级参数**处添加如下配置：
```shell
pipeline.max-parallelism: 2048
metrics.reporters: promgateway
metrics.reporter.promgateway.host: xx.xx.xx.xx              # Prometheus实例地址 
metrics.reporter.promgateway.port: 9090                     # Prometheus实例端口
metrics.reporter.promgateway.needBasicAuth: true
metrics.reporter.promgateway.password: xxxxxxxxxxx          # Prometheus实例密码
metrics.reporter.promgateway.interval: 10 SECONDS
```
2. 在任一 Oceanus 作业中，单击**云监控**进入云 Prometheus 实例，点击链接进入 Grafana（灰度中的 Grafana 不能由此进入），导入 json 文件，详情请参见 [接入 Prometheus 自定义监控](https://cloud.tencent.com/document/product/849/55239)。  
![](https://main.qcloudimg.com/raw/b9ec7fd573cb03160f19da0f26d161fa.png)
3. 展现出来的 flink 任务监控效果如下，用户也可以单击 **Edit** 设置不同 Panel 来优化展现效果。  
![](https://main.qcloudimg.com/raw/0f20d8f88d59caf8a29e03e1dc24b81a.png)

#### 告警配置
1. 进入腾讯云监控界面，单击 **Prometheus 监控**，点击已购买的实例进入服务管理页面，然后选择**告警策略 > 新建**，配置相关信息。具体操作参考 [接入 Prometheus 自定义监控](https://cloud.tencent.com/document/product/849/55239)。
![](https://main.qcloudimg.com/raw/087bcaae5b0399b72df65f2dc0cfa4b2.png)
2. 设置告警通知。选择**选择模版**或**新建**，设置通知模版。
![](https://main.qcloudimg.com/raw/7b45ce11c3cc10f8887c5b0b6fd3ac73.png)
3. 短信通知消息
![](https://main.qcloudimg.com/raw/413c5a402ce361f4d753bb3016e976f9.png)

### 业务指标监控  
通过 Filebeat 采集到应用业务数据，经过 Oceanus 服务的加工处理已经被存入 ES，可以通过 ES + Grafana 来实现业务数据的监控。
1. Grafana 配置 ES 数据源。进入灰度发布中的 [Grafana 控制台](https://console.cloud.tencent.com/monitor/grafana)，进入刚创建的 Grafana 服务，找到外网地址并打开。Grafana 账号为 admin，登录后选择 **Configuration > Add Source**，搜索`elasticsearch`，填写相关 ES 实例信息，添加数据源。![](https://main.qcloudimg.com/raw/7257558c62455946a90e54bc2733f397.png)
2. 选择左侧 **Dashboards > Manage**，单击右上角 **New Dashboard**，新建面板。![](https://main.qcloudimg.com/raw/fbfc5bde957f3a323f9c96d794303bfe.png)
展现效果如下：
 - `总数据量写入实时监控`：对写入数据源的总数据量进行监控。 
 - `数据来源实时监控`：对来源于某个特定 log 的数据写入量进行监控。
 - `字段平均值监控`：对某个字段的平均值进行监控。
 - `num字段最大值监控`：对 num 字段的最大值进行监控。
![](https://main.qcloudimg.com/raw/fd657fee538252f026d148272d3ada78.png)

>?此处只做示例，无实际业务。

## 总结
本方案中对系统监控指标和业务监控指标2种方式都进行尝试。若只需要对业务指标进行监控，可省略 Promethus 相关操作。此外，需要注意的是：
1. Ckafka 的版本和开源版本 Kafka 并没有严格对应，方案中 Ckafka2.4.1 和开源 Filebeat-1.14.1 版本能够调试成功。
2. 云监控中的 Promethus 服务已经嵌入了 Grafana 监控服务。但不支持自定义数据源，该嵌入的 Grafana 只能接入 Promethus，需使用独立灰度发布的 Grafana 才能完成 ES 数据接入 Grafana。
