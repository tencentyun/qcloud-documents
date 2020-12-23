## 功能描述

GET LiveChannel - status 接口用于获取指定通道（Live Channel）的当前推流状态。

## 请求

#### 请求示例

```plaintext
GET /<ChannelName>?live&comp=status HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String

```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数
此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

响应体示例如下：

``` plaintext
<LiveChannelStatus>
  <Status>Live</Status>
  <ConnectedTime>2016-08-25T06:25:15.000Z</ConnectedTime>
  <RemoteAddr>127.0.0.1:47745</RemoteAddr>
  <RequestId>NWZjMzUyM2NfNWNhM2IwYV8xOTYyX2Mz****</RequestId>
  <Video>
    <Width>1280</Width>
    <Height>720</Height>
    <FrameRate>24</FrameRate>
    <Bandwidth>71510</Bandwidth>
    <Codec>H264</Codec>
  </Video>
  <Audio>
    <Bandwidth>13308</Bandwidth>
    <SampleRate>48000</SampleRate>
    <Codec>AAC</Codec>
  </Audio>
</LiveChannelStatus>
```

该请求返回的响应体节点描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型       |
| ------------------ | ----------------- | ------------------------------------------------------------ | ---------- |
| LiveChannelStatus  | 无                | 保存 GetLiveChannelStatus 返回结果的容器                       | Container  |
| Status             | LiveChannelStatus | 通道当前的推流状态，有效值：Live，Idle                    | EnumString |
| ConnnectedTime     | LiveChannelStatus | 当 Status 为 Live 时，表示当前客户端开始推流的时间。使用 ISO8601格式 | EnumString |
| RemoteAddr         | LiveChannelStatus | 当 Status 为 Live 时，表示当前推流客户端的 IP 地址                 | Container  |
| RequestId          | LiveChannelStatus | 当 Status 为 Live 时，表示当前推流请求的 RequestId                | String     |
| Video              | LiveChannelStatus | 当 Status 为 Live 时，保存视频流信息的容器。<br/>说明：Video、Audio 容器只有在 Status 为 Live 时才会返回，但 Status 为 Live 时不一定返回这两个容器。例如，客户端已经连接到 LiveChannel，但尚未发送音视频数据，这种情况不会返回这两个容器 | Container  |
| Width              | Video             | 当前视频流的画面宽度，单位：像素                             | String     |
| Heigth             | Video             | 当前视频流的画面高度，单位：像素                             | String     |
| FrameRate          | Video             | 当前视频流的帧率                                             | String     |
| Bandwidth          | Video             | 当前视频流的码率，单位：B/s                               | String     |
| Codec              | Video             | 当前视频流的编码格式                                         | EnumString |
| Audio              | LiveChannelStatus | 当 Status 为 Live 时，保存音频流信息的容器。<br/>说明：Video、Audio 容器只有在 Status 为 Live 时才会返回，但 Status 为 Live 时不一定返回这两个容器。例如，客户端已经连接到 LiveChannel，但尚未发送音视频数据，这种情况不会返回这两个容器 | Container  |
| SampleRate         | Audio             | 当前音频流的采样率                                           | String     |
| Bandwidth          | Audio             | 当前音频流的码率，单位：B/s                               | String     |
| Codec              | Audio             | 当前音频流的编码格式                                         | String     |



#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：无推流时推道处于 Idle 状态

#### 请求

```plaintext
GET /test-channel?live&comp=status HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2020 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
 
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelStat>
  <Status>Idle</Status>
</LiveChannelStat>
```

#### 案例二：有推流时推道处于 Live 状态

#### 请求

```plaintext
GET /test-channel?live&comp=status HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2020 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
 
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelStatus>
  <Status>Live</Status>
  <ConnectedTime>2016-08-25T06:25:15.000Z</ConnectedTime>
  <RemoteAddr>127.0.0.1:47745</RemoteAddr>
  <RequestId>NWZjMzUyM2NfNWNhM2IwYV8xOTYyX2Mz****</RequestId>
  <Video>
    <Width>1280</Width>
    <Height>720</Height>
    <FrameRate>24</FrameRate>
    <Bandwidth>71510</Bandwidth>
    <Codec>H264</Codec>
  </Video>
  <Audio>
    <Bandwidth>13308</Bandwidth>
    <SampleRate>48000</SampleRate>
    <Codec>AAC</Codec>
  </Audio>
</LiveChannelStatus>
```

