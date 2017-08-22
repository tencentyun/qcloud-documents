# Qcloud_CDN  CTS doc
## 描述
- 本文档用于腾讯云CDN转码服务结果查询和回调
- 请求域名：cdn.api.qcloud.com
- 请求方式：POST 或者GET
- 签名方法：https://www.qcloud.com/document/product/228/1725
- SDK： https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API
- secretKey和secretId：https://console.qcloud.com/capi

## 1. 视频转码结果查询接口(GetCtsInfo)
### 功能描述
查询转码任务结果

### 请求参数
| 参数名称 | 必选   | 类型     | 说明    |
| ---- | ---- | ------ | ----- |
| vid  | 否    | String | 视频的ID |
| url  | 否    | String | 转码URL |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功，其他值：失败 |
| message | String | 错误信息            |
| data    | 对象     | 结果数据，详细说明见下文    |

#### data字段说明
| 名称          | 类型     | 说明                |
| ----------- | ------ | ----------------- |
| vid         | String | 视频ID              |
| app_id      | Int    | 用户app_id          |
| bucket_name | String | cos bucket名       |
| name        | String | 视频名               |
| size        | Int    | 视频大小              |
| duration    | Int    | 视频时长              |
| height      | Int    | 视频高度              |
| width       | Int    | 视频宽度              |
| bitrate     | Int    | 视频码率              |
| create_time | String | 转码任务创建时间          |
| update_time | String | 转码任务更新时间          |
| url         | String | 视频文件的原始URL        |
| url_f0      | String | 视频文件的原始路径         |
| v_type      | String | 视频文件类型            |
| region      | String | 存储地区              |
| status      | Int    | 详细说明见备注           |
| error_code  | Int    | 转码错误码             |
| error_msg   | String | 转码错误描述            |
| deleted     | String | yes表示任务删除，no表示未删除 |
| result      | Array  | 转码成功后的信息,详细说明见下文  |


#### result 字段说明
| 名称    | 类型    | 说明                      |
| ----- | ----- | ----------------------- |
| video | Array | 转码后视频的相关信息,包含dst和info字段 |
| gif   | Array | gif的相关信息,包含dst和info字段   |
| cover | Array | 截图相关信息，包含dst和info字段     |
| dst   | Array | 转码后的存储信息                |


#### video 中info字段说明
| 名称         | 类型     | 说明               |
| ---------- | ------ | ---------------- |
| width      | Int    | 转码后视频宽度          |
| name       | Array  | 规格名称             |
| fps        | Array  | 帧率               |
| path       | String | 转码后的存储路径         |
| bitrate    | Array  | 转码后的码率           |
| height     | Array  | 转码后视频高度          |
| trans_size | Int    | 转码后的视频大小(m3u8为0) |

#### cover 中info字段说明
| 名称     | 类型    | 说明      |
| ------ | ----- | ------- |
| width  | Int   | 截图宽度    |
| path   | Array | 截图的存储路径 |
| count  | Array | 截图数     |
| name   | Array | 规格名称    |
| height | Array | 转码后视频高度 |

#### gif 中info字段说明
| 名称     | 类型     | 说明       |
| ------ | ------ | -------- |
| width  | 转码     | 截图宽度     |
| path   | String | 转码后的存储路径 |
| name   | Array  | 规格名称     |
| height | Array  | 转码后视频高度  |
#### 备注
+ status 状态：1.待处理 2.已获取视频基本信息 3.转码中 4.转码失败 5.转码成功
+ 当同一个文件重复提交时，会将之前提交的任务标记为删除。
+ 转码结果字段result与具体的配置有关，其中gif和cover可能不存在。
+ dst 字段为转码后的存储信息，可配置，默认为原视频的信息。

#### 转码及截图规格说明
| 规格   | 类型   | 说明                                |
| ---- | ---- | --------------------------------- |
| f10  | 视频   | 流畅 270p                           |
| f20  | 视频   | 标清 480p                           |
| f30  | 视频   | 高清 720p                           |
| f40  | 视频   | 超清 1080p                          |
| s_x  | 截图   | 短边配置，x表示短边大小,例如s_270              |
| l_x  | 截图   | 长边配置，x表示长边大小,例如l_1920             |
| w_x  | 截图   | 指定宽度，x表示宽度,实际高度根据原尺寸等比缩放，例如w_1920 |
| h_x  | 截图   | 指定高度，x表示高度,实际宽度根据原尺寸等比缩放，例如h_1080 |
| 0_0  | 截图   | 视频原尺寸,例如1920_1080                 |
| x_y  | 截图   | 指定宽度和高度,例如400_200                 |


### 请求示例
``` shell
https://cdn.api.qcloud.com/v2/index.php?Action=GetCtsInfo&SecretId=AKIDxUCsd01oB7BxxxxxxFihD8hlRhftKmXr&Nonce=44207&Timestamp=1480384094&Region=gz&vid=000628c22a4cfa9daac321c31d496393&Signature=njTouxSxxxxxxPjeGKr0ZG%2Fi%2FE%3D
```
###　回包示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "963f1d40dfdfadfdd9b94e922d5696",
        "app_id": 1233444,
        "bucket_name": "cts",
        "bucket_region": "sh",
        "name": "/1233444/cts/test/w.mp4",
        "url": "http://cts-1233444.cossh.myqcloud.com/test/w.mp4",
        "url_f0": "/test/w.mp4",
        "size": 322960391,
        "duration": 600,
        "bitrate": 4205,
        "width": 1920,
        "height": 1080,
        "v_type": "mov,mp4,m4a,3gp,3g2,mj2",
        "create_time": "2016-12-23 21:11:42",
        "update_time": "2016-12-26 10:12:56",
        "status": 5,
        "error_code": null,
        "error_msg": null,
        "deleted": "no",
        "result": {
            "video": {
                "info": [
                    {
                        "bitrate": 300,
                        "width": 480,
                        "height": 270,
                        "fps": 25,
                        "path": "/test/w.mp4.f10.mp4",
                        "name": "f10",
                        "trans_size":100000
                        
                    },
                    {
                        "bitrate": 600,
                        "width": 852,
                        "height": 480,
                        "fps": 25,
                        "path": "/test/w.mp4.f20.mp4",
                        "name": "f20",
                        "trans_size":200000,
                    },
                    {
                        "bitrate": 1200,
                        "width": 1280,
                        "height": 720,
                        "fps": 25,
                        "path": "/test/w.mp4.f30.mp4",
                        "name": "f30",
                        "trans_size":100000
                    },
                    {
                        "bitrate": 2400,
                        "width": 1920,
                        "height": 1080,
                        "fps": 25,
                        "path": "/test/w.mp4.f40.mp4",
                        "name": "f40",
                        "trans_size":100000
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            },
            "gif": {
                "info": [
                    {
                        "height": 1080,
                        "width": 1920,
                        "path": "/test/w.mp4.0_0.gif",
                        "name": "0_0"
                    },
                    {
                        "height": 200,
                        "width": 400,
                        "path": "/test/w.mp4.400_200.gif",
                        "name": "400_200"
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            },
            "cover": {
                "info": [
                    {
                        "height": 1080,
                        "width": 1920,
                        "count": 5,
                        "path": [
                            "/test/w.mp4.0_0.p0.png",
                            "/test/w.mp4.0_0.p1.png",
                            "/test/w.mp4.0_0.p2.png",
                            "/test/w.mp4.0_0.p3.png",
                            "/test/w.mp4.0_0.p4.png"
                        ],
                        "name": "0_0"
                    },
                    {
                        "height": 200,
                        "width": 400,
                        "count": 2,
                        "path": [
                            "/test/w.mp4.400_200.p0.png",
                            "/test/w.mp4.400_200.p1.png"
                        ],
                        "name": "400_200"
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            }
        }
    }
}
```

## 2. 视频转码完成回调
### 功能描述
回调用户实时将完成的转码结果详情回传给用户，需要用户配置回调地址。
### 回调方式
回调域名：需用户提供
回调方式：HTTP POST 请求

### 回调格式说明
#### 转码成功
- 参数说明
| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success 表示转码成功，fail表示转码失败 |
| vid           | String | 视频ID                      |
| detail        | Array  | 详情                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 视频文件的原始URL                |
| url_f0        | String | 视频文件的原始路径                 |
| v_type        | String | 视频文件类型                    |



- detail 说明
| 名称       | 类型    | 说明                   |
| -------- | ----- | -------------------- |
| size     | Int   | 视频大小                 |
| duration | Int   | 视频时长                 |
| height   | Int   | 视频高度                 |
| width    | Int   | 视频宽度                 |
| bitrate  | Int   | 视频码率                 |
| result   | Array | 转码后的结果，详情见GetCtsInfo |


- 示例
```
{
    "status":"success",
    "url_f0":"/test/w.mp4",
    "v_type":"mov,mp4,m4a,3gp,3g2,mj2",
    "name":"/123456/cts/test/w.mp4",
    "vid":"963f1d4048dfdfad362d9b94e922d5696",
    "url":"http://cts-123456.cossh.myqcloud.com/test/w.mp4",
    "detail":{
        "height":1080,
        "width":1920,
        "result":{
            "gif":{
                "info":[
                    {
                        "path":"/test/w.mp4.0_0.gif",
                        "width":1920,
                        "name":"0_0",
                        "height":1080
                    },
                    {
                        "path":"/test/w.mp4.400_200.gif",
                        "width":400,
                        "name":"400_200",
                        "height":200
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            },
            "video":{
                "info":[
                    {
                        "width":480,
                        "name":"f10",
                        "fps":25,
                        "path":"/test/w.mp4.f10.mp4",
                        "bitrate":300,
                        "height":270,
                        "trans_size":100000
                    },
                    {
                        "width":852,
                        "name":"f20",
                        "fps":25,
                        "path":"/test/w.mp4.f20.mp4",
                        "bitrate":600,
                        "height":480,
                        "trans_size":100000
                    },
                    {
                        "width":1280,
                        "name":"f30",
                        "fps":25,
                        "path":"/test/w.mp4.f30.mp4",
                        "bitrate":1200,
                        "height":720,
                        "trans_size":100000
                    },
                    {
                        "width":1920,
                        "name":"f40",
                        "fps":25,
                        "path":"/test/w.mp4.f40.mp4",
                        "bitrate":2400,
                        "height":1080,
                        "trans_size":100000
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            },
            "cover":{
                "info":[
                    {
                        "count":5,
                        "path":[
                            "/test/w.mp4.0_0.p0.png",
                            "/test/w.mp4.0_0.p1.png",
                            "/test/w.mp4.0_0.p2.png",
                            "/test/w.mp4.0_0.p3.png",
                            "/test/w.mp4.0_0.p4.png"
                        ],
                        "width":1920,
                        "name":"0_0",
                        "height":1080
                    },
                    {
                        "count":2,
                        "path":[
                            "/test/w.mp4.400_200.p0.png",
                            "/test/w.mp4.400_200.p1.png"
                        ],
                        "width":400,
                        "name":"400_200",
                        "height":200
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            }
        },
        "duration":600,
        "bitrate":4205,
        "size":322960391
    },
    "app_id":123456,
    "create_time":"2016-12-23 21:11:42",
    "bucket_name":"cts",
    "bucket_region":"sh"
}
```
####  转码失败
- 参数说明
  | 名称            | 类型     | 说明                        |
  | ------------- | ------ | ------------------------- |
  | status        | String | success 表示转码成功，fail表示转码失败 |
  | vid           | String | 视频ID                      |
  | detail        | Array  | 详情                        |
  | bucket_name   | String | cos bucket名               |
  | bucket_region | String | cos地区                     |
  | create_time   | String | 转码任务创建时间                  |
  | app_id        | Int    | 用户app_id                  |
  | url           | String | 视频文件的原始URL                |
  | url_f0        | String | 视频文件的原始路径                 |
  | v_type        | String | 视频文件类型                    |

- detail 说明
  | 名称         | 类型    | 说明                   |
  | ---------- | ----- | -------------------- |
  | error_code | Array | 转码错误码                |
  | error_msg  | Array | 错误码描述与error_code一一对应 |

- 示例
```
{
    "status":"fail",   			  "url_f0":"/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
 "name":"/10032344/cts/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
    "vid":"7d70b89fdf72ee6b98dcc0b0211",
    "url":"http://cts-10032344.cossh.myqcloud.com/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
    "detail":{
        "error_code":[
            122,
        ],
        "error_msg":[
            "回调Gif提交接口调用失败",
        ]
    },
    "app_id":123456,
    "create_time":"2016-12-15 14:31:46",
    "bucket_name":"cts",
    "bucket_region":"sh"
}
```


## 3. 音频转码结果查询接口(GetCtsaudioInfo)
### 功能描述
查询转码任务结果

### 请求参数
| 参数名称 | 必选   | 类型     | 说明    |
| ---- | ---- | ------ | ----- |
| vid  | 否    | String | 音频的ID |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功，其他值：失败 |
| message | String | 错误信息            |
| data    | 对象     | 结果数据，详细说明见下文    |

#### data字段说明
| 名称          | 类型     | 说明                |
| ----------- | ------ | ----------------- |
| vid         | String | 音频ID              |
| app_id      | Int    | 用户app_id          |
| bucket_name | String | cos bucket名       |
| name        | String | 音频名               |
| size        | Int    | 音频大小              |
| duration    | Int    | 音频时长              |
| format      | String | 音频格式              |
| sample_rate | 采样率    | 采样率               |
| bitrate     | Int    | 音频bitrate（kbps）   |
| create_time | String | 转码任务创建时间          |
| update_time | String | 转码任务更新时间          |
| url         | String | 音频文件的原始URL        |
| url_f0      | String | 音频文件的原始路径         |
| v_type      | String | 音频文件类型            |
| region      | String | 存储地区              |
| status      | Int    | 详细说明见备注           |
| error_code  | Int    | 转码错误码             |
| error_msg   | String | 转码错误描述            |
| deleted     | String | yes表示任务删除，no表示未删除 |
| result      | Array  | 转码成功后的信息,详细说明见下文  |


#### result 字段说明
| 名称    | 类型    | 说明                      |
| ----- | ----- | ----------------------- |
| audio | Array | 转码后音频的相关信息,包含dst和info字段 |
| dst   | Array | 转码后的存储信息                |


#### video 中info字段说明
| 名称          | 类型     | 说明                 |
| ----------- | ------ | ------------------ |
| bitrate     | Int    | 比特率,其中ape flac格式为0 |
| name        | Array  | 规格名称               |
| sample_rate | Array  | 采样率                |
| path        | String | 转码后的存储路径           |
| format      | String | 格式                 |
| encoder     | String | 编码器                |
| trans_size  | Int    | 转码后的音频大小           |

#### 备注
+ status 状态：1.待处理 2.已获取音频基本信息 3.转码中 4.转码失败 5.转码成功
+ 当同一个文件重复提交时，会将之前提交的任务标记为删除。
+ 转码结果字段result与具体的配置有关，其中gif和cover可能不存在。
+ dst 字段为转码后的存储信息，可配置，默认为原音频的信息。

#### 转码规格说明
| 规格   | 类型   | 说明            |
| ---- | ---- | ------------- |
| x_y  | 音频   | 其中x表示码率，y表示格式 |


### 请求示例
``` shell
https://cdn.api.qcloud.com/v2/index.php?Action=GetCtsaudioInfo&SecretId=AKIDxUCsd01oB7BxxxxxxFihD8hlRhftKmXr&Nonce=44207&Timestamp=1480384094&Region=gz&vid=000628c22a4cfa9daac321c31d496393&Signature=njTouxSxxxxxxPjeGKr0ZG%2Fi%2FE%3D
```
###　回包示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "6e50fd43c6f20d56c88d1c1d8f6db2641503390019",
        "app_id": 1253125191,
        "bucket_name": "onlinemusic",
        "bucket_region": "gz",
        "name": "/1253125191/onlinemusic/20170717/Maid.mp3",
        "url": "http://onlinemusic-1253125191.cosgz.myqcloud.com/20170717/Maid.mp3",
        "url_f0": "/20170717/Maid.mp3",
        "size": 4113874,
        "duration": 170,
        "bitrate": 187,
        "format": "mp3",
        "sample_rate": 44100,
        "encoder": "mp3",
        "create_time": "2017-08-22 16:20:19",
        "update_time": "2017-08-22 16:21:02",
        "status": 5,
        "error_code": null,
        "error_msg": null,
        "deleted": "no",
        "result": {
            "audio": {
                "info": [
                    {
                        "bitrate": 191488,
                        "sample_rate": 44100,
                        "format": "mp3",
                        "encoder": "lame",
                        "path": "/20170717/Maid.mp3.191488_mp3.mp3",
                        "name": "191488_mp3",
                        "trans_size": 4264747
                    }
                ],
                "dst": {
                    "app_id": 1253125191,
                    "bucket_name": "onlinemusic",
                    "bucket_region": "gz"
                }
            }
        }
    }
}
```

## 4. 音频转码完成回调
### 功能描述
回调用户实时将完成的转码结果详情回传给用户，需要用户配置回调地址。
### 回调方式
回调域名：需用户提供
回调方式：HTTP POST 请求

### 回调格式说明
#### 转码成功
- 参数说明
| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success 表示转码成功，fail表示转码失败 |
| vid           | String | 音频ID                      |
| detail        | Array  | 详情                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 音频文件的原始URL                |
| url_f0        | String | 音频文件的原始路径                 |




- detail 说明
| 名称          | 类型     | 说明                        |
| ----------- | ------ | ------------------------- |
| encoder     | String | 编码器                       |
| duration    | Int    | 音频时长                      |
| sample_rate | Int    | 采样率                       |
| bitrate     | Int    | 音频大小                      |
| result      | Array  | 转码后的结果，详情见GetCtsaudioInfo |


- 示例
```
    
{
    "status":"success",
    "url_f0":"/20170428/strength.mp3",
    "name":"/1253125191/onlinemusic/20170428/strength.mp3",
    "vid":"e5fea7f66851b7176b8c89c254d0a11b1493379478",
    "url":"http://onlinemusic-1253125191.cosgz.myqcloud.com/20170428/strength.mp3",
    "detail":{
        "encoder":"mp3",
        "sample_rate":48000,
        "result":{
            "audio":{
                "info":[
                    {
                        "sample_rate":44100,
                        "format":"ape",
                        "trans_size":16889420,
                        "path":"/20170428/strength.mp3.0_ape.ape",
                        "bitrate":0,
                        "trans_name":"0_ape",
                        "encoder":"ape"
                    },
                    {
                        "sample_rate":44100,
                        "format":"flac",
                        "trans_size":16843751,
                        "path":"/20170428/strength.mp3.0_flac.flac",
                        "bitrate":0,
                        "trans_name":"0_flac",
                        "encoder":"flac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":2664306,
                        "path":"/20170428/strength.mp3.128000_mp3.mp3",
                        "bitrate":128000,
                        "trans_name":"128000_mp3",
                        "encoder":"libmp3lame"
                    },
                    {
                        "sample_rate":44100,
                        "format":"m4a",
                        "trans_size":453401,
                        "path":"/20170428/strength.mp3.24000_m4a.m4a",
                        "bitrate":24000,
                        "trans_name":"24000_m4a",
                        "encoder":"fdk_aac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":984842,
                        "path":"/20170428/strength.mp3.24000_mp3.mp3",
                        "bitrate":24000,
                        "trans_name":"24000_mp3",
                        "encoder":"libmp3lame"
                    },
                    {
                        "sample_rate":44100,
                        "format":"m4a",
                        "trans_size":872852,
                        "path":"/20170428/strength.mp3.48000_m4a.m4a",
                        "bitrate":48000,
                        "trans_name":"48000_m4a",
                        "encoder":"fdk_aac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":1264718,
                        "path":"/20170428/strength.mp3.48000_mp3.mp3",
                        "bitrate":48000,
                        "trans_name":"48000_mp3",
                        "encoder":"libmp3lame"
                    }
                ],
                "dst":{
                    "bucket_name":"onlinemusic",
                    "bucket_region":"gz",
                    "app_id":1253125191
                }
            }
        },
        "duration":140,
        "bitrate":312,
        "size":5641493
    },
    "app_id":1253125191,
    "create_time":"2017-04-28 19:37:58",
    "bucket_name":"onlinemusic",
    "bucket_region":"gz"
}
```
####  转码失败
- 参数说明
| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success 表示转码成功，fail表示转码失败 |
| vid           | String | 音频ID                      |
| detail        | Array  | 详情                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 音频文件的原始URL                |
| url_f0        | String | 音频文件的原始路径                 |

- detail 说明
| 名称         | 类型    | 说明                   |
| ---------- | ----- | -------------------- |
| error_code | Array | 转码错误码                |
| error_msg  | Array | 错误码描述与error_code一一对应 |


## 5. 增加音频转码任务(AddCtsAudioTask)
### 功能描述
增加音频转码任务

### 请求参数
| 参数名称         | 必选   | 类型     | 说明          |
| ------------ | ---- | ------ | ----------- |
| bucketRegion | 是    | String | 地域          |
| url          | 是    | String | 转码音频完整cos路径 |
| bucketName   | 是    | String | bucket名     |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功，其他值：失败 |
| message | String | 错误信息            |
| data    | 对象     | 结果数据，详细说明见下文    |

#### data字段说明
| 名称   | 类型     | 说明     |
| ---- | ------ | ------ |
| vid  | String | 音频唯一ID |

### 请求示例
json
```
https://cdn.api.qcloud.com/v2/index.php?Action=AddCtsAudioTask&SecretId=1&Nonce=47825&Timestamp=1503372336&Region=sh&Uin=2418826573&AppId=1253125191&url=http%3A%2F%2Fonlinemusic-1253125191.cosgz.myqcloud.com%2F20170717%2FMaid.mp3&bucketName=onlinemusic&bucketRegion=gz&Signature=LXe8bGz%2BSULUuCo1XF8PjzxT1fI%3D
```

### 回包示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "5ba52a3a31688f83571c34de9dd44f6c1503372336"
    }
}
```