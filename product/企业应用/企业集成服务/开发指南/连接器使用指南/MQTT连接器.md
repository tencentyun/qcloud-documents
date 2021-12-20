
## 简介
MQTT（Message Queuing Telemetry Transport，消息队列遥测传输协议），是一种基于发布/订阅（publish/subscribe）模式的"轻量级"通讯协议，该协议构建于 TCP/IP 协议上。MQTT 最大优点在于，可以以极少的代码和有限的带宽，为连接远程设备提供实时可靠的消息服务。作为一种低开销、低带宽占用的即时通讯协议，使其在物联网、小型设备、移动应用等方面有较广泛的应用。

MQTT 目前主流使用的协议版本是 MQTT V3.1.1版本，iPaaS MQTT 连接器基于该协议实现，可使用 MQTT Consumer 操作从 MQTT Broker 中消费消息，或通过 MQTT Producer 操作，将各类 SaaS 应用产生的消息发布到指定的 Broker 上。

## 连接器配置
### 通用配置标签页

| 参数                | 数据类型 | 描述                                                         | 是否必填 | 默认值    |
| ------------------- | -------- | ------------------------------------------------------------ | -------- | --------- |
| Broker URL          | string   | MQTT Server Broker 地址，格式为 ip:port/path或url:port/path           | 是       |    无       |
| 连接协议       | enum     | 选择连接协议类型，需和 port 对应                                       | 是       | TCP       |
| Client ID    | enum     | 客户端 ID                          | 是       | 无   |
| 用户名          | string   | MQTT 用户名                 | 否       |       无    |
| 密码            | string   | MQTT 密码                   | 否       |      无     |
| TLS 客户端证书  | file   | 使用提供的客户端证书对连接进行加密，仅当连接协议为 TLS 或 WebSocket Secure 时可配置 | 否       |     无      |
| TLS 客户端 Key    | file     | 客户端证书文件对应的 Key 文件，仅当连接协议为 TLS 或 WebSocket Secure 时可配置 | 否       |       无    |
| TLS 服务端证书  | file   | 使用提供的服务端证书对连接进行加密，仅当连接协议为 TLS 或 WebSocket Secure 时可配置 | 否       |    无       |

<img src="https://qcloudimg.tencent-cloud.cn/raw/15e3f536471219f9b7d0ebc55f748c30.png" width="600px">

### 高级配置标签页

| 参数                | 数据类型 | 描述                                                         | 是否必填 | 默认值    |
| ------------------- | -------- | ------------------------------------------------------------ | -------- | --------- |
| 是否启用遗嘱消息    | bool   |            | 否       |  false         |
| 遗嘱主题       | string     | 启用遗嘱后，可填写                        | 否       |    无    |
| 遗嘱内容       | string     | 启用遗嘱后，可填写                        | 否       |   无     |
| 遗嘱 QoS        | enum       | 启用遗嘱后，可填写                        | 否       |    无       |
| 是否保存遗嘱消息  | bool     | 启用遗嘱后，可填写                         | 否       |     无      |
| 是否清除会话    | bool   | clean session       | 否       |   true        |
| 是否顺序发送    | bool   | order               | 否       |   false       |
| keep-alive 超时时间  | string   |  | 否       |    无       |
| ping 超时时间        | string   |  | 否       |     无      |
| connec t超时时间  | string   |  | 否       |   无        |
| 是否自动重试连接  | bool   | auto-reconnect  | 否       |  false         |
| reconnect 最大间隔时间  | string   | 仅当自动重试连接为true时可填写 | 否       |  无         |
| 是否重试 connect  | bool   | retry connect | 否       |   false        |
| connect 重试间隔时间  | string   | 仅当重试connect为true时可填写 | 否       |   无        |
| write 超时时间  | string   |  | 否       |   无        |

<img src="https://qcloudimg.tencent-cloud.cn/raw/6b8e1441e02274b66417d2455d42ef45.png" width="600px">


## 操作配置

MQTT 连接器包含 Consumer（消费消息）和 Producer（生产消息）两种操作。

###  Consumer 操作

#### 输入参数

| 参数       | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| ---------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 订阅主题   | Array Of String   | 订阅的队列名称列表                          | 是       |    无    |
| QoS | enum   | At Most Once                                                   | 否       |     无   |
| 确认模式     | enum     | 消息消费后的应答模式，有两种：  <li>消费后直到触发的流成功结束后才确认 offset </li><li> 消费后立即确认offset，不等待流的触发及运行结果</li>  | 流运行成功后确认       | true   |

![MQTT Consumer](https://qcloudimg.tencent-cloud.cn/raw/1e788102f3b79f2a99d913a155ba19b6.png)	

#### 输出参数
Consumer 操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 的 raw data 为 byte 数组                                |
| error       | <li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 执行成功后，attribute 为 dict，[查看属性列表](#property)                    |
| variable    | 继承上个组件的 variable 信息                                   |

atrrbites 属性列表：[](id:property)

- QoS：int, 0:At most once, 1:At least once, 2:Exactly once
- topic：string, 消费到的消息所属的Topic
- messageID：uint16，消息ID

例如，执行成功后，message payload的raw data 值为 byte 数组，message attribute 值如下：
```json
{
    "QoS": 1,
    "topic": "some topic",
    "messageID": 4
}
```

执行失败后，message error值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "some error message."
}
```

###  Producer 操作

#### 输入参数（通用）


| 参数         | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 主题 | string   | 消息内容将发布到指定的主题                                       | 是       |    无    |
| 消息内容 | string     |                                        | 否       |     无   |
| QoS       | enum   |  | 否       | At Most Once       |
| 是否保存消息     | bool   |                                                      | 否       | false       |

![MQTT Producer](https://qcloudimg.tencent-cloud.cn/raw/86365a513c2f3bdcaa81572b05b30785.png)	

####  输出参数

Publish 操作执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload 信息                                    |
| error       | <li>执行成功后，error为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

执行失败后，message error值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "some error message."
}
```
