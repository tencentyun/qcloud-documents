## 接口名称
UploadPart

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
> - 该接口仅支持POST方法，不支持GET方法。

### 最高调用频率
10000次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileSha | 是 | String | 整个文件SHA（注意不是当前分片的SHA），必须与初始化上传(InitUpload)中所填写的fileSha一致 |
| offset | 是 | Integer | 分片在文件中的相对偏移，注意该值必须为dataSize的整数倍 |
| dataSize | 是 | Integer | 分片大小，详见下文介绍 |
| dataMd5 | 是 | String | 该分片所上传数据的md5，计算方法详见 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

**dataMd5的计算方法：**

1. 采用[MD5散列算法](https://zh.wikipedia.org/wiki/MD5)计算整个视频文件的哈希值，得到128位(16字节)的二进制串；
1. 对得到的二进制串进行十六进制编码，编码算法必须使用小写字母，即a-f，而不是A-F。

**关于dataSize：**

1. 除了最后一个分片之外，其他分片dataSize的值必须与调用初始化上传(InitUpload)时传入的值保持一致；
1. 最后一个分片的dataSize必须小于等于初始化上传(InitUpload)时传入的dataSize值。

**举例：**

1. 假定需要上传一个6000000字节（大约5.72MB）的视频文件，初始化上传时设置的dataSize为1048576(1MB)；
1. 整个视频会被分为6个分片，对于前五个分片，其dataSize为1048576(1MB)，offset分别为0, 1048576, 2097152，3145728，4194304；
1. 对于最后一个分片，其dataSize为757120(计算方法：6000000 - 5 * 1048576)，offset为5242880。

### 请求示例
如下为请求URL，真正的视频数据需要在POST请求的body中提交。

```
https://vod2.qcloud.com/v2/index.php?Action=UploadPart
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&offset=0
&dataSize=1048576
&dataMd5=0bee89b07a248e27c83fc3d5951213c1
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

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| -10001 | 检查公共参数出错 |
| -10002 | 检查签名出错 |
| -10003 | 检查协议参数出错 |
| -10004 | 写缓存信息失败 |
| -10005 | 获取缓存信息失败|
| -10006 | 包体非法 |

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "",
    "canRetry": 0
}
```
