## PC直播简介

![](//mc.qcloudimg.com/static/img/f47bf4ef0fcb96bdccf6f302b274afce/image.png)

腾讯云PC直播是在PC（**windows/mac**）上借助安装的推流软件 **OBS（推荐）**或者 **XSplit**，向腾讯**视频云**的**推流地址**，推送经过压缩编码**现场活动**、**教学**、**投影**或者**游戏**等画面。同时观众可以通过和推流地址相对应的播放地址收看**实时画面**。


## PC直播流程
PC直播流程非常简单，主要步骤：
- 从腾讯云直播控制台获取一个**推流地址**和3个播放地址，解决**往哪推流**的问题。
- 采用第三方的推流软件，设置推流音视频源以及编码参数，解决推什么**内容**的问题。
- 观众就可以使用我们提供的RTMP DEMO通过设置播放地址即可进行观看。解决内容**触达到观众**那里的问题。

![](//mc.qcloudimg.com/static/img/617e7cc6ae3313a2456e2672535e4097/image.png)


## 1. 直播前准备
- 在腾讯云开通云直播服务
如果您尚未开通，单击这里[申请开通](https://console.cloud.tencent.com/live)云直播服务。
![](//mc.qcloudimg.com/static/img/f45715687e787ee9a8e18154d1e13b92/image.png)

### 1.2 生成推流地址
如何您尚未准备好**推流地址**，单击这里[接入管理 >> 直播码接入 >>推流生成器](https://console.cloud.tencent.com/live)生成一个**推流地址**和三个播放地址。

其中，域名为 **livepush.myqcloud.com** 的即为推流地址：
![](//mc.qcloudimg.com/static/img/98b9b659be67a9ac32384b606ace943f/image.png)

### 1.3 准备好直播用的网络
- **网络选择**

|网络类型|方便性|稳定性|
|--|--|--|
|有线网|差|好|
|WIFI|好|差|
条件容许建议用有线网络，相对WIFI比较稳定，信号不容易受到干扰。如果是活动直播建议WIFI，更加便捷。

- **上行带宽测量**
对于上行带宽的要求，视视频质量，分辨率而定。一般视频质量越好，分辨率越高，对上行带宽的要求，就越高。建议上行带宽不低于1Mbps。如何知道当前网络的上行带宽情况呢？推荐使用[speedtest](http://www.speedtest.net/)测试一下。
![](//mc.qcloudimg.com/static/img/b5724af9873220c395e295894205e4ad/image.png)

### 1.4 安装推流软件
- **OBS安装**
去[OBS官网](https://obsproject.com/download)，下载相应的安装包，按照默认设置进行安装。OBS支持 Windows/Mac/Linux等系统。确认是Open Broadcaster Software。OBS也提供OBS Studio，不是本文介绍的软件。
![](//mc.qcloudimg.com/static/img/dcbb929e364b1d8e80c04e326a756a26/image.png)

- **XSplit安装**
去[XSplit官网](https://www.xsplit.com/zh_cn/)，下载安装包，安装默认设置进行安装。
XSplit是收费的，如果银子不够的话，推荐用OBS（**Free**）。XSplit游戏直播有单独的安装包，非游戏直播推荐使用 BroadCaster。
![](//mc.qcloudimg.com/static/img/18c47cb7646e189acc168e6a5e8e4714/image.png)

## 2. 软件参数设置
### 2.1 设置推流地址
假设准备好的推流地址为:
> rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

设置时会分为前后两部分进行设置:
> 其中推流地址前半部分 **“rtmp://3891.livepush.myqcloud.com/live/”** 一般被称为 **FMS URL**
> 推流地址的后半部分**“3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F”**一般被称为**串流码**。

- **OBS推流地址设置**
![](//mc.qcloudimg.com/static/img/8f5dabbdea9882531464017385648e0c/image.png)
单击**设定** 选中 **广播设定**，依次配置模式为**直播流**、串流服务为**Custom**、FMS URL为推流地址的前半部分、播放路径/串码流为推流地址的后半部分。自动重连是在OBS检测到网络断开等异常情况，自动触发推流连接操作，建议勾选。
![](//mc.qcloudimg.com/static/img/88024aaff126c5e34f4e96b9cd7e37c2/image.png)

- **OBS Studio推流地址设置**
![](//mc.qcloudimg.com/static/img/023f599e7fe3e22a8d348a6b4b7b0720/image.png)
单击界面右下角**设置**选中**串流**，依次配置串流类型为**自定义流媒体服务器**、URL为推流地址的前半部分、流密钥为推流地址的后半部分。

### 2.2 设置音视频源
音视频源相当于您要投递的包裹的内容。内容形式主要有三种:
- 来自视频采集设备，如camera 或者是专业的录像设备等。
- 来自PC窗口或者游戏源。
- 来自存放在PC上的视频图片等媒体文件。

- **OBS 音视频源设置**
**特别提醒**：在来源框中**单击鼠标右键**，左键是没有反应的。弹出添加菜单，随后弹出**获取窗口**、显示器获取、图片源、投影片放映、文字来源、CLR Browser、 **视频捕捉设备**、游戏源等。其中获取窗口和视频捕捉设备两项比较常用。不用的来源，相应的设置就不太一样。接下来主要介绍 **视频捕捉设备** 的设置。
![](//mc.qcloudimg.com/static/img/c2f5a64918807e99aad4bd7778259e62/image.png)
![](//mc.qcloudimg.com/static/img/6f15746021918db02fbaefa6dc56c22b/image.png)
![](//mc.qcloudimg.com/static/img/d60b1a9c246d381a5e698bafac8c3f4e/image.png)

- **OBS Studio音视频源设置**
参考**OBS 音视频源设置**。

### 2.3 设置音视频格式
设置好视频来源后，虽然能够获取音视频信号，但是原始的音视频信号对带宽的需求过大不适合在网络上传播。因此直播前最重要一步，就是要设置音视频编码参数。

| 设置项 | 功能案例 | 
|:--------:|---------|
|**x264**|工业界使用最为广泛的h264编码器，在同等画质下有更高的视频压缩比，**建议勾选**。|
|Nvidia NVENC|采用nv显卡专用的视频处理核心来编码。需要Nvidia显卡的支持。|
|Quick Sync|是采用英特尔快速视频同步技术，硬件编码，编码速度和画质都较好，但<font color='red'>兼容性差</font>、码率高。|
|**CBR**|视频编码码率控制模式之一，称为固定输出码率控制。稳定的码率更加适合网络的传输，**建议勾选**。|
| **AAC** | 目前最流行的直播音频编码格式，**建议勾选**。|

- **OBS 音视频格式设置**
![](//mc.qcloudimg.com/static/img/eb91f2e51ca3b3d8c39028262b4eae21/image.png)

- **OBS Studio音视频格式设置**
![](//mc.qcloudimg.com/static/img/1d473aed08fcdc7611d8de599184e75c/image.png)
![](//mc.qcloudimg.com/static/img/baa533b47d920f70ca08b12771ee3158/image.png)

## 3. 播放验证

### 3.1 确认播放地址
如果推理地址（livepush）为：
> rtmp://3891.**<font color='blue'>livepush</font>**.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

那么播放地址（liveplay）即：

| 播放协议 | 播放地址 | 
|---------|---------|
| FLV |  `rtmp://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test` |
| RTMP | `http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.flv` |
| HLS(m3u8) | `http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.m3u8` |


### 3.2 RTMP DEMO 播放验证
[下载](https://cloud.tencent.com/document/product/454/6555) RTMP DEMO，将播放地址用在线二维码[生成器](http://cli.im/)生成二维码后，即可扫码播放。

### 3.3 VLC 播放验证
[VLC下载地址](http://www.videolan.org/vlc/)，安装按照默认设置即可。打开后单击**媒体菜单**，选择**打开网络串流**，填写播放地址，单击**播放**。
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)



