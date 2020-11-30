## 功能描述
DescribeTemplates 用于搜索转码模板。

## 请求
### 请求实例

```shell
GET /template HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

> Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| tag           | 无        | 模板Tag：Transcode       | String    |是|
| category      | 无   | Official，Custom，默认值: Custom | String    |是|
| ids           | 无        | 模板 ID, 以,符号分割字符串  | String     |否|
| name          | 无        | 模板名称前缀              | String     |否|
| pageNumber    | 无        | 第几页                   | Integer     |否|
| pageSize      | 无        | 每页个数                 | Integer     |否|


## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Desc>TemplateDesc</Desc>
        <Tag>Transcode</Tag>
        <TransTpl>
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
        </TransTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 模版总数                       | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| TemplateList       | Response | 模版数组                       | Container |

Container 节点 TemplateList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.TemplateList | 模版 ID                                                      | String    |
| Name               | Response.TemplateList | 模版名字                                                     | String    |
| Desc               | Response.TemplateList | 模版描述                                                     | String    |
| BucketId           | Response.TemplateList | 模版所属存储桶                                                | String    |
| Category           | Response.TemplateList | 模版属性，Custom 或者 Official                                | String    |
| Tag                | Response.TemplateList | 模版类型，Transcode                                          | String    |
| UpdateTime         | Response.TemplateList | 更新时间                                                     | String    |
| CreateTime         | Response.TemplateList | 创建时间                                                     | String    |
| TransTpl           | Response.TemplateList | 详细的模版参数                                                | Container |

Container 节点 TransTpl 的内容：

| 节点名称（关键字） | 父节点                         | 描述     | 类型      |
| :----------------- | :----------------------------- | :------- | :-------- |
| TimeInterval       | Response.TemplateList.TransTpl | 时间区间 | Container |
| Container          | Response.TemplateList.TransTpl | 容器格式 | Container |
| Video              | Response.TemplateList.TransTpl | 视频信息 | Container |
| Audio              | Response.TemplateList.TransTpl | 音频信息 | Container |
| TransConfig        | Response.TemplateList.TransTpl | 转码配置 | Container |

TransTpl 节点 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format                | Request.Container | 容器格式: mp4，flv，hls，ts               | String    | 是   |

TransTpl 节点 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Response.TemplateList.TransTpl.Video | 编解码格式            | String | 否   |   视频原始编码 | 1. H.264                                          |
| Width                      | Response.TemplateList.TransTpl.Video | 宽                    | String | 否   | 视频原始宽度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | Response.TemplateList.TransTpl.Video | 高                    | String | 否   | 视频原始高度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | Response.TemplateList.TransTpl.Video | 帧率                  | String | 否   | 视频原始帧率 | 1. 值范围：(0，60]<br>2. 单位：fps<br>3. 帧率超过60时，设置为60<br/>用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率。 |
| Remove                     | Response.TemplateList.TransTpl.Video | 是否删除视频流        | String | 否   | false        | 1. true、false                                               |
| Profile                    | Response.TemplateList.TransTpl.Video | 编码级别              | String | 否   | high         | 1. 支持 baseline、main、high<br/>2. baseline：适合移动设备；<br/>3. main：适合标准分辨率设备；<br/>4. high：适合高分辨率设备;<br/>5. 仅 H.264支持此参数。 |
| Bitrate                    | Response.TemplateList.TransTpl.Video | 视频输出文件的码率    | String | 否   |  无           | 1. 值范围：[10，50000]<br/>2. 单位：Kbps                     |
| Crf                        | Response.TemplateList.TransTpl.Video | 码率-质量控制因子     | String | 否   | 26           | 1. 值范围：[0，51]<br/>2. 如果设置了 Crf，则 Bitrate 的设置失效 |
| Gop                        | Response.TemplateList.TransTpl.Video | 关键帧间最大帧数      | String | 否   |  无            | 1. 值范围：[0，100000]                                          |
| Preset                     | Response.TemplateList.TransTpl.Video | 视频算法器预置        | String | 否   | medium       | 1. 仅 H.264支持该参数<br/>2. 取值 veryfast、fast、medium、slow、slower |
| Bufsize                    | Response.TemplateList.TransTpl.Video | 缓冲区大小            | String | 否   | 0            | 1. 值范围：[1000，128000]<br/>2. 单位：Kb<br/>3. 默认值为0表示不使用 buf |
| Maxrate                    | Response.TemplateList.TransTpl.Video | 视频码率峰值          | String | 否   | 0            | 1. 值范围：[10，50000]<br/>2. 单位：Kbps<br/>3. 默认值0表示不使用此参数 |

TransTpl 节点 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Response.TemplateList.TransTpl.TimeInterval | 开始时间 | String    | 否   | 0 | 1. [0 视频时长] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |
| Duration             | Response.TemplateList.TransTpl.TimeInterval | 持续时间 | String    | 否   | 视频时长 | 1. [0 视频时长] <br/> 2. 单位为秒 <br/> 3. 支持 float 格式，执行精度精确到毫秒 |

TransTpl 节点 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Response.TemplateList.TransTpl.Audio | 编解码格式     | String | 否   | aac    | 取值 aac、mp3                                                |
| Samplerate         | Response.TemplateList.TransTpl.Audio | 采样率         | String | 否   | 44100  | 1. 单位：Hz<br/>2. 44100、32000、44100、48000、96000<br/>3. 若视频容器格式为 flv，音频编解码格式选择为 mp3 时，采样率不支持32000、48000、96000；音频编解码格式为 mp3 时，采样率不支持96000。 |
| Bitrate            | Response.TemplateList.TransTpl.Audio | 原始音频码率   | String | 否   | 128    | 1. 单位：Kbps<br/>2. 值范围：[8，1000]                       |
| Channels           | Response.TemplateList.TransTpl.Audio | 声道数         | String | 否   |  无      | 1. 当 Codec 设置为 aac，支持1、2、4、5、6、8<br/>2. 当 Codec 设置为 mp3，支持1、2 |
| Remove             | Response.TemplateList.TransTpl.Audio | 是否删除音频流 | String | 否   |   无    | 取值 true、false                                             |

TransTpl 节点 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Response.TemplateList.TransTpl.TransConfig | 分辨率调整方式   | String | 否   | none   | 1. 取值 scale、crop、pad、none。<br/>2. 当输出视频的宽高比与原视频不等时，需要此参数进行执行调整方式。 |
| IsCheckReso           | Response.TemplateList.TransTpl.TransConfig | 是否检查分辨率   | String | 否   | false  | 1. true、false <br/> 2. 当为 false 时，按照配置参数转码 |
| ResoAdjMethod         | Response.TemplateList.TransTpl.TransConfig | 分辨率调整方式   | String | 否   | 0      | 1. 取值0、1；0 表示使用原视频分辨率；1表示返回转码失败<br/>2. 当 IsCheckReso 为 true 时生效 |
| IsCheckVideoBitrate   | Response.TemplateList.TransTpl.TransConfig | 是否检查视频码率 | String | 否   | false  | 1. true、false <br/>2. 当为 false 时，按照配置参数转码 |
| VideoBitrateAdjMethod | Response.TemplateList.TransTpl.TransConfig | 视频码率调整方式 | String | 否   | 0      | 1. 取值0、1；0 表示使用原视频码率；1表示返回转码失败<br/>2. 当 IsCheckVideoBitrate 为 true 时生效 |
| IsCheckAudioBitrate   | Response.TemplateList.TransTpl.TransConfig | 是否检查音频码率 | String | 否   | false  | 1. true、false <br/>2. 当为 false 时，按照配置参数转码<br/> |
| AudioBitrateAdjMethod | Response.TemplateList.TransTpl.TransConfig | 音频码率调整方式 | String | 否   | 0      | 1. 取值0、1；0 表示使用原音频码率；1表示返回转码失败<br/>2. 当 IsCheckAudioBitrate 为 true 时生效 |


### 错误码

该请求无特有错误信息，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例
### 按照模板ID维度查询
#### 请求

```shell
GET /template?ids=A,B,C HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Desc>TemplateDesc</Desc>
        <Tag>Transcode</Tag>
        <TransTpl>
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
        </TransTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
    <NonExistTIDs>
        <TemplateId>B</TemplateId>
        <TemplateId>C</TemplateId>
    </NonExistTIDs>
</Response>
```

### 按照分页列表维度查询
#### 请求

```shell
GET /template?pageSize=10&pageNumber=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Name>TemplateName</Name>
        <Desc>TemplateDesc</Desc>
        <Tag>Transcode</Tag>
        <TransTpl>
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
        </TransTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>
```
