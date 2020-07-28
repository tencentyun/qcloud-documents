## 功能描述

DescribeDocProcessBuckets 接口用于查询存储桶是否已开通文档预览功能。

## 请求

#### 请求示例

```shell
GET /docbucket?pageNumber=1&pageSize=2 HTTP/1.1
Host: ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

| 名称        | 描述                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | -------- |
| regions     | 地域信息，以“,”分隔字符串，支持 All、ap-shanghai、ap-beijing | string | 否       |
| bucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索              | string | 否       |
| bucketName  | 存储桶名称前缀，前缀搜索                                     | string | 否       |
| pageNumber  | 第几页                                                       | string | 否       |
| pageSize    | 每页个数                                                     | string | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
        <TotalCount>1</TotalCount>
        <RequestId>RequestId</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>2</PageSize>
        <DocBucketList>
                <Name>BucketName-APPID</Name>
                <CreateTime>Time</CreateTime>
                <Region>Region</Region>
                <AliasBucketId/>
                <BucketId>BucketName-APPID</BucketId>
        </DocBucketList>
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
| TotalCount         | Response | 文档预览 Bucket 总数            | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| DocBucketList      | Response | 文档预览 Bucket 列表            | Container |

Container 节点 DocBucketList 的内容：

| 节点名称（关键字） | 父节点                 | 描述                    | 类型   |
| :----------------- | :--------------------- | :---------------------- | :----- |
| BucketId           | Response.DocBucketList | 存储桶 ID               | String |
| Name               | Response.DocBucketList | 存储桶名称，同 BucketId | String |
| Region             | Response.DocBucketList | 所在的地域              | String |
| CreateTime         | Response.DocBucketList | 创建时间                | String |
| AliasBucketId      | Response.DocBucketList | 存储桶别名              | String |


#### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求 

```plaintext
GET /docbucket?regions=ap-chongqing HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: Authorization
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:00:43 GMT
Content-Type: application/xml
Content-Length: 843
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTdiOWJfYzc2OTQzNjRfM2Qz****

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>3</TotalCount>
        <RequestId>NWYxZTdiOWJfYzc2OTQzNjRfM2Qz****</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <DocBucketList>
                <Name>examplebucket-1250000000</Name>
                <CreateTime>2020-07-27T10:54:42+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>examplebucket-1250000000</BucketId>
        </DocBucketList>
        <DocBucketList>
                <Name>examplebucket-1250000000</Name>
                <CreateTime>2020-07-24T22:42:26+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>examplebucket-1250000000</BucketId>
        </DocBucketList>
</Response>
```

