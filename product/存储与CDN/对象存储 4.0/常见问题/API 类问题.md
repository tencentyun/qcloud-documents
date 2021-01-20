
### 调用 API 接口时，出现“Request has expired”等错误信息，该如何处理？

出现该提示，存在两种可能：
- 一是因为您发起请求的时间超过了签名的有效时间。
- 二是您本地系统时间和所在时区的时间不一致。

针对第一种可能，建议重新获取有效的请求签名再进行 API 操作。若是第二种可能，请将您的本地系统时间按照所在时区的时间进行校正。

### 如何调用 API 删除掉未完成上传文件？

首先调用接口 ListMultipartUploads 列出未完成上传文件，然后调用 Abort Multipart upload 接口舍弃一个分块上传并删除已上传的块。

### 调用批量删除接口返回正确，但实际文件删除失败怎么办？

请检查删除的文件路径，文件路径不需要以`/`开头。



### 通过 JSON API 创建的存储桶和上传的对象，是否可以使用 XML API 管理？

可以，XML API 是基于 COS 底层架构，可以通过 XML API 操作由 JSON API 产生的数据。

### XML API 与 JSON API 之间的关系？

JSON API 接口即从2016年9月起用户接入 COS 使用的 API，上传域名为`<Region>.file.myqcloud.com`。 JSON API 接口将保持维护状态，可以正常使用但是不发展新特性。其与标准 XML API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。

### XML API 与 JSON API 的密钥是否通用？

通用。有关密钥信息可前往 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中的**云 API 密钥**页面进行查看和获取。

### XML API 与 JSON API 的签名是否通用？

不通用，XML API 和 JSON API 各自有各自的签名方式。详情请参见：

- [JSON API 签名](https://cloud.tencent.com/document/product/436/6054)
- [XML API 签名](https://cloud.tencent.com/document/product/436/7778)

### XML API 与 JSON API 设置的 ACL 权限是否通用？

不通用，XML API 和 JSON API 各自有各自的 ACL 权限。


### 如何通过 API 修改对象的存储类型？

用户可通过调用 PUT  Object - Copy 接口，修改 x-cos-storage-class 参数实现修改对象的存储类型，详情请参见 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881)。

### 对象存储怎么设置签名永久有效？

对象存储的签名是使用时间戳来判断请求是否过期，并不能设置永久有效。假设用户使用永久密钥生成签名，希望签名达到长期有效的目的，可以设置一个较为长久的时间戳，例如过期时间为当前时间+50年。若用户使用临时密钥生成签名，由于临时密钥的有效期最多为2小时，那么生成的签名，其有效期也在2小时内。



