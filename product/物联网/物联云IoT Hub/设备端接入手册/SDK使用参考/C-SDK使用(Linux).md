## 编译

请先下载最新版本设备端 C 语言 SDK [SDK下载](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)

解压之后，打开编译配置文件```make.settings```，根据需要编辑配置项

```
BUILD_TYPE                    = release	#release/debug

PLATFORM_CC                   = gcc
PLATFORM_AR                   = ar
PLATFORM_OS                   = linux
PLATFORM_SSL                  = mbedtls

#
# Uncomment below and specify PATH to your toolchain when cross-compile SDK
#
# PLATFORM_CC                 = /home/shock/openwrt/packages/toolchain/mipsel-linux-gcc
# PLATFORM_AR                 = /home/shock/openwrt/packages/toolchain/mipsel-linux-ar
# PLATFORM_CC                 = armcc
# PLATFORM_AR                 = armar

FEATURE_MQTT_COMM_ENABLED     = y    # 是否打开 MQTT 通道的总开关
FEATURE_MQTT_DEVICE_SHADOW    = y    # 是否打开设备影子的总开关
FEATURE_COAP_COMM_ENABLED     = y    # 是否打开 CoAP 通道的总开关
FEATURE_NBIOT_COMM_ENABLED    = y    # 是否打开NBIoT通道的消息组装

FEATURE_OTA_COMM_ENABLED      = y    # 是否打开 OTA 固件升级总开关
FEATURE_OTA_SIGNAL_CHANNEL    = MQTT # OTA 信令通道类型：MQTT/COAP

FEATURE_AUTH_MODE             = CERT # MQTT/CoAP 接入认证方式，使用证书认证：CERT；使用密钥认证：KEY
FEATURE_AUTH_WITH_NOTLS       = n    # 接入认证是否不使用 TLS，证书方式必须选择使用 TLS，密钥认证可选择不使用 TLS

FEATURE_SYSTEM_COMM_ENABLED   = y    # 是否打开获取 IoT 后台时间功能
```
具体含义参考下表:

| 配置选项                       | 含义                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| BUILD_TYPE                    | 编译模式，若是 debug 则开启代码跟踪功能，开启后程序运行过程中函数的调用堆栈将被跟踪并打印         |
| PLATFORM_CC                   | C 源码编译器，使用交叉编译时，请确保 gcc/ar 在同一目录                                      |
| PLATFORM_AR                   | 静态库压缩器，使用交叉编译时，请确保 gcc/ar 在同一目录                                      |
| PLATFORM_OS                   | 指定目标平台的操作系统，SDK 中包含 Linux 版本示例                                          |
| FEATURE_MQTT_COMM_ENABLED     | 是否开启设备 MQTT 功能，默认开启                                                         |
| FEATURE_MQTT_DEVICE_SHADOW    | 是否开启设备影子功能，默认开启                                                            |
| FEATURE_COAP_COMM_ENABLED     | 是否开启设备 CoAP 功能，默认开启                                                          |
| FEATURE_OTA_COMM_ENABLED      | 是否开启设备 OTA 功能，默认开启                                                           |
| FEATURE_OTA_SIGNAL_CHANNEL    | OTA 通道选择 MQTT/COAP，默认 MQTT 通道                                                  |
| FEATURE_AUTH_MODE             | MQTT/CoAP 接入认证方式，使用证书认证：CERT；使用密钥认证：KEY，默认CERT                       |
| FEATURE_AUTH_WITH_NOTLS       | 接入认证是否不使用 TLS，证书方式必须选择使用 TLS，密钥认证可选择不使用 TLS，默认不选择不使用 TLS    |
| FEATURE_SYSTEM_COMM_ENABLED   | 是否打开获取 IoT 后台时间功能，默认开启                                                     |

## 运行
请参考[快速开始](https://cloud.tencent.com/document/product/634/11912)

## C-SDK 提供的功能 API 说明
以下是 V2.1.0 版本 C-SDK 提供的功能和对应 API，用于客户编写业务逻辑，更加详细详细的说明请查看 src/sdk-impl/qcloud_iot_export.h 及 src/sdk-impl/exports/*.h 中的注释

### 1. 日志接口

| 序号 | 函数名                     | 说明                                          |
| ---- | -------------------------- | --------------------------------------------- |
| 1    | IOT_Log_Set_Level          | 设置打印的日志等级                            |
| 2    | IOT_Log_Get_Level          | 返回日志输出的等级                            |
| 3    | IOT_Log_Set_MessageHandler | 设置日志回调函数，接管 SDK 日志用于其它输出方式 |


### 2. MQTT接口

| 序号 | 函数名               | 说明                                            |
| ---- | -------------------- | ----------------------------------------------- |
| 1    | IOT_MQTT_Construct   | 构造 MQTTClient 并完成 MQTT 连接                |
| 2    | IOT_MQTT_Destroy     | 关闭 MQTT 连接并销毁 MQTTClient                 |
| 3    | IOT_MQTT_Yield       | 在当前线程为底层 MQTT 客户端让出一定 CPU 执行时间 |
| 4    | IOT_MQTT_Publish     | 发布 MQTT 消息                                  |
| 5    | IOT_MQTT_Subscribe   | 订阅 MQTT 主题                                  |
| 6    | IOT_MQTT_Unsubscribe | 取消订阅已订阅的 MQTT 主题                      |
| 7    | IOT_MQTT_IsConnected | 客户端目前是否已连接                            |


### 3. 设备影子接口

| 序号  | 函数名                                             | 说明                                            |
| ---- | -------------------------------------------------- | ---------------------------------------------- |
| 1    | IOT_Shadow_Construct                               | 构造 ShadowClient                              |
| 2    | IOT_Shadow_Publish                                 | 发布 MQTT 消息                                  |
| 3    | IOT_Shadow_Subscribe                               | 订阅 MQTT 消息                                  |
| 4    | IOT_Shadow_Unsubscribe                             | 取消订阅 MQTT 消息                               |
| 5    | IOT_Shadow_IsConnected                             | Shadow 客户端目前是否已连接                       |
| 6    | IOT_Shadow_Destroy                                 | 关闭 Shadow 连接并销毁 ShadowClient              |
| 7    | IOT_Shadow_Yield                                   | 在当前线程为底层 Shadow 客户端让出一定 CPU 执行时间  |
| 8    | IOT_Shadow_Update                                  | 异步更新设备影子文档                              |
| 9    | IOT_Shadow_Update_Sync                             | 同步方式更新设备影子文档                           |
| 10   | IOT_Shadow_Get                                     | 异步方式获取设备影子文档                           |
| 11   | IOT_Shadow_Get_Sync                                | 同步方式获取设备影子文档                           |
| 12   | IOT_Shadow_Register_Property                       | 注册当前设备的设备属性                             |
| 13   | IOT_Shadow_UnRegister_Property                     | 删除已经注册过的设备属性                           |
| 14   | IOT_Shadow_JSON_ConstructReport                    | 在JSON文档中添加reported字段，不覆盖更新            | 
| 15   | IOT_Shadow_JSON_Construct_OverwriteReport          | 在JSON文档中添加reported字段，覆盖更新              |
| 16   | IOT_Shadow_JSON_ConstructReportAndDesireAllNull    | 在JSON文档中添加reported字段，同时清空desired字段   |
| 17   | IOT_Shadow_JSON_ConstructDesireAllNull             | 在JSON文档中添加 "desired": null 字段             |


### 4. CoAP 接口

| 序号 | 函数名                       | 说明                                                |
| ---- | ---------------------------- | ------------------------------------------------- |
| 1    | IOT_COAP_Construct           | 构造 CoAPClient 并完成 CoAP 连接                   |
| 2    | IOT_COAP_Destroy             | 关闭 CoAP 连接并销毁 CoAPClient                    |
| 3    | IOT_COAP_Yield               | 在当前线程为底层 COAP 客户端让出一定 CPU 执行时间      |
| 4    | IOT_COAP_SendMessage         | 发布 CoAP 消息                                    |
| 5    | IOT_COAP_GetMessageId        | 获取 COAP Response 消息 msgId                     |
| 6    | IOT_COAP_GetMessagePayload   | 获取 COAP Response 消息内容                        |
| 7    | IOT_COAP_GetMessageCode      | 获取 COAP Response 消息错误码                      |


### 5. OTA 接口

| 序号  | 函数名                        | 说明                                              |
| ---- | ---------------------------- | ------------------------------------------------- |
| 1    | IOT_OTA_Init                 | 初始化 OTA 模块，客户端必须在调用此接口之前进行初始化     |
| 2    | IOT_OTA_Destroy              | 释放 OTA 模块相关的资源                              |
| 3    | IOT_OTA_ReportVersion        | 向 OTA 服务器报告固件版本信息                         |
| 4    | IOT_OTA_ReportUpgradeBegin   | 当进行升级前，需要向 OTA 服务器上报升级开始的状态        |
| 5    | IOT_OTA_ReportUpgradeSuccess | 当升级成功后，需要向 OTA 服务器上报升级成功的状态        |
| 6    | IOT_OTA_ReportUpgradeFail    | 当升级失败后，需要向 OTA 服务器上报升级失败的状态        |
| 7    | IOT_OTA_IsFetching           | 检查是否处于下载固件的状态                            |
| 8    | IOT_OTA_IsFetchFinish        | 检查固件是否已经下载完成                              |
| 9    | IOT_OTA_FetchYield           | 从具有特定超时值的远程服务器获取固件                    |
| 10   | IOT_OTA_Ioctl                | 获取指定的 OTA 信息                                 |
| 11   | IOT_OTA_GetLastError         | 获取最后一个错误代码                                 |


### 6. SYSTEM 接口

| 序号  | 函数名                        | 说明                                              |
| ---- | ---------------------------- | ------------------------------------------------- |
| 1    | IOT_SYSTEM_GET_TIME          | 获取 IoT hub 后台系统时间，目前仅支持 MQTT 通道对时功能 |

### 7. NBIoT 接口

| 序号  | 函数名                        | 说明                                              |
| ---- | ---------------------------- | ------------------------------------------------- |
| 1    | IOT_NB_setMessage          | NBIoT 平台上行消息编码接口 |
| 2    | IOT_NB_getMessage          | NBIoT 平台下行消息解码接口 |