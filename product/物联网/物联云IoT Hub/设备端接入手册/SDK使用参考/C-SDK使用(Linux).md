## 编译

请先下载最新版本设备端C语言SDK [SDK下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/release_V1_00_C_20171115.zip)

解压之后，打开编译配置文件`make.settings`，根据需要编辑配置项

```
BUILD_TYPE                  	= release 			#debug

PLATFORM_CC                 	= gcc
PLATFORM_AR                 	= ar
PLATFORM_OS                 	= linux

FEATURE_MQTT_COMM_ENABLED       = y
FEATURE_COAP_COMM_ENABLED   	= y
FEATURE_SDKTESTS_ENABLED        = n
FEATURE_MQTT_RMDUP_MSG_ENABLED  = n
```
具体含义参考下表:

| 配置选项                       | 含义                                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| BUILD_TYPE                     | 编译模式，若是 debug 则开启代码跟踪功能，开启后程序运行过程中函数的调用堆栈将被跟踪并打印 |
| PLATFORM_CC                    | C 源码编译器，使用交叉编译时，请确保 gcc/ar 在同一目录                                    |
| PLATFORM_AR                    | 静态库压缩器，使用交叉编译时，请确保 gcc/ar 在同一目录                                    |
| PLATFORM_OS                    | 指定目标平台的操作系统，SDK 中包含 Linux 版本示例                                         |
| FEATURE_MQTT_COMM_ENABLED      | 是否开启设备 MQTT 功能，默认开启                                                          |
| FEATURE_COAP_COMM_ENABLED      | 是否开启设备 CoAP 功能，默认开启                                                          |
| FEATURE_SDKTESTS_ENABLED       | 是否编译测试代码                                                                          |
| FEATURE_MQTT_RMDUP_MSG_ENABLED | 是否启用 MQTT 消息去重功能                                                                |

## 运行
请参考[快速开始](https://cloud.tencent.com/document/product/634/11912)

## C-SDK提供的功能API说明
以下是 V1.2.0 版本 C-SDK 提供的功能和对应 API，用于客户编写业务逻辑，更加详细详细的说明请查看 src/sdk-impl/qcloud_iot_export.h 及 src/sdk-impl/exports/*.h 中的注释

### 1. 日志接口

| 序号 | 函数名                     | 说明                                          |
| ---- | -------------------------- | --------------------------------------------- |
| 1    | IOT_Log_Set_Level          | 设置打印的日志等级                            |
| 2    | IOT_Log_Get_Level          | 返回日志输出的等级                            |
| 2    | IOT_Log_Set_MessageHandler | 设置日志回调函数，接管SDK日志用于其它输出方式 |


### 2. MQTT接口

| 序号 | 函数名               | 说明                                            |
| ---- | -------------------- | ----------------------------------------------- |
| 1    | IOT_MQTT_Construct   | 构造 MQTTClient 并完成 MQTT 连接                |
| 2    | IOT_MQTT_Destroy     | 关闭 MQTT 连接并销毁 MQTTClient                 |
| 3    | IOT_MQTT_Yield       | 在当前线程为底层 MQTT 客户端让出一定CPU执行时间 |
| 4    | IOT_MQTT_Publish     | 发布 MQTT 消息                                  |
| 5    | IOT_MQTT_Subscribe   | 订阅 MQTT 主题                                  |
| 6    | IOT_MQTT_Unsubscribe | 取消订阅已订阅的 MQTT 主题                      |
| 7    | IOT_MQTT_IsConnected | 客户端目前是否已连接                            |


### 3. 设备影子接口

| 序号 | 函数名                         | 说明                                                |
| ---- | ------------------------------ | --------------------------------------------------- |
| 1    | IOT_Shadow_Construct           | 构造 ShadowClient                                   |
| 2    | IOT_Shadow_Destroy             | 关闭 Shadow 连接并销毁 ShadowClient                 |
| 3    | IOT_Shadow_Yield               | 在当前线程为底层 Shadow 客户端让出一定 CPU 执行时间 |
| 4    | IOT_Shadow_Update              | 异步更新设备影子文档                                |
| 5    | IOT_Shadow_Update_Sync         | 同步方式更新设备影子文档                            |
| 6    | IOT_Shadow_Get                 | 异步方式获取设备影子文档                            |
| 7    | IOT_Shadow_Get_Sync            | 同步方式获取设备影子文档                            |
| 8    | IOT_Shadow_Register_Property   | 注册当前设备的设备属性                              |
| 9    | IOT_Shadow_UnRegister_Property | 删除已经注册过的设备属性                            |


### 4. CoAP 接口

| 序号 | 函数名                     | 说明                                              |
| ---- | -------------------------- | ------------------------------------------------- |
| 1    | IOT_COAP_Construct         | 构造 CoAPClient 并完成 CoAP 连接                  |
| 2    | IOT_COAP_Destroy           | 关闭 CoAP 连接并销毁 CoAPClient                   |
| 3    | IOT_COAP_Yield             | 在当前线程为底层 COAP 客户端让出一定 CPU 执行时间 |
| 4    | IOT_COAP_SendMessage       | 发布 CoAP 消息                                    |
| 5    | IOT_COAP_GetMessageId      | 获取 COAP Response 消息 msgId                     |
| 6    | IOT_COAP_GetMessagePayload | 获取 COAP Response 消息内容                       |
| 7    | IOT_COAP_GetMessageCode    | 获取 COAP Response 消息错误码                     |
