数字版权管理解决方案（Digital Rights Management，DRM）通过技术手段加密内容，以控制带版权作品的使用、更改和分发，保护带版权内容的安全。适用于音乐、电影等带版权的多媒体内容。

直播 DRM 方案提供了从直播流加密、CDN 加速到许可证生成的一站式服务。

![](https://main.qcloudimg.com/raw/aa42e43282601e2f58b99389f3578346.svg)

## 操作步骤

### 使用 Widevine 方案

1. 在推流参数中，增加 WideVine DRM 参数，详细操作请参见 [直播 DRM 推拉流](#DRM)。
2. 搭建业务鉴权服务。

### 使用 Fairplay 方案

1. 提交 SDK 材料至腾讯云。
2. 在推流参数中，增加 Fairplay DRM 参数，详细操作请参见 [直播 DRM 推拉流](#DRM)。
3. 搭建业务鉴权服务。

[](id:DRM)
## 直播 DRM 推拉流
[](id:push)
### 推流
直播使用 DRM，在推流参数中添加 txDRMInfo 参数即可，示例如下：

```
 rtmp://xxx.livepush.myqcloud.com/live/test?bizid=1234&txDRMInfo=hls:fairplay,dash:widevine
```

Widevine 对应参数为 dash，Fairplay 对应参数为 hls，同一条直播流可同时使用多种 DRM 方案。

[](id:play)
### 拉流
在流 ID 后添加 `.mpd`（Widevine 方案）或 `.m3u8`（Fairplay 方案）即可拉取加密流，示例如下：
```
http://xxx.liveplay.myqcloud.com/test/test.mpd?bizid=1234
```

>! 华为手机调用 DRM 参数存在兼容性问题，建议用户避免此操作。

