## 接口名称
InitUploadEx

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
> - 该接口仅支持GET方法，不支持POST方法。

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileSha | 是 | String | 视频文件的SHA值，计算方法见下文 |
| fileSize | 是 | Integer | 视频文件的总大小，单位字节Byte |
| dataSize | 是 | Integer | 调用分片上传接口(UploadPartEx)时，每个分片的大小；可选值：524288(512KB)、1048576(1MB) |
| signature | 是 | String | UGC上传签名，参见UGC视频上传签名生成 |

**注意：**

- 文件名称、文件分类、是否转码等控制项，不是由客户端指定的，而是由服务端在signature中传递。

**fileSha的计算方法：**

1. 采用[SHA-1散列算法](https://zh.wikipedia.org/wiki/SHA-1)计算整个视频文件的哈希值，得到160位(20字节)的二进制串；
1. 对得到的二进制串进行十六进制编码，编码算法必须使用小写字母，即a-f，而不是A-F。

### 请求示例
```
https://vod2.qcloud.com/v2/index.php?Action=InitUploadEx
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=20350000
&dataSize=1048576
&signature=IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZ
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 小于0：失败；0：初始化成功，可以进行分片上传；1：文件部分存在，可以进行断点续传；2：文件已经存在，无需再次上传(秒传) |
| message | String | 返回信息说明 |
| listParts | Array | 当可以进行断点续传时(即code为1)，该数组列出了服务端目前已经存在的分片，这些分片无需再次进行上传 |
| listParts.offset | Integer | 已经存在的分片在文件中的相对偏移 |
| listParts.dataSize | Integer | 已经存在的分片的大小 |
| listParts.dataMd5 | String | 已经存在的分片的md5 |
| codeDesc | String | 后台记录的错误信息 |
| dataSize | Integer | code为1时返回，表示该文件可以进行断点续传，但之前的上传已指定了分片大小，本次上传过程中，后续的分片上传(UploadPart)的dataSize必须需以此值为准 |
| fileId | String | code为2时返回，表示文件已经存在，该值表示视频文件的fileId |
| url | String | code为2时返回，表示文件已经存在，该值表示视频文件的url |
| canRetry | Integer | 当code小于0时，说明上传过程遇到错误；此时如果该值为1表示该错误可以通过重试来解决，否则表示该错误无法通过重试解决，必须进行排查 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| -10001 | 检查公共参数出错 |
| -10002 | 检查签名出错 |
| -10003 | 检查协议参数出错 |
| -10004 | 写缓存信息失败 |
| -10005 | 获取缓存信息失败|
| -10006 | 包体非法 |

其他错误码可能为网络原因导致的偶发失败。所有小于0的错误码，当canRetry为1时，均可重试解决。

### 应答示例

**正常上传：**

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "",
    "canRetry": 0
}
```

**断点续传：**

如下应答包体的含义是：视频文件的第一个1MB的分片，以及第二个1MB的分片已经存在，后续的分片上传(UploadPart)无需再上传这两个分片，只需补齐其他分片即可。

```javascript
{
    "code": 1,
    "message": "",
    "codeDesc": "",
    "canRetry": 0,
    "listParts": [
        {
            "offset": 0,
            "dataSize": 1048576,
            "dataMd5": "0bee89b07a248e27c83fc3d5951213c1"
        },
        {
            "offset": 1048576,
            "dataSize": 1048576,
            "dataSha": "f5ac8127b3b6b85cdc13f237c6005d80"
        }
    ]
}
```

**秒传：**

```javascript
{
    "code": 2,
    "message": "",
    "fileId": "16092504232103571364",
    "url": "http://10013.vod2.myqcloud.com/vod10013/16092504232103571364/f0.mp4"
}
```

**上传失败：**

```javascript
{
    "code": -10001,
    "message": "invalid arg",
    "canRetry" : 0
}
```