## 功能描述
DescribeStreamRecord  用于查看国标历史流视频列表及下载，最多可支持3天时间。

## 请求

#### 请求示例

```plaintext
GET /device/stream/record?projectId=p15a20e50c92f4b089bf11bf77b558809&gbid=44010300001320000024&channelId=34020000001310000001&beginTime=1637735693543&endTime=1637735753536 HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。
>


#### 请求参数

Url 参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   是否必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| projectId   | 无        | 项目 ID                 | String     | 是 |
| gbid | 无        | 设备 GBID | String | 是 |
| channelId | 无 | 通道 ID | String | 是 |
| beginTime | 无 | 视频开始时间，毫秒时间戳 | String | 是 |
| endTime | 无 | 视频结束时间，毫秒时间戳 | String | 是 |
| prefix | 无 | 结果文件的前缀， 默认"/" (跟路径) | String | 否 |
| object | 无 | 结果文件的名称，默认是 “当前时间戳”.m3u8 | String | 否 |
| preSign | 无 | 生成的 m3u8 链接带不带预签名 | Boolean | 否 |


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <RequestId>NjBlZDViYjlfOTBmYTUwNjRfNGRiYV8x</RequestId>
    <Url>http://test-record-xxx.cos.ap-beijing.myqcloud.com/test-1.m3u8</Url>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container节点Response的内容：

| 节点名称（关键字） | 父节点   | 描述                | 类型   |
| :----------------- | :------- | :------------------ | :----- |
| RequestId          | Response | 请求 ID              | String |
| Url                | Response | 历史视频地址/可下载 | String |

#### 错误码

常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求


```plaintext
GET /recordstream?projectId=p1cf0d8f4d375478c830c88657357d81c&gbid=44010300001320000024&channelId=34020000001310000001&&beginTime=1616169600000&endTime=1616256000000 HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
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
   <RequestId>NjBlZDViYjlfOTBmYTUwNjRfNGRi****</RequestId>
   <Url>http://test-record-xxx.cos.ap-beijing.myqcloud.com/test-1.m3u8</Url>
</Response>

```
