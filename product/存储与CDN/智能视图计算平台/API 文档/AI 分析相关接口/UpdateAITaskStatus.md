
## 功能描述

UpdateAITaskStatus 用于更新 AI 任务状态。

```shell
PUT /ivc/ai/task/status?TaskId=xxx&Status=on HTTP/1.1
```

#### 请求参数

**path**

```
TaskId=xxx&Status=on
```

| 字段名 | 类型   | 描述        | 必须 | 备注                                              |
| :----- | :----- | :---------- | :--- | :------------------------------------------------ |
| TaskId | String | AI 任务 ID  | 是   |                                                   |
| Status | String | AI 任务状态 | 是   | "on"代表开启了AI分析任务，"off"代表停止AI分析任务 |

#### 返回结果

```shell
{
  "Code": 0,
  "StatusCode": 200,
  "Message": "ok",
  "RequestId": "MTgzNWRlODdhZjJfYzkzNGI5MGJfMF83OA=="
}
```

具体的数据内容如下：

| 名称       | 类型    | 描述      |
| :--------- | :------ | :-------- |
| Code       | Integer | 响应 code |
| StatusCode | Integer | 状态 code |
| Message    | String  | 响应消息  |
| RequestId  | String  | requestId |
