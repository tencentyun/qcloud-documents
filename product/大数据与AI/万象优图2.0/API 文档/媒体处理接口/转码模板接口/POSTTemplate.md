## 功能描述

CreateMediaTemplate 接口用于新增转码模板。

## 请求

#### 请求示例

```plaintext
POST /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```xml
<Request>
   <Tag>Animation</Tag>
   <Name>Template Name</Name>
   <Container>
      <Format>gif</Format>
   </Container>
   <Video>
      <Codec>GIF</Codec>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Fps>1-60</Fps>
      <Remove>false</Remove>
   </Video>
   <TimeInterval>
      <Start></Start>
      <Duration></Duration>
   </TimeInterval>
</Request>

<Request>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <Snapshot>
      <Mode>Interval</Mode>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
</Request>
```

具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Request</td>
      <td>无</td>
      <td>保存请求的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
</table>

Container 类型 Request 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Tag</td>
      <td>Request</td>
      <td>模板类型 Animation，Snapshot，Transcode</td>
      <td>String</td>
      <td>是</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Name</td>
      <td>Request</td>
      <td>模板名称</td>
      <td>String</td>
      <td>是</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Container</td>
      <td>Request</td>
      <td>容器格式</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>Video</td>
      <td>Request</td>
      <td>视频信息</td>
      <td>Container</td>
      <td>否</td>
      <td>Tag 为 Animation，Transcode 时生效</td>
   </tr>
   <tr>
      <td>Audio</td>
      <td>Request</td>
      <td>音频信息</td>
      <td>Container</td>
      <td>否</td>
      <td>Tag 为 Transcode 时生效</td>
   </tr>
   <tr>
      <td>TransConfig</td>
      <td>Request</td>
      <td>转码配置</td>
      <td>Container</td>
      <td>否</td>
      <td>Tag 为 Transcode 时生效</td>
   </tr>
   <tr>
      <td>TimeInterval</td>
      <td>Request</td>
      <td>转码时间区间</td>
      <td>Container</td>
      <td>否</td>
      <td>Tag 为 Animation，Transcode 时生效</td>
   </tr>
   <tr>
      <td>Snapshot</td>
      <td>Request</td>
      <td>截图</td>
      <td>Container</td>
      <td>否</td>
      <td>Tag 为 Snapshot 时生效</td>
   </tr>
</table>

Container 类型 Container 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Format</td>
      <td>Request.Container</td>
      <td>容器格式</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
      <td>
        gif，hgif，webp，mp4，flv，m3u8，ts。hgif 为高质量 gif，即清晰度比较高的 gif 格式图<br>
      </td>
   </tr>
</table>

Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字）         | 父节点        | 描述                   | 类型   | 是否必选 | 默认值       | 限制                                                         |
| -------------------------- | ------------- | ---------------------- | ------ | -------- | ------------ | ------------------------------------------------------------ |
| Codec                      | Request.Video | 编解码格式             | String | 否       | 无           | h264、gif、webp                                              |
| Width                      | Request.Video | 宽                     | String | 否       | 视频原始宽度 | 1.  值范围：[128，4096]<br>2. 单位：px<br>3. 若只设置 Width 时，按照视频原始比例计算 Height |
| Height                     | Request.Video | 高                     | String | 否       | 视频原始高度 | 1. 值范围：[128，4096]<br>2. 单位：px<br>3. 若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                        | Request.Video | 帧率                   | String | 否       | 视频原始帧率 | 1.  值范围：(0，60]<br>2. 单位：fps<br>3. 帧率超过60时，设置为60 <br> 4. 用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率 |
| Remove                     | Request.Video | 是否删除视频流         | String | 否       | FALSE        | true、false                                                  |
| AnimateOnlyKeepKeyFrame    | Request.Video | 动图只保留关键帧       | String | 否       | 无           | 1.  true、false  <br>  2. 动图保留关键帧参数                 |
| AnimateTimeIntervalOfFrame | Request.Video | 动图抽帧间隔时间       | String | 否       | 无           | 1.  （0，视频时长] <br>  2. 动图抽帧时间间隔 <br> 3. 若设置 TimeInterval.Duration，则小于该值 |
| AnimateFramesPerSecond     | Request.Video | Animation 每秒抽帧帧数 | String | 否       | 无           | 1.（0，视频帧率)    <br>2. 动图抽帧频率 <br>3. 优先级：AnimateFramesPerSecond > AnimateOnlyKeepKeyFrame >  AnimateTimeIntervalOfFrame |
| Quality                    | Request.Video | 设置相对质量           | String | 否       | 无           | 1. [1,  100)  <br>2. webp 图像质量设定生效，gif 没有质量参数 |
| Profile                    | Request.Video | 编码级别               | String | 否       | high         | 1. 支持 baseline、main、high  <br>2. baseline：适合移动设备  <br>3. main：适合标准分辨率设备 <br>4. high：适合高分辨率设备 <br>5. 仅h264支持此参数 |
| Bitrate                    | Request.Video | 视频输出文件的码率     | String | 否       | 无           | 1. 值范围：[10，50000]  <br>2.  单位：Kbps                   |
| Crf                        | Request.Video | 码率-质量控制因子      | String | 否       | 26           | 1. 值范围：[0，51]  <br>2. 如果设置了 Crf，则 Bitrate 的设置失效 |
| Gop                        | Request.Video | 关键帧间最大帧数       | String | 否       | 无           | 值范围：[0，100000]                                          |
| Preset                     | Request.Video | 视频算法器预置         | String | 否       | medium       | 1. 仅h264支持该参数   <br>2. 取值 veryfast、fast、medium、slow、slower |
| Bufsize                    | Request.Video | 缓冲区大小             | String | 否       | 0            | 1. 值范围：[1000，128000] <br>2. 单位：Kb  <br>3. 默认值为0表示不使用 Bufsize |
| Maxrate                    | Request.Video | 视频码率峰值           | String | 否       | 0            | 1. 值范围：[10，50000]  <br>2. 单位：Kbps  <br>3. 默认值0表示不使用此参数 |

Container 类型 TimeInterval 的具体数据描述如下：

<table width="100%">
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Start</td>
      <td>Request.TimeInterval</td>
      <td>开始时间</td>
      <td>String</td>
      <td>否</td>
      <td>0</td>
      <td>
        1. [0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>Duration</td>
      <td>Request.TimeInterval</td>
      <td>持续时间</td>
      <td>String</td>
      <td>否</td>
      <td>视频时长</td>
      <td>
        1. (0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
</table>

Container 类型 Snapshot 的具体数据描述如下：

<table width="100%">
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>默认值</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Start</td>
      <td>Request.Snapshot</td>
      <td>开始时间</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
      <td>
        1. [0 视频时长] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>TimeInterval</td>
      <td>Request.Snapshot</td>
      <td>截图频率</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. (0 3600] <br>
        2. 单位为秒 <br>
        3. 支持 float 格式，执行精度精确到毫秒
      </td>
   </tr>
   <tr>
      <td>Count</td>
      <td>Request.Snapshot</td>
      <td>截图数量</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
      <td>
        (0 10000] <br>
      </td>
   </tr>
   <tr>
      <td>Width</td>
      <td>Request.Snapshot</td>
      <td>宽</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始宽度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Width 时，按照视频原始比例计算 Height<br>
      </td>
   </tr>
   <tr>
      <td>Height</td>
      <td>Request.Snapshot</td>
      <td>高</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始高度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px<br>
        3. 若只设置 Height 时，按照视频原始比例计算 Width<br>
      </td>
   </tr>
   <tr>
      <td>Mode</td>
      <td>Request.Snapshot</td>
      <td>截屏模式</td>
      <td>String</td>
      <td>否</td>
      <td>Interval</td>
      <td>
        1. 值范围：{Interval, Average}<br>
        2. Interval 表示间隔模式 Average 表示平均模式<br>
        3. Interval 模式：Start，TimeInterval，Count 参数生效。当设置 Count，未设置 TimeInterval 时，表示截取所有帧，共 Count 张图片<br>
        4. Average 模式：Start，Count 参数生效。表示从 Start 开始到视频结束，按平均间隔截取共 Count 张图片
      </td>
   </tr>
</table>

Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------- | -------------- | ------ | -------- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Audio | 编解码格式     | String | 否       | aac    | 取值 aac、mp3                                                |
| Samplerate         | Request.Audio | 采样率         | String | 否       | 44100  | 1. 单位：Hz<br/>2. 44100、32000、44100、48000、96000<br/>3. 若视频容器格式为 flv，音频编解码格式选择为 mp3时，采样率不支持32000、48000、96000；音频编解码格式为 mp3时，采样率不支持96000。 |
| Bitrate            | Request.Audio | 原始音频码率   | String | 否       | 128    | 单位：Kbps<br/>2. 值范围：[8，1000]                          |
| Channels           | Request.Audio | 声道数         | String | 否       |        | 1. 当 Codec 设置为 aac，支持1、2、4、5、6、8<br/>2. 当 Codec 设置为 mp3，支持1、2 |
| Remove             | Request.Audio | 是否删除音频流 | String | 否       |        | 取值 true、false                                             |

Container 类型 TransConfig 的具体数据描述如下：

| 节点名称（关键字）    | 父节点              | 描述             | 类型   | 是否必选 | 默认值 | 限制                                                         |
| --------------------- | ------------------- | ---------------- | ------ | -------- | ------ | ------------------------------------------------------------ |
| AdjDarMethod          | Request.TransConfig | 分辨率调整方式   | String | 否       | none   | 1. 取值 rescale、crop、pad、none。<br/>2. 当输出视频的宽高比与原视频不等时，需要此参数进行执行调整方式。 |
| IsCheckReso           | Request.TransConfig | 是否检查分辨率   | String | 否       | false  | 1. 如果分辨率大于视频原始分辨率，则保持视频原始分辨率<br/>2. true、false |
| ResoAdjMethod         | Request.TransConfig | 分辨率调整方式   | String | 否       | 0      | 1. 取值0、1；0 表示使用原视频分辨率；1表示返回转码失败<br/>2. 当 IsCheckReso 为 true 时生效 |
| IsCheckVideoBitrate   | Request.TransConfig | 是否检查视频码率 | String | 否       | false  | 1. 如果码率大于视频原始码率，则保持视频原始码率<br/>2. true、false |
| VideoBitrateAdjMethod | Request.TransConfig | 视频码率调整方式 | String | 否       | 0      | 1. 取值0、1；0 表示使用原视频码率；1表示返回转码失败<br/>2. 当 IsCheckVideoBitrate 为 true 时生效 |
| IsCheckAudioBitrate   | Request.TransConfig | 是否检查音频码率 | String | 否       | false  | 1. 如果码率大于音频原始码率，则保持视频音频码率<br/>2. true、false |
| AudioBitrateAdjMethod | Request.TransConfig | 音频码率调整方式 | String | 否       | 0      | 1. 取值0、1；0 表示使用原音频码率；1表示返回转码失败<br/>2. 当 IsCheckAudioBitrate 为 true 时生效 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```xml
<Response>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <Tag>Animation</Tag>
    <TransTpl>
      <Container>
         <Format>mp4</Format>
      </Container>
      <Video>
         <Codec>GIF</Codec>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Remove>false</Remove>
      </Video>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型      |
| :----------------- | :----- | :----------------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器，同 DescribeMediaTemplates 中的 Response.TemplateList | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

### 截帧示例

#### 请求

```plaintext
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Name>Template Name</Name>
    <Tag>Animation</Tag>
    <Container>
        <Format>mp4</Format>
    </Container>
    <Video>
        <Codec>GIF</Codec>
        <Width>128-4096</Width>
        <Height>128-4096</Height>
        <Fps>1-60</Fps>
        <Remove>false</Remove>
    </Video>
    <TimeInterval>
        <Start></Start>
        <Duration></Duration>
    </TimeInterval>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <Tag>Animation</Tag>
    <Name>Template Name</Name>
    <TemplateID></TemplateID>
    <TransTpl>
      <Container>
         <Format>mp4</Format>
      </Container>
      <Video>
         <Codec>GIF</Codec>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Remove>false</Remove>
      </Video>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```

### 视频转动图示例

#### 请求

```plaintext
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <Snapshot>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
   <Tag>Snapshot</Tag>
   <Name>Template Name</Name>
   <TemplateID></TemplateID>
   <Snapshot>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Start></Start>
      <TimeInterval></TimeInterval>
      <Count></Count>
   </Snapshot>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```
