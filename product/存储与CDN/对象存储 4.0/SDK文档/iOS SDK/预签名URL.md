
本文档重点提供关于如何通过带了预签名的 URL 来上传、下载或者进行其他操作（SDK 或者服务器端都可以生成一个带了预签名的 URL 来上传、下载或者进行其他操作使用）。

- 我们假设您已经按照 [快速入门](https://cloud.tencent.com/document/product/436/11280) 文档中的指引完成了 SDK 下载、安装和初始化的过程。
- 查询时建议使用 Command+F 搜索到想要查询的接口，然后看我们给出的接口简单说明，复制示例到您的工程中运行。
> ?如果需要了解接口的功能或者参数的意义，建议直接查看代码里的注释，Xcode 支持通过三指轻按、Force-touch 重按或者将鼠标停留在变量上，按 Control+Command+D 的方式查看它的释义。   

#### 步骤说明

1. 生成一个 QCloudGetPresignedURLRequest 实例。
2. 填入必要信息，如请求的 Bucket，Object， HTTPMethod 等。
3. 如果使用时会另外加入 HTTP 头部或者参数，生成带预签名的 URL 时候就要调用 QCloudGetPresignedURLRequest 中对应的方法加入。
4. 调用 QCloudCOSXMLService 中的 getPresignedURL 发出请求，并且在结果中获取带预签名的 URL。

#### QCloudGetPresignedURLRequest 参数说明

| 参数名称    | 描述                                                         | 类型      | 必填 |
| ----------- | ------------------------------------------------------------ | --------- | ---- |
| bucket      | 使用预签名请求的存储桶名，可在 [COS V5 控制台](https://console.cloud.tencent.com/cos5/bucket) 上面看到，格式为&lt;BucketName-APPID&gt; ，例如 examplebucket-1250000000                                    | NSString* | 是   |
| object      | 使用预签名请求的 Object。 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/text.txt 中，对象键为 doc1/text.txt。更详细的描述可以参考 [对象描述](https://cloud.tencent.com/document/product/436/13324) | NSString* | 是   |
| HTTPMethod  | 使用预签名 URL 的请求的 HTTP 方法。有效值（大小写敏感）为：@"GET"、@"PUT"、@"POST"、@"DELETE" | NSString* | 是   |
| contentType | 指定请求和响应的 HTTP body 内容编码类型        | NSString* | 否   |
| contentMD5  | 文件的 MD5 值        | NSString* | 否   |

>!如果需要设置使用预签名 URL 生成的请求中的头部，或者 URL 参数的话，那么需要通过以下的方法进行设置：

```objective-c
/**
 添加使用预签名请求的头部

 @param value HTTP header 的值
 @param requestHeader HTTP header的key
 */
- (void)setValue:(NSString * _Nullable)value forRequestHeader:(NSString * _Nullable)requestHeader;

/**
 添加使用预签名请求的 URL 参数

 @param value 参数的值
 @param requestParameter 参数的key
 */
- (void)setValue:(NSString * _Nullable)value forRequestParameter:(NSString *_Nullable)requestParameter;
```

#### 获取带预签名 URL 的示例

```objective-c
QCloudGetPresignedURLRequest* getPresignedURLRequest = [[QCloudGetPresignedURLRequest alloc] init];
getPresignedURLRequest.bucket = @“examplebucket-1250000000”;
getPresignedURLRequest.HTTPMethod = @"GET";
getPresignedURLRequest.object = @"text.txt";
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
