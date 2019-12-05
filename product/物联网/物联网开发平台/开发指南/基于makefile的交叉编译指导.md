## 简介

本文为您详细介绍如何基于 makefile 实现交叉编译。

## 操作步骤

**1. 下载最新版本设备端 [C-SDK](https://github.com/tencentyun/qcloud-iot-sdk-embedded-c/releases)**
**2. 配置编译配置文件 make.settings**
**2.1 配置交叉编译工具链路径及 OS、TLS 平台适配目录**

```
BUILD_TYPE                   = release	#release/debug

#PLATFORM_CC                   = gcc  
#PLATFORM_AR                   = ar
#PLATFORM_OS                   = linux
#PLATFORM_SSL                  = mbedtls

#
# Uncomment below and specify PATH to your toolchain when cross-compile SDK
#
PLATFORM_CC                 = /home/shock/openwrt/packages/toolchain/mipsel-linux-gcc
PLATFORM_AR                 = /home/shock/openwrt/packages/toolchain/mipsel-linux-ar
PLATFORM_OS                 = mbedos
PLATFORM_SSL                = mbedtls
```

**2.2 配置期望使能的功能选项及鉴权模式**

```
FEATURE_MQTT_COMM_ENABLED               = y     # 是否打开MQTT通道的总开关
FEATURE_MQTT_DEVICE_SHADOW			  = y	 # 是否打开设备影子的总开关
FEATURE_COAP_COMM_ENABLED               = y     # 是否打开CoAP通道的总开关
FEATURE_NBIOT_COMM_ENABLED              = y     # 是否打开NBIoT通道的消息组装

FEATURE_OTA_COMM_ENABLED                = y     # 是否打开OTA固件升级总开关
FEATURE_OTA_SIGNAL_CHANNEL              = MQTT  # OTA信令通道类型：MQTT/COAP

FEATURE_AUTH_MODE				       = KEY	# MQTT/CoAP接入认证方式，使用证书认证：CERT；使用密钥认证：KEY
FEATURE_AUTH_WITH_NOTLS				 = n	  # 接入认证是否不使用TLS，证书方式必须选择使用TLS，密钥认证可选择不使用TLS

FEATURE_LOG_UPLOAD_ENABLED              = n     # 是否打开日志上报云端功能
FEATURE_EVENT_POST_ENABLED              = y     # 是否打开事件上报功能
FEATURE_SYSTEM_COMM_ENABLED             = y     # 是否打开获取iot后台时间功能
FEATURE_MULTITHREAD_TEST_ENABLED        = n     # 是否编译Linux多线程测试例程
```

**3. 执行编译**

```shell
cd qcloud-iot-sdk-embedded-c
make
```

**4. 上传到目标系统**
编译执行后，将`output\release\bin`目录下的二进制文件，上传到目标硬件平台上，即可运行。或者将生成的 SDK 核心逻辑库 libiot_sdk.a 和平台移植库 libiot_platform.a 链接到目标应用镜像中。

make.settings 具体含义参考下表：

<table>
   <tr>
      <th>配置选项</th>
      <th>含义</th>
   </tr>
   <tr>
      <td>BUILD_TYPE</td>
      <td>编译模式，若是 debug 则开启代码跟踪功能，开启后程序运行过程中函数的调用堆栈将被跟踪并打印。</td>
   </tr>
   <tr>
      <td>PLATFORM_CC</td>
      <td>C 源码编译器，使用交叉编译时，请确保 gcc/ar 在同一目录。</td>
   </tr>
   <tr>
      <td>PLATFORM_AR</td>
      <td>静态库压缩器，使用交叉编译时，请确保 gcc/ar 在同一目录。</td>
   </tr>
   <tr>
      <td>PLATFORM_OS</td>
      <td>指定目标平台的操作系统，SDK 中包含 Linux 版本示例。</td>
   </tr>
   <tr>
      <td>FEATURE_MQTT_COMM_ENABLED</td>
      <td>是否开启设备 MQTT 功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_MQTT_DEVICE_SHADOW</td>
      <td>是否开启设备影子功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_COAP_COMM_ENABLED</td>
      <td>是否开启设备 CoAP 功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_OTA_COMM_ENABLED</td>
      <td>是否开启设备 OTA 功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_OTA_SIGNAL_CHANNEL</td>
      <td>OTA 通道选择 MQTT/COAP，默认 MQTT 通道。</td>
   </tr>
   <tr>
      <td>FEATURE_AUTH_MODE</td>
      <td>MQTT/CoAP 接入认证方式，使用证书认证：CERT；使用密钥认证：KEY，默认为 CERT。</td>
   </tr>
   <tr>
      <td>FEATURE_AUTH_WITH_NOTLS</td>
      <td>接入认证是否不使用 TLS，证书方式必须选择使用 TLS，密钥认证可选择不使用 TLS，默认不选择不使用 TLS。</td>
   </tr>
   <tr>
      <td>FEATURE_SYSTEM_COMM_ENABLED</td>
      <td>是否打开获取 IoT 后台时间功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_LOG_UPLOAD_ENABLED</td>
      <td>是否打开日志上报云端功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_EVENT_POST_ENABLED</td>
      <td>是否打开事件上报功能，默认开启。</td>
   </tr>
   <tr>
      <td>FEATURE_MULTITHREAD_TEST_ENABLED</td>
      <td>是否编译 Linux 多线程测试例程，默认开启。</td>
   </tr>
</table>

