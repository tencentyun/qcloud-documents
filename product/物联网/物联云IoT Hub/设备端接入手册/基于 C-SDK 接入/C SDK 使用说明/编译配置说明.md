
本文档对 C SDK 的编译方式和编译配置选项进行说明，并介绍了 Linux 和 Windows 开发环境下的编译环境搭建以及编译示例。

## C SDK 编译方式说明
C SDK 支持以下编译方式。

####  cmake 方式
- 推荐使用 cmake 作为跨平台的编译工具，支持在 Linux 和 Windows 开发环境下进行编译。
- cmake 方式采用 CMakeLists.txt 作为编译配置选项输入文件。

#### Makefile 方式
- 对于不支持 cmake 的环境，使用 Makefile 直接编译的方式。
- Makefile 方式与 SDK v3.0.3及之前的版本保持一致，采用 make.settings 作为编译配置选项输入文件，修改完成后执行 make 即可。

#### 代码抽取方式
- 该方式可根据需求选择功能，将相关代码抽取到一个单独的文件夹，文件夹里面的代码层次目录简洁，方便用户拷贝集成到自己的开发环境。
- 该方式需要依赖 cmake 工具，在 CMakeLists.txt 中配置相关功能模块的开关，并将 EXTRACT_SRC 设置为 ON，在 Linux 环境运行以下命令：
```
mkdir build
cd build
cmake ..
```
 - 即可在 output/qcloud_iot_c_sdk 中找到相关代码文件，目录层次如下：
```
 qcloud_iot_c_sdk
 ├── include
 │   ├── config.h
 │   ├── exports
 ├── platform
 └── sdk_src
     └── internal_inc
```
 - include 目录为 SDK 供用户使用的 API 及可变参数，其中 config.h 为根据编译选项生成的编译宏。
 - platform 目录为平台相关的代码，可根据设备的具体情况进行修改适配。
 - sdk_src 为 SDK 的核心逻辑及协议相关代码，一般无需修改，其中 internal_inc 为 SDK 内部使用的头文件。

>?用户可将 qcloud_iot_c_sdk 拷贝到其目标平台的编译开发环境，并根据具体情况修改编译选项。

## C SDK 编译选项说明

#### 编译配置选项
以下配置选项大部分都适用于 cmake 和 make.setting。cmake 中的 ON 值对应于 make.setting 的 y，OFF 对应于 n。

| 名称                             | cmake 值            | 说明                                                         |
| :------------------------------- | ------------- | ------------------------------------------------------------ |
| BUILD_TYPE                       | release/debug | release：不启用 IOT_DEBUG 信息，编译输出到 release 目录下。<br />debug：启用 IOT_DEBUG 信息，编译输出到 debug 目录下。 |
| EXTRACT_SRC                      | ON/OFF        | 代码抽取功能开关，仅对使用 cmake 有效。                                             |
| COMPILE_TOOLS                    | gcc           | 支持 gcc 和 msvc，也可以是交叉编译器。例如 arm-none-linux-gnueabi-gcc。 |
| PLATFORM                         | Linux         | 包括 Linux/Windows/Freertos/Nonos。                             |
| FEATURE_MQTT_COMM_ENABLED        | ON/OFF        | MQTT 通道总开关。                                               |
| FEATURE_MQTT_DEVICE_SHADOW       | ON/OFF        | 设备影子总开关。                                               |
| FEATURE_COAP_COMM_ENABLED        | ON/OFF        | CoAP 通道总开关。                                               |
| FEATURE_GATEWAY_ENABLED          | ON/OFF        | 网关功能总开关。                                               |
| FEATURE_OTA_COMM_ENABLED         | ON/OFF        | OTA 固件升级总开关。                                            |
| FEATURE_OTA_SIGNAL_CHANNEL       | MQTT/COAP     | OTA 信令通道类型。                                              |
| FEATURE_AUTH_MODE                | KEY/CERT      | 接入认证方式。                                                 |
| FEATURE_AUTH_WITH_NOTLS          | ON/OFF        | OFF：TLS 使能， ON：TLS 关闭。    |                                
| FEATURE_DEV_DYN_REG_ENABLED      | ON/OFF        | 设备动态注册开关。                                             |
| FEATURE_LOG_UPLOAD_ENABLED       | ON/OFF        | 日志上报开关。                                                 |
| FEATURE_EVENT_POST_ENABLED       | ON/OFF        | 事件上报开关。                                                 |
| FEATURE_DEBUG_DEV_INFO_USED      | ON/OFF        | 设备信息获取来源开关。                                         |
| FEATURE_SYSTEM_COMM_ENABLED      | ON/OFF        | 获取后台时间开关。                                             |
| FEATURE_AT_TCP_ENABLED           | ON/OFF        | AT 模组 TCP 功能开关。                                            |
| FEATURE_AT_UART_RECV_IRQ         | ON/OFF        | AT 模组中断接受功能开关。                                       |
| FEATURE_AT_OS_USED               | ON/OFF        | AT 模组多线程功能开关。                                         |
| FEATURE_AT_DEBUG                 | ON/OFF        | AT 模组调试功能开关。                                           |
| FEATURE_MULTITHREAD_TEST_ENABLED | ON/OFF        | 是否编译 Linux 多线程测试例程。                                  |

配置选项之间存在依赖关系，当依赖选项的值为有效值时，部分配置选项才有效，主要如下：

| 名称                             | 依赖选项                                                | 有效值       |
| :------------------------------- | ------------------------------------------------------- | ------------ |
| FEATURE_MQTT_DEVICE_SHADOW       | FEATURE_MQTT_COMM_ENABLED                               | ON           |
| FEATURE_GATEWAY_ENABLED          | FEATURE_MQTT_COMM_ENABLED                               | ON             |
| FEATURE_OTA_SIGNAL_CHANNEL(MQTT) | FEATURE_OTA_COMM_ENABLED<br />FEATURE_MQTT_COMM_ENABLED | ON<br />ON   |
| FEATURE_OTA_SIGNAL_CHANNEL(COAP) | FEATURE_OTA_COMM_ENABLED<br />FEATURE_COAP_COMM_ENABLED | ON<br />ON   |
| FEATURE_AUTH_WITH_NOTLS          | FEATURE_AUTH_MODE                                       | KEY          |
| FEATURE_AT_UART_RECV_IRQ         | FEATURE_AT_TCP_ENABLED                                  | ON           |
| FEATURE_AT_OS_USED               | FEATURE_AT_TCP_ENABLED                                  | ON           |
| FEATURE_AT_DEBUG                 | FEATURE_AT_TCP_ENABLED                                  | ON           |


#### 设备信息选项
在腾讯云物联控制台创建设备之后，需要将设备信息（ProductID/DeviceName/DeviceSecret/Cert/Key 文件）配置在 SDK 中才能正确运行。在开发阶段，SDK 提供两种方式存储设备信息：
- 存放在代码中（编译选项 DEBUG_DEV_INFO_USED = ON），则在`platform/os/xxx/HAL_Device_xxx.c`中修改设备信息，在无文件系统的平台下可以使用这种方式。
- 存放在配置文件中（编译选项 DEBUG_DEV_INFO_USED = OFF），则在`device_info.json`文件修改设备信息，此方式下更改设备信息不需重新编译 SDK，在 Linux/Windows 平台下开发推荐使用这种方式。

