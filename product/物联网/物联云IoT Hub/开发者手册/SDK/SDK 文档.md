### 1. 相关下载

根证书: [下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/root-ca.zip)
SDK源码: [下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/C-SDK.zip)

### 2. 日志接口

| 序号  | 函数名                     	 | 说明                                                                   |
|-------|-----------------------------|-----------------------------------------------------------------------|
|     1 | qcloud_iot_set_log_level   | 设置打印的日志等级，接受一个枚举`LOG_LEVEL`的入参，枚举包括`ERROR`、`WARN`、`INFO`、`DEBUG`， 打印详细度依次增加。|
|     2 | qcloud_iot_get_log_level  | 返回日志输出的等级`LOG_LEVEL`。|


### 3. MQTT接口

| 序号  | 函数名                  		           | 说明                                                                    |
|-------|---------------------------------------|-------------------------------------------------------------------------|
|     1 | qcloud_iot_mqtt_init   		        | MQTT 实例构造函数，入参为`MQTTInitParams`结构体和`Client`实例指针。 |
|     2 | qcloud_iot_mqtt_connect  	        | 建立基于 MQTT 连接，入参为`ConnectParams`结构体和`Client`实例指针。  |
|     3 | qcloud_iot_mqtt_publish   	        | 组织一个完整的`MQTT Publish`报文并向服务端发布报文。|
|     4 | qcloud_iot_mqtt_subscribe           | 组织一个完整的`MQTT Subscribe`报文并向服务端发送订阅请求。|
|     5 | qcloud_iot_mqtt_resubscribe         | MQTT 客户端重新订阅断开连接之前已订阅的主题。 |
|     6 | qcloud_iot_mqtt_unsubscribe         | 组织一个完整的`MQTT UnSubscribe`报文并向服务端发送取消订阅请求。 |
|     7 | qcloud_iot_mqtt_disconnect          | 断开 MQTT 客户端与服务器的连接。|
|     8 | qcloud_iot_mqtt_yield               | 在当前线程为底层 MQTT 客户端让出一定 CPU 执行时间，内含了心跳的维持，服务器下行报文的收取等。 |
|     9 | qcloud_iot_mqtt_attempt_reconnect   | MQTT 客户端与服务器重新建立连接。 |
|    10 | qcloud_iot_mqtt_is_connected       | 判断 MQTT 客户端目前是否已连接，返回真则客户端在连接状态，反之客户端已经断开连接。|

### 4. 设备影子接口

| 序号  | 函数名                   	                  | 说明                                               |
|-------|---------------------------------------------|----------------------------------------------------|
|     1 | qcloud_iot_shadow_init   	              | MQTT 实例构造函数，入参为`MQTTInitParams`结构体和`Client`实例指针。|
|     2 | qcloud_iot_shadow_connect  	              | 建立基于 MQTT 连接，入参为`ShadowConnectParams`结构体和`Client`实例指针。  |
|     3 | qcloud_iot_shadow_yield   	              | 在当前线程为底层 MQTT 客户端让出一定 CPU 执行时间，内含了心跳的维持，服务器下行报文的收取等。  |
|     4 | qcloud_iot_shadow_disconnect              | 断开 MQTT 连接。|
|     5 | qcloud_iot_shadow_get   	                 | 把服务器端被缓存的 JSON 数据下拉到本地, 更新本地的数据属性。  |
|     6 | qcloud_iot_shadow_delete   	              | 客户发向服务端发送请求，删除服务器端的缓存数据。  |
|     7 | qcloud_iot_shadow_update   	              | 把本地的数据属性上推到服务器缓存的 JSON 数据, 更新服务端的数据属性。 |
|     8 | qcloud_iot_shadow_register_update_documents| 监听本地推动数据到服务端的请求结果。 |
|     9 | qcloud_iot_shadow_register_property        | 创建一个数据类型注册到服务端。 |
|    10 | qcloud_iot_shadow_reset_document_version   | 重置本地设备文档版本号。                     |
|    11 | qcloud_iot_shadow_get_document_version     | 获取本地设备文档版本号 。                   |
