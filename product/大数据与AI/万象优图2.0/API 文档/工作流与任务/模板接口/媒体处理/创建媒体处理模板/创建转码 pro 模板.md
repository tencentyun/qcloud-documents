## 功能描述

创建转码 pro 模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateTranscodeProTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>TranscodePro</Tag>
    <Name>TemplateName</Name>
    <Container>
        <Format>mxf</Format>
    </Container>
    <Video>
        <Codec>xavc</Codec>
        <Profile>XAVC-HD_422_10bit</Profile>
        <Width>1920</Width>
        <Height>1080</Height>
        <Interlaced>true</Interlaced>
        <Fps>30000/1001</Fps>
        <Bitrate>50000</Bitrate>
    </Video>
    <Audio>
        <Codec>pcm_s24le</Codec>
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

<span id="Request"></span>
Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 限制 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- | ---- |
| Tag                | Request | 模板类型：TranscodePro                                    | String    | 是   | 无 |
| Name               | Request | 模板名称 仅支持中文、英文、数字、\_、\-和\*                  | String    | 是   | 无 |
| Container          | Request | 容器格式                                               | Container | 是   | 无 |
| Video              | Request | 视频信息                                               | Container | 是  | 无 |
| TimeInterval       | Request | 时间区间                                               | Container | 否   | 无 |
| Audio              | Request | 音频信息                                               | Container | 否   | 不传 Audio，相当于删除音频信息 |
| TransConfig        | Request | 转码配置                                               | Container | 否   | 无 |

<span id="Container"></span>
Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                   | 类型      | 是否必选 |
| ------------------ | ------- | ---------------------------------------------------- | --------- | ---- |
| Format             | Request.Container | 容器格式：mxf、mov、mkv                      | String    | 是   |

设定 container，音频视频支持的格式如下表：

| Container                  | Audio Codecs  | Video Codecs          |
| -------------------------- | ------------- | --------------------- | 
| mxf                        | pcm_s24le     | xavc                  |
| mov、mkv                   | aac、mp3      | apple_prores          |

<span id="Video"></span>
Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述                  | 类型   | 是否必选 | 默认值    | 限制  |
| ---------------- | ------------- | -------------------- | ------ | ---- | ------------ |------ |
| Codec            | Request.Video | 编解码格式            | String | 是   | 无   | xavc、apple_prores |
| Profile          | Request.Video | 视频算法器预置        | String | 是   | 无       | 取值范围见下表  |
| Width            | Request.Video | 宽                   | String | 是   | 无       | 取值范围见下表 |
| Height           | Request.Video | 高                   | String | 是   | 无       | 取值范围见下表 |
| Interlaced       | Request.Video | 场模式               | String | 是   | 无       | 取值范围见下表 |
| Fps              | Request.Video | 帧率                 | String | 是   | 无       | 取值范围见下表 |
| Bitrate          | Request.Video | 视频输出文件的码率    | String | 否   | 无       | 取值范围见下表 |
| Rotate           | Request.Video | 旋转角度             | String | 否   | 无        |1. 值范围：[0, 360)<br/>2. 单位：度 |

<br>
视频参数约束表:<br>
注：'-' 表示留空。码率可选值与帧率可选值序号对应。

当 Video.Codec 为 xavc 时：

| Profile                          | Width  | Height | Interlaced| Fps | Bitrate(单位:kbps)    |
| -------------------------------- | ------ | ------ | --------- | --- | ---------- |
| XAVC-HD_intra_420_10bit_class50  | 1440   | 1080   | true | 1、25<br>2、30000/1001 |-|
| XAVC-HD_intra_420_10bit_class50  | 1440   | 1080   | false| 1、25<br>2、24000/1001<br>3、30000/1001|-|
| XAVC-HD_intra_422_10bit_class100 | 1280   | 720    | false| 1、50<br>2、60000/1001 |-|
| XAVC-HD_intra_422_10bit_class100 | 1920   | 1080   | true | 1、25<br>2、30000/1001 |-|
| XAVC-HD_intra_422_10bit_class100 | 1920   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-HD_intra_422_10bit_class200 | 1920   | 1080   | true | 1、25<br>2、30000/1001 |-|
| XAVC-HD_intra_422_10bit_class200 | 1920   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit_class100 | 2048   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit_class300 | 3840   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit_class300 | 4096   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit_class480 | 3840   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit_class480 | 4096   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |-|
| XAVC-4K_intra_422_10bit          | 2048   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |                                                            1、93000<br>2、185000<br>3、89000<br>4、111000<br>5、222000  |
| XAVC-4K_intra_422_10bit          | 3840   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |                                                            1、250000或400000<br>2、500000或800000<br>3、240000或384000<br>4、300000或480000<br>5、600000或960000  |
| XAVC-4K_intra_422_10bit          | 4096   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |                                              1、250000或400000<br>2、500000或800000<br>3、240000或384000<br>4、300000或480000<br>5、600000或960000  |
| XAVC-HD_422_10bit                | 1280   | 720   | false| 1、50<br>2、60000/1001 | 1、50000<br>2、50000|
| XAVC-HD_422_10bit                | 1920   | 1080  | true | 1、25<br>2、30000/1001 | 1、25000或35000或50000<br>2、25000或35000或50000|
| XAVC-HD_422_10bit                | 1920   | 1080  | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 | 1、25000或35000或50000<br>2、35000或50000<br>3、25000或35000或50000<br>4、25000或35000或50000<br>5、35000或50000|
| XAVC-4K_422_10bit                | 3840   | 2160  | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 | 1、100000或140000或200000<br>2、140000或200000<br>3、100000或140000或200000<br>4、100000或140000或200000<br>5、140000或200000|
| XAVC-4K_420_8bit                 | 3840   | 2160  | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 | 1、188000<br>2、300000<br>3、188000<br>4、188000<br>5、300000|

当 Video.Codec 为 apple_prores 时：

| Profile |
| ------ |
|1.ProRes_422_Proxy</br>2.ProRes_422_LT</br>3.ProRes_422</br>4.ProRes_422_HQ</br>5.ProRes_4444</br>6.ProRes_4444_XQ</br>7.ProRes_4444_alpha</br>8.ProRes_4444_XQ_alpha    |

| Width  | Height | Interlaced| Fps |Bitrate(单位:kbps)    |
| ------ | ------ | --------- | --- | --- |
| 720    | 486    | false| 1、24000/1001<br>2、30000/1001 |取值范围:[2000,3000000]|
| 720    | 486    | true | 1、60000/1001 |取值范围:[2000,3000000]|
| 720    | 576    | false| 1、25 |取值范围:[2000,3000000]|
| 720    | 576    | true | 1、50 |取值范围:[2000,3000000]|
| 960    | 720    | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 1280   | 720    | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 1280   | 1080   | false| 1、24000/1001<br>2、30000/1001 |取值范围:[2000,3000000]|
| 1280   | 1080   | true | 1、60000/1001 |取值范围:[2000,3000000]|
| 1440   | 1080   | false| 1、24000/1001<br>2、25<br>3、30000/1001 |取值范围:[2000,3000000]|
| 1440   | 1080   | true | 1、50<br>2、60000/1001 |取值范围:[2000,3000000]|
| 1920   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 1920   | 1080   | true | 1、50<br>2、60000/1001 |取值范围:[2000,3000000]|
| 2048   | 1080   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 2048   | 1556   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 3840   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 4096   | 2160   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 5120   | 2700   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 6144   | 3240   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|
| 8192   | 4320   | false| 1、25<br>2、50<br>3、24000/1001<br>4、30000/1001<br>5、60000/1001 |取值范围:[2000,3000000]|

<span id="TimeInterval"></span>
Container 类型 TimeInterval 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Start                | Request.TimeInterval | 开始时间 | String    | 否   | 0  | <ul  style="margin: 0;"><li>[0 视频时长] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li></ul> |
| Duration             | Request.TimeInterval | 持续时间 | String    | 否   | 视频原始时长 | <ul  style="margin: 0;"><li>[0 视频时长] </li><li>单位为秒 </li><li>支持 float 格式，执行精度精确到毫秒</li></ul> |

<span id="Audio"></span>
Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 | 默认值 | 限制  |
| ------------------ | ------------- | ----------- | ------ | ---- | ------ | ----------------------------- |
| Codec              | Request.Audio | 编解码格式   | String | 是   | 无    | pcm_s24le、aac、mp3|
| Remove             | Request.Audio | 是否删除源音频流 | String | 否   | false    | 取值 true、false|

<span id="TransConfig"></span>
Container 类型 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 是否必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Request.TransConfig | 分辨率调整方式   | String | 否   | none   | <ul  style="margin: 0;"><li>取值 scale、crop、pad、none</li><li>当输出视频的宽高比与原视频不等时，根据此参数做分辨率的相应调整</li></ul> |
| IsCheckReso           | Request.TransConfig | 是否检查分辨率   | String | 否   | false  | <ul  style="margin: 0;"><li>true、false </li><li>当为 false时，按照配置参数转码</li></ul> |
| ResoAdjMethod         | Request.TransConfig | 分辨率调整方式   | String | 否   | 0      | <ul  style="margin: 0;"><li>取值0、1；0 表示使用原视频分辨率；</li>1表示返回转码失败</li><li>当 IsCheckReso 为 true 时生效</li></ul> |
| IsCheckVideoBitrate   | Request.TransConfig | 是否检查视频码率 | String | 否   | false  | <ul  style="margin: 0;"><li>true、false </li><li>当为 false 时，按照配置参数转码</li></ul> |
| VideoBitrateAdjMethod | Request.TransConfig | 视频码率调整方式 | String | 否   | 0      | <ul  style="margin: 0;"><li>取值0、1；当输出视频码率大于原视频码率时，0表示使用原视频码率；1表示返回转码失败</li><li>当 IsCheckVideoBitrate 为 true 时生效</li></ul> |
| IsCheckAudioBitrate   | Request.TransConfig | 是否检查音频码率 | String | 否   | false  | <ul  style="margin: 0;"><li>true、false</li><li>当为 false 时，按照配置参数转码 </li></ul> |
| AudioBitrateAdjMethod | Request.TransConfig | 音频码率调整方式 | String | 否   | 0      | <ul  style="margin: 0;"><li>取值0、1；当输出音频码率大于原音频码率时，0 表示使用原音频码率；1表示返回转码失败</li><li>当 IsCheckAudioBitrate 为 true 时生效</li></ul> |
| IsCheckVideoFps       | Request.TransConfig | 是否检查视频帧率 | String | 否   | false  | <ul  style="margin: 0;"><li>true、false </li><li>当为 false 时，按照配置参数转码</li></ul> |
| VideoFpsAdjMethod     | Request.TransConfig | 视频帧率调整方式 | String | 否   | 0      | <ul  style="margin: 0;"><li>取值0、1；当输出视频帧率大于原视频帧率时，0表示使用原视频帧率；1表示返回转码失败</li><li>当 IsCheckVideoFps 为 true 时生效</li></ul> |
| DeleteMetadata        | Request.TransConfig | 是否删除文件中的MetaData信息 | String | 否   | false     | <ul  style="margin: 0;"><li>true、false </li><li>当为 false 时，保留源文件信息</li></ul>| 
| IsHdr2Sdr             | Request.TransConfig | 是否开启HDR转SDR | String | 否   | false        | true/false |

AdjDarMethod 参数图示：

![](https://main.qcloudimg.com/raw/3436731be8c1caa5ffd565b2c44b9643.png)

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Template>
        <Tag>TranscodePro</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <BucketId>test-1234567890</BucketId>
        <Category>Custom</Category>
        <TransProTpl>
            <Container>
                <Format>mxf</Format>
            </Container>
            <Video>
                <Codec>xavc</Codec>
                <Profile>XAVC-HD_422_10bit</Profile>
                <Width>1920</Width>
                <Height>1080</Height>
                <Interlaced>true</Interlaced>
                <Fps>30000/1001</Fps>
                <Bitrate>50000</Bitrate>
            </Video>
            <Audio>
                <Codec>pcm_s24le</Codec>
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
        </TransProTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

<span id="Response"></span>
Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId         | Response.Template     | 模板 ID                                                      | String    |
| Name               | Response.Template     | 模板名称                                                     | String    |
| BucketId           | Response.Template     | 模板所属存储桶                                                | String    |
| Category           | Response.Template     | 模板属性，Custom 或者 Official                                | String    |
| Tag                | Response.Template     | 模板类型，TranscodePro                                          | String    |
| UpdateTime         | Response.Template     | 更新时间                                                     | String    |
| CreateTime         | Response.Template     | 创建时间                                                     | String    |
| TransProTpl        | Response.Template     | 详细的模板参数                                                | Container |


Container 节点 TransProTpl 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                    | 类型      |
| :----------------- | :----------------------------- | :-------------------------------------- | :-------- |
| TimeInterval       | Response.Template.TransProTpl | 同请求体中的 <br/>Request.TimeInterval | Container |
| Container          | Response.Template.TransProTpl | 同请求体中的 <br/>Request.Container    | Container |
| Video              | Response.Template.TransProTpl | 同请求体中的 <br/>Request.Video        | Container |
| Audio              | Response.Template.TransProTpl | 同请求体中的 <br/>Request.Audio        | Container |
| TransConfig        | Response.Template.TransProTpl | 同请求体中的 <br/>Request.TransConfig  | Container |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
POST /template HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signatrue=28e9a4986df11bed0255e97ff90500557e0e****
Host: test-1234567890.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Tag>TranscodePro</Tag>
    <Name>TemplateName</Name>
    <Container>
        <Format>mxf</Format>
    </Container>
    <Video>
        <Codec>xavc</Codec>
        <Profile>XAVC-HD_422_10bit</Profile>
        <Width>1920</Width>
        <Height>1080</Height>
        <Interlaced>true</Interlaced>
        <Fps>30000/1001</Fps>
        <Bitrate>50000</Bitrate>
    </Video>
    <Audio>
        <Codec>pcm_s24le</Codec>
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
Date: Thu, 14 Jul 2022 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <Template>
        <Tag>TranscodePro</Tag>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <BucketId>test-1234567890</BucketId>
        <Category>Custom</Category>
        <TransProTpl>
            <Container>
                <Format>mxf</Format>
            </Container>
            <Video>
                <Codec>xavc</Codec>
                <Profile>XAVC-HD_422_10bit</Profile>
                <Width>1920</Width>
                <Height>1080</Height>
                <Interlaced>true</Interlaced>
                <Fps>30000/1001</Fps>
                <Bitrate>50000</Bitrate>
            </Video>
            <Audio>
                <Codec>pcm_s24le</Codec>
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
        </TransProTpl>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </Template>
</Response>
```
