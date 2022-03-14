## 操作场景
用户创建完 LoRaWAN 设备后，需要通过 LoRaWAN 网关将设备接入到平台。本文档主要介绍如何使用物联网开发平台进行 LoRaWAN 网关管理。

## 操作步骤

### 使用腾讯 LoRaWAN 社区网络

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，单击某一个已新建产品的项目。
2. 进入项目列表页，选择左侧菜单**网络管理** > **LoRaWAN 网关管理**。导航栏右侧会展示出腾讯 LoRaWAN 社区网络的地图页面。
3. 您可以单击地图，并查看自己的附近是否有正在运行的 LoRaWAN 网关，这些网关为社区的开发者主动共享的，可以直接通过这些网关进行 LoRaWAN 设备的无线接入。

### 新建用户 LoRaWAN 网关

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，单击某一个已新建产品的项目。
2. 进入项目列表页，选择左侧菜单**网络管理** > ** LoRaWAN 网关管理**，单击**添加网关**。
![](https://main.qcloudimg.com/raw/92cf582c64511029e9d8086c28cba3e6.png)
3. 在新建网关页面，填写网关基本信息。
    - 网关名称，本示例中填写 GW1。
    - GwEUI，为网关唯一 ID。
    - 是否公开。
     - 选择“是”，表示社区开发者可在社区网络中看到该网关，并可通过这个网关进行 LoRaWAN 节点接入。
     - 选择“否”，则只有用户自己才能查看该网关。

![](https://main.qcloudimg.com/raw/8fa4b51d45f3de44ba9bdde5262aaa05.png)
4. 网关新建成功后，您可在网关列表页查看到“GW1”。

### 用户 LoRaWAN 网关操作

>?用户的 LoRaWAN 网关需支持 [Packet Forwarder 协议](https://github.com/Lora-net/packet_forwarder/blob/master/PROTOCOL.TXT)。

LoRaWAN 网关上的配置需做如下调整：
```
配置接入域名：loragw.things.qcloud.com
接入端口：1700
```
当网关按要求配置并重启运行之后，即可在网关列表页查看到网关的在线状态变为“在线”。
