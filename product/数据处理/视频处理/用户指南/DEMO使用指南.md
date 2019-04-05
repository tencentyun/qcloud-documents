
新用户请直接参考 COS [iOS Demo](https://cloud.tencent.com/document/product/436/6530) 和 [Android Demo](https://cloud.tencent.com/document/product/436/6517)。

## 1	视频处理 DemoAPP 简介及下载

### 1.1 视频处理 DemoAPP 简介
视频处理 DemoAPP，是腾讯云提供给开发者的一个测试 APP，包括图片（数据万象）和视频（视频处理）两个体验模块。图片体验模块包括图片的上传、暂停、删除、查询和复制等功能；视频体验模块包括视频的上传、暂停、查询和删除等功能。开发者可以使用 DemoAPP 体验腾讯云视频处理服务，也可以在 DemoAPP 上注册自己的 APP 来验证其视频处理服务是否正常开通。 

### 1.2 视频处理 DemoAPP 下载
Android 和 iOS 均参考 [SDK 下载](https://cloud.tencent.com/document/product/314/3499)。

## 2	视频处理 DemoAPP 使用说明
### 2.1	注册 APP
DemoAPP 本身自带了官网内置的APP应用信息，可以直接使用上传、暂停、删除、查询、复制等操作来体验视频处理服务。如果开发者希望验证自己的视频处理服务是否开通，可以在 DemoAPP 上注册自己的 APP，如下图所示，其中
(1). APPID 为开发者在 [移动服务控制台——应用管理](http://app.qcloud.com/) 创建应用时获取的 AppID；
(2). USERID 是开发者自己业务体系中的 userid，用户可以自己设置也可以使用 DemoAPP 自带的 123456；
(3). SIGN 为签名。签名是开发者客户端向其业务服务器请求得到的，验证自己的移动是否开通时，开发者可以参考 [服务器端 SDK](http://cloud.tencent.com/doc/product/314/SDK%E4%B8%8B%E8%BD%BD)，选择熟悉的语言 SDK，根据其提供的接口生成签名。

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-1.jpg)

填写注册信息：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-2.jpg)

### 2.2	使用上传、暂停、删除、查询、复制等操作
图片服务页面如下：

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-3.jpg)

视频服务页面如下：

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-4.jpg)

### 2.3	iOS 返回码说明
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-5.jpg)

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-6.jpg)

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-7.jpg)

### 2.4	Android 返回码说明
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-8.jpg)

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/demo-9.jpg)
