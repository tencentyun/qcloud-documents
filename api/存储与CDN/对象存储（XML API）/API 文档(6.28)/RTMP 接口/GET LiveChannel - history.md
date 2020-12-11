## 功能描述

GET LiveChannel - history 接口用于获取指定通道（Live Channel）历史推流记录。该接口最多会返回10次推流记录。


>!如果通道超过90天没有推流，COS 将会清理它的推流记录。

## 请求

#### 请求示例

```plaintext
GET /<ChannelName>?live&comp=history HTTP 1.1
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

| 节点名称（关键字） | 父节点             | 描述                                    | 类型      |
| ------------------ | ------------------ | --------------------------------------- | --------- |
| LiveChannelHistory | 无                 | 保存 GetLiveChannelHistory 返回结果的容器 | Container |
| LiveRecord         | LiveChannelHistory | 保存一次推流记录信息的容器              | Container |
| StartTime          | LiveRecord         | 推流请求开始时间，使用 ISO8601格式       | String    |
| EndTime            | LiveRecord         | 推流请求结束时间，使用 ISO8601格式       | String    |
| RemoteAddr         | LiveRecord         | 推流客户端的 IP 地址                      | String    |
| RequestId          | LiveRecord         | 推流请求的 RequestId                     | String    |



#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例



#### 请求

```plaintext
GET /test-channel?live&comp=history HTTP 1.1
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
<LiveChannelHistory>
        <LiveRecord>
                <StartTime>2020-11-27T04:13:19Z</StartTime>
                <EndTime>2020-11-27T04:13:22Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMDdjZGZfODVjMTNiMGFfNmIw****</RequestId>
        </LiveRecord>57126
        <LiveRecord>
                <StartTime>2020-11-27T04:17:12Z</StartTime>
                <EndTime>2020-11-27T04:17:15Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMDdkYzhfODVjMTNiMGFfNmIw****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-27T07:28:09Z</StartTime>
                <EndTime>2020-11-27T07:28:16Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMGFhODlfODVjMTNiMGFfNmIy****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-27T07:41:12Z</StartTime>
                <EndTime>2020-11-27T07:41:15Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMGFkOThfODVjMTNiMGFfMjAyNV8y</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-27T07:50:09Z</StartTime>
                <EndTime>2020-11-27T07:50:15Z</EndTime>
                <RemoteAddr>10.59.193.160</RemoteAddr>
                <RequestId>NWZjMGFmYjFfNzhjMTNiMGFfNzdl****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-27T08:00:17Z</StartTime>
                <EndTime>2020-11-27T08:00:23Z</EndTime>
                <RemoteAddr>10.59.193.160:57126</RemoteAddr>
                <RequestId>NWZjMGIyMTFfNzhjMTNiMGFfMTA5****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-27T10:55:57Z</StartTime>
                <EndTime>2020-11-27T10:55:59Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMGRiM2RfODVjMTNiMGFfNmIy****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-28T07:49:00Z</StartTime>
                <EndTime>2020-11-28T07:49:23Z</EndTime>
                <RemoteAddr>127.0.0.1</RemoteAddr>
                <RequestId>NWZjMjAwZWNfODVjMTNiMGFfNmI0****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-28T08:10:15Z</StartTime>
                <EndTime>2020-11-28T08:10:22Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMjA1ZTdfODVjMTNiMGFfNmI1****</RequestId>
        </LiveRecord>
        <LiveRecord>
                <StartTime>2020-11-28T08:12:11Z</StartTime>
                <EndTime>2020-11-28T08:12:14Z</EndTime>
                <RemoteAddr>127.0.0.1:57126</RemoteAddr>
                <RequestId>NWZjMjA2NWJfODVjMTNiMGFfNmIy****</RequestId>
        </LiveRecord>
</LiveChannelHistory>
```



