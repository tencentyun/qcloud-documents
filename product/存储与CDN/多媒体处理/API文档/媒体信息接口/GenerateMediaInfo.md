## 功能描述

GenerateMediainfo 接口用于获取媒体文件的信息。

## 请求

#### 请求示例

```shell
POST /mediainfo HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml

<body>
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体

该 API 接口请求的请求体具体节点内容为：

```shell
<Request>
  <Input>
    <Object></Object>
  </Input>
</Request>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                | 类型      | 是否必选 |
| :----------------- | :----- | :---------------------------------- | :-------- | :------- |
| Request            | 无     | 保存 Generate Media info 请求的容器 | Container | 是       |

Container 节点 Request 的内容：

| 节点名称（关键字） | 父节点  | 描述               | 类型      | 是否必选 |
| :----------------- | :------ | :----------------- | :-------- | :------- |
| Input              | Request | 媒体文件的位置信息 | Container | 是       |

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 |
| :----------------- | :------------ | :------------- | :----- | :------- |
| Object             | Request.Input | 媒体文件的名称 | String | 是       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

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

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| MediaInfo          | Response | 媒体的详细信息 | Container |

Container 节点 MediaInfo 的内容：

| 节点名称（关键字） | 父节点             | 描述     | 类型      |
| :----------------- | :----------------- | :------- | :-------- |
| Stream             | Response.MediaInfo | 流信息   | Container |
| Format             | Response.MediaInfo | 格式信息 | Container |

Container 节点 Stream 的内容：

| 节点名称（关键字） | 父节点                    | 描述     | 类型      |
| :----------------- | :------------------------ | :------- | :-------- |
| Video              | Response.MediaInfo.Stream | 视频信息 | Container |
| Audio              | Response.MediaInfo.Stream | 音频信息 | Container |
| Subtitle           | Response.MediaInfo.Stream | 字幕信息 | Container |

Container 节点 Format 的内容：

| 节点名称（关键字） | 父节点                    | 描述                                        | 类型   |
| :----------------- | :------------------------ | :------------------------------------------ | :----- |
| NumStream          | Response.MediaInfo.Format | Stream（包含 Video、Audio、Subtitle）的数量 | Int    |
| NumProgram         | Response.MediaInfo.Format | 节目的数量                                  | Int    |
| FormatName         | Response.MediaInfo.Format | 容器格式名称                                | String |
| FormatLongName     | Response.MediaInfo.Format | 容器格式的详细名称                          | String |
| StartTime          | Response.MediaInfo.Format | 起始时间，单位为秒                          | Float  |
| Duration           | Response.MediaInfo.Format | 时长，单位为秒                              | Float  |
| Bitrate            | Response.MediaInfo.Format | 比特率，单位为 kbps                         | Int    |
| Size               | Response.MediaInfo.Format | 大小，单位为 Byte                           | Int    |

Container 节点 Video 的内容：

| 节点名称（关键字） | 父节点                          | 描述                   | 类型   |
| :----------------- | :------------------------------ | :--------------------- | :----- |
| Index              | Response.MediaInfo.Stream.Video | 该流的编号             | Int    |
| CodecName          | Response.MediaInfo.Stream.Video | 编解码格式名称         | String |
| CodecLongName      | Response.MediaInfo.Stream.Video | 编解码格式的详细名称   | String |
| CodecTimeBase      | Response.MediaInfo.Stream.Video | 编码时基               | String |
| CodecTagString     | Response.MediaInfo.Stream.Video | 编码标签名             | String |
| CodecTag           | Response.MediaInfo.Stream.Video | 编码标签               | String |
| Profile            | Response.MediaInfo.Stream.Video | 视频编码档位           | String |
| Height             | Response.MediaInfo.Stream.Video | 视频高                 | Int    |
| Width              | Response.MediaInfo.Stream.Video | 视频宽                 | Int    |
| HasBFrame          | Response.MediaInfo.Stream.Video | 是否有B帧              | Int    |
| RefFrames          | Response.MediaInfo.Stream.Video | 视频编码的参考帧个数   | Int    |
| Sar                | Response.MediaInfo.Stream.Video | 采样宽高比             | String |
| Dar                | Response.MediaInfo.Stream.Video | 显示宽高比             | String |
| PixFormat          | Response.MediaInfo.Stream.Video | 像素格式               | String |
| FieldOrder         | Response.MediaInfo.Stream.Video | 场的顺序               | String |
| Level              | Response.MediaInfo.Stream.Video | 视频编码等级           | Int    |
| Fps                | Response.MediaInfo.Stream.Video | 视频帧率               | Int    |
| AvgFps             | Response.MediaInfo.Stream.Video | 平均帧率               | String |
| Timebase           | Response.MediaInfo.Stream.Video | 时基                   | String |
| StartTime          | Response.MediaInfo.Stream.Video | 视频开始时间，单位为秒 | Float  |
| Duration           | Response.MediaInfo.Stream.Video | 视频时长，单位为秒     | Float  |
| Bitrate            | Response.MediaInfo.Stream.Video | 比特率，单位为 kbps    | Float  |
| NumFrames          | Response.MediaInfo.Stream.Video | 总帧数                 | Int    |
| Language           | Response.MediaInfo.Stream.Video | 语言                   | String |

Container 节点 Audio 的内容：

| 节点名称（关键字） | 父节点                          | 描述                   | 类型   |
| :----------------- | :------------------------------ | :--------------------- | :----- |
| Index              | Response.MediaInfo.Stream.Audio | 该流的编号             | Int    |
| CodecName          | Response.MediaInfo.Stream.Audio | 编解码格式名称         | String |
| CodecLongName      | Response.MediaInfo.Stream.Audio | 编解码格式的详细名称   | String |
| CodecTimeBase      | Response.MediaInfo.Stream.Audio | 编码时基               | String |
| CodecTagString     | Response.MediaInfo.Stream.Audio | 编码标签名             | String |
| CodecTag           | Response.MediaInfo.Stream.Audio | 编码标签               | String |
| SampleFmt          | Response.MediaInfo.Stream.Audio | 采样格式               | String |
| SampleRate         | Response.MediaInfo.Stream.Audio | 采样率                 | Int    |
| Channel            | Response.MediaInfo.Stream.Audio | 通道数量               | Int    |
| ChannelLayout      | Response.MediaInfo.Stream.Audio | 通道格式               | String |
| Timebase           | Response.MediaInfo.Stream.Audio | 时基                   | String |
| StartTime          | Response.MediaInfo.Stream.Audio | 音频开始时间，单位为秒 | Float  |
| Duration           | Response.MediaInfo.Stream.Audio | 音频时长，单位为秒     | Float  |
| Bitrate            | Response.MediaInfo.Stream.Audio | 比特率，单位为 kbps    | Float  |
| Language           | Response.MediaInfo.Stream.Audio | 语言                   | String |

Container 节点 Subtitle 的内容：

| 节点名称（关键字） | 父节点                             | 描述       | 类型   |
| :----------------- | :--------------------------------- | :--------- | :----- |
| Index              | Response.MediaInfo.Stream.Subtitle | 该流的编号 | Int    |
| Language           | Response.MediaInfo.Stream.Subtitle | 语言       | String |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
POST /mediainfo HTTP/1.1
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b4****
Content-Length: 352
Content-Type: application/xml

<Request>
  <Input>
    <Object>video-for-test.mp4</Object>
  </Input>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-ci
x-ci-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZm****

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
                                <Duration>10.125000</Duration>
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
                                <CodecName>H.264</CodecName>
                                <CodecTag>0x31637661</CodecTag>
                                <CodecTagString>avc1</CodecTagString>
                                <CodecTimeBase>1/12288</CodecTimeBase>
                                <Dar>40:53</Dar>
                                <Duration>10.125000</Duration>
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

