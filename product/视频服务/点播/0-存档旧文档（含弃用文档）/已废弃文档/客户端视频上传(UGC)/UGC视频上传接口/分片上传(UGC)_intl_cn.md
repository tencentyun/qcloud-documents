## 接口名称
UploadPartEx

## 功能说明
1. 该接口适用于APP将自己**客户端**上的视频上传到点播服务端；
1. 该接口亦可用于APP将自己服务端视频上传到点播服务端的场景，但我们建议使用服务端上传SDK或者服务端上传接口（[InitUpload](/document/product/266/7809)/[UploadPart](/document/product/266/7810)/[FinishUpload](/document/product/266/7811)）来进行上传；
1. 由于视频文件通常较大，故而一般需要采用分片上传的方式；整个上传过程涉及[初始化上传(UGC)](/document/product/266/7902)、[分片上传(UGC)](/document/product/266/7903)、[结束上传(UGC)](/document/product/266/7904)三步，具体流程参见下图；
1. 支持秒传、断点续传；
1. 接口本身逻辑较为复杂，点播封装了多种语言的UGC上传SDK来简化开发者的调用，详见[UGC视频上传综述](/document/product/266/7835)。

![](//mc.qcloudimg.com/static/img/03bceeaebef439eb218edd080ef4d7fa/image.png)

## 请求方式

### 请求域名
vod2.qcloud.com

> 注意：
> - UGC视频上传、服务端视频上传的域名与其他服务端API不同，**不是**vod.api.qcloud.com；
> - UGC视频上传的签名(signature)生成方式与服务端API不同，方法参见UGC视频上传签名生成；
> - 单个视频文件上传所调用的所有接口，包括[初始化上传(UGC)](/document/product/266/7902)、[分片上传(UGC)](/document/product/266/7903)、[结束上传(UGC)](/document/product/266/7904)，均使用相同的signature；
> - 该接口仅支持POST方法，不支持GET方法。

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileSha | 是 | String | 文件SHA（注意不是当前分片的SHA），必须与初始化上传(InitUpload)中所填写的fileSha一致 |
| offset | 是 | Integer | 分片在文件中的相对偏移，注意该值必须为dataSize的整数倍 |
| dataSize | 是 | Integer | 分片大小，详见下文介绍 |
| dataMd5 | 是 | String | 该分片所上传数据的md5，计算方法详见 |
| signature | 是 | String | UGC上传签名，参见UGC视频上传签名生成 |

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
https://vod2.qcloud.com/v2/index.php?Action=UploadPartEx
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&offset=0
&dataSize=1048576
&dataMd5=0bee89b07a248e27c83fc3d5951213c1
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
