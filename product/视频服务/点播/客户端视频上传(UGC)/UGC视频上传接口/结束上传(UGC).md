## 接口名称
FinishUploadUGC

## 功能说明
1. 该接口适用于APP将自己**客户端**上的视频上传到点播服务端；
1. 该接口亦可用于APP将自己服务端视频上传到点播服务端的场景，但我们建议使用服务端上传SDK或者服务端上传接口（[InitUpload](/document/product/266/7809)/[UploadPart](/document/product/266/7810)/[FinishUpload](/document/product/266/7811)）来进行上传；
1. 由于视频文件通常较大，故而一般需要采用分片上传的方式；整个上传过程涉及[初始化上传(UGC)](/document/product/266/7902)、[分片上传(UGC)](/document/product/266/7903)、[结束上传(UGC)](/document/product/266/7904)三步，具体流程参见下图；
1. 支持秒传、断点续传；
1. 接口本身逻辑较为复杂，点播封装了多种语言的UGC上传SDK来简化开发者的调用，详见[UGC视频上传综述](/document/product/266/7835)。

![](//mc.qcloudimg.com/static/img/2d025243b3a9c492a53e309f92f3a2c1/image.png)

## 请求方式

### 请求域名
vod2.qcloud.com

> 注意：
> - UGC视频上传、服务端视频上传的域名与其他服务端API不同，**不是**vod.api.qcloud.com；
> - UGC视频上传的签名(signature)生成方式与服务端API不同，方法参见UGC视频上传签名生成；
> - 单个视频文件上传所调用的所有接口，包括[初始化上传(UGC)](/document/product/266/7902)、[分片上传(UGC)](/document/product/266/7903)、[结束上传(UGC)](/document/product/266/7904)，均使用相同的signature；
> - 该接口仅支持GET方法，不支持POST方法。

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileSha | 是 | String | 文件sha |
| signature | 是 | String | UGC上传签名，参见UGC视频上传签名生成 |

### 请求示例

```
https://vod2.qcloud.com/v2/index.php?Action=FinishUploadUGC
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&signature=IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZ
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 小于0：失败；0：成功 |
| message | String | 返回信息说明 |
| codeDesc | String | 后台记录的错误信息，腾讯云后台定位用 |
| canRetry | Integer | 当code小于0时，说明上传过程遇到错误；此时如果该值为1表示该错误可以通过重试来解决，否则表示该错误无法通过重试解决，必须进行排查 |
| fileId | String | 文件id |
| url | String | 文件url |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| -10001 | 检查公共参数出错 |
| -10002 | 检查签名出错 |
| -10003 | 检查协议参数出错 |
| -10004 | 写缓存信息失败 |
| -10005 | 获取缓存信息失败|
| -10006 | 包体非法 |

其他错误码可能为网络原因导致的偶发失败。所有小于0的错误码，当canRetry=1时，均可重试解决。

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "fileId": "7031868222808505913",
    "url": "http://10013.vod2.myqcloud.com/vod10013/7031868222808505913/f0.mp4"
}
```