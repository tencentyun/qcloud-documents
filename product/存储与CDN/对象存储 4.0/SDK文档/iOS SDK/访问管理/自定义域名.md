## 简介

本文档提供关于自定义域名的 API 概览以及 SDK 示例代码。

| API               | 操作名         | 操作描述                   |
| ----------------- | -------------- | -------------------------- |
| PUT Bucket domain | 设置自定义域名 | 设置存储桶的自定义域名信息 |
| GET Bucket domain | 查询自定义域名 | 查询存储桶的自定义域名信息 |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。

## 设置自定义域名

#### 功能说明

PUT Bucket domain 用于为存储桶配置自定义域名。

#### 示例代码
**Objective-C**

[//]: # (.cssg-snippet-put-bucket-domain)
```objective-c
QCloudPutBucketDomainRequest *req = [QCloudPutBucketDomainRequest new];

// 存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
req.bucket = @"examplebucket-1250000000";

QCloudDomainConfiguration *config = [QCloudDomainConfiguration new];
QCloudDomainRule *rule = [QCloudDomainRule new];

// 源站状态，可选 QCloudDomainStatueEnabled、 QCloudDomainStatueDisabled
rule.status = QCloudDomainStatueEnabled;
// 域名信息
rule.name = @"www.baidu.com";

// 替换已存在的配置、有效值CNAME/TXT 填写则强制校验域名所有权之后，再下发配置
rule.replace = QCloudCOSDomainReplaceTypeTxt;
rule.type = QCloudCOSDomainTypeRest;

// 规则描述集合的数组
config.rules = @[rule];

// 域名配置的规则
req.domain  = config;

[req setFinishBlock:^(id outputObject, NSError *error) {
    // outputObject 包含所有的响应 http 头部
    NSDictionary* info = (NSDictionary *) outputObject;
    
}];
[[QCloudCOSXMLService defaultCOSXML]PutBucketDomain:req];
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/BucketDomain.m) 查看。

**Swift**

[//]: # (.cssg-snippet-put-bucket-domain)
```swift
let req = QCloudPutBucketDomainRequest.init();

// 存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
req.bucket = "examplebucket-1250000000";

let config = QCloudDomainConfiguration.init();
let rule = QCloudDomainRule.init();
// 开启状态，可选 .enabled, .disabled
rule.status = .enabled;
rule.name = "www.baidu.com";

// 替换已存在的配置、有效值CNAME/TXT 填写则强制校验域名所有权之后，再下发配置
rule.replace = .txt;
rule.type = .rest;

// 规则描述集合的数组
config.rules = [rule];

// 域名配置的规则
req.domain = config;
req.finishBlock = {(result,error) in
    if let result = result {
        // result 包含响应的 header 信息
    } else {
        print(error!);
    }
}
QCloudCOSXMLService.defaultCOSXML().putBucketDomain(req);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/BucketDomain.swift) 查看。

#### 返回错误码说明

该请求可能会发生的一些常见的特殊错误如下：

| 状态码                                 | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| HTTP 409 Conflict                      | 该域名记录已存在，且请求中没有设置强制覆盖。或者该域名记录不存在，且请求中设置了强制覆盖 |
| HTTP 451 Unavailable For Legal Reasons | 该域名是中国境内域名，并且没有备案                           |

## 查询自定义域名

#### 功能说明

GET Bucket domain 用于查询存储桶的自定义域名信息。

#### 示例代码
**Objective-C**

[//]: # (.cssg-snippet-get-bucket-domain)
```objective-c
QCloudGetBucketDomainRequest *getReq =  [QCloudGetBucketDomainRequest new];

// 存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
getReq.bucket = @"examplebucket-1250000000";

[getReq setFinishBlock:^(QCloudDomainConfiguration * _Nonnull result,
                         NSError * _Nonnull error) {
    // 规则描述集合的数组
    NSArray *rules = result.rules;
}];
[[QCloudCOSXMLService defaultCOSXML]GetBucketDomain:getReq];
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/BucketDomain.m) 查看。


**Swift**

[//]: # (.cssg-snippet-get-bucket-domain)
```swift
let req = QCloudGetBucketDomainRequest.init();

// 存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
req.bucket = "examplebucket-1250000000";

req.finishBlock = {(result,error) in
    if let result = result {
        // result 包含源站信息
    } else {
        print(error!);
    }
}
QCloudCOSXMLService.defaultCOSXML().getBucketDomain(req);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/BucketDomain.swift) 查看。


#### 返回参数说明

<table>
<thead>
<tr>
<th>参数名称</th>
<th>描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td nowrap="nowrap">x-cos-domain-txt-verification</td>
<td>域名校验信息，该字段是一个 MD5 校验值，原串格式为：<code>cos[Region][BucketName-APPID][BucketCreateTime]</code>，其中 Region 为存储桶所在地域，BucketCreateTime 为存储桶 GMT 创建时间</td>
<td>String</td>
</tr>
</tbody></table>

