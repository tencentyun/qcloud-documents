## 概述

本文档介绍如何将设备端 C-SDK 移植到目标硬件平台。C-SDK 采用模块化设计，分离核心协议服务与硬件抽象层，在进行跨平台移植时，一般只需对硬件抽象层进行修改适配即可。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C-SDK](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c)。

## 接入指引

非典型平台接入腾讯云物联网开发平台可以分为以下3个步骤：

1. 硬件抽象层移植
2. 应用开发

### 硬件抽象层移植

HAL 层主要有几大块的移植，分别是 OS 相关、网络及 TLS 相关、时间及打印相关、设备信息相关。
SDK 在 **platform/os** 目录示例了 Linux、Windows、FreeRTOS 及 nonOS 四个场景的硬件抽象层实现，可以参考最相近的目录展开目标平台的移植。

#### 1. OS 相关接口

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_Malloc             | 动态申请内存块     |
| 2    | HAL_Free               | 释放内存块                              |
| 3   | HAL_ThreadCreate        | 线程创建                                |
| 4   | HAL_ThreadDestroy        | 线程销毁                               |
| 5   | HAL_MutexCreate        | 创建互斥锁                               |
| 6   | HAL_MutexDestroy       | 销毁互斥锁                               |
| 7   | HAL_MutexLock          | mutex 加锁                               |
| 8   | HAL_MutexUnlock        | mutex 解锁                               |
| 9   | HAL_SemaphoreCreate        | 创建信号量                               |
| 10   | HAL_SemaphoreDestroy        | 销毁信号量                               |
| 11   | HAL_SemaphoreWait        | 等待信号量                               |
| 12   | HAL_SemaphorePost        | 释放信号量                               |
| 13    | HAL_SleepMs            | 休眠                                     |

#### 2. 网络及 TLS 相关的 HAL 接口

网络相关接口提供二选一的适配移植。对于具备网络通讯能力并且本身集成 TCP/IP 网络协议栈的设备，需要实现 POSIX_socket 的网络 HAL 接口，使用 TLS/SSL 加密通讯的还需要实现 TLS 相关的 HAL 接口。而对于 **MCU+ 通用 TCP_AT 模组** 的设备，则可以选择 SDK 提供的 AT_Socket 框架，并实现相关的 AT 模组接口。

**基于 POSIX_socket 的 HAL 接口**

其中 TCP/UDP 相关接口基于 POSIX socket 函数实现。TLS 相关接口依赖于 **mbedtls** 库，移植之前必须确保系统上有可用的 **mbedtls** 库。如果采用其他 TLS/SSL 库，可参考 **platform/tls/mbedtls** 相关实现进行移植适配。
UDP/DTLS 相关的函数仅在使能 **COAP** 通讯的时候才需要移植。

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_TCP_Connect               | 建立 TCP 连接                              |
| 2    | HAL_TCP_Disconnect             | 断开 TCP 连接 |
| 3   | HAL_TCP_Write        | TCP 写                                |
| 4   | HAL_TCP_Read        | TCP 读                               |
| 5   | HAL_TLS_Connect        | 建立 TLS 连接              |
| 6   | HAL_TLS_Disconnect     | 断开 TLS 连接                            |
| 7   | HAL_TLS_Write          | TLS 写                   |
| 8   | HAL_TLS_Read           | TLS 读                  |
| 9    | HAL_UDP_Connect               | 建立 TCP 连接                              |
| 10    | HAL_UDP_Disconnect             | 断开 TCP 连接 |
| 11  | HAL_UDP_Write        | UDP 写                                |
| 12   | HAL_UDP_Read        | UPD 读                               |
| 13   | HAL_DTLS_Connect        | 建立 DTLS 连接              |
| 14   | HAL_DTLS_Disconnect     | 断开 DTLS 连接                            |
| 15   | HAL_DTLS_Write          | DTLS 写                   |
| 16   | HAL_DTLS_Read           | DTLS 读                  |

**基于 AT_socket 的 HAL 接口**

通过使能编译宏 **AT_TCP_ENABLED** 选择 AT_socket，则 SDK 会调用 `network_at_tcp.c` 的 `at_socket` 接口， at_socket 层不需要移植，需要实现 AT 串口驱动及 AT 模组驱动，AT 模组驱动只需要实现 AT 框架中 at_device 的驱动结构体 `at_device_op_t` 的驱动接口即可，可以参照 at_device 目录下的已支持的模组。AT 串口驱动需要实现串口的中断接收，然后在中断服务程序中调用回调函数 `at_client_uart_rx_isr_cb` 即可，可以参考 `HAL_AT_UART_freertos.c` 实现目标平台的移植。

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_AT_Uart_Init               |初始化 AT 串口                           |
| 2    | HAL_AT_Uart_Deinit             | 去初始化 AT 串口 |
| 3   | HAL_AT_Uart_Send        | AT 串口发送数据                                |
| 4   | HAL_AT_UART_IRQHandler        | AT 串口接收中断服务程序                               |


#### 3. 时间及打印相关的 HAL 接口

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_Printf             | 将格式化的数据写入标准输出流中          |
| 2    | HAL_Snprintf           | 将格式化的数据写入字符串                 |
| 3    | HAL_UptimeMs           | 检索自系统启动以来已运行的毫秒数         |
| 4    | HAL_DelayMs           | 阻塞延时，单位毫秒         |

#### 4. 设备信息相关的 HAL 接口

接入 IoT 平台需要在平台创建产品和设备信息，同时需要将产品及设备信息保存在设备侧的非易失存储介质。可以参考  `platform/os/linux/HAL_Device_linux.c` 示例实现。

| 序号 | 函数名                 | 说明                                       |
| ---- | ---------------------- | ------------------------------------------ |
| 1    | HAL_GetDevInfo             | 设备信息读取          |
| 2    | HAL_SetDevInfo           | 设备信息保存                     |

### 应用开发

可参考 SDK samples 目录下的例程进行开发。

## SDK 使用参考

请参见[C SDK 使用参考](设备开发指南\设备端SDK说明\SDK 使用参考\C SDK 使用参考\C SDK 使用参考)。
