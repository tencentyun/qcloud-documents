### 使用临时密钥操作时报错 403，该如何处理？

请检查申请临时密钥时填写的 action 和 allowPrefix 是否正确。

1. 例如调用 cos.putObject()，但是 action 里并没有填写**name/cos:PutObject**，即没有 putObject 权限导致报错 403。
2. 例如操作的 Key 是 `1.jpg`，但是 allowPrefix 填写的是 `test/*`（只允许操作 `test/*` 路径），即没有对应路径的操作权限导致报错 403。

若 aciton 和 allowPrefix 都正确，请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 和 [访问 COS 时返回 403 错误码](https://cloud.tencent.com/document/product/436/54303)。
字段说明：不同语言的 STS SDK，action 和 allowPrefix 所使用的字段不同，例如 STS JAVA SDK 使用的是 allowActions 和 allowPrefixes 字段，请注意留意 STS SDK 中的示例。

### 小程序 SDK 报错请求过期：Request has expired (Status Code: 403; Error Code: AccessDenied)，该如何处理？

由于签名过期导致，重新生成签名即可解决；若重新生成签名仍报相同的错误，可以再检查机器的本地时间是否为标准的北京时间。

### 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，可以使用 `ForcePathStyle:true` 打开后缀式。只需要真正请求的 url，其格式如下：

```
https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>
```

后缀式请求在签名时，存储桶名称 `/<BucketName-APPID>` 也会加入签名计算。

### 小程序如何保存图片到本地？

1. 通过 `cos.getObjectUrl` 获取图片 url。
2. 调用 `wx.downloadFile` 下载图片得到临时路径。
3. 单击保存按钮，调用 `wx.saveImageToPhotosAlbum` 保存到相册。

### QQ 小程序可以使用小程序 SDK 上传文件至 COS 吗？

COS 目前仅支持微信小程序，由于 QQ 小程序和微信小程序不互通，无法使用小程序 SDK。

### 小程序用 cos-wx-sdk-v5 上传文件到存储桶中，getAuthorization 这个函数有什么作用？

小程序 SDK 中的 getAuthorization 函数是后端通过获取临时密钥给到前端，前端计算签名，然后进行上传、删除等操作。推荐您使用临时密钥的形式，防止密钥泄露。详情请参见 [小程序 SDK 创建 COS 实例示例](https://cloud.tencent.com/document/product/436/31953#.E9.85.8D.E7.BD.AE.E9.A1.B9)。
