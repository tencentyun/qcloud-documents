## 方案背景
为降低客户接入门槛，TRTC 支持 RTMP 标准协议推流，在 PC 端推流时候，您可根据实际情况选择安装 [OBS](https://obsproject.com/download) 或 FFmpeg 进行推流。 OBS 是一款好用的第三方开源程序直播流媒体内容制作软件，为用户提供免费使用，它可支持 OS X、Windows、Linux 操作系统，适用多种直播场景，满足大部分直播行为的操作需求，您可以到 [OBS 官网下载](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 最新版本软件。

本功能目前免费开放内测中（后续若收费会提前通知），但接入的 RTMP 流会作为房间中的虚拟用户产生正常的通话费用，详情参见 [计费概述](https://cloud.tencent.com/document/product/647/17157)。如果您有需要可以联系页面右下方对话框 [售前在线咨询](https://cloud.tencent.com/online-service?source=PRESALE&from=doc_647)，提交工单申请加入白名单进行使用（需提供 SdkAppId）。


>! 不支持 RTMP 从 TRTC 拉流，如果需要旁路 CDN 直播观看，请参考 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826)。

## OBS 推流设置
### 准备工作[](id:ready)
安装并打开 [OBS](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 工具进行下述操作。

### 选择输入源[](id:step1)
查看底部工具栏的**来源**标签，单击**+**按钮，根据您的业务需要选择输入源。常用来源输入有：

| 输入源         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| 图像           | 适用于单张图像直播。                                         |
| 图像幻灯片放映 | 可循环或者顺序多张播放图片。                                 |
| 场景           | 实现各种强大的直播效果。此时，另一个场景是作为来源被添加进当前场景的，可以实现整个场景的插入。 |
| 媒体源         | 可上传本地视频，并本地点播视频文件进行直播化处理。           |
| 文本           | 实时添加文字在直播窗口中。                                   |
| 窗口捕获       | 可根据您选择的窗口进行实时捕获，直播仅显示您当前窗口内容，其他窗口不会进行直播捕获。 |
| 视频捕获设备   | 实时动态捕捉摄像设备，可将摄像后的画面进行直播。             |
| 音频输入捕获   | 用于音频直播活动（音频输入设备）。                           |
| 音频输出捕获   | 用于音频直播活动（音频输出设备）。                           |


![](https://main.qcloudimg.com/raw/c59eff44ffd2ac4c785fe4e4e3bd79b8.png)


### 设置推流参数[](id:step2)
1. 通过底部工具栏的 **控件>设置** 按钮进入设置界面。
![img](https://main.qcloudimg.com/raw/56e4c19f24d08df7b8f8815f1ffb6857.png)
2. 单击 **推流** 进入推流设置页签，选择服务类型为**自定义**。
3. 服务器填写：`rtmp://rtmp.rtc.qq.com/push/`。
4. 填写串流密钥格式如下：
```
房间号?sdkappid=应用&userid=用户名&usersig=签名
```
其中房间号、应用、用户名、签名需要换成业务的，例如：
```
22998?sdkappid=140*****66&userid=******rtmp2&usersig=eJw1jdE***************ZLgi5UAgOzoMhrayt*cjbmiCJ699T09juc833IMT94Ld7I0iHZqVDzvVAqkZsG-IKlzLiXOnEhswHu1iUyTc9pv*****D8MQwoA496Ke6U1ip4EAH4UMc5H9pSmv6MeTBWLamhwFnWRBZ8qKGRj8Yp-wVbv*mGMVZqS7w-mMDQL
```
	- 为简化参数，只支持字符串房间号，不超过64个字符，字符只能是数字、字母、下划线。TRTC 其他端如果要观看 RTMP 流，需要使用字符串房间号进房。
	- usersig 的生成规则，请参见 [UserSig 相关](https://cloud.tencent.com/document/product/647/17275) （**请注意签名要在有效期内**）。
	- 以上服务器地址 + 串流密钥组成 RTMP 推流地址，也可以供 FFmpeg 或其他 RTMP 库推流。
![](https://qcloudimg.tencent-cloud.cn/raw/fdd4696c30c19061189ced4c864e20ef.png)     


### 设置输出[](id:step3)
RTMP 后台不支持传输 B 帧，用户可以通过如下设置调整推流端软件的视频编码参数来去除 B 帧。
1. 在**设置**中单击**输出**页签进行配置。
2. 在**输出模式**中选择**高级**，**关键帧间隔建议填写1或2**，单击**确定**保存设置。

![](https://qcloudimg.tencent-cloud.cn/raw/6f331bf0f0299060470008acab20954a.png)  


### 设置视频选项[](id:step4)
在**设置**中单击**视频**页签，设置分辨率和帧率。分辨率决定了观众看到的画面清晰程度，分辨率越高画面越清晰。FPS 是视频帧率，它控制观看视频的流畅，普通视频帧率有24帧 - 30帧，低于16帧画面看起来有卡顿感，而游戏对帧率要求比较高，一般小于30帧游戏会显得不连贯。
![](https://qcloudimg.tencent-cloud.cn/raw/a67ecbbdf5e44c9316604bef3a20ca05.png)


### 高级选项[](id:step5)
- 建议不启用**串流延迟**以减少端到端延迟。
- 启动**自动重连**，建议设置**重试延迟**时长尽量短，网络抖动时如果连接断开可尽快重连上。
![](https://qcloudimg.tencent-cloud.cn/raw/f500c91d29963f7f772a084ccea2d930.png)


### 单击推流[](id:step6)
1. 查看 OBS 底部工具栏的 **控件**，单击 **开始推流**。
![](https://qcloudimg.tencent-cloud.cn/raw/22953d87c6a7cbfa34b9e7639507be37.png)
2. 推流成功后，正常情况在界面底部会展示推流状态，TRTC 控制台仪表盘上有该用户进房记录。
![](https://qcloudimg.tencent-cloud.cn/raw/a4b27551f991d73539bb5d2f834a4d38.png)

### 其他端观看[](id:step7)
如前面 [设置推流参数](#step2) 所说，TRTC 其他端进房需要使用字符串房间号，Web 端观看 RTMP 流的效果如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ae71beea5458b056697433acdbf6844e.png)

