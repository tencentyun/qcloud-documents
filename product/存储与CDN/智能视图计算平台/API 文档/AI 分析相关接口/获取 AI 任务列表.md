
## 功能描述

ListAITasks 用于获取 AI 任务列表。

```shell
GET /ivc/ai/tasks?IsContainChannelList=true&IsContainTemplate=true&PageNumber=1&PageSize=20 HTTP/1.1
```

#### 请求参数

| 字段名               | 类型    | 描述             | 必须 | 备注                                                         |
| :------------------- | :------ | :--------------- | :--- | :----------------------------------------------------------- |
| IsContainChannelList | Boolean | 是否包含通道列表 | 否   | "true"代表包含通道列表，"false"代表不包含通道列表，默认为 false。 |
| IsContainTemplate    | Boolean | 是否包含任务配置 | 否   | "true"代表包含任务配置，"false"代表不包含任务配置，默认为 false。 |
| PageNumber           | Integer | 页码             | 否   | 默认为1。                                                    |
| PageSize             | Integer | 每页数量         | 否   | 可选值1～200，默认为20。                                     |

#### 返回结果

```shell
{
  "Code": 0,
  "StatusCode": 200,
  "Message": "ok",
  "RequestId": "MTgzNWVjNjVlNzlfN2Q0ODI5MWVfMF8zYw==",
  "Data": {
    "TotalCount": 1,
    "List": [
      {
        "TaskId": "at553be1f6768a42698445e5d248fac1ac",
        "Name": "ai-task-test",
        "Desc": "xxx",
        "Status": "on",
        "ChannelList": [
          "channelId01",
          "channelId02"
        ],
        "CallbackUrl": "http://xxx",
        "Templates": [
          {
            "Tag": "AI",
            "AIConfig": {
              "DetectType": "Car",
              "TimeInterval": 10,
              "OperTimeslot": [
                {
                  "Start": "10:00:00",
                  "End": "11:00:00"
                },
                {
                  "Start": "13:00:00",
                  "End": "14:00:00"
                }
              ]
            }
          }
        ],
        "CreatedTime": "2022-11-01 11:27:03",
        "UpdatedTime": "2022-11-01 11:27:03"
      }
    ]
  }
}
```

具体的数据内容如下：

| 名称       | 类型    | 描述                                                         |
| ---------- | ------- | ------------------------------------------------------------ |
| Code       | Integer | 响应 code                                                    |
| StatusCode | Integer | 状态 code                                                    |
| Message    | String  | 响应消息                                                     |
| RequestId  | String  | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |
| Data       | Object  | 返回信息                                                     |

Data 的内容：

| 参数名称   | 类型    | 描述        |
| :--------- | :------ | :---------- |
| TotalCount | Integer | AI 任务数量 |
| List       | Array   | AI 任务列表 |

List 的内容：

| 参数名称    | 类型   | 描述                                                         |
| :---------- | :----- | :----------------------------------------------------------- |
| TaskId      | String | AI 任务 ID                                                   |
| Name        | String | AI 任务名称                                                  |
| Desc        | String | AI 任务描述                                                  |
| Status      | String | AI 任务状态。"on"代表开启了AI分析任务，"off"代表停止 AI 分析任务 |
| ChannelList | Array  | 通道 ID 列表                                                 |
| CallbackUrl | String | AI 结果回调地址                                               |
| Templates   | Array  | AI 配置列表                                                  |
| CreatedTime | String | 创建时间                                                     |
| UpdatedTime | String | 更新时间                                                     |

Templates 具体描述如下：

| 参数名称       | 类型   | 描述       |
| :------------- | :----- | :--------- |
| Tag            | String | AI 类别    |
| AIConfig       | Object | AI 分析配置 |
| SnapshotConfig | Object | 截图配置   |

AIConfig 具体描述如下：

| 参数名称     | 类型    | 描述             |
| :----------- | :------ | :--------------- |
| DetectType   | String  | AI 分析类型       |
| TimeInterval | Integer | 截图频率         |
| OperTimeslot | String  | 模板生效的时间段 |

OperTimeslot 具体描述如下：

| 参数名称 | 类型   | 描述     |
| :------- | :----- | :------- |
| Start    | String | 开始时间 |
| End      | String | 结束时间 |

SnapshotConfig 具体描述如下：

| 参数名称     | 类型    | 描述             |
| :----------- | :------ | :--------------- |
| TimeInterval | Integer | 截图频率         |
| OperTimeslot | String  | 模板生效的时间段 |
