### 使用 Go SDK 如何读取文件的所有属性？

使用 [GET Object](https://cloud.tencent.com/document/product/436/35057#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1) 接口，在 Response.Header 中获取文件属性。

### Go SDK 支持上传文件流吗？

支持上传文件流或字节流，详情请参见 [上传对象](https://cloud.tencent.com/document/product/436/65644) 文档。


### Go SDK 报错“403 AccessDenied(Message: Request has expired, RequestId: xxx, TraceId: xxx)”，该如何处理？


由于签名过期导致，重新生成签名即可解决；若重新生成签名仍报相同的错误，可以再检查下机器的本地时间是否已设置为标准的北京时间。


