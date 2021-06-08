
## 简介
- Apache Kafka 连接器用于连接 Kafka 集群和 iPaaS 集群，可消费 Kafka 集群的消息并作为集成流的 trigger，也可将集成流的消息生产发布到 Kafka 集群中。
- Apache Kafka 是一个分布式发布-订阅消息传递系统，kafka 有以下一些基本概念：
 - **Producer**：消息生产者，即向 kafka broker 发布消息的客户端。
 - **Consumer**：消息消费者，负责消费 Kafka 服务器上的消息。
 - **Topic**：主题，用于建立 Producer 和 Consumer 之间的订阅关系。
 - **Partition**：消息分区，一个 topic 可以分为多个 partition，每个 partition 是一个有序的队列，partition 中的每条消息都会被分配一个有序的 ID（offset）。
 - **Broker**：一台 kafka 服务器即为一个 broker，一个集群由多个 broker 组成，一个 broker 可以容纳多个 topic。
 - **Consumer Group**：消费者分组，用于归组同类消费者，每个 consumer 属于一个特定的 consumer group，多个消费者可以共同消息一个 Topic 下的消息，每个消费者消费其中的部分消息，这些消费者就组成一个分组，拥有同一个分组名称。
 - **Offset**：消息在 partition 中的偏移量，每一条消息在 partition 都有唯一的偏移量，消息者可以指定偏移量来指定要消费的消息。
- Producer、Consumer、Broker 关系如下图：
![](https://main.qcloudimg.com/raw/b0528e274a36f97d334040e590205faf/bc99c2a3176ee1695a3d4f1f4f08a5c8.png)	
- Broker 保存消息数据，和 topic、partition 关系示意图如下：
![](https://main.qcloudimg.com/raw/0ccc812dcce03c8d210f654c0bc95f9b/image-20210426170303717.png)	
- 同一 topic 的各 partition 逻辑关系如下图，kafka 仅保证同一 partition 下的消息有序。
![img](https://main.qcloudimg.com/raw/81d6b33f8147779b18e489445fff4eff/v2-f04083507c2860e62a686c3e868c719a_1440w.jpg)

## 连接器配置
<dx-tabs>
::: 通用配置标签页-连接配置
<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>集群地址</td><td>string</td><td>Apache Kafka 集群地址，配置的格式：ip:port,ip:port</td><td>是</td><td></td></tr><tr><td>集群 Kafka 版本</td><td>enum</td><td>选择 Kafka 集群的版本号</td><td>否</td><td>1.1</td></tr><tr><td>SASL 安全认证模式</td><td>enum</td><td>选择连接到 Kafka 集群时的安全认证模式</td><td>否</td><td>PlainText</td></tr><tr><td>SASL 用户名</td><td>string</td><td>SASL/Plain 和 SASL/SCRAM 安全认证模式下的用户名</td><td>否</td><td></td></tr><tr><td>SASL 密码</td><td>string</td><td>SASL/Plain 和 SASL/SCRAM 安全认证模式下的密码</td><td>否</td><td></td></tr><tr><td>SASL/SCRAM 加密类型</td><td>enum</td><td>SASL/SCRAM 安全认证模式下的加密类型</td><td>否</td><td></td></tr><tr><td>使能 TLS 安全传输协议</td><td>bool</td><td>是否使用 TLS 加密和 Kafka 集群间的连接</td><td>否</td><td>false</td></tr><tr><td>TLS 客户端证书</td><td>file</td><td>可选，使用提供的证书对连接进行加密，仅当使能 TLS 安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr><tr><td>TLS 客户端Key</td><td>file</td><td>可选，使用提供的证书对连接进行加密，需和客户端证书同时提供，仅当使能 TLS 安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr><tr><td>TLS 服务端证书</td><td>file</td><td>可选，使用提供的证书对连接进行加密，仅当使能TLS安全传输协议设置为 True 才可配置</td><td>否</td><td></td></tr></tbody></table>

![](https://main.qcloudimg.com/raw/70cd309b7f199c8d3b2c947ce5d171bb/image-20210426172832136.png)	

:::
::: 通用配置标签页-消费者配置
<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>消费者组</td><td>string</td><td>消费时的所属的消费者组名称</td><td>是</td><td></td></tr><tr><td>主题</td><td>string</td><td>订阅的主题列表，支持正则表达式</td><td>是</td><td></td></tr><tr><td>消费者数量</td><td>int</td><td>消费者组内的消费者数量，必须小于主题的 partition 数量</td><td>否</td><td>1</td></tr></tbody></table>

![](https://main.qcloudimg.com/raw/f94e58a786e90e5fc8a5165316d2edfc/image-20210426172924488.png)	

:::
::: 高级配置标签页-消费者组配置
<table><thead><tr><th>参数</th><th>数据类型</th><th>描述</th><th>是否必填</th><th>默认值</th></tr></thead><tbody><tr><td>消息确认模式</td><td>enum</td><td>消费消息后，在 Kafka 上确认 Offset 的模式，有两种：<br><li>消费后直到触发的流成功结束后才确认 Offset  <br></li><li>消费后立即确认 Offset</li></td><td>否</td><td>流运行成功后确认</td></tr><tr><td>隔离级别</td><td>enum</td><td>Kafka 的事务隔离级别，可选 Read Uncommitted 和 Read committed</td><td>否</td><td>Read Uncommitted</td></tr><tr><td>重试阻塞时间</td><td>int</td><td>重试阻塞时间（毫秒），避免在失败场景下以紧密循环的方式重复发送请求</td><td>否</td><td>2000</td></tr><tr><td>请求超时时间</td><td>int</td><td>请求超时时间（毫秒）</td><td>否</td><td>30000</td></tr><tr><td>会话超时时间</td><td>int</td><td>会话超时时间（毫秒）</td><td>否</td><td>10000</td></tr><tr><td>心跳时间</td><td>int</td><td>心跳时间（毫秒）</td><td>否</td><td>3000</td></tr><tr><td>Rebalance 检测频率</td><td>int</td><td>Rebalance 检测频率（毫秒），Kafka 消费者组重平衡检测的间隔时间</td><td>否</td><td>60000</td></tr><tr><td>Rebalance 策略</td><td>enum</td><td>Rebalance 策略，按区间划分（Range）和轮询（RoundRobin）两种策略</td><td>否</td><td>Range</td></tr><tr><td>Rebalance 最大重试次数</td><td>int</td><td>Rebalance 最大重试次数</td><td>否</td><td>4</td></tr><tr><td>Rebalance 重试阻塞时间</td><td>int</td><td>Rebalance 重试阻塞时间（毫秒）</td><td>否</td><td>2000</td></tr><tr><td>最小拉取数据量</td><td>int</td><td>最小拉取数据量（字节）</td><td>否</td><td>1</td></tr><tr><td>默认拉取数据量</td><td>int</td><td>默认拉取数据量（字节） ，默认为1048756(1024*1024)</td><td>否</td><td>1048576</td></tr><tr><td>最大拉取数据量</td><td>int</td><td>最大拉取数据量（兆），设置为0时无限制</td><td>否</td><td>0</td></tr><tr><td>拉取阻塞时间</td><td>int</td><td>拉取阻塞时间（毫秒）</td><td>否</td><td>250</td></tr><tr><td>提交频率</td><td>int</td><td>提交频率（毫秒）</td><td>否</td><td>1000</td></tr><tr><td>初始偏移量</td><td>enum</td><td>初始偏移量，取值为 Offset Newest 和 Offset Latest</td><td>否</td><td>Offset Newest</td></tr><tr><td>偏移量保留的时间</td><td>int</td><td>偏移量保留的时间（秒），0表示不过期</td><td>否</td><td>0</td></tr></tbody></table>

![image-20210426173044144](https://main.qcloudimg.com/raw/6ea8a869d66e6eff056a177fe5f1d7de/image-20210426173044144.png)
:::
::: 高级配置标签页-生产者配置
| 参数                     | 数据类型 | 描述                                                         | 是否必填 | 默认值     |
| ------------------------ | -------- | ------------------------------------------------------------ | -------- | ---------- |
| 最大消息限制             | int      | 最大消息限制（字节），单条消息允许发送的最大数据量             | 否       | 1000000    |
| 确认模式                 | enum     | 确认模式，可选值为：None、LeaderOnly、All。其中 None 为不需确认，LeaderOnly 仅需 Leader 确认，All 需要 Leader 及所有 follower 都确认 | 否       | LeaderOnly |
| 请求超时时间             | int      | 请求超时时间                                                 | 否       | 10000      |
| 幂等性使能开关           | bool     | 幂等性使能开关，设置为 true 时，打开 kafka 幂等性功能，实现 Exactly-Once 语义 | 否       | false      |
| 消息刷新到磁盘的数据量   | int      | 消息刷新到磁盘的数据量（字节），设置为0时不设置该参数          | 否       | 0          |
| 消息刷新到磁盘的消息数量 | int      | 消息刷新到磁盘的消息数量，设置为0时不设置该参数              | 否       | 0          |
| 消息刷新到磁盘的间隔时间 | int      | 消息刷新到磁盘的间隔时间（毫秒），设置为0时不设置该参数        | 否       | 0          |
| 消息刷新的最大消息量     | int      | 消息刷新的最大消息量，设置为0时不设置该参数                  | 否       | 0          |

![](https://main.qcloudimg.com/raw/eb768a3fbd5a7187237b3174a3f6ede2/image-20210426173227817.png)	

:::
</dx-tabs>


## 操作配置

Apache Kafka 连接器包含 Consumer 和 Publish 两种操作。

### Consumer 操作
#### 输入参数
None，Consumer 操作没有输入参数。
![image-20210426173307712](https://main.qcloudimg.com/raw/2c448cd5f1ef1036401c607764da7653/image-20210426173307712.png)

####  输出
Consumer 操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 byte 数组                                |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 执行成功后，attribute 为 dict，属性列表见下表。                   |
| variable    | 继承上个组件的 variable 信息                                   |

**atrrbites 属性列表：**

| atrrbites 属性 | 数据类型 | 描述 | 
|---------|---------|---------|
| topic | string| 消息所属的 topic | 
| partition | int32| 消息的 partition | 
|offset | int64| 消息的 offset | 

例如：执行成功后，message payload 值为 byte 数组，message attribute 值如下：
```json
{
    "topic": "test-topic",
    "partition": 1,
    "offset": 4
}
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "kafka: client has run out of available brokers to talk to (Is your cluster reachable?)"
}
```

#### 案例
1. 按照 Kafka 集群信息，填写 kafka 连接器配置。
![](https://main.qcloudimg.com/raw/f100d37faac267dbaba29a3f2225337f/image-20210426182517246.png)	
2. 新建流，将 kafka consumer 作为 trigger 节点。
![](https://main.qcloudimg.com/raw/71f1c1aab2737fbbdad70826684ccef7/image-20210426182558860.png)	
3. 添加其他业务逻辑，处理消费到的数据，例如：增加 amqp publish，将消费到的消息发布到 rabbitMQ。
![](https://main.qcloudimg.com/raw/ef98f8533e1a436280f0ca8056cff730/image-20210426182730034.png)	
4. 若配置正确，流发布后，可以看到 kafka 中的流被正确消费，且被发布到 rabbitMQ 中。

### Publish 操作
#### 输入参数
**通用配置**

| 参数                  | 数据类型       | 说明                  | 是否必填 | 默认值 |
| --------------------- | -------------- | --------------------- | -------- | ------ |
| 要写入的 Kafka 主题名称 | string         | 写入的 kafka 主题       | 是       |        |
| 要写入的 Kafka 消息内容 | string或byte | 待发布的 Kafka 消息内容 | 是       |        |

![](https://main.qcloudimg.com/raw/9954069f0d2b4e5abf143354eab6530e/image-20210426183248082.png)	

**高级配置**

| 参数          | 数据类型 | 说明                                  | 是否必填 | 默认值 |
| ------------- | -------- | ------------------------------------- | -------- | ------ |
| 目标 partition | string   | 指定写入的 partition                   | 否       |        |
| key           | string   | key 相同的 message 会写入到同一 partition | 否       |        |
| header        | string   | header的 JSON 字符串                    | 否       |        |

![](https://main.qcloudimg.com/raw/088f146b1298091055cb2179a64156cd/image-20210426183310650.png)	

####  输出

Publish 操作执行成功后，输出属性会保存在 message 消息体的 attribute；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 执行成功后，attribute 为 dict，属性列表见下                    |
| variable    | 继承上个组件的 variable 信息                                   |

**atrrbites 属性列表：**

| atrrbites 属性 | 数据类型 | 描述 | 
|---------|---------|---------|
| topic | string| 消息所属的 topic | 
| partition | int32| 消息的 partition | 
|offset | int64| 消息的 offset | 

例如：执行成功后，message attribute 值如下：
```json
{
    "topic": "test-topic",
    "partition": 1,
    "offset": 4
}
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "kafka: client has run out of available brokers to talk to (Is your cluster reachable?)"
}
```

#### 案例
1. 按照 Kafka 集群信息，填写 kafka 连接器配置。
![](https://main.qcloudimg.com/raw/f100d37faac267dbaba29a3f2225337f/image-20210426182517246.png)	
2. 新建流，添加 trigger，例如：HTTP listener。
![](https://main.qcloudimg.com/raw/c9f5431f0a1c1cef9aa5bf2df51247a7/image-20210426183648712.png)	
3. 在流中增加 kafka publish 操作，填写消息内容，将消息发布到 Kafka 集群中。
![](https://main.qcloudimg.com/raw/ddce99bb9dd7c50b277f4cd9aab537cf/image-20210426183719986.png)	
4. 发布流，触发流后，若连接参数及消息参数配置正确，消息将成功投递到所配置的 Kafka 集群的对应队列中。
