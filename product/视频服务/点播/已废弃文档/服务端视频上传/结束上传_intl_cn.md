## 接口名称
FinishUpload

## 功能说明
1. 该接口适用于APP将自己**服务器**上的视频上传到点播服务端；
1. 对于将**客户端**（iOS/Android/Web）视频上传到点播服务端的需求（UGC），**不适合**使用该接口进行上传（因为APP不应当将自己的SecretId和SecretKey暴露到客户端）；应当使用[UGC视频上传综述](/document/product/266/7835)中描述的方法进行上传；
1. 由于视频文件通常较大，故而一般需要采用分片上传的方式；整个上传过程涉及[初始化上传](/document/product/266/7809)、[分片上传](/document/product/266/7810)、[结束上传](/document/product/266/7811)三步，具体流程参见下图；
1. 支持断点续传；
1. 接口本身逻辑较为复杂，点播封装了多种语言的SDK来简化开发者的调用；我们建议开发者直接使用服务端SDK来实现服务端本地视频上传逻辑。

![](//mc.qcloudimg.com/static/img/0e4d6bd7e7b153089d9bc5982947964e/image.png)

## 事件通知
文件上传成功可触发[事件通知-视频上传完成](/document/product/266/7830)。APP后台可据此监听点播系统中的视频上传行为。

更多参见[服务端事件通知简介](/document/product/266/7829)。

## 请求方式

### 请求域名
vod2.qcloud.com

> 注意：
> - 服务端视频上传的域名与其他服务端API不同，**不是**vod.api.qcloud.com；
> - 该接口仅支持GET方法，不支持POST方法。

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileSha | 是 | String | 文件sha |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

```
https://vod2.qcloud.com/v2/index.php?Action=FinishUpload
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&COMMON_PARAMS
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