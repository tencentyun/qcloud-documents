

## SDK 获取
SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [C SDK 5G](https://github.com/tencentyun/qcloud-iot-explorer-5G-sdk-embedded)。

## 5G SDK 架构
5G SDK 集成  IoT Explorer C SDK，通过 MQTT 协议与 IoT Explorer 保持双向连接，实现5G模组状态上报、用户指令下发等基础通信功能。5G SDK 架构图如下：
![architecture](https://main.qcloudimg.com/raw/49489e2ba2c9135cbebec7cc04d14ebd/5G-SDK-architecture.png)
除此之外，SDK 还包括或者规划了以下功能：
- **应用层**
  提供模组管理、故障管理、软件安装和 Web 服务功能。
  - 模组管理通过模组的通用 AT 指令或专用信令接口（例如：高通的 QMI）读取模组/网络状态、配置网络参数和发起拨号操作，实现终端入网和运行状态监控。
  - 故障管理利用网络故障诊断工具、系统日志以及其它诊断手段，在进程运行异常时对网络、模组以及上位机进行故障定位并对可排除的故障进行系统恢复。当检测到无法排除的故障时，记录当前故障的特征，待设备通过其它途径恢复正常后，上报该次故障。同时，故障管理可提供模组固件升级功能。
  - 软件安装监听并执行用户通过 IoT Explorer 下发的软件安装指令。利用此功能的典型应用是 VPN 客户端软件的安装。
  - Web 服务为本地应用提供一组 RESTFul API 访问及配置模组，调用 QoS 加速功能。
- **网络层**
  提供隧道配置和 QoS 加速功能。
  - 隧道配置负责创建并管理从终端到 TSEC 网关的 IPSEC 或其它类型的 IP 隧道（例如：IPinIP），实现 VPN 组网。包括信令面配置和数据面配置两部分：
    - 信令面配置通过接收 IoT Explorer 下发的相关指令，启动 VPN 客户端与 TSEC 网关协商私网 IP 地址和数据加密方法，并周期地确认协商结果的有效性，当发现协商结果失效或对端“掉线”时，重新发起协商或删除该隧道端口。
    - 数据面配置创建虚拟隧道接口，并将协商好的 IP 地址配置到该接口，为用户应用程序提供数据封装和加解密等服务。
  - QoS 加速为本地应用提供4G/5G空口带宽及时延保障。应用程序调用 QoS 加速相关的 RESTFul API，向 TSEC 发起 QoS 加速请求，后者通过调用运营商能力开放平台的接口，为该应用创建专用数据通道实现空口 QoS 保障。QoS 加速屏蔽了运营商的差异性，向应用程序提供一个统一的接口。
- **驱动层**
  提供驱动配置功能。根据模组厂商的具体实现，为模组的 USB 接口加载相应的驱动，例如利用 option.ko 和 cdc_ether.ko 来创建虚拟以太网卡和虚拟串口，实现数据收发和 AT 指令的下发。 
	
>?为方便用户体验 IoT Explorer 5G模组管理功能，SDK 还提供了模组仿真器供无5G模组的环境下使用。

## 5G SDK 目录结构

| 名称                               | 说明                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| qcloud-iot-explorer-sdk-embedded-c | IoT Explorer C SDK 代码库                                     |
| mm-lib                             | 模组管理库，包含已完成对接的5G模组的管理函数集，以插件形式提供 |
| module-manager.c                   | 模组管理的顶层函数，调用 mm-lib 和 C SDK 上报模组和网络的状态，同时接收 IoT Explorer 下发的指令创建、配置或者销毁 IP 隧道 |
| device_info.json                   | 设备信息文件，取代 C SDK 下的同名文件，为5G SDK 提供模组鉴权信息  |
| Makefile                           | 使用 Makefile 直接编译                                        |

## 编译步骤

>?编译环境为 Ubuntu 版本 v18.04。
### 1. 编译配置说明

通过修改 `qcloud-iot-explorer-sdk-embedded-c` 目录下的 make.settings 文件，可以修改5G SDK 功能，例如：配置 `FEATURE_ACTION_ENABLED` 项打开数据行为功能。

编译配置选项的详细说明请参考 [C SDK编译配置说明](https://cloud.tencent.com/document/product/1081/39327)。 

### 2. make 编译

- 运行 git submodule，更新子模块 C SDK 并切换到 v3.1.0。 
```git submodule update --init```
- 运行 make，编译可执行文件 module-manager。
```make```

### 3. 填写设备信息

将在腾讯云物联网平台创建的设备的设备信息（以密钥认证设备为例，包括 ProductId，DeviceName 和 DiviceSecret），填写到5G SDK 根目录下 device_info.json 中，示例代码如下： 
```json
{
    "auth_mode":"KEY",

    "productId":"********",
    "productSecret":"YOUR_PRODUCT_SECRET",
    "deviceName":"dev_test",

    "key_deviceinfo":{    
        "deviceSecret":"xxxxxxxxxxxxxxxxx=="
    },

    "cert_deviceinfo":{
        "devCertFile":"YOUR_DEVICE_CERT_FILE_NAME",
        "devPrivateKeyFile":"YOUR_DEVICE_PRIVATE_KEY_FILE_NAME"
    },

    "subDev":{
        "sub_productId":"YOUR_SUBDEV_PRODUCT_ID",
        "sub_devName":"YOUR_SUBDEV_DEVICE_NAME"
    }
}
```



### 4. 运行参数配置

根目录下运行`./module-manager`，通过参数分别实现：

- **-S**：使用模组仿真器。
- **无参数**：使用5G模组。

