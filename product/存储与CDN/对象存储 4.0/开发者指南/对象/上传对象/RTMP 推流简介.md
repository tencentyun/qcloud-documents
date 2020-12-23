## 简介

腾讯云对象存储服务 COS 提供 RTMP 协议接口，可以直接将视频、音频内容推送至客户指定的 COS 存储桶中，并转存为指定格式的文件。

在推流前，需要调用 COS 提供的 HTTP 形式的 LiveChannel 接口，提前创建一个通道并获取对象的推流地址。

此外，COS 还提供丰富的查询、管理以及点播等 LiveChannel 接口，以方便您使用、管理、分享 COS 中的音视频内容。


## 适用场景

适用于家庭监控、安防监控等音视频推流上传场景。


## 使用方法

#### 使用 REST API

您可以直接使用 REST API 使用 LiveChannel 接口，具体可参考以下 API 文档：

- [PUT LiveChannel](https://cloud.tencent.com/document/product/436/50887)
- [List LiveChannels](https://cloud.tencent.com/document/product/436/50886)
- [DELETE LiveChannel](https://cloud.tencent.com/document/product/436/50889)



## 限制说明



- 只能使用 RTMP 协议进行推流，不支持 RTMP 协议的拉流功能。
- 必须包含视频流，且视频流格式为 H.264。
- 音频流可选，只支持 AAC 格式，其他格式的音频流会被丢弃。
- 转储只支持 HLS 协议。
- 一个通道在同一时刻只能被一个客户端推流。
