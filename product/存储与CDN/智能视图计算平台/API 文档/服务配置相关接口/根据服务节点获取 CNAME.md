## 功能描述

用于根据服务节点获取 CNAME 值。

## 请求

#### 请求url

> GET /ivc/cms/domain/cname?ClusterId=xxxxx

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```js
ClusterId = xxxx - xxxxxxx - xxxxxx - xxxxx
```

| 字段名    | 类型   | 描述       | 是否必须 | 备注 |
| :-------- | :----- | :--------- | :------- | :--- |
| ClusterId | string | 服务节点 ID | 是       |    -  |

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
   "Data": "xxxxxxxx.play-iss.ap-shanghai.tencentivc.cn"
}
```

| 字段名     | 类型   | 描述                             | 备注 |
| :--------- | :----- | :------------------------------- | :--- |
| RequestId  | string | 请求 ID                          |   -   |
| Code       | int    | 状态码，0 成功，500 操作失败     |    -  |
| StatusCode | int    | 错误码，200 OK，其他详见错误中心 | -     |
| Message    | string | 返回消息                         |   -   |
| Data       | object | 返回结果                         |  -    |

+ Data

| 字段名 | 类型   | 描述        | 是否必须 | 备注 |
| :----- | :----- | :---------- | :------- | :--- |
| Data   | string | CNAME 记录值 | 是       |   -   |
