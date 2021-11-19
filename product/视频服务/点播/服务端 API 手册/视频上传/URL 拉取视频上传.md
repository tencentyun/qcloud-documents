<!-- TODO:
接口需要完善的功能：
调用该接口之后，可以通过查询任务状态接口来查看转拉状态（TODO）；
转拉完成之后，如果配置了服务端回调，云点播后台会发起URL转拉完成之后回调（TODO）。
对于已经存在的转拉任务，是跳过，还是重置？
回调URL，回调方式，不能通过指定，全部读配置-->

## 接口名称
MultiPullVodFile

## 功能说明
1. 通过传递视频 URL，把已经存在于网络上的视频批量拉取到腾讯云。
2. 支持批量拉取多个视频文件（最多50个），通过输入参数中的`n`值区分是第几个视频。
3. 视频拉取格式，请参见 [音视频上传](https://cloud.tencent.com/document/product/266/2834#.E9.9F.B3.E8.A7.86.E9.A2.91.E4.B8.8A.E4.BC.A0)。

>! 请确保 URL 为视频文件，而不是包含视频文件的网页地址。

## 事件通知
视频文件上传成功可触发 [事件通知 - URL 拉取视频上传完成](/document/product/266/7831)。App 后台可据此监听云点播系统中的 URL 拉取行为。更多请参见 [服务端事件通知概述](https://cloud.tencent.com/document/product/266/33779)。

## 请求方式

#### 请求域名
`vod.api.qcloud.com`

#### 最高调用频率
100次/分钟

#### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
|pullset.n.url | 是 | String | 需要拉取的第 n 个视频的 URL。n 从0开始，依次递增，下同。 |
|pullset.n.fileName | 是 | String | 视频文件的名称。 |
|pullset.n.fileMd5 | 否 | String | 视频文件的 MD5。 |
|pullset.n.isTranscode | 否 | Integer | 是否转码，0：否，1：是，默认为0；如果不执行转码，上传后可以在控制台的视频文件管理中进行转码。|
|pullset.n.isScreenshot | 否 | Integer | 是否截图，0：否，1：是，默认为0。 |
|pullset.n.isWatermark | 否 | Integer | 是否打水印，0：否，1：是，默认为0；如果选择打水印，请务必在控制台提前完成水印文件选择和位置设定，否则可能导致上传失败。|
|pullset.n.classId | 否 | Integer | 视频的分类 ID。 |
|pullset.n.tags | 否 | String | 视频的标签，有多个标签的话采用英文逗号分隔。 |
|pullset.n.priority | 否 | Integer | 优先级，0：中；1：高；2：低。 |
| COMMON_PARAMS | 是 |  -| 请参见 [公共参数](/document/api/213/6976)。 |

#### 请求示例

```
https://vod.api.qcloud.com/v2/index.php?Action=MultiPullVodFile
&pullset.0.url=http://www.demo.com/1.mp4
&pullset.0.fileName=MyTestVideo
&pullset.0.isTranscode=1
&pullset.0.priority=1
&pullset.0.isScreenshot=1
&pullset.0.isWatermark=1
&pullset.0.classId=0
&COMMON_PARAMS
```

## 接口应答

#### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码。 |
| message | String | 错误信息说明。  |
| data | Array | 拉取上传文件任务信息集合，每个元素代表一个拉取文件的信息。 |
| data.source_url | String | 视频的源 URL。 |
| data.file_id | String | 视频的文件 ID。 |
| data.file_name | String | 上传视频的文件名称。 |
| data.vod_task_id | String | 上传任务的任务 ID。 |

#### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000 - 7000 | 请参见 [公共错误码](https://cloud.tencent.com/document/api/213/6982)。  |
| 1 | 内部错误。  |
| 1000 | 无效参数。  |
| 1001 | 用户信息错误。 |
| 1010 | 内部错误。 |
| 1011 | 内部错误。 |
| 1018 | 拉取任务过多，请稍后再试。 |
| 1100 | 内部错误。 |
| 1159 | 内部错误。 |
| 1163 | 没有水印，但请求中指定了要设置水印。 |
| 10003 | 内部错误。 |

#### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "data": [
        {
            "source_url": "http://www.demo.com/1.mp4",
            "file_id": "11624759161874546966",
            "file_name": "MyTestVideo",
            "vod_task_id": "pull-d4eeccd2563c711d14405f217ea4f82e"
        }
    ]
}
```


