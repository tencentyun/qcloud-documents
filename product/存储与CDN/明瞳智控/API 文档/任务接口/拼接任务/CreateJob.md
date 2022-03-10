## 功能描述
用于提交一个任务。

## 请求

#### 请求示例

```plaintext
POST /project/<ProjectId>/jobs HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数
此接口无请求参数。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
  <Tag>Concat</Tag>
  <Operation>
    <Concat>
      <Fragments></Fragments>
      <Container></Container>
      <Effect></Effect>
      <Video></Video>
      <Audio></Audio>
      <Index></Index>
    </Concat>
    <Output>
      <Region></Region>
      <Bucket></Bucket>
      <Object></Object>
    </Output>
    <Notify>
      <Url></Url>
    </Notify>
  </Operation>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                  | 类型      | 是否必选 |
| ------------------ | ------- | ----------------------- | --------- | ---- |
| Tag                | Request | 创建任务的 Tag：Concat | String    | 是   |
| Operation          | Request | 操作规则                | Container | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| Concat               | Request.Operation | 指定拼接参数   | Container | 是  |
| Output                       | Request.Operation | 结果输出地址                                          | Container | 是   |
| Notify | Request.Operation | 任务结果通知地址 | Container | 否 |
| Watermark | Request.Operation | 水印参数，可以设置多个 | Container | 否 |

Container 类型 Concat 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                    | 类型      | 是否必选 | 默认值       |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---|
| Fragments     |  Request.Operation.Concat | 拼接节点    | Container 数组    | 是   | 无  |
| Container | Request.Operation.Concat | 封装格式 | Container | 是 | 无 |
| Effect | Request.Operation.Concat | 拼接特效。可选 FADE(淡入淡出)、GRADIENT(渐变)| String | 否 | 无 |
| Time | Request.Operation.Concat | 场景变化的时间，单位为秒，支持浮点型 | String | 否 | 1 |
| Audio               | Request.Operation.Concat | 音频参数  | Container    | 否   | 无  |
| Video               | Request.Operation.Concat | 视频参数  | Container    | 否   | 无  |
| Index               | Request.Operation.Concat | Fragments 中 Index 下标的视频作为主视频，用于获取默认参数为原视频值的参数 | Integer | 否   | 0  |
| AudioMix      | Request.Operation.Concat | 混音参数 | Container | 否   | 无  |


Container 类型 Fragments 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---|
| Url                 | Request.Operation.Concat.Fragments | 拼接对象地址   | String    | 是   | 无   |
| Decrypt            | Request.Operation.Concat.Fragments | 视频文件的解密配置 | Container | 否   | 无       |
| StartTime          | Request.Operation.Concat.Fragments | 开始时间           | Float     | 否   | 视频开始 |
| EndTime            | Request.Operation.Concat.Fragments | 结束时间           | Float     | 否   | 视频结束 |

Container 类型 Decrypt 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                     | 描述                                            | 类型   | 是否必选 | 默认值 |
| ------------------ | ------------------------------------------ | ----------------------------------------------- | ------ | ---- | ------ |
| Key                | Request.Operation.Concat.Fragments.Decrypt | 解密的 Key，当 Method 为 XIAOYI 时，此值对应 pwd      | String | 是   | 无     |
| Salt               | Request.Operation.Concat.Fragments.Decrypt | 额外的处理参数，当 Method 为 XIAOYI 时，此值对应 uid | String | 否   | 无     |
| Method             | Request.Operation.Concat.Fragments.Decrypt | 解密方法，取值为 XIAOYI                         | String | 否   | AES    |

Container 类型 Audio 的具体数据描述如下：

| 节点名称（关键字） | 父节点                         | 描述         | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------------------------ | ------------ | ------ | ---- | ------ | ------------------------------------------------------------ |
| Codec              | Request.Operation.Concat.Audio | 编解码格式   | String | 否   | aac    | 取值 aac、mp3                                                |
| Samplerate         | Request.Operation.Concat.Audio | 采样率       | String | 否   | 44100  | 1. 单位：Hz<br/>2. 可选 11025、22050、32000、44100、48000、96000<br/>3. 不同的封装，mp3 支持不同的采样率，如下表所示 |
| Bitrate            | Request.Operation.Concat.Audio | 音频码率     | String | 否   | 无     | 1. 单位：Kbps<br/>2. 值范围：[8，1000]                       |
| Channels           | Request.Operation.Concat.Audio | 声道数       | String | 否   | 无     | 1. 当Codec设置为aac，支持1、2、4、5、6、8<br/>2. 当Codec设置为mp3，支持1、2 |
| Remove             | Request.Operation.Concat.Audio | 是否删除音频 | String | 否   | false  | 取值 true、false                                             |

采样率 Samplerate 与封装格式的支持情况如下表，Y 表示支持这种采样率，N 表示不支持。

| 封装格式/音频采样率 | 11025 | 22050 | 32000 | 44100 | 48000 | 96000 |
| ------------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| mp3                 | Y     | Y     | Y     | Y     | Y     | N     |
| aac                 | Y     | Y     | Y     | Y     | Y     | Y     |

Container 类型 Container 的具体数据描述如下：

| 节点名称（关键字） | 父节点                             | 描述                                  | 类型   | 必选 |
| ------------------ | ---------------------------------- | ------------------------------------- | ------ | ---- |
| Format             | Request.Operation.Concat.Container | 容器格式: mp4、flv、hls、ts、mp3、aac | String | 是   |

设定 container，音频视频支持的格式如下表：

| Container                  | Audio Codecs  | Video Codecs          |
| -------------------------- | ------------- | --------------------- |
| mp4/ts/hls                 | AAC、MP3      | H.264、H.265          |
| flv                        | AAC、MP3      | H.264                 |
| aac                        | aac           | 不支持                |
| mp3                        | mp3           | 不支持                |

Container 类型 Video 的具体数据描述如下：

| 节点名称（关键字） | 父节点                         | 描述               | 类型   | 是否必选 | 默认值       | 限制                                                         |
| ------------------ | ------------------------------ | ------------------ | ------ | ---- | ------------ | ------------------------------------------------------------ |
| Codec              | Request.Operation.Concat.Video | 编解码格式         | String | 否   | H.264        | 1. H.264；2.H.265                                            |
| Width              | Request.Operation.Concat.Video | 宽                 | String | 否   | 视频原始宽度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Width 时，按照视频原始比例计算 Height |
| Height             | Request.Operation.Concat.Video | 高                 | String | 否   | 视频原始高度 | 1. 值范围：[128，4096]<br/>2. 单位：px<br/>3. 若只设置 Height 时，按照视频原始比例计算 Width |
| Fps                | Request.Operation.Concat.Video | 帧率               | String | 否   | 无           | 1. 值范围：(0，60]<br>2. 单位：fps                           |
| Profile            | Request.Operation.Concat.Video | 编码级别           | String | 否   | high         | 1. 支持 baseline、main、high<br/>2. baseline：适合移动设备；<br/>3. main：适合标准分辨率设备；<br/>4. high：适合高分辨率设备;<br/>5. 仅H.264支持此参数。 |
| Bitrate            | Request.Operation.Concat.Video | 视频输出文件的码率 | String | 否   | 无           | 1. 值范围：[10，50000]<br/>2. 单位：Kbps                     |
| Remove             | Request.Operation.Concat.Video | 是否删除视频流     | String | 否   | false        | 取值 true、false                                             |

Container 类型 AudioMix 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述         | 类型   | 是否必选 | 默认值 | 限制    |
| ----------------- | ------------------------------ | ------------ | ------ | ---- | ------ | ---------------------------- |
| AudioSource       | Request.Operation.Concat.AudioMix | 需要被混音的音轨媒体地址  | String | 是   | 无  | 需与 Input 媒体文件存储于同一 bucket |
| MixMode           | Request.Operation.Concat.AudioMix | 混音模式  | String | 否   | Repeat| 1. Repeat:背景音循环<br/>2. Once:背景音一次播放|
| Replace           | Request.Operation.Concat.AudioMix | 是否用混音音轨媒体替换 Input 媒体文件的原音频  | String | 否   | false  | true/false|
| EffectConfig      | Request.Operation.Concat.AudioMix | 混音淡入淡出配置  | Container | 否   | false  | 无|

Container 类型 EffectConfig 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述         | 类型   | 是否必选 | 默认值 | 限制    |
| ----------------- | ------------------------------ | ------------ | ------ | ---- | ------ | ---------------------------- |
| EnableStartFadein | Request.Operation.Concat.AudioMix.EffectConfig | 开启淡入  | String | 否   | false       | true/false |
| StartFadeinTime   | Request.Operation.Concat.AudioMix.EffectConfig | 淡入时长  | String | 否   | 无    | 大于0，支持浮点数|
| EnableEndFadeout  | Request.Operation.Concat.AudioMix.EffectConfig | 开启淡出  | String | 否   | false       | true/false |
| EndFadeoutTime    | Request.Operation.Concat.AudioMix.EffectConfig | 淡出时长  | String | 否   | 无    | 大于0，支持浮点数|
| EnableBgmFade     | Request.Operation.Concat.AudioMix.EffectConfig | 开启 bgm 转换淡入  | String | 否   | false       | true/false |
| BgmFadeTime       | Request.Operation.Concat.AudioMix.EffectConfig | bgm 转换淡入时长  | String | 否   | 无    | 大于0，支持浮点数|

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Request.Operation.Output | 存储桶的地域                                                | String | 是   |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                              | String | 是   |
| Object             | Request.Operation.Output | 输出结果的文件名                                             | String | 是   |

Container 类型 Notify 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                           | 类型   | 是否必选 | 默认值 |
| ------------------ | ------------------------ | -------- | ------ | ---- |
| Url                | Request.Operation.Notify | 通知地址 | String | 是   | 无 |
| ContentType        | Request.Operation.Notify | 内容格式。可选 XML、JSON。 | String | 否   | XML    |

Container 类型 Watermark 的具体数据描述如下：

| 节点名称（关键字） | 描述         | 类型      | 是否必选 | 默认值 | 取值介绍                                                     |
| ------------------ | ------------ | --------- | ---- | ------ | ------------------------------------------------------------ |
| Type               | 水印类型     | String    | 是   | 无     | Text：文字水印、Image：图片水印                          |
| Pos                | 基准位置     | String    | 是   | 无     | 1. TopRight、TopLeft、BottomRight、BottomLeft<br/>2.当 Image.Mode 为 Cover 时，此参数值无效 |
| LocMode            | 偏移方式     | String    | 是   | 无     | 1. Relativity：按比例、Absolute：固定位置<br/>2.当 Image.Mode 为 Cover 时，此参数值无效 |
| Dx                 | 水平偏移     | String    | 是   | 无     | 1. 当 LocMode 为 Relativity 时，单位为%，取值范围：[0 100] <br/>2. 当 LocMode 为 Absolute 时，单位为 px，取值范围：[0 4096]<br/>3.当 Image.Mode 为 Cover 时，此参数值无效 |
| Dy                 | 垂直偏移     | String    | 是   | 无     | 1. 当 LocMode 为 Relativity 时，单位为%，取值范围：[0 100] <br/>2. 当 LocMode 为 Absolute 时，单位为px，值范围：[0 4096]<br/>3.当 Image.Mode 为 Cover 时，此参数值无效 |
| Image              | 图片水印节点 | Container | 否   | 无     | 无                                                           |
| Text               | 文本水印节点 | Container | 否   | 无     | 无                                                           |


Container 类型 Image 的具体数据描述如下：

| 节点名称（关键字） | 描述                            | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------------------------------- | ------ | ---- | ------ | ------------------------------------------------------------ |
| Url                | 水印图地址(需要 Urlencode 后传入) | String | 是   | 无     | 水印图片地址                                              |
| Mode               | 尺寸模式                        | String | 是   | 无     | 1. Original: 原有尺寸 <br/>2. Proportion: 按比例 <br/>3. Fixed: 固定大小<br/>4. Cover: 覆盖整个视频 |
| Width              | 宽                              | String | 否   | 无     | 1. 当 Mode 为 Original 时，值为水印图宽 <br/>2. 当 Mode 为 Proportion 时，单位为%，值范围：[1 100]<br/>3. 当 Mode 为 Fixed 时，单位为 px，取值范围：[1，4096]<br/>4. 当 Mode 为 Cover 时，值无效<br/>5. 若只设置 Width 时，按照视频原始比例计算 Height |
| Height             | 高                              | String | 否   | 无     | 1. 当 Mode 为 Original 时，值为水印图高 <br/>2. 当 Mode 为 Proportion 时，单位为%，值范围：[1 100]<br/>3. 当 Mode 为 Fixed 时，单位为 px，取值范围：[1，4096]<br/>4. 当 Mode 为 Cover 时，值无效<br/>5.若只设置 Height 时，按照视频原始比例计算 Width |
| Transparency       | 透明度                          | String | 是   | 无     | 值范围：[1 100]，单位为%                                    |

水印位置说明：

![](https://qcloudimg.tencent-cloud.cn/raw/20b7a6ecc16b125f71052c6824d1cbb5.png)

Container 类型 Text 的具体数据描述如下：

| 节点名称（关键字） | 描述     | 类型   | 是否必选 | 默认值 | 限制                                                   |
| ------------------ | -------- | ------ | ---- | ------ | ------------------------------------------------------ |
| FontSize           | 字体大小 | String | 是   | 无     | 值范围：[5 100]，单位 px                             |
| FontType           | 字体类型 | String | 是   | 无     | 参考下表                                            |
| FontColor          | 字体颜色 | String | 是   | 无     | 格式：0xRRGGBB                                      |
| Transparency       | 透明度   | String | 是   | 无     | 值范围：[1 100]，单位%                              |
| Text               | 水印内容 | String | 是   | 无     | 长度不超过64个字符，仅支持中文、英文、数字、_、-和* |

Text 的 FontType 具体数据描述如下：

| 字体名称               | 支持的语言             | 描述|
| ------------------     | -------                | ------|
| simfang.ttf            |  中/英                 | 仿宋|
| simhei.ttf             |  中/英                 | 黑体|
| simkai.ttf             |  中/英                 | 楷体|
| simsun.ttc             |  中/英                 | 宋体|
| STHeiti-Light.ttc      |  中/英                 | 华文黑体|
| STHeiti-Medium.ttc     |  中/英                 | 华文黑体中|
| youyuan.TTF            |  中/英                 | 幼圆|
| ariblk.ttf             |  英                    | 无|
| arial.ttf              |  英                    | 无|
| ahronbd.ttf            |  英                    | 无|
| Helvetica.dfont        |  英                    | 无|
| HelveticaNeue.dfont    |  英                    | 无|

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
  <JobsDetail>
    <Code></Code>
    <Message></Message>
    <JobId></JobId>
    <State></State>
    <CreationTime></CreationTime>
    <EndTime></EndTime>
    <ProjectId></ProjectId>
    <Tag>Concat</Tag>
    <Operation>
      <Concat></Concat>
      <Output>
        <Region></Region>
        <Bucket></Bucket>
        <Object></Object>
      </Output>
    </Operation>
  </JobsDetail>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息 |  Container |


Container 节点 JobsDetail 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Code | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义 |  String |
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| Tag | Response.JobsDetail | 新创建任务的 Tag：Concat | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| ProjectId | Response.JobsDetail | 任务所属的项目 ID |  String |
| Operation | Response.JobsDetail | 该任务的规则 |  Container |

Container 节点 Operation 的内容：
同请求中的 Request.Operation 节点。

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求

```plaintext
POST /project/p893bcda225bf4945a378da6662e81a89/jobs HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1660
Content-Type: application/xml

<Request>
  <Tag>Concat</Tag>
  <Operation>
    <Concat>
        <Fragments>
            <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
        </Fragments>
        <Fragments>
            <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
        </Fragments>
        <Audio>
            <Codec>mp3</Codec>
            <Samplerate></Samplerate>
            <Bitrate></Bitrate>
            <Channels></Channels>
        </Audio>
        <Video>
            <Codec>H.264</Codec>
            <Bitrate>1000</Bitrate>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
        </Video>
        <Container>
            <Format>mp4</Format>
        </Container>
    </Concat>
    <Output>
      <Region>ap-beijing</Region>
      <Bucket>aabc-1250000000</Bucket>
      <Object>concat.mp4</Object>
    </Output>
  </Operation>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>je8f65004eb8511eaaed4f377124a303c</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <EndTime></EndTime>
    <ProjectId>p893bcda225bf4945a378da6662e81a89</ProjectId>
    <Tag>Concat</Tag>
    <Operation>
      <Concat>
        <Fragments>
            <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
        </Fragments>
        <Fragments>
            <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
        </Fragments>
        <Audio>
            <Codec>mp3</Codec>
            <Samplerate></Samplerate>
            <Bitrate></Bitrate>
            <Channels></Channels>
        </Audio>
        <Video>
            <Codec>H.264</Codec>
            <Bitrate>1000</Bitrate>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
        </Video>
        <Container>
            <Format>mp4</Format>
        </Container>
      </Concat>
      <Output>
        <Region>ap-beijing</Region>
        <Bucket>aabc-1250000000</Bucket>
        <Object>concat.mp4</Object>
      </Output>
    </Operation>
  </JobsDetail>
</Response>
```
