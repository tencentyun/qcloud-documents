## 背景

LoRa Edge 是 Semtech 在 2020 年推出的面向资产管理应用的产品系列，支持 GPS 及北斗卫星扫描、无源 Wi-Fi 扫描等多重定位技术，同时集成了远距离 LoRa 收发器。其中 LR1110 是该系列的第一款芯片，主打特色是超低的定位功耗以及极具吸引力的 BOM 成本。
![](https://qcloudimg.tencent-cloud.cn/raw/093e83e937bc9e967b654d80e4d262da.jpg)

据介绍，LR1110 在 GNSS 定位的功耗优势主要在于将传统的卫星解算流程进行优化，芯片本地只扫描空口的卫星导航电文，将导航电文上报到云平台进行详细位置解算，从而节省了芯片本地的工作时长和运算需求。因此，LR1110 需要配套云平台进行使用。国外用户可以使用 Semtech LoRa Cloud，但中国用户在使用体验上不大理想。

目前针对中国用户，腾讯云物联网开发平台已经支持 LoRa Edge LR1110 定位功能，用户还可以利用腾讯连连小程序、IoT Enable等功能快速开发特色应用。

>? 这篇文章先总体介绍 LoRa Edge 接入腾讯云物联网开发平台的系统架构，接着分别介绍各组件的具体开发细节，包含节点、网关、物联网平台及腾讯连连小程序的操作。



## 1 系统架构

系统架构图参考。
![](https://qcloudimg.tencent-cloud.cn/raw/861525205814e0cbf9215d6f7b58f1ec.png)

## 2 LR1110 节点操作

这里 LR1110 节点先采用 Semtech LR1110 EVK，官方配套的软件采用的 GCC 编译器，需要在 Linux 环境下编译。后面 TencentOS tiny 也会开放一套 EVK，支持 MDK 编译器，Window 下的 Keil 就能编译了。

### 2.1 节点硬件准备

![](https://qcloudimg.tencent-cloud.cn/raw/202527fde301e8879dd4b24524fd7445.png)

Semtech LR1110 EVK, 采用 STM32L476RG Nucleo 底板 + LR1110 shield 的形式，两个 shield 分别支持不同的天线：
• PCB_E592V01B does not have a LNA and connects to the long antenna
• PCB_E516V02B includes one LNA and can only use the short antenna.

我们采用 PCB_E592V01B，配套一根长长的无源天线，方便测试。

### 2.2 节点软件操作

Basic modem 的软件已在 [github 开源](https://github.com/lorabasics/lorabasicsmodem/tree/develop/)。


## 3 腾讯云 IoT Explorer 控制台操作

腾讯云物联网开发平台完整的 [使用手册说明](https://cloud.tencent.com/document/product/1081)。
LoRaWAN 产品完整的 [使用手册说明](https://cloud.tencent.com/document/product/1081/52426)。

### 3.1 LoRaWAN 网关接入

>? 用户的 LoRaWAN 网关需支持 [Packet Forwarder 协议](https://github.com/Lora-net/packet_forwarder/blob/master/PROTOCOL.TXT)。

LoRaWAN 网关上的配置需做如下调整：

```
配置接入域名：loragw.things.qcloud.com
接入端口：1700
```

详细的网关接入操作及腾讯云物联网开发平台的操作，可以查看文档 [LoRaWAN 网关管理](https://cloud.tencent.com/document/product/1081/41192)。

### 3.2 腾讯LoRa社区网络

除了自建网关之外，值得一提的是还可以借助腾讯 LoRa 社区网络实现更广的网络覆盖，可以极大方便 LR1110 的测试。

尤其是在深圳，可以看到周围有腾讯开放的一些社区网关，采用 80~87 上行信道，也就是 486.3 ~ 487.7 MHz。
![](https://qcloudimg.tencent-cloud.cn/raw/326c8e08a67b2b874ef19981e7b35c9b.png)


### 3.3 创建产品及设备

1. 创建产品
	- 产品品类：智慧生活-安防报警-定位器。// 别的产品品类或者不选也都可以，这个产品品类的好处是在腾讯连连中有一个地图免开发面板，方便查看位置。
	- 设备类型：设备
	- 认证方式：密钥认证
	- 通信方式：LoRaWAN
2. 物模型添加标准功能
菜单操作为：物模型 -> 添加标准功能 -> 通用类型 -> 勾选“wifi定位”、“GNSS导航电文”
“wifi定位”为扫描的AP信息，包含MAC地址和RSSI。
“GNSS导航电文”为视野卫星的导航电文。
3. 新建设备
在设备调试tab中，点击“新建设备”。按照之前源码中配置的 DevEUI 和 AppKey 来创建设备。

### 3.4 查看设备日志

LR1110 节点如果上电工作，且LoRaWAN网关保持上线，那么控制台中就会看到设备数据更新。

设备属性 tab 页面中可以看到数据更新：
![](https://qcloudimg.tencent-cloud.cn/raw/f31260c957683378e981506efe7a9e28.png)

设备日志 tab 页面中可以看到设备原始数据：
![](https://qcloudimg.tencent-cloud.cn/raw/6cfdc0d31f8f06814622d76f9955b670.png)

### 3.5 位置空间操作

如果想要在控制台看到设备的实时位置，需要新建位置空间。菜单位于“增值服务-位置服务”。
![](https://qcloudimg.tencent-cloud.cn/raw/9c46e3eb864772e28f6ef53da9c1ac33.png)

打开位置空间，将会看到最近的实时位置。
![](https://qcloudimg.tencent-cloud.cn/raw/e75398cd123fc1970d204e2f8a2f580f.png)

位置空间还有更丰富的功能，可以查看历史轨迹、热力图，以及操作围栏等等。
![](https://qcloudimg.tencent-cloud.cn/raw/e75398cd123fc1970d204e2f8a2f580f.png)


### 3.6 通过腾讯云API获取设备历史位置

腾讯云API提供位置服务相关接口，用户可以通过API的方式来获取位置服务相关信息，参考[位置服务相关接口](https://cloud.tencent.com/document/product/1081/62446)
![](https://qcloudimg.tencent-cloud.cn/raw/ae8c591c591e99140b556e416628c162.png)

### 3.7 第三方应用

第三方应用如果想要获得设备原始数据，可以使用数据同步功能，将数据通过HTTP或者CKafka推送到第三方服务器，菜单位于“基础服务-数据同步”。

## 4 使用腾讯连连小程序

### 4.1 扫码绑定设备

设备列表 tab 页面可以快速查看设备的二维码，打开“腾讯连连”小程序扫码绑定设备。
![](https://qcloudimg.tencent-cloud.cn/raw/859bc40284dd96cafc2dd101dc58d7c3.png)

### 4.2 打开面板

交互开发 tab 页面默认是“标准面板”，展现产品 json 物模型。如果要在小程序中看到地图，需要调整为“免开发面板”。
![](https://qcloudimg.tencent-cloud.cn/raw/5431faffde45ea6bf48625145c069d41.png)

### 4.3 小程序界面

打开腾讯连连小程序，即可看到设备的实时位置。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d8aaba7bf77557e1e2f0caccc96bf82d.jpg" width="300px">


