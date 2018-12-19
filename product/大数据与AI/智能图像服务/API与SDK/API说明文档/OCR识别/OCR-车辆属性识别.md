## 简介
车辆属性别服务，传入一张图片，返回该图片中的最大车辆的车系、品牌、车辆类型、颜色等属性的 Top5 识别结果。

### 调用 URL
支持 http 和 https 两种协议：
```
http://recognition.image.myqcloud.com/car/classify
```

## 基本概念说明
| 概念    | 解释              |
| ----- | --------------- |
| appid | 项目 ID，接入项目的唯一标识 |

## http 请求
车辆检测识别接口采用 http 协议，支持上传本地图片数据进行识别。

### 头部信息
| 参数名            | 值                              | 描述                                       |
| -------------- | ------------------------------ | ---------------------------------------- |
| Host           | recognition.image.myqcloud.com | 腾讯云文字识别服务器域名                           |
| Content-Length | 包体总长度                          | 整个请求包体内容的总长度，单位：字节（Byte）          |
| Content-Type   | multipart/form-data               | 上传本地图片                                 |
| Authorization  | 鉴权签名                           | 多次有效签名，用于鉴权， 具体生成方式详见 [鉴权签名方法](/document/product/641/12409) |

><font color="#0000cc">**注意：** </font>
- 每个请求的包体大小限制为 6 MB；
- 所有接口都为 POST 方法；
- 不支持 .gif 这类的动图。

### 请求参数
| 参数名称   | 是否必选 | 类型     | 说明           |
| ------ | ---- | ------ | ------------ |
| app_id | 必须   | String | 腾讯云申请的 AppId |
| image  | 可选   | Binary | base64 图片数据   |

### 示例：使用图片文件
```
POST /car/classify HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: text/json

{
  "app_id": "123456",
  "image": "base64ImageData"
}
```

## 返回值
### 返回内容

| 字段        | 类型            | 说明         |
| --------- | ------------- | ---------- |
| code      | Int           | 返回状态值      |
| message   | String        | 返回错误消息     |
| data.tags | Array(CarTag) | 识别出的所有字段信息 |

CarTag 说明

| 字段         | 类型     | 说明     |
| ---------- | ------ | ------ |
| idx        | Int64  | 腾讯汽车 ID |
| confidence | Float  | 置信度    |
| serial     | String | 车系     |
| brand      | String | 品牌     |
| type       | String | 车辆类型   |
| color      | String | 颜色     |

### 示例
```
{
"code":0,
"message":"OK",
"data":{
"tags":[
{
"serial":"保时捷911#2013款",
"idx":"229",
"brand":"保时捷",
"type":"跑车",
"color":"红",
"confidence":0.3941769897937775
},
{
"serial":"保时捷911#2016款",
"idx":"229",
"brand":"保时捷",
"type":"跑车",
"color":"红",
"confidence":0.331961989402771
},
{
"serial":"保时捷911#2012款",
"idx":"229",
"brand":"保时捷",
"type":"跑车",
"color":"红",
"confidence":0.11419600248336792
},
{
"serial":"保时捷911#2015款",
"idx":"229",
"brand":"保时捷",
"type":"跑车",
"color":"红",
"confidence":0.07140179723501206
},
{
"serial":"保时捷911#2014款",
"idx":"229",
"brand":"保时捷",
"type":"跑车",
"color":"红",
"confidence":0.05329570174217224
}
]
}
}
```

## 错误码

| 错误码   | 含义                         |
| ----- | -------------------------- |
| 3     | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服  |
| 4     | 签名为空                       |
| 5     | 签名串错误                      |
| 6     | 签名中的 APPID/Bucket 与操作目标不匹配 |
| 9     | 签名过期                       |
| 10    | APPID 不存在                  |
| 11    | SecretId 不存在               |
| 12    | APPID 和 SecretId 不匹配       |
| 13    | 重放攻击                       |
| 14    | 签名校验失败                     |
| 15    | 操作太频繁，触发频控                 |
| 16    | Bucket 不存在                  |
| 21    | 无效参数                       |
| 23    | 请求包体过大                     |
| 24    | 没有权限                       |
| 25    | 您购买的资源已用完                  |
| 107   | 鉴权服务内部错误                   |
| 108   | 鉴权服务不可用                    |
| 213   | 内部错误                       |
| -1410 | 图片解码失败                     |
| -1300 | 图片为空                       |
| -1301 | 参数为空                       |
| -1304 | 参数过长                       |
| -1308 | 图片下载失败                     |
| -9011 | 识别失败                       |
