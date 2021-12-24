## 操作场景

该任务以 Python 客户端为例指导您使用 VPC 网络接入消息队列 CKafka 并收发消息。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/pythonkafkademo/VPC)

## 操作步骤

将下载的 Demo 中的 pythonkafkademo 上传至 Linux 服务器，登录 Linux 服务器，进入 pythonkafkademo 目录。

### 步骤一：添加 Python 依赖库

执行以下命令安装：

```bash
pip install kafka-python
```


### 步骤二：生产消息

1. 修改生产消息程序 producer.py 中配置参数。

```python
#coding:utf8
from kafka import KafkaProducer
import json
producer = KafkaProducer(
   bootstrap_servers = ['$domainName:$port'],
   api_version = (0,10,0)
)
message = "Hello World! Hello Ckafka!"
msg = json.dumps(message).encode()
producer.send('topic_name',value = msg)
print("produce message " + message + " success.");
producer.close()
```

| 参数              | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| bootstrap_servers | 接入网络，在控制台的实例详情页面**接入方式**模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/88b29cffdf22e3a0309916ea715057a1.png) |
| topic_name        | Topic 名称，您可以在控制台上**topic管理**页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |

2. 编译并运行 producer.py。
3. 查看运行结果。
   ![](https://main.qcloudimg.com/raw/312d264676c655838e398ab9fa03b491.png) 
4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的**topic管理**页面，选择对应的 Topic，单击**更多** > **消息查询**，查看刚刚发送的消息。
   ![](https://main.qcloudimg.com/raw/ec5fbf218cf50ff3d760be15f6331867.png)




### 步骤三：消费消息

1. 修改消费消息程序 consumer.py 中配置参数。

```python
#coding:utf8
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    '$topic_name',
    group_id = "$group_id",
    bootstrap_servers = ['$domainName:$port'],
    api_version = (0,10,0)
)

for message in consumer:
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" % (message.topic, message.partition, message.offset, message.value))
```

| 参数              | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| bootstrap_servers | 接入网络，在控制台的实例详情页面**接入方式**模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/88b29cffdf22e3a0309916ea715057a1.png) |
| group_id          | 消费者的组 ID，根据业务需求自定义                            |
| topic_name        | Topic名称，您可以在控制台上**topic管理**页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |

2. 编译并运行 consumer.py。

3. 查看运行结果。
   ![](https://main.qcloudimg.com/raw/479f3b14e67a5f50f9d49781ab4df39f.png)

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的**Consumer Group**页面，选择对应的消费组名称，在主题名称输入 Topic 名称，单击**查询详情**，查看消费详情。
   ![](https://main.qcloudimg.com/raw/27775267907600f4ff759e6a197195ee.png)
