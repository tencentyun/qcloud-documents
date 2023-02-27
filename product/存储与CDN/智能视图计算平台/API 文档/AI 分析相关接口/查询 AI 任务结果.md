
## 功能描述

GetAITaskResult 用于查询 AI 任务结果。

```shell
GET /ivc/ai/task/result?TaskId=xxx&ChannelId=channel01&Object=xxx&AIType=Pet&BeginTime=xxx&EndTime=xx HTTP/1.1
```

#### 请求参数

| 字段名     | 类型    | 描述               | 必须 | 备注                                                         |
| :--------- | :------ | :----------------- | :--- | :----------------------------------------------------------- |
| TaskId     | String  | AI 任务 ID         | 是   |                  -                                            |
| ChannelId  | String  | 通道 ID            | 是   |                    -                                          |
| Object     | String  | 桶内文件的路径     | 否   | 例如:想要查看 `bucket-id/a/b/c/dog.ts` 的识别结果，此时传的值为"a/b/c/dog.ts" |
| DetectType | String  | AI 任务识别类型    | 否   | 可选值为Facemask(口罩识别)、Chefhat(厨师帽识别)、Smoking(抽烟检测)、Chefcloth(厨师服识别)、PhoneCall(接打电话识别)、Pet(宠物识别)、Body(人体识别)和 Car(车辆车牌识别) |
| BeginTime  | Integer | 开始时间时间       | 否   | 秒级时间戳。                                                 |
| EndTime    | Integer | 结束时间时间       | 否   | 秒级时间戳。开始时间和结束时间跨度小于等于30天               |
| PageNumber | Integer | 页码               | 否   | 默认为1。                                                    |
| PageSize   | Integer | 每页AI识别结果数量 | 否   | 可选值1～100，默认为10（按时间倒序显示识别结果）。           |

#### 返回结果

```shell
{
  "Code": 0,
  "StatusCode": 200,
  "Message": "ok",
  "RequestId": "MTgzNWVjNjVlNzlfN2Q0ODI5MWVfMF8zYw==",
  "Data": {
    "TaskId": "at553be1f6768a42698445e5d248fac1ac",
    "AIResultCount": 2,
    "AIResults": {
      "Body": [
        {
          "Time": "2022-11-01 11:27:03",
          "Url": "image url1",
          "BodyInfo": [
            {
              "Name": "person",
              "Score": 100,
              "Location": {
                "Height": "731",
                "Width": "459",
                "X": "55",
                "Y": "222"
              }
            }
          ]
        },
        {
          "Time": "2022-11-01 11:27:05",
          "Url": "image url2",
          "BodyInfo": [
            {
              "Name": "person",
              "Score": 100,
              "Location": {
                "Height": "731",
                "Width": "459",
                "X": "55",
                "Y": "222"
              }
            }
          ]
        }
      ],
      "Pet": [],
      "Car": [],
      "Chefhat": [],
      "Chefcloth": [],
      "Facemask": [],
      "Smoking": [],
      "PhoneCall": []
    }
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

| 参数名称      | 类型    | 描述                                                         |
| :------------ | :------ | :----------------------------------------------------------- |
| TaskId        | String  | AI 任务 ID                                                   |
| AIResultCount | Integer | 在 BeginTime 和 EndTime 时间之内，有识别结果的 AI 调用次数（分页依据此数值）。 |
| AIResults     | Array   | AI 任务执行结果详情                                          |

AIResults 具体描述如下：

| 参数名称  | 类型  | 描述                 |
| :-------- | :---- | :------------------- |
| Body      | Array | 人体识别结果列表     |
| Pet       | Array | 宠物识别结果列表     |
| Car       | Array | 车辆车牌识别结果列表 |
| Chefhat   | Array | 厨师帽结果列表       |
| Chefcloth | Array | 厨师服结果列表       |
| Facemask  | Array | 口罩识别结果列表     |
| Smoking   | Array | 抽烟检测结果列表     |
| PhoneCall | Array | 接打电话识别结果列表 |

Body 具体描述如下：

| 参数名称 | 类型   | 描述       |
| :------- | :----- | :--------- |
| Time     | String | 时间字符串 |
| Url      | String | 截图 URL    |
| BodyInfo | Array  | 人体信息   |

Pet 具体描述如下：

| 参数名称 | 类型   | 描述     |
| :------- | :----- | :------- |
| Time     | String | 时间     |
| Url      | String | 截图 URL  |
| PetInfo  | Array  | 宠物信息 |

Car 具体描述如下：

| 参数名称 | 类型   | 描述         |
| :------- | :----- | :----------- |
| Time     | String | 时间         |
| Url      | String | 截图 URL      |
| CarInfo  | Array  | 车辆车牌信息 |

Chefhat 具体描述如下：

| 参数名称    | 类型   | 描述       |
| :---------- | :----- | :--------- |
| Time        | String | 时间       |
| Url         | String | 截图 URL    |
| ChefhatInfo | Array  | 厨师帽信息 |

Chefcloth 具体描述如下：

| 参数名称      | 类型   | 描述       |
| :------------ | :----- | :--------- |
| Time          | String | 时间       |
| Url           | String | 截图URL    |
| ChefclothInfo | Array  | 厨师服信息 |

Facemask 具体描述如下：

| 参数名称     | 类型   | 描述     |
| :----------- | :----- | :------- |
| Time         | String | 时间     |
| Url          | String | 截图 URL  |
| FacemaskInfo | Array  | 口罩信息 |

Smoking 具体描述如下：

| 参数名称    | 类型   | 描述     |
| :---------- | :----- | :------- |
| Time        | String | 时间     |
| Url         | String | 截图 URL  |
| SmokingInfo | Array  | 抽烟信息 |

PhoneCall 具体描述如下：

| 参数名称      | 类型   | 描述         |
| :------------ | :----- | :----------- |
| Time          | String | 时间         |
| Url           | String | 截图 URL      |
| PhoneCallInfo | Array  | 接打电话信息 |

BodyInfo、PetInfo、CarInfo、ChefhatInfo、ChefclothInfo、FacemaskInfo、SmokingInfo 和 PhoneCallInfo 具体描述如下：

| 参数名称 | 类型    | 描述           | 备注                                                         |
| :------- | :------ | :------------- | :----------------------------------------------------------- |
| Name     | String  | 名称           | 返回值有人体识别结果名称(person)、宠物识别结果名称(cat和dog) 、车辆车牌识别结果名称(vehicle) |
| Score    | Integer | 置信度         |                     -                                         |
| Location | Object  | 视频中坐标信息 |                      -                                        |

Location 具体描述如下：

| 参数名称 | 类型    | 描述            |
| :------- | :------ | :-------------- |
| X        | Integer | 左上角 X 坐标轴 |
| Y        | Integer | 左上角 Y 坐标轴 |
| Width    | Integer | 方框宽          |
| Height   | Integer | 方框高          |
