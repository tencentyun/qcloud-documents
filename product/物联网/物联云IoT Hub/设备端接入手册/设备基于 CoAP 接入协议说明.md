
目前物联网通信支持 CoAP 标准协议接入。 具体的协议请参考 [RFC7252](https://tools.ietf.org/html/rfc7252) 协议文档。

## 和标准 CoAP 区别
1. 目前只支持消息的上报，将 SDK 的信息上传到物联网通信。
2. 支持 POST 方法，不支持 GET/PUT/DELETE 方法。 

## CoAP 通道，安全等级
1. 支持 DTLS 的协议来建立安全连接，安全级别高。
2. 支持非对称加密。

## URI 规范
CoAP 消息发送到 URI，URI 的格式为`/${productId}/${deviceName}/xxx`，productId 为在控制台注册的产品 ID，deviceName 为 productId 产品下的设备名称。

默认情况下创建产品后，该产品下的所有设备都拥有以下 Topic 类的权限：
1. `${productId}/${deviceName}/event`发布。
2. `${productId}/${deviceName}/control`订阅。

即 URI 与 MQTT Topic 相对应。
