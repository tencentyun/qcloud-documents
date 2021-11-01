## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况 |用于查询已经开通媒体处理功能的存储桶      |

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

>! COS iOS SDK 版本需要大于等于 v5.9.6。

#### 请求示例
**Objective-C**
```objective-c
QCloudGetDescribeMediaBucketsRequest * reqeust = [[QCloudGetDescribeMediaBucketsRequest alloc]init];

// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域
request.regions = regions;
// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
request.bucketNames = bucketNames;
// 存储桶名称前缀，前缀搜索
request.bucketName = bucketName;
// 第几页
request.pageNumber = pageNumber;
// 每页个数
request.pageSize = pageSize;

reqeust.finishBlock = ^(QCloudDescribeMediaInfo * outputObject, NSError *error) {
    // outputObject 请求到的媒体信息，详细字段请查看api文档或者SDK源码
    // QCloudDescribeMediaInfo  类；
};
[[QCloudCOSXMLService defaultCOSXML] CIGetDescribeMediaBuckets:reqeust];
```

**Swift**
```swift
let request : QCloudGetDescribeMediaBucketsRequest = QCloudGetDescribeMediaBucketsRequest();
// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域
request.regions = regions;
// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
request.bucketNames = bucketNames;
// 存储桶名称前缀，前缀搜索
request.bucketName = bucketName;
// 第几页
request.pageNumber = pageNumber;
// 每页个数
request.pageSize = pageSize;
        
request.finishBlock = { (result, error) in
    // result 请求到的媒体信息，详细字段请查看api文档或者SDK源码
    // QCloudMediaInfo 类；
}
QCloudCOSXMLService.defaultCOSXML().CIGetDescribeMediaBuckets(request);
```

