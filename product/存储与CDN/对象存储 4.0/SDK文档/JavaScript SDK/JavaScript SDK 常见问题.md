### 上传时报错 cors error，该如何处理？

报错如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/47bdd8a90f724d577a60f7b8dcb894e4.png)
原因是存储桶的跨域访问没有正确设置，请 [参考文档](https://cloud.tencent.com/document/product/436/11488) 进行跨域设置。

### 使用临时密钥操作时报错 403，该如何处理？

请检查申请临时密钥时填写的 action 和 allowPrefix 是否正确。

1. 例如调用 cos.putObject()，但是 action 里并没有填写**name/cos:PutObject**，即没有 putObject 权限导致报错 403。
2. 例如操作的 Key 是 `1.jpg`，但是 allowPrefix 填写的是 `test/*`（只允许操作 `test/*` 路径），即没有对应路径的操作权限导致报错 403。

若 aciton 和 allowPrefix 都正确，请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 和 [访问 COS 时返回 403 错误码](https://cloud.tencent.com/document/product/436/54303)。
字段说明：不同语言的 STS SDK，action 和 allowPrefix 所使用的字段不同，例如 STS JAVA SDK 使用的是 allowActions 和 allowPrefixes 字段，请注意留意 STS SDK 中的示例。

### JavaScript SDK 报错请求过期：Request has expired (Status Code: 403; Error Code: AccessDenied)，该如何处理？

由于签名过期导致，重新生成签名即可解决；若重新生成签名仍报相同的错误，可以再检查机器的本地时间是否为标准的北京时间。

### 使用 JavaScript SDK 实现分块上传时，第一次上传成功后，后续请求都是 403，该如何处理？

请求出现 403 报错，可参考 [访问 COS 时返回 403 错误码](https://cloud.tencent.com/document/product/436/54303) 文档进行排查。如果您使用临时密钥进行分块上传，建议您检查是否被授予 [分块上传权限](https://cloud.tencent.com/document/product/436/31923#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)，以及授权路径是否正确。

### JavaScript SDK 上传速度达不到满载带宽，该如何处理？

可以使用分块上传接口，通过增加每个分块的大小解决。例如当前设置每个分块大小为 1MB，您可以适当调整分块大小为 5MB 或者其他大小，观察带宽使用情况，详情请参见 [分块操作](https://cloud.tencent.com/document/product/436/64960#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)。

### JavaScript SDK 如何获取文件上传进度？

JavaScript SDK 的简单上传对象接口和分块上传对象接口会返回进度，详情请参考 [分块操作](https://cloud.tencent.com/document/product/436/64960#.E5.88.86.E5.9D.97.E6.93.8D.E4.BD.9C)。

### JavaScript SDK 的 List Multipart Uploads 能否直接获取进度？

当前 List Multipart Uploads 接口需要使用回调函数来返回，暂时无法直接获取。
