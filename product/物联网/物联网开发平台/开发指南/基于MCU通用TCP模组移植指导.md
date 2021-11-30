## 简介

IOT 设备从联网的方式来看大的情形分为两种，一种是 MCU+模组的形式，一种是 SOC 的方式。对于前者网络协议栈在模组中实现，对于后者网络协议栈在系统侧实现。对于模组又有两种大的情形，一种是模组提供通用的 TCP/UDP 通信的 AT 指令，MCU 侧基于 AT 指令的封装实现 TCP 应用层的读写接口。另一种是将物联网平台的 SDK 封装在模组中，对外暴露 MQTT 协议或者其他的协议指令，MCU 侧不用感知 TCP/UDP 的存在，直接进行基于封装的 AT 指令进行 MQTT 应用层的协议开发。

本文阐述 MCU+通用 TCP 模组如何移植腾讯 IoT Explorer C-SDK。MCU+定制 MQTT 模组移植，请参阅 [移植指导](https://cloud.tencent.com/document/product/1081/34719)。

## 操作步骤

### 移植操作

**1. 下载最新版本设备端 [C-SDK](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)**
**2. 代码放置**
将 C-SDK 整个代码目录作为通信组件放在类似 RTOS、FATFS 的第三方组件的同级目录，系统代码框架大体如下：
![](https://main.qcloudimg.com/raw/0abd92705ca57141da4314004fa8cca1.jpg)
**3. HAL 层移植**
SDK 移植到具体平台硬件，需要做的移植工作是实现工程目录`/qcloud-iot-sdk-embedded-c/src/platform/OS`下的平台相关的 HAL 层接口。HAL 层主要是网络适配（TCP/UDP连接、读、写）、OS 适配（锁、内存申请释放随机数、延时、打印）、Timer 适配（时间戳、ms 数获取）。如下：

**必须实现：**

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_Free               | 释放内存块。                               |
| 2    | HAL_Malloc             | 分配一块的内存，返回一个指向块开始的指针。 |
| 3    | HAL_Printf             | 将格式化的数据写入标准输出流中。           |
| 4    | HAL_Snprintf           | 将格式化的数据写入字符串。                 |
| 5    | HAL_UptimeMs           | 检索自系统启动以来已运行的毫秒数。         |
| 6    | HAL_SleepMs            | 休眠。                                     |
| 7    | HAL_Timer_init         | 初始化定时器结构体。                       |
| 8    | HAL_Timer_remain       | 检查给定定时器还剩余时间。                 |
| 9    | HAL_Timer_expired      | 判断定时器时间是否已经过期。               |
| 10   | HAL_Timer_countdown    | 根据定时器开始计时，单位：s                |
| 11   | HAL_Timer_countdown_ms | 根据定时器开始计时，单位：ms               |
| 12   | HAL_Timer_current      | 获取当前时间格式化字符串 。                |
| 13   | HAL_TLS_Connect        | 为 MQTT 客户端建立 TLS 连接，              |
| 14   | HAL_TLS_Disconnect     | 断开 TLS 连接。                            |
| 15   | HAL_TLS_Write          | 从一个 TLS 连接中写数据。                  |
| 16   | HAL_TLS_Read           | 从一个 TLS 连接中读数据。                  |
| 17   | HAL_MutexCreate        | 创建 mutex。                               |
| 18   | HAL_MutexDestroy       | 销毁 mutex。                               |
| 19   | HAL_MutexLock          | mutex 加锁。                               |
| 20   | HAL_MutexUnlock        | mutex 解锁。                               |

**仅在使用 CoAP 必须实现：**

| 序号 | 函数名              | 说明                                                     |
| ---- | ------------------- | -------------------------------------------------------- |
| 1    | HAL_DTLS_Connect    | 为 CoAP 客户端建立 DTLS 连接，仅在需要使用 CoAP 时实现。 |
| 2    | HAL_DTLS_Disconnect | 断开 DTLS 连接。                                         |
| 3    | HAL_DTLS_Write      | 从一个 DTLS 连接中写数据。                               |
| 4    | HAL_DTLS_Read       | 从一个 DTLS 连接中读数据。                               |

基于模组的 TCP AT 指令如何实现网络读写的 HAL 层适配，请参考 [示例工程STM32+BC26](https://github.com/tencentyun/qcloud-iot-sdk-for-stm32withfreeRTOS-example.git) 移植实现。参考示例头文件at_for_bc206.h 相关接口的适配实现，注意处理好各接口返回值。对于 TLS/DTLS，一般使用 mbedTLS 库，需要解决 mbedTSL 的移植依赖，SDK 调用的是 SSL_TLS 层的标准 API。移植好的示例工程目录结构如下：
![](https://main.qcloudimg.com/raw/2189a594ccc658e1b6f4ffc432565f00.png)

### 设备创建、配置、鉴权及通信

**1. 设备创建**
 设备完成 SDK 移植后，下一步即是接入腾讯云平台。
1.1 登录 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer) ，并 [创建产品](https://cloud.tencent.com/document/product/1081/34739)。
1.2 [创建设备](https://cloud.tencent.com/document/product/1081/34740)。

**2. 设备侧设备信息配置**
设备创建完毕后，[查看设备信息](https://cloud.tencent.com/document/product/1081/34741#.E6.9F.A5.E7.9C.8B.E8.AE.BE.E5.A4.87.E4.BF.A1.E6.81.AF)，根据认证方式，将设备信息赋给示例程序的相应宏，量产产品，需要实现这些信息的生产写入及运行过程的获取，建议对这些信息写入与读取进行加密加扰增加产品安全性。

```
#ifdef AUTH_MODE_CERT
	/* 产品名称, 与云端同步设备状态时需要  */
	#define QCLOUD_IOT_MY_PRODUCT_ID            "YOUR_PRODUCT_ID"
	/* 设备名称, 与云端同步设备状态时需要 */
	#define QCLOUD_IOT_MY_DEVICE_NAME           "YOUR_DEVICE_NAME"
    /* 客户端证书文件名  非对称加密使用*/
    #define QCLOUD_IOT_CERT_FILENAME            "YOUR_DEVICE_NAME_cert.crt"
    /* 客户端私钥文件名 非对称加密使用*/
    #define QCLOUD_IOT_KEY_FILENAME             "YOUR_DEVICE_NAME_private.key"

    static char sg_cert_file[PATH_MAX + 1];      //客户端证书全路径
    static char sg_key_file[PATH_MAX + 1];       //客户端密钥全路径

#else
	/* 产品名称, 与云端同步设备状态时需要  */
	#define QCLOUD_IOT_MY_PRODUCT_ID            "YOUR_PRODUCT_ID"
	/* 设备名称, 与云端同步设备状态时需要 */
	#define QCLOUD_IOT_MY_DEVICE_NAME           "YOUR_DEVICE_NAME"
	#define QCLOUD_IOT_DEVICE_SECRET            "YOUR_IOT_PSK"
#endif
```

**3. 设备和平台通信**
C-SDK 同时支持腾讯云现有的两个物联网平台 [物联网通信](https://console.cloud.tencent.com/iotcloud/products) 和 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer)。
物联网开发平台是基于物联网通信平台的底层能力，物联网通信平台实现了 Coap、Mqtt、Ota、Shadow、GateWay、Nbiot 等底层数据通信能力，物联网开发平台则是基于开发者的角度对数据的进一步抽象封装，形成 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916)，开发者基于物联网开发平台的数据模板可以实现产品的快速开发。

- 物联网通信平台示例：
基础示例 Coap、Mqtt、Ota、Shadow、GateWay、Nbiot 及 scenarized 目录下的 [空调](https://cloud.tencent.com/document/product/634/11914) 和 [门控](https://cloud.tencent.com/document/product/634/11913) 的场景示例。各示例的数据流，参阅 [功能组件](https://cloud.tencent.com/document/product/634/11915) ，其中 [示例工程 STM32+BC26](https://github.com/tencentyun/qcloud-iot-sdk-for-stm32withfreeRTOS-example) exhibitor_shadow_sample.c 是嵌入式平台已经移植好的示例，这个示例对应的硬件是腾讯云+峰会的参会证，原理图在 doc 目录，其他示例可以参考修改移植。开发者可以基于设备的具体应用场景参考最接近的示例开发。

- 物联网开发平台示例：
基础示例 data_template、event 及 scenarized 目录下的 [智能灯](https://cloud.tencent.com/document/product/1081/34744)。

**4. 查看云日志**

设备和云端的交互日志可以在控制台的云日志功能查看，可以看到设备的上下线信息、pulish 的消息属性、规则引擎转发情况等。物联网开发平台的调试日志查看，请参阅 [设备调试]( https://cloud.tencent.com/document/product/1081/34741#.E6.9F.A5.E7.9C.8B.E8.AE.BE.E5.A4.87.E4.BF.A1.E6.81.AF) 文档。



