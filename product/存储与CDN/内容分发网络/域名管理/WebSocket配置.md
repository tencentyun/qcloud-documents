如果您的业务有弹幕聊天、互动直播、社交订阅、协同会话、多玩家游戏、行情播报、体育实况更新、在线教育和物联网等场景，您可在 ECDN 全站加速配置WebSocket。

## 功能介绍

WebSocket 协议是基于 TCP 的一种持久化协议，它实现了客户端与服务器全双工（full-duplex）通信，允许服务器主动发送信息给客户端。在 Websocket 协议之前，实现客户端和服务端双工通讯的 Web App 需要通过不断发送 HTTP 请求呼叫来进行询问，这导致了服务成本增加和效率低下的问题。WebSocket 具有全双工通信的优势，客户端和服务器只需要完成一次握手，两者之间就可创建持久性的连接并能实现双向数据的传输，能更好地节省服务器资源和带宽，并且能够更实时地进行通讯。 

## 注意事项

1. WebSocket 是 ECDN 全站加速特性功能，配置WebSocket前请先选择 ECDN 全站加速域名。
2. WebSocket 属于动态资源，无需配置任何缓存规则，同时需要源站支持 WebSocket。
3. WebSocket 超时时间配置最大可以设置300s，如果已配置时间内没有消息传递，将默认关闭连接。


## 配置说明

### 域名管理内配置

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)；
2. 单击左侧菜单内的 **域名管理**，进入域名管理列表；
3. 选择需要配置的 ECDN 全站加速域名，单击**管理进入**域名配置页面；
4. 单击**高级配置**，找到 WebSocket 超时时间配置，即可启用 WebSocket；
![](https://qcloudimg.tencent-cloud.cn/raw/47464f41b884033e49ebe0b2b5fbedb5.png)
5. 启用 WebSocket 后，您可以在 0- 300s 内自定义编辑超时时间。

### 推荐配置

WebSocket 是客户端和源站间建立的会话连接，建议根据您的心跳包机制配置 WebSocket 超时时间，若您的 WebSocket 没有心跳包机制则您的 WebSocket 超时时间建议配置成60s

### 配置约束
 
WebSocket 超时时间配置仅支持ECDN全站加速域名，若您域名不属于 ECDN 全站加速域名（加速类型为 ECDN 动静加速和 ECDN 动态加速），您的域名将无法配置 WebSocket。

## 配置示例

### 示例一

若 WebSocket 为关闭状态，域名 `cloud.tencent.com` 的 WebSocket 超时时间配置项如下：
![](https://qcloudimg.tencent-cloud.cn/raw/13828cad2c5b4ec6e27dba5b71b3276c.png)
`cloud.tencent.com` 不支持 WebSocket协议，如有 WebSocket 请求，连接容易断开或失败。

### 示例二

若 WebSocket 为开启状态，并且超时时间配置100s，域名 `cloud.tencent.com` 的 WebSocket 超时时间配置项如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5633675c828f8517af9da7b840f81378.png)

`cloud.tencent.com` 支持 WebSocket 协议，协议的会话保持时间遵循 WebSocket 超时时间配置的100s做会话保持，超过100s 无通讯请求即断开连接。

## 关联的常见问题

[CDN 支持 WebSocket 吗？](https://cloud.tencent.com/document/product/228/11200#q26)
