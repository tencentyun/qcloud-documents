在接口文档中，我们假设您已经完成了初始化的过程。接口文档重点在于列出详细的接口列表，并且举例如何使用。查询时建议 Command+F 搜索到想要查询的接口，然后看我们给出的接口简单说明，复制示例到您的工程中运行。    

> ?如果需要更多的功能，或者不明白返回的参数是什么意义，建议直接查看代码里的注释，可以三指轻按、Force-touch 重按或者将鼠标停留在变量上，按 Control+Command+D 查看它的释义。

## 常见操作的最佳实践

该小节中概述了最常见的一些操作的最佳实践，不过这些的前提都是完成了快速入门中指引的初始化工作。

### 上传文件

可以参考快速入门中的 [上传文件](https://cloud.tencent.com/document/product/436/11280#step---2-.E4.B8.8A.E4.BC.A0.E6.96.87.E4.BB.B6) 环节。

### 上传文件时的断点续传

对于大于1M 的文件，SDK 都会以分片上传的方式进行上传，即将文件切分成多个1M 大小的分块，然后并行地（最大并行数为4）进行上传。对于每个已经完成上传的分片，后台服务器都会将其保存起来，这是上传时候断点续传的基础。    

在分片上传的过程中，初始化分片上传完成、或者是主动取消上传的话，都会产生一个用于恢复上传的 resumeData，可以通过这个 resumetData 重新生成一个上传请求，再继续用这个上传请求上传即可接着继续上传，并且进度也会相应叠加。可以参照下面获取 ResumeData 的例子：

```objective-C
QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
//···设置一些上传的参数
put.initMultipleUploadFinishBlock = ^(QCloudInitiateMultipartUploadResult * multipleUploadInitResult, QCloudCOSXMLUploadObjectResumeData resumeData) {
	//在初始化分片上传完成以后会回调该block，在这里可以获取 resumeData，并且可以通过 resumeData 生成一个分片上传的请求
	QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
};

[[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];

//···在完成了初始化，并且上传没有完成前
NSError* error;
//这里是主动调用取消，并且产生 resumetData 的例子
resumeData = [put cancelByProductingResumeData:&error];
if (resumeData) {
QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
 }
 //生成的用于恢复上传的请求可以直接上传
 [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:request];

```

注意的是，按照分片上传的运行原理，只有当一个分片上传完了，那么后台服务器才会将该分片记录下来，并且叠加进度。并且以下几种情况无法进行断点续传，而是重新开始一次上传过程：

- 上传的文件小于1M，没有进行分片上传。
- 没有使用 QCloudCOSXMLUploadObjectRequest 类进行上传，而是直接使用简单上传接口。
- 取消生成 resumeData 时候初始化分片上传还没有完成（完成初始化上传的回调还没有调用）。

### 下载文件

可以参考快速入门中的 [下载文件](https://cloud.tencent.com/document/product/436/11280#3.-.E4.B8.8B.E8.BD.BD.E6.96.87.E4.BB.B6) 环节。

### 复制文件

#### 说明

先初始化一个 QCloudCOSXMLCopyObjectRequest 对象，然后调用 QCloudCOSTransferMangerService 的 CopyObject 方法即可。注意对于比较大的文件，将会使用分块复制的方式进行复制。这个过程对于用户是没有感知的。  

> !如果是跨域复制，这里使用的 transferManager 所在的 region 必须为目标桶所在的 region。

#### QCloudCOSXMLCopyObjectRequest 参数说明

| 参数名称          | 描述                                                         | 类型       | 必填 |
| ----------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket            | 要创建的存储桶名，您可以在 [COS 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，注意存储桶名只能由数字和小写字母组成，并且长度不能超过40个字符，否则会创建失败 | NSString * | 是   |
| sourceBucket |  复制的源文件所在 Bucket | NSString * | 是  |
| sourceObject         | 复制的源文件的对象名，key | NSString * | 是   |
| sourceAPPID        | 复制的源文件的 APPID                             | NSString * | 是   |
| sourceRegion  | 复制的源文件所在的区域                             | NSString * | 是   |
| metadataDirective  | 是否拷贝元数据，枚举值：Copy，Replaced，默认值 Copy。假如标记为 Copy，忽略 Header 中的用户元数据信息直接复制；假如标记为 Replaced，按 Header 信息修改元数据。当目标路径和原路径一致，即用户试图修改元数据时，必须为 Replaced                            | NSString * | 否   |
| storageClass  | 对象的存储级别，枚举值：STANDARD（QCloudCOSStorageStandard），STANDARD_IA（QCloudCOSStorageStandardIA）。默认值：STANDARD（QCloudCOSStorageStandard）                          | QCloudCOSStorageClass| 否   |


#### 示例

```objective-c
QCloudCOSXMLCopyObjectRequest* request = [[QCloudCOSXMLCopyObjectRequest alloc] init];
request.bucket = @"目的Bucket";
request.object = @"目的文件名";
request.sourceBucket = @"文件来源Bucket，需要是公有读或者在当前账号有权限";
request.sourceObject = @"来源的文件名";
request.sourceAPPID = @"来源的APPID";
request.sourceRegion= @"来源的园区";
[request setFinishBlock:^(QCloudCopyObjectResult* result, NSError* error) {
    //完成回调
    if (nil == error) {
      //成功
    }
}];
//注意如果是跨域复制，这里使用的transferManager所在的region必须为目标桶所在的region
[[QCloudCOSTransferMangerService defaultCOSTransferManager] CopyObject:request];
```

## Service 操作

### 列出所有 Bucket - Get Service

Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）。

#### 返回结果 QCloudListAllMyBucketsResult 参数说明

| 参数名称 | 描述               | 类型          |
| -------- | ------------------ | ------------- |
| owner    | 存储桶持有者的信息 | QCloudOwner * |
| buckets  | 所有的bucket信息   | NSArray<QCloudBucket*> *    |

#### 示例

```objective-c
QCloudGetServiceRequest* request = [[QCloudGetServiceRequest alloc] init];
[request setFinishBlock:^(QCloudListAllMyBucketsResult* result, NSError* error) {
//回调完成的处理
}];
[[QCloudCOSXMLService defaultCOSXML] GetService:request];
```

### 生成与使用带预签名的 URL

SDK 或者服务器端都可以生成一个带了预签名的 URL 来上传、下载或者进行其他操作使用。

#### 步骤说明

1. 生成一个 QCloudGetPresignedURLRequest 实例。
2. 填入必要信息，如请求的 Bucket, Object， HTTPMethod 等。
3. 如果使用时会另外加入 HTTP 头部或者参数，生成带预签名的 URL 时候就要调用QCloudGetPresignedURLRequest 中对应的方法加入。
4. 调用 QCloudCOSXMLService 中的 getPresignedURL 发出请求，并且在结果中获取带预签名的 URL。

#### QCloudGetPresignedURLRequest 参数说明

| 参数名称    | 描述                                                         | 类型      | 必填 |
| ----------- | ------------------------------------------------------------ | --------- | ---- |
| bucket      | 使用预签名请求的 Bucket                                      | NSString* | 是   |
| object      | 使用预签名请求的 Object。 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString* | 是   |
| HTTPMethod  | 使用预签名URL的请求的 HTTP 方法。有效值(大小写敏感)为:@"GET",@"PUT",@"POST",@"DELETE" | NSString* | 是   |
| contentType | 如果使用预签名 URL 的请求有该头部，那么通过这里设置          | NSString* | 否   |
| contentMD5  | 如果使用预签名 URL 的请求有该头部，那么通过这里设置          | NSString* | 否   |

**注意：** 如果需要设置使用预签名URL生成的请求中的头部，或者URL参数的话，那么需要通过以下的方法进行设置：    

```objective-c
/**
 添加使用预签名请求的头部

 @param value HTTP header的值
 @param requestHeader HTTP header的key
 */
- (void)setValue:(NSString * _Nullable)value forRequestHeader:(NSString * _Nullable)requestHeader;

/**
 添加使用预签名请求的URL参数

 @param value 参数的值
 @param requestParameter 参数的key
 */
- (void)setValue:(NSString * _Nullable)value forRequestParameter:(NSString *_Nullable)requestParameter;
```

#### 获取带预签名 URL 的示例

```objective-c
QCloudGetPresignedURLRequest* getPresignedURLRequest = [[QCloudGetPresignedURLRequest alloc] init];
getPresignedURLRequest.bucket = self.bucket;
getPresignedURLRequest.HTTPMethod = @"GET";
getPresignedURLRequest.object = @"testUploadWithPresignedURL";
[getPresignedURLRequest setFinishBlock:^(QCloudGetPresignedURLResult * _Nonnull result, NSError * _Nonnull error) {
if (nil == error) {
 NSString* presignedURL = result.presienedURL;
}
}
[[QCloudCOSXMLService defaultCOSXML] getPresignedURL:getPresignedURLRequest];

```

#### 使用带预签名 URL 的示例

这里演示一个使用带预签名 URL 进行下载的例子。

```objective-C
NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:[NSURL URLWithString:@"带预签名的URL"]];
request.HTTPMethod = @"GET";
request.HTTPBody = [@"文件内容" dataUsingEncoding:NSUTF8StringEncoding];
[[[NSURLSession sharedSession] downloadTaskWithRequest:request completionHandler:^(NSURL * _Nullable location, NSURLResponse * _Nullable response, NSError * _Nullable error) {
    NSInteger statusCode = [(NSHTTPURLResponse*)response statusCode];
}] resume];
```

## 存储桶操作

### 创建 bucket

#### 方法原型

在开始使用 COS 时，需要在指定的账号下先创建一个 Bucket 以便于对象的使用和管理. 并指定 Bucket 所属的地域.创建 Bucket 的用户默认成为 Bucket 的持有者.若创建 Bucket 时没有指定访问权限，则默认为私有读写（private）权限。具体步骤如下：    

1. 实例化 QCloudPutBucketRequest，填入需要的参数。
2. 调用 QCloudCOSXMLService 对象中的 PutBucket 方法发出请求。
3. 从回调的 finishBlock 中的 outputObject 获取具体内容。

#### QCloudPutBucketRequest 参数说明

| 参数名称          | 描述                                                         | 类型       | 必填 |
| ----------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket            | 要创建的存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，注意存储桶名只能由数字和小写字母组成，并且长度不能超过40个字符，否则会创建失败 | NSString * | 是   |
| accessControlList | 定义 Bucket 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | NSString * | 否   |
| grantRead         | 赋予被授权者读的权限。格式： id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"  其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID | NSString * | 否   |
| grantWrite        | 授予被授权者写的权限。格式同上。                             | NSString * | 否   |
| grantFullControl  | 授予被授权者读写权限。格式同上。                             | NSString * | 否   |

#### 示例

```objective-c
QCloudPutBucketRequest* request = [QCloudPutBucketRequest new];
request.bucket = @"bucketname-appid"; //additional actions after finishing
[request setFinishBlock:^(id outputObject, NSError* error) {

}];
[[QCloudCOSXMLService defaultCOSXML] PutBucket:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 列举存储桶内的内容

#### 方法原型

进行存储桶操作之前，我们需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudGetBucketRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudGetBucketRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的 GetBucket 方法发出请求。    
3. 从回调的 finishBlock 中的 QCloudListBucketResult 获取具体内容。   

#### QCloudGetBucketRequest 参数说明

| 参数名称     | 描述                                                         | 类型       | 必填 |
| ------------ | ------------------------------------------------------------ | ---------- | ---- |
| bucket       | 存储桶名，可在 [COS V5 控制台 ](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为 &lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |
| prefix       | 前缀匹配，用来规定返回的文件前缀地址                         | NSString * | 否   |
| delimiter    | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始。可以将其理解为结束的符号，例如如果想要结尾是 A 的结果，那么将delimiter设置为 A 即可。 | NSString * | 否   |
| encodingType | 规定返回值的编码方式，可选值：url                            | NSString * | 否   |
| marker       | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  | NSString * | 否   |
| maxKeys      | 单次返回的最大条目数量，默认1000                             | int        | 否   |

#### 示例

```objective-c
QCloudGetBucketRequest* request = [QCloudGetBucketRequest new];
request.bucket = @“testBucket-123456789”;
request.maxKeys = 1000;
[request setFinishBlock:^(QCloudListBucketResult * result, NSError*   error) {
//additional actions after finishing
}];
[[QCloudCOSXMLService defaultCOSXML] GetBucket:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 获取存储桶的 ACL（Access Control List）

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudGetBucketACLRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudGetBucketACLRequest，填入获取 ACL 的存储桶。    
2. 调用 QCloudCOSXMLService 对象中的 GetBucketACL 方法发出请求。    
3. 从回调的 finishBlock 中的 QCloudACLPolicy 获取具体内容。    

#### QCloudGetBucketACLRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |

#### 返回结果 QCloudACLPolicy 参数说明

| 参数名称 | 描述                               | 类型             |
| -------- | ---------------------------------- | ---------------- |
| owner    | 存储桶持有者的信息                 | QCloudACLOwner * |
| accessControlList     | 被授权者与权限的信息 | QCloudAccessControlList *        |

#### 示例

```objective-c
QCloudGetBucketACLRequest* getBucketACl   = [QCloudGetBucketACLRequest new];
getBucketACl.bucket = @"testbucket-123456789";
[getBucketACl setFinishBlock:^(QCloudACLPolicy * _Nonnull result, NSError * _Nonnull error) {
   //QCloudACLPolicy中包含了 Bucket 的 ACL 信息。
}];

[[QCloudCOSXMLService defaultCOSXML] GetBucketACL:getBucketACl];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404, 503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 设置存储桶的 ACL（Access Control List）

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudPutBucketACLRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudPutBucketACLRequest，填入需要设置的存储桶，然后根据设置值的权限类型分别填入不同的参数。    
2. 调用 QCloudCOSXMLService 对象中的 PutBucketACL 方法发出请求。    
3. 从回调的 finishBlock 中的获取设置是否成功，并做设置成功后的一些额外动作。   

#### QCloudPutBucketACLRequest 参数说明

| 参数名称          | 描述                                                         | 类型       | 必填 |
| ----------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket            | 存储桶名，可在[COSV5控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |
| accessControlList | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | NSString * | 否   |
| grantRead         | 赋予被授权者读的权限。格式： id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;"  <br>其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID | NSString * | 否   |
| grantWrite        | 授予被授权者写的权限。格式同上。                             | NSString * | 否   |
| grantFullControl  | 授予被授权者读写权限。格式同上。                             | NSString * | 否   |

#### 示例

```objective-c
QCloudPutBucketACLRequest* putACL = [QCloudPutBucketACLRequest new];
NSString* appID = @“您的 APPID”;
NSString *ownerIdentifier = [NSString stringWithFormat:@"qcs::cam::uin/%@:uin/%@", appID, appID];
NSString *grantString = [NSString stringWithFormat:@"id=\"%@\"",ownerIdentifier];
putACL.grantFullControl = grantString;
putACL.bucket = @“testBucket-123456789”;
[putACL setFinishBlock:^(id outputObject, NSError *error) {
//error occucs if error != nil
}];
[[QCloudCOSXMLService defaultCOSXML] PutBucketACL:putACL];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 获取存储桶的 CORS（跨域访问）设置

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudGetBucketCORSRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudGetBucketCORSRequest，填入需要获取 CORS 的存储桶。    
2. 调用 QCloudCOSXMLService 对象中的 GetBucketCORS 方法发出请求。    
3. 从回调的 finishBlock 中获取结果。结果封装在了 QCloudCORSConfiguration 对象中，该对象的 rules 属性是一个数组，数组里存放着一组 QCloudCORSRule，具体的 CORS 设置就封装在 QCloudCORSRule 对象里。   

#### QCloudGetBucketCORSRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |

#### 返回结果 QCloudCORSConfiguration 参数说明

| 参数名称 | 描述                                             | 类型                                |
| -------- | ------------------------------------------------ | ----------------------------------- |
| rules    | 放置 CORS 的数组, 数组内容为 QCloudCORSRule 实例 | NSArray&lt;CloudCORSRule`*`&gt; `*` |

#### QCloudCORSRule 参数说明

| 参数名称      | 描述                                                         | 类型                           |
| ------------- | ------------------------------------------------------------ | ------------------------------ |
| identifier    | 配置规则的 ID                                                | NSString *                     |
| allowedMethod | 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE       | NSArray&lt;NSString`*`&gt;`*`  |
| allowedOrigin | 允许的访问来源，支持通配符 * , 格式为：协议://域名[:端口]如：`http://www.qq.com` | NSString *                     |
| allowedHeader | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * | NSArray&lt;NSString`*`&gt; `*` |
| maxAgeSeconds | 设置 OPTIONS 请求得到结果的有效期                            | int                            |
| exposeHeader  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | NSString *                     |

#### 示例

```objective-c
QCloudGetBucketCORSRequest* corsReqeust = [QCloudGetBucketCORSRequest new];
corsReqeust.bucket = @"testBucket-123456789";
[corsReqeust setFinishBlock:^(QCloudCORSConfiguration * _Nonnull result, NSError * _Nonnull error) {
   //CORS设置封装在result中。
}];

[[QCloudCOSXMLService defaultCOSXML] GetBucketCORS:corsReqeust];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 设置存储桶的 CORS（跨域访问）

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudPutBucketCORSRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudPutBucketCORSRequest，设置存储桶，并且将需要的 CORS 装入 QCloudCORSRule 中，如果有多组 CORS 设置，可以将多个 QCloudCORSRule 放在一个 NSArray 里，然后将该数组填入 QCloudCORSConfiguration的rules 属性里，放在 request 中。    
2. 调用 QCloudCOSXMLService 对象中的 PutBucketCORS 方法发出请求。    
3. 从回调的 finishBlock 中的获取设置成功与否（error 是否为空），并且做一些设置后的额外动作。   

#### QCloudPutBucketCORSRequest 参数说明

| 参数名称          | 描述                                                         | 类型                      | 必填 |
| ----------------- | ------------------------------------------------------------ | ------------------------- | ---- |
| bucket            | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString *                | 是   |
| corsConfiguration | 封装了 CORS 的具体参数                                       | QCloudCORSConfiguration * | 是   |

#### QCloudCORSConfiguration 参数说明

| 参数名称 | 描述                                             | 类型                             |
| -------- | ------------------------------------------------ | -------------------------------- |
| rules    | 放置 CORS 的数组, 数组内容为 QCloudCORSRule 实例 | NSArray&lt;QCloudCORSRule`*` > * |

#### QCloudCORSRule 参数说明

| 参数名称      | 描述                                                         | 类型                         |
| ------------- | ------------------------------------------------------------ | ---------------------------- |
| identifier    | 配置规则的 ID                                                | NSString *                   |
| allowedMethod | 允许的 HTTP 操作，枚举值：GET、PUT、HEAD、POST、DELETE       | NSArray &lt;NSString`*`> *   |
| allowedOrigin | 允许的访问来源，支持通配符 * , 格式为：协议://域名[:端口]如：`http://www.qq.com` | NSString *                   |
| allowedHeader | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * | NSArray &lt;NSString `*` > * |
| maxAgeSeconds | 设置 OPTIONS 请求得到结果的有效期                            | int                          |
| exposeHeader  | 设置浏览器可以接收到的来自服务器端的自定义头部信息           | NSString *                   |

#### 示例

```objective-c
QCloudPutBucketCORSRequest* putCORS = [QCloudPutBucketCORSRequest new];
QCloudCORSConfiguration* cors = [QCloudCORSConfiguration new];

QCloudCORSRule* rule = [QCloudCORSRule new];
rule.identifier = @"sdk";
rule.allowedHeader = @[@"origin",@"host",@"accept",@"content-type",@"authorization"];
rule.exposeHeader = @"ETag";
rule.allowedMethod = @[@"GET",@"PUT",@"POST", @"DELETE", @"HEAD"];
rule.maxAgeSeconds = 3600;
rule.allowedOrigin = @"*";
cors.rules = @[rule];
putCORS.corsConfiguration = cors;
putCORS.bucket = @"testBucket-123456789";
[putCORS setFinishBlock:^(id outputObject, NSError *error) {
    if (!error) {
      //success
  }
}];
[[QCloudCOSXMLService defaultCOSXML] PutBucketCORS:putCORS];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 获取存储桶的地域信息 Get Bucket Location

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudGetBucketLocationRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudGetBucketLocationRequest，填入 Bucket 名。    
2. 调用 QCloudCOSXMLService 对象中的 GetBucketLocation 方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudGetBucketLocationRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |

#### 返回结果 QCloudBucketLocationConstraint 参数说明

| 参数名称           | 描述                 | 类型      |
| ------------------ | -------------------- | --------- |
| locationConstraint | 说明 Bucket 所在区域 | NSString* |

#### 示例

```objective-c
QCloudGetBucketLocationRequest* locationReq = [QCloudGetBucketLocationRequest new];
locationReq.bucket = @"testBucket-123456789";
 __block QCloudBucketLocationConstraint* location;
[locationReq setFinishBlock:^(QCloudBucketLocationConstraint * _Nonnull result, NSError * _Nonnull error) {
       location = result;
}];
[[QCloudCOSXMLService defaultCOSXML] GetBucketLocation:locationReq];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 删除存储桶 CORS 设置

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudDeleteBucketCORSRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudDeleteBucketCORSRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudDeleteBucketCORSRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |

#### 示例

```objective-c
QCloudDeleteBucketCORSRequest* deleteCORS = [QCloudDeleteBucketCORSRequest new];
deleteCORS.bucket = @"testBucket-123456789";
[deleteCORS setFinishBlock:^(id outputObject, NSError *error) {
   //success if error == nil
}];
[[QCloudCOSXMLService defaultCOSXML] DeleteBucketCORS:deleteCORS];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是[苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中[关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 查询 Bucket 中正在进行的分块上传 List Bucket Multipart Uploads

#### 方法原型

进行存储桶操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudListBucketMultipartUploadsRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudListBucketMultipartUploadsRequest，填入需要的参数，如返回结果的前缀、编码方式等。    
2. 调用 QCloudCOSXMLService 对象中的 ListBucketMultipartUploads 方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudListBucketMultipartUploadsRequest 参数说明

| 参数名称       | 描述                                                         | 类型       | 必填 |
| -------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket         | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |
| prefix         | 限定返回的 Object key 必须以 Prefix 作为前缀。注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix | NSString * | 否   |
| delimiter      | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始。可以将其理解为结束的符号，例如如果想要结尾是 A 的结果，那么将delimiter设置为 A 即可。 | NSString * | 否   |
| encodingType   | 规定返回值的编码方式，可选值：url                            | NSString * | 否   |
| keyMarker      | 列出条目从该 key 值开始                                      | NSString * | 否   |
| uploadIDMarker | 列出条目从该 UploadId 值开始                                 | int        | 否   |
| maxUploads     | 设置最大返回的  multipart 数量，合法值1到1000                | int        | 否   |

#### 返回结果 QCloudListMultipartUploadsResult 参数说明

| 参数名称     | 描述                                                         | 类型       |
| ------------ | ------------------------------------------------------------ | ---------- |
| bucket       | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * |
| prefix       | 限定返回的 Object key 必须以 Prefix 作为前缀。注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix | NSString * |
| delimiter    | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 | NSString * |
| encodingType | 规定返回值的编码方式，可选值：url                            | NSString * |
| keyMarker    | 列出条目从该 key 值开始                                      | NSString * |
| maxUploads   | 设置最大返回的 multipart 数量，合法值1到1000                 | int        |
| uploads      | 所有已经上传的分片信息                                       | NSArray*   |

#### 示例

```objecitve-c
QCloudListBucketMultipartUploadsRequest* uploads = [QCloudListBucketMultipartUploadsRequest new];
uploads.bucket = @"testBucket-123456789";
uploads.maxUploads = 100;
__block NSError* resulError;
__block QCloudListMultipartUploadsResult* multiPartUploadsResult;
[uploads setFinishBlock:^(QCloudListMultipartUploadsResult* result, NSError *error) {
    multiPartUploadsResult = result;
    localError = error;
}];
[[QCloudCOSXMLService defaultCOSXML] ListBucketMultipartUploads:uploads];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。返回错误码（封装在返回的error里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码由苹果公司定义，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 查询 Bucket 是否存在 Head Bucket

Head Bucket 请求可以确认该 Bucket 是否存在，是否有权限访问。Head 的权限与 Read 一致。当该 Bucket 存在时，返回200；当该 Bucket 无访问权限时，返回403；当该 Bucket 不存在时，返回404。    

#### QCloudHeadBucketRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString * | 是   |

#### 示例

```objective-c
 QCloudHeadBucketRequest* request = [QCloudHeadBucketRequest new];
 request.bucket = @"testBucket-123456789";
 [request setFinishBlock:^(id outputObject, NSError* error) {
     //设置完成回调。如果没有error，则可以正常访问bucket。如果有error，可以从error code和messasge中获取具体的失败原因。
 }];
 [[QCloudCOSXMLService defaultCOSXML] HeadBucket:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码由苹果公司定于，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### Put Bucket Lifecycle

COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集 (其中每个规则为 COS 定义一个操作)。
这些操作分为以下两种：

- 转换操作：定义对象转换为另一个存储类的时间。例如，您可以选择在对象创建30天后将其转换为 STANDARD_IA（IA，适用于不常访问）存储类别。
- 过期操作：指定 Object 的过期时间。COS 将会自动为用户删除过期的 Object。

Put Bucket Lifecycle 用于为 Bucket 创建一个新的生命周期配置。如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。

#### 参数说明

| 参数名称  | 描述                                                         | 类型                          | 必填 |
| --------- | ------------------------------------------------------------ | ----------------------------- | ---- |
| bucket    | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString*                     | 是   |
| lifeCycle | 生命周期配置                                                 | QCloudLifecycleConfiguration* | 是   |

#### QCloudLifecycleConfiguration 参数说明

| 参数名称 | 描述               | 类型                            | 必填 |
| -------- | ------------------ | ------------------------------- | ---- |
| rules    | 规则描述集合的数组 | NSArray<QCloudLifecycleRule*> * | 是   |

#### QCloudLifecycleRule 参数说明

| 参数名称                       | 描述                                              | 类型                                          | 必填 |
| ------------------------------ | ------------------------------------------------- | --------------------------------------------- | ---- |
| identifier                     | 用于唯一地标识规则，长度不能超过255 个字符        | NSString*                                     | 是   |
| filter                         | Filter 用于描述规则影响的 Object 集合             | QCloudLifecycleRuleFilter*                    |      |
| status                         | 指明规则是否启用，枚举值：Enabled，Disabled       | QCloudLifecycleStatue                         | 是   |
| abortIncompleteMultipartUpload | 设置允许分片上传保持运行的最长时间                | QCloudLifecycleAbortIncompleteMultipartUpload | 否   |
| transition                     | 规则转换属性，对象何时转换被转换为 Standard_IA 等 | QCloudLifecycleTransition*                    | 否   |
| expiration                     | 规则过期属性                                      | QCloudLifecycleExpiration*                    | 否   |
| noncurrentVersionExpiration    | 指明非当前版本对象何时过期                        | QCloudLifecycleExpiration*                    | 否   |
| noncurrentVersionTransition    | 指明非当前版本对象何时转换被转换为 STANDARD_IA 等 | QCloudNoncurrentVersionExpiration*            | 否   |

#### QCloudLifecycleTransition 参数说明

| 参数名称                       | 描述                                              | 类型                                          | 必填 |
| ------------------------------ | ------------------------------------------------- | --------------------------------------------- | ---- |
| days                    | 指明规则对应的动作在对象最后的修改日期过后多少天操作，在 Transition 里，该字段有效值是非负整数       | NSString* | 否   |
| transitionDate                         |  指明规则对应的动作在何时操作         | NSString *                   |   否   |
| storageClass                         | 对象的存储级别，枚举值：STANDARD（QCloudCOSStorageStandard），STANDARD_IA（QCloudCOSStorageStandardIA），ARCHIVE（QCloudCOSStorageARCHIVE）。默认值：STANDARD（QCloudCOSStorageStandard）       | QCloudCOSStorageClass           | 是   |

#### 示例

```objective-c
QCloudPutBucketLifecycleRequest* request = [QCloudPutBucketLifecycleRequest new];
request.bucket = @"填入bucket名";
__block QCloudLifecycleConfiguration* configuration = [[QCloudLifecycleConfiguration alloc] init];
QCloudLifecycleRule* rule = [[QCloudLifecycleRule alloc] init];
rule.identifier = @"identifier";
rule.status = QCloudLifecycleStatueEnabled;
QCloudLifecycleRuleFilter* filter = [[QCloudLifecycleRuleFilter alloc] init];
filter.prefix = @"0";
rule.filter = filter;

QCloudLifecycleTransition* transition = [[QCloudLifecycleTransition alloc] init];
transition.days = 100;
transition.storageClass = QCloudCOSStorageStandarIA;
rule.transition = transition;
request.lifeCycle = configuration;
request.lifeCycle.rules = @[rule];
[request setFinishBlock:^(id outputObject, NSError* error) {
   //设置完成回调
}];
[[QCloudCOSXMLService defaultCOSXML] PutBucketLifecycle:request];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### Get Bucket Lifecycle

#### 返回结果 QCloudLifecycleConfiguration 参数说明

与 Put Bucket Lifecycle 接口中的 QCloudLifecycleConfiguration 一致。

#### 示例

```objective-c
QCloudGetBucketLifecycleRequest* request = [QCloudGetBucketLifecycleRequest new];
request.bucket = @"testBucket-123456789";
[request setFinishBlock:^(QCloudLifecycleConfiguration* result,NSError* error) {
    //设置完成回调
}];
[[QCloudCOSXMLService defaultCOSXML] GetBucketLifecycle:request];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### Delete Bucket Lifecycle

#### 返回结果 QCloudLifecycleConfiguration 参数说明

与 Put Bucket Lifecycle 接口中的QCloudLifecycleConfiguration一致。

#### 示例

```objective-c
QCloudDeleteBucketLifeCycleRequest* request = [[QCloudDeleteBucketLifeCycleRequest alloc ] init];
request.bucket = @"testBucket-123456789";
 [request setFinishBlock:^(QCloudLifecycleConfiguration* result, NSError* error) {
 //设置完成回调
}];
 [[QCloudCOSXMLService defaultCOSXML] DeleteBucketLifeCycle:request];
```

### <span id="pbv">Put Bucket Versioning</span>   

Put Bucket Versioning 接口实现启用或者暂停存储桶的版本控制功能。请注意这是一个不可逆的接口，开启以后不可撤销。

#### QCloudPutBucketVersioningRequest 参数说明

| 参数名称      | 描述                                                         | 类型                                 | 必填 |
| ------------- | ------------------------------------------------------------ | ------------------------------------ | ---- |
| bucket        | 存储桶名，可在 [COS V5 控制台 ](https://console.cloud.tencent.com/cos5/bucket)上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString*                            | 是   |
| configuration | 版本控制的具体信息                                           | QCloudBucketVersioningConfiguration* | 是   |

#### QCloudBucketVersioningConfiguration 参数说明

| 参数名称 | 描述                                        | 类型                            | 必填 |
| -------- | ------------------------------------------- | ------------------------------- | ---- |
| status   | 说明版本是否开启，枚举值：Suspended\Enabled | QCloudCOSBucketVersioningStatus | 是   |

#### 示例

```objective-c
QCloudPutBucketVersioningRequest* request = [[QCloudPutBucketVersioningRequest alloc] init];
request.bucket = @"testBucket-123456789";
QCloudBucketVersioningConfiguration* configuration = [[QCloudBucketVersioningConfiguration alloc] init];
request.configuration = configuration;
configuration.status = QCloudCOSBucketVersioningStatusEnabled;
[request setFinishBlock:^(id outputObject, NSError* error) {
   //设置完成回调
 }];
 [[QCloudCOSXMLService defaultCOSXML] PutBucketVersioning:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### Get Bucket Versioning  

#### 返回结果 QCloudBucketVersioningConfiguration 参数说明

| 参数名称 | 描述                                        | 类型                            |
| -------- | ------------------------------------------- | ------------------------------- |
| status   | 说明版本是否开启，枚举值：Suspended\Enabled | QCloudCOSBucketVersioningStatus |

#### 示例

```objective-c
QCloudGetBucketVersioningRequest* request = [[QCloudGetBucketVersioningRequest alloc] init];
request.bucket = @"testBucket-123456789";
[request setFinishBlock:^(QCloudBucketVersioningConfiguration* result, NSError* error) {
   //设置完成回调
}];
[[QCloudCOSXMLService defaultCOSXML] GetBucketVersioning:request];
```

### Put Bucket Replication  

Put Bucket Replication 请求用于向开启版本管理的存储桶添加 replication 配置。如果存储桶已经拥有 replication 配置，那么该请求会替换现有配置。    

#### QCloudPutBucketReplicationRequest参数说明

| 参数名称     | 描述                                                         | 类型                                 | 必填 |
| ------------ | ------------------------------------------------------------ | ------------------------------------ | ---- |
| bucket       | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString*                            | 是   |
| configuation | 说明所有跨区域配置信息                                       | QCloudBucketReplicationConfiguation* | 是   |



> !使用该接口存储桶必须已经开启版本管理，版本管理详细请参见 [Put Bucket Versioning](#pbv)。



#### 返回结果  参数说明

#### 示例

```objective-c
QCloudPutBucketReplicationRequest* request = [[QCloudPutBucketReplicationRequest alloc] init];
request.bucket = @"source-bucket";
QCloudBucketReplicationConfiguation* configuration = [[QCloudBucketReplicationConfiguation alloc] init];
configuration.role = [NSString identifierStringWithID:@"uin" :@"uin"];
QCloudBucketReplicationRule* rule = [[QCloudBucketReplicationRule alloc] init];
rule.identifier = @"identifier";
rule.status = QCloudQCloudCOSXMLStatusEnabled;

QCloudBucketReplicationDestination* destination = [[QCloudBucketReplicationDestination alloc] init];
//qcs:id/0:cos:[region]:appid/[AppId]:[bucketname]
NSString* destinationBucket = @"destinationBucket";
NSString* region = @"destinationRegion"
destination.bucket = [NSString stringWithFormat:@"qcs:id/0:cos:%@:appid/%@:%@",@"region",@"appid",@"destinationBucket"];
rule.destination = destination;
configuration.rule = @[rule];
request.configuation = configuration;
[request setFinishBlock:^(id outputObject, NSError* error) {
     //设置完成回调
}];
 [[QCloudCOSXMLService defaultCOSXML] PutBucketRelication:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### Get Bucket Replication

Get Bucket Replication 接口请求实现读取存储桶中用户跨区域复制配置信息。

#### 返回结果 QCloudBucketReplicationConfiguation 参数说明

| 参数名称 | 描述                                                         | 类型                                    |
| -------- | ------------------------------------------------------------ | --------------------------------------- |
| role     | 发起者身份标识，格式为：qcs::cam::uin/<OwnerUin>:uin/<SubUin> | NSString*                               |
| rule     | 具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶 | NSArray<QCloudBucketReplicationRule*> * |

#### QCloudBucketReplicationRule 参数说明

| 参数名称    | 描述                                                     | 类型                                |
| ----------- | -------------------------------------------------------- | ----------------------------------- |
| status      | 标志 Rule 是否生效                                       | QCloudQCloudCOSXMLStatus            |
| identifier  | 用来标注具体 rule 的名称                                 | NSString*                           |
| prefix      | 前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空 | NSString*                           |
| destination | 目标存储桶信息                                           | QCloudBucketReplicationDestination* |

#### 示例

```objective-c
QCloudGetBucketReplicationRequest* request = [[QCloudGetBucketReplicationRequest alloc] init];
request.bucket = @"testBucket-123456789";
[request setFinishBlock:^(QCloudBucketReplicationConfiguation* result, NSError* error) {
    //设置完成回调
}];
[[QCloudCOSXMLService defaultCOSXML] GetBucketReplication:request];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### Delete Bucket Replication  

Delete Bucket Replication 接口请求实现删除存储桶中用户跨区域复制配置。

#### 参数说明

#### 返回结果  参数说明

#### 示例

```objective-c
QCloudDeleteBucketReplicationRequest* request = [[QCloudDeleteBucketReplicationRequest alloc] init];
request.bucket = @"testBucket-123456789";
[request setFinishBlock:^(id outputObject, NSError* error) {
   //设置完成回调
}];
[[QCloudCOSXMLService defaultCOSXML] DeleteBucketReplication:request];
```

## 文件操作

在 COS 中，每个文件就是一个 Object（对象）。对文件的操作，其实也就是对对象的操作。

### 简单上传 (Put Object)

简单上传仅限于小文件（20MB以下）。简单上传支持从内存中上传文件。

> !当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请在上传时不要设置，默认继承 Bucket 权限。

#### QCloudPutObjectRequest 参数说明

| 参数名称                      | 说明                                                         | 类型                  | 必填 |
| ----------------------------- | ------------------------------------------------------------ | --------------------- | ---- |
| Object                        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString *            | 是   |
| bucket                        | 存储桶名,可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ,例如 testBucket-1253653367 | NSString *            | 是   |
| body                          | 如果文件存放在硬盘中，这里是需要上传的文件的路径，填入NSURL * 类型变量。如果文件存放在内存中，则这里可以填入包含文件二进制数据的NSData * 类型变量 | BodyType              | 是   |
| storageClass                  | 对象的存储级别，枚举值：STANDARD(QCloudCOSStorageStandard)，STANDARD_IA(QCloudCOSStorageStandardIA)，ARCHIVE(QCloudCOSStorageARCHIVE)。默认值：STANDARD(QCloudCOSStorageStandard)                                            | QCloudCOSStorageClass | 否  |
| cacheControl                  | RFC 2616 中定义的缓存策略                                    | NSString *            | 否   |
| contentDisposition            | RFC 2616中定义的文件名称                                     | NSString *            | 否   |
| expect                        | 当使用expect=@"100-Continue"时，在收到服务端确认后才会发送请求内容 | NSString *            | 否   |
| expires                       | RFC 2616中定义的过期时间                                     | NSString *            | 否   |
| initMultipleUploadFinishBlock | 如果该 request 产生了分片上传的请求，那么在分片上传初始化完成后，会通过这个 block 来回调，可以在该回调 block 中获取分片完成后的 bucket， key， uploadID，以及用于后续上传失败后恢复上传的ResumeData。 | block                 | 否   |
| accessControlList             | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | NSString *            | 否   |
| grantRead                     | 赋予被授权者读的权限。格式： id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"  其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID | NSString *            | 否   |
| grantWrite                    | 授予被授权者写的权限。格式同上。                             | NSString *            | 否   |
| grantFullControl              | 授予被授权者读写权限。格式同上。                             | NSString *            | 否   |

#### 示例    

```objective-C
QCloudPutObjectRequest* put = [QCloudPutObjectRequest new];
put.object = @"object-name";
put.bucket = @"bucket-12345678";
put.body =  [@"testFileContent" dataUsingEncoding:NSUTF8StringEncoding];
[put setFinishBlock:^(id outputObject, NSError *error) {
   //完成回调
  if (nil == error) {
   //成功
   }
   }];
[[QCloudCOSXMLService defaultCOSXML] PutObject:put];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 查询对象的 ACL（Access Control List）

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudGetObjectACLRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudGetObjectACLRequest，填入存储桶的名称，和需要查询对象的名称。    
2. 调用 QCloudCOSXMLService 对象中的 GetObjectACL 方法发出请求。    
3. 从回调的 finishBlock 中的获取的 QCloudACLPolicy 对象中获取封装好的 ACL 的具体信息。   

#### QCloudGetObjectACLRequest 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket   | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |
| object   | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString * | 是   |

#### 示例

```objective-c
request.bucket = self.aclBucket;
request.object = @"对象的名称";
request.bucket = @"testBucket-123456789"
__block QCloudACLPolicy* policy;
[request setFinishBlock:^(QCloudACLPolicy * _Nonnull result, NSError * _Nonnull error) {
     policy = result;
}];
[[QCloudCOSXMLService defaultCOSXML] GetObjectACL:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 设置对象的 ACL（Access Control List）

当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

#### 方法原型

进行对象操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudPutObjectACLRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudPutObjectACLRequest，填入存储桶名，和一些额外需要的参数，如授权的具体信息等。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中获取设置的完成情况，若 error 为空，则设置成功。   

#### QCloudPutObjectACLRequest 参数说明

| 参数名称          | 描述                                                         | 类型       | 必填 |
| ----------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket            | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |
| object            | 对象名                                                       | NSString * | 是   |
| accessControlList | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | NSString * | 否   |
| grantRead         | 赋予被授权者读的权限。格式： id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" <br> 其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID | NSString * | 否   |
| grantWrite        | 授予被授权者写的权限。格式同上。                             | NSString * | 否   |
| grantFullControl  | 授予被授权者读写权限。格式同上。                             | NSString * | 否   |

#### 示例

```objective-c
QCloudPutObjectACLRequest* request = [QCloudPutObjectACLRequest new];
request.object = @"需要设置 ACL 的对象名";
request.bucket = @"testBucket-123456789";
NSString *ownerIdentifier = [NSString stringWithFormat:@"qcs::cam::uin/%@:uin/%@",self.appID, self.appID];
NSString *grantString = [NSString stringWithFormat:@"id=\"%@\"",ownerIdentifier];
request.grantFullControl = grantString;
__block NSError* localError;
[request setFinishBlock:^(id outputObject, NSError *error) {
     localError = error;
}];
[[QCloudCOSXMLService defaultCOSXML] PutObjectACL:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的error里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 下载文件

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### 参数说明

| 参数名称                   | 描述                                                         | 类型       | 必填 |
| -------------------------- | ------------------------------------------------------------ | ---------- | ---- |
| bucket                     | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |
| object                     | 对象名                                                       | NSString * | 是   |
| range                      | RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位     | NSString * | 否   |
| ifModifiedSince            | 如果文件修改时间晚于指定时间，才返回文件内容。否则返回 412 (not modified) | NSString * | 否   |
| responseContentType        | 设置响应头部中的 Content-Type 参数                           | NSString * | 否   |
| responseContentLanguage    | 设置响应头部中的 Content-Language 参数                       | NSString * | 否   |
| responseContentExpires     | 设置响应头部中的 Content-Expires 参数                        | NSString * | 否   |
| responseCacheControl       | 设置响应头部中的 Cache-Control 参数                          | NSString * | 否   |
| responseContentDisposition | 设置响应头部中的 Content-Disposition 参数。                  | NSString * | 否   |
| responseContentEncoding    | 设置响应头部中的 Content-Encoding 参数                       | NSString * | 否   |

#### 示例

```objective-c
QCloudGetObjectRequest* request = [QCloudGetObjectRequest new];
//设置下载的路径 URL，如果设置了，文件将会被下载到指定路径中.如果该参数没有设置，那么文件将会被下载至内存里，存放在在 finishBlock 的 	outputObject 里。
request.downloadingURL = [NSURL URLWithString:QCloudTempFilePathWithExtension(@"downding")];
request.object = @“您的 Object-Key”;
request.bucket = @"testBucket-123456789";
[request setFinishBlock:^(id outputObject, NSError *error) {
    //additional actions after finishing
}];
[request setDownProcessBlock:^(int64_t bytesDownload, int64_t totalBytesDownload, int64_t totalBytesExpectedToDownload) {
   //下载过程中的进度
}];
[[QCloudCOSXMLService defaultCOSXML] GetObject:request];
```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### Object 跨域访问配置的预请求

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudOptionsObjectRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudOptionsObjectRequest，填入需要设置的对象名、存储桶名、模拟跨域访问请求的 http 方法和模拟跨域访问允许的访问来源。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudOptionsObjectRequest 参数说明

| 参数名称                   | 描述                                                         | 类型                        | 必填 |
| -------------------------- | ------------------------------------------------------------ | --------------------------- | ---- |
| object                     | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString *                  | 是   |
| bucket                     | 存储桶名，可在 [COS V5 控制台 ](https://console.cloud.tencent.com/cos5/bucket)上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString *                  | 是   |
| accessControlRequestMethod | 模拟跨域访问的请求HTTP方法                                   | NSArray&lt;NSString`*`> *   | 是   |
| origin                     | 模拟跨域访问允许的访问来源，支持通配符 * , 格式为：协议://域名[:端口]如：`http://www.qq.com` | NSString *                  | 是   |
| allowedHeader              | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * | NSArray&lt;NSString `*` > * | 否   |

#### 示例

```objective-c
QCloudOptionsObjectRequest* request = [[QCloudOptionsObjectRequest alloc] init];
request.bucket =@"存储桶名";
request.origin = @"*";
request.accessControlRequestMethod = @"get";
request.accessControlRequestHeaders = @"host";
request.object = @"对象名";
__block id resultError;
[request setFinishBlock:^(id outputObject, NSError* error) {
     resultError = error;
 }];

[[QCloudCOSXMLService defaultCOSXML] OptionsObject:request];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。


### Object restore :恢复 Bucket中归档为 archive 类型的对象

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudPostObjectRestoreRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudPostObjectRestoreRequest，填入需要设置的对象名、存储桶名。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudPostObjectRestoreRequest 参数说明

| 参数名称                   | 描述                                                         | 类型                        | 必填 |
| -------------------------- | ------------------------------------------------------------ | --------------------------- | ---- |
| object                     | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString *                  | 是   |
| bucket                     | 存储桶名，可在 [COS V5 控制台 ](https://console.cloud.tencent.com/cos5/bucket)上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString *                  | 是   |
| restoreRequest | 模恢复数据的配置信息                                   | QCloudRestoreRequest *   | 是   |

#### QCloudRestoreRequest 参数说明

| 参数名称                   | 描述                                                         | 类型                        | 必填 |
| -------------------------- | ------------------------------------------------------------ | --------------------------- | ---- |
| days                     | 设置临时副本的过期时间 | int64_t                 | 是   |
| CASJobParameters                     | 复原的过程类型配置信息 |CASJobParameters *                | 是   |

#### CASJobParameters 参数说明

| 参数名称                   | 描述                                                         | 类型                        | 必填 |
| -------------------------- | ------------------------------------------------------------ | --------------------------- | ---- |
| tier                     | 恢复模式，支持的三种恢复模式，分别为 Standard（标准模式，恢复任务在35小时内完成）、Expedited（极速模式，恢复任务在15分钟内可完成）以及 Bulk（批量模式，恢复任务在5-12小时内完成） | QCloudCASTier                 | 是   |


#### 示例

```objective-c
	QCloudPostObjectRestoreRequest *req = [QCloudPostObjectRestoreRequest new];
 	req.bucket = @"bucket-appid";
 	req.object = @"objectName";
 	req.restoreRequest.days  = 10;
 	req.restoreRequest.CASJobParameters.tier =QCloudCASTierStandard;
 	[req setFinishBlock:^(id outputObject, NSError *error) {
 }];
 [[QCloudCOSXMLService defaultCOSXML] PostObjectRestore:req];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。


### 删除单个对象

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudDeleteObjectRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudDeleteObjectRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudDeleteObjectRequest 参数说明

| 参数名称 | 类型                                                         | 必填       | 描述 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| object   | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString * | 是   |
| bucket   | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |

#### 示例

```objective-c
QCloudDeleteObjectRequest* deleteObjectRequest = [QCloudDeleteObjectRequest new];
deleteObjectRequest.bucket = @"testBucket-123456789";
deleteObjectRequest.object = @"对象名";
__block NSError* resultError;
[deleteObjectRequest setFinishBlock:^(id outputObject, NSError *error) {
    resultError = error;
}];
[[QCloudCOSXMLService defaultCOSXML] DeleteObject:deleteObjectRequest];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的error里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 删除多个对象

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudDeleteMultipleObjectRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudDeleteMultipleObjectRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudDeleteMultipleObjectRequest 参数说明

| 参数名称      | 描述                                                         | 类型               | 必填 |
| ------------- | ------------------------------------------------------------ | ------------------ | ---- |
| object        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString *         | 是   |
| deleteObjects | 封装了需要批量删除的多个对象的信息                           | QCloudDeleteInfo * | 是   |

#### QCloudDeleteInfo参数说明

| 参数名称 | 描述                       | 类型                                      | 必填 |
| -------- | -------------------------- | ----------------------------------------- | ---- |
| objects  | 存放需要删除对象信息的数组 | NSArray&lt;QCloudDeleteObjectInfo `*` > * | 是   |

#### QCloudDeleteObjectInfo 参数说明

| 参数名称 | 描述                                                         | 类型       | 必填 |
| -------- | ------------------------------------------------------------ | ---------- | ---- |
| key      | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString * | 是   |

#### 示例

```objective-c
QCloudDeleteMultipleObjectRequest* delteRequest = [QCloudDeleteMultipleObjectRequest new];
delteRequest.bucket = @"testBucket-123456789";

QCloudDeleteObjectInfo* deletedObject0 = [QCloudDeleteObjectInfo new];
deletedObject0.key = @"第一个对象名";

QCloudDeleteObjectInfo* deleteObject1 = [QCloudDeleteObjectInfo new];
deleteObject1.key = @"第二个对象名";

QCloudDeleteInfo* deleteInfo = [QCloudDeleteInfo new];
deleteInfo.quiet = NO;
deleteInfo.objects = @[ deletedObject0,deleteObject2];
delteRequest.deleteObjects = deleteInfo;
__block NSError* resultError;
[delteRequest setFinishBlock:^(QCloudDeleteResult* outputObject, NSError *error) {
      localError = error;
      deleteResult = outputObject;
}];
[[QCloudCOSXMLService defaultCOSXML] DeleteMultipleObject:delteRequest];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的error里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。



### 初始化分片上传

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudInitiateMultipartUploadRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudInitiateMultipartUploadRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的 InitiateMultipartUpload 方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### 参数说明

| 参数名称           | 描述                                                         | 类型                  | 必填 |
| ------------------ | ------------------------------------------------------------ | --------------------- | ---- |
| Object             | 上传文件（对象）的文件名，也是对象的key。 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString *            | 是   |
| bucket             | 存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString *            | 是   |
| cacheControl       | RFC 2616中定义的缓存策略                                     | NSString *            | 否   |
| contentDisposition | RFC 2616中定义的文件名称                                     | NSString *            | 否   |
| expect             | 当使用 `expect=@"100-continue" `时，在收到服务端确认后才会发送请求内容 | NSString *            | 否   |
| expires            | RFC 2616 中定义的过期时间                                    | NSString *            | 否   |
| storageClass       | 对象的存储级别，枚举值：STANDARD(QCloudCOSStorageStandard)，STANDARD_IA(QCloudCOSStorageStandardIA)，ARCHIVE(QCloudCOSStorageARCHIVE)。默认值：STANDARD(QCloudCOSStorageStandard)                                               | QCloudCOSStorageClass | 否   |
| accessControlList  | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | NSString *            | 否   |
| grantRead          | 赋予被授权者读的权限。格式： id=" ",id=" "；<br>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;"  <br>其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID | NSString *            | 否   |
| grantWrite         | 授予被授权者写的权限。格式同上。                             | NSString *            | 否   |
| grantFullControl   | 授予被授权者读写权限。格式同上。                             | NSString *            | 否   |

#### 示例

```objective-c
QCloudInitiateMultipartUploadRequest* initrequest = [QCloudInitiateMultipartUploadRequest new];
initrequest.bucket = @"testBucket-123456789";
initrequest.object = @"对象名";
__block QCloudInitiateMultipartUploadResult* initResult;
[initrequest setFinishBlock:^(QCloudInitiateMultipartUploadResult* outputObject, NSError *error) {
    initResult = outputObject;
}];
[[QCloudCOSXMLService defaultCOSXML] InitiateMultipartUpload:initrequest];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的 error 里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

### 获取对象meta信息

#### 方法原型

进行文件操作之前，需要导入头文件 QCloudCOSXML/QCloudCOSXML.h。在此之前您需要完成前文中的 STEP-1 初始化操作。先生成一个 QCloudHeadObjectRequest 实例，然后填入一些需要的额外限制条件，通过并获得内容。具体步骤如下：    

1. 实例化 QCloudHeadObjectRequest，填入需要的参数。    
2. 调用 QCloudCOSXMLService 对象中的 HeadObject 方法发出请求。    
3. 从回调的 finishBlock 中的获取具体内容。   

#### QCloudHeadObjectRequest 参数说明

| 参数名称        | 描述                                                         | 类型       | 必填 |
| --------------- | ------------------------------------------------------------ | ---------- | ---- |
| Object          | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString * | 是   |
| bucket          | 存储桶名，可在 [COS V5 控制台 ](https://console.cloud.tencent.com/cos5/bucket)上面看到，格式为&lt;bucketName&gt;-&lt;APPID&gt; ，例如 testBucket-1253653367 | NSString * | 是   |
| ifModifiedSince | 如果文件修改时间晚于指定时间，才返回文件内容。否则返回 304 （not modified） | NSString * | 是   |

#### 示例

```objective-c
QCloudHeadObjectRequest* headerRequest = [QCloudHeadObjectRequest new];
headerRequest.object = @“对象名”;
headerRequest.bucket = @"testBucket-123456789";

   __block id resultError;
[headerRequest setFinishBlock:^(NSDictionary* result, NSError *error) {
      resultError = error;
}];
[[QCloudCOSXMLService defaultCOSXML] HeadObject:headerRequest];

```

#### 返回错误码说明

当 SDK 请求失败的时候，返回的 error 将不为空，并且包括了错误码、错误描述和其它一些调试必备的信息，以帮助开发者快速解决问题。

返回错误码（封装在返回的error里）主要包括两类：设备本身因为网络原因等返回的错误码，以及 COS 返回的错误码。

- 对于设备本身因为网络原因产生的错误码，都是负数并且是四位数，例如-1001，这类错误码是苹果定义的，可以参考 NSURLError.h 头文件内的定义，或者是 [苹果官方文档说明](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes)。
- 对于COS返回的错误码，是基于 HTTP 的状态码而来的，也就是404，503这类。对于这类错误码，可以参考 COS 官方文档中 [关于错误码的说明]( https://cloud.tencent.com/document/product/436/7730) 寻求解决方案。

## 加入自定义头部

如果有需要加入自定义头部的需求，可以使用自定义头部。支持加入自定义头部的类，都会有 customHeaders 这个属性：

```objective-c
@property (strong, nonatomic) NSMutableDictionary* customHeaders;
```

对于所有该属性内的键值对，都会以对应的形式加入到构建请求的 HTTP 头部中。

## 服务器加密

如果需要对上传的对象进行加密，我们支持以下加密方式

### 使用cos托管加密密钥的服务端加密（SSE-COS）保护数据

COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密.

iOS SDK 通过调用 -(void)setCOSServerSideEncyption 方法来完成。

```objective-c
[request setCOSServerSideEncyption];
```

### 使用客户提供的加密密钥的服务器端加密 （SSE-C）保护数据

iOS sdk 通过调用-(void)setCOSServerSideEncyptionWithCustomerKey:(NSString *)customerKey方法来完成。
  注意：

1. 该加密所运行的服务需要使用 HTTPS 请求，请参考“[开启 HTTPS 服务](#https)”这一小节。
2. customerKey：用户提供的密钥，传入一个32字节的字符串，支持数字、字母、字符的组合，不支持中文
3. 如果上传的源文件调用了该方法，那么在使用QCloudCOSXMLDownloadObjectRequest(下载)、QCloudHeadObjectRequest（查询）、QCloudCOSXMLUploadObjectReques（上传）、QCloudCOSXMLUploadObjectRequest（copy）对源对象操作的时候也要调用该方法。

```objective-c
NSString *customKey = @"123456qwertyuioplkjhgfdsazxcvbnm";
[put setCOSServerSideEncyptionWithCustomerKey:customKey];
```

## <span id="https">开启 HTTPS 服务</span>

iOS SDK支持 HTTPS 请求，只需要在初始化 QCloudServiceConfiguration 配置对象的时候，设置其 endpoint 的useHTTPS 为 YES 即可

```objective-c
QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
configuration.appID = kAppID;
configuration.signatureProvider = self;
QCloudCOSXMLEndPoint* endpoint = [[QCloudCOSXMLEndPoint alloc] init];
endpoint.regionName = kRegion;
endpoint.useHTTPS = YES;
configuration.endpoint = endpoint;
[QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
[QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];
}
```
