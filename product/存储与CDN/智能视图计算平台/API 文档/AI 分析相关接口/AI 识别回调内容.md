
## AI识别回调内容

#### 内容介绍

下面以宠物识别为例，该响应体返回为 application/json 数据，包含完整节点数据的内容展示如下：

```json
{
  "Tag": "AI",
  "AIConfig": {
    "DetectType": "Pet",
    "TimeInterval": 10,
    "OperTimeslot": [
      {
        "Start": "14: 00: 00",
        "End": "16: 00: 00"
      }
    ]
  },
  "AIJobDetail": {
    "PetRecognition": [
      {
        "Time": "0.000000",
        "Url": "https://xxx",
        "PetInfo": [
          {
            "Name": "cat",
            "Score": 85,
            "Location": {
              "X": 738,
              "Y": 171,
              "Height": 440,
              "Width": 253
            }
          },
          {
            "Name": "cat",
            "Score": 79,
            "Location": {
              "X": 1014,
              "Y": 264,
              "Height": 551,
              "Width": 365
            }
          }
        ]
      },
      {
        "Time": "10.000000",
        "Url": "https://xxx",
        "PetInfo": [
          {
            "Name": "cat",
            "Score": 89,
            "Location": {
              "X": 891,
              "Y": 246,
              "Height": 496,
              "Width": 394
            }
          },
          {
            "Name": "cat",
            "Score": 84,
            "Location": {
              "X": 603,
              "Y": 111,
              "Height": 455,
              "Width": 256
            }
          }
        ]
      },
      {
        "Time": "20.000000",
        "Url": "https://xxx",
        "PetInfo": [
          {
            "Name": "cat",
            "Score": 85,
            "Location": {
              "X": 756,
              "Y": 204,
              "Height": 470,
              "Width": 299
            }
          },
          {
            "Name": "cat",
            "Score": 85,
            "Location": {
              "X": 1029,
              "Y": 312,
              "Height": 518,
              "Width": 371
            }
          }
        ]
      }
    ]
  }
}
```

具体的数据内容如下：

| 名称        | 类型   | 描述                         |
| ----------- | ------ | ---------------------------- |
| Tag         | String | AI标签，值为"AI"或"Snapshot" |
| AIConfig    | Object | AI配置                       |
| AIJobDetail | Object | AI识别详情                   |

AIConfig 的内容如下：

| 参数名称     | 类型    | 描述                                                         |
| :----------- | :------ | :----------------------------------------------------------- |
| DetectType   | String  | AI分析类型，可选值为Facemask(口罩识别)、Chefhat(厨师帽识别)、Smoking(抽烟检测)、Chefcloth(厨师服识别)、PhoneCall(接打电话识别)、Pet(宠物识别)、Body(人体识别)和 Car(车辆车牌识别)等 |
| TimeInterval | Integer | 截图频率                                                     |
| OperTimeslot | String  | 模板生效的时间段                                             |

OperTimeslot 具体描述如下：

| 参数名称 | 类型   | 描述                        |
| :------- | :----- | :-------------------------- |
| Start    | String | 开始时间， 格式为"hh:mm:ss" |
| End      | String | 结束时间， 格式为"hh:mm:ss" |

AIJobDetail 的内容如下：

| 参数名称             | 类型  | 描述                                 |
| :------------------- | :---- | :----------------------------------- |
| BodyRecognition      | Array | 人体识别结果，没有识别结果就不展示   |
| PetRecognition       | Array | 宠物识别结果，没有识别结果就不展示   |
| CarRecognition       | Array | 车辆识别结果，没有识别结果就不展示   |
| ChefhatRecognition   | Array | 厨师帽识别结果，没有识别结果就不展示 |
| ChefclothRecognition | Array | 厨师服识别结果，没有识别结果就不展示 |
| FacemaskRecognition  | Array | 口罩识别结果，没有识别结果就不展示   |
| SmokingRecognition   | Array | 抽烟识别结果，没有识别结果就不展示   |
| PhoneCallRecognition | Array | 打手机识别结果，没有识别结果就不展示 |

BodyRecognition 具体描述如下：

| 参数名称 | 类型   | 描述       |
| :------- | :----- | :--------- |
| Time     | String | 时间字符串 |
| Url      | String | 截图 URL    |
| BodyInfo | Array  | 人体信息   |

PetRecognition 具体描述如下：

| 参数名称 | 类型   | 描述     |
| :------- | :----- | :------- |
| Time     | String | 时间     |
| Url      | String | 截图 URL  |
| PetInfo  | Array  | 宠物信息 |

CarRecognition 具体描述如下：

| 参数名称 | 类型   | 描述         |
| :------- | :----- | :----------- |
| Time     | String | 时间         |
| Url      | String | 截图URL      |
| CarInfo  | Array  | 车辆车牌信息 |

ChefhatRecognition 具体描述如下：

| 参数名称    | 类型   | 描述       |
| :---------- | :----- | :--------- |
| Time        | String | 时间       |
| Url         | String | 截图 URL    |
| ChefhatInfo | Array  | 厨师帽信息 |

ChefclothRecognition 具体描述如下：

| 参数名称      | 类型   | 描述       |
| :------------ | :----- | :--------- |
| Time          | String | 时间       |
| Url           | String | 截图URL    |
| ChefclothInfo | Array  | 厨师服信息 |

FacemaskRecognition 具体描述如下：

| 参数名称     | 类型   | 描述     |
| :----------- | :----- | :------- |
| Time         | String | 时间     |
| Url          | String | 截图 URL  |
| FacemaskInfo | Array  | 口罩信息 |

SmokingRecognition 具体描述如下：

| 参数名称    | 类型   | 描述     |
| :---------- | :----- | :------- |
| Time        | String | 时间     |
| Url         | String | 截图 URL  |
| SmokingInfo | Array  | 抽烟信息 |

PhoneCallRecognition 具体描述如下：

| 参数名称      | 类型   | 描述         |
| :------------ | :----- | :----------- |
| Time          | String | 时间         |
| Url           | String | 截图 URL      |
| PhoneCallInfo | Array  | 接打电话信息 |

BodyRecognition、PetRecognition、CarRecognition、ChefhatRecognition、ChefclothRecognition、FacemaskRecognition、SmokingRecognition、PhoneCallRecognition
具体描述如下：

| 参数名称 | 类型    | 描述           | 备注                                                         |
| :------- | :------ | :------------- | :----------------------------------------------------------- |
| Name     | String  | 名称           | 返回值有人体识别结果名称(person)、宠物识别结果名称(cat和dog) 、车辆车牌识别结果名称(vehicle) |
| Score    | Integer | 置信度         |                          -                                    |
| Location | Object  | 视频中坐标信息 |                   -                                           |

Location 具体描述如下：

| 参数名称 | 类型    | 描述            |
| :------- | :------ | :-------------- |
| X        | Integer | 左上角 X 坐标轴 |
| Y        | Integer | 左上角 Y 坐标轴 |
| Width    | Integer | 方框宽          |
| Height   | Integer | 方框高          |
