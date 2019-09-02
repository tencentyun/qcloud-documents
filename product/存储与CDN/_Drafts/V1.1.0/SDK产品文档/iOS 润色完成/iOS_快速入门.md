## 开发准备
### SDK 获取
对象存储服务的 iOS SDK 地址：[XML iOS SDK](https://github.com/tencentyun/qcloud-sdk-ios.git)    。
需要下载打包好的 Framework 格式的 SDK 可以从 realease 中选择需要的版本进行下载。

更多示例可参考 Demo：[ XML iOS  SDK Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples.git)    。

### 开发准备

-  SDK 支持 iOS 8.0 及以上版本的系统；
-  手机必须要有网络（GPRS、3G 或 Wifi 网络等）；
-  从 [COS v4 控制台](https://console.cloud.tencent.com/cos4/secret) 获取 APPID、SecretId、SecretKey。

> 关于文章中出现的 SecretID、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

### SDK 配置
#### SDK 导入
您可以通过 cocoapods 或者下载打包好的动态库的方式来集成 SDK。在这里我们推荐您使用 cocoapods 的方式来进行导入。
##### 使用Cocoapods导入(推荐)
在Podfile文件中使用：
```
pod 'QCloudCOSXML'
```

##### 使用打包好的动态库导入

将的 **QCloudCOSXML.framework和QCloudCore.framework** 拖入到工程中：
![](//mc.qcloudimg.com/static/img/7a26a0cdbfa897ca3270ecad402ae3b4/image.png)
并添加以下依赖库：

1. CoreTelephony
2. Foundation
3. SystemConfiguration
4. libstdc++.tbd

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。
![参数配置](http://ericcheung-1253653367.cosgz.myqcloud.com/WechatIMG24.jpeg)
腾讯云对象存储 XML iOS 的 SDK 使用的是 HTTP 协议。为了在 iOS 系统上可以运行，您需要开启允许通过 HTTP 传输。
您可以通过以下两种方式开启允许通过 HTTP 传输：
-  **手动设置方式：**在工程 info.plist 文件中添加 App Transport Security Settings 类型，然后在 App Transport Security Settings 下添加 Allow Arbitrary Loads 类型 Boolean，值设为YES。
- **代码设置方式：**您可以在集成 SDK 的 APP 的 info.plist 中需要添加如下代码：
```
<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSExceptionDomains</key>
		<dict>
			<key>myqcloud.com</key>
			<dict>
				<key>NSIncludesSubdomains</key>
				<true/>
				<key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
				<true/>
			</dict>
		</dict>
	</dict>
```

### 初始化

在使用 SDK 的功能之前，需要导入一些必要的头文件和进行一些初始化工作。

引入上传 SDK 的头文件：
```objective-c
QCloudCore.h,    
QCloudCOSXML/QCloudCOSXML.h
```    
 另外，使用 SDK 操作前，首先要实例化一个云服务配置对象 *QCloudServiceConfiguration*，其次需要实例化 *QCloudCOSXMLService* 和 *QCloudCOSTransferManagerService* 对象。

#### 方法原型
实例化 *QCloudServiceConfiguration* 对象：
```
 QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
 configuration.appID = @""//项目ID;
```
实例化 *QCloudCOSXMLService* 对象：
```
+ (QCloudCOSXMLService*) registerDefaultCOSXMLWithConfiguration:(QCloudServiceConfiguration*)configuration;
```
实例化 *QCloudCOSTransferManagerService* 对象：
```
+ (QCloudCOSTransferMangerService*) registerDefaultCOSTransferMangerWithConfiguration:(QCloudServiceConfiguration*)configuration;
```

#### QCloudServiceConfiguration 参数说明

| 参数名称   |  说明                 |类型         | 必填 |
| ------ | ---------- | ---- | --------------|
| appID  | 项目 ID，即 APP ID。         |NSString * | 是    |


#### 初始化示例

下面用到的 APPID， SecretId， SecretKey 等可以从 [COS v4 控制台](https://console.cloud.tencent.com/cos4/secret) 中获取。

```objective-c
//AppDelegate.m

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
     QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
     configuration.appID = @"*****";
     configuration.signatureProvider = self;
     QCloudCOSXMLEndPoint* endpoint = [[QCloudCOSXMLEndPoint alloc] init];
     endpoint.regionName = @"ap-beijing";//服务地域名称，可用的地域请参考注释
     configuration.endpoint = endpoint;

     [QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
     [QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];

}
```

## 快速入门

这里演示的上传和下载的基本流程，更多细节可以参考 [XML iOS  SDK Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples)。具体每一个接口如何使用请参照 Demo 中提供的单元测试文件。
>**注意：**在进行这一步之前必须在 [腾讯云控制台](https://console.cloud.tencent.com/cos4/secret) 上申请 COS 业务的 APPID。

### STEP - 1 初始化

#### 示例
**注意：** *QCloudServiceConfiguration* 的 *signatureProvider* 对象需要实现 *QCloudSignatureProvider* 协议。
```objective-c
//AppDelegate.m
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
	QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
	configuration.appID = @"*****";
	configuration.signatureProvider = self;
	QCloudCOSXMLEndPoint* endpoint = [[QCloudCOSXMLEndPoint alloc] init];
	endpoint.regionName = @"ap-beijing";//服务地域名称，可用的地域请参考注释
	configuration.endpoint = endpoint;

	[QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
	[QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];
}
```

#### 示例
```objective-c
//AppDelegate.m
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{
//实现签名的过程，我们推荐在服务器端实现签名的过程，具体请参考接下来的“生成签名”这一章。
}

```

### STEP - 2 上传文件

这里，假设您已经申请了自己业务 Bucket。事实上，SDK 所有的请求对应了相应的 Request 类，只要生成相应的请求，设置好相应的属性，然后将请求交给 QCloudCOSXMLService 对象，就可以完成相应的动作。其中，request 的 body 部分传入需要上传的文件在本地的 URL（NSURL* 类型）。    

上传文件的接口需要用到签名来进行身份认证，发错的请求会自动向初始化时指定的遵循 QCloudSignatureProvider 协议的对象去请求签名。签名如何生成可以参考下一章节中的生成签名。
>**注意：**URL 所对应的文件在上传过程中是不能进行变更的，否则会导致出错。

#### 示例

```objective-c
  QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];

    NSURL* url = /*文件的URL*/;
    put.object = @"文件名.jpg";
    put.bucket = /*bucket名*/;
    put.body =  url;
    [put setSendProcessBlock:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
        NSLog(@"upload %lld totalSend %lld aim %lld", bytesSent, totalBytesSent, totalBytesExpectedToSend);
    }];
    [put setFinishBlock:^(id outputObject, NSError* error) {

    }];
    [[QCloudCOSTransferMangerService defaultCOSTRANSFERMANGER] UploadObject:put];

```    

#### QCloudCOSXMLUploadObjectRequest 参数含义    

| 参数名称   |  说明                                |类型         | 必填 |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | 上传文件（对象）的文件名，也是对象的key          | NSString * | 是    |
|bucket|上传的存储桶的名称|NSString * |是|
|body|需要上传的文件的路径。填入NSURL * 类型变量|BodyType|是|
| storageClass |  对象的存储级别 |QCloudCOSStorageClass | 是    |
|cacheControl|RFC 2616 中定义的缓存策略|NSString *  |否|
|contentDisposition|RFC 2616中定义的文件名称|NSString * |否|
|expect|当使用expect=@"100-Continue"时，在收到服务端确认后才会发送请求内容|NSString * | 否 |
|expires| RFC 2616中定义的过期时间|NSString * |否 |
|initMultipleUploadFinishBlock| 如果该 request 产生了分片上传的请求，那么在分片上传初始化完成后，会通过这个 block 来回调，可以在该回调 block 中获取分片完成后的 bucket， key， uploadID，以及用于后续上传失败后恢复上传的ResumeData。|block|否|
|accessControlList|定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|NSString * |否|
|grantRead|赋予被授权者读的权限。格式： id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"，当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>"  其中 OwnerUin 指的是根账户的 ID，而 SubUin 指的是子账户的 ID|NSString * |否|
|grantWrite| 授予被授权者写的权限。格式同上。|NSString * |否|
|grantFullControl| 授予被授权者读写权限。格式同上。|NSString * |否|


### STEP - 3 下载文件

#### 示例

```objective-c
  QCloudGetObjectRequest* request = [QCloudGetObjectRequest new];
  //设置下载的路径 URL，如果设置了，文件将会被下载到指定路径中
  request.downloadingURL = [NSURL URLWithString:QCloudTempFilePathWithExtension(@"downding")];
  request.object = @“你的Object-Key”;
  request.bucket = @"你的bucket名";
  [request setFinishBlock:^(id outputObject, NSError \*error) {
    //additional actions after finishing
}];
	[request setDownProcessBlock:^(int64_t bytesDownload, int64_t totalBytesDownload, int64_t totalBytesExpectedToDownload) {
	 //下载过程中的进度
	}];
	[[QCloudCOSXMLService defaultCOSXML] GetObject:request];
```  

## 生成签名

SDK 中的请求需要用到签名，以确认访问的用户的身份，也保障了访问的安全性。当签名不正确时，大部分 COS 的服务将无法访问并且返回 403 错误。在 SDK 中可以生成签名，每个请求会向 QCloudServiceConfiguration 对象中的signatureProvider 对象来请求生成签名。我们可以将负责生成签名的对象在一开始赋值给 signatureProvider，该生成签名的对象需要遵循 QCloudSignatureProvider 协议，并实现生成签名的方法：
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields* )fileds    
                     request:(QCloudBizHTTPRequest* )request    
                  urlRequest:(NSURLRequest* )urlRequst    
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
```
### 最佳实践：接入CAM系统实现临时签名

虽然在本地提供了永久的 SecretId 和 SecretKey 来生成签名的接口，但请注意，将永久的 SecretId 和SecretKey 存储在本地是非常危险的行为，容易造成泄露引起不必要的损失。因此基于安全性的考虑，建议您在服务器端实现签名的过程。        

推荐您在自己的签名服务器内接入腾讯云的 CAM（Cloud Access Manager， 访问管理）来实现整个签名流程。     

![接入CAM签名部署图](http://ericcheung-1253653367.cosgz.myqcloud.com/Logical%20View.png)        
签名服务器接入 CAM 系统后，当客户端向签名服务器端请求签名时，签名服务器端会向 CAM 系统请求临时证书，然后返回给客户端。CAM 系统会根据您的永久 SecretId 和 SecretKey 来生成临时的 Secret ID, Secret Key 和临时Token 来生成签名，可以最大限度地提高安全性。

```objective-c
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{

		/*向签名服务器请求临时的 Secret ID,Secret Key,Token*/
    QCloudCredential* credential = [QCloudCredential new];
    credential.secretID = @"从 CAM 系统获取的临时 Secret ID";
    credential.secretKey = @"从 CAM 系统获取的临时 Secret Key";
		credential.token = @"从 CAM 系统返回的 Token，为会话 ID"
		credential.expiretionDate	 = /*签名过期时间*/
    QCloudAuthentationCreator* creator = [[QCloudAuthentationCreator alloc] initWithCredential:credential];
    QCloudSignature* signature =  [creator signatureForCOSXMLRequest:request];
    continueBlock(signature, nil);
}

```

### 在终端使用永久密钥生成签名（不推荐，有极大的泄密风险）
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSMutableURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{

    QCloudCredential* credential = [QCloudCredential new];
    credential.secretID = @"永久的SecretID";
    credential.secretKey = @"永久的SecretKey";
    QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
    QCloudSignature* signature =  [creator signatureForData:urlRequst];
    continueBlock(signature, nil);
}

```

### 使用脚手架工具管理异步签名过程
其实到这一步，您已经可以生成签名正常使用 SDK 里面的接口了。但为了方便您实现临时签名，从服务器端获取tempSecretKey 等临时签名需要的信息，我们提供了脚手架工具可供使用。您可以依照前面的代码来生成签名，也可以通过我们的脚手架工具 QCloudCredentailFenceQueue 来方便地获取临时签名。QCloudCredentailFenceQueue 提供了栅栏机制，也就是说您使用 QCloudCredentailFenceQueue 获取签名的话，所有需要获取签名的请求会等待签名完成后再执行，免去了自己管理异步过程。   
使用 QCloudCredentailFenceQueue，我们需要先生成一个实例。
```objective-c
//AppDelegate.m
//AppDelegate需遵循QCloudCredentailFenceQueueDelegate协议
//
- (BOOL)application:(UIApplication * )application didFinishLaunchingWithOptions:(NSDictionary * )launchOptions {
    // init step
    self.credentialFenceQueue = [QCloudCredentailFenceQueue new];
    self.credentialFenceQueue.delegate = self;
    return YES;
}
```   
然后调用 QCloudCredentailFenceQueue 的类需要遵循 QCloudCredentailFenceQueueDelegate 并实现协议内定义的方法：
```objective-c
- (void) fenceQueue:(QCloudCredentailFenceQueue * )queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
```
当通过 QCloudCredentailFenceQueue 去获取签名时，所有需要签名的 SDK 里的请求都会等待该协议定义的方法内拿到了签名所需的参数并生成有效的签名后执行。请看以下例子：
```objective-c
//AppDelegate.m
- (void) fenceQueue:(QCloudCredentailFenceQueue * )queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
{
   QCloudCredential* credential = [QCloudCredential new];
	 //在这里可以同步过程从服务器获取临时签名需要的secretID,secretKey,expiretionDate和token参数
   credential.secretID = @"****";
   credential.secretKey = @"****";
   credential.experationDate = [NSDate dateWithTimeIntervalSince1970:1504183628];
   credential.token = @"****";
   QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
   continueBlock(creator, nil);
}

```   
至此，就可以通过我们提供的脚手架工具来生成临时签名了。您也可以自己去实现具体的签名过程。
