## 操作场景

该任务以 Python 客户端为例，指导您使用公网 SASL_PLAINTEXT 方式接入消息队列 CKafka 并收发消息。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/pythonkafkademo/PUBLIC_SASL)

## 操作步骤

### 步骤一：准备工作
1. 创建接入点。
	1. 在 **[实例列表](https://console.cloud.tencent.com/ckafka/index)** 页面，单击目标实例 ID，进入实例详情页。
	2. 在 **基本信息** > **接入方式** 中，单击**添加路由策略**，在打开窗口中选择：`路由类型：公网域名接入`, `接入方式：SASL_PLAINTEXT`。
	![](https://qcloudimg.tencent-cloud.cn/raw/4ac0033364e13d3f2c81d464c878d7f4.png)

2. 创建角色。
在**用户管理**页面新建角色，设置密码。
![](https://qcloudimg.tencent-cloud.cn/raw/b4fd547ddb7d4fdac1c24d59bb4806bc.png)

3. 创建 Topic。
在控制台 **topic 管理**页面新建 Topic（参考 [创建 Topic](https://cloud.tencent.com/document/product/597/20247#.E5.88.9B.E5.BB.BA-topic)）。

4. 添加 Python 依赖库。
执行以下命令安装：
```bash
pip install kafka-python
```

### 步骤二：生产消息

1. 修改生产消息程序 `producer.py` 中配置参数。
```python
producer = KafkaProducer(
    bootstrap_servers = ['xx.xx.xx.xx:port'],
    api_version = (1, 1),

    #
    # SASL_PLAINTEXT 公网接入
    #
    security_protocol = "SASL_PLAINTEXT",
    sasl_mechanism = "PLAIN",
    sasl_plain_username = "instanceId#username",
    sasl_plain_password = "password",
)

message = "Hello World! Hello Ckafka!"
msg = json.dumps(message).encode()
producer.send('topic_name', value = msg)
print("produce message " + message + " success.")
producer.close()
```

| 参数                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| `bootstrap_servers`   | 接入网络，在控制台的实例详情页面**接入方式**模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/c5cf200a66f6dcf627d2ca6f1c747ecf.png) |
| `sasl_plain_username` | 用户名，格式为 `实例 ID` + `#` + `用户名`。实例 ID 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的实例详情页面的基本信息获取，用户在**用户管理**创建用户时设置。 |
| `sasl_plain_password` | 用户密码，在 CKafka 控制台实例详情页面的**用户管理**创建用户时设置。 |
| `topic_name`          | Topic 名称，您可以在控制台上**topic管理**页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |

2. 编译并运行 producer.py。
   
3. 查看运行结果。
![](https://main.qcloudimg.com/raw/312d264676c655838e398ab9fa03b491.png)

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的 **topic管理**页面，选择对应的 Topic ， 单击**更多** > **消息查询**，查看刚刚发送的消息。
![](https://main.qcloudimg.com/raw/ec5fbf218cf50ff3d760be15f6331867.png)


### 步骤三：消费消息

1. 修改消费消息程序 consumer.py 中配置参数。
```python
consumer = KafkaConsumer(
    'topic_name',
    group_id = "group_id",
    bootstrap_servers = ['xx.xx.xx.xx:port'],
    api_version = (1,1),

    #
    # SASL_PLAINTEXT 公网接入
    #
    security_protocol = "SASL_PLAINTEXT",
    sasl_mechanism = 'PLAIN',
    sasl_plain_username = "instanceId#username",
    sasl_plain_password = "password",
)

for message in consumer:
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" %
    (message.topic, message.partition, message.offset, message.value))

```

| 参数                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| `bootstrap_servers`   | 接入网络，在控制台的实例详情页面**接入方式**模块的网络列复制。<br/>![img](https://main.qcloudimg.com/raw/c5cf200a66f6dcf627d2ca6f1c747ecf.png) |
| `group_id`            | 消费者的组 ID，根据业务需求自定义。                          |
| `sasl_plain_username` | 用户名，格式为 `实例 ID` + `#` + `用户名`。实例 ID 在CKafka 控制台的实例详情页面的基本信息获取，用户在**用户管理**创建用户时设置。 |
| `sasl_plain_password` | 用户名密码，在 CKafka 控制台实例详情页面的**用户管理**创建用户时设置 |
| `topic_name`          | Topic 名称，您可以在控制台上 **topic管理**页面复制。<br/>![img](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |

2. 编译并运行 consumer.py。

3. 查看运行结果。
![](https://main.qcloudimg.com/raw/479f3b14e67a5f50f9d49781ab4df39f.png)

4. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 的 **Consumer Group** 页面，选择对应的消费组名称，在主题名称输入 Topic 名称，单击**查询详情**，查看消费详情。  
![](https://main.qcloudimg.com/raw/27775267907600f4ff759e6a197195ee.png)
