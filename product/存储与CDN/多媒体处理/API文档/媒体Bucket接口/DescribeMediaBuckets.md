## 功能描述

DescribeMediaBuckets 接口用于查询已经开通媒体处理功能的存储桶。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=DescribeMediaBuckets&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


## 请求

#### 请求示例

```shell
GET /mediabucket HTTP/1.1
Host: ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数



| 名称        |  描述                     | 类型   |是否必选 |
| :---------- | :----- | :------------------ | :------- |
| regions     |  地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066) |string |  否    |
| bucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索  |string |否 |
| bucketName  | 存储桶名称前缀，前缀搜索        |string |  否       |
| pageNumber  | 第几页                  |  string |否       |
| pageSize    | 每页个数                | string | 否       |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <MediaBucketList>
        <BucketId></BucketId>
        <Region></Region>
        <CreateTime></CreateTime>
    </MediaBucketList>
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
| MediaBucketList    | Response | 媒体 Bucket 列表                | Container |

Container 节点 MediaBucketList 的内容：

| 节点名称（关键字） | 父节点                   | 描述                    | 类型   |
| :----------------- | :----------------------- | :---------------------- | :----- |
| BucketId           | Response.MediaBucketList | 存储桶 ID               | String |
| Name               | Response.MediaBucketList | 存储桶名称，同 BucketId | String |
| Region             | Response.MediaBucketList | 所在的地域              | String |
| CreateTime         | Response.MediaBucketList | 创建时间                | String |

#### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
GET /mediabucket HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****



<Response>
      <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
      <TotalCount>1</TotalCount>
      <PageNumber>1</PageNumber>
      <PageSize>10</PageSize>
      <MediaBucketList>
            <BucketId></BucketId>
            <Region></Region>
            <CreateTime></CreateTime>
      </MediaBucketList>
      <MediaBucketList>
            <BucketId></BucketId>
            <Region></Region>
            <CreateTime></CreateTime>
      </MediaBucketList>
</Response>
```