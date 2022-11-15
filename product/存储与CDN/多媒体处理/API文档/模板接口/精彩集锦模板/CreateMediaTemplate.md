## 功能描述
CreateMediaTemplate 用于新增精彩集锦模板。

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
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。


#### 请求体
该请求操作的实现需要有如下请求体：

```shell
<Request>
    <Tag>VideoMontage</Tag>
    <Name>TemplateName</Name>
    <Duration></Duration>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>H.264</Codec>
        <Bitrate>1000</Bitrate>
        <Width>1280</Width>
        <Height></Height>
        <Fps>30</Fps>
    </Video>
    <Audio>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
        <Remove>false</Remove>
    </Audio>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |


Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型: VideoMontage                                    | String    | 是   | 无 |
| Name               | Request | 模板名称 仅支持中文、英文、数字、\_、\-和\*                    | String    | 是   | 无 |
| Duration           | Request | 集锦时长                                                 | String    | 否   | 1. 默认自动分析时长</br>2. 单位为秒</br>3. 支持 float 格式，执行精度精确到毫秒|
| Container          | Request | 容器格式                                                 | Container | 是   | 无 |
| Video              | Request | 视频信息                                                 | Container | 是   | 无|
| Audio              | Request | 音频信息                                                 | Container | 否   | 无|


Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| -----------------| ------- | ----------------------------------------------------    | --------- | ---- |
| Format           | Request.Container | 容器格式: mp4、flv、hls、ts、mkv             | String    | 是   |

设定 container，音频视频支持的格式如下表：

| Container                  | Audio Codecs  | Video Codecs          |
| -------------------------- | ------------- | --------------------- | 
| mp4/ts/hls/mkv             | AAC、MP3      | H.264、H.265          |
| flv                        | AAC、MP3      | H.264                 |


Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                  | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | --------------------- | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式            | String | 否   |   H.264      | 1. H.264<br/> 2.H.265  |
| Width                      | Request.Video | 宽                    | String | 否   | 视频原始宽度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Width 时，按照视频原始比例计算 Height<br/>4. 必须为偶数 |
| Height                     | Request.Video | 高                    | String | 否   | 视频原始高度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Height 时，按照视频原始比例计算 Width<br/>4. 必须为偶数 |
| Fps                        | Request.Video | 帧率                  | String | 否   | 无           | 1. 值范围：(0，60]<br>2. 单位：fps |
| Bitrate                    | Request.Video | 视频输出文件的码率    | String | 否   |  无          | 1. 值范围：[10，50000]<br/>2. 单位：Kbps                     |
| Crf                        | Request.Video | 码率-质量控制因子     | String | 否   | 无           | 1. 值范围：(0, 51]<br/>2. 如果设置了 Crf，则 Bitrate 的设置失效<br/>3. 当 Bitrate 为空时，默认为25 |

Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否   | aac    | 取值 aac、mp3                                               |
| Samplerate         | Request.Audio | 采样率         | String | 否   | 44100  | 1. 单位：Hz<br/>2. 可选 11025、22050、32000、44100、48000、96000<br/>3. 不同的封装，mp3 支持不同的采样率，如下表所示|
| Bitrate            | Request.Audio | 原始音频码率   | String | 否   | 无     | 1. 单位：Kbps<br/>2. 值范围：[8，1000]                       |
| Channels           | Request.Audio | 声道数         | String | 否   | 无     | 1. 当 Codec 设置为 aac，支持1、2、4、5、6、8<br/>2. 当 Codec 设置为 mp3，支持1、2|
| Remove             | Request.Audio | 是否删除音频流 | String | 否   | false  | 取值 true、false|

>? Y 表示支持这种采样率，N 表示不支持。
>

| 封装格式/音频采样率| 	11025  | 	22050| 	 32000 | 	44100|  	48000|   	96000 |
| ------------------ | ------- | ------- | ------- | ------- |------------| ------------- |
| flv	             | Y       | 	Y| 	N| 	Y| 	N| 	N|
| mp4                | N       | 	Y| 	Y| 	Y| 	Y| 	N|
| hls/ts/mkv         | Y       | 	Y| 	Y| 	Y| 	Y| 	N|


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>VideoMontage</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <VideoMontage>
            <Duration></Duration>
            <Container>
                <Format>mp4</Format>
            </Container>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Audio>
                <Codec>aac</Codec>
                <Samplerate>44100</Samplerate>
                <Bitrate>128</Bitrate>
                <Channels>4</Channels>
                <Remove>false</Remove>
            </Audio>
        </VideoMontage>
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
| Name               | Response.Template     | 模板名称                                                    | String    |
| BucketId           | Response.Template     | 模板所属存储桶                                                | String    |
| Category           | Response.Template     | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response.Template     | 模板类型，VideoMontage                                          | String    |
| UpdateTime         | Response.Template     | 更新时间                                                     | String    |
| CreateTime         | Response.Template     | 创建时间                                                     | String    |
| VideoMontage       | Response.Template     | 详细的模板参数                                                | Container |


Container节点VideoMontage的内容：

| 节点名称（关键字） | 父节点                         | 描述                               | 
| :----------------- | :----------------------------- | :------------------------------- |
| Duration           | Response.TemplateList.VideoMontage | 同请求体中的 Request.Duration     | 
| TimeInterval       | Response.TemplateList.VideoMontage | 同请求体中的 Request.TimeInterval |
| Container          | Response.TemplateList.VideoMontage | 同请求体中的 Request.Container    |
| Video              | Response.TemplateList.VideoMontage | 同请求体中的 Request.Video        |
| Audio              | Response.TemplateList.VideoMontage | 同请求体中的 Request.Audio        |


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
    <Tag>VideoMontage</Tag>
    <Name>TemplateName</Name>
    <Duration></Duration>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>H.264</Codec>
        <Bitrate>1000</Bitrate>
        <Width>1280</Width>
        <Height></Height>
        <Fps>30</Fps>
    </Video>
    <Audio>
        <Codec>aac</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>128</Bitrate>
        <Channels>4</Channels>
        <Remove>false</Remove>
    </Audio>
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
        <Tag>VideoMontage</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <VideoMontage>
            <Duration></Duration>
            <Container>
                <Format>mp4</Format>
            </Container>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Audio>
                <Codec>aac</Codec>
                <Samplerate>44100</Samplerate>
                <Bitrate>128</Bitrate>
                <Channels>4</Channels>
                <Remove>false</Remove>
            </Audio>
        </VideoMontage>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
