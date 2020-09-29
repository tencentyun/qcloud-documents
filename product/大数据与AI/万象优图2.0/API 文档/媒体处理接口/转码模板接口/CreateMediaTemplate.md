## 功能描述

CreateMediaTemplate 用于新增转码模板。

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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

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
        <AdjDarMethod>rescale</AdjDarMethod>
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

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 模板类型：Transcode                                    | String    | 是   |
| Name               | Request | 模板名称仅支持中文、英文、数字、_、-和*                    | String    | 是   |
| Container          | Request | 容器格式                                               | Container | 是   |
| Video              | Request | 视频信息                                               | Container | 否   |
| TimeInterval       | Request | 时间区间                                               | Container | 否   |
| Audio              | Request | 音频信息                                               | Container | 否   |
| TransConfig        | Request | 转码配置                                               | Container | 否   |


Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format                | Request.Container | 容器格式：mp4，flv，hls，ts               | String    | 是   |


Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式            | String | 否   |   H.264 |  H.264                                          |
| Width                      | Request.Video | 宽                    | String | 否   | 视频原<br/>始宽度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Width 时，按照<br/>视频原始比例计算 Height |
| Height                     | Request.Video | 高                    | String | 否   | 视频原<br/>始高度 | <li>值范围：[128，4096]<br/><li>单位：px<br/><li>若只设置 Height 时，按照<br/>视频原始比例计算 Width |
| Fps                        | Request.Video | 帧率                  | String | 否   | 无 | <li>值范围：(0，60]<br><li>单位：fps |
| Remove                     | Request.Video | 是否删除<br/>视频流        | String | 否   | false        | true、false                                               |
| Profile                    | Request.Video | 编码级别              | String | 否   | high         | <li>支持 baseline、main、high<br/><li>baseline：适合移动设备<br/><li>main：适合标准分辨率设备<br/><li>high：适合高分辨率设备<br/><li>仅H.264支持此参数 |
| Bitrate                    | Request.Video | 视频输出<br/>文件的码率    | String | 否   |  无           | <li>值范围：[10，50000]<br/><li>单位：Kbps                     |
| Crf                        | Request.Video | 码率-质量<br/>控制因子     | String | 否   | 无           | <li>值范围：(0，51]<br/><li>如果设置了 Crf，则 <br/>Bitrate 的设置失效 |
| Gop                        | Request.Video | 关键帧间<br/>最大帧数      | String | 否   |  无            | 值范围：[0，100000]                                          |
| Preset                     | Request.Video | 视频算法<br/>器预置        | String | 否   | medium       | <li>仅H.264支持该参数<br/><li>取值 veryfast、fast、<br/>medium、slow、slower |
| Bufsize                    | Request.Video | 缓冲区<br/>大小            | String | 否   | 无            | <li>值范围：[1000，128000]<br/><li>单位：Kb<br/> |
| Maxrate                    | Request.Video | 视频码率<br/>峰值          | String | 否   | 无            | <li>值范围：[10，50000]<br/><li>单位：Kbps<br/> |
| HlsTsTime                  | Request.Video | hls 分片<br/>时间           | String | 否   | 5            | <li>(0 视频时长] <br/><li>单位为秒 |
| Pixfmt                     | Request.Video | 视频颜色<br/>格式           | String | 否   | 无           | 支持 yuv420p、yuv422p、<br/>yuv444p、yuvj420p、yuvj422p、yuvj444p |

Container 类型 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Request.TimeInterval | 开始时间 | String    | 否   | 无 | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |
| Duration             | Request.TimeInterval | 持续时间 | String    | 否   | 无 | <li>[0 视频时长] <br/><li>单位为秒 <br/><li>支持 float 格式，执行精度精确到毫秒 |


Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否   | aac    | 取值 aac、mp3                                                |
| Samplerate         | Request.Audio | 采样率         | String | 否   | 44100  | <li>单位：Hz<br/><li>可选 11025、22050、32000、44100、48000、96000<br/><li>不同的封装，mp3 支持不同的采样率，如下表所示|
| Bitrate            | Request.Audio | 原始音频码率   | String | 否   | 无    | <li>单位：Kbps<br/><li>值范围：[8，1000]                       |
| Channels           | Request.Audio | 声道数         | String | 否   | 无      | <li>当 Codec 设置为 aac，支持1、2、4、5、6、8<br/><li>当 Codec 设置为 mp3，支持1、2 |
| Remove             | Request.Audio | 是否删除音频流 | String | 否   | false    | 取值 true、false                                             |


Y表示支持这种采样率，N表示不支持

| 封装格式/音频采样率| 	11025  | 	22050| 	 32000 | 	44100|  	48000|   	96000 |
| ------------------ | ------- | ------- | ------- | ------- |------------| ------------- |
| flv	             | Y       | 	Y| 	N| 	Y| 	N| 	N|
| mp4                | N       | 	Y| 	Y| 	Y| 	Y| 	N|
| avi/hls/ts/mp3     | Y       | 	Y| 	Y| 	Y| 	Y| 	N|


Container 类型 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Request.TransConfig | 分辨率调整方式   | String | 否   | none   | <li>取值 scale、crop、pad、none<br/><li>当输出视频的宽高比与原视频不等时，<br/>需要此参数进行执行调整方式 |
| IsCheckReso           | Request.TransConfig | 是否检查分辨率   | String | 否   | false  | <li>true、false <br/><li>当为 false时，按照配置参数转码 |
| ResoAdjMethod         | Request.TransConfig | 分辨率调整方式   | String | 否   | 0      | <li>取值0、1；0 表示使用原视频分辨率；<br/>1表示返回转码失败<br/><li>当 IsCheckReso 为 true 时生效 |
| IsCheckVideoBitrate   | Request.TransConfig | 是否检查视频码率 | String | 否   | false  | <li>true、false <br/><li>当为 false 时，按照配置参数转码 |
| VideoBitrateAdjMethod | Request.TransConfig | 视频码率调整方式 | String | 否   | 0      | <li>取值0、1；0 表示使用原视频码率；<br/>1表示返回转码失败<br/><li>当 IsCheckVideoBitrate 为 true 时生效 |
| IsCheckAudioBitrate   | Request.TransConfig | 是否检查音频码率 | String | 否   | false  | <li>true、false <br/><li>当为false时，按照配置参数转码<br/> |
| AudioBitrateAdjMethod | Request.TransConfig | 音频码率调整方式 | String | 否   | 0      | <li>取值0、1；0 表示使用原音频码率；<br/>1表示返回转码失败<br/><li>当 IsCheckAudioBitrate 为 true 时生效 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>Transcode</Tag>
        <TemplateId></TemplateId>
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
            <AdjDarMethod>rescale</AdjDarMethod>
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
| TemplateId         | Response.TemplateList | 模版 ID                                                      | String    |
| Name               | Response.TemplateList | 模版名字                                                     | String    |
| BucketId           | Response.TemplateList | 模版所属存储桶                                                | String    |
| Category           | Response.TemplateList | 模版属性，Custom 或者 Official                                | String    |
| Tag                | Response.TemplateList | 模版类型，Transcode                                          | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| TransTpl           | Response.TemplateList | 详细的模版参数                                                | Container |


Container节点TransTpl的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :-------------------------------------- | :-------- |
| TimeInterval       | Response.TemplateList.TransTpl | 同请求体中的 <br/>Request.TimeInterval | Container |
| Container          | Response.TemplateList.TransTpl | 同请求体中的 <br/>Request.Container    | Container |
| Video              | Response.TemplateList.TransTpl | 同请求体中的 <br/>Request.Video        | Container |
| Audio              | Response.TemplateList.TransTpl | 同请求体中的 <br/>Request.Audio        | Container |
| TransConfig        | Response.TemplateList.TransTpl | 同请求体中的 <br/>Request.TransConfig  | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
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
        <AdjDarMethod>rescale</AdjDarMethod>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=

<Response>
    <Template>
        <Tag>Transcode</Tag>
        <TemplateId></TemplateId>
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
            <AdjDarMethod>rescale</AdjDarMethod>
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
