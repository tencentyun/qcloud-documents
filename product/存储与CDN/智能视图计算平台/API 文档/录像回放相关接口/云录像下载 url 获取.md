## 功能描述

用于获取云录像下载url。

## 请求

#### 请求url

> POST /ivc/vds/VideoDownloadUrl

#### 请求参数

该请求操作无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体

该请求操作的实现需要如下请求体。

```json
{
   "ChannelId": "4dfb778c-fe2b-4892-92c6-ec361f59f4ab",
   "BeginTime": "1668996000",
   "EndTime": "1668996600",
   "FileType": "mp4"
}
```

| 字段名    | 类型   | 描述           | 必须 | 备注                                              |
| :-------- | :----- | :------------- | :--- | :------------------------------------------------ |
| ChannelId | string | 通道id         | 是   |                                                   |
| BeginTime | string | 下载的开始时间 | 是   | UTC秒数，开始和结束时间段最长为30分钟，且不能跨天 |
| EndTime   | string | 下载的结束时间 | 是   | UTC秒数，开始和结束时间段最长为30分钟，且不能跨天 |
| FileType  | string | 文件格式       | 是   | "mp4"：mp4格式，"ts"：ts文件格式                  |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体

该响应体返回为 **application/json** 数据，包含完整节点数据的内容展示如下：

```json
{
   "RequestId": "MTg0YzZhOWY5NmFfYjBkMDJmMWVfMF8xNw==",
   "Code": 0,
   "StatusCode": 200,
   "Message": "OK",
   "Data": {
      "Url": "https://somedomain.com/video.mp4?source=4dfb778c-fe2b-4892-92c6-ec361f59f4ab%3B1668996000%3B1668996600%3Bmp4&res=ba639f7f4f9b9d635fad97c589bc1e02&expires=600&signTime=1671000320&sign=3563a7f6401e9130e4204462d99bca3f"
   }
}
```

| 字段名     | 类型   | 描述                             | 备注 |
| :--------- | :----- | :------------------------------- | :--- |
| RequestId  | string | 请求id                           |      |
| Code       | int    | 状态码，0 成功，500 操作失败     |      |
| StatusCode | int    | 错误码，200 OK，其他详见错误中心 |      |
| Message    | string | 返回消息                         |      |
| Data       | object | 返回结果                         |      |

+ Data

| 字段名 | 类型   | 描述            | 备注                                                         |
| :----- | :----- | :-------------- | :----------------------------------------------------------- |
| Url    | string | 录像文件下载URL | 1）URL有效期是10分钟，过期后将拒绝访问，若需再用请重新获取 <br> 2）录像文件下载采用分块传输编码，响应头Transfer-Encoding:chunked <br> 3）下载文件命名格式为{ChannelId}-{BeginTime}-{EndTime}.{FileType} |

