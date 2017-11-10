### 1. 相关下载

根证书下载请点击: [下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/root-ca.zip)
SDK 源码下载请点击: [下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/C-SDK.zip)

### 2. 日志接口

| 序号 | 函数名            | 说明                                                                                                               |
| ---- | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1    | IOT_Log_Set_Level | 设置打印的日志等级|
| 2    | IOT_Log_Get_Level | 返回日志输出的等级                                                                   |


### 3. MQTT接口

| 序号 | 函数名               | 说明                                            |
| ---- | -------------------- | ----------------------------------------------- |
| 1    | IOT_MQTT_Construct   | 构造 MQTTClient 并完成 MQTT 连接                |
| 2    | IOT_MQTT_Destroy     | 关闭 MQTT 连接并销毁 MQTTClient                 |
| 3    | IOT_MQTT_Yield       | 在当前线程为底层 MQTT 客户端让出一定CPU执行时间 |
| 4    | IOT_MQTT_Publish     | 发布 MQTT 消息                                  |
| 5    | IOT_MQTT_Subscribe   | 订阅 MQTT 主题                                  |
| 6    | IOT_MQTT_Unsubscribe | 取消订阅已订阅的 MQTT 主题                      |
| 7    | IOT_MQTT_IsConnected | 客户端目前是否已连接                            |


### 4. 设备影子接口

| 序号 | 函数名                               | 说明                                              |
| ---- | ------------------------------------ | ------------------------------------------------- |
| 1    | IOT_Shadow_Construct                 | 构造 ShadowClient                                 |
| 2    | IOT_Shadow_Destroy                   | 关闭 Shadow 连接并销毁 ShadowClient               |
| 3    | IOT_Shadow_Yield                     | 在当前线程为底层 Shadow 客户端让出一定CPU执行时间 |
| 4    | IOT_Shadow_Update                    | 更新设备影子文档                                  |
| 5    | IOT_Shadow_Get                       | 获取设备影子文档                                  |
| 6    | IOT_Shadow_Delete                    | 删除设备影子文档                                  |
| 7    | IOT_Shadow_Register_Update_Documents | 订阅设备影子文档更新成功的消息                    |
| 8    | IOT_Shadow_Register_Property         | 注册当前设备的设备属性                            |
