## MQTT连接器

### 1. 简介
MQTT（Message Queuing Telemetry Transport，消息队列遥测传输协议），是一种基于发布/订阅（publish/subscribe）模式的"轻量级"通讯协议，该协议构建于TCP/IP协议上，由IBM在1999年发布。MQTT最大优点在于，可以以极少的代码和有限的带宽，为连接远程设备提供实时可靠的消息服务。作为一种低开销、低带宽占用的即时通讯协议，使其在物联网、小型设备、移动应用等方面有较广泛的应用。
MQTT目前主流使用的协议版本是MQTT V3.1.1版本，iPaaS MQTT连接器基于该协议实现，可使用MQTT Consumer操作从MQTT Broker中消费消息，或通过MQTT Producer操作，将各类SaaS应用产生的消息发布到指定的Broker上。

### 2. 连接器配置
通用配置标签页

| 参数                | 数据类型 | 描述                                                         | 是否必填 | 默认值    |
| ------------------- | -------- | ------------------------------------------------------------ | -------- | --------- |
| Broker URL          | string   | MQTT Server Broker地址，格式为ip:port/path或url:port/path           | 是       |           |
| 连接协议       | enum     | 选择连接协议类型，需和port对应                                       | 是       | TCP       |
| Client ID    | enum     | 客户端ID                          | 是       |    |
| 用户名          | string   | MQTT用户名                 | 否       |           |
| 密码            | string   | MQTT密码                   | 否       |           |
| TLS客户端证书  | file   | 可选，使用提供的客户端证书对连接进行加密，仅当连接协议为TLS或WebSocket Secure时可配置 | 否       |           |
| TLS客户端Key    | file     | 可选，客户端证书文件对应的Key文件，仅当连接协议为TLS或WebSocket Secure时可配置 | 否       |           |
| TLS服务端证书  | file   | 可选，使用提供的服务端证书对连接进行加密，仅当连接协议为TLS或WebSocket Secure时可配置 | 否       |           |

![MQTT连接器通用配置](https://qcloudimg.tencent-cloud.cn/raw/56cc90fd421b9c4d65a82b110d645f66.png)

高级配置标签页

| 参数                | 数据类型 | 描述                                                         | 是否必填 | 默认值    |
| ------------------- | -------- | ------------------------------------------------------------ | -------- | --------- |
| 是否启用遗嘱消息    | bool   |            | 否       |  false         |
| 遗嘱主题       | string     | 启用遗嘱后，可填写                        | 否       |        |
| 遗嘱内容       | string     | 启用遗嘱后，可填写                        | 否       |        |
| 遗嘱QoS        | enum       | 启用遗嘱后，可填写                        | 否       |           |
| 是否保存遗嘱消息  | bool     | 启用遗嘱后，可填写                         | 否       |           |
| 是否清除会话    | bool   | clean session       | 否       |   true        |
| 是否顺序发送    | bool   | order               | 否       |   false       |
| keep-alive超时时间  | string   |  | 否       |           |
| ping超时时间        | string   |  | 否       |           |
| connect超时时间  | string   |  | 否       |           |
| 是否自动重试连接  | bool   | auto-reconnect  | 否       |  false         |
| reconnect最大间隔时间  | string   | 仅当自动重试连接为true时可填写 | 否       |           |
| 是否重试connect  | bool   | retry connect | 否       |   false        |
| connect重试间隔时间  | string   | 仅当重试connect为true时可填写 | 否       |           |
| write超时时间  | string   |  | 否       |           |

![MQTT连接器高级配置](https://qcloudimg.tencent-cloud.cn/raw/6b8e1441e02274b66417d2455d42ef45.png)

### 3. 操作配置

MQTT连接器包含Consumer和Producer两种操作

#### 3.1 Consumer操作

##### 输入参数：

| 参数       | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| ---------- | -------- | ------------------------------------------------------------ | -------- | ------ |
| 订阅主题   | Array Of String   | 订阅的队列名称列表                          | 是       |        |
| QoS | enum   | At Most Once                                                   | 否       |        |
| 确认模式     | enum     | 消息消费后的应答模式，有两种：  1. 消费后直到触发的流成功结束后才确认offset  2. 消费后立即确认offset，不等待流的触发及运行结果  | 流运行成功后确认       | true   |

![MQTT Consumer](https://qcloudimg.tencent-cloud.cn/raw/1e788102f3b79f2a99d913a155ba19b6.png)	

##### 输出参数
Consumer操作执行成功后，输出结果会保存在message消息体的payload；执行失败后，错误信息会保存在Message消息体的error。

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload的raw data为byte数组                                |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 执行成功后，attribute为dict，属性列表见下                    |
| variable    | 继承上个组件的variable信息                                   |

atrrbites属性列表：

- QoS：int, 0:At most once, 1:At least once, 2:Exactly once
- topic：string, 消费到的消息所属的Topic
- messageID：uint16，消息ID

例如，执行成功后，message payload的raw data值为byte数组，message attribute值如下：

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

#### 3.2 Producer操作

##### 输入参数：

通用：

| 参数         | 数据类型 | 说明                                                         | 是否必填 | 默认值 |
| ------------ | -------- | ------------------------------------------------------------ | -------- | ------ |
| 主题 | string   | 消息内容将发布到指定的主题                                       | 是       |        |
| 消息内容 | string     |                                        | 否       |        |
| QoS       | enum   |  | 否       | At Most Once       |
| 是否保存消息     | bool   |                                                      | 否       | false       |

![MQTT Producer](https://qcloudimg.tencent-cloud.cn/raw/86365a513c2f3bdcaa81572b05b30785.png)	

#####  输出参数

Publish操作执行失败后，错误信息会保存在message消息体的error。

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的payload信息                                    |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的attribute信息                                  |
| variable    | 继承上个组件的variable信息                                   |

执行失败后，message error值如下：

```json
{
    "Code": "CORE:RUNTIME",
    "Description": "some error message."
}
```
