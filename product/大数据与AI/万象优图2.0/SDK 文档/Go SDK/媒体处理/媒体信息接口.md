## 简介

本文档提供关于媒体信息接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
|  [GetMediaInfo](https://cloud.tencent.com/document/product/436/55672)    |   查询文件信息 |用于查询媒体文件的信息      |


## 查询文件信息

#### 功能说明

用于查询媒体文件的信息。

>! COS Go SDK 版本需要大于等于 v0.7.32。

#### 方法原型

```go
func (s *CIService) GetMediaInfo(ctx context.Context, name string, opt *ObjectGetOptions, id ...string) (*GetMediaInfoResult, *Response, error)
```

#### 请求示例
```go
res, _, err := c.CI.GetMediaInfo(context.Background(), "test.mp4", nil)
if err != nil {
    // ERROR
}
fmt.Printf("res: %+v\n", res)
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 是否必填 |
| :------- | :----------------------------------------------------------- | :----- | :------- |
| name     | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg`中，对象键为 doc/pic.jpg | name   | 是       |
| opt      | 公共请求头部和参数，详见 [Get Object](https://cloud.tencent.com/document/product/436/35057#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1) | struct | 否       |
| id       | 针对版本控制的对象 VersionId                                 | string | 否       |

#### 返回结果说明

```go
type GetMediaInfoResult struct {
    XMLName   xml.Name
    MediaInfo struct {
        Format struct {
            Bitrate        float32
            Duration       float32
            FormatLongName string
            FormatName     string
            NumProgram     int
            NumStream      int
            Size           int
            StartTime      float32
        }
        Stream struct {
            Audio []struct {
                Index          int 
                CodecName      string
                CodecLongName  string
                CodecTimeBase  string
                CodecTagString string
                CodecTag       string
                SampleFmt      string
                SampleRate     int
                Channel        int
                ChannelLayout  string
                Timebase       string
                StartTime      float32
                Duration       float32
                Bitrate        float32
                Language       string
            }
            Subtitle struct {
                Index    int
                Language string
            }
            Video struct {
                Index          int
                CodecName      string
                CodecLongName  string
                CodecTimeBase  string
                CodecTagString string
                CodecTag       string
                Profile        string
                Height         int
                Width          int
                HasBFrame      int
                RefFrames      int
                Sar            string
                Dar            string
                PixFormat      string
                FieldOrder     string
                Level          int
                Fps            float32
                AvgFps         string
                Timebase       string
                StartTime      float32
                Duration       float32
                Bitrate        float32
                NumFrames      int
                Language       string
            }
        }
    }
}
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

| 节点名称（关键字） | 父节点                     | 描述     | 类型      |
| :----------------- | :------------------------- | :------- | :-------- |
| Video              | Response.MediaInfo. Stream | 视频信息 | Container |
| Audio              | Response.MediaInfo. Stream | 音频信息 | Container |
| Subtitle           | Response.MediaInfo. Stream | 字幕信息 | Container |

Container 节点 Format 的内容（查询视频信息时，可能部分字段未返回）：

| 节点名称（关键字） | 父节点                     | 描述                                        | 类型   |
| :----------------- | :------------------------- | :------------------------------------------ | :----- |
| NumStream          | Response.MediaInfo. Format | Stream（包含 Video、Audio、Subtitle）的数量 | Int    |
| NumProgram         | Response.MediaInfo. Format | 节目的数量                                  | Int    |
| FormatName         | Response.MediaInfo. Format | 容器格式名字                                | String |
| FormatLongName     | Response. MediaInfo.Format | 容器格式的详细名字                          | String |
| StartTime          | Response.MediaInfo. Format | 起始时间，单位为秒                          | Float  |
| Duration           | Response.MediaInfo. Format | 时长，单位为秒                              | Float  |
| Bitrate            | Response.MediaInfo. Format | 比特率，单位为 kbps                         | Int    |
| Size               | Response.MediaInfo. Format | 大小，单位为 Byte                           | Int    |

Container 节点 Video 的内容（查询视频信息时，可能部分字段未返回）：

| 节点名称（关键字） | 父节点                           | 描述                        | 类型   |
| :----------------- | :------------------------------- | :-------------------------- | :----- |
| Index              | Response.MediaInfo. Stream.Video | 该流的编号                  | Int    |
| CodecName          | Response.MediaInfo. Stream.Video | 编解码格式名字              | String |
| CodecLongName      | Response.MediaInfo. Stream.Video | 编解码格式的详细名字        | String |
| CodecTimeBase      | Response.MediaInfo. Stream.Video | 编码时基                    | String |
| CodecTagString     | Response.MediaInfo. Stream.Video | 编码标签名                  | String |
| CodecTag           | Response.MediaInfo. Stream.Video | 编码标签                    | String |
| Profile            | Response.MediaInfo. Stream.Video | 视频编码档位                | String |
| Height             | Response.MediaInfo. Stream.Video | 视频高，单位 px             | Int    |
| Width              | Response.MediaInfo. Stream.Video | 视频宽，单位 px             | Int    |
| HasBFrame          | Response.MediaInfo. Stream.Video | 是否有B帧。1表示有，0表示无 | Int    |
| RefFrames          | Response.MediaInfo. Stream.Video | 视频编码的参考帧个数        | Int    |
| Sar                | Response.MediaInfo. Stream.Video | 采样宽高比                  | String |
| Dar                | Response.MediaInfo. Stream.Video | 显示宽高比                  | String |
| PixFormat          | Response.MediaInfo. Stream.Video | 像素格式                    | String |
| FieldOrder         | Response.MediaInfo. Stream.Video | 场的顺序                    | String |
| Level              | Response.MediaInfo. Stream.Video | 视频编码等级                | Int    |
| Fps                | Response.MediaInfo. Stream.Video | 视频帧率                    | Int    |
| AvgFps             | Response.MediaInfo. Stream.Video | 平均帧率                    | String |
| Timebase           | Response.MediaInfo. Stream.Video | 时基                        | String |
| StartTime          | Response.MediaInfo. Stream.Video | 视频开始时间，单位为秒      | Float  |
| Duration           | Response.MediaInfo. Stream.Video | 视频时长，单位为秒          | Float  |
| Bitrate            | Response.MediaInfo. Stream.Video | 比特率，单位为 kbps         | Float  |
| NumFrames          | Response.MediaInfo. Stream.Video | 总帧数                      | Int    |
| Language           | Response.MediaInfo. Stream.Video | 语言                        | String |

Container 节点 Audio 的内容（查询视频信息时，可能部分字段未返回）：

| 节点名称（关键字） | 父节点                           | 描述                 | 类型   |
| :----------------- | :------------------------------- | :------------------- | :----- |
| Index              | Response.MediaInfo. Stream.Audio | 该流的编号           | Int    |
| CodecName          | Response.MediaInfo. Stream.Audio | 编解码格式名字       | String |
| CodecLongName      | Response.MediaInfo. Stream.Audio | 编解码格式的详细名字 | String |
| CodecTimeBase      | Response.MediaInfo. Stream.Audio | 编码时基             | String |
| CodecTagString     | Response.MediaInfo. Stream.Audio | 编码标签名           | String |
| CodecTag           | Response.MediaInfo. Stream.Audio | 编码标签             | String |
| SampleFmt          | Response.MediaInfo. Stream.Audio | 采样格式             | String |
| SampleRate         | Response.MediaInfo. Stream.Audio | 采样率               | Int    |
| Channel            | Response.MediaInfo. Stream.Audio | 通道数量             | Int    |
| ChannelLayout      | Response.MediaInfo. Stream.Audio | 通道格式             | String |
| Timebase           | Response.MediaInfo. Stream.Audio | 时基                 | String |
| StartTime          | Response.MediaInfo. Stream.Audio | 音频开始时间，单位秒 | Float  |
| Duration           | Response.MediaInfo. Stream.Audio | 音频时长，单位秒     | Float  |
| Bitrate            | Response.MediaInfo. Stream.Audio | 比特率，单位 kbps    | Float  |
| Language           | Response.MediaInfo. Stream.Audio | 语言                 | String |

Container 节点 Subtitle 的内容：

| 节点名称（关键字） | 父节点                              | 描述                     | 类型   |
| :----------------- | :---------------------------------- | :----------------------- | :----- |
| Index              | Response.MediaInfo. Stream.Subtitle | 该流的编号               | Int    |
| Language           | Response.MediaInfo. Stream.Subtitle | 语言，und 表示无查询结果 | String |
