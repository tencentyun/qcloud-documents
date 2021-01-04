### 客户端网络正常，但是通过 http 访问 cos 非常慢，或者报错 Connection reset，该如何处理？
部分区域的运营商可能会对 cos 的域名进行劫持，因此尽量通过 https 来访问 cos。

### 调用完成分块上传接口时没有包含 etag 信息，导致报错 400 BadRequest，该如何处理？
可能是所在的网络过滤了 Etag 头部，sdk 在上传分块后没有解析到对应的参数，导致 sdk 在结束分块上传时报错。

### QCloudResultListener 或者其他回调函数没有回调，该如何处理？
如果您是通过日志查看没有回调，可能是输出日志过滤级别太高，或者其他过滤方式将日志过滤了，可以调整过滤规则，或者通过在回调函数中打断点的方式来判断回调情况。

### 调用接口时报错 NoClassDefFoundError，该如何处理？
sdk 依赖于 bolts 和 okHttp 两个常见的类，如果是这两个类中的方法找不到，那么可能是您自己的项目中也导入了这两个依赖，但是版本较低，尽量使用和 sdk 中相同的版本，或者更高的版本。

### SDK 获取手机权限问题，该如何处理？
如果需要在外部存储中上传或者下载文件，那么必须获取网络和外部存储读写权限，其他权限比如定位权限，设备信息权限均不是必须权限，如果对权限问题很敏感，可以不导入 MtaUtils 这个包，或者升级到 5.5.8 及其以上版本。

### 使用 https 报错 `java.security.cert.CertPathValidatorException: Trust anchor for certification path not found`，该如何处理？
如果您是通过代理的方式访问 cos，那么首先检查下代理是否支持 https，否则请向我们 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。

### 上传进度到了 100%，最终还是回调了 onFailed 接口，该如何处理？
上传进度这里只是代表 sdk 写入到网络中的进度，100% 并不表示上传完成，只有回调 onSuccess 接口才真正上传成功，如果在最后发送 Complete Multipart Upload 请求时产生了异常，那么会回调 onFailed 接口。

### 使用分块上传报错，比如 400 BadRequest、409 Conflict 等错误，该如何处理？
请尽量使用 sdk 提供的高级接口 TransferManager 来上传和下载，不要自己去封装分块上传的接口，否则很容易出错。

### 通过 TransferManager 上传和下载报错权限问题，该如何处理？
TransferManager 下载文件时会先进行 Head 操作，因此需要同时授权 HeadObject 和 GetObject 两个权限，上传时则需要简单上传和分块上传所有接口的权限。

### 调用接口时，报错 lock timeout 或者 no credential for sign，或者签名过期等错误，该如何处理？
如果您自己实现了 BasicLifecycleCredentialProvider#fetchNewCredentials() 方法，请在这里判断密钥是否及时更新了，或者密钥是否有效，如果是临时密钥则需要带上 token。

### 上传报错 `java.lang.RuntimeException: Can't create handler inside thread that has not called Looper.prepare()`，该如何处理？
如果在主线程中调用 TransferManager#upload() 方法进行上传时报该错误，这个是 mta 上报事件误报了，不影响使用。此外您也可以升级到 5.5.8 及其以上版本解决。

### 在回调中直接操作 ui 导致应用报错，该如何处理？
sdk 回调线程不一定是主线程，请不要直接操作 ui。

### 上传时报错 calculate md5 error，该如何处理？
可能是您在上传的过程中修改了文件，导致文件的 MD5 值发生了变化，或者网络很差导致服务端收包产生错误。

### 请求返回 ServerError 错误，该如何处理？
可能是您通过代理访问 cos，但是代理没有做好转发，直接返回了不正确的回包，导致 sdk 解析错误，可以抓包查看客户端接收的回包是否正常。

### 调用接口报错 403 权限错误，该如何处理？
权限问题一般不是 sdk 的问题，检查自己授权信息，或者 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。
