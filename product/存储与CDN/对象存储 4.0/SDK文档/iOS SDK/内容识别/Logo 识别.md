

## 简介

本文档提供关于Logo 识别相关的 API 概览以及 SDK 示例代码。

| API                                                          | 操作描述                                  |
| ------------------------------------------------------------ | ----------------------------------------- |
| [Logo 识别](https://cloud.tencent.com/document/product/436/79734) | 对象存储通过数据万象 RecognizeLogo 接口实现对图片内电商 Logo 的识别，返回图片中 Logo 的名称、坐标、置信度分值。|

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。


## Logo 识别

对象存储通过数据万象 RecognizeLogo 接口实现对图片内电商 Logo 的识别，返回图片中 Logo 的名称、坐标、置信度分值。

> ! COS iOS SDK 版本需要大于等于 v6.1.6。

#### 示例代码
**Objective-C**

[//]: # (.cssg-snippet-head-object)
```objective-c
QCloudCIRecognizeLogoRequest * request = [QCloudCIRecognizeLogoRequest new];
request.regionName = @"regionName";
// 对象键，是对象在 COS 上的完整路径，如果带目录的话，格式为 "dir1/object1"
request.object = @"exampleobject";
// 存储桶名称，格式为 BucketName-APPID
request.bucket = @"examplebucket-1250000000";
[request setFinishBlock:^(QCloudCILogoRecognitionResult * _Nullable result, NSError * _Nullable error) {
    
}];
[[QCloudCOSXMLService defaultCOSXML] RecognizeLogo:request];
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/RecognizeLogo.m) 查看。
