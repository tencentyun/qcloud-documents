
在 Linux 环境下快速体验利用设备端 C-SDK 接入腾讯云物联网平台服务。

## 编译选项说明
1. 请先 [下载](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases) 最新版本设备端 C 语言 SDK 。
2. 在 Linux 开发环境下解压 C-SDK 代码包之后，打开编译配置文件`make.settings`，根据实际需要编辑配置项。
以下是 SDK v3.0.1 版本的 make.setting 编译选项说明：

| 配置选项                       | 含义                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| BUILD_TYPE                    | 编译模式，若是 debug 则开启代码跟踪功能，开启后程序运行过程中函数的调用堆栈将被跟踪并打印         |
| PLATFORM_CC                   | C 源码编译器，使用交叉编译时，请确保 gcc/ar 在同一目录                       |
| PLATFORM_AR                   | 静态库压缩器，使用交叉编译时，请确保 gcc/ar 在同一目录                            |
| PLATFORM_OS                   | 指定目标平台的操作系统，SDK 中包含 Linux 版本示例                                   |
| PLATFORM_SSL                  | 指定目标平台的 SSL/TLS 库，SDK 中包含 mbedTLS 版本示例                    |
| FEATURE_MQTT_COMM_ENABLED     | 是否开启设备 MQTT 功能，默认开启                                 |
| FEATURE_MQTT_DEVICE_SHADOW    | 是否开启设备影子功能，默认开启                                       |
| FEATURE_COAP_COMM_ENABLED     | 是否开启设备 CoAP 功能，默认开启                                     |
| FEATURE_NBIOT_COMM_ENABLED    | 是否开启设备 NBIoT 消息组装功能，默认开启              |
| FEATURE_GATEWAY_ENABLED       | 是否开启设备 MQTT 网关功能，默认关闭                                 |
| FEATURE_OTA_COMM_ENABLED      | 是否开启设备 OTA 功能，默认开启                            |
| FEATURE_OTA_SIGNAL_CHANNEL    | OTA 通道选择 MQTT/COAP，默认 MQTT 通道                  |
| FEATURE_AUTH_MODE             | MQTT/CoAP 接入认证方式，使用证书认证：CERT；使用密钥认证：KEY，默认 KEY                  |
| FEATURE_AUTH_WITH_NOTLS       | 接入认证是否不使用 TLS 加密，证书方式必须选择使用 TLS，密钥认证可选择不使用 TLS，默认选择使用 TLS    |
| FEATURE_DEV_DYN_REG_ENABLED   | 是否打开设备动态注册功能，默认开启    |                                                
| FEATURE_LOG_UPLOAD_ENABLED    | 是否打开运行日志上报云端功能，默认开启  |                                                 
| FEATURE_EVENT_POST_ENABLED    | 是否打开事件上报功能，默认开启            |
| FEATURE_SYSTEM_COMM_ENABLED   | 是否打开获取 IoT 后台时间功能，默认开启    |                                                
| FEATURE_MULTITHREAD_TEST_ENABLED   | 是否编译 Linux 多线程测试例程，默认关闭  |                                                   

## 可变参数配置
C-SDK 的使用可以根据具体场景需求，配置相应的参数，满足实际业务的运行。可变接入参数包括 MQTT 心跳消息发送周期， MQTT 阻塞调用(包括连接, 订阅, 发布等)的超时时间，TLS 连接握手超时时间，MQTT/CoAP 协议发送消息和接受消息的缓冲区大小等等参数。具体可参考SDK docs目录下产品使用文档的可变接入参数配置部分

## 编译及运行
快速体验可以参考 SDK docs 目录下物联网通信平台使用文档的编译示例程序部分，在云端控制台创建设备和设置权限之后，按照步骤进行 sample 代码的修改，编译及运行，即可以在 Linux 环境下进行一个简单虚拟设备的连接以及消息收发测试。
如下面运行示例日志输出：
```
INF|2019-06-21 21:41:55|device.c|iot_device_info_set(65): SDK_Ver: 3.0.1, Product_ID: S3EUVBRJLB, Device_Name: test_dev_key
DBG|2019-06-21 21:41:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(204): Connecting to /S3EUVBRJLB.iotcloud.tencentdevices.com/8883...
DBG|2019-06-21 21:41:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(209): Setting up the SSL/TLS structure...
DBG|2019-06-21 21:41:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(251): Performing the SSL/TLS handshake...
INF|2019-06-21 21:41:55|HAL_TLS_mbedtls.c|HAL_TLS_Connect(269): connected with /S3EUVBRJLB.iotcloud.tencentdevices.com/8883...
INF|2019-06-21 21:41:55|mqtt_client.c|IOT_MQTT_Construct(114): mqtt connect with id: 8674N success
INF|2019-06-21 21:41:55|mqtt_sample.c|main(397): Cloud Device Construct Success
DBG|2019-06-21 21:41:55|mqtt_client_subscribe.c|qcloud_iot_mqtt_subscribe(139): topicName=S3EUVBRJLB/test_dev_key/data|packet_id=29284
INF|2019-06-21 21:41:55|mqtt_sample.c|event_handler(92): subscribe success, packet-id=29284
DBG|2019-06-21 21:41:56|mqtt_client_publish.c|qcloud_iot_mqtt_publish(337): publish packetID=0|topicName=S3EUVBRJLB/test_dev_key/data|payload={"action": "publish_test", "count": "0"}
INF|2019-06-21 21:41:56|mqtt_sample.c|on_message_callback(149): Receive Message With topicName:S3EUVBRJLB/test_dev_key/data, payload:{"action": "publish_test", "count": "0"}
INF|2019-06-21 21:41:56|mqtt_client_connect.c|qcloud_iot_mqtt_disconnect(443): mqtt disconnect!
INF|2019-06-21 21:41:56|mqtt_client.c|IOT_MQTT_Destroy(172): mqtt release!
```
进一步的使用请参考 [快速开始](https://cloud.tencent.com/document/product/634/11912)，构建一个简单的智能家居设备互联互通的场景。

## C-SDK API 说明
以下是 C-SDK v3.0.1版本提供的主要功能和对应 API 接口说明，用于客户编写业务逻辑，更加详细的说明如接口参数及返回值可查看 SDK 代码 qcloud_iot_export.h 及 exports/qcloud_iot_export_*.h 等头文件中的注释。

### MQTT 接口

| 函数名               | 说明                                            |
| -------------------- | ----------------------------------------------- |
| IOT_MQTT_Construct   | 构造 MQTTClient 并连接 MQTT 云端服务                |
| IOT_MQTT_Destroy     | 关闭 MQTT 连接并销毁 MQTTClient                 |
| IOT_MQTT_Yield       | 在当前线程上下文中，进行 MQTT 报文读取，消息处理，超时请求，心跳包及重连状态管理等任务 |
| IOT_MQTT_Publish     | 发布 MQTT 消息                                  |
| IOT_MQTT_Subscribe   | 订阅 MQTT 主题                                  |
| IOT_MQTT_Unsubscribe | 取消订阅已订阅的 MQTT 主题                      |
| IOT_MQTT_IsConnected | 查看当前 MQTT 是否已连接                            |

### 设备影子接口
关于设备影子功能介绍，请参考 [设备影子详情](https://cloud.tencent.com/document/product/634/11918)。

| 函数名                                             | 说明                                            |
| -------------------------------------------------- | ---------------------------------------------- |
| IOT_Shadow_Construct                               | 构造设备影子客户端 ShadowClient，并连接 MQTT 云端服务         |
| IOT_Shadow_Publish                                 | 影子客户端发布 MQTT 消息                                  |
| IOT_Shadow_Subscribe                               | 影子客户端订阅 MQTT 主题                                  |
| IOT_Shadow_Unsubscribe                             | 影子客户端取消订阅已订阅的 MQTT 主题                         |
| IOT_Shadow_IsConnected                             | 查看当前影子客户端的 MQTT 是否已连接                       |
| IOT_Shadow_Destroy                                 | 关闭 Shadow MQTT 连接并销毁 ShadowClient              |
| IOT_Shadow_Yield                                   | 在当前线程上下文中，进行 MQTT 报文读取，消息处理，超时请求，心跳包及重连状态管理等任务  |
| IOT_Shadow_Update                                  | 异步更新设备影子文档                              |
| IOT_Shadow_Update_Sync                             | 同步方式更新设备影子文档                           |
| IOT_Shadow_Get                                     | 异步方式获取设备影子文档                           |
| IOT_Shadow_Get_Sync                                | 同步方式获取设备影子文档                           |
| IOT_Shadow_Register_Property                       | 注册当前设备的设备属性                             |
| IOT_Shadow_UnRegister_Property                     | 删除已经注册过的设备属性                           |
| IOT_Shadow_JSON_ConstructReport                    | 在 JSON 文档中添加 reported 字段，不覆盖更新            | 
| IOT_Shadow_JSON_Construct_OverwriteReport          | 在 JSON 文档中添加 reported 字段，覆盖更新              |
| IOT_Shadow_JSON_ConstructReportAndDesireAllNull    | 在 JSON 文档中添加 reported 字段，同时清空 desired 字段|   
| IOT_Shadow_JSON_ConstructDesireAllNull             | 在 JSON 文档中添加 "desired": null 字段             |

### CoAP 接口

| 函数名                       | 说明                                                |
| ---------------------------- | ------------------------------------------------- |
| IOT_COAP_Construct           | 构造 CoAPClient 并完成 CoAP 连接                   |
| IOT_COAP_Destroy             | 关闭 CoAP 连接并销毁 CoAPClient                    |
| IOT_COAP_Yield               | 在当前线程上下文中，进行 CoAP 报文读取和消息处理等任务      |
| IOT_COAP_SendMessage         | 发布 CoAP 消息                                    |
| IOT_COAP_GetMessageId        | 获取 COAP Response 消息 msgId                     |
| IOT_COAP_GetMessagePayload   | 获取 COAP Response 消息内容                        |
| IOT_COAP_GetMessageCode      | 获取 COAP Response 消息错误码                      |

### OTA 接口
关于 OTA 固件下载功能介绍，可以参考 [设备固件升级](https://cloud.tencent.com/document/product/634/14674)

| 函数名                        | 说明                                              |
| ---------------------------- | ------------------------------------------------- |
| IOT_OTA_Init                 | 初始化 OTA 模块，客户端在调用此接口之前需要先进行 MQTT/COAP 的初始化     |
| IOT_OTA_Destroy              | 释放 OTA 模块相关的资源                              |
| IOT_OTA_ReportVersion        | 向 OTA 服务器报告固件版本信息                         |
| IOT_OTA_IsFetching           | 检查是否处于下载固件的状态                            |
| IOT_OTA_IsFetchFinish        | 检查固件是否已经下载完成                              |
| IOT_OTA_FetchYield           | 从具有特定超时值的远程服务器获取固件                    |
| IOT_OTA_Ioctl                | 获取指定的 OTA 信息                                 |
| IOT_OTA_GetLastError         | 获取最后一个错误代码                                 |

### 日志接口
设备日志上报云端功能的详细说明可以参考SDK docs目录下物联网通信平台文档设备日志上报功能部分

| 函数名                     | 说明                                          |
| -------------------------- | --------------------------------------------- |
| IOT_Log_Set_Level          | 设置 SDK 日志的打印等级                            |
| IOT_Log_Get_Level          | 返回 SDK 日志打印的等级                            |
| IOT_Log_Set_MessageHandler | 设置日志回调函数，重定向 SDK 日志于其它输出方式  |
| IOT_Log_Init_Uploader      | 开启 SDK 日志上报云端的功能并初始化资源                |
| IOT_Log_Fini_Uploader      | 停止 SDK 日志上报云端功能并释放资源                      |
| IOT_Log_Upload             | 将 SDK 运行日志上报到云端                         |
| IOT_Log_Set_Upload_Level   | 设置 SDK 日志的上报等级                            |
| IOT_Log_Get_Upload_Level   | 返回 SDK 日志上报的等级                            |
| Log_d/i/w/e                | 按级别打印添加 SDK 日志的接口                         |

### SYSTEM 接口

| 函数名                        | 说明                                              |
| ---------------------------- | ------------------------------------------------- |
| IOT_SYSTEM_GET_TIME          | 获取 IoT hub 后台系统时间，目前仅支持 MQTT 通道对时功能 |

### NBIoT 接口

| 函数名                        | 说明                                              |
| ---------------------------- | ------------------------------------------------- |
| IOT_NB_setMessage          | NBIoT 平台上行消息编码接口 |
| IOT_NB_getMessage          | NBIoT 平台下行消息解码接口 |

### 网关功能接口
关于网关功能介绍，可以参考 SDK docs 目录下物联网通信平台文档网关产品部分。

| 函数名                       | 说明                                                |
| ---------------------------- | ------------------------------------------------- |
| IOT_Gateway_Construct        | 构造 Gateway client 并完成 MQTT 连接                   |
| IOT_Gateway_Destroy          | 关闭 MQTT 连接并销毁 Gateway client                    |
| IOT_Gateway_Subdev_Online    | 子设备上线              |
| IOT_Gateway_Subdev_Offline   | 子设备下线                                    |
| IOT_Gateway_Yield            | 在当前线程上下文中，进行 MQTT 报文读取，消息处理，超时请求，心跳包及重连状态管理等任务 |
| IOT_Gateway_Publish          | 发布 MQTT 消息                                  |
| IOT_Gateway_Subscribe        | 订阅 MQTT 主题                                  |
| IOT_Gateway_Unsubscribe      | 取消订阅已订阅的 MQTT 主题                      |



关于设备端 SDK 使用的常见问题，请参考 [设备接入和上报问题](https://cloud.tencent.com/document/product/634/19450)。
