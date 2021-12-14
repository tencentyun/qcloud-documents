## 操作场景

本文以调用 Python SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-python-sdk-demo.zip)

## 操作步骤

### 步骤1. 准备环境

Rocketmq-client Python 基于[rocketmq-client-cpp](https://github.com/apache/rocketmq-client-cpp) 进行包装，因此需要先安装**`librocketmq`**。

1. 安装 librocketmq （版本2.0.0及以上）， 安装教程参考 [librocketmq 安装](https://github.com/apache/rocketmq-client-python)。

2. 执行如下命令安装 rocketmq-client-python。

   ```shell
   pip install rocketmq-client-python
   ```

### 步骤2. 生产消息

创建并编译运行生产消息程序。

```python
from rocketmq.client import Producer, Message

# 初始化生产者，并设置生产组信息
producer = Producer(groupName)
# 设置服务地址
producer.set_name_server_address(nameserver)
# 设置权限（角色名和密钥）
producer.set_session_credentials(
 	accessKey,  # 角色密钥
    secretKey,  # 角色名称
    ''
)
# 启动生产者
producer.start()

# 组装消息   topic名称为  命名空间全称拼接上topic名称后的全名称  例：rocketmq-xxx|namespace_python%topic1
msg = Message(topicName)
# 设置keys
msg.set_keys(TAGS)
# 设置tags
msg.set_tags(KEYS)
# 消息内容
msg.set_body('This is a new message.')

# 发送同步消息
ret = producer.send_sync(msg)
print(ret.status, ret.msg_id, ret.offset)
# 资源释放
producer.shutdown()
```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| groupName  | 生产者组名称。在控制台集群管理中`Group` tab中获取。          |
| nameserver | 集群接入地址，在控制台**集群管理**页面操作列的**获取接入地址**获取。![](https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png) |
| secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| topicName  | topicName 是`命名空间全称`+`%`+`topic名称`。<li> 命名空间全称在控制台集群管理中`Topic` 页签中页面复制，格式是**集群 ID +|+命名空间** 。![](https://qcloudimg.tencent-cloud.cn/raw/9251db01de6d447bbba7d3ca7f3591ef.png) </li> <li> Topic 名称在控制台集群管理中`Topic`页签中复制具体 Topic 名称。![](https://qcloudimg.tencent-cloud.cn/raw/f27fdecdf352468ef411cfdafc096d86.png)</li> |
| TAGS       | 用来设置消息的TAG。                                          |
| KEYS       | 设置消息业务key。                                            |

### 步骤3. 消费消息

创建并编译运行消费消息程序。

```python
import time

from rocketmq.client import PushConsumer, ConsumeStatus


# 消息处理回调
def callback(msg):
    # 模拟业务
    print('Received message. messageId: ', msg.id, ' body: ', msg.body)
    # 消费成功回复CONSUME_SUCCESS
    return ConsumeStatus.CONSUME_SUCCESS
    # 消费成功回复消息状态
    # return ConsumeStatus.RECONSUME_LATER


# 初始化消费者，并设置消费者组信息 (消费者组信息为命名空间全称拼接上group名称， 例：rocketmq-xxx|namespace_python%group11)
consumer = PushConsumer(groupName)
# 设置服务地址
consumer.set_name_server_address(nameserver)
# 设置权限（角色名和密钥）
consumer.set_session_credentials(
	accessKey,	 # 角色密钥
    secretKey,   # 角色名称
    ''
)
# 订阅topic
consumer.subscribe(topicName, callback, TAGS)
print(' [Consumer] Waiting for messages.')
# 启动消费者
consumer.start()

while True:
    time.sleep(3600)
# 资源释放
consumer.shutdown()

```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| groupName  | 消费者组信息为命名空间全称拼接上group名称， 例：rocketmq-xxx\|namespace_python%group11。topic名称和名称空间名称可在控制台中的`命名空间`  和 `G`roup tab中获取 |
| nameserver | ![](https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png) |
| secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| topicName  | topicName 是`命名空间全称`+`%`+`topic名称`。<li> 命名空间全称在控制台集群管理中`Topic` 页签中页面复制，格式是**集群 ID +｜+命名空间**。![](https://qcloudimg.tencent-cloud.cn/raw/9251db01de6d447bbba7d3ca7f3591ef.png) </li> <li> Topic 名称在控制台集群管理中`Topic`页签中复制具体 Topic 名称。![](https://qcloudimg.tencent-cloud.cn/raw/f27fdecdf352468ef411cfdafc096d86.png)</li> |
| TAGS       | 设置订阅消息的tag，默认为`"*"`，表示订阅所有消息             |



### 步骤4：查看消费详情

登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![img](https://main.qcloudimg.com/raw/7187da67219534d767206553e2a383ab.png)

上述是对消息的发布和订阅方式的简单介绍。更多操作可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-python-sdk-demo.zip) 或 [RocketMQ-Client-Python示例](https://github.com/apache/rocketmq-client-python/tree/master/samples) 。

