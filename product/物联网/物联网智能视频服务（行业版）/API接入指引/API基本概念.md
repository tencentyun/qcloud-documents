本文为您介绍物联网智能视频服务（行业版）的 API 接口基本概念。

 

 ## 设备相关概念

- 主设备(`master device`)
主设备是指通过国标协议（GB28181 协议）接入到腾讯云物联网智能视频服务的设备，常见主设备包括：常规 IPC 摄像机，NVR，VMS 等，也可以由其他支持国标协议设备组成，例如车载监控设备，无人机，国标软终端，其他国标硬终端等。每个主设备在腾讯云平台创建后，会被分配一个主设备编码（DeviceCode）编码规则可以参考 GB/T28181-2016 详细定义。
- 通道(`channel`)
通道是对国标设备下具备音视频或者告警能力能力描述，例如 NVR 下面可以接入8个IPC设备，在 NVR 内部描述为 D1~D7 ，可以描述为8个通道，每个通道都具备一个一个通道编码，编码规则可以参考 GB/T28181-2016 详细定义。

 ## API 文档概念解析

 

- 公共参数
![](https://qcloudimg.tencent-cloud.cn/raw/f5c77f03f4611b73f537782b72a67693.png)
- 设备编码(DeviceCode)
控制台添加设备，由平台分配的编码。
![](https://qcloudimg.tencent-cloud.cn/raw/b011e857a15bb8e39f174309af86d6ed.png)
- 通道编码(ChannelCode)
通道编码一般有用户自定义，通过 GB28181 协议上报到上级平台的。
![](https://qcloudimg.tencent-cloud.cn/raw/f6994f4e9dbe3c3a6224bbd8d9a3da2c.png)
- 设备 ID(DeviceId)
用户控制台添加主设备后，平台会分配一个主设备 ID，主设备 ID 可以用过接口 [DescribeDeviceList](https://cloud.tencent.com/document/api/1361/53721) 或者 [DescribeGroupDevices](https://cloud.tencent.com/document/product/1361/53748) 获取设备列表信息，这里以 [DescribeDeviceList](https://cloud.tencent.com/document/api/1361/53721)  为例：
![](https://qcloudimg.tencent-cloud.cn/raw/f271c1d07aa4dfaa7105dadc9ef8163f.png)
- 通道 ID(ChannelId)
添加主设备成功后，通过 GB28181 命令，设备上报 catlog 携带自身通道信息，平台会分配一个通道 ID，可以通过 [DescribeChannels](https://cloud.tencent.com/document/product/1361/67429) 接口获取，示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/27968835b09a1c3ccabb13550c95f8bd.png)

 
