## 接口名称
InitUpload

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
| fileName | 是 | String | 视频文件本地名称，长度在40个字节以内，不得包含\ / : * ? " < > 等字符（注意不包含文件后缀名，例如.mp4） |
| fileSha | 是 | String | 视频文件的SHA值，计算方法见下文 |
| fileSize | 是 | Integer | 视频文件的总大小，单位字节Byte |
| dataSize | 是 | Integer | 调用分片上传接口(UploadPart)时，每个分片的大小；可选值：524288(512KB)、1048576(1MB) |
| fileType | 是 | String | 视频文件的类型，一般为视频的的后缀名称，例如mp4、flv等 |
| tags.n | 否 | String | 视频标签 |
| classId | 否 | Integer | 视频的分类ID |
| isTranscode | 否 | Integer | 是否转码，0：否，1：是；默认为0；如果不执行转码，可在上传成功后通过控制台进行转码，或者调用([视频转码接口](/document/product/266/7822)) |
| isScreenshot | 否 | Integer | 是否截图，0：否，1：是；默认为0 |
| isWatermark | 否 | Integer | 是否打水印，0：否，1：是，默认为0；如果选择打水印，请务必在管理控制台提前完成水印文件选择和位置设定，否则可能导致上传失败 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

**fileSha的计算方法：**

1. 采用[SHA-1散列算法](https://zh.wikipedia.org/wiki/SHA-1)计算整个视频文件的哈希值，得到160位(20字节)的二进制串；
1. 对得到的二进制串进行十六进制编码，编码算法必须使用小写字母，即a-f，而不是A-F。

### 请求示例
```
https://vod2.qcloud.com/v2/index.php?Action=InitUpload
&fileName=test
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=20350000
&dataSize=1048576
&fileType=mp4
&tags.1=foo
&tags.2=bar
&isTranscode=1
&isScreenshot=1
&isWatermark=1
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 小于0：失败；0：初始化成功，可以进行分片上传；1：文件部分存在，可以进行断点续传； |
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


**上传失败：**

```javascript
{
    "code": -10001,
    "message": "invalid arg",
    "canRetry" : 0
}
```