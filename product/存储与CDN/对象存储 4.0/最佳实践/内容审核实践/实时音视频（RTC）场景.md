

## 概述

随着低延时的实时音视频技术越来越成熟，也吸引了越来越多的用户使用实时音视频产品开发实现自己的音视频业务。在拓展音视频业务的同时，如何更好的管控音视频内容避免违规尤为重要。

为更好的支持用户在各种业务场景下的内容安全风险，对象存储与数据万象在原有静态音视频审核的基础上，进一步提供了流式音视频的审核，当用户直播内容属于违规内容时，可以及时发现并进行处理。

以腾讯云实时音视频产品（Tencent Real-Time Communication，TRTC）为例，整体审核流程如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/d4aad5897e217133ee01da1399033126.png)

流程如下：

1. TRTC 客户端发起直播请求。
2. TRTC 服务端收到请求后进行直播。
3. 通过 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826) 可以拿到所需的直播流地址，有 rtmp、flv、hls 三种格式可用。
4. 使用万象直播流审核接口进行直播审核，SDK 封装此接口方便用户下载使用。
5. 客户拿到审核回调进行后续业务处理。

## 实践步骤

### 1. 创建存储桶
- 如果您已创建存储桶，可跳过该步骤。
- 如果您是首次使用 COS 控制台，可参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 进行操作。



### 2. 创建 TRTC 应用

如果您已创建 TRTC 应用，且能够使用 TRTC 相关功能时，可直接跳转到 [步骤4. 开启旁路推流](#4)。

（1）登录 [TRTC 控制台](https://console.cloud.tencent.com/trtc)，单击**应用管理**，可以看到应用列表，单击**创建应用**，相关说明可参见 [创建应用](https://cloud.tencent.com/document/product/647/50493)。
  ![](https://qcloudimg.tencent-cloud.cn/raw/136541b1d562d4f221ec9be857f61e78.png)
（2）创建应用后，单击右侧的**配置管理**，可以看到应用概览，其中 `SDKAppID`、`appid`、`bizid` 需要在后续流程中用到，可以先记录下来。
  ![](https://qcloudimg.tencent-cloud.cn/raw/65da6d2bd9fba3cdc18ffe4ce636135d.png)
（3）单击左侧导航栏的**快速上手**，能够看到签发 UserSig 的密钥信息，复制保存下来，待后续使用。
  ![](https://qcloudimg.tencent-cloud.cn/raw/c2f1d34a393b26884f2cb338e39518b9.png)
（4）完成以上步骤，我们已经知道了 `SDKAppID`、`appid`、`bizid`、`密钥` 这四个重要数据，切记不要泄漏这些数据。接下来可以开始对 TRTC DEMO 进行搭建了。



### 3. TRTC DEMO 搭建流程

本 DEMO 目的是使客户快速了解直播流程，客户业务需求的具体实现可参考 [TRTC 官网使用文档](https://cloud.tencent.com/document/product/647)。流程如下：

（1）下载所需平台的 [SDK&Demo 源码](https://console.cloud.tencent.com/trtc/helpcenter)，直接下载 ZIP 包即可，本次示例使用的是 Android 平台。
![](https://qcloudimg.tencent-cloud.cn/raw/4b0b6b3a718ed47f87da912d4e27e128.png)
（2）配置 TRTC-API-Example 工程文件。找到并打开 `LiteAVSDK_TRTC_Android 版本号/TRTC-API-Example/Debug/src/main/java/com/tencent/trtc/debug/GenerateTestUserSig.java` 文件。设置 `GenerateTestUserSig.java` 文件中的相关参数：
 - SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
 - SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。
 - BIZID：默认为 PLACEHOLDER ，请设置为实际的 bizid。
 - APPID：默认为 PLACEHOLDER ，请设置为实际的 appid。
<img style="width:518px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4fbf3547ccb1ed2f60b8fd89c0ce236e.png" />
（3）编译运行。使用 Android Studio（3.5及以上的版本）打开源码工程 TRTC-API-Example，单击<strong>运行</strong>即可。运行成功后页面如下图所示，TRTC DEMO 提供视频通话、录屏直播等多种功能示例。<br>
<img style="width:518px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/39e35346a1072f30e6736800ba1c0159.png" />


[](id:4)

### 4. 开启旁路推流

（1）登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
（2）在左侧导航栏选择**应用管理**，单击目标应用右侧的**功能配置**。
（3）在**旁路转推配置**中，单击**开启旁路转推**右侧的![img](https://main.qcloudimg.com/raw/5f58afe211aa033037e5c0b793023b49.png)，在弹出的**开启旁路转推功能**对话框中，单击**开启旁路转推功能**即可开通。
![](https://qcloudimg.tencent-cloud.cn/raw/eace3daf2690b61e0d493a1f1846b0a2.png)



### 5. 云直播 CDN 拉流

可以通过 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826) 获取到直播流数据，最后生成一条直播流地址，有 rtmp、flv、hls 三种协议可用。若使系统指定 streamId，可以根据文档内 `streamId` 定位到房间号、用户 ID 等直播信息。

- SDKAppID：您可以在 [TRTC 控制台](https://console.cloud.tencent.com/trtc/app) > **应用管理** > **应用信息**中获取。
- bizid：您可以在 [TRTC 控制台](https://console.cloud.tencent.com/trtc/app) > **应用管理** > **应用信息**中获取。
- roomId：由您在 `enterRoom` 函数的参数 `TRTCParams` 中指定。
- userId：由您在 `enterRoom` 函数的参数 `TRTCParams` 中指定。
- streamType： 摄像头画面为 main，屏幕分享为 aux（WebRTC 由于同时只支持一路上行，因此 WebRTC 上屏幕分享的流类型是 main）。

此时您可以得到直播流地址，三种协议可选：

```
rtmp 协议的播放地址：rtmp://live.myhost.com/live/streamd1001
flv 协议的播放地址：http://live.myhost.com/live/streamd1001.flv
hls 协议的播放地址：http://live.myhost.com/live/streamd1001.m3u8
```



### 6. 调用审核接口

获取到直播流后，使用万象的直播流审核接口进行直播审核，审核配置目前无法自主配置，您可以根据业务场景提供例如截帧频率、审核场景等信息，由技术人员在后台配置。

- 直播流审核可使用对应语言的 [COS SDK](https://cloud.tencent.com/document/product/436/6474)。
- 直播审核参数说明，请参见 [提交直播审核任务](https://cloud.tencent.com/document/product/436/76260)。
- 直播审核回调内容，请参见 [直播审核回调内容](https://cloud.tencent.com/document/product/436/76267)。

提交审核时可以设置客户业务信息，审核回调时会原样返回，拿到审核回调后可以得到具体房间或具体用户的违规情况。相关参数说明，请参见 [UserInfo 节点说明](https://cloud.tencent.com/document/product/436/76260#.E8.AF.B7.E6.B1.82)。

### 7. 违规解散房间或踢用户

收到回调后判断是否违规，发现违规后发起解散房间或移出用户等处置操作。API 文档指引如下：

- [移出用户](https://cloud.tencent.com/document/product/647/40496)
- [解散房间](https://cloud.tencent.com/document/product/647/50089)

TRTC 相关 API 接口可使用 API 文档页面提供的 SDK。

### 8. 费用相关
在本次实践操作过程中涉及到的费用如下：
- [音视频时长计费说明](https://cloud.tencent.com/document/product/647/44248)
- [CDN 拉流费用](https://cloud.tencent.com/document/product/267/34175)
- [云端混流转码费用](https://cloud.tencent.com/document/product/647/49446)
- [对象存储相关费用](https://cloud.tencent.com/document/product/436/53482)
