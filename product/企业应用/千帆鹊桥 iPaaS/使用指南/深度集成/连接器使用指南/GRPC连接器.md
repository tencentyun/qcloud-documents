
## 简介

GRPC:Request 连接器作为 GRPC 客户端，可以发起 GRPC 请求并将得到的响应作为消息传递给下一个组件。



## 操作说明

### 输入参数

GRPC:Request 操作配置包括基本配置、服务定义、GRPC 参数和安全网关配置：
<img src="https://qcloudimg.tencent-cloud.cn/raw/fa43806031544934577a29c2d9850fb4.png" width="500px">

>?您可以点击以下页签，查看操作配置中涉及到的不同模块的参数描述。


<dx-tabs>
::: 基本配置
| 参数           | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 请求域名       | string   | 对应的请求域名                                               | 是           | 无         |
| 请求端口       | int      | 请求端口                                                     | 是           | 无         |
| 认证机制       | enum     | 默认为 No Auth，目前支持 Basic Auth，如果为 Basic Auth，则需配置用户名、密码 | 否           | No Auth    |
| 用户名         | string   | 用户名                                                       | 否           | 无         |
| 密码           | string   | 密码                                                         | 否           | 无         |
| 启用 SSL/TLS    | bool     | 是否启用 SSL/TLS                                              | 否           | false      |
| 服务器证书文件 | file     | 服务器证书文件                                               | 否           | 无         |
| 请求体         | entity   | GRPC 请求发送的请求体                                         | 是           | 无         |
:::
::: 服务定义
| 参数                  | 数据类型 | 描述                        | **是否必填** | **默认值** |
| --------------------- | -------- | --------------------------- | ------------ | ---------- |
| Proto 文件             | file     | GRPC 请求的服务端的 proto 文件 | 是           | 无         |
| Proto 文件过期时间（秒） | int      | Proto 文件的缓存过期时间     | 否           | 300        |
| 服务名称              | string   | GRPC 请求的服务名称          | 是           | 无         |
| 方法名称              | string   | GRPC 请求的方法名称          | 是           | 无         |
:::
::: GRPC 参数
| 参数                     | 参数类型 | 描述                                     | 是否必填 | 默认值      |
| ------------------------ | -------- | ---------------------------------------- | -------- | ----------- |
| 保活心跳间隔时间（秒）     | int      | GRPC 请求的保活心跳间隔时间，最小为10 | 否       | 60          |
| 保活心跳确认超时时间（秒）  | int      | GRPC 请求的保活心跳确认超时时间       | 否       | 20          |
| 是否允许发送保活心跳     | bool     | 是否允许发送保活心跳                     | 否       | false       |
| 连接超时时间（秒）         | int      | 连接超时时间                       | 否       | 60          |
| 最大消息大小（MB）       | int      | GRPC 请求发送和接收的最大消息大小     | 否       | 5           |
| 负载均衡策略             | enum     | GRPC 请求的负载均衡策略                   | 否       | Round Robin |
:::
::: 安全网关配置
| 参数     | 数据类型 | 描述                                    | **是否必填** | **默认值** |
| -------- | -------- | --------------------------------------- | ------------ | ---------- |
| 安全网关 | string   | 直接请求内网域名/IP 时，需要绑定安全网关 | 否           | 无         |
:::
</dx-tabs>



### 输出参数

GRPC:Request 请求的响应返回后，会将响应结果生成对应的消息传递给下一个组件。其中，响应的 body 会放到消息的 payload 中。

GRPC:Request 输出消息描述：

| 消息属性   | 值                                                           |
| ---------- | ------------------------------------------------------------ |
| payload    | 响应 body 保存在 payload 中                                      |
| error      | 执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attributes | 默认为空                                                     |
| variables  | 默认为空                                                     |

### 案例

1. 组件筛选 GRPC:Request：
<img src="https://qcloudimg.tencent-cloud.cn/raw/94c07765ca29a6220eb9dc986c26bc6a.png" width="500px">

2. 新建 GRPC:Request 连接器：
<img src="https://qcloudimg.tencent-cloud.cn/raw/a0f469da0f9766212740185399ea5b58.png" width="500px">

3. 使用操作配置：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d63090ed322c85e7adbcc54e9af3e17e.png" width="500px">

4. 发布并触发：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e0454006622760e9589642fbda04fc2d.png" width="500px">
