### 客户端网络正常，但是通过 HTTP 访问 COS 非常慢，或者报错 Connection reset，该如何处理？
部分区域的运营商可能会对 COS 的域名进行劫持，因此尽量通过 HTTPS 来访问 COS。

### 上传进度到了 100%，最终还是回调了 failCallBack 接口，该如何处理？
上传进度这里只是代表 SDK 写入到网络中的进度，100% 并不表示上传完成，只有回调 successCallBack 接口才真正上传成功，如果在最后发送 Complete Multipart Upload 请求时产生了异常，那么会回调 failCallBack 接口。

### 通过 CosTransferManger 上传和下载报错权限问题，该如何处理？
CosTransferManger 下载文件时会先进行 Head 操作，因此需要同时授权 HeadObject 和 GetObject 两个权限，上传时则需要简单上传和分块上传所有接口的权限。

### 调用接口时，报错 lock timeout 或者 no credential for sign，或者签名过期等错误，该如何处理？
如果使用的是临时密钥的方式，请检查 initWithSessionCredentialCallback 方法中返回的密钥是否及时更新了，或者密钥是否有效，如果是临时密钥则需要带上 token。

### 上传时报错 calculate md5 error，该如何处理？
可能是您在上传的过程中修改了文件，导致文件的 MD5 值发生了变化，或者网络很差导致服务端收包产生错误。

### 请求返回 ServerError 错误，该如何处理？
可能是您通过代理访问 COS，但是代理没有做好转发，直接返回了不正确的回包，导致 SDK 解析错误，可以抓包查看客户端接收的回包是否正常。

### 调用接口报错 403 权限错误，该如何处理？
权限问题一般不是 SDK 的问题，请检查自己授权信息。您也可以 [联系我们](https://cloud.tencent.com/document/product/436/37708) 处理。

