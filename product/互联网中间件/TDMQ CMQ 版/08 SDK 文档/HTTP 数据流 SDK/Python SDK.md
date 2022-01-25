## 操作步骤

本文以 Python SDK 为例介绍客户端接入 TDMQ CMQ 版服务并收发消息的操作步骤。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-python-sdk-demo.zip)

## 一、队列模型

1. 在控制台创建符合需求的队列，参考 [创建队列服务](https://cloud.tencent.com/document/product/1496/61015)。

   > ? 创建消息队列可在控制台手动创建，或通过云 API 进行创建，使用云 API 需要安装相关 SDK，SDK 安装可参考 [Python SDK 安装](https://cloud.tencent.com/document/sdk/Python)。

   ```shell
   pip install --upgrade tencentcloud-sdk-python
   ```

   ```python
   # api认证信息
   cred = credential.Credential(SecretId, SecretKey)
   httpProfile = HttpProfile()
   httpProfile.endpoint = NameServerAddress
   
   clientProfile = ClientProfile()
   clientProfile.httpProfile = httpProfile
   # 创建tdmq客户端
   client = tdmq_client.TdmqClient(cred, "ap-guangzhou", clientProfile)
   
   # 创建cmq队列请求参数
   req = models.CreateCmqQueueRequest()
   params = {
       "QueueName": "queue_api",
       # 下面是死信队列相关配置
       "DeadLetterQueueName": "dead_queue_api",  # 死信队列，该消息队列要先创建
       "Policy": 0,  # 0为消息被多次消费未删除，1为Time-To-Live过期
       "MaxReceiveCount": 3  # 最大接收次数 1-1000
   }
   req.from_json_string(json.dumps(params))
   
   # 创建cmq消息队列
   resp = client.CreateCmqQueue(req)
   ```

   | 参数                | 说明                                                         |
   | :------------------ | :----------------------------------------------------------- |
   | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
   | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |

2. 在项目中引入 [CMQ 相关文件](https://github.com/tencentyun/cmq-python-sdk)，需要根据使用的python版本选择分支，默认为 Python2 SDK，您可切换至 Python3 分支中查看 Python3 SDK。

3. 发送消息。

   ```python
   import os
   import sys
   
   sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
   
   import logging
   from cmq.account import Account
   from cmq.queue import Message
   from cmq.cmq_exception import CMQExceptionBase
   
   # 腾讯云账户 secretId、secretKey, 此处还需注意密钥对的保密
   # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
   secretId = 'AKIDSiiRtxxxx'
   secretKey = 'GGzSeaM5xxxx'
   # CMQ的服务调用地址
   nameServerAddress = 'https://cmq-gz.public.tencenttdmq.com'
   
   # 初始化 my_account, my_queue
   # Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
   my_account = Account(nameServerAddress, secretId, secretKey, debug=True)
   my_account.set_log_level(logging.DEBUG)
   # 消息队列名称
   queue_name = sys.argv[1] if len(sys.argv) > 1 else "python_queue"
   my_queue = my_account.get_queue(queue_name)
   
   try:
       # 消息内容
       msg_body = "I am test message."
       msg = Message(msg_body)
       # 发送消息
       re_msg = my_queue.send_message(msg)
       # 发送结果
       print("Send Message Succeed! MessageBody:%s MessageID:%s" % (msg_body, re_msg.msgId))
   except CMQExceptionBase as e:
       print("Send Message Fail! Exception:%s\n" % e)
   
   ```

   | 参数                | 说明                                                         |
   | :------------------ | :----------------------------------------------------------- |
   | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
   | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |
   | queue_name          | 队列名称，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务**列表页面获取。 |

4. 消费消息。

   ```python
   import os
   import sys
   
   sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
   
   import logging
   from cmq.account import Account
   from cmq.cmq_exception import CMQExceptionBase
   
   # 腾讯云账户 secretId、secretKey, 此处还需注意密钥对的保密
   # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
   secretId = 'AKIDSiiRtxxxx'
   secretKey = 'GGzSeaM5xxxx'
   # CMQ的服务调用地址
   nameServerAddress = 'https://cmq-gz.public.tencenttdmq.com'
   
   # 初始化 my_account, my_queue
   # Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
   my_account = Account(nameServerAddress, secretId, secretKey, debug=True)
   my_account.set_log_level(logging.DEBUG)
   queue_name = sys.argv[1] if len(sys.argv) > 1 else "python_queue"
   my_queue = my_account.get_queue(queue_name)
   
   try:
       wait_seconds = 3
       # 获取消息
       recv_msg = my_queue.receive_message(wait_seconds)
       # 具体业务
       print("Receive Message Succeed! ReceiptHandle:%s MessageBody:%s MessageID:%s" % (
           recv_msg.receiptHandle, recv_msg.msgBody, recv_msg.msgId))
       # 消费成功，删除消息
       my_queue.delete_message(recv_msg.receiptHandle)
   except CMQExceptionBase as e:
       print("Receive Message Fail! Exception:%s\n" % e)
   ```

   | 参数                | 说明                                                         |
   | :------------------ | :----------------------------------------------------------- |
   | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
   | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |
   | queue               | 队列名称，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务**列表页面获取。 |

## 二、主题模型

1. 准备所需资源，创建主题订阅和订阅者。

   1. 创建主题订阅。可通过控制台手动创建，也可以通过云 API 进行创建，使用云 API 需要安装相关 SDK，SDK 安装可参考 [Python SDK 安装](https://cloud.tencent.com/document/sdk/Python)。

      ```python
      # api认证信息
      cred = credential.Credential(SecretId, SecretKey)
      httpProfile = HttpProfile()
      httpProfile.endpoint = NameServerAddress
      
      clientProfile = ClientProfile()
      clientProfile.httpProfile = httpProfile
      client = tdmq_client.TdmqClient(cred, "ap-guangzhou", clientProfile)
      
      req = models.CreateCmqTopicRequest()
      params = {
          "TopicName": "topic_api",  # 主题名字，在单个地域同一帐号下唯一
          "FilterType": 1,  # 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略
          "MsgRetentionSeconds": 86400  # 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天）
      }
      req.from_json_string(json.dumps(params))
      
      # 创建topic
      resp = client.CreateCmqTopic(req)
      ```

      | 参数                | 说明                                                         |
      | :------------------ | :----------------------------------------------------------- |
      | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
      | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |

   2. 创建订阅者。可通过控制台进行手动创建，也可以通过云 API 进行创建，使用云 API 需要安装相关 SDK，SDK 安装可参考 [Python SDK 安装](https://cloud.tencent.com/document/sdk/Python)。

      ```python
      # api认证信息
      cred = credential.Credential(SecretId, SecretKey)
      httpProfile = HttpProfile()
      httpProfile.endpoint = NameServerAddress
      
      clientProfile = ClientProfile()
      clientProfile.httpProfile = httpProfile
      client = tdmq_client.TdmqClient(cred, "ap-guangzhou", clientProfile)
      
      req = models.CreateCmqSubscribeRequest()
      params = {
          "TopicName": "topic_api",  # 创建订阅的topic名称
          "SubscriptionName": "sub",  # 订阅名称
          "Protocol": "queue",  # 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。
          "Endpoint": "topic_queue_api",   # 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“http://”开头，host可以是域名或IP；对于Queue，则填QueueName。
          "NotifyStrategy": "BACKOFF_RETRY",  # CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。
          "FilterTag": ["TAG"],  # 消息标签（用于消息过滤)。标签数量不能超过5个
          # "BindingKey": ["a.b.c"],  # BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略
          "NotifyContentFormat": "SIMPLIFIED"  # 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。
      }
      req.from_json_string(json.dumps(params))
      
      # 创建订阅
      resp = client.CreateCmqSubscribe(req)
      ```

      > !BindingKey 与 FilterTag 要根据所订阅topic类型进行设置，否则无效。

      | 参数                | 说明                                                         |
      | :------------------ | :----------------------------------------------------------- |
      | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
      | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |

2. 在项目中引入 [CMQ 相关文件](https://github.com/tencentyun/cmq-python-sdk)，需要根据使用的 Python 版本选择分支，默认为 Python2 SDK，您可切换至 Python3 分支中查看 Python3 SDK。

3. 创建 my_topic，用来发布消息。

   ```python
   import os
   import sys
   
   sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
   
   import logging
   from cmq.account import Account
   from cmq.cmq_exception import *
   from cmq.topic import *
   
   # 腾讯云账户 secretId、secretKey, 此处还需注意密钥对的保密
   # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
   secretId = 'AKIDSiiRtxxxx'
   secretKey = 'GGzSeaM5xxxx'
   # CMQ的服务调用地址
   nameServerAddress = 'https://cmq-gz.public.tencenttdmq.com'
   
   try:
       # 初始化 my_account
       # Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
       my_account = Account(nameServerAddress, secretId, secretKey, debug=True)
       my_account.set_log_level(logging.DEBUG)
       # topic主题名称
       topic_name = sys.argv[1] if len(sys.argv) > 1 else "python_topic_route"
       my_topic = my_account.get_topic(topic_name)
   except CMQExceptionBase as e:
       print("Exception:%s\n" % e)
   
   ```

   | 参数                | 说明                                                         |
   | :------------------ | :----------------------------------------------------------- |
   | NameServerAddress   | API 调用地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。![img](https://main.qcloudimg.com/raw/397c634ac38494666e878caf69cf55e7.png) |
   | SecretId、SecretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png) |
   | topic_name          | 主题订阅名称，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**主题订阅**列表页面获取。 |

4. 发送 TAG 类型消息。

   ```python
   # 消息tag
   tags = ["TAG", "TAG1", "TAG2"]
   for tag in tags:
       # 发送tag消息
       message = Message("this is a test TAG message. TAG:" + tag, [tag])
       re_msg = my_topic.publish_message(message)
       # 发送结果
       print("Send Message Succeed! MessageBody:%s MessageID:%s" % (message.msgBody, re_msg.msgId))
   ```

5. 发送 route 消息。

   ```python
   # 消息route信息routes = ["a.b.c", "a.b.x", "a.c.d", "x.y.z", "x.y.c"]for route in routes:    message = Message("this is a test route message. Route:" + route)    # 发送route消息    re_msg = my_topic.publish_message(message, route)    # 发送结果    print("Send Message Succeed! MessageBody:%s MessageID:%s" % (message.msgBody, re_msg.msgId))
   ```

6. 消费者消费订阅者订阅的消息队列即可。

以上是 CMQ 两种模型下的生产和消费方式的简单介绍，更多使用可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-cmq-demo/tdmq-cmq-python-sdk-demo.zip) 或 [CMQ 代码仓库](https://github.com/tencentyun/cmq-python-sdk)。

