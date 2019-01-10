## 内容介绍

腾讯云实时音视频（TRTC）服务是专门面向1v1视频通话和多人视频会议的视频服务，在时延和流畅度上相比于常规直播服务有明显的优势，但它也有两个明显的短板：
- 价格较 CDN 直播服务偏贵
- 房间总人数限制为 1000 人以内

所以，如果要支持超过1000人的大房间应用场景，更为了让带宽成本可控，可以使用 TRTC 的**旁路直播**功能，将 TRTC 音视频房间里的音视频流（经过混流转码）转推到腾讯云直播 CDN 上，从而获得高并发和低成本的观看能力。

![](https://main.qcloudimg.com/raw/f17148b48148aa50c430f2d83832060b.png)

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |    ✖     |   ✖     |

## 全局自动开启

- 全局自动开启是指默认为房间里的每一路画面都配备一路对应的播放地址，但是画面之间相互独立，并没有进行混流。

- 在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**功能配置**页面里可以开启自动旁路推流。
![](https://main.qcloudimg.com/raw/91672da223a6eb7c24e8c9891018ead1.png)

- 开启此选项后，每一路画面都有一个对应的播放地址

## 指定房间开启

通过 TRTCCloud 的 `startPublishCDNStream` 可以将当前房间中的音视频流，转推到其参数 `TRTCPublishCDNParam` 指定的 URL 上，该方案支持将多路画面混合到同一路音视频流中。

### TRTCPublishCDNParam

| 参数字段 | 参数含义 | 备注说明 |
|---------|---------|---------|
| appId |  腾讯云直播 appid | 获取方式见下图 |
| bizId | 腾讯云直播 bizid | 获取方式见下图 |
| url | 转推的 rtmp url | 可以是非腾讯云地址，但只有腾讯云地址才不加收转推费用。 |
| enableTranscoding | 是否要开启混流转码 | 如果开启混流转码，腾讯云会对房间里的多路画面进行合并，如果不开启，则腾讯云仅转推当前调用者的画面 |

- **appid 和 bizid**
您可以在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**账号信息**页面看到这两个信息。
![](https://main.qcloudimg.com/raw/4bacb840b1ece10544f1f3414635fe7c.png)

 > 如果您看到上述区域的数值为空，说明您还没有开通直播服务，在腾讯云直播[控制台](https://console.cloud.tencent.com/live)开通直播服务即可。

- **url 的获取**
RTMP推流URL的获取，各家云服务商都有各自的方案，腾讯云的方案非常简单，您可以参考文档：[“快速获得推流地址”](https://cloud.tencent.com/document/product/267/7977) 或 [“后台自动拼装”](https://cloud.tencent.com/document/product/267/13457) 了解详情。

 > 这里的 url 是推流url，也就是只能用来推流不能用来播放，不过每一个推流url都有其对应的播放url。以腾讯云为例，您可以参考文档 [“直播码模式获取播放地址”](https://cloud.tencent.com/document/product/267/13484) 或 [“业务后台生成播放地址”](https://cloud.tencent.com/document/product/267/13485)，从而了解如何获取对应的播放URL。
 
- **enableTranscoding**
如果开启混流转码，您需要调用 TRTCCloud 的 `startCloudMixTranscoding` 对各路画面的摆放位置以及最终的画面质量进行配置，这里的配置方法需要您参考文档：[云端混流转码](https://cloud.tencent.com/document/product/647/16827)。

 > `startCloudMixTranscoding` 并不是在终端进行混流，而是将混流配置传输到云端，由云端进行混流和转码，所以不用担心这里的性能问题。

### 示例代码

- **Objective-C**

``` Objective-C
- (void)startCDN {
    // 构造推流参数
    TRTCPublishCDNParam *cdnParam = [[TRTCPublishCDNParam alloc] init];
    cdnParam.appId = <#appId#>;         //请填写您的直播appid
    cdnParam.bizId = <#bizId#>;         //请填写您的直播bizid
    cdnParam.url   = @"rtmp://xxxxxx";  //请填写您的推流url
    // 这里不进行混流，如果需要将多路视频混为一个视频流，将enableTranscoding置为YES并参见"云端混流转码"进行配置
    cdnParam.enableTranscoding = NO;
    // 启动CDN旁路推
    [trtcCloud startPublishCDNStream:cdnParam];
}
```

- **Java**

``` java
public void startCDN() {
    TRTCCloudDef.TRTCPublishCDNParam cdnParam = new TRTCCloudDef.TRTCPublishCDNParam();
    cdnParam.appId = <#appId#>;         //请填写您的直播appid
    cdnParam.bizId = <#bizId#>;         //请填写您的直播bizid
    cdnParam.url   = "rtmp://xxxxxx";   //请填写您的推流url
    // 这里不进行混流，如果需要将多路视频混为一个视频流，将enableTranscoding置为true并参见"云端混流转码"进行配置
    cdnParam.enableTranscoding = false;
    // 启动CDN旁路推
    trtcCloud.startPublishCDNStream(cdnParam);
}
```

- **C++**

``` c++
void startCDN()
{
    // 构造推流参数
    TRTCPublishCDNParam cdnParam;
    cdnParam.appId = <#appId#>;
    cdnParam.bizId = <#bizId#>;
    cdnParam.url = "<#rtmp推流url# >";
    // 这里不进行混流，如果需要将多路视频混为一个视频流，将enableTranscoding置为YES并参见"云端混流转码"进行配置
    cdnParam.enableTranscoding = false;
    // 启动CDN旁路推
    trtcCloud->startPublishCDNStream(cdnParam);
}
```

## 如何播放

在各种播放地址中，我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http-flv** 地址，该地址的播放具有时延低、秒开效果好且非常稳定可靠的特点。

播放器推荐使用已经打包在 TRTC SDK 里的 TXLivePlayer 播放器，该播放器的参考文档为：
- [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/454/7880)

- [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/454/7886)

- [TXLivePlayer(Windows)](https://cloud.tencent.com/document/product/454/13676#.E6.92.AD.E6.94.BE.E5.8A.9F.E8.83.BD)

## 注意事项
1. 视频通话期间请勿测试，以免影响通话质量
2. 测速本身会消耗一定的流量，所以也会产生极少量额外的流量费用（基本可以忽略）



