### 如何调用 API 删除掉未完成上传文件？

首先调用接口 ListMultipartUploads 列出未完成上传文件，然后调用 Abort Multipart upload 接口舍弃一个分块上传并删除已上传的块。

### 调用批量删除接口返回正确，但实际文件删除失败怎么办？

请检查删除的文件路径，文件路径不需要以“/”开头。

### 通过 JSON API 创建的存储桶和上传的对象，是否可以使用 XML API 管理？

可以，XML API 是基于 COS 底层架构，可以通过 XML API 操作由 JSON API 产生的数据。

### XML API 与 JSON API 之间的关系？

 JSON API 接口即从 2016 年 9 月起用户接入 COS 使用的 API，上传域名为`<Region>.file.myqcloud.com`。 JSON API 接口将保持维护状态，可以正常使用但是不发展新特性。其与标准 XML API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。

### XML API 与 JSON API 的密钥是否通用？

通用，密钥可通过 [云 API 密钥控制台](https://console.cloud.tencent.com/capi) 查看。

### XML API 与 JSON API 的签名是否通用？

不通用，XML API 和 JSON API 各自有各自的签名方式。详情请参考：

- [JSON API 签名](https://cloud.tencent.com/document/product/436/6054)
- [XML API 签名](https://cloud.tencent.com/document/product/436/7778)

### XML API 与 JSON API 设置的 ACL 权限是否通用？

不通用，XML API 和 JSON API 各自有各自的 ACL 权限。

### 如何获取 Python SDK 下载文件的临时链接？

详情请查阅 [获取预签名下载链接](https://cloud.tencent.com/document/product/436/12270#.E8.8E.B7.E5.8F.96.E9.A2.84.E7.AD.BE.E5.90.8D.E4.B8.8B.E8.BD.BD.E9.93.BE.E6.8E.A5) 文档。

### 最新版本 SDK 是否支持 C# SDK?

暂不支持，预计2月中旬上线。

### SDK 能否使用 CDN 加速域名进行访问？

支持，请根据您所使用的编程语言，并参阅对应的 [SDK 文档](https://cloud.tencent.com/document/sdk) 进行操作。


### 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，使用`ForcePathStyle:true`可以打开后缀式，只需要真正请求 url 格式如下 https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>后缀式请求，在签名时会存储桶名称 /<BucketName-APPID> 也会加入签名计算。

### 小程序如何保存图片到本地？
先预先通过`cos.getObjectUrl`获取图片 url，而后调用`wx.downloadFile`下载图片得到临时路径，界面显示保存图片按钮，用户单击按钮后，调用`wx.saveImageToPhotosAlbum 保存到相册。
