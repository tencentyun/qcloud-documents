## 接口名称
FinishUploadEx

## 功能说明
1. 该接口适用于APP将自己**客户端**上的视频上传到点播服务端；
1. 该接口亦可用于APP将自己服务端视频上传到点播服务端的场景，但我们建议使用服务端上传SDK或者服务端上传接口（[InitUpload](/document/product/266/7809)/[UploadPart](/document/product/266/7810)/[FinishUpload](/document/product/266/7811)）来进行上传；
1. 由于视频文件通常较大，故而一般需要采用分片上传的方式；整个上传过程涉及[初始化上传(UGC)](/document/product/266/7902)、[分片上传(UGC)](/document/product/266/7903)、[结束上传(UGC)](/document/product/266/7904)三步，具体流程参见下图；
1. 支持秒传、断点续传；
1. 若客户端上传成功后将fileID上报到APP服务器，支持APP服务器通过该接口提供的校验信息字段对fileID的合法性进行校验，防止客户端篡改上传文件的信息；
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
| fileSha | 是 | String | 文件sha |
| signature | 是 | String | UGC上传签名，参见UGC视频上传签名生成 |

### 请求示例

```
https://vod2.qcloud.com/v2/index.php?Action=FinishUploadEx
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
| verify_content | String | 信息合法性校验内容，当客户端向业务Server上报上传成功的fileId信息时，可以使用该字段校验上报的fileID是否合法（使用方式请见“合法性校验方式说明”），如果无需校验可以忽略这个字段 |

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
    "verify_content": "MzMyOTY0NGIwNTk4YTc2YzZjNDljNTk3YTJhNzNkOGE1ZjA3YWJlOUV4cFRpbWU9MTQ4ODE2MDI2NCZGaWxlSWQ9NzAzMTg2ODIyMjgwODUwNTkxMw=="
}
```

### 合法性校验方式说明

客户端结束上传后，将获得上传文件的fileId。一般的，APP服务器会要求客户端将上传的fileId上报给服务器记录下来，用于上传视频的管理。但是，如果用户单独上传fileId，APP服务器无法保证fileId的合法性，即用户有可能随意篡改上报的fileId。

为了校验用户上传fileID的合法性，用户可以要求客户端将结束上传得到的响应包体里的verify_content字段连同fileId一起上报到APP服务器，APP服务器可以用点播派发的verify_key来校验fileId是否合法。

####例子
如果用户有校验fileId合法的需求，可以向点播客户索要校验用的verify_key，这个例子中verify_key为字符串```"6367c48dd193d56ea7b0baad25b19455e529f5ee"```。

当客户端结束上传后，将获得fileId和verify_content，这里假设fileId和verify_content分别为字符串```"7031868222808505913"```和字符串```"MzMyOTY0NGIwNTk4YTc2YzZjNDljNTk3YTJhNzNkOGE1ZjA3YWJlOUV4cFRpbWU9MTQ4ODE2MDI2NCZGaWxlSWQ9NzAzMTg2ODIyMjgwODUwNTkxMw=="```。

客户端需要将fileId和verify_content一同上报给APP服务器。

APP服务器接收到verify_content后进行BASE64解码，得到一段二进制内容，其中前20字节为HashedContent，后面剩下的内容为PlainText。

PlainText为字符形式，例子中PlainText为字符串```"ExpTime=1488160264&FileId=7031868222808505913"```。APP服务器可以校验PlainText的内容是否已经过期（ExpTime超过当前服务器时间）以及上报内容是否匹配（FileId是否匹配）。如果内容已经过期或者不匹配，表示验证失败。

如果PlainText校验通过，则对PlainText使用verify_key作为秘钥进行HAMC-SHA1加密并得出结果（例子中的加密结果使用16进制表示为```3329644b0598a76c6c49c597a2a73d8a5f07abe9```），如果该结果能够与前面提到的HashedContent匹配，则验证通过，否则验证失败。