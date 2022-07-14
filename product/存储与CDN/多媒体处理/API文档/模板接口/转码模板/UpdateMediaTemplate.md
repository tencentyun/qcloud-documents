## 功能描述

UpdateMediaTemplate 用于更新转码模板。

## 请求

#### 请求示例

```shell
PUT /template/<TemplateId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>Transcode</Tag>
    <Name>TemplateName</Name>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>H.264</Codec>
        <Profile>high</Profile>
        <Bitrate>1000</Bitrate>
        <Crf></Crf>
        <Width>1280</Width>
        <Height></Height>
        <Fps>30</Fps>
        <Gop></Gop>
        <Preset>medium</Preset>
        <ScanMode></ScanMode>
        <Bufsize>0</Bufsize>
        <Maxrate>0</Maxrate>
    </Video>
    <Audio>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
    </Audio>
    <TransConfig>
        <AdjDarMethod>scale</AdjDarMethod>
        <IsCheckReso>false</IsCheckReso>
        <ResoAdjMethod>1</ResoAdjMethod>
    </TransConfig>
    <TimeInterval>
        <Start>0</Start>
        <Duration>60</Duration>
    </TimeInterval>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                                      | 类型      | 必选 |
| :----------------- | :----- | :---------------------------------------- | :-------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |----|
| Tag                | Request | 模板类型：Transcode                                    | String    | 是   | 无 |
| Name               | Request | 模板名称 仅支持中文、英文、数字、_、-和*                    | String    | 是   | 无 |
| Container          | Request | 容器格式                                               | Container | 是   | 无 |
| Video              | Request | 视频信息                                               | Container | 否   | 不传 Video，相当于删除视频信息 |
| TimeInterval       | Request | 时间区间                                               | Container | 否   | 无 |
| Audio              | Request | 音频信息                                               | Container | 否   | 不传 Audio，相当于删除音频信息 |
| TransConfig        | Request | 转码配置                                               | Container | 否   | 无 |

Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format                | Request.Container | 容器格式：mp4，flv，hls，ts，WebM               | String    | 是   |

Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式            | String | 否   |   H.264，当format为WebM时，为VP8 | <li> H.264<br/><li> H.265<br/><li> VP8 |
| Width                      | Request.Video | 宽                    | String | 否   | 视频原始宽度 | <li> 值范围：[128, 4096]<br/><li> 单位：px<br/><li> 若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | Request.Video | 高                 | String | 否   | 视频原始高度 | <li> 值范围：[128, 4096]<br/><li> 单位：px<br/><li> 若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | Request.Video | 帧率                  | String | 否   | 视频原<br/>始帧率 |  <li>值范围：(0，60]<br> <li>单位：fps<br> <li>帧率超过60时，设置为60<br/>用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率 |
| Remove                     | Request.Video | 是否删除视频流       | String | 否   | false        | true、false                                               |
| Profile                    | Request.Video | 编码级别            | String | 否   | high         | <li> 支持baseline、main、high<br/><li> baseline：适合移动设备 <br/><li> main：适合标准分辨率设备 <br/><li> high：适合高分辨率设备 <br/><li> 仅H.264支持此参数 |
| Bitrate                    | Request.Video | 视频输出文件的码率    | String | 否   |  无           | <li> 值范围：[10, 50000]<br/><li> 单位：Kbps                     |
| Crf                        | Request.Video | 码率-质量控制因子     | String | 否   | 无           | <li> 值范围：(0, 51]<br/><li> 如果设置了 Crf，则 Bitrate 的设置失效<br/><li>默认为不设置 Crf |
| Gop                        | Request.Video | 关键帧间最大帧数      | String | 否   |  无            | <li> 值范围：[0, 100000]<br/><li>默认不设置 Gop<br/><li> Codec 为 VP8不支持此参数                                       |
| Preset                     | Request.Video | 视频算法器预置        | String | 否   | medium       | <li> 仅H.264支持该参数<br/><li> 取值veryfast、fast、medium、slow、slower<br/><li> Codec 为 VP8不支持此参数 |
| Bufsize                    | Request.Video | 缓冲区大小           | String | 否   | 无            | <li> 值范围：[1000, 128000]<br/><li> 单位：Kb<br/><li> Codec 为 VP8不支持此参数<br/><li>默认值为0，表示不使用缓冲区|
| Maxrate                    | Request.Video | 视频码率峰值         | String | 否   | 无            | <li> 值范围：[10, 50000]<br/><li> 单位：Kbps<br/><li> Codec 为 VP8不支持此参数 <br/><li>默认值为0，表示不使用此参数|
| HlsTsTime                  | Request.Video | hls分片时间          | String | 否   | 5            | <li> (0 视频时长] <br/> <li> 单位为秒<br/><li> Codec 为 VP8不支持此参数 |
| Pixfmt                     | Request.Video | 视频颜色格式          | String | 否   | 无           |<li>支持 yuv420p、yuv422p、yuv444p、yuvj420p、yuvj422p、yuvj444p<br/><li>Codec为VP8不支持此参数|
| LongShortMode              | Request.Video | 长短边自适应          | String | 否   | false        | <li> true、false<br/><li> Codec 为 VP8不支持此参数

Container 类型 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Request.TimeInterval | 开始时间 | String    | 否   | 0 |  <li>[0 视频时长] <br/> <li>单位为秒 <br/> <li>支持 float 格式，执行精度精确到毫秒 |
| Duration             | Request.TimeInterval | 持续时间 | String    | 否   | 视频时长 |  <li>[0 视频时长] <br/> <li>单位为秒 <br/> <li>支持 float 格式，执行精度精确到毫秒 |

Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否   | aac，当 format 为 WebM 时，为 Vorbis    | 取值 aac、mp3、flac、amr、Vorbis    |
| Samplerate         | Request.Audio | 采样率         | String | 否   | 44100,当Codec为opus时，默认值为48000  | <li>单位：Hz<br/><li> 可选 8000、11025、12000、16000、22050、24000、32000、44100、48000、88200、96000<br/><li>不同的封装，mp3 支持不同的采样率，如下表所示<br/><li>当Codec设置为amr时，只支持8000<br/><li>当Codec设置为opus时，仅支持8000，16000，24000，48000|
| Bitrate            | Request.Audio | 原始音频码率   | String | 否   | 无    | <li>单位：Kbps<br/><li>值范围：[8，1000]                       |
| Channels           | Request.Audio | 声道数         | String | 否   | 无      | <li>当 Codec 设置为 aac/flac，支持1、2、4、5、6、8<br/><li>当 Codec 设置为 mp3/Vorbis/opus时，支持1、2<br/><li>当 Codec 设置为 amr，只支持1 |
| Remove             | Request.Audio | 是否删除音频流 | String | 否   | false    | 取值 true、false。当 Video.Codec 为H.265时，此参数无效 
| KeepTwoTracks      | Request.Audio | 保持双音轨 | String | 否   | false    | 取值 true、false。 当 Video.Codec 为H.265时，此参数无效 
| SwitchTrack        | Request.Audio | 转换轨道 | String | 否   | false    | 取值 true、false。 当 Video.Codec 为H.265时，此参数无效                                       |
| SampleFormat       | Request.Audio | 采样位宽  | String | 否   | 无      | 1. 当 Codec 设置为 aac，支持 fltp<br/>2. 当 Codec 设置为 mp3，支持 fltp、s16p、s32p<br/>3. 当 Codec 设置为 flac，支持 s16、s32<br/>4. 当 Codec 设置为 amr，支持 s16<br/>5. 当 Video.Codec 为H.265时，此参数无效 |

Container 类型 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Request.TransConfig | 分辨率调整方式   | String | 否   | none   |  <li>取值 scale、crop、pad、none<br/> <li>当输出视频的宽高比与原视频不等时，根据此参数做分辨率的相应调整 |
| IsCheckReso           | Request.TransConfig | 是否检查分辨率   | String | 否   | false  |  <li>true、false <br/> <li>当为 false 时，按照配置参数转码 |
| ResoAdjMethod         | Request.TransConfig | 分辨率调整方式   | String | 否   | 0      |  <li>取值0、1；0 表示使用原视频分辨率；1表示返回转码失败<br/> <li>当 IsCheckReso 为 true 时生效 |
| IsCheckVideoBitrate   | Request.TransConfig | 是否检查视频码率 | String | 否   | false  |  <li>true、false <br/> <li>当为 false 时，按照配置参数转码 |
| VideoBitrateAdjMethod | Request.TransConfig | 视频码率调整方式 | String | 否   | 0      |  <li>取值0、1；0 表示使用原视频码率；1表示返回转码失败<br/> <li>当 IsCheckVideoBitrate 为 true 时生效 |
| IsCheckAudioBitrate   | Request.TransConfig | 是否检查音频码率 | String | 否   | false  |  <li>true、false <br/> <li>当为 false 时，按照配置参数转码<br/> |
| AudioBitrateAdjMethod | Request.TransConfig | 音频码率调整方式 | String | 否   | 0      |  <li>取值0、1；0 表示使用原音频码率；1表示返回转码失败<br/> <li>当 IsCheckAudioBitrate 为 true 时生效 |
| DeleteMetadata        | Request.TransConfig | 是否删除文件中的 MetaData 信息 | String | 否   | false     | 1. true、false <br/>2. 当为 false 时，保留源文件信息<br/>3. 当 Video.Codec 为H.265时，此参数无效 | 
| IsHdr2Sdr             | Request.TransConfig | 是否开启 HDR 转 SDR | String | 否   | false        | true/false |
| HlsEncrypt             | Request.TransConfig | HLS 加密配置 | Container | 否   | 无        | 无 |


AdjDarMethod 参数图示：

![](https://main.qcloudimg.com/raw/3436731be8c1caa5ffd565b2c44b9643.png)


Container 类型 HlsEncrypt 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 必选 | 默认值 | 限制 |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| IsHlsEncrypt          | Request.TransConfig.HlsEncrypt | 是否开启 HLS 加密 | String | 否   | false        | 1. true/false<br/>2. 当 Video.Codec 为H264或H265并且 Container.Format 为 HLS 时支持加密 |
| UriKey                | Request.TransConfig.HlsEncrypt | HLS 加密的 key | String | 否   | 无        | 当 IsHlsEncrypt 为 true 时，该参数才有意义 |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>Transcode</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <Container>
            <Format>mp4</Format>
        </Container>
        <Video>
            <Codec>H.264</Codec>
            <Profile>high</Profile>
            <Bitrate>1000</Bitrate>
            <Crf></Crf>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
            <Gop></Gop>
            <Preset>medium</Preset>
            <ScanMode></ScanMode>
            <Bufsize>0</Bufsize>
            <Maxrate>0</Maxrate>
        </Video>
        <Audio>
            <Codec>aac</Codec>
            <Samplerate>44100</Samplerate>
            <Bitrate>128</Bitrate>
            <Channels>4</Channels>
        </Audio>
        <TransConfig>
            <AdjDarMethod>scale</AdjDarMethod>
            <IsCheckReso>false</IsCheckReso>
            <ResoAdjMethod>1</ResoAdjMethod>
        </TransConfig>
        <TimeInterval>
            <Start>0</Start>
            <Duration>60</Duration>
        </TimeInterval>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器，同 CreateMediaTemplate 中的 Response | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response | 模板 ID                                                      | String    |
| Name               | Response | 模板名字                                                     | String    |
| Tag                | Response | 模板类型，Transcode                                          | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| TimeInterval       | Response | 同请求体中 Request.TimeInterval | Container |
| Container          | Response | 同请求体中 Request.Container    | Container |
| Video              | Response | 同请求体中 Request.Video        | Container |
| Audio              | Response | 同请求体中 Request.Audio        | Container |
| TransConfig        | Response | 同请求体中 Request.TransConfig  | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
PUT /template/<TemplateId> HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml



<Request>
    <Tag>Transcode</Tag>
    <Name>TemplateName</Name>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>H.264</Codec>
        <Profile>high</Profile>
        <Bitrate>1000</Bitrate>
        <Crf></Crf>
        <Width>1280</Width>
        <Height></Height>
        <Fps>30</Fps>
        <Gop></Gop>
        <Preset>medium</Preset>
        <ScanMode></ScanMode>
        <Bufsize>0</Bufsize>
        <Maxrate>0</Maxrate>
    </Video>
    <Audio>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
    </Audio>
    <TransConfig>
        <AdjDarMethod>scale</AdjDarMethod>
        <IsCheckReso>false</IsCheckReso>
        <ResoAdjMethod>1</ResoAdjMethod>
    </TransConfig>
    <TimeInterval>
        <Start>0</Start>
        <Duration>60</Duration>
    </TimeInterval>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****



<Response>
    <Template>
        <Tag>Transcode</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <Container>
            <Format>mp4</Format>
        </Container>
        <Video>
            <Codec>H.264</Codec>
            <Profile>high</Profile>
            <Bitrate>1000</Bitrate>
            <Crf></Crf>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
            <Gop></Gop>
            <Preset>medium</Preset>
            <ScanMode></ScanMode>
            <Bufsize>0</Bufsize>
            <Maxrate>0</Maxrate>
        </Video>
        <Audio>
            <Codec>aac</Codec>
            <Samplerate>44100</Samplerate>
            <Bitrate>128</Bitrate>
            <Channels>4</Channels>
        </Audio>
        <TransConfig>
            <AdjDarMethod>scale</AdjDarMethod>
            <IsCheckReso>false</IsCheckReso>
            <ResoAdjMethod>1</ResoAdjMethod>
        </TransConfig>
        <TimeInterval>
            <Start>0</Start>
            <Duration>60</Duration>
        </TimeInterval>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
