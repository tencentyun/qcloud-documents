## 插件简介

- 腾讯视频云 OBS 265推流插件，让OBS-studio(版本20.0.0及以上)支持向腾讯视频云推 H.265 视频流进行直播。
- 采用 H.265 编码推流，比 H.264 更省流量，或相同流量下，画面质量更高。
- 本插件支持 **Intel** 和 **Nvidia** 平台的硬件加速
- 腾讯视频云会自动将 H.265 视频流转为 H.264 视频流，默认的播放地址是H.264视频流，要联系我们开启H.265播放配置才能得到H.265视频流播放地址。
- 推流地址无须特别设置。


## 使用说明

### step1: 下载并安装 OBS-Studio 
在 OBS Studio [官网](https://obsproject.com/)下载并安装 obs studio **20.0.0** 或以上版本。

### step2: 下载并安装 265 编码插件
点击 [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/OBS_Plugins/tx265-plugin-setup.exe) H.265 插件并安装，该插件仅能安装在 **20.0.0** 或以上版本的 OBS Studio 上。 

![](https://main.qcloudimg.com/raw/98f69bbefe4e5efee58e609446a5ba6a.png)

> 插件安装包会自动检测OBS studio安装的目录，检测失败需要您手动选择 OBS Studio 安装的目录


### step3: 设置OBS推流参数

#### 3.1 OBS 设置 - 流：
OBS设置-流-流类型选择 **Tencent Stream(H.265) Service**，填写推流地址

 [开通](https://console.cloud.tencent.com/live)直播服务后，可以使用 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 生成推流地址，详细信息可以参考 [获得推流播放URL](https://cloud.tencent.com/document/product/454/7915)。
![](https://main.qcloudimg.com/raw/81b7aaa96e7beb2744550360d3c1e1dd.png)


#### 3.2 OBS 设置 - 输出：
OBS设置-输出-输出模式-选择**高级**
OBS设置-输出-流-编码器-选择带**TX265开头的编码器**，并按需设置编码参数
![](https://main.qcloudimg.com/raw/da8c892c2c0cc5ac12c033d40163a2dd.png)

编码器名称|说明
-|-
TX265-Intel QuickSync HEVC Encoder | Intel 平台265硬编
TX265-NVENC HEVC Encoder | NVIDIA 平台265硬编
TX265-QQ265 HEVC Encoder | Tencent 音视频实验室自研265软编
TX265-x265 HEVC Encoder    |x265实现的265软编

若无法再编码器列表中看到硬编码器，请按照如下步骤开启：

**如何启用nvdia 265硬编:**
1. Windows版本要求: Windows 7/8/10
2. [查询显卡是否支持 NVENC H.265 (HEVC) ](https://developer.nvidia.com/video-encode-decode-gpu-support-matrix)
Desktop GPU: Geforce GTX 950系列或更高版本的显卡
Laptop GPU: GTX 965M, 970M, 980M系列或更高版本的显卡
3. 驱动版本高于378.66. [下载最新驱动程序](http://www.nvidia.com/drivers)

**如何启用Intel 265硬编:**

1. Windows版本要求: Windows 7/8/10
2. [检查您的CPU型号是否支持 “Intel® Quick Sync video”](https://ark.intel.com/zh-cn/)
Skylake或更高级的架构能很好的支持"Intel® Quick Sync video"
3. [下载/安装最新的 “Intel® HD Graphics" 驱动程序](https://downloadcenter.intel.com/zh-cn/)
4. ***双显卡用户要启用Intel 265硬编，需要在BIOS/CMOS设置下启用 “Internal Graphics”，把板载VGA或DVI接口(集成显卡)连接显示器***

### step4: 联系我们开启265播放

腾讯视频云自动把 265 的流转为 264 播放流，要播放 265 流，可以通过工单或者 400 电话联系我们启用 265 流播放配置，264 的播放地址依然有效，适合无法正常播放 265 流的客户端。
