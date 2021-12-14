## 功能描述
DescribeStreams 用于查找推流配置。

## 请求

#### 请求示例

```plaintext
GET /stream HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   是否必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| projectId     | 无        | 项目 Id                 | String     | 是 |
| name          | 无        | 流名称前缀              | String     | 否 |
| pageNumber    | 无        | 第几页                  | Integer    | 否 |
| pageSize      | 无        | 每页个数                | Integer    | 否 |



#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <StreamList>
        <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
        <Name>streamName</Name>
        <Duration>5</Duration>
        <Type>HLS</Type>
        <Switch>Enabled</Switch>
        <StreamUrl>rtmp://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/live/streamName</StreamUrl>
        <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
        <Bucket>
            <Region>ap-beijing</Region>
            <BucketId>examplebucket-1250000000</BucketId>
            <Prefix>/streamName</Prefix>
        </Bucket>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </StreamList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                           | 类型      |
| :----------------- | :------- | :----------------------------- | :-------- |
| TotalCount         | Response | 项目总数                       | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| StreamList        | Response | 流地址数组                       | Container |

Container节点 StreamList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ProjectId          | Response.StreamList | 项目 Id                                                       | String    |
| Name               | Response.StreamList | 流名称                                                       | String    |
| Duration           | Response.StreamList | 录制周期                                                     | String    |
| Type               | Response.StreamList | 录制格式                                                     | String    |
| Switch             | Response.StreamList | 推流状态                                                     | String    |
| StreamUrl          | Response.StreamList | 推流地址                                                     | String    |
| PlayUrl            | Response.StreamList | 播放地址                                                     | String    |
| UpdateTime         | Response.StreamList | 更新时间                                                     | String    |
| CreateTime         | Response.StreamList | 创建时间                                                     | String    |
| TemplateList       | Response.StreamList | 参考更新项目接口的模板列表                                     | Container |
| Bucket             | Response.StreamList | 存储 Bucket 信息                                               | Container |


Container 类型 Bucket 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region            | Response.StreamList.Bucket     | bucket 地域 | String      | 是   | 无 | 无|
| BucketId          | Response.StreamList.Bucket     | bucket 的 ID | String      | 是   | 无  | 无 |
| Prefix            | Response.StreamList.Bucket     | 对象 key 前缀 | String      | 否   | 无  | 无 |

Container 节点 TemplateList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId      | Response.StreamList.TemplateList | 模板 ID                                               | String    |
| Tag             | Response.StreamList.TemplateList | 模板类型                                               | String    |
| Name            | Response.StreamList.TemplateList | 模板名称                                               | String    |
| Status          | Response.StreamList.TemplateList | 模板状态                                               | String    |
| Notify          | Response.StreamList.TemplateList | 模板回调                                                | String    |
| Output          | Response.StreamList.TemplateList | 模板输出                                                | Container    |


Container节点 Output 的内容：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ |
| Region             | Response.StreamList.TemplateList.Output | 存储桶的地域                                   | String |
| Bucket             | Response.StreamList.TemplateList.Output | 存储结果的存储桶                                | String |
| Object             | Response.StreamList.TemplateList.Output | 结果文件名                                  | String |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 按照分页列表维度查询

#### 请求


```plaintext
GET /stream?name=stream HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <StreamList>
        <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
        <Name>streamName</Name>
        <Duration>5</Duration>
        <Type>HLS</Type>
        <Switch>Enabled</Switch>
        <StreamUrl>rtmp://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/live/streamName</StreamUrl>
        <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
        <Bucket>
            <Region>ap-beijing</Region>
            <BucketId>examplebucket-1250000000</BucketId>
            <Prefix>/streamName</Prefix>
        </Bucket>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <TemplateList>
            <TemplateId></TemplateId>
            <Tag></Tag>
            <Name></Name>
            <Status></Status>
            <Output>
                <Region>ap-beijing</Region>
                <Bucket>abc-1250000000</Bucket>
                <Object>snapshot-${Number}.jpg</Object>
            </Output>
            <Notify></Notify>
        </TemplateList>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </StreamList>
</Response>
```
