[Beats 平台](https://www.elastic.co/cn/products/beats) 集合了多种单一用途数据采集器。这些采集器安装后可用作轻量型代理，从成百上千或成千上万台机器向目标发送采集数据。
![](https://main.qcloudimg.com/raw/e48ad4b5a9d1d4576bbb5f574125b8aa.png)
Beats 有多种采集器，您可以根据自身的需求下载对应的采集器。本文以 Filebeat（轻量型日志采集器）为例，向您介绍 Filebeat 接入 CKafka 的操作指方法，及接入后常见问题的解决方法。

## 前提条件

- 下载并安装 Filebeat（参见 [Download Filebeat](https://www.elastic.co/guide/en/logstash/7.6/installing-logstash.html)）
- 下载并安装JDK 8（参见 [Download JDK 8](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)）
- 已 [创建 CKafka 实例](https://cloud.tencent.com/document/product/597/53207)

## 操作步骤

### 步骤1：获取 CKafka 实例接入地址

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击实例的“ID”，进入实例基本信息页面。
3. 在实例的基本信息页面的**接入方式**模块，可获取实例的接入地址。
   ![](https://main.qcloudimg.com/raw/a28b5599889166095c168510ce1f5e89.png)

### 步骤2：创建 Topic

1. 在实例基本信息页面，选择顶部**Topic管理**页签。
2. 在 Topic 管理页面，单击**新建**，创建一个名为 test 的 Topic。
	 ![](https://main.qcloudimg.com/raw/adc18f407be9ff1a1e195891b82031c5.png)

### 步骤3：准备配置文件

进入 Filebeat 的安装目录，创建配置监控文件 filebeat.yml。
<dx-codeblock>
:::  yaml
#======= Filebeat7.x之后的版本，将 filebeat.prospectors 修改为 filebeat.inputs 即可 =======
filebeat.prospectors:

- input_type: log 

# 此处为监听文件路径
  paths:
    - /var/log/messages

#=======  Outputs =========

#------------------ kafka -------------------------------------
output.kafka:
  version:0.10.2 // 根据不同 CKafka 实例开源版本配置
  # 设置为CKafka实例的接入地址
  hosts: ["xx.xx.xx.xx:xxxx"]
  # 设置目标topic的名称
  topic: 'test'
  partition.round_robin:
    reachable_only: false

  required_acks: 1
  compression: none
  max_message_bytes: 1000000

  # SASL 需要配置下列信息，如果不需要则下面两个选项可不配置
  username: "yourinstance#yourusername"  //username 需要拼接实例ID和用户名
  password: "yourpassword"
:::
</dx-codeblock>


### 步骤4：Filebeat 发送消息

1. 执行如下命令启动客户端。
	```
	sudo ./filebeat -e -c filebeat.yml 
	```
2. 为监控文件增加数据（示例为写入监听的 testlog 文件）。
	```
	echo ckafka1 >> testlog
	echo ckafka2 >> testlog
	echo ckafka3 >> testlog
	```

3. 开启 Consumer 消费对应的 Topic，获得以下数据。
	```
	{"@timestamp":"2017-09-29T10:01:27.936Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka1","offset":500,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
	{"@timestamp":"2017-09-29T10:01:30.936Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka2","offset":508,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
	{"@timestamp":"2017-09-29T10:01:33.937Z","beat":{"hostname":"10.193.9.26","name":"10.193.9.26","version":"5.6.2"},"input_type":"log","message":"ckafka3","offset":516,"source":"/data/ryanyyang/hcmq/beats/filebeat-5.6.2-linux-x86_64/testlog","type":"log"}
	```

### SASL/PLAINTEXT 模式

如果您需要进行 SALS/PLAINTEXT 配置，则需要配置用户名与密码。 在 Kafka 配置区域新增加 username 和 password 配置即可。
<dx-codeblock>
:::  yaml
 # SASL 需要配置下列信息，如果不需要则下面两个选项可不配置
  username: "yourinstance#yourusername"  //username 需要拼接实例ID和用户名
  password: "yourpassword"
:::
</dx-codeblock>


## 常见问题

在 Filebeat 日志（默认路径`/var/log/filebeat/filebeat`）中，发现有大量 INFO 日志，例如：

```
2019-03-20T08:55:02.198+0800    INFO    kafka/log.go:53 producer/broker/544 starting up
2019-03-20T08:55:02.198+0800    INFO    kafka/log.go:53 producer/broker/544 state change to [open] on wp-news-filebeat/4
2019-03-20T08:55:02.198+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/4 selected broker 544
2019-03-20T08:55:02.198+0800    INFO    kafka/log.go:53 producer/broker/478 state change to [closing] because EOF
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 Closed connection to broker bitar1d12:9092
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/5 state change to [retrying-3]
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/4 state change to [flushing-3]
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/5 abandoning broker 478
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/2 state change to [retrying-2]
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/2 abandoning broker 541
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/leader/wp-news-filebeat/3 state change to [retrying-2]
2019-03-20T08:55:02.199+0800    INFO    kafka/log.go:53 producer/broker/478 shut down
```

出现大量 INFO 可能是 Filebeat 版本有问题，因为 Elastic 家族的产品发版速度很频繁，而且不同大版本有很多不兼容。
例如：6.5.x 默认支持 Kafka 的版本是 0.9、0.10、1.1.0、2.0.0，而 5.6.x 默认支持的是0.8.2.0。

您需要检查配置文件中的版本配置：
<dx-codeblock>
:::  yaml
output.kafka:
  version:0.10.2 // 根据不同 CKafka 实例开源版本配置
:::
</dx-codeblock>


