
目前物联网通信支持 MQTT 标准协议接入(兼容3.1.1版本协议)，具体的协议请参考 [MQTT 3.1.1](http://mqtt.org/?spm=5176.doc30540.2.3.BU9nwt) 协议文档。

## 和标准 MQTT 区别
1. 支持 MQTT 的 PUB、SUB、PING、PONG、CONNECT、DISCONNECT、UNSUB 等报文。
2. 支持 cleanSession。
3. 不支持 will、retain msg。
4. 不支持 QOS2。

## MQTT 通道，安全等级
支持 TLSV1, TLSV1.1，TLSV1.2 版本的协议来建立安全连接，安全级别高。

## TOPIC 规范
默认情况下创建产品后，该产品下的所有设备都拥有以下 topic 类的权限：
1. `${productId}/${deviceName}/control` 订阅。
2. `${productId}/${deviceName}/event` 发布。
3. `$shadow/operation/${productId}/${deviceName}` 发布。通过包体内部 type 来区分：update/get，分别对应设备影子文档的更新和拉取等操作。
4. `$shadow/operation/result/${productId}/${deviceName}` 订阅。通过包体内部 type 来区分：update/get/delta，type 为 update/get 分别对应设备影子文档的更新和拉取等操作的结果；当用户通过 restAPI 修改设备影子文档后，服务端将通过该 topic 发布消息，其中 type 为 delta。
    
