## 功能描述
CreateStream 用于新增推流配置。

## 请求

#### 请求示例

```plaintext
POST /stream HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数
此接口无请求参数。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Name>streamName</Name>
    <Duration>5</Duration>
    <Type>HLS</Type>
    <Switch>Enabled</Switch>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点                         | 描述         | 类型   | 是否必选 | 默认值 | 限制                                                         |
| ------------------ | ------- | ---------------------------------------- | --------- | ---- |----|----|
| Name               | Request | 流名称。仅支持英文、数字      | String    | 是   | 无 | 不超过128个长度字符 |
| Duration           | Request | 录制周期                  | String    | 否   | 5 | 当 Type 为 HLS, 表示生成 ts 文件的时长，范围为[1,100] |
| Type               | Request | 录制格式                  | String | 否   | HLS | HLS |
| Switch             | Request | 推流状态                  | String | 否   | Enabled | Enabled，Disabled |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ProjectId          | Response | 项目 Id                                                       | String    |
| Name               | Response | 流名称                                                       | String    |
| Duration           | Response | 录制周期                                                     | String    |
| Type               | Response | 录制格式                                                     | String    |
| Switch             | Response | 推流状态                                                     | String    |
| StreamUrl          | Response | 推流地址                                                     | String    |
| PlayUrl            | Response | 播放地址                                                     | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| Bucket             | Response | 存储 Bucket 信息                                               | Container |

Container 类型 Bucket 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region            | Response.Bucket     | bucket 地域 | String      | 是   | 无 | 无|
| BucketId          | Response.Bucket     | bucket 的 ID | String      | 是   | 无  | 无 |
| Prefix            | Response.Bucket     | 对象 key 前缀 | String      | 否   | 无  | 无 |


#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求

```plaintext
POST /stream HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Name>streamName</Name>
    <Duration>5</Duration>
    <Type>HLS</Type>
</Request>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```
