## 功能描述

PUT LiveChannel 接口用于创建一个通道（Live Channel），用于传输音频、视频数据流。

>!
> - 只有存储桶的拥有者才能进行该请求操作。
> - 重复调用此接口创建同一通道接口会覆盖上一次创建的通道。但是当通道正处于推流状态时，禁止调用此接口覆盖通道。

## 请求

#### 请求示例

```plaintext
PUT /<ChannelName>?live HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String

XML Body
```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称        | 描述                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | :------- |
| ChannelName | 需符合对象键的命名规范。另外，ChannelName 不能包含斜杠（/），且不超过128个长度字符。 | string | 是       |




#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

```plaintext
<LiveChannelConfiguration>
  <Description>ChannelDescription</Description>
  <Switch>ChannelSwitch</Switch>
  <Target>
     <Type>HLS</Type>
     <FragDuration>FragDuration</FragDuration>
     <FragCount>FragCount</FragCount>
     <PlaylistName>PlaylistName</PlaylistName>
  </Target>
</LiveChannelConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）      | 父节点                  | 描述                                         | 类型      | 是否必选 |
| :---------------------- | :---------------------- | :------------------------------------------- | :-------- | ----------------------- |
| LiveChannelConfiguration | 无                      | 保存所有 LiveChannel 配置的容器  | Container | 是 |
| Description | LiveChannelConfiguration | 自定义的通道简述，上限为128字节      | String | 否 |
| Switch | LiveChannelConfiguration |  指定 LiveChannel 的开关状态，有效值：Enabled，Disabled。默认值：Enabled  | EnumString | 否 |
| Target | LiveChannelConfiguration |   保存转存配置的容器            | Container | 是 |
| Type | Target                |  指定转存的类型，有效值：HLS。<br/>说明：转储类型为 HLS 时，COS 在生成每个 ts 文件后更新 m3u8文件。m3u8文件中最多包含最近的 FragCount 个 ts 文件  | EnumString | 是 |
| FragDuration | Target                | 指定每个 ts 文件的时长，有效值范围为[1,100]，默认值：5。<br/>说明：FragDuration 和 FragCount 的默认值只有在两者都未指定时才会生效；指定了其中一个，则另一个的值也必须指定 | String | 否 |
| FragCount | Target | 指定 m3u8 文件中包含 ts 文件的个数，有效值范围为[1,100]。默认值：3。<br/>说明：FragDuration 和 FragCount 的默认值只有在两者都未指定时才会生效；指定了其中一个，则另一个的值也必须指定 | String | 否 |
| PlaylistName | Target | 指定生成的 m3u8文件的名称。必须以`.m3u8`结尾，长度范围为[6, 128]，默认值：playlist.m3u8。<br/>说明：生成的播放列表作为对象的对象名为`ChannelName/PlaylistName` | String | 否 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求返回的响应体节点描述如下：

| 节点名称（关键字）      | 父节点                  | 描述                                         | 类型      |
| :---------------------- | :---------------------- | :------------------------------------------- | :-------- |
| CreateLiveChannelResult | 无                      | 保存 CreateLiveChannel 请求结果的容器 | Container |
| PublishUrls | CreateLiveChannelResult | 保存推流地址的容器              | Container |
| Url | PublishUrls | 推流地址<br> 说明：这里返回的推流地址未加签名信息，可通过调用 SDK 或者参见 [RTMP 请求地址与签名](#跳转到 RTMP 请求地址与签名) 获取签名 | String |
| PlayUrls | CreateLiveChannelResult | 保存播放地址的容器 | Container |
| Url | PlayUrls | 播放地址 | String |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
PUT /test-channel?live HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String

<?xml version="1.0" encoding="utf-8"?>
<LiveChannelConfiguration>
    <Description/>
    <Switch>Enabled</Status>
    <Target>
        <Type>HLS</Type>
        <FragDuration>2</FragDuration>
        <FragCount>3</FragCount>
    </Target>
</LiveChannelConfiguration>
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
<CreateLiveChannelResult>
  <PublishUrls>
    <Url>rtmp://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/live/test-channel</Url>
  </PublishUrls>
  <PlayUrls>
    <Url>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/test-channel/playlist.m3u8</Url>
  </PlayUrls>
</CreateLiveChannelResult>
```
