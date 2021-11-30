### 设备接入

<table>
<thead>
<tr>
<th colspan="2">
限制类别&描述	
</th>
<th>
限制参数
</th>
<tr>
</thead>
<tr>
<td>
产品数量
</td>
<td>
一个账号下最多可以创建的产品数。
</td>
<td>
2000
</td>
</tr>
<tr>
<td>
设备数量
</td>
<td>
一个产品最多可以添加的设备数。
</td>
<td>
1000000
</td>
</tr>
<tr>
<td>
网关与子设备
</td>
<td>
一个网关下最多添加的子设备数。
</td>
<td>
1500
</td>
</tr>
<tr>
<td  rowspan="3">
设备分组
</td>
<td>
一个账号下最多可有父分组和子分组的总个数。
</td>
<td>
无限制
</td>
<tr>
<td>
一个分组内最多可添加设备的个数。
</td>
<td>
无限制
</td>
</tr>
<tr>
<td>
一个设备最多可被添加到的分组个数。
</td>
<td>
无限制
</td>
</tr>
<tr>
<td>
远程配置
</td>
<td>
远程配置文件，仅支持 JSON 格式。文件大小的上限。
</td>
<td>
8KB
</td>
</tr>
<tr>
</thead>
<tr>
<td>
数据存储时间
</td>
<td>
产品运行时，产生的属性、事件、服务数据存储时间天数
</td>
<td>
7
</td>
</tr>
<tr>
<td rowspan="2">
文件管理
</td>
<td>
一个账号可存储在物联网平台服务器的文件总大小的上限。
</td>
<td>
1GB
</td>
</tr>
<tr>
<td>
一个设备最多可存储的文件数量。
</td>
<td>
1000
</td>
</tr>
<tr>
<td rowspan="2">
OTA 升级
</td>
<td>
一个升级包文件大小限制。
</td>
<td>
1024
</td>
</tr>
<tr>
<td>
单次批量升级最多可升级的设备数量。
</td>
<td>
10000
</td>
</tr>
</table>

### 消息通信

<table>
<thead>
<tr>
<th colspan="2">
限制类别&描述	
</th>
<th>
限制参数
</th>
<tr>
</thead>
<tr>
<td>
设备接入限制
</td>
<td>
使用同一个设备证书信息，在同一时间，只能和平台服务器建立一个连接。
</td>
<td>
是
</td>
</tr>
<tr>
<td>
连接次数
</td>
<td>
一个设备每秒最大 MQTT 连接请求数。
</td>
<td>
1次/5s
</td>
</tr>
<tr>
<td>
设备订阅数
</td>
<td>
一个设备的最大订阅数。
</td>
<td>
未限制
</td>
</tr>
<tr>
<td  rowspan="2">
请求数量
</td>
<td>
一个账号每秒由设备端向物联网平台发送的请求数。
</td>
<td>
暂不限制
</td>
<tr>
<td>
一个账号每秒由物联网平台向设备端发送的请求数。
</td>
<td>
暂不限制
</td>
</tr>
<tr>
<td rowspan="2">
消息通信限流
</td>
<td>
一个设备每秒最多可上报的消息数量。
</td>
<td>
30
</td>
</tr>
<tr>
<td>
一个设备接收下行消息的最大限制每秒条数（受限于网络环境）
</td>
<td>
50
</td>
</tr>
<tr>
<td>
带宽
</td>
<td>
一个连接每秒的吞吐量（带宽）最大限制。
</td>
<td>
暂不限制
</td>
</tr>
<tr>
<td>
缓存请求数
</td>
<td>
物联网平台限制了每个客户端的最大未确认入站发布请求数。
</td>
<td>
150
</td>
</tr>
<tr>
<td>
消息存储时长
</td>
<td>
QoS1 消息的最大存储时间。
</td>
<td>
24h
</td>
</tr>
<tr>
<td>
MQTT 消息长度
</td>
<td>
MQTT 单个发布消息最大长度。超过此大小的发布请求将被直接拒绝。
</td>
<td>
16KB
</td>
</tr>
<tr>
<td>
CoAP 消息长度
</td>
<td>
CoAP 单个发布消息最大长度。超过此大小的发布请求将被直接拒绝。
</td>
<td>
1KB
</td>
</tr>
<tr>
<td>
MQTT 保活
</td>
<td>
MQTT 连接心跳时间。心跳时间不在此区间内，服务器将会拒绝连接。</td>
<td>
900s
</td>
</tr>
<tr>
<td>
RRPC 超时时间
</td>
<td>
设备响应 RRPC 请求的超时时间。
<td>
10s
</td>
</tr>
<tr>
<td rowspan="2">
离线消息
</td>
<td>
离线消息数量
<td>
单设备最多150条
</td>
</tr>
<tr>
<td>
离线消息存储时长。
<td>
消息最多存储24小时
</td>
</tr>
<tr>
<td>
KeepAlive 时长
</td>
<td>
KeepAlive 时长取值范围
<td>
0-900s
</td>
</tr>
</table>

### Topic

<table>
<thead>
<tr>
<th colspan="2">
限制类别&描述	
</th>
<th>
限制参数
</th>
<tr>
</thead>
<tr>
<td>
自定义 Topic 类数量
</td>
<td>
一个产品最多定义 Topic 类数量。</td>
<td>
100
</td>
</tr>
<tr>
<td>
Topic 长度
</td>
<td>
Topic 长度限制。
</td>
<td>
255字节，UTF-8 编码字符。
</td>
</tr>
<tr>
<td>
Topic 类目
</td>
<td>
一个 Topic 中最多可包含多少个层级类目，即 Topic 中斜杠的最大数量。</td>
<td>
10
</td>
</tr>
<tr>
<td>
订阅数
</td>
<td>
每个订阅请求的最大订阅数。
</td>
<td>
1
</td>
</tr>
<tr>
<td>
操作生效时间
</td>
<td>
订阅和取消订阅都是操作生效时间。
</td>
<td>
5s
</td>
</tr>
<tr>
<td rowspan="2">
广播 Topic
</td>
<td>
要广播的消息主体报文限制。
</td>
<td>
8KB，需要将消息原文转换成二进制数据，并进行 Base64 编码，从而生成消息主体。
</td>
</tr>
<tr>
<td>
服务端 SDK 每分钟全量广播消息。
</td>
<td>
单产品同时只能执行一个任务。
</td>
</tr>
</table>

### 规则引擎

<table>
<thead>
<tr>
<th colspan="2">
限制类别&描述	
</th>
<th>
限制参数
</th>
<tr>
</thead>
<tr>
<td>
规则数量
</td>
<td>
一个账号最多设置规则数。
</td>
<td>
100
</td>
</tr>
<tr>
<td>
流转目标数量
</td>
<td>
一条规则中转发数据的操作数。
</td>
<td>
10
</td>
</tr>
<tr>
<td>
规则引擎处理消息量
</td>
<td>
数据转发为一个账号提供的数据处理能力。
</td>
<td>
无
</td>
</tr>
<tr>
<td>
写入消息量
</td>
<td>
在目标云产品实例性能足够的情况下，数据转发为一个账号提供的数据转发能力。
</td>
<td>
无
</td>
</tr>
<tr>
<td>
流转目标要求
</td>
<td>
数据转发依赖目标产品，需确保目标产品实例正常。目标产品的实例宕机、欠费、参数错误、配置错误等异常状况将会导致消息流转失败。
</td>
<td>
需要实例正常
</td>
</tr>
<tr>
<td >
消息去重
</td>
<td>
数据流转时，为确保消息送达，同一条消息可能重复发送，直到客户端返回 ACK 或消息过期。
</td>
<td>
无，发送消息中的唯一 ID 自由实现。
</td>
</tr>
</table>

### 设备影子&服务端订阅

<table>
<thead>
<tr>
<th colspan="2">
限制类别&描述	
</th>
<th>
限制参数
</th>
<tr>
</thead>
<tr>
<td>
JSON 层级
</td>
<td>
设备影子 JSON 文档的最大层级深度。
</td>
<td>
5
</td>
</tr>
<tr>
<td>
文件大小
</td>
<td>
设备影子 JSON 文档的最大限制。
</td>
<td>
8KB
</td>
</tr>
<tr>
<td>
属性数量
</td>
<td>
设备影子 JSON 文档的属性数量限制。
</td>
<td>
无
</td>
</tr>
<tr>
<td>
每秒请求数
</td>
<td>
每个设备每秒的最大请求数。</td>
<td>
无
</td>
</tr>
<tr>
<td>
失败推送重试策略
</td>
<td>
由于消费客户端离线、消息消费慢等原因，消息不能实时消费，而进入堆积队列。</td>
<td>
无
</td>
</tr>
</table>
