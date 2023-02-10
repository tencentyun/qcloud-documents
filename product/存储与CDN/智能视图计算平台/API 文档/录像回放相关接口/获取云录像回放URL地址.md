## 功能描述

用于获取云端录像回放 url 地址。

## 请求

#### 请求url

> GET /ivc/record/playback/url?ChannelId=xxx&StartTime=xxx&EndTime=xxx

#### 请求参数

该请求操作的实现需要有如下请求参数。

| 字段名    | 类型      | 描述         | 必须 | 备注                                                         |
| :-------- | :-------- | :----------- | :--- | :----------------------------------------------------------- |
| ChannelId | string    | 设备通道 ID  | 是   |             -                                                 |
| StartTime | timestamp | 回放开始时间 | 是   | UTC 秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天 |
| EndTime   | timestamp | 回放结束时间 | 是   | UTC 秒数，例如：1662114246，开始和结束时间段最长为一天，且不能跨天 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体

该请求操作无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体

该响应体返回为 **application/json** 数据，包含完整节点数据的内容展示如下：

```json
{
   "RequestId": "",
   "Code": 0,
   "StatusCode": 200,
   "Message": "ok",
   "Data": {
      "Hls": "https://somedomain.com/record/streamid/hls.m3u8?starttime=1662114146&endtime=1662114846&token="
   }
}
```

| 字段名     | 类型   | 描述                             | 备注 |
| :--------- | :----- | :------------------------------- | :--- |
| RequestId  | string | 请求 ID                          |    -  |
| Code       | int    | 状态码，0 成功，500 操作失败     |   -   |
| StatusCode | int    | 错误码，200 OK，其他详见错误中心 |  -    |
| Message    | string | 返回信息                         |    -  |
| Data       | object | 返回结果                         |   -   |

+ Data

| 字段名 | 类型   | 描述       | 备注 |
| :----- | :----- | :--------- | :--- |
| Hls    | string | hls 回放 url |   -   |
