## 编译
请先下载根证书 [根证书下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/root-ca.zip)

请先下载最新版本设备端C语言SDK [SDK下载](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/release_V1_00_C_20171115.zip)

解压之后，打开编译配置文件```config.mk```，根据需要编辑配置项

```
DEBUG				 = y

PLATFORM             = linux
PLATFORM_CC          = gcc
PLATFORM_AR          = ar

TLS_LIB              = mbedtls

ENABLE_SHADOW        = y
ENABLE_TRACE         = n

IOT_SDK_LIB_NAME     = libiotsdk
```
具体含义参考下表:

| 配置选项 					                          | 含义                                           |
| ---------------------------------------------- | ---------------------------------------------  |
| PLATFORM                                       | 指定目标平台的操作系统，SDK中包含Linux版本示例|
| PLATFORM_CC                                    | C源码编译器，使用交叉编译时，请确保gcc/ar 在同一目录|
| PLATFORM_AR                                    | 静态库压缩器，使用交叉编译时，请确保gcc/ar 在同一目录|
| TLS_LIB                                        | TLS库，SDK提供mbedtls作为默认TLS库|
| ENABLE_SHADOW                                  | 是否开启设备影子功能 |
| ENABLE_TRACE                                   | 是否开启代码跟踪功能，开启后程序运行过程中函数的调用堆栈将被跟踪并打印 |

## 运行
请参考[快速开始](https://cloud.tencent.com/document/product/634/11912)

## C-SDK提供的功能API说明
以下是V1.0.0版本C-SDK提供的功能和对应API，用于客户编写业务逻辑，更加详细详细的说明请查看src/sdk-impl/qcloud_iot_export.h及src/sdk-impl/exports/*.h中的注释

### 1. 日志接口

| 序号 | 函数名            | 说明                                                                                                               |
| ---- | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1    | IOT_Log_Set_Level | 设置打印的日志等级|
| 2    | IOT_Log_Get_Level | 返回日志输出的等级|
| 2    | IOT_Log_Set_MessageHandler | 设置日志回调函数，接管SDK日志用于其它输出方式|


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
