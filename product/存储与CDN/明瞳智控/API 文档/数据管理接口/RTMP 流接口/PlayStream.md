## 功能描述
PlayStream 用于生成一个可供点播的播放列表。

## 请求

#### 请求示例

```plaintext
POST /stream/<StreamName>?ProjectId=xxx HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。



#### 请求参数
参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   是否必选    |
|:---           |:--         |:--                    |   :--     |   :--    |
| projectId     | 无         | 项目 Id                 | String     | 是 |



#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
    <PlaylistName></PlaylistName>
    <StartTime></StartTime>
    <EndTime></EndTime>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                     | 类型      | 是否必选 | 默认值 | 限制  |
| ------------------ | ------- | ------------------------------------- | --------- | ---- |----|----|
| PlaylistName       | Request | 指定生成的用于点播的 m3u8 文件的名称，生成的播放列表名为 StreamName/PlaylistName  | String    |是   | playlist.m3u8 | 必须以`.m3u8`结尾，长度范围为[6,128]|
| StartTime          | Request | 指定查询 ts 文件的起始时间                  | String | 是   | 无 | 格式为 Unix timestamp，单位：秒 |
| EndTime            | Request | 指定查询 ts 文件的终止时间                  | String | 是   | 无 | 格式为 Unix timestamp，单位：秒，EndTime 必须大于 StartTime，且时间跨度不能大于1天 |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext

<Response>
    <RequestId></RequestId>
    <StreamName>streamName</StreamName>
    <PlaylistName>playlistName</PlaylistName>
    <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                   | 类型      |
| :----------------- | :----- | :----------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| RequestId          | Response | 请求 ID                                                       | String    |
| StreamName         | Response | 流名称                                                       | String    |
| PlaylistName       | Response | 播放对象                                                     | String    |
| PlayUrl            | Response | 播放地址                                                     | String    |


#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求

```plaintext
POST /stream/<StreamName>?ProjectId=xxx HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<Request>
    <PlaylistName></PlaylistName>
    <StartTime></StartTime>
    <EndTime></Switch>
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
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzh****</RequestId>
    <StreamName>streamName</StreamName>
    <PlaylistName>playlistName</PlaylistName>
    <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
</Response>
```
