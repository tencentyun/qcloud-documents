## 操作场景

该任务以 Python 客户端为例，指导您使用消息队列 CKafka 数据接入平台Topic并收发消息。

## 前提条件

- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)

## 操作步骤

### 步骤1：准备环境

执行以下命令安装添加 Python 依赖库。
<dx-codeblock>
:::  bash
pip install kafka-python
:::
</dx-codeblock>


### 步骤2：创建 Topic 和订阅关系

1. 在 DIP 控制台的 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页面创建一个 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/0c819b768bba37502eafa6dc974576fa.png)
2. 单击 Topic 的 “ID” 进入基本信息页面，获取用户名、密码和地址信息。
![](https://qcloudimg.tencent-cloud.cn/raw/79ded618f3cdd20e68528fbd5eeca2a8.png)
3. 在**订阅关系**页签，新建一个订阅关系（消费组）。
   ![img](https://qcloudimg.tencent-cloud.cn/raw/ea08126a23715f24c50936d564421655.png)





### 步骤3：生产消息

1. 修改生产消息程序 `producer.py`中配置参数。
<dx-codeblock>
:::  python
 producer = KafkaProducer(
		 bootstrap_servers = ['xx.xx.xx.xx:port'],#地址
		 api_version = (1, 1),
		 security_protocol = "SASL_PLAINTEXT",
		 sasl_mechanism = "PLAIN",
		 sasl_plain_username = "username",#用户名
		 sasl_plain_password = "password",#密码
 )

 message = "Hello World! Hello Ckafka!"
 msg = json.dumps(message).encode()
 producer.send('topic_name', value = msg)#topic名称
 print("produce message " + message + " success.")
 producer.close()
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/06c556b84cdc4b4438989638f0c73045.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>sasl_plain_username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>sasl_plain_password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic_name</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
</tbody></table>
2. 编译并运行 producer.py。
3. 查看运行结果。
![img](https://main.qcloudimg.com/raw/312d264676c655838e398ab9fa03b491.png)

### 步骤4：消费消息

1. 修改消费消息程序 consumer.py 中配置参数。
<dx-codeblock>
:::  python
   consumer = KafkaConsumer(
       'topic_name',#topic名称
       group_id = "group_id",#消费组
       bootstrap_servers = ['xx.xx.xx.xx:port'],#地址
       api_version = (1,1),
   
       security_protocol = "SASL_PLAINTEXT",
       sasl_mechanism = 'PLAIN',
       sasl_plain_username = "username",#用户名
       sasl_plain_password = "password",#密码
   )
   
   for message in consumer:
       print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" %
       (message.topic, message.partition, message.offset, message.value))
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/c38e9070e291e52839e270d40d788cac.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>sasl_plain_username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>sasl_plain_password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic_name</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>group.id</code></td>
<td align="left">消费组名称，在 DIP 控制台的 <strong>订阅关系</strong>列表获取。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/2935f4b6739f48e39287957ef73188a0.png" alt=""></td>
</tr>
</tbody></table>
3. 编译并运行 consumer.py。
4. 查看运行结果。
   ![img](https://main.qcloudimg.com/raw/479f3b14e67a5f50f9d49781ab4df39f.png)