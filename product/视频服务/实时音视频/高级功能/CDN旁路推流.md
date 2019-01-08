## 内容介绍

腾讯云实时音视频（TRTC）服务是专门面向1v1视频通话和多人视频会议的视频服务，在时延和流畅度上相比于常规直播服务有明显的优势，但它也有两个明显的短板：
- 价格较 CDN 直播服务偏贵
- 房间总人数限制为 1000 人

所以，如果要支持多人大房间的应用场景，更为了让带宽成本可控，可以使用 TRTC 的**旁路推流**功能，将 TRTC 音视频房间里的音视频流（经过混流转码）转推到腾讯云直播 CDN 上，从而获得高并发和低成本的观看能力。

![](https://main.qcloudimg.com/raw/f17148b48148aa50c430f2d83832060b.png)

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |    ✖     |   ✖     |


## 指定房间开启

### startCDNPublish

### stopCDNPublish

- **Objective-C**

``` Objective-C
- (void)startCDN {
    // 构造推流参数
    TRTCPublishCDNParam *cdnParam = [[TRTCPublishCDNParam alloc] init];
    cdnParam.appId = <#appId#>;
    cdnParam.bizId = <#bizId#>;
    cdnParam.url = @"<#rtmp推流url#>";
    // 这里不进行混流，如果需要将多路视频混为一个视频流，将enableTranscoding置为YES并参见"云端混流转码"进行配置
    cdnParam.enableTranscoding = NO;
    // 启动CDN旁路推
    [trtcCloud startPublishCDNStream:cdnParam];
}
```

- **Java**

``` java
//启动网络测速的示例代码

```

- **C++**

``` C++
//启动网络测速的示例代码

```


## 全局自动开启





