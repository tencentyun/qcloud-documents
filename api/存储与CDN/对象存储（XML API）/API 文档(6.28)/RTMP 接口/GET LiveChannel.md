## 功能描述

GET LiveChannel 接口用于获取指定通道（Live Channel）的配置信息。

## 请求

#### 请求示例

```plaintext
GET /<ChannelName>?live HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String

```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数
此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求返回的响应体节点描述如下：

| 节点名称（关键字）       | 父节点                   | 描述                                                         | 类型       |
| ------------------------ | ------------------------ | ------------------------------------------------------------ | ---------- |
| LiveChannelConfiguration | 无                       | 保存 GetLiveChannel 返回结果的容器                             | Container  |
| Description              | LiveChannelConfiguration | 自定义的通道简述                                             | String     |
| Switch                   | LiveChannelConfiguration | 指定 LiveChannel 的开关状态，具体说明请参见 [PUT LiveChannel]() 中参数说明 | EnumString |
| Target                   | LiveChannelConfiguration | 保存转储配置的容器                                           | Container  |
| Type                     | Target                   | 指定转储的类型，具体说明请参见 [PUT LiveChannel]() 中参数说明        | EnumString |
| FragDuration             | Target                   | 指定每个 ts 文件的时长，具体说明请参见 [PUT LiveChannel]() 中参数说明  | String     |
| FragCount                | Target                   | 指定 m3u8 文件中包含 ts 文件的个数<br/>具体说明请参见 [PUT LiveChannel]() 中参数说明 | String     |
| PlaylistName             | Target                   | 指定生成的m3u8文件的名称，具体说明请参见 [PUT LiveChannel]() 中参数说明 | String     |
| PublishUrls              | Target                   | 保存推流地址的容器，具体说明请参见 [PUT LiveChannel]() 中参数说明    | String     |
| Url                      | PublishUrls              | 推流地址，具体说明请参见 [PUT LiveChannel]() 中参数说明              | String     |
| PlayUrls                 | Target                   | 保存播放地址的容器，具体说明请参见 [PUT LiveChannel]() 中参数说明    | String     |
| Url                      | PlayUrls                 | 播放地址，具体说明请参见 [PUT LiveChannel]() 中参数说明              | String     |



#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
GET /test-channel?live HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2020 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
 
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelConfiguration>
        <Description>description</Description>
        <Switch>Enabled</Switch>
        <Target>
                <Type>HLS</Type>
                <FragDuration>3</FragDuration>
                <FragCount>3</FragCount>
                <PlaylistName>playlist.m3u8</PlaylistName>
                <PublishUrls>
                        <Url>rtmp://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/live/test-channel</Url>
                </PublishUrls>
                <PlayUrls>
                        <Url>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/test-channel/playlist.m3u8</Url>
                </PlayUrls>
        </Target>
</LiveChannelConfiguration>
```
