## 接口描述

### 更新历史
发布时间：2018-11-30 

本次发布包含了以下内容：

补充域名的使用限制（2018.12.1之后申请的用户须使用新域名）

补充鉴黄鉴政的请求参数、返回参数

增加鉴黄鉴政的返回示例

### 服务简介
本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。

### URL 说明
支持https协议：

`https://aiconsole.cloud.tencent.com/fuseapi/face`
>**注意：本域名仅适用于2018年11月前发布的活动。因引擎算法升级，请2018年12月1日后申请接入的开发者，使用新域名xxx。**

## 请求包 header
所有请求都要求含有下表列出的头部信息：

| 参数名          | 必选 | 值                                        | 描述                                       |
| -------------- |--- |---------------------------------------- | ---------------------------------------- |
| Host          | 是 | aiconsole.cloud.tencent.com              | 服务器域名。                                |
| Content-Length| 否 | 包体总长度                                | 整个请求包体内容的总长度，单位：字节（Byte）。 |
| Content-Type  | 是 | application/json                         | 参数类型 。                                 |
| Authorization | 是 | 鉴权签名                                  | 用于 [**鉴权**](https://cloud.tencent.com/document/product/641/12409)  的签名。 |

> **注意：**
> - 每个请求的包体大小限制为6MB；
> - 所有接口都为 POST 方法；
> - 不支持.gif 这类的动图。

### 请求参数
使用 application/json 格式：

| 参数名    | 必选 | 类型     | 说明    |
| ------ | ---- | ------ | ------- |
| appid  | 是   | string | 项目 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看。   |
| uin    | 是   | string | 账号 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看。|
| project_id    | 是   | string | 活动 ID，可在 [控制台](https://console.cloud.tencent.com/ai/facemerge)查看。 |
| model_id    | 是   | string | 素材 ID，可在 [控制台](https://console.cloud.tencent.com/ai/facemerge)查看。 |
| img_data    | 是   | string | 图片 base64数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理。图片大小不超过 500k，分辨率不超过 1080\*1080。 |
| rsp_img_type    | 是   | string | 返回图像方式（url 或 base64) ，二选一。 |
| porn_detect   |  否 |  int |0表示不需要鉴黄，1表示需要鉴黄。2018年12月之后创建的活动默认为1，之前创建的活动默认为0 |
| celebrity_identify | 否 | int | 0表示不需要鉴政治，1表示需要鉴政。2018年12月之后创建的活动默认为1，之前创建的活动默认为0 |


### 返回参数

| 字段                 | 类型     | 说明      |
| ------------------ | ------ | ------- |
| ret | int | 错误码 |
| img_url               | string    | rsp_img_type 为 url 时，返回结果的 url，  rsp_img_type 为 base64 时返回 base64 数据。   |
| img_base64 | string | 请求参数中rsp_img_type 为 base64 时，返回结果的 base64 | 
| PornDetectResult |  json|  鉴黄的结果，详见返回示例2或3| 
| CelebrityIdentifyResult |  json |  鉴政的结果，详见返回示例2或3| 

### demo示例

- [单击下载 PHP 代码 demo>> ](https://main.qcloudimg.com/raw/e6601ec77d988a193a06cb940595da97.php)
- [单击下载 Java 代码 demo>>](https://main.qcloudimg.com/raw/74c360901626b508e2efd937d47a988e.java)

### 请求示例

```
{
	"rsp_img_type":"url",
	"project_id":"xxxxxxxx",
	"appid":"xxxxxxxx", 
	"uin":"xxxxxxxx",
	"img_data":"xxxxxxxx",
	"model_id":"xxxxxxxx"
}

```

> **注意：**
> 若选择 base64 进行图片数据传送，请勿在 base64 数据中包含头部。



### 返回示例

#### 示例1-无鉴黄鉴政
```
{
	"img_url":"http://activity-10053123.image.myqcloud.com/XXXX",
	"ret":"0"
}
```
#### 示例2-支持鉴黄鉴政
```
{
  "img_url": "https://facefushin20181105-1257981459.cos.ap-shanghai.myqcloud.com/1542942817318592104.jpg",
  "ret": 0,
  "PornDetectResult": {
    "code": 0,
    "message": "ok",
    "data": [
      {
        "items": [
          {
            "level_name": "porn",
            "probability": 0.0000000019030628184424
          },
          {
            "level_name": "vulgar",
            "probability": 0.00000019579806576075
          },
          {
            "level_name": "somewhat",
            "probability": 0.0000022935407741898
          },
          {
            "level_name": "sexy",
            "probability": 0.000022541460566572
          },
          {
            "level_name": "normal",
            "probability": 0.99997502565384
          },
          {
            "level_name": "penis_normal",
            "probability": 0.0000000000098002821136145
          },
          {
            "level_name": "penis_porn",
            "probability": 0.000000000000015923067443573
          },
          {
            "level_name": "vulva_normal",
            "probability": 0.0000000000027108406665255
          },
          {
            "level_name": "vulva_porn",
            "probability": 0.000000000000010953401475221
          },
          {
            "level_name": "handcuff",
            "probability": 0.00000000000000042438071193115
          },
          {
            "level_name": "bead_stick",
            "probability": 0.00000000000005655154147158
          },
          {
            "level_name": "vibrate_egg",
            "probability": 0.0000000000023811278469787
          },
          {
            "level_name": "sextoy_anatomy",
            "probability": 0.0000000000000032320193816735
          },
          {
            "level_name": "human_anatomy",
            "probability": 0.00000000000069076509920038
          }
        ]
      }
    ]
  },
  "CelebrityIdentifyResult": {
    "code": 0,
    "message": "ok",
    "data": {
      "faces": [
        {
          "face_infos": [
            {
              "face_id": "n010070",
              "face_name": "丁俊晖",
              "confidence": 0.71566122770309,
              "tags": [
                {
                  "name": "体育",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n014650",
              "face_name": "筷子兄弟肖央",
              "confidence": 0.69636118412018,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n004910",
              "face_name": "Uzi（简自豪）",
              "confidence": 0.430599629879,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n009555",
              "face_name": "岳云鹏",
              "confidence": 0.41021433472633,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n012585",
              "face_name": "班赞",
              "confidence": 0.37928435206413,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            }
          ],
          "face_coord": {
            "x": 124,
            "y": 260,
            "width": 547,
            "height": 745
          }
        }
      ]
    }
  }
}
```

#### 示例3-支持鉴黄鉴政（base64）
```
{
  "img_base64": "xxxxxxx",
  "ret": 0,
  "PornDetectResult": {
    "code": 0,
    "message": "ok",
    "data": [
      {
        "items": [
          {
            "level_name": "porn",
            "probability": 0.0000000019030628184424
          },
          {
            "level_name": "vulgar",
            "probability": 0.00000019579806576075
          },
          {
            "level_name": "somewhat",
            "probability": 0.0000022935407741898
          },
          {
            "level_name": "sexy",
            "probability": 0.000022541460566572
          },
          {
            "level_name": "normal",
            "probability": 0.99997502565384
          },
          {
            "level_name": "penis_normal",
            "probability": 0.0000000000098002821136145
          },
          {
            "level_name": "penis_porn",
            "probability": 0.000000000000015923067443573
          },
          {
            "level_name": "vulva_normal",
            "probability": 0.0000000000027108406665255
          },
          {
            "level_name": "vulva_porn",
            "probability": 0.000000000000010953401475221
          },
          {
            "level_name": "handcuff",
            "probability": 0.00000000000000042438071193115
          },
          {
            "level_name": "bead_stick",
            "probability": 0.00000000000005655154147158
          },
          {
            "level_name": "vibrate_egg",
            "probability": 0.0000000000023811278469787
          },
          {
            "level_name": "sextoy_anatomy",
            "probability": 0.0000000000000032320193816735
          },
          {
            "level_name": "human_anatomy",
            "probability": 0.00000000000069076509920038
          }
        ]
      }
    ]
  },
  "CelebrityIdentifyResult": {
    "code": 0,
    "message": "ok",
    "data": {
      "faces": [
        {
          "face_infos": [
            {
              "face_id": "n010070",
              "face_name": "丁俊晖",
              "confidence": 0.71566122770309,
              "tags": [
                {
                  "name": "体育",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n014650",
              "face_name": "筷子兄弟肖央",
              "confidence": 0.69636118412018,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n004910",
              "face_name": "Uzi（简自豪）",
              "confidence": 0.430599629879,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n009555",
              "face_name": "岳云鹏",
              "confidence": 0.41021433472633,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            },
            {
              "face_id": "n012585",
              "face_name": "班赞",
              "confidence": 0.37928435206413,
              "tags": [
                {
                  "name": "娱乐",
                  "type": "domain"
                }
              ]
            }
          ],
          "face_coord": {
            "x": 124,
            "y": 260,
            "width": 547,
            "height": 745
          }
        }
      ]
    }
  }
}

```

## 错误码

| **错误码** | **含义**                              |
| ------- | ----------------------------------- |
| 1000       | 无人脸。                               |
| 0       | 成功。                              |
| -1       | 用户身份不合法。                               |
| -3       | 图片尺寸太大。                                |
| -4       | 识别人脸出错。                              |
| -5       | 平台内部错误。                 |
| -6       | 必填的参数字段或者值有误。                        |
| -7       | 鉴权信息过期。                        |
| -8       | 模板无人脸。                                |
| -1000       | 必填的参数字段或者值有误。                                |
| -1001       | 图像处理错误。                                |
| -1002       | 读写 CKV 出错。                                |
| -1003       | 读写 REDIS 出错。                                |
| -1004       | 保存结果图片出错。                                |
| -1005       | 下载用户图片出错。                                |
| -1007       | 服务器内部逻辑出错。                                |
| -1008       | 人脸检测失败。                                |
| -1009       | 请求值不是规范的 json 格式。                                |
| -2011~-2015       | 访问频率超出限制。                                |
| -2100       | http 头错误。                                |
| -2102       | 图片操作功能不存在。                                |
| -2103       | 图片操作功能无权限。                                |
| -20001      |  鉴权信息为空。                            |
| -20002      |  鉴权信息解析错误。                            |
| -20003      |  鉴权失败。                            |
| -20004      |  操作太频繁，触发频控。                           |
| -20005      |  后端服务故障。                           |
| -20006      |  参数格式不是 json 格式。                            |
| -20007      |  素材 ID（model_id）传入为空。                            |
| -20008      |  活动 ID（project_id）传入为空。                            |
| -20009      |  图片数据（image_data）传入为空。                            |
| -20010      |  返回图片类型（rsp_img_type)为空。                            |
| -20011      |  appid 传入为空。                            |
| -20012      |  uin 传入为空。                            |
人脸融合老API接口
