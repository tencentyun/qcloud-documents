
## 功能描述

CreateAITask 用于创建 AI 任务。（当前AI是对已通过录像计划功能拉流上云的数据进行分析）

```shell
POST /ivc/ai/task HTTP/1.1
```

#### 请求参数

```json
{
  "Name": "ai-task-test",
  "Desc": "xxx",
  "ChannelList": [
    "channelId01",
    "channelId02"
  ],
  "CallbackUrl": "http://xxx",
  "IsStartTheTask": true,
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
    },
    {
      "Tag": "AI",
      "AIConfig": {
        "DetectType": "Pet",
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
  ]
}
```

具体数据描述如下：

| 参数名称       | 类型    | 描述               | 必选 | 备注                                                         |
| :------------- | :------ | :----------------- | :--- | :----------------------------------------------------------- |
| Name           | String  | AI 任务名称        | 是   | 仅支持中文、英文、数字、_、-，长度不超过32个字符；           |
| Desc           | String  | AI 任务描述        | 否   | 仅支持中文、英文、数字、_、-，长度不超过128个字符；          |
| ChannelList    | Array   | 通道 ID 列表       | 是   | 不能添加存在于其他 AI 任务的通道，限制1000个通道。             |
| CallbackUrl    | String  | AI 结果回调地址     | 否   | 类似"http://ip:port/xxx"或者"https://domain/xxx"             |
| IsStartTheTask | Boolean | 是否立即开启 AI 任务 | 否   | "true"代表立即开启 AI 任务，"false"代表暂不开启 AI 任务，默认为 false。 |
| Templates      | Array   | AI 配置列表         | 是   | AI 的配置列表。                                               |

Templates 具体描述如下：

| 参数名称       | 类型   | 描述       | 必选 | 备注                                                         |
| :------------- | :----- | :--------- | :--- | :----------------------------------------------------------- |
| Tag            | String | AI 类别    | 是   | 可选值 AI(AI分析)和 Snapshot(截图)，Templates 列表中只能出现一种类型。 |
| AIConfig       | Object | AI 分析配置 | 否   | 和"SnapshotConfig"二选一。                                   |
| SnapshotConfig | Object | 截图配置   | 否   | 和"AIConfig"二选一。                                         |

AIConfig 具体描述如下：

| 参数名称     | 类型    | 描述             | 必选 | 备注                                                         |
| :----------- | :------ | :--------------- | :--- | :----------------------------------------------------------- |
| DetectType   | String  | AI 分析类型       | 是   | 可选值为 Facemask(口罩识别)、Chefhat(厨师帽识别)、Smoking(抽烟检测)、Chefcloth(厨师服识别)、PhoneCall(接打电话识别)、Pet(宠物识别)、Body(人体识别)和Car(车辆车牌识别)等 |
| TimeInterval | Integer | 截图频率         | 是   | 可选值1～20秒                                                |
| OperTimeslot | String  | 模板生效的时间段 | 是   | 最多包含5组时间段                                            |

OperTimeslot 具体描述如下：

| 参数名称 | 类型   | 描述     | 必选 | 备注                                 |
| :------- | :----- | :------- | :--- | :----------------------------------- |
| Start    | String | 开始时间 | 是   | 格式为"hh:mm:ss"，且Start必须小于 End |
| End      | String | 结束时间 | 是   | 格式为"hh:mm:ss"，且Start必须小于 End |

SnapshotConfig 具体描述如下：

| 参数名称     | 类型    | 描述             | 必选 | 备注              |
| :----------- | :------ | :--------------- | :--- | :---------------- |
| TimeInterval | Integer | 截图频率         | 是   | 可选值1～20秒     |
| OperTimeslot | String  | 模板生效的时间段 | 否   | 最多包含5组时间段 |

#### 返回结果

```shell
{
  "Code": 0,
  "StatusCode": 200,
  "Message": "ok",
  "RequestId": "MTgzNWRlODdhZjJfYzkzNGI5MGJfMF83OA==",
  "Data": {
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
      },
      {
        "Tag": "AI",
        "AIConfig": {
          "DetectType": "Pet",
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
}
```

具体的数据内容如下：

| 名称       | 类型    | 描述      |
| :--------- | :------ | :-------- |
| Code       | Integer | 响应 code |
| StatusCode | Integer | 状态 code |
| Message    | String  | 响应消息  |
| RequestId  | String  | requestId |
| Data       | Object  | 返回信息  |

Data 的内容：

| 参数名称    | 类型    | 描述                                                         |
| :---------- | :------ | :----------------------------------------------------------- |
| TaskId      | String  | AI 任务 ID                                                   |
| Name        | String  | AI 任务名称                                                  |
| Desc        | String  | AI 任务描述                                                  |
| Status      | Integer | AI 任务状态。"on"代表开启了 AI 分析任务，"off"代表停止 AI 分析任务 |
| ChannelList | Array   | 通道 ID 列表                                                 |
| CallbackUrl | String  | AI 结果回调地址                                               |
| Templates   | Array   | AI 配置列表                                                  |
| CreatedTime | String  | 创建时间                                                     |
| UpdatedTime | String  | 更新时间                                                     |
