## 推流

直播使用 DRM，在推流参数中添加 txDRMInfo 参数即可，示例如下：

```
 rtmp://xxx.livepush.myqcloud.com/live/test?bizid=1234&txDRMInfo=hls:fairplay,dash:widevine
```

Widevine 对应参数为 dash，Fairplay 对应参数为 hls，同一条直播流可同时使用多种 DRM 方案。

## 拉流

在流 id 后添加 .mpd（Widevine 方案）或 .m3u8（Fairplay 方案）即可拉取加密流，示例如下：

```
http://xxx.liveplay.myqcloud.com/test/test.mpd?bizid=1234
```
