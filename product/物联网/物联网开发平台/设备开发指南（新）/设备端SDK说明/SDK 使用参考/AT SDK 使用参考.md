
AT SDK 面向内置腾讯云物联网 AT 指令的模组，提供实现和定制模组交互的 SDK。

## SDK 获取

在 IoT explorer 平台 [创建产品和设备](https://cloud.tencent.com/document/product/1081/34739) 后，选择基于 MQTT AT 定制模组开发的方式，将会自动生成 MCU 侧的 [AT SDK](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based.git) 代码，并且把在平台创建的数据模板和事件生成了对应的配置及初始化代码。

## 软件架构
AT SDK 软件架构图如下：
![](https://main.qcloudimg.com/raw/0e49d40088a7b54102f73facf953ee23.jpg)
SDK 分四层设计，从上至下分别为应用层、核心协议层、AT 传输层、硬件抽象层。
- **服务层**
  在网络协议层之上，实现了包括设备接入鉴权，设备影子，网关，动态注册，日志上报和 OTA 等功能。
- **协议层**
  设备端和 IoT 平台交互的网络协议包括 MQTT/COAP/HTTP。
- **AT 传输层**
  实现基于腾讯云物联网定制 AT 指令的网络协议栈。
- **硬件抽象层**
  实现对不同硬件平台的底层操作抽象封装，需要针对具体的软硬件平台开展移植，分为必须实现和可选实现两部分 HAL 层接口。

## 目录结构

| 名称                            | 说明                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| docs                            | 文档目录，包含腾讯 AT 指令集定义。                           |
| port                            | HAL 层移植目录，需要实现串口的收发接口（中断接收），延时函数，模组上下电及 OS 相关接口。 |
| sample                          | 应用示例，示例使用 MQTT、影子、数据模板的使用方式。          |
| src                             | AT 框架及协议逻辑实现。                                      |
| ─  event                     | 事件功能协议封装。                                           |
| ─  module_at                 | at client 抽象，实现 RX 解析，命令下行，urc 匹配，resp 异步匹配。 |
| ─  shadow                    | 基于 AT 框架的 shadow 逻辑实现。                             |
| ─  mqtt                      | 基于AT 框架的 MQTT 协议实现。                                |
| ─  utils                     | json、timer、链表等应用。                                    |
| ─  include                   | SDK 对外头文件及设备信息配置头文件。                         |
| usr_logic                       | 自动生成的基于用户产品定义的业务逻辑框架代码。               |
| ─  data_config.c             | 用户定义的数据点。                                           |
| ─  events_config.c           | 用户定义的事件。                                             |
| ─data_template_usr_logic.c | 用户业务处理逻辑框架，实现预留的上下行业务逻辑处理函数即可。 |
| tools                           | 代码生成脚本。                                               |
| README.md                       | SDK 使用说明。                                               |

## 移植指引

|开发平台|参考文档|
|---|---|
|MCU+ 定制 AT 模组（蜂窝类）|[MCU+定制MQTT AT模组（蜂窝类）接入指引](https://cloud.tencent.com/document/product/1081/48395)|
|MCU+ 定制 AT 模组（Wi-Fi类）|[MCU+定制MQTT AT模组（Wi-Fi 类）接入指引](https://cloud.tencent.com/document/product/1081/48394)|

## SDK 接口说明

关于 SDK 的更多使用方式及接口了解，请参见 [qcloud_iot_api_export.h ](https://github.com/tencentyun/qcloud-iot-sdk-tencent-at-based/tree/master/include)。
