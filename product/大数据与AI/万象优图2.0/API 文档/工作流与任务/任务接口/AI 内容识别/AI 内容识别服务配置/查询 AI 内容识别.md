## 功能描述

查询 AI 内容识别服务状态。


## 请求

#### 请求示例

```shell
GET /ai_bucket HTTP/1.1
Host: ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数



| 名称        |  描述                     | 类型   |是否必选 |
| :---------- | :----- | :------------------ | :------- |
| regions     |  地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066) |string |  否    |
| bucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索  |string |否 |
| bucketName  | 存储桶名称前缀，前缀搜索        |string |  否       |
| pageNumber  | 第几页，默认值1    | Int | 否     |
| pageSize    | 每页个数，默认值10 | Int | 否     |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NjJmMzY1Y2NfOTBmYTUwNjRfNTA5YV8y</RequestId>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>5</PageSize>
    <AiBucketList>
        <BucketId>test-1234567890</BucketId>
        <Name>test-1234567890</Name>
        <Region>ap-chongqing</Region>
        <CreateTime2022-08-08T16:23:11+0800></CreateTime>
    </AiBucketList>
    <AiBucketList>
        <BucketId>test-1-1234567890</BucketId>
        <Name>test-1-1234567890</Name>
        <Region>ap-chongqing</Region>
        <CreateTime2022-08-09T16:23:11+0800></CreateTime>
    </AiBucketList>
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
| AiBucketList    | Response | 媒体 Bucket 列表                | Container |

Container 节点 AiBucketList 的内容：

| 节点名称（关键字） | 父节点                   | 描述                    | 类型   |
| :----------------- | :----------------------- | :---------------------- | :----- |
| BucketId           | Response.AiBucketList | 存储桶 ID               | String |
| Name               | Response.AiBucketList | 存储桶名称，同 BucketId | String |
| Region             | Response.AiBucketList | 所在的地域              | String |
| CreateTime         | Response.AiBucketList | 创建时间                | String |

#### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /ai_bucket?regions=ap-chongqing&pageSize=5&bucketName=t HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: test-1234567890.ci.ap-chongqing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 09 Aug 2022 16:23:12 GMT
Server: tencent-ci
x-ci-request-id: NjJmMzY1Y2NfOTBmYTUwNjRfNTA5YV8y

<Response>
    <RequestId>NjJmMzY1Y2NfOTBmYTUwNjRfNTA5YV8y</RequestId>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>5</PageSize>
    <AiBucketList>
        <BucketId>test-1234567890</BucketId>
        <Name>test-1234567890</Name>
        <Region>ap-chongqing</Region>
        <CreateTime2022-08-08T16:23:11+0800></CreateTime>
    </AiBucketList>
    <AiBucketList>
        <BucketId>test-1-1234567890</BucketId>
        <Name>test-1-1234567890</Name>
        <Region>ap-chongqing</Region>
        <CreateTime2022-08-09T16:23:11+0800></CreateTime>
    </AiBucketList>
</Response>
```
