## 功能描述

用于获取设备本地录像 URL 地址。

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

<table>
<thead>
<tr>
<th width=10%>字段名</th>
<th width=10%>类型</th>
<th width=10%>描述</th>
<th width=10%>是否必须</th>
<th width=40%>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td>ChannelId</td>
<td>string</td>
<td>通道 ID</td>
<td>是</td>
<td>-</td>
</tr>
<tr>
<td>Start</td>
<td>int64</td>
<td>起始时间</td>
<td>是</td>
<td>-</td>
</tr>
<tr>
<td>End </td>
<td>int64</td>
<td> 结束时间</td>
<td>是</td>
<td>-</td>
</tr>
<tr>
<td>StreamType</td>
<td>int</td>
<td>流类型</td>
<td>否</td>
<td><li>主码流<li>子码流（不可以和 Resolution 同时下发）</td>
</tr>
<tr>
<td>Resolution</td>
<td>string</td>
<td>分辨率</td>
<td>否</td>
<td><li>QCIF<li>CIF<li>4CIF<li>D1<li>720P<li>1080P/I<li> 自定义的19201080等等（需设备支持） （不可以和 StreamType 同时下发）</td>
</tr>
</tbody>
</table>

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
| RequestId  | string | 请求 ID                           |   -   |
| Code       | int    | 状态码，0 成功，500 操作失败     |   -   |
| StatusCode | int    | 错误码，200 OK，其他详见错误中心 |    -  |
| Message    | string | 返回消息                         |     - |
| Data       | object | 返回结果                         |    -  |

+ Data

| 字段名 | 类型   | 描述         | 备注 |
| :----- | :----- | :----------- | :--- |
| Flv    | string | 录像播放地址 |  -    |
