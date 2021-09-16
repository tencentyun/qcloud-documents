对于不具备网络通讯能力的 MCU，一般采用 MCU+ 通讯模组的方式，通讯模组（包括 Wi-Fi/2G/4G/NB-IoT）一般提供了基于串口的 AT 指令协议供 MCU 进行网络通讯。针对这种场景，C-SDK 封装了 AT-socket 网络层，网络层之上的核心协议和服务层无须移植。本文阐述针对 MCU（FreeRTOS）+通用 TCP AT 模组的目标环境，如何移植 C-SDK 并接入腾讯云物联网平台。

## SDK 下载
下载最新版本设备端 [C-SDK](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c)。

##  SDK 功能配置
使用通用 TCP 模组编译配置选项配置如下：

| 名称                             | 配置        | 说明                                                         |
| :------------------------------- | ------------- | ------------------------------------------------------------ |
| BUILD_TYPE                       | debug/release| 根据需要设置  |
| EXTRACT_SRC                      | ON       | 使能代码抽取                                               |
| COMPILE_TOOLS                    | gcc/MSVC      | 根据需要设置，IDE 情况不关注            |
| PLATFORM                         | Linux/Windows | 根据需要设置，IDE 情况不关注                |
| FEATURE_OTA_COMM_ENABLED         | ON/OFF       | 根据需要设置                     |
| FEATURE_AUTH_MODE                | KEY      | 资源受限设备认证方式建议选密钥认证    |
| FEATURE_AUTH_WITH_NOTLS          | ON/OFF        | 根据需要是否使能 TLS             |
| FEATURE_EVENT_POST_ENABLED       | ON/OFF        | 根据需要是否使能事件上报    |
| FEATURE_AT_TCP_ENABLED           | ON        | AT 模组 TCP 功能开关                        |
| FEATURE_AT_UART_RECV_IRQ         | ON        | AT 模组中断接受功能开关                |
| FEATURE_AT_OS_USED               | ON        | AT 模组多线程功能开关                         |
| FEATURE_AT_DEBUG              | OFF      | 默认关闭 AT 模组调试功能，有调试需要再打开|

## 代码抽取
1. 在 Linux 环境运行以下命令：
```
mkdir build
cd build
cmake ..
```
2. 即可在 output/qcloud_iot_c_sdk 中，找到相关代码文件，目录层次如下：
```
 qcloud_iot_c_sdk
 ├── include
 │   ├── config.h
 │   ├── exports
 ├── platform
 └── sdk_src
     └── internal_inc
```
>?
 - include 目录：SDK 供用户使用的 API 及可变参数，其中 config.h 为根据编译选项生成的编译。
 - platform 目录：平台相关的代码，可根据设备的具体情况进行修改适配。
 - sdk_src ：SDK 的核心逻辑及协议相关代码，一般不需要修改，其中 internal_inc 为 SDK 内部使用的头文件。
3. 用户可将 qcloud_iot_c_sdk 拷贝到其目标平台的编译开发环境，并根据具体情况修改编译选项。

##  HAL 层移植

请先参考 [C-SDK_Porting 跨平台移植概述](https://cloud.tencent.com/document/product/634/38388) 进行移植。
对于网络相关的 HAL 接口，通过上面的编译选项已选择 SDK 提供的 `AT_Socket` 框架，SDK 会调用 `network_at_tcp.c` 的 `at_socket` 接口，`at_socket` 层不需要移植，需要实现 AT 串口驱动及AT模组驱动，AT模组驱动只需要实现 AT 框架中`at_device`的驱动结构体 `at_device_op_t`的驱动接口即可，可以参照`at_device`目录下的已支持的模组。
目前 SDK 针对物联网使用较广的 Wi-Fi 模组 ESP8266 提供了底层接口实现，供移植到其他通讯模组时作为参考。

## 业务逻辑开发

您可参考 SDK samples 目录下的例程进行开发。


