
##  前提条件

* 在 IoT Video（Consumer Version） 平台 [创建产品](https://cloud.tencent.com/document/product/1131/42177)，开发产品。
* 在 AWS 平台注册、审核。
* 在 AWS 平台创建并配置 skill。
* 开发者需实现和部署 OAuth2 服务。

## Alexa 连接设备工作流程

Alexa 支持 RTSP 流媒体，下图是用户通过语言控制 Alexa EchoShow 连接 IoT Video（Consumer Version） 设备，查看实时监控视频的工作流程。
![](https://main.qcloudimg.com/raw/d23668cfa628c13f941fa3852ec0815e.jpg)


## Lambda 开发

开发者需要开发 Lambda 实现对接，在 Lambda 中调用 IoT Video（Consumer Version） 平台的请求设备直播流地址接口，将获取到的 RTSP 地址及参数，封装到`Alexa.CameraStreamController.Response`结构中。

详情请参见 [Alexa 开发文档](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-camerastreamcontroller.html)。

## 设备端开发

开发者应在设备端实现 RTSP 推流功能。

设备端 SDK 提供 **RTSP 推流通知**的应用层接口，应用层通过此接口获取 RTSP 推流地址，启动 RTSP 推流。此推流地址具有时效性，过期后云端会自动断开相应流媒体传输过程。

## 约束及限制

* Alexa 目前不支持 H265/HEVC 视频编码格式，开发者实现 RTSP 推流时，应确定使用正确的音视频编码格式，例如：H264。
* IoT Video（Consumer Version） 平台提供直播流媒体转发功能，平台限定每次设备推流的最大有效时长为1分钟，超过该时间，相应流媒体地址失效。

