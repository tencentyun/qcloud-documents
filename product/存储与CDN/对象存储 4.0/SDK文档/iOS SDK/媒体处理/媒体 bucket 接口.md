## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况 |用于查询已经开通媒体处理功能的存储桶      |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

>! COS iOS SDK 版本需要大于等于 v5.9.6。

#### 请求示例
**Objective-C**

[//]: # (.cssg-snippet-media-buckets)
```objective-c
QCloudGetDescribeMediaBucketsRequest * request = [[QCloudGetDescribeMediaBucketsRequest alloc]init];

// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域
request.regions = @[@"ap-shanghai"];
// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
request.bucketNames = @[@"examplebucket-1250000000"];
// 存储桶名称前缀，前缀搜索
request.bucketName = @"examplebucket-1250000000";
// 第几页
request.pageNumber = 0;
// 每页个数
request.pageSize = 100;

request.finishBlock = ^(QCloudDescribeMediaInfo * outputObject, NSError *error) {
    // outputObject 请求到的媒体信息，详细字段请查看api文档或者SDK源码
    // QCloudDescribeMediaInfo  类；
};
[[QCloudCOSXMLService defaultCOSXML] CIGetDescribeMediaBuckets:request];
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/GetSnapshot.m) 查看。


**Swift**

[//]: # (.cssg-snippet-media-buckets)
```swift
let request : QCloudGetDescribeMediaBucketsRequest = QCloudGetDescribeMediaBucketsRequest();
// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域
request.regions = ["ap-shanghai"];
// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
request.bucketNames = ["bucketNames"];
// 存储桶名称前缀，前缀搜索
request.bucketName = "bucketName";
// 第几页
request.pageNumber = 0;
// 每页个数
request.pageSize = 100;
        
request.finishBlock = { (result, error) in
    // result 请求到的媒体信息，详细字段请查看api文档或者SDK源码
    // QCloudMediaInfo 类；
}
QCloudCOSXMLService.defaultCOSXML().ciGetDescribeMediaBuckets(request);
```
>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/GetSnapshot.swift) 查看。

