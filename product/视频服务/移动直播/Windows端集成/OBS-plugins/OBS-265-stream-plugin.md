### 腾讯视频云OBS 265推流插件

腾讯视频云OBS 265推流插件，让OBS-studio(版本20.0.0及以上)支持向腾讯视频云推H.265视频流进行直播。

采用H.265编码推流，比H.264流更省流量，或相同流量下，画面质量更高。

本插件支持**Intel**和**nvdia**平台的265硬编。

腾讯视频云会自动将H.265视频流转为H.264视频流，默认的播放地址是H.264视频流，要联系我们开启H.265播放配置才能得到H.265视频流播放地址。

推流地址无须特别设置。


#### 使用说明

**一. [下载](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/OBS_Plugins/tx265-plugin-setup.exe)插件安装** 

**需要OBS-Studio 20.0.0及以上版本**

![](https://main.qcloudimg.com/raw/98f69bbefe4e5efee58e609446a5ba6a.png)

目标文件夹：插件安装包会自动检测OBS studio安装的目录，检测失败需要手动选择OBS studio安装的目录



**二. 设置OBS推流参数**

OBS设置-流-流类型选择**Tencent Stream(H.265) Service**，填写推流地址

获取测试URL
[开通](https://console.cloud.tencent.com/live)直播服务后，可以使用 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 生成推流地址，详细信息可以参考 [获得推流播放URL](https://cloud.tencent.com/document/product/454/7915)。

![](https://main.qcloudimg.com/raw/81b7aaa96e7beb2744550360d3c1e1dd.png)

OBS设置-输出-输出模式-选择**高级**

OBS设置-输出-流-编码器-选择带**TX265开头的编码器**，并按需设置编码参数

![](https://main.qcloudimg.com/raw/da8c892c2c0cc5ac12c033d40163a2dd.png)


编码器名称|说明
-|-
TX265-Intel QuickSync HEVC Encoder | Intel平台265硬编
TX265-NVENC HEVC Encoder | nvdia平台265硬编
TX265-QQ265 HEVC Encoder|Tencent音视频实验室自研265软编
TX265-x265 HEVC Encoder|x265实现的265软编

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

**三. 配置腾讯视频云启用265播放**

腾讯视频云自动把265的流转为264播放流，要播放265流，需要联系我们启用265流播放配置，264的播放地址依然有效，适合无法正常播放265流的客户端
