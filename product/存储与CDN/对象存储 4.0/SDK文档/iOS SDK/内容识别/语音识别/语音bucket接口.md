

## 简介

本文档提供关于查询语音识别开通状态相关的 API 概览以及 SDK 示例代码。

| API                                                          |  说明                                  |
| ------------------------------------------------------------ | ----------------------------------------- |
| [查询语音识别开通状态](https://cloud.tencent.com/document/product/436/47598) |接口用于查询存储桶是否已开通语音识别功能。               |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询语音识别开通状态

#### 功能说明

接口用于查询存储桶是否已开通语音识别功能。

>! COS iOS SDK 版本需要大于等于 v6.1.3。
>

#### 示例代码

**Objective-C**

[//]: # (.cssg-snippet-get-audiodiscern-bucketlist)
```objective-c
QCloudGetAudioDiscernOpenBucketListRequest * request = [[QCloudGetAudioDiscernOpenBucketListRequest alloc]init];

// 存储桶名称前缀，前缀搜索
request.bucketName = @"examplebucket-1250000000";

request.regionName = @"regionName";
// 地域信息，以“,”分隔字符串，支持 All、ap-shanghai、ap-beijing
request.regions = @"regions";

request.finishBlock = ^(QCloudGetAudioOpenBucketListResult * outputObject, NSError *error) {
    // outputObject 详细字段请查看api文档或者SDK源码
    // QCloudGetAudioOpenBucketListResult 类；
};
[[QCloudCOSXMLService defaultCOSXML] GetAudioDiscernOpenBucketList:request];
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/AudioDiscernTaskQueue.m) 查看。
>

**Swift**

[//]: # (.cssg-snippet-get-audiodiscern-bucketlist)
```swift
let request = QCloudGetAudioDiscernOpenBucketListRequest.init();

// 存储桶名称前缀，前缀搜索
request.bucketName = "examplebucket-1250000000";

request.regionName = "regionName";
// 地域信息，以“,”分隔字符串，支持 All、ap-shanghai、ap-beijing
request.regions = "regions";

request.setFinish { outputObject, error in
    // outputObject 详细字段请查看api文档或者SDK源码
    // QCloudGetAudioOpenBucketListResult 类；
}
QCloudCOSXMLService.defaultCOSXML().getAudioDiscernOpenBucketList(request);
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/AudioDiscernTaskQueue.swift) 查看。
>

