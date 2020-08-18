
##  前提条件

* 在 IoT Video 平台创建产品，开发产品。
* 在 AWS 平台注册、审核。
* 在 AWS 平台创建并配置 skill。
* 开发者需实现和部署 OAuth2 服务。

## Alexa 连接设备工作流程

Alexa 支持 RTSP 流媒体，下图是用户通过语言控制 Alexa EchoShow 连接 IoT Video 设备，查看实时监控视频的工作流程。

```
sequenceDiagram
participant E  as Alexa EchoShow
participant A  as Alexa Cloud
participant W  as Lambda(开发者实现)
participant IW as IoT Video API
participant D  as 设备
participant R  as IoT Video流媒体服务器

E->>A:   1.1 用户语音控制指令
A->>W:   1.2 InitializeCameraStreams directive
W->>IW:  1.3 请求设备直播流地址(RTSP)
IW->>IW: 1.4 分配流媒体转发资源
IW->>D:  1.5 通知设备推流
IW-->>W: 1.6 返回RTSP直播流地址
W-->>A:  1.7 InitializeCameraStreams response
A-->>E:  1.8 返回
D->>R:   2.1 RTSP推流(开发者实现)
E->>R:   2.2 RTSP拉流
```


## Lambda 开发

开发者需要开发 Lambda 实现对接，在 Lambda 中调用 IoT Video 平台的 [请求设备直播流地址](https://note.youdao.com/share/?token=FA4CBB102AB44CADBC344B5158D13C27&gid=108651055) 接口，将获取到的 RTSP 地址及参数，封装到`Alexa.CameraStreamController.Response`结构中。

参见 [Alexa 开发文档](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-camerastreamcontroller.html)。

## 设备端开发

开发者应在设备端实现 RTSP 推流功能。

设备端 SDK 提供 **RTSP 推流通知**的应用层接口,应用层通过此接口获取 RTSP 推流地址，启动 RTSP 推流。此推流地址具有时效性，过期后云端会自动断开相应流媒体传输过程。

## 约束及限制

* Alexa 目前不支持 H265/HEVC 的视频编码格式，开发者实现 RTSP 推流时，应确定使用正确的音视频编码格式；
* IoT Video 平台提供直播流媒体转发功能，平台限定每次设备推流的最大有效时长为1分钟，超过该时间。相应流媒体地址失效。
