## 功能描述

用于获取设备本地录像URL地址。

## 请求

#### 请求url

> POST /ivc/cms/control/record

#### 请求参数

该请求操作无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体

该请求操作的实现需要如下请求体。

```json
{
   "ChannelId": "0022c12a-e220-42e0-975f-800f872fc89e",
   "Start": 1231313123,
   "End": 123131231,
   "StreamType": 1,
   "Resolution": "3"
}
```

| 字段名     | 类型   | 描述     | 必须 | 备注                                                         |
| :--------- | :----- | :------- | :--- | :----------------------------------------------------------- |
| ChannelId  | string | 通道id   | 是   |                                                              |
| Start      | int64  | 起始时间 | 是   |                                                              |
| End        | int64  | 结束时间 | 是   |                                                              |
| StreamType | int    | 流类型   | 否   | 1：主码流；2：子码流（不可以和Resolution同时下发）           |
| Resolution | string | 分辨率   | 否   | 1.QCIF；2.CIF；3.4CIF；4.D1；5.720P；6.1080P/I; 自定义的19201080等等（需设备支持） （不可以和StreamType同时下发） |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体

该响应体返回为 **application/json** 数据，包含完整节点数据的内容展示如下：

```json
{
   "RequestId": "xxxxx",
   "Code": 0,
   "StatusCode": 200,
   "Message": "ok",
   "Data": {
      "Flv": "http://192.168.0.201:18080/live/5c46860f-8e2e-41bd-be5f-a5e47cab08df@c451066b-bc6d-46ba-86cd-53fc3c7c1d7c.live.flv?start=1656604800&end=1656608400&stream_type=1&resolution=6"
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

+Data

| 字段名 | 类型   | 描述         | 备注 |
| :----- | :----- | :----------- | :--- |
| Flv    | string | 录像播放地址 |      |

