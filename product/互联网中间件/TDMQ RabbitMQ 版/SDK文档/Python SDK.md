## 操作场景

本文以调用 Python SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-python-sdk-demo.zip)



## 操作步骤

### 步骤1：添加依赖

1. 根据 RabbitMQ 官网推荐使用 pika，首先要在客户端使用环境中安装 pika。
   ```shell
   python -m pip install pika --upgrade
   ```

2. 在创建客户端时导入 pika。
   ```python
   import pika
   ```



### 步骤2：生产消息

创建并编译运行生产消息程序 messageProducer.py。
```python
import pika

# 使用用户名和密码创建登录凭证对象
credentials = pika.PlainCredentials('rolename', 'eyJr***')
# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='amqp-xx.rabbitmq.x.com', port=5672, virtual_host='amqp-xxx|Vhostname', credentials=credentials))
# 建立信道
channel = connection.channel()
# 声明交换机
channel.exchange_declare(exchange='direct_exchange', exchange_type="direct")

routingKeys = ['aaa.bbb.ccc', 'aaa.bbb.ddd', 'aaa.ccc.zzz', "xxx.yyy.zzz"]

for routingKey in routingKeys:
    # 发送消息到指定的交换机
    # 不指定交换机的情况下发送消息，需要指定消息队列，参数routing_key在使用指定交换机时，表示routing_key，不指定交换机时代表消息队列名称
    channel.basic_publish(exchange='direct_exchange',
                          routing_key=routingKey,
                          body=(routingKey + 'This is a new direct message.').encode(),
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # 设置消息持久化
                          ))
    print('send success msg to rabbitmq')
connection.close()
```

| 参数            | 说明                                                         |
| :-------------- | :----------------------------------------------------------- |
| rolename        | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| eyJr***         | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| host            | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| port            | 集群接入地址端口，在**集群管理**页面操作列的**获取接入地址**获取。 |
| virtual_host    | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| direct_exchange | Exchange 名称，在控制台 Exchange 列表获取。                  |
| routingKeys     | 消息的路由规则，在控制台 绑定关系列表的**绑定 Key**列获取。![img](https://main.qcloudimg.com/raw/66d31e7d7ec8519843a8fc67bff87265.png) |

### 步骤3：消费消息

创建并编译运行消费消息程序 messageConsumer.py。
```python
import os
import pika
import sys


def main():
    # 使用用户名和密码创建登录凭证对象
    credentials = pika.PlainCredentials('rolename', 'eyJr***')
    # 创建连接
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='amqp-xx.rabbitmq.x.com', port=5672, virtual_host='amqp-xxx|Vhostname', credentials=credentials))
    # 建立信道
    channel = connection.channel()
    # 声明消息队列
    channel.queue_declare(queue='route_queue1', exclusive=True, durable=True)
    # 绑定消息队列到交换机，并指定 routing key
    routing_keys = ['aaa.bbb.ccc', 'aaa.bbb.ddd']
    for routingKey in routing_keys:
        channel.queue_bind(exchange='direct_exchange', queue="route_queue1", routing_key=routingKey)
    # 设置只接受一个未确认消息
    channel.basic_qos(prefetch_count=1)

    # 消息消费逻辑
    def callback(ch, method, properties, body):
        print(" [Consumer1(Direct 'aaa.bbb.ccc'/'aaa.bbb.ddd')] Received (%r)" % body)
        # 手动回复ACK
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # 创建消费者，消费消息队列中的消息
    channel.basic_consume(queue='route_queue1',
                          on_message_callback=callback,
                          auto_ack=False)  # 设置为非自动确认

    print(" [Consumer1(Direct 'aaa.bbb.ccc'/'aaa.bbb.ddd')] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
   ```

| 参数            | 说明                                                         |
| :-------------- | :----------------------------------------------------------- |
| rolename        | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| eyJr***         | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| host            | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| port            | 集群接入地址端口，在**集群管理**页面操作列的**获取接入地址**获取。 |
| virtual_host    | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| direct_exchange | Exchange 名称，在控制台 Exchange 列表获取。                  |
| route_queue1    | Queue名称，在控制台 Queue 列表获取。                         |
| routingKey      | 消息的路由规则，在控制台 绑定关系列表的**绑定 Key**列获取。![img](https://main.qcloudimg.com/raw/66d31e7d7ec8519843a8fc67bff87265.png) |

### 步骤4：查看消息

如果您想确认消息是否成功发送至 TDMQ RabbitMQ 版，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面查看接入的消费者情况。

![img](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)

完整示例或其他使用可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-python-sdk-demo.zip) 或者 [RabbitMQ 官方使用文档](https://www.rabbitmq.com/getstarted.html)。
