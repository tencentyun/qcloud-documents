### 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，使用`ForcePathStyle:true`可以打开后缀式，只需要真正请求 url 格式如下`https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>`后缀式请求，在签名时存储桶名称`/<BucketName-APPID>`也会加入签名计算。

### 小程序如何保存图片到本地？

先预先通过`cos.getObjectUrl`获取图片 url，而后调用`wx.downloadFile`下载图片得到临时路径，界面显示保存图片按钮，用户单击按钮后，调用`wx.saveImageToPhotosAlbum` 保存到相册。
