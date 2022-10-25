## 操作场景

本文以调用 Python SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rocketmq/tdmq-rocketmq-python-sdk-demo.zip)

## 操作步骤

### 步骤1：准备环境

Rocketmq-client Python 基于 [rocketmq-client-cpp](https://github.com/apache/rocketmq-client-cpp) 进行包装，因此需要先安装 **`librocketmq`**。

1. 安装 librocketmq （版本2.0.0及以上）， 安装教程参见 [librocketmq 安装](https://github.com/apache/rocketmq-client-python)。
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
   
   # 初始化生产者，并设置生产组信息，组名称使用全称，例：rocketmq-xxx|namespace_python%group1
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
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">groupName</td>
<td align="left">生产者组名称。在控制台集群管理中 <code>Group</code> tab 中获取。</td>
</tr>
<tr>
<td align="left">nameserver</td>
<td align="left">集群接入地址，在控制台<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。新版共享集群与专享集群命名接入点地址在<strong>命名空间</strong>列表获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png" alt=""></td>
</tr>
<tr>
<td align="left">secretKey</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">accessKey</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" alt="img"></td>
</tr>
<tr>
        <td>topicName</td>
        <td>topicName 是<code>命名空间全称</code>+<code>%</code>+<code>topic 名称</code>。
				<ul style = "margin-bottom: 0px;"><li>命名空间全称可在控制台集群管理命名空间页签中复制，格式是<code>集群 ID</code> +<code>｜</code>+<code>命名空间</code>。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/c483d23c09d2f728aaa08b195d9ddd40.png" style="width: 100%"></li><li>Topic 名称在控制台集群管理命名空间页签中复制具体 Topic 名称。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/4b096254ae2fa8db0f45c1f864718915.png" style="width: 100%">
						</li>
						</ul>
        </td>
</tr>
<tr>
<td align="left">TAGS</td>
<td align="left">用来设置消息的 TAG。</td>
</tr>
<tr>
<td align="left">KEYS</td>
<td align="left">设置消息业务 key。</td>
</tr>
</tbody></table>

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
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">groupName</td>
<td align="left">消费者组信息为命名空间全称拼接上 group 名称， 例：rocketmq-xxx|namespace_python%group11。topic 名称和名称空间名称可在控制台中的<code>命名空间</code>  和 <code>G</code>roup tab 中获取</td>
</tr>
<tr>
<td align="left">nameserver</td>
<td align="left">集群接入地址，在控制台<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。新版共享集群与专享集群命名接入点地址在<strong>命名空间</strong>列表获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/45b3582e4d089041cae7030797bc447e.png" alt=""></td>
</tr>
<tr>
<td align="left">secretKey</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">accessKey</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" alt="img"></td>
</tr>
<tr>
<td align="left">topicName</td>
<td align="left">topicName 是<code>命名空间全称</code>+<code>%</code>+<code>topic 名称</code>。<li> 命名空间全称在控制台集群管理中 <code>Topic</code> 页签中页面复制，格式是<strong>集群 ID +｜+命名空间</strong>。<img src="https://qcloudimg.tencent-cloud.cn/raw/9251db01de6d447bbba7d3ca7f3591ef.png" alt=""> </li> <li> Topic 名称在控制台集群管理中 <code>Topic</code> 页签中复制具体 Topic 名称。<img src="https://qcloudimg.tencent-cloud.cn/raw/f27fdecdf352468ef411cfdafc096d86.png" alt=""></li></td>
</tr>
<tr>
<td align="left">TAGS</td>
<td align="left">设置订阅消息的tag，默认为<code>"*"</code>，表示订阅所有消息</td>
</tr>
</tbody></table>



### 步骤4：查看消费详情

登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![img](https://main.qcloudimg.com/raw/7187da67219534d767206553e2a383ab.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rocketmq/tdmq-rocketmq-python-sdk-demo.zip) 或 [RocketMQ-Client-Python示例](https://github.com/apache/rocketmq-client-python/tree/master/samples) 。

