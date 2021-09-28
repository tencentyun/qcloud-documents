## 操作场景

该任务以 Python 客户端为例介绍您在控制台创建集群、Vhost、Exchange等资源后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)

## 操作步骤

1. 下载 Demo（[Demo下载地址]()），并配置相关参数。

   **生产消息**

   ```python
   #!/usr/bin/env python
   import pika
   
   host="amqp://amqp-****"
   username='yourname'
   password='eyJr****'
   vhost='amqp-****|****'
   credentials = pika.PlainCredentials(username, password)
   connection = pika.BlockingConnection(pika.ConnectionParameters(
       host=host, port=****, virtual_host=vhost, credentials=credentials ))
   channel = connection.channel()
   channel.basic_publish(exchange='****', routing_key='****', body='Hello World!')
   print('send success msg to rabbitmq')
   connection.close()
   ```

   | 参数        | 说明                                                         |
   | ----------- | ------------------------------------------------------------ |
   | host        | 集群接入地址，在控制台【集群管理】>【接入地址】处获取。![](https://main.qcloudimg.com/raw/563ccee3ab8755552144b2a5b3385dd7.png) |
   | username    | Vhost用户名，在【Vhost】页面的鉴权信息列获取。![](https://main.qcloudimg.com/raw/cea52a2f0c741b09b80059746b1ef149.png) |
   | password    | Vhost密码，获取位置同上。                                    |
   | vhost       | vhost名称，在【Vhost】页面复制。                             |
   | port        | 集群接入地址端口号，在控制台【集群管理】>【接入地址】处复制。 |
   | exchange    | exchange名称，在控制台【exchange】页面复制。                 |
   | routing_key | ![](https://main.qcloudimg.com/raw/05464563f97f55a6526df714caef531b.png) |

   **消费消息**

   ```python
   #!/usr/bin/env python
   
   import pika
   
   host="amqp://amqp-****"
   username='yourname'
   password='eyJr****'
   vhost='amqp-****|****'
   queue="****"
   credentials = pika.PlainCredentials(username, password)
   connection = pika.BlockingConnection(pika.ConnectionParameters(
       host=host, port=****, virtual_host=vhost, credentials=credentials ))
   channel = connection.channel()
   
   def callback(ch, method, properties, body):
       print(" [x] Received %r" % body)
   
   channel.basic_consume(on_message_callback=callback,queue=queue)
   print(' [*] Waiting for messages. To exit press CTRL+C')
   channel.start_consuming()
   ```

   | 参数     | 说明                                                         |
   | -------- | ------------------------------------------------------------ |
   | host     | 集群接入地址，在控制台【集群管理】>【接入地址】处获取。![](https://main.qcloudimg.com/raw/563ccee3ab8755552144b2a5b3385dd7.png) |
   | username | Vhost用户名，在【Vhost】页面的鉴权信息列获取。![](https://main.qcloudimg.com/raw/cea52a2f0c741b09b80059746b1ef149.png) |
   | password | Vhost密码，获取方式同上。                                    |
   | vhost    | vhost名称，在控制台【Vhost】页面复制。                       |
   | queue    | queue名称，在控制台【queue】页面复制。                       |
   | port     | 集群接入地址端口号，在控制台【集群管理】>【接入地址】处复制。 |

2. 在python demo目录下，打开一个终端窗口，编译并运行consumer_demo.py启动消费者。

   ```python
   python3 consumer_demo.py
   ```

3. 另外开一个终端窗口编译并运行producer_demo.py启动生产者。

   ```python
   python3 producer_demo.py
   ```

4. 查看运行结果，可以看到生产端发送消息后，消费端也几乎同时收到了消息。

   ![](https://main.qcloudimg.com/raw/4ecb1cd699b1073aaae65a4ea3b2353b.png)

   

