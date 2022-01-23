## 功能描述
CreateMediaTemplate 用于新增转码模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateTranscodeTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

```shell
POST /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。

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

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型：Transcode                                    | String    | 是   | 无 |
| Name               | Request | 模板名称 仅支持中文、英文、数字、\_、\-和\*                    | String    | 是   | 无 |
| Container          | Request | 容器格式                                               | Container | 是   | 无 |
| Video              | Request | 视频信息                                               | Container | 否   | 不传 Video，相当于删除视频信息 |
| TimeInterval       | Request | 时间区间                                               | Container | 否   | 无 |
| Audio              | Request | 音频信息                                               | Container | 否   | 不传 Audio，相当于删除音频信息 |
| TransConfig        | Request | 转码配置                                               | Container | 否   | 无 |


Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format                | Request.Container | 容器格式：mp4、flv、hls、ts、mp3、aac、WebM           | String    | 是   |

设定 container，音频视频支持的格式如下表：

| Container                  | Audio Codecs  | Video Codecs          |
| -------------------------- | ------------- | --------------------- | 
| mp4/hls                    | AAC、MP3      | H.264、H.265          |
| ts/mkv                     | AAC、MP3      | H.264                 |
| flv                        | AAC、MP3      | H.264                 |
| aac                        | aac           | 不支持                |
| mp3                        | mp3           | 不支持                |
| flac                       | flac          | 不支持                |
| amr                        | amr           | 不支持                |
| WebM                       | Vorbis、opus           | VP8                |


Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式            | String | 否   |   H.264，当 format 为 WebM 时，为 VP8 | 1. H.264<br/>2. H.265<br/>3. VP8 |
| Width                      | Request.Video | 宽                    | String | 否   | 视频原始宽度 | 1. 值范围：[128, 4096]<br/>2. 单位：px<br/>3. 若只设置 Width 时，按照视频原始比例计算 Height<br/>4. 必须为偶数 |
| Height                     | Request.Video | 高                 | String | 否   | 视频原始高度 | 1. 值范围：[128, 4096]<br/>2. 单位：px<br/>3. 若只设置 Height 时，按照视频原始比例计算 Width<br/>4. 必须为偶数 |
| Fps                        | Request.Video | 帧率                | String | 否   | 无 | 1. 值范围：(0, 60]<br>2. 单位：fps |
| Remove                     | Request.Video | 是否删除视频流       | String | 否   | false        | 1. true、false                                               |
| Profile                    | Request.Video | 编码级别            | String | 否   | high         | 1. 支持 baseline、main、high<br/>2. baseline：适合移动设备 <br/>3. main：适合标准分辨率设备 <br/>4. high：适合高分辨率设备 <br/>5. 仅H.264支持此参数 <br/>6.  Codec 为 VP8不支持此参数 |
| Bitrate                    | Request.Video | 视频输出文件的码率    | String | 否   |  无           | 1. 值范围：[10, 50000]<br/>2. 单位：Kbps                     |
| Crf                        | Request.Video | 码率-质量控制因子     | String | 否   | 无           | 1. 值范围：(0, 51]<br/>2. 如果设置了 Crf，则 Bitrate 的设置失效<br/>3. 当 Bitrate 为空时，默认为25 |
| Gop                        | Request.Video | 关键帧间最大帧数      | String | 否   |  无            | 1. 值范围：[0, 100000]                                    |
| Preset                     | Request.Video | 视频算法器预置        | String | 否   | medium，当 Codec 为 VP8时，为 good    | 1. H.264支持该参数，取值 veryfast、fast、medium、slow、slower<br/>2. VP8支持该参数，取值 good、realtime |
| Bufsize                    | Request.Video | 缓冲区大小           | String | 否   | 无            | 1. 值范围：[1000, 128000]<br/>2. 单位：Kb<br/>3. Codec 为 VP8不支持此参数|
| Maxrate                    | Request.Video | 视频码率峰值         | String | 否   | 无            | 1. 值范围：[10, 50000]<br/>2. 单位：Kbps<br/>3. Codec 为 VP8不支持此参数 |
| HlsTsTime                  | Request.Video | hls分片时间          | String | 否   | 5            | 1. (0 视频时长] <br/> 2. 单位为秒<br/>3. Codec 为 VP8不支持此参数 |
| Pixfmt                     | Request.Video | 视频颜色格式          | String | 否   | 无           |H.264支持：yuv420p、yuv422p、yuv444p、yuvj420p、yuvj422p、yuvj444p<br/>H.265支持：yuv420p<br/>Codec 为 VP8不支持此参数|
| LongShortMode              | Request.Video | 长短边自适应          | String | 否   | false        | 1. true、false<br/>2. Codec 为 VP8不支持此参数 |

Container 类型 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Request.TimeInterval | 开始时间 | String    | 否   | 0  | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |
| Duration             | Request.TimeInterval | 持续时间 | String    | 否   | 视频原始时长 | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |


Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否   | aac，当 format 为 WebM 时，为 Vorbis    | 取值 aac、mp3、flac、amr、Vorbis、opus    |
| Samplerate         | Request.Audio | 采样率         | String | 否   | 44100，当 Codec 为 opus 时，默认值为48000  | <li>单位：Hz<br/><li> 可选 8000、11025、12000、16000、22050、24000、32000、44100、48000、88200、96000<br/><li>不同的封装，mp3 支持不同的采样率，如下表所示<br/><li>当 Codec 设置为 amr 时，只支持8000<br/><li>当 Codec 设置为 opus 时，仅支持8000，16000，24000，48000|
| Bitrate            | Request.Audio | 原始音频码率   | String | 否   | 无    | <li>单位：Kbps<br/><li>值范围：[8，1000]                       |
| Channels           | Request.Audio | 声道数         | String | 否   | 无      | <li>当 Codec 设置为 aac/flac，支持1、2、4、5、6、8<br/><li>当 Codec 设置为 mp3/Vorbis/opus 时，支持1、2<br/><li>当 Codec 设置为 amr，只支持1 |
| Remove             | Request.Audio | 是否删除音频流 | String | 否   | false    | 取值 true、false。当 Video.Codec 为H.265时，此参数无效       
| KeepTwoTracks      | Request.Audio | 保持双音轨 | String | 否   | false    | 取值 true、false。 当 Video.Codec 为H.265时，此参数无效 
| SwitchTrack        | Request.Audio | 转换轨道 | String | 否   | false    | 取值 true、false。 当 Video.Codec 为H.265时，此参数无效                                        |
| SampleFormat       | Request.Audio | 采样位宽  | String | 否   | 无      | 1. 当 Codec 设置为 aac, 支持 fltp<br/>2. 当 Codec 设置为 mp3，支持 fltp、s16p、s32p<br/>3. 当 Codec 设置为 flac，支持 s16、s32<br/>4. 当 Codec 设置为 amr，支持 s16<br/>5. 当 Video.Codec 为H.265时，此参数无效 |

>? Y 表示支持这种采样率，N 表示不支持。
>


Audio.Codec采样率支持列表

| Audio.Codec | aac    | amr  | flac | opus | Vorbis | mp3 |
| ----------  | ------ | ---- |----- |----- | ------ | --- |
| 8000        | Y | Y | Y | Y | Y | 封装不同，支持不同 |
| 11025       | Y | N | Y | N | Y | - |
| 12000       | Y | N | Y | N | Y | - |
| 16000       | Y | N | Y | Y | Y | - |
| 22050       | Y | N | Y | N | Y | - |
| 24000       | Y | N | Y | Y | Y | - |
| 32000       | Y | N | Y | N | Y | - |
| 44100       | Y | N | Y | N | Y | - |
| 48000       | Y | N | Y | Y | Y | - |
| 88200       | Y | N | Y | N | Y | - |
| 96000       | Y | N | Y | N | Y | - |

当 Audio.Codec 为 mp3 时Container.Format的采样率兼容

| 封装格式/音频采样率 | 8000    |	11025  | 12000 | 16000 | 	22050 | 24000 | 	 32000 | 	44100|  	48000| 88200 |  	96000 |
| ------------------ | ------- | ------- |------- |------- | ------- | ------- | ------- |------------| ------------ | ------------- |-------- |
| flv	             | N|Y       | N | N | 	Y| N | 	N| 	Y| 	N| N |	N|
| mp4                | N|N       | N | Y | 	Y| Y |	Y| 	Y| 	Y| N |	N|
| hls/ts/mp3/mkv     | N|Y       | Y | Y | 	Y| Y |	Y| 	Y| 	Y| N |	N|










Container 类型 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 是否必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Request.TransConfig | 分辨率调整方式   | String | 否   | none   | <li>取值 scale、crop、pad、none<br/><li>当输出视频的宽高比与原视频不等时，根据此参数做分辨率的相应调整<br/><li>当 Video.Codec 为H.265时，此参数无效 |
| IsCheckReso           | Request.TransConfig | 是否检查分辨率   | String | 否   | false  | <li>true、false <br/><li>当为 false 时，按照配置参数转码 |
| ResoAdjMethod         | Request.TransConfig | 分辨率调整方式   | String | 否   | 0      | <li>取值0、1；0 表示使用原视频分辨率 <br/>1表示返回转码失败<br/><li>当 IsCheckReso 为 true 时生效 |
| IsCheckVideoBitrate   | Request.TransConfig | 是否检查视频码率 | String | 否   | false  | <li>true、false <br/><li>当为 false 时，按照配置参数转码 <br/><li>当 Video.Codec 为H.265时，此参数无效 |
| VideoBitrateAdjMethod | Request.TransConfig | 视频码率调整方式 | String | 否   | 0      | <li>取值0、1；0 表示使用原视频码率；1表示返回转码失败<br/><li>当 IsCheckVideoBitrate 为 true 时生效<br/><li>当 Video.Codec 为H.265时，此参数无效 |
| IsCheckAudioBitrate   | Request.TransConfig | 是否检查音频码率 | String | 否   | false  | <li>true、false <br/><li>当为 false 时，按照配置参数转码<br/><li>当 Video.Codec 为H.265时，此参数无效 |
| AudioBitrateAdjMethod | Request.TransConfig | 音频码率调整方式 | String | 否   | 0      | <li>取值0、1；0 表示使用原音频码率；1表示返回转码失败<br/><li>当 IsCheckAudioBitrate 为 true 时生效 <br/><li>当 Video.Codec 为H.265时，此参数无效</li> |
| DeleteMetadata        | Request.TransConfig | 是否删除文件中的 MetaData 信息 | String | 否   | false     | 1. true、false <br/>2. 当为 false 时，保留源文件信息<br/>3. 当 Video.Codec 为H.265时，此参数无效 | 
| IsHdr2Sdr             | Request.TransConfig | 是否开启 HDR 转 SDR | String | 否   | false        | true/false |
| HlsEncrypt             | Request.TransConfig | hls 加密配置 | Container | 否   | 无        | 无 |

AdjDarMethod 参数图示：

![](https://main.qcloudimg.com/raw/3436731be8c1caa5ffd565b2c44b9643.png)


Container 类型 HlsEncrypt 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 必选 | 默认值 | 限制 |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| IsHlsEncrypt          | Request.TransConfig.HlsEncrypt | 是否开启 HLS 加密 | String | 否   | false        | 1. true/false<br/>2. 当 Container.Format 为 hls 时支持加密 |
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

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |


Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.Template     | 模板 ID                                                      | String    |
| Name               | Response.Template     | 模板名称                                                     | String    |
| BucketId           | Response.Template     | 模板所属存储桶                                                | String    |
| Category           | Response.Template     | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response.Template     | 模板类型，Transcode                                          | String    |
| UpdateTime         | Response.Template     | 更新时间                                                     | String    |
| CreateTime         | Response.Template     | 创建时间                                                     | String    |
| TransTpl           | Response.Template     | 详细的模板参数                                                | Container |


Container节点TransTpl的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :-------------------------------------- | :-------- |
| TimeInterval       | Response.Template.TransTpl | 同请求体中的 <br/>Request.TimeInterval | Container |
| Container          | Response.Template.TransTpl | 同请求体中的 <br/>Request.Container    | Container |
| Video              | Response.Template.TransTpl | 同请求体中的 <br/>Request.Video        | Container |
| Audio              | Response.Template.TransTpl | 同请求体中的 <br/>Request.Audio        | Container |
| TransConfig        | Response.Template.TransTpl | 同请求体中的 <br/>Request.TransConfig  | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。


## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
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
