<!-- TODO:
接口需要完善的功能：
调用该接口之后，可以通过查询任务状态接口来查看转拉状态（TODO）；
转拉完成之后，如果配置了服务端回调，云点播后台会发起URL转拉完成之后回调（TODO）。
对于已经存在的转拉任务，是跳过，还是重置？
回调URL，回调方式，不能通过指定，全部读配置

文档需要完善：
错误码 -->


## 接口描述
接口名称：MultiPullVodFile

## 功能说明
1. 通过用户传递的URL，从已有的资源库批量拉取视频文件到腾讯云；
2. 支持批量拉取多个视频文件，通过输入参数中的n值区分是第几个视频。

## 请求方式

### 请求域名
vod2.api.qcloud.com

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
|pullset.n.url | 是 | String | 需要拉取的视频URL，n为一个整数，第一个视频n填1，第二个视频n填2，依次递增；下同|
|pullset.n.fileName | 是 | String | 视频文件的名称|
|pullset.n.fileMd5 | 否 | string | 视频文件的MD5|
|pullset.n.isTranscode | 否 | Int | 是否转码，0：否，1：是，默认为0；如果不执行转码，可在上传后，在管理控制台视频文件管理进行转码；|
|pullset.n.isScreenshot | 否 | Int | 是否截图，0：否，1：是，默认为0|
|pullset.n.isWatermark | 否 | Int | 是否打水印，0：否，1：是，默认为0；如果选择打水印，请务必在管理控制台提前完成水印文件选择和位置设定，否则可能导致上传失败；|
|pullset.n.notifyUrl | 否 | String | 腾讯云通过回调该URL地址通知；调用方该视频已经拉取完毕。|
|pullset.n.classId | 否 | Int | 视频的分类ID|
|pullset.n.tags | 否 | String | 视频的标签，有多个标签的话采用逗号分隔|
|pullset.n.priority | 否 | Int | 优先级0:中 1：高 2：低|
|pullset.n.isReport | 否 | Int | 回调开关，是否需要回包给开发商，0：否，1：是，默认为0|

### 请求示例
```
https://vod2.api.qcloud.com/v2/index.php?Action=ActionName
&pullset.1.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.html%3Fvid%3Dc0152uievii
&pullset.1.fileName=test
&pullset.1.isTranscode=1
&pullset.1.priority=1
&pullset.1.isScreenshot=1
&pullset.1.isWatermark=1
&pullset.1.notifyUrl=http%3A%2F%2Ftest.com%2Ftest
&pullset.1.classId=0
&pullset.1.isReport=1
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Int | 错误码 |
| message | String | 错误信息说明  |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| aaa-bbb | 公共错误码，参见xxxx。  |
| xxx | 说明说明说明说明  |
| yyy | 说明说明说明说明 |

### 应答示例
```
{
    "code": 0,
    "message": ""
}
```
