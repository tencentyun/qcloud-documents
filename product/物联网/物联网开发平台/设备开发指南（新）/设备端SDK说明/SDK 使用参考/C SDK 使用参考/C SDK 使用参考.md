
腾讯云物联网设备端 C SDK 依靠安全且性能强大的数据通道，为物联网领域开发人员提供设备端快速接入云端，并和云端进行双向通信的能力。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C SDK](https://github.com/tencentyun/qcloud-iot-explorer-sdk-embedded-c/releases)。

## 软件架构

<img src="https://main.qcloudimg.com/raw/76fc3f15c4c91ea6cf7e496f25d5d572.jpg"  width="80%">

SDK 分四层设计，从上至下分别为平台服务层、核心协议层、网络层、硬件抽象层。

- **服务层**
 - 在网络协议层之上，实现了包括设备接入鉴权，设备影子，网关，动态注册，日志上报和 OTA 等功能。
 - 设备侧和 IoT Explorer 平台交互的核心协议为 MQTT，基于此核心协议，实现了数据模板和 OTA 功能。平台通过对 IoT 设备的通用抽象定义了 [数据模板协议](https://cloud.tencent.com/document/product/1081/34916)，云端和设备基于 MQTT 的 payload 承载的数据实现数据模板协议数据流交互。OTA 功能的升级命令、版本及固件信息通过 MQTT 协议通道交互，固件下载通过 HTTPS 协议通道交互。
- **协议层**
  设备端和 IoT 平台交互的网络协议包括 MQTT/CoAP/HTTP。
- **网络层**
 网络层的实现支持基于 bsd_socket 方式和 AT_socket 方式，对于资源丰富系统本身集成 TCP/IP 或 LwIP 网络协议栈的，可以选择 bsd_socket 的网络接口。对于部分资源受限设备，通过通信模组（蜂窝模组/Wi-Fi 模组等）和 MCU 交互而实现网络接入的可以选择 SDK 提供 at_socket 框架，SDK 未支持的通信模组参照 SDK 支持的通信模组实现 at_device 结构体 at_device_op_t 里的驱动接口即可。
- **硬件抽象层**
硬件抽象层需要针对具体的软硬件平台开展移植，分为必须实现和可选实现两部分 HAL 层接口。必选实现的接口为时间（获取毫秒数）、打印、格式化打印、内存操作、设备信息读写。可选实现接口，使用 RTOS 的，需要实现锁、信号量、线程创建及销毁、延时睡眠。使用 AT_Socket 接入网络，需要实现 AT 串口驱动及模组驱动。SDK 已经支持 Linux、Windows、FreeRTOS、nonOS 四种典型环境的 HAL 层示例移植实现，在 Linux 和 Windows 环境可以直接编译运行相关示例。

## 移植指引

|开发平台|文档|
|---|---|
|Linux|[Linux 平台接入指引](https://cloud.tencent.com/document/product/1081/48387)|
|Windows|[Windows 平台接入指引](https://cloud.tencent.com/document/product/1081/48392)|
|MCU+ 通用 AT 模组+nonOS|[MCU+ 通用 TCP AT 模组（FreeRTOS）接入指引](https://cloud.tencent.com/document/product/1081/48396)|
|MCU+ 通用 AT 模组+nonOS|[MCU+ 通用 TCP AT 模组（nonOS）接入指引](https://cloud.tencent.com/document/product/1081/48397)|
|FreeRTOS+lwIP|[FreeRTOS+lwIP 平台接入指引](https://cloud.tencent.com/document/product/1081/48388)|
|其他平台|[C SDK 移植接入指引](https://cloud.tencent.com/document/product/1081/48389)|

## SDK 相关文档

SDK 相关文档，详情请参见 [SDK 使用参考](https://cloud.tencent.com/document/product/1081/48370)。
