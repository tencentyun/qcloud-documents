## 概述

腾讯云物联网开发平台针对不同的设备开发场景，提供了多版本语言的设备 SDK 供客户使用：

- `qcloud-iot-explorer-sdk-embedded-c`是针对嵌入式设备接入使用腾讯 IoT Explorer 平台提供的 C 语言版本 SDK。
- `qcloud-iot-explorer-sdk-android` 是针对智能设备接入使用腾讯 IoT Explorer 平台的 Android 版本 SDK。


## C SDK 代码托管

- 自 V3.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c.git) 托管 C 设备 SDK 代码。
- 请下载最新版 [C-SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。
- SDK 3.1.0之前的 C SDK 版本 [访问此处](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)。

>! V3.1.0之前的版本相较于3.1.0及以后的版本代码 Git 路径不一样，同时与平台交互协议有较大区别。


## Android SDK 代码托管

自 V3.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-sdk-android) 托管 Android 设备 SDK 代码。

## 5G SDK 代码托管

- 腾讯云物联开发平台 （IoT Explorer） 5G SDK 是腾讯5G物联开发套件的设备端组件，通过与 IoT Explorer 配合，为宽带物联应用提供5G模组远程运维，接入腾讯边缘接入和网络加速平台（TSEC）实现 VPN 组网，空口加速等功能，降低用户使用5G网络及边缘计算的门槛。
- 自 V0.1.0 版本开始，使用独立的 [Github](https://github.com/tencentyun/qcloud-iot-explorer-5G-sdk-embedded) 托管 5G SDK 代码。


## C SDK 使用说明

SDK 分四层设计，从上至下分别为平台服务层、核心协议层、网络层、硬件抽象层。

- 设备侧和 IoT Explorer 平台交互的核心协议为 MQTT，基于此核心协议，实现了数据模板和 OTA 功能。平台通过对 IoT 设备的通用抽象定义了 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916)，云端和设备基于 MQTT 的 payload 承载的数据实现数据模板协议数据流交互。OTA 功能的升级命令、版本及固件信息通过 MQTT 协议通道交互，固件下载通过 HTTPS 协议通道交互。

- 网络层的实现支持基于 bsd_socket 方式和 AT_socke t方式,对于资源丰富系统本身集成 TCP/IP 或 LwIP 网络协议栈的，可以选择 bsd_socket 的网络接口。对于部分资源受限设备，通过通信模组（蜂窝模组/WIFI模组等）和 MCU 交互而实现网络接入的可以选择 SDK 提供 at_socket 框架，SDK 未支持的通信模组参照 SDK 支持的通信模组实现 at_device 结构体 at_device_op_t 里的驱动接口即可。

- 硬件抽象层需要针对具体的软硬件平台开展移植，分为必须实现和可选实现两部分 HAL 层接口。其中必选实现的接口为时间（获取毫秒数）、打印、格式化打印、内存操作、设备信息读写。可选实现接口，使用 RTOS 的，需要实现锁、信号量、线程创建及销毁、延时睡眠。使用 AT_Socket 接入网络的，需要实现 AT 串口驱动及模组驱动。SDK 已经支持 Linux、Windows、FreeRTOS、nonOS 四种典型环境的 HAL 层示例移植实现，在 Linux 和 Windows 环境可以直接编译运行相关示例。
  ![frame_work](https://main.qcloudimg.com/raw/76fc3f15c4c91ea6cf7e496f25d5d572.jpg)
