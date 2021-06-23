### 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，使用`ForcePathStyle:true`可以打开后缀式，只需要真正请求 url 格式如下`https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>`后缀式请求，在签名时存储桶名称`/<BucketName-APPID>`也会加入签名计算。

### 小程序如何保存图片到本地？

先预先通过`cos.getObjectUrl`获取图片 url，而后调用`wx.downloadFile`下载图片得到临时路径，界面显示保存图片按钮，用户单击按钮后，调用`wx.saveImageToPhotosAlbum` 保存到相册。


### QQ 小程序可以使用小程序 SDK 上传文件至 COS 吗？

COS 目前仅支持微信小程序，由于 QQ 小程序和微信小程序不互通，无法使用小程序 SDK。

### 小程序用 cos-wx-sdk-v5 上传文件到存储桶中，getAuthorization 这个函数有什么作用？

小程序 SDK 中的 getAuthorization 函数是后端通过获取临时密钥给到前端，前端计算签名，然后进行上传、删除等操作。推荐您使用临时密钥的形式，防止密钥泄露。详情请参见 [小程序 SDK 创建 COS 实例示例](https://cloud.tencent.com/document/product/436/31953#.E9.85.8D.E7.BD.AE.E9.A1.B9)。

### COS 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，使用 ForcePathStyle:true 可以打开后缀式，只需要真正请求的 url，其格式如下。后缀式请求，在签名时存储桶名称 `<BucketName-APPID>` 也会加入签名计算。
```
https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>
```
