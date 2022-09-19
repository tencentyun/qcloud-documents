

## 简介

本文档提供关于开通AI 内容识别服务并生成队列相关的 API 概览以及 SDK 示例代码。

| API                                                          |  说明                                  |
| ------------------------------------------------------------ | ----------------------------------------- |
| [开通AI 内容识别服务并生成队列](https://cloud.tencent.com/document/product/436/79596) |接口用于开通AI 内容识别服务并生成队列。               |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。

## 开通AI 内容识别服务并生成队列

#### 功能说明

接口用于开通AI 内容识别服务并生成队列

>! COS iOS SDK 版本需要大于等于 v6.1.4。
>

#### 示例代码

**Objective-C**

```objective-c
QCloudOpenAIBucketRequest * request = [[QCloudOpenAIBucketRequest alloc]init];

// 存储桶名称，格式为 BucketName-APPID
request.bucket = @"examplebucket-1250000000";

request.regionName = @"regionName";

[request setFinishBlock:^(QCloudOpenAIBucketResult *  _Nullable result, NSError * _Nullable error) {
    // result 详细字段请查看api文档或者SDK源码
    // QCloudOpenAIBucketResult 类；
}];
[[QCloudCOSXMLService defaultCOSXML] OpenAIBucket:request];
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/WordsGeneralizeQueue.m) 查看。
>

**Swift**

```swift
let request = QCloudOpenAIBucketRequest.init();

// 存储桶名称，格式为 BucketName-APPID
request.bucket = "examplebucket-1250000000";

request.regionName = "regionName";

request.setFinish { outputObject, error in
    // outputObject 详细字段请查看api文档或者SDK源码
    // QCloudOpenAIBucketResult 类；
}
QCloudCOSXMLService.defaultCOSXML().openAIBucket(request);
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/WordsGeneralizeQueue.swift) 查看。
>

