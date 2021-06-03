### 使用 JavaScript SDK 实现分块上传时，第一次上传成功后，后续请求都是403，该如何处理？

请求出现403报错，可参考 [访问 COS 时返回403错误码](https://cloud.tencent.com/document/product/436/54303) 文档进行排查。如果您使用临时密钥进行分块上传，建议您检查是否被授予 [分块上传权限](https://cloud.tencent.com/document/product/436/31923#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)，以及授权路径是否正确。

### JavaScript SDK 上传速度达不到满载带宽，该如何处理？

可以使用分块上传接口，通过增加每个分块的大小解决。例如当前设置每个分块大小为1MB，您可以适当调整分块大小为5MB或者其他大小，观察带宽使用情况，详情请参见 [分块上传指引](https://cloud.tencent.com/document/product/436/35649#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1)。

### JavaScript SDK 如何获取文件上传进度？

JavaScript SDK 的简单上传对象接口和分块上传对象接口会返回进度，详情请参考 [对象操作](https://cloud.tencent.com/document/product/436/35649#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1)。

### JavaScript SDK 的 List Multipart Uploads 能否直接获取进度？

当前 List Multipart Uploads 接口需要使用回调函数来返回，暂时无法直接获取。

