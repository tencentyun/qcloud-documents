## 操作背景

该任务指导您如何在 VPC 环境下，通过 SASL 接入点接入消息队列 CKafka，并使用 PLAIN 机制收发消息。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)

## 操作步骤

### 步骤一：添加 Python 依赖库
执行以下命令安装：
```bash
pip install kafka-python
```

### 步骤二：修改配置

#### 生产消息

```python
#coding:utf8
from kafka import KafkaProducer

producer = KafkaProducer(
	bootstrap_servers = ['$ip:$port'],
   	ssl_check_hostname = False,
   	security_protocol = "SASL_PLAINTEXT",
   	sasl_mechanism = "PLAIN",
	sasl_plain_username = "$instance_id#$username",
   	sasl_plain_password = "$password",
	api_version = (0,10,0)
)

producer.send('$topic_name',value="Hello World! Hello Ckafka!")
producer.close()
```

| 参数                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| bootstrap_servers   | SASL接入点，在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的实例详情页面的【基本信息】>【接入方式】获取 |
| sasl_plain_username | 用户名，格式为 `实例 ID` + `#` + `用户名`。实例 ID 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的实例详情页面的基本信息获取，用户在【用户管理】创建用户时设置 |
| sasl_plain_password | 用户密码，在 CKafka 控制台实例详情页面的【用户管理】创建用户时设置 |
| topic_name          | Topic 名称，在 CKafka 控制台实例详情页面的【topic管理】创建和获取 |

#### 消费消息

```python
#coding:utf8
from kafka import KafkaConsumer

consumer = KafkaConsumer(
	'$topic_name',
	group_id = "$group_id",
	bootstrap_servers = ['$ip:$port'],
	security_protocol = "SASL_PLAINTEXT",
	sasl_mechanism = 'PLAIN',
	sasl_plain_username = "$instance_id#$username",
   	sasl_plain_password = "$password",
	api_version = (0,10,0)
)

for message in consumer:
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" % (message.topic, message.partition, message.offset, message.value))
```

| 参数                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| bootstrap_servers   | SASL 接入点，在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的实例详情页面的【基本信息】>【接入方式】获取 |
| group_id            | 消费者的组 ID，根据业务需求自定义                            |
| sasl_plain_username | 用户名，格式为 `实例 ID` + `#` + `用户名`。实例 ID 在CKafka 控制台的实例详情页面的基本信息获取，用户在【用户管理】创建用户时设置 | 
| sasl_plain_password | 用户名密码，在 CKafka 控制台实例详情页面的【用户管理】创建用户时设置 |
| topic_name          | Topic 名称，在 CKafka 控制台实例详情页面的【topic管理】创建和获取 |
