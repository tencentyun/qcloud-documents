## 功能描述
创建自定义模板，包含容器格式、视频转码配置设置。

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

>?Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
   <Tag>Animation</Tag>
   <Name>Template Name</Name>
   <Container>
      <Format>mp4</Format>
   </Container>
   <Video>
      <Codec>GIF</Codec>
      <Profile>high</Profile>
      <Bitrate>10-50000</Bitrate>
      <Crf>0-51</Crf>
      <Width>128-4096</Width>
      <Height>128-4096</Height>
      <Fps>1-60</Fps>
      <Gop>1-100000</Gop>
      <Preset>fast</Preset>
      <ScanMode>interlaced</ScanMode>
      <Bufsize>1000-128000</Bufsize>
      <Maxrate>10-50000</Maxrate>
      <PixFmt>yuv420p</PixFmt>
      <Remove>false</Remove>
      <Crop>border</Crop>
      <Pad></Pad>
      <LongShortMode>false</LongShortMode>
   </Video>
   <Audio>
      <Codec>AAC</Codec>
      <Profile>aac_he</Profile>
      <Samplerate>44100</Samplerate>
      <Bitrate>8</Bitrate>
      <Channels>2</Channels>
      <Remove>false</Remove>
   </Audio>
   <TransConfig>
      <TransMode>onepass</TransMode>
      <IsCheckReso>true</IsCheckReso>
      <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
      <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
   </TransConfig>
   <TimeInterval>
      <Start></Start>
      <Duration></Duration>
   </TimeInterval>
</Request>

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
      <td>模板类型 Animation，Snapshot</td>
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
      <td>无</td>
   </tr>
   <tr>
      <td>Audio</td>
      <td>Request</td>
      <td>音频信息</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>TransConfig</td>
      <td>Request</td>
      <td>转码配置</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
   <tr>
      <td>Snapshot</td>
      <td>Request</td>
      <td>截图</td>
      <td>Container</td>
      <td>否</td>
      <td>无</td>
   </tr>
</table>

Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述     | 类型   | 是否必选 | 默认值 | 限制                                           |
| ------------------ | ----------------- | -------- | ------ | -------- | ------ | ---------------------------------------------- |
| Format             | Request.Container | 容器格式 | String | 否       | mp4    | 参考 [容器格式和视频音频编解码格式支持情况](#1) 表格 |

Container 类型 Video 的具体数据描述如下：
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
      <td>Codec</td>
      <td>Request.Video</td>
      <td>编解码格式</td>
      <td>String</td>
      <td>否</td>
      <td>H.264</td>
      <td>可选值为：GIF、WEBP
      </td>
   </tr>
   <tr>
      <td>Profile</td>
      <td>Request.Video</td>
      <td>编码级别</td>
      <td>String</td>
      <td>否</td>
      <td>high</td>
      <td>
        1. 支持 baseline、main、high<br>
        2. baseline：适合移动设备<br>
        3. main：适合标准分辨率设备<br>
        4. high：适合高分辨率设备<br>
      </td>
   </tr>
   <tr>
      <td>Bitrate</td>
      <td>Request.Video</td>
      <td>视频的码率</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. 值范围：[10，50000]<br>
        2. 单位：Kbps<br>
      </td>
   </tr>
   <tr>
      <td>Crf</td>
      <td>Request.Video</td>
      <td>码率-质量控制因子</td>
      <td>String</td>
      <td>否</td>
      <td>26</td>
      <td>
        1. 值范围：[0，51]<br>
        2. 如果设置了 Crf，则 Bitrate 的设置失效
      </td>
   </tr>
   <tr>
      <td>Width</td>
      <td>Request.Video</td>
      <td>宽</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始宽度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px
      </td>
   </tr>
   <tr>
      <td>Height</td>
      <td>Request.Video</td>
      <td>高</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始高度</td>
      <td>
        1. 值范围：[128，4096]<br>
        2. 单位：px
      </td>
   </tr>
   <tr>
      <td>Fps</td>
      <td>Request.Video</td>
      <td>帧率</td>
      <td>String</td>
      <td>否</td>
      <td>视频原始帧率</td>
      <td>
        1. 值范围：(0，60]<br>
        2. 单位：fps<br>
        3. 帧率超过60时，设置为60<br>
      </td>
   </tr>
   <tr>
      <td>Gop</td>
      <td>Request.Video</td>
      <td>关键帧间最大时间间隔或者最大帧数</td>
      <td>String</td>
      <td>否</td>
      <td>10s</td>
      <td>
        1. 值范围：[0，100000]<br>
        2. 最大时间间隔单位 s<br>
        3. 最大帧数无单位<br>
      </td>
   </tr>
   <tr>
      <td>Preset</td>
      <td>Request.Video</td>
      <td>视频算法器预置</td>
      <td>String</td>
      <td>否</td>
      <td>medium</td>
      <td>
        1. H.264 支持该参数<br>
        2. veryfast、fast、medium、slow、slower
      </td>
   </tr>
   <tr>
      <td>ScanMode</td>
      <td>Request.Video</td>
      <td>扫描模式</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td> interlaced、progressive
      </td>
   </tr>
   <tr>
      <td>Bufsize</td>
      <td>Request.Video</td>
      <td>缓冲区大小</td>
      <td>String</td>
      <td>否</td>
      <td>6000</td>
      <td>
        1. 值范围：[1000，128000]<br>
        2. 单位：Kb
      </td>
   </tr>
   <tr>
      <td>Maxrate</td>
      <td>Request.Video</td>
      <td>视频码率峰值</td>
      <td>String</td>
      <td>否</td>
      <td>6000</td>
      <td>
        1. 值范围：[10，50000]<br>
        2. 单位：Kbps
      </td>
   </tr>
   <tr>
      <td>PixFmt</td>
      <td>Request.Video</td>
      <td>视频颜色格式</td>
      <td>String</td>
      <td>否</td>
      <td>yuv420p</td>
      <td> yuv420p、yuvj420p<br>
      </td>
   </tr>
   <tr>
      <td>Remove</td>
      <td>Request.Video</td>
      <td>是否删除视频流</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td> true、false<br>
      </td>
   </tr>
   <tr>
      <td>Crop</td>
      <td>Request.Video</td>
      <td>视频画面裁切</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. 自动监测黑边并裁切：border<br>
        2. 自定义裁切：width:height:left:top
      </td>
   </tr>
   <tr>
      <td>Pad</td>
      <td>Request.Video</td>
      <td>视频贴黑边</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>width:height:left:top<br>
      </td>
   </tr>
   <tr>
      <td>LongShortMode</td>
      <td>Request.Video</td>
      <td>是否开启横竖屏自适应</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td> true、false<br>
      </td>
   </tr>
   <tr>
      <td>AnimateOnlyKeepKeyFrame</td>
      <td>Request.Video</td>
      <td>动图只保留关键帧</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td>true、false<br>
      </td>
   </tr>
   <tr>
      <td>AnimateTimeIntervalOfFrame</td>
      <td>Request.Video</td>
      <td>动图抽帧间隔时间</td>
      <td>String</td>
      <td>否</td>
      <td>1</td>
      <td>
        1. （0，视频时长]<br>
        2.  若设置 TimeInterval.Duration，则小于该值<br>
      </td>
   </tr>
   <tr>
      <td>AnimateFramesPerSecond</td>
      <td>Request.Video</td>
      <td>Animation 每秒抽帧帧数</td>
      <td>String</td>
      <td>否</td>
      <td>1</td>
      <td>（0，视频帧率)<br>
      </td>
   </tr>
   <tr>
      <td>Quality</td>
      <td>Request.Video</td>
      <td>设置相对质量</td>
      <td>String</td>
      <td>否</td>
      <td>1</td>
      <td>无</td>
   </tr>
</table>

动图转码参数说明：

|参数| 描述|
|---|---|
|动图相关参数|包括有 AnimateOnlyKeepKeyFrame、AnimateTimeIntervalOfFrame、AnimateFramesPerSecond。<br><li>优先级：AnimateFramesPerSecond >  AnimateOnlyKeepKeyFrame  > AnimateTimeIntervalOfFrame<br><li>优先级高的设置生效，那么其他的忽略。要求有一个设置，其他两个为0|
|Fps 帧率|用户可以设置 fps，如果不设置，那么播放速度按照原来的时间戳。这里设置 fps 为动图的播放帧率
|Width Heidht|转码之后的宽高|
|Quality 质量参数|webp 图像质量设定生效，gif 没有质量参数设置。默认输出为无限循环|


Container 类型 Audio 的具体数据描述如下：
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
      <td>Codec</td>
      <td>Request.Audio</td>
      <td>编解码格式</td>
      <td>String</td>
      <td>否</td>
      <td>AAC</td>
      <td> AAC、MP3
      </td>
   </tr>
   <tr>
      <td>Profile</td>
      <td>Request.Audio</td>
      <td>音频编码预置</td>
      <td>String</td>
      <td>否</td>
      <td>无</td>
      <td>
        1. 仅支持 AAC 编码<br>
        2. aac_low、aac_he、aac_ld、aac_eld
      </td>
   </tr>
   <tr>
      <td>Samplerate</td>
      <td>Request.Audio</td>
      <td>采样率</td>
      <td>String</td>
      <td>否</td>
      <td>44100</td>
      <td>单位：Hz。可选值为：44100、32000、44100、48000、96000
      </td>
   </tr>
   <tr>
      <td>Bitrate</td>
      <td>Request.Audio</td>
      <td>原始音频码率</td>
      <td>String</td>
      <td>否</td>
      <td>128</td>
      <td>
        1. 单位：Kbps<br>
        2. 值范围：[8，1000]
      </td>
   </tr>
   <tr>
      <td>Channels</td>
      <td>Request.Audio</td>
      <td>声道数</td>
      <td>String</td>
      <td>否</td>
      <td>2</td>
      <td>
        1. 当 Codec 设置为 aac，支持1、2、4、5、6、8<br>
        2. 当 Codec 设置为 mp3，支持1、2<br>
      </td>
   </tr>
   <tr>
      <td>Remove</td>
      <td>Request.Audio</td>
      <td>是否删除音频流</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td>true、false</td>
   </tr>
</table>

Container 类型 TransConfig 的具体数据描述如下：
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
      <td>TransMode</td>
      <td>Request.TransConfig</td>
      <td>转码模式</td>
      <td>String</td>
      <td>否</td>
      <td>onepass</td>
      <td>可选值为：onepass、twopass、CBR</td>
   </tr>
   <tr>
      <td>IsCheckReso</td>
      <td>Request.TransConfig</td>
      <td>是否检查分辨率</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td>
       如果分辨率大于视频原始分辨率，则保持视频原始分辨率。可选值为：true、false
      </td>
   </tr>
   <tr>
      <td>IsCheckVideoBitrate</td>
      <td>Request.TransConfig</td>
      <td>是否检查视频码率</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td>如果码率大于视频原始码率，则保持视频原始码率。可选值为：true、false</td>
   </tr>
   <tr>
      <td>IsCheckAudioBitrate</td>
      <td>Request.TransConfig</td>
      <td>是否检查音频码率</td>
      <td>String</td>
      <td>否</td>
      <td>false</td>
      <td> 如果码率大于音频原始码率，则保持视频音频码率。可选值为：true、false </td>
   </tr>
</table>

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
      <td> [0，视频时长]<br>
      </td>
   </tr>
   <tr>
      <td>Duration</td>
      <td>Request.TimeInterval</td>
      <td>持续时间</td>
      <td>String</td>
      <td>否</td>
      <td>视频时长</td>
      <td> [0，视频时长]<br>
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
      <td>否</td>
      <td>0</td>
      <td> [0，视频时长]<br>
      </td>
   </tr>
   <tr>
      <td>TimeInterval</td>
      <td>Request.Snapshot</td>
      <td>截图频率</td>
      <td>String</td>
      <td>否</td>
      <td>0</td>
      <td> [0，10]<br>
      </td>
   </tr>
   <tr>
      <td>Count</td>
      <td>Request.Snapshot</td>
      <td>截图数量</td>
      <td>String</td>
      <td>否</td>
      <td>0</td>
      <td> [0，100]<br>
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
        2. 单位：px
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
        2. 单位：px
      </td>
   </tr>
</table>

<span id=1>

容器格式与视频音频编解码格式支持情况如下：

| Container | Audio Codec | Video Codec  |
| --------- | ----------- | ------------ |
| gif       | 不支持音频  | GIF          |
| webp      | 不支持音频  | WEBP         |
| m3u8      | AAC、MP3    | H.264、H.265 |
| flv       | AAC、MP3    | H.264        |
| mp4       | AAC、MP3    | H.264、H.265 |

视频编码格式与视频流配置参数支持情况如下：

| Video   Codec | H.264 | H.265  | GIF    |
| ------------- | ----- | ------ | ------ |
| Profile       | 支持  | 不支持 | 不支持 |
| Bitrate       | 支持  | 支持   | 不支持 |
| Crf           | 支持  | 支持   | 不支持 |
| Width         | 支持  | 支持   | 支持   |
| Height        | 支持  | 支持   | 支持   |
| Fps           | 支持  | 支持   | 支持   |
| Gop           | 支持  | 支持   | 不支持 |
| Preset        | 支持  | 不支持 | 不支持 |
| ScanMode      | 支持  | 支持   | 支持   |
| Bufsize       | 支持  | 支持   | 不支持 |
| Maxrate       | 支持  | 支持   | 不支持 |
| PixFmt        | 支持  | 支持   | 不支持 |

## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
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
         <Profile>high</Profile>
         <Bitrate>10-50000</Bitrate>
         <Crf>0-51</Crf>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Gop>1-100000</Gop>
         <Preset>fast</Preset>
         <ScanMode>interlaced</ScanMode>
         <Bufsize>1000-128000</Bufsize>
         <Maxrate>10-50000</Maxrate>
         <PixFmt>yuv420p</PixFmt>
         <Remove>false</Remove>
         <Crop>border</Crop>
         <Pad></Pad>
         <LongShortMode>false</LongShortMode>
      </Video>
      <Audio>
         <Codec>AAC</Codec>
         <Profile>aac_he</Profile>
         <Samplerate>44100</Samplerate>
         <Bitrate>8</Bitrate>
         <Channels>2</Channels>
         <Remove>false</Remove>
      </Audio>
      <TransConfig>
         <TransMode>onepass</TransMode>
         <IsCheckReso>true</IsCheckReso>
         <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
         <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
      </TransConfig>
      <TimeInterval>
         <Start></Start>
         <Duration></Duration>
      </TimeInterval>
   </TransTpl>
   <CreateTime></CreateTime>
   <UpdateTime></UpdateTime>
</Response>
```

#### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

错误码|描述|HTTP 状态码
---|---|---
InternalErrror|服务端内部错误|500 Internal Server
AccessDenied|签名或者权限不正确，拒绝访问|403 Forbidden

## 实际案例

### 截帧示例

#### 请求

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
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
        <Profile>high</Profile>
        <Bitrate>10-50000</Bitrate>
        <Crf>0-51</Crf>
        <Width>128-4096</Width>
        <Height>128-4096</Height>
        <Fps>1-60</Fps>
        <Gop>1-100000</Gop>
        <Preset>fast</Preset>
        <ScanMode>interlaced</ScanMode>
        <Bufsize>1000-128000</Bufsize>
        <Maxrate>10-50000</Maxrate>
        <PixFmt>yuv420p</PixFmt>
        <Remove>false</Remove>
        <Crop>border</Crop>
        <Pad></Pad>
        <LongShortMode>false</LongShortMode>
    </Video>
    <Audio>
        <Codec>AAC</Codec>
        <Profile>aac_he</Profile>
        <Samplerate>44100</Samplerate>
        <Bitrate>8</Bitrate>
        <Channels>2</Channels>
        <Remove>false</Remove>
    </Audio>
    <TransConfig>
        <TransMode>onepass</TransMode>
        <IsCheckReso>true</IsCheckReso>
        <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
        <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
    </TransConfig>
    <TimeInterval>
        <Start></Start>
        <Duration></Duration>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

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
         <Profile>high</Profile>
         <Bitrate>10-50000</Bitrate>
         <Crf>0-51</Crf>
         <Width>128-4096</Width>
         <Height>128-4096</Height>
         <Fps>1-60</Fps>
         <Gop>1-100000</Gop>
         <Preset>fast</Preset>
         <ScanMode>interlaced</ScanMode>
         <Bufsize>1000-128000</Bufsize>
         <Maxrate>10-50000</Maxrate>
         <PixFmt>yuv420p</PixFmt>
         <Remove>false</Remove>
         <Crop>border</Crop>
         <Pad></Pad>
         <LongShortMode>false</LongShortMode>
      </Video>
      <Audio>
         <Codec>AAC</Codec>
         <Profile>aac_he</Profile>
         <Samplerate>44100</Samplerate>
         <Bitrate>8</Bitrate>
         <Channels>2</Channels>
         <Remove>false</Remove>
      </Audio>
      <TransConfig>
         <TransMode>onepass</TransMode>
         <IsCheckReso>true</IsCheckReso>
         <IsCheckVideoBitrate>true</IsCheckVideoBitrate>
         <IsCheckAudioBitrate>true</IsCheckAudioBitrate>
      </TransConfig>
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

```shell
POST /template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
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

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

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
