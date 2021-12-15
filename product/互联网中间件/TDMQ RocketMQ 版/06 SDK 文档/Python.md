## 操作场景

本文以调用 Python SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-python-sdk-demo.zip)

## 操作步骤

### 步骤1：准备环境

Rocketmq-client Python 基于 [rocketmq-client-cpp](https://github.com/apache/rocketmq-client-cpp) 进行包装，因此需要先安装 **librocketmq**。

1. 安装 librocketmq （版本2.0.0及以上）， 安装教程参见  [librocketmq 安装](https://github.com/apache/rocketmq-client-python)。
2. 执行如下命令安装 rocketmq-client-python。
<dx-codeblock>
:::  shell
   pip install rocketmq-client-python
:::
</dx-codeblock>


### 步骤2：生产消息

创建并编译运行生产消息程序。
<dx-codeblock>
:::  python
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
:::
</dx-codeblock>
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>groupName</td>
        <td>生产者组名称。在控制台集群管理中 Group 页签中获取。</td>
    </tr>
    <tr>
        <td>nameserver</td>
        <td>集群接入地址，在<b>集群管理</b>页面操作列的<b>接入地址</b>获取。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/88046dcc0b052e11dc5c7c2ee8a901e4.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>secretKey</td>
        <td>角色名称，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制。</td>
    </tr>
    <tr>
        <td>accessKey</td>
        <td>角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制<b>密钥</b>列复制。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/738800581043835d6123385964281f37.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>topicName</td>
        <td>topicName 是<code>命名空间全称</code>+<code>%</code>+<code>topic 名称</code>。
				<ul style = "margin-bottom: 0px;"><li>命名空间全称可在控制台集群管理 Topic 页签中复制，格式是<code>集群 ID</code> +<code>｜</code>+<code>命名空间</code>。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/c483d23c09d2f728aaa08b195d9ddd40.png" style="width: 100%"></li><li>Topic 名称在控制台集群管理 Topic 页签中复制具体 Topic 名称。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/4b096254ae2fa8db0f45c1f864718915.png" style="width: 100%">
						</li>
						</ul>
        </td>
    </tr>
    <tr>
        <td>TAGS</td>
        <td>用来设置订阅消息的 TAG。</td>
    </tr>
		 <tr>
        <td>KEYS</td>
        <td>设置消息业务 key。</td>
    </tr>
</table>

### 步骤3：消费消息

创建并编译运行消费消息程序。
<dx-codeblock>
:::  python
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
:::
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>groupName</td>
        <td>消费者组信息为命名空间全称拼接上 group 名称， 例如：<code>rocketmq-xxx|namespace_python%group11</code>。topic 名称和名称空间名称可在控制台中的命名空间和 Group 页签中获取。</td>
    </tr>
    <tr>
        <td>nameserver</td>
        <td>集群接入地址，在<b>集群管理</b>页面操作列的<b>接入地址</b>获取。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/88046dcc0b052e11dc5c7c2ee8a901e4.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>secretKey</td>
        <td>角色名称，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制。</td>
    </tr>
    <tr>
        <td>accessKey</td>
        <td>角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制<b>密钥</b>列复制。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/738800581043835d6123385964281f37.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>topicName</td>
        <td>topicName 是<code>命名空间全称</code>+<code>%</code>+<code>topic 名称</code>。
				<ul style = "margin-bottom: 0px;"><li>命名空间全称可在控制台集群管理 Topic 页签中复制，格式是<code>集群 ID</code> +<code>｜</code>+<code>命名空间</code>。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/c483d23c09d2f728aaa08b195d9ddd40.png" style="width: 100%"></li><li>Topic 名称在控制台集群管理 Topic 页签中复制具体 Topic 名称。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/4b096254ae2fa8db0f45c1f864718915.png" style="width: 100%">
						</li>
						</ul>
        </td>
    </tr>
    <tr>
        <td>TAGS</td>
        <td>设置订阅消息的 tag，默认为 <code>*</code>，表示订阅所有消息。</td>
    </tr>
</table>



### 步骤4：查看消费详情

登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![](https://qcloudimg.tencent-cloud.cn/raw/924898b7a5568be778449bf51034396d.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-python-sdk-demo.zip) 或 [RocketMQ-Client-Python 示例](https://github.com/apache/rocketmq-client-python/tree/master/samples) 。

