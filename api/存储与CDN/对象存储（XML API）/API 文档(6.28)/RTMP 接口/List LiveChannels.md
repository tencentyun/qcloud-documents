## 功能描述

List LiveChannels 接口用于列举指定存储桶内的部分或者全部通道（Live Channel）。

## 请求

#### 请求示例

```plaintext
GET /?live HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String
```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求参数

此接口使用的请求参数如下：

| 名称    | 描述                                         | 类型      | 是否必选  |
| :---------------------- | :------------------------------------------- | :-------- | --------- |
| max-keys | 每页可以列出通道数量的最大值，有效值范围为[1, 1000]，默认值：100 | String | 否 |
| prefix | 限定返回的 LiveChannel 必须以 prefix 作为前缀。注意：使用 prefix 查询时，返回的 key 中仍会包含 prefix。 | String | 否 |
| marker | 设定结果从 marker 之后按字母排序的第一个开始返回。 | String | 否 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

响应体示例如下：

```plaintext
<ListLiveChannelResult>
	<MaxKeys></MaxKeys>
	<Prefix></Prefix>
	<IsTruncated>true</IsTruncated>
	<NextMarker>channel-0</NextMarker>
    <LiveChannel>
        <Name>String</Name>
        <LastModified>String</LastModified>
    </LiveChannel>
    <LiveChannel>
      ...
    </LiveChannel>
</ListSignalingChannelsResult>
```

该请求返回的响应体节点描述如下：

| 节点名称（关键字）      | 父节点                  | 描述                                         | 类型      |
| :---------------------- | :---------------------- | :------------------------------------------- | :-------- |
| ListLiveChannelResult | 无 | 保存列举通道结果的所有信息 | Container |
| MaxKeys | ListLiveChannelResult | 每页可以列出通道数量的最大值                       | String |
| Prefix | ListLiveChannelResult | 指定通道数量的最大值                       | String |
| IsTruncated | ListLiveChannelResult | 终止符，用于判断是否拥有下一页                       | String |
| NextMarker | ListLiveChannelResult | 指定通道数量的最大值                     | String |
| LiveChannel | ListLiveChannelResult | 列举出的通道信息                   | Container |
| Name | LiveChannel           | 通道名称                       | String |
| LastModified | SignalingChannelConfiguration                      |  LiveChannel 配置的最后修改时间。使用ISO8601格式  | String |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
GET /?live&max-keys=10&marker=test-channel-0 HTTP 1.1
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
<ListLiveChannelResult>
        <Prefix/>
        <Marker>test-channel-0</Marker>
        <MaxKeys>10</MaxKeys>
        <IsTruncated>true</IsTruncated>
        <NextMarker>test-channel-108</NextMarker>
        <LiveChannel>
                <Name>test-channel-1</Name>
                <LastModified>2020-11-29T02:58:31.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-100</Name>
                <LastModified>2020-11-26T03:47:41.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-101</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-102</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-103</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-104</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-105</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-106</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-107</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
        <LiveChannel>
                <Name>test-channel-108</Name>
                <LastModified>2020-11-25T12:07:45.000Z</LastModified>
        </LiveChannel>
</ListLiveChannelResult>
```
