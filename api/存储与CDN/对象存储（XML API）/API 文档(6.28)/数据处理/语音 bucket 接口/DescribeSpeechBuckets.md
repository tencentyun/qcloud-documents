## 功能描述

DescribeSpeechBuckets 接口用于查询存储桶是否已开通语音识别功能。

## 请求

#### 请求示例

```shell
GET /asrbucket HTTP/1.1
Host: ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
```

>?
- 此接口 Host 需要填写数据万象域名。
- Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称        | 描述                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | -------- |
| regions     | 地域信息，以“,”分隔字符串，支持 All、ap-shanghai、ap-beijing | string | 否       |
| bucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索              | string | 否       |
| bucketName  | 存储桶名称前缀，前缀搜索                                     | string | 否       |
| pageNumber  | 第几页                                                       | string | 否       |
| pageSize    | 每页个数                                                     | string | 否       |

#### 请求头

此接口仅使用公共请求头部，详情请参见数据万象 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见数据万象 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <SpeechBucketList>
        <BucketId></BucketId>
        <Region></Region>
        <CreateTime></CreateTime>
    </SpeechBucketList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 媒体 Bucket 总数                | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| SpeechBucketList   | Response | 语音 Bucket 列表                | Container |

Container 节点 SpeechBucketList 的内容：

| 节点名称（关键字） | 父节点                   | 描述                    | 类型   |
| :----------------- | :----------------------- | :---------------------- | :----- |
| BucketId           | Response.MediaBucketList | 存储桶 ID               | String |
| Name               | Response.MediaBucketList | 存储桶名称，同 BucketId | String |
| Region             | Response.MediaBucketList | 所在的地域              | String |
| CreateTime         | Response.MediaBucketList | 创建时间                | String |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见数据万象 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

**请求：查询是否已开通语音识别功能**

```plaintext
GET /asrbucket HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKIDnOr9IDiIUNYWGrrWb2IJ4YmywDXc****&q-sign-time=1597999958;1598010018&q-key-time=1597999958;1598010018&q-header-list=content-type;host&q-url-param-list=&q-signature=a3ae564aa6f9798a4a7389badf3cb54a59f7****
```

**响应**

```plaintext
HTTP/1.1 200 OK
Date: Fri, 21 Aug 2020 08:53:38 GMT
Content-Type: application/xml
Content-Length: 1309
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYzZjhiOTJfOTBmYTUwNjRfMjJi****

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>5</TotalCount>
        <RequestId>NWYzZjhiOTJfOTBmYTUwNjRfMjJi****</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <AsrBucketList>
                <Name>examplebucket-1250000000</Name>
                <CreateTime>2020-05-26T13:31:41+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>examplebucket-1250000000</BucketId>
        </AsrBucketList>
</Response>
```



