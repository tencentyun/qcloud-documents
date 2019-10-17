<!-- TODO:
接口需要完善的功能：
调用该接口之后，可以通过查询任务状态接口来查看转拉状态（TODO）；
转拉完成之后，如果配置了服务端回调，云点播后台会发起URL转拉完成之后回调（TODO）。
对于已经存在的转拉任务，是跳过，还是重置？
回调URL，回调方式，不能通过指定，全部读配置-->

## 接口名称
MultiPullVodFile

## 功能说明
1. 通过用户传递的URL，从已有的资源库批量拉取视频文件到腾讯云；
2. 支持批量拉取多个视频文件，通过输入参数中的n值区分是第几个视频。

> 注意：
> 请务必确保URL为视频文件，而不是包含视频文件的网页地址。

## 事件通知
文件上传成功可触发[事件通知-URL转拉完成](/document/product/266/7831)。APP后台可据此监听点播系统中的URL转拉行为。

更多参见[服务端事件通知简介](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
|pullset.n.url | 是 | String | 需要拉取的第 n 个视频的 URL。n 从0开始，依次递增，下同。 |
|pullset.n.fileName | 是 | String | 视频文件的名称 |
|pullset.n.fileMd5 | 否 | string | 视频文件的MD5 |
|pullset.n.isTranscode | 否 | Integer | 是否转码，0：否，1：是，默认为0；如果不执行转码，可在上传后，在管理控制台视频文件管理进行转码|
|pullset.n.isScreenshot | 否 | Integer | 是否截图，0：否，1：是，默认为0 |
|pullset.n.isWatermark | 否 | Integer | 是否打水印，0：否，1：是，默认为0；如果选择打水印，请务必在管理控制台提前完成水印文件选择和位置设定，否则可能导致上传失败；|
|pullset.n.classId | 否 | Integer | 视频的分类ID |
|pullset.n.tags | 否 | String | 视频的标签，有多个标签的话采用英文逗号分隔 |
|pullset.n.priority | 否 | Integer | 优先级：0:中 1：高 2：低 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

```
https://vod.api.qcloud.com/v2/index.php?Action=MultiPullVodFile
&pullset.0.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.html%3Fvid%3Dc0152uievii
&pullset.0.fileName=test
&pullset.0.isTranscode=1
&pullset.0.priority=1
&pullset.0.isScreenshot=1
&pullset.0.isWatermark=1
&pullset.0.classId=0
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码 |
| message | String | 错误信息说明  |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误  |
| 1000 | 无效参数  |
| 1001 | 用户信息错误 |
| 1010 | 内部错误 |
| 1011 | 内部错误 |
| 1018 | 拉取任务过多，请稍后再试 |
| 1100 | 内部错误 |
| 1159 | 内部错误 |
| 1163 | 没有水印，但请求中指定了要设置水印 |
| 10003 | 内部错误 |

### 应答示例
```javascript
{
    "code": 0,
    "message": ""
}
```
