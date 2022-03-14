TS over SRT 推流通过 **SRT 协议**直接传输包含音视频数据的 ts 流，下行复用了现有直播系统。TS over SRT 已作为 Haivision 硬件及 OBS 的推流格式标准。
此种模式下，SRT 服务器会解析负载（TS），并转封装为 RTMP 协议，转推到后端 RTMP 服务器。
![](https://main.qcloudimg.com/raw/5ceb4e1d0d3a2e1f07bb601d17d04eb5.png)

>! 上行选用了 SRT 推流协议并不会增加成本。

## 上行卡顿率对比
在使用 SRT 推流后，可以明显的看到卡顿率有所改善，如下质量对比图所示：
![](https://main.qcloudimg.com/raw/8c55654a4d4050092f98a88b21949e4f.png)


## 推流丢包率对比
下行方面，在应用 SRT 推流后由于上行质量的优化，下行流畅度也得到相应的提升。以下为斗鱼 App 实际对比效果。
- Android 平台 SRT 推流性能测试数据（测试平台—MI9）：
![](https://main.qcloudimg.com/raw/91d7a0a3ba846ce2cb92415e4b096b16.png)
- iOS 平台 SRT 推流性能测试数据（测试平台—iphone XR）：
![](https://main.qcloudimg.com/raw/5104e085e29b7bea3b955407086ed342.png)



## 抗丢包对比
在传输质量指标上，与 QUIC 做了对比。SRT 通过更精准和快速的重传控制，以及针对直播流媒体场景的 Pacing 机制，使得在相同丢包率下，应用层丢包较少。当丢包率在 50%时，SRT 相比 QUIC 仍能保证稳定的传输。

和 QUIC 上行对比，在推流端相同链路同一直播文件的情况下，每5分钟提高了5%的丢包率，通过以下示图可以看出 SRT 的推流帧率更平稳。
![](https://main.qcloudimg.com/raw/aa34e85a1751ed5e9c1f0547fcf9c03a.png)

## 直播推流
### 接入方法
直播推流支持 SRT 协议，需使用**9000端口**进行推流。推流地址可以在云直播控制台的 **[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)** 中 [生成推流地址](https://cloud.tencent.com/document/product/267/35257#push) 然后在按照以下规则拼接即可。

腾讯云 SRT 推流 URL：
```
srt://${rtmp-push-domain}:9000?streamid=#!::h=${rtmp-push-domain},r=${app}/${stream},txSecret=${txSecret},txTime=${txTime}
```

>!  `${app}` 表示内容可变,实际填写不需要`$`、`{`、`}` 这3个字符。

### 实现方法
SRT 服务器会将 TS 转封装为 RTMP，并转推到 `${rtmp-push-domain}域名`。
OBS 推流码填写示例：
![](https://main.qcloudimg.com/raw/d0257df71d0905036eeb0779bcbd74f9.png)

>! 若您需使用 SRT 协议推流，OBS 版本不能低于 25.0。


## 直播拉流
按照正常拉流播放流程操作即可，具体请参见 [直播播放](https://cloud.tencent.com/document/product/267/32733)。



