## 功能描述
GetMediainfo 接口用于获取媒体文件的信息。

## 请求

#### 请求示例

```shell
GET /for-test.mp4?ci-process=videoinfo HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/) 文档）

#### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求体
该请求无请求体。

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                           | 类型   | 必选 |
| :----------------- | :----- | :----------------------------- | :----- | :--- |
| ci-process         | 无     | 操作类型，固定使用 videoinfo | String | 是   |

## 响应

#### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/) 文档。

#### 特有响应头
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <MediaInfo>
    <Stream>
      <Video>
        <Index></Index>
        <CodecName></CodecName>
        <CodecLongName></CodecLongName>
        <CodecTimeBase></CodecTimeBase>
        <CodecTagString></CodecTagString>
        <CodecTag></CodecTag>
        <Profile></Profile>
        <Width></Width>
        <Height></Height>
        <HasBFrame></HasBFrame>
        <RefFrames></RefFrames>
        <Sar></Sar>
        <Dar></Dar>
        <PixFormat></PixFormat>
        <FieldOrder></FieldOrder>
        <Level></Level>
        <Fps></Fps>
        <AvgFps></AvgFps>
        <Timebase></Timebase>
        <StartTime></StartTime>
        <Duration></Duration>
        <Bitrate></Bitrate>
        <NumFrames></NumFrames>
        <Language></Language>
      </Video>
      <Audio>
        <Index></Index>
        <CodecName></CodecName>
        <CodecLongName></CodecLongName>
        <CodecTimeBase></CodecTimeBase>
        <CodecTagString></CodecTagString>
        <CodecTag></CodecTag>
        <SampleFmt></SampleFmt>
        <SampleRate></SampleRate>
        <Channel></Channel>
        <ChannelLayout></ChannelLayout>
        <Timebase></Timebase>
        <StartTime></StartTime>
        <Duration></Duration>
        <Bitrate></Bitrate>
        <Language></Language>
      </Audio>
      <Subtitle>
        <Index></Index>
        <Language></Language>
      </Subtitle>
    </Stream>
    <Format>
      <NumStream></NumStream>
      <NumProgram></NumProgram>
      <FormatName></FormatName>
      <FormatLongName></FormatLongName>
      <StartTime></StartTime>
      <Duration></Duration>
      <Bitrate></Bitrate>
      <Size></Size>
    </Format>
  </MediaInfo>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| MediaInfo | Response | 媒体的详细信息 |  Container |

Container 节点 MediaInfo 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Stream | Response.MediaInfo | 流信息 |  Container |
| Format | Response.MediaInfo | 格式信息 |  Container |

Container 节点 Stream 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Video | Response.MediaInfo.<br>Stream | 视频信息 |  Container |
| Audio | Response.MediaInfo.<br>Stream | 音频信息 |  Container |
| Subtitle | Response.MediaInfo.<br>Stream | 字幕信息 |  Container |

Container 节点 Format 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| NumStream | Response.MediaInfo.<br>Format | Stream（包含 Video、Audio、Subtitle）的数量 |  Int |
| NumProgram | Response.MediaInfo.<br>Format | 节目的数量 |  Int |
| FormatName | Response.MediaInfo.<br>Format | 容器格式名字 |  String |
| FormatLongName | Response.<br>MediaInfo.Format | 容器格式的详细名字 |  String |
| StartTime | Response.MediaInfo.<br>Format | 起始时间，单位为秒 |  Float |
| Duration | Response.MediaInfo.<br>Format | 时长，单位为秒 |  Float |
| Bitrate | Response.MediaInfo.<br>Format | 比特率，单位为 kbps |  Int |
| Size | Response.MediaInfo.<br>Format | 大小，单位为 Byte |  Int |

Container 节点 Video 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Index | Response.MediaInfo.<br>Stream.Video | 该流的编号 |  Int |
| CodecName | Response.MediaInfo.<br>Stream.Video | 编解码格式名字 |  String |
| CodecLongName | Response.MediaInfo.<br>Stream.Video | 编解码格式的详细名字 |  String |
| CodecTimeBase | Response.MediaInfo.<br>Stream.Video | 编码时基 |  String |
| CodecTagString | Response.MediaInfo.<br>Stream.Video | 编码标签名 |  String |
| CodecTag | Response.MediaInfo.<br>Stream.Video | 编码标签 |  String |
| Profile | Response.MediaInfo.<br>Stream.Video | 视频编码档位 |  String |
| Height | Response.MediaInfo.<br>Stream.Video | 视频高 |  Int |
| Width | Response.MediaInfo.<br>Stream.Video | 视频宽 | Int |
| HasBFrame | Response.MediaInfo.<br>Stream.Video | 是否有B帧 |  Int |
| RefFrames | Response.MediaInfo.<br>Stream.Video | 视频编码的参考帧个数 |  Int |
| Sar | Response.MediaInfo.<br>Stream.Video | 采样宽高比 |  String |
| Dar | Response.MediaInfo.<br>Stream.Video | 显示宽高比 |  String |
| PixFormat | Response.MediaInfo.<br>Stream.Video | 像素格式 |  String |
| FieldOrder | Response.MediaInfo.<br>Stream.Video | 场的顺序 |  String |
| Level | Response.MediaInfo.<br>Stream.Video | 视频编码等级 |  Int |
| Fps | Response.MediaInfo.<br>Stream.Video | 视频帧率 |  Int |
| AvgFps | Response.MediaInfo.<br>Stream.Video | 平均帧率 |  String |
| Timebase | Response.MediaInfo.<br>Stream.Video | 时基 |  String |
| StartTime | Response.MediaInfo.<br>Stream.Video | 视频开始时间，单位为秒 |  Float |
| Duration | Response.MediaInfo.<br>Stream.Video | 视频时长，单位为秒 |  Float |
| Bitrate | Response.MediaInfo.<br>Stream.Video | 比特率，单位为 kbps |  Float |
| NumFrames | Response.MediaInfo.<br>Stream.Video | 总帧数 |  Int |
| Language | Response.MediaInfo.<br>Stream.Video | 语言 |  String |

Container 节点 Audio 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Index | Response.MediaInfo.<br>Stream.Audio | 该流的编号 |  Int |
| CodecName | Response.MediaInfo.<br>Stream.Audio | 编解码格式名字 |  String |
| CodecLongName | Response.MediaInfo.<br>Stream.Audio | 编解码格式的详细名字 |  String |
| CodecTimeBase | Response.MediaInfo.<br>Stream.Audio | 编码时基 |  String |
| CodecTagString | Response.MediaInfo.<br>Stream.Audio | 编码标签名 |  String |
| CodecTag | Response.MediaInfo.<br>Stream.Audio | 编码标签 |  String |
| SampleFmt | Response.MediaInfo.<br>Stream.Audio | 采样格式 |  String |
| SampleRate | Response.MediaInfo.<br>Stream.Audio | 采样率 |  Int |
| Channel | Response.MediaInfo.<br>Stream.Audio | 通道数量 |  Int |
| ChannelLayout | Response.MediaInfo.<br>Stream.Audio | 通道格式 |  String |
| Timebase | Response.MediaInfo.<br>Stream.Audio | 时基 |  String |
| StartTime | Response.MediaInfo.<br>Stream.Audio | 音频开始时间，单位秒 |  Float |
| Duration | Response.MediaInfo.<br>Stream.Audio | 音频时长，单位秒 |  Float |
| Bitrate | Response.MediaInfo.<br>Stream.Audio | 比特率，单位 kbps |  Float |
| Language | Response.MediaInfo.<br>Stream.Audio | 语言 |  String |

Container 节点 Subtitle 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Index | Response.MediaInfo.<br>Stream.Subtitle | 该流的编号 |  Int |
| Language | Response.MediaInfo.<br>Stream.Subtitle | 语言 |  String |

#### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/) 文档。


## 实际案例

#### 请求

```shell
GET /for-test.mp4?ci-process=videoinfo HTTP/1.1
Host: bucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfG****-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b4****
Content-Length: 0
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

<Response>
        <MediaInfo>
                <Format>
                        <Bitrate>1014.950000</Bitrate>
                        <Duration>10.125000</Duration>
                        <FormatLongName>QuickTime / MOV</FormatLongName>
                        <FormatName>mov,mp4,m4a,3gp,3g2,mj2</FormatName>
                        <NumProgram>0</NumProgram>
                        <NumStream>2</NumStream>
                        <Size>1284547</Size>
                        <StartTime>0.000000</StartTime>
                </Format>
                <Stream>
                        <Audio>
                                <Bitrate>70.451000</Bitrate>
                                <Channel>1</Channel>
                                <ChannelLayout>mono</ChannelLayout>
                                <CodecLongName>AAC (Advanced Audio Coding)</CodecLongName>
                                <CodecName>aac</CodecName>
                                <CodecTag>0x6134706d</CodecTag>
                                <CodecTagString>mp4a</CodecTagString>
                                <CodecTimeBase>1/44100</CodecTimeBase>
                                <Duration>0.440294</Duration>
                                <Index>1</Index>
                                <Language>und</Language>
                                <SampleFmt>fltp</SampleFmt>
                                <SampleRate>44100</SampleRate>
                                <StartTime>0.000000</StartTime>
                                <Timebase>1/44100</Timebase>
                        </Audio>
                        <Subtitle/>
                        <Video>
                                <AvgFps>24/1</AvgFps>
                                <Bitrate>938.164000</Bitrate>
                                <CodecLongName>H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10</CodecLongName>
                                <CodecName>h264</CodecName>
                                <CodecTag>0x31637661</CodecTag>
                                <CodecTagString>avc1</CodecTagString>
                                <CodecTimeBase>1/12288</CodecTimeBase>
                                <Dar>40:53</Dar>
                                <Duration>0.124416</Duration>
                                <Fps>24.500000</Fps>
                                <HasBFrame>2</HasBFrame>
                                <Height>1280</Height>
                                <Index>0</Index>
                                <Language>und</Language>
                                <Level>32</Level>
                                <NumFrames>243</NumFrames>
                                <PixFormat>yuv420p</PixFormat>
                                <Profile>High</Profile>
                                <RefFrames>1</RefFrames>
                                <Sar>25600:25599</Sar>
                                <StartTime>0.000000</StartTime>
                                <Timebase>1/12288</Timebase>
                                <Width>966</Width>
                        </Video>
                </Stream>
        </MediaInfo>
</Response>
```
