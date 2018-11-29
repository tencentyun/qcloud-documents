## 服务器端 SDK

服务器端SDK集成了签名生成、对象上传、下载、资源管理等功能，腾讯云-对象存储提供了以下语言的服务器端SDK供开发者下载使用：

[Restful API使用文档](/doc/product/227/API%20概览)

如果开发者希望自行实现签名生成功能，请参照[签名算法](/doc/product/227/签名算法)。

## 客户端SDK

[Android-SDK接入流程及API使用说明](/doc/product/227/Android%20SDK)

[iOS-SDK接入流程及API使用说明](/doc/product/227/iOS%20SDK)

**注意：**SDK中用到的SIGN，推荐使用服务器端SDK提供的接口来生成，并由移动端向业务服务器请求。SIGN的具体生成和使用请参照[签名算法](http://cloud.tencent.com/doc/product/227/%E7%AD%BE%E5%90%8D%E7%AE%97%E6%B3%95)。签名的生成不能在终端APP上进行，否则会产生极大的安全隐患。