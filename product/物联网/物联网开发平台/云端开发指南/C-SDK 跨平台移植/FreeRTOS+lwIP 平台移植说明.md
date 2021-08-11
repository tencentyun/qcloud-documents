
本文档介绍如何将腾讯云物联 C-SDK 移植到 **FreeRTOS+lwIP** 平台。

## 简介
FreeRTOS 作为一个微内核系统，主要提供任务创建及调度和任务间通信等 OS 核心机制，在不同设备平台还需要搭配多个软件组件包括 C 运行库（例如 newlib 或者 ARM CMSIS 库）和 TCP/IP 网络协议栈（如 lwIP）才能形成完整的嵌入式运行平台。同时各个设备平台的编译开发环境也各不相同，因此在移植 C-SDK 时，需要根据不同设备的具体情况进行适配。

>?SDK 在 **platform/os/freertos** 里提供了一个基于 **FreeRTOS+lwIP+newlib** 的参考实现，该实现已在乐鑫 ESP8266 平台上验证测试。


## 抽取代码
因为基于 RTOS 系统的平台编译方式各不相同，一般无法直接使用 SDK 的 cmake 或者 make 编译，因此 SDK 提供了代码抽取功能，可根据需要将相关代码抽取到一个单独的文件夹，文件夹里面的代码层次目录简洁，方便用户拷贝集成到自己的开发环境。

1. 修改 CMakeLists.txt 中配置为 freertos 平台，并开启代码抽取功能：
```
set(BUILD_TYPE                  "release")
set(PLATFORM 	                "freertos")
set(EXTRACT_SRC ON)
set(FEATURE_AT_TCP_ENABLED OFF)
```
2. 在 Linux 环境运行以下命令：
```
mkdir build
cd build
cmake ..
```
3. 即可在 output/qcloud_iot_c_sdk 中，找到相关代码文件，目录层次如下：
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
 - include 目录：SDK 供用户使用的 API 及可变参数，其中 config.h 为根据编译选项生成的编译宏。API 具体介绍请参考 [接口及可变参数说明](https://cloud.tencent.com/document/product/1081/39329)。
 - platform目录：平台相关的代码，可根据设备的具体情况进行修改适配。具体的函数说明请参考[ C-SDK_Porting 跨平台移植概述](https://cloud.tencent.com/document/product/1081/39316)。
 - sdk_src：SDK 的核心逻辑及协议相关代码，一般不需要修改，其中 internal_inc 为 SDK 内部使用的头文件。
4. 用户可将 qcloud_iot_c_sdk 拷贝到其目标平台的编译开发环境，并根据具体情况修改编译选项。



## 移植示例
在 Linux 开发环境基于乐鑫 ESP8266 RTOS 平台搭建一个工程示例。

1. 请参考 [ESP8266_RTOS_SDK](https://github.com/espressif/ESP8266_RTOS_SDK) 获取 RTOS_SDK 和交叉编译器，并创建一个项目工程。
2. 将上面抽取的 qcloud_iot_c_sdk 目录，拷贝到 components/qcloud_iot 下。
3. 在 components/qcloud_iot 下，新建一个编译配置文件 component.mk，内容如下：
```
#
# Component Makefile
#
COMPONENT_ADD_INCLUDEDIRS := \
qcloud_iot_c_sdk/include \
qcloud_iot_c_sdk/include/exports \
qcloud_iot_c_sdk/sdk_src/internal_inc
COMPONENT_SRCDIRS := \
qcloud_iot_c_sdk/sdk_src \
qcloud_iot_c_sdk/platform
```
至此，您可以将 qcloud_iot_c_sdk 作为一个组件进行编译了，之后在用户代码里面就可以调用物联 C-SDK 的接口进行连接和收发消息。




