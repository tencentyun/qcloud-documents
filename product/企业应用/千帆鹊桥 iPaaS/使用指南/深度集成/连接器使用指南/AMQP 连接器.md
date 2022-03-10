## 简介

AMQP 连接器用于连接 RabbitMQ 集群和 iPaaS 集群，可消费 RAbbitMQ 集群的消息并作为集成流的 trigger，也可将集成流的消息生产发布到 RabbitMQ 集群中。

AMQP 连接器遵从 AMQP 0.9.1 协议。AMQP 协议基本概念如下：

![img](https://main.qcloudimg.com/raw/be3753c8ad7e8916163cb27603e7d635/v2-16ff33136781adf0fa51cbe31fb25eec_1440w.jpg)

- **Producer**：生产者，负责向 RabbitMQ 投递消息（实际是向交换机投递而非消息队列）。
- **RoutingKey**：路由键，生产者投递消息时所指定的参数，用于交换机根据一定的路由规则转发消息到相关消息队列中。
- **Consumer**：消费者，负责从 RabbitMQ 的消息队列中接收消息。
- **Exchange**：交换机。生产者在向 RabbitMQ 投递消息时，并不能直接将消息投递到消息队列中。实际上，生产者是将消息投递到生产者所指定交换机上，不同类型的交换机具有其各自的路由规则，交换机根据一定的路由规则（使用消息所携带的 RoutingKey 和绑定在该交换机上的消息队列的 BindingKey），再将消息转发给相应的消息队列上。
- **Queue** : 消息队列，用于接收、储存交换机转发的消息，消费者通过其接收、消费消息。
- **BindingKey** : 绑定键，在消息队列绑定到交换机的过程中，可以指定 BindingKey 参数，用于交换机根据一定的路由规则转发消息到相关消息队列中。


## 连接器配置
<dx-tabs>
::: 连接配置参数

<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>集群地址</td><td>string</td><td>rabbitMQ 集群地址</td><td>是</td><td></td></tr><tr><td>集群端口</td><td>int</td><td>rabbitMQ 集群端口号</td><td>是</td><td></td></tr><tr><td>虚拟集群地址</td><td>string</td><td>虚拟集群地址</td><td>否</td><td>/</td></tr><tr><td>用户名</td><td>string</td><td>rabbitMQ 集群用户名</td><td>否</td><td></td></tr><tr><td>密码</td><td>string</td><td>rabbitMQ 集群密码</td><td>否</td><td></td></tr><tr><td>使能 TLS 安全传输协议</td><td>bool</td><td>是否使用 TLS 加密和 rabbitMQ 集群间的连接</td><td>否</td><td>false</td></tr><tr><td>TLS 客户端证书</td><td>file</td><td>可选，使用提供的证书对连接进行加密，仅当使 TLS 安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr><tr><td>TLS 客户端 Key</td><td>file</td><td>可选，使用提供的证书对连接进行加密，需和客户端证书同时提供，仅当使 TLS 安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr><tr><td>TLS 服务端证书</td><td>file</td><td>可选，使用提供的证书对连接进行加密，仅当使 TLS 安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr></tbody></table>


![](https://main.qcloudimg.com/raw/737b00c725c981459c964456f09d9d42/image-20210426162650164.png)	

:::
::: 通用配置

<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>消息类型</td><td>enum</td><td>消息类型，默认为 text/plain</td><td>否</td><td>text/plain</td></tr><tr><td>消息编码格式</td><td>enum</td><td>消息编码格式</td><td>否</td><td>UTF-8</td></tr></tbody></table>


![](https://main.qcloudimg.com/raw/ca7ef4619b0e59cfaa35baecf76ff8f2/image-20210426162825272.png)	

:::
::: 消费者配置

<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>应答模式</td><td>enum</td><td>消息消费后的应答模式分为两种：<br><li>  消费后直到触发的流成功结束后才确认 offset  <br></li><li> 消费后立即确认 offset</li></td><td>否</td><td>流运行成功后确认</td></tr><tr><td>消费模式</td><td>enum</td><td>消费模式，可选：<br><li> 拉模式<br></li><li> 推模式</li></td><td>否</td><td>拉模式</td></tr><tr><td>NoLocal</td><td>bool</td><td>设置为 true，表示不能将同一个 Connection 中生产者发送的消息传递给该 Connection 中的消费者</td><td>否</td><td>false</td></tr><tr><td>Exclusive</td><td>bool</td><td>设置为是否排他</td><td>否</td><td>false</td></tr><tr><td>消费者数量</td><td>int</td><td>设置消费者数量</td><td>否</td><td>1</td></tr></tbody></table>


![](https://main.qcloudimg.com/raw/6ec1f9c4f7d70f51a90f9f5d8743a4ad/image-20210426162934914.png)	

:::
::: 生产者配置

| 参数     | 数据类型 | 描述                                    | 是否必填 | 默认值 |
| -------- | -------- | --------------------------------------- | -------- | ------ |
| 投递模式 | int      | 生产消息时的投递模式（持久化/不持久化） | 否       | 持久化 |


![](https://main.qcloudimg.com/raw/eb29ad4c9acfe0fd35d4ea254aadb8e4/image-20210426163259478.png)	

:::
::: 服务质量配置

| 参数             | 数据类型 | 描述     | 是否必填 | 默认值 |
| ---------------- | -------- | -------- | -------- | ------ |
| 预取大小（字节） | int      | 预取大小 | 否       | 0      |
| 预取数量         | int      | 预取数量 | 否       | 0      |


![](https://main.qcloudimg.com/raw/3e75ae3d112df57d59031b35299b394a/image-20210426163320374.png)	

:::
</dx-tabs>

## 操作配置
AMQP 连接器包含 Consumer 和 Publish 两种操作。

### Consumer 操作
#### 输入参数

| 参数       | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| ---------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 队列名称   | string   | 消费的队列名称                                               | 是       |     -   |
| 消费者标识 | string   | 消费者标识                                                   | 否       |     -   |
| NoWait     | bool     | 为 true 时，client 端将不会等待 server 的 response，server 也不会 response；若 server 无法完成消费请求，则会抛出 channel 或 connection异常。 | 否       | true   |

![](https://main.qcloudimg.com/raw/dc3580023f45ca3b9b80ae7556bd2527/image-20210408151251318.png)	

#### 输出

Consumer 操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 byte 数组                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 执行成功后，attribute 为 dict，属性列表见下表                    |
| variable    | 继承上个组件的 variable 信息                                   |

**atrrbites 属性列表：**

| atrrbites 属性 | 数据类型                                    |
| -------------- | ------------------------------------------- |
| headers        | map[string]interface{}                      |
| deliveryMode   | uint8，non-persistent (1) or persistent (2) |
| priority       | uint8，0 to 9                               |
| correlationId  | string                                      |
| replyTo        | string                                      |
| expiration     | string                                      |
| messageId      | string                                      |
| timestamp      | time.Time                                   |
| type           | string                                      |
| userId         | string                                      |
| appId          | string                                      |

例如：执行成功后，message payload 值为 byte 数组，message attribute 值如下：

```json
{
    "headers": {},
    "deliveryMode": 1,
    "priority": 4,
    "correlationId": "someId",
    "replyTo": "some_replyto",
    "expiration": "messageId",
    "timestamp": "2021-04-25T15:30:30Z08:00",
    "type": "",
    "userId": "",
    "appId": ""
}
```

执行失败后，message error 值如下：

```json
{
    "Code": "CORE:RUNTIME",
    "Description": "some error message."
}
```

####  案例
1. 按照 rabbitMQ 集群信息，填写 AMQP 连接器配置的连接配置，其他配置保持默认。
   ![image-20210426154407837](https://main.qcloudimg.com/raw/94994df1e398e21b56d39b33e54be92c/image-20210426154407837.png)
2. 新建流，将 AMQP Consumer 作为 trigger 节点，配置待消费的队列名称。
   ![image-20210426154524045](https://main.qcloudimg.com/raw/cfad6d19d5c483f930b525f500875397/image-20210426154524045.png)
3. 添加其他业务逻辑，处理消费到的数据。例如：发布到 kafka。
![](https://main.qcloudimg.com/raw/a92e0704ae588ab5c6bb47c0fdb97e5f/image-20210426154934076.png)	
4. 若参数配置正确，流发布后，即可将 rabbitMQ 的消息消费并发布到 kafka 队列中。

### Publish 操作

#### 输入参数

<dx-tabs>
::: 通用配置
| 参数         | 数据类型 | 说明                                                         | 是否必填 | 
| ------------ | -------- | ------------------------------------------------------------ | -------- |
| Exchange 名称 | string   | AMQP 模型的 Exchange 名称                                       | 是       |  
| Exchange 类型 | enum     | AMQP 模型的 Exchange 类型                                       | 是       |      
| 路由键       | string   | 生产者投递消息时所指定的参数，用于交换机根据一定的路由规则转发消息到相关消息队列中 | 否       |      
| 上下文 ID     | string   | 上下文 ID                                                     | 否       |        

![](https://main.qcloudimg.com/raw/45c58ec7acd9b320372a0ad076ef87b6/image-20210426163614955.png)	

:::
::: Exchange 配置
| 参数                                       | 数据类型 | 说明                                           | 是否必填 | 默认值 |
| ------------------------------------------ | -------- | ---------------------------------------------- | -------- | ------ |
| 不等待服务端确认投递结果（NoWait）         | bool     | 设置为 True 时，客户端不等待服务端确认投递结果   | 否       | false  |
| 是否持久化                                 | bool     | 设置是否持久化                                 | 否       | true   |
| 是否自动删除                               | bool     | 设置是否自动删除                               | 否       | false  |

![image-20210426163635595](https://main.qcloudimg.com/raw/bb5486f9f56cca10c96ab1f4c0df7a84/image-20210426163635595.png)
:::
::: 消息配置
| 参数               | 数据类型 | 说明                                     | 是否必填 | 默认值  |
| ------------------ | -------- | ---------------------------------------- | -------- | ------- |
| 优先级             | int      | 设置消息优先级                           | 否       | 0       |
| 消息标识 ID         | string   | 设置消息标识 ID                           | 否       |  -       |
| 应答队列名称       | string   | 设置应答队列名称                         | 否       |     -    |
| 消息存活时间（毫秒） | int      | 设置消息存活时间                         | 否       | 1800000 |
| 生产者用户 ID       | string   | 生产者用户 ID                             | 否       | -        |
| 生产者应用 ID       | string   | 生产者应用 ID                             | 否       |  -       |
| 消息类型           | string   | 消息的 MIME 类型                           | 否       | -        |
| 消息头             | map      | 消息头，字典类型，可添加用户自定义 header | 否       |    -     |
| 消息体             | string   | 消息体，投递的具体消息内容               | 否       |   -      |

![](https://main.qcloudimg.com/raw/6ed92019a7639e76d634a9e0270ddbfe/image-20210426163717757.png)	
:::
</dx-tabs>



####  输出

Publish 操作执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

执行失败后，message error 值如下：

```json
{
    "Code": "CORE:RUNTIME",
    "Description": "some error message."
}
```

#### 案例
1. 按照 rabbitMQ 集群信息，填写 AMQP 连接器配置的连接配置，其他配置保持默认。
   ![image-20210426154407837](https://main.qcloudimg.com/raw/94994df1e398e21b56d39b33e54be92c/image-20210426154407837.png)
2. 新建流，添加 trigger，例如：http_listener。
   ![image-20210426160900282](https://main.qcloudimg.com/raw/d925de11b15322ac75ed9393a15f9900/image-20210426160900282.png)
3. 在流中增加 amqp publish 操作，填写消息属性及消息内容。
![image-20210426160829456](https://main.qcloudimg.com/raw/52ee09fa46761f26bad6bf87afc84916/image-20210426160829456.png)
![image-20210426160947755](https://main.qcloudimg.com/raw/7368579eb40d73bae40653831ee16e45/image-20210426160947755.png)
4. 发布流，触发流后，若连接参数及消息参数配置正确，消息将成功投递到所配置的 rabbitMQ 集群的对应队列中。
:::
</dx-tabs>
