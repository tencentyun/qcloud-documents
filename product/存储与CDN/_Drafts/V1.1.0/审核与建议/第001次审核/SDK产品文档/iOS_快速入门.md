## 开发准备

### SDK 获取

对象存储服务的 iOS SDK 地址：[iOS SDK](https://github.com/tencentyun/qcloud-sdk-ios.git)    
需要下载打包好的Framework格式的SDK可以从realease中选择需要的版本进行下载。

更多示例可参考Demo：[iOS Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples.git)    
（本版本SDK基于XML API封装组成）

### 开发准备

-  iOS 8.0+；
-  手机必须要有网络（GPRS、3G或Wifi网络等）；


### SDK 配置

#### SDK 导入
您可以通过cocoapods或者下载打包好的动态库的方式来集成SDK。在这里我们推荐您使用cocoapods的方式来进行导入。
##### 使用Cocoapods导入(推荐)

在Podfile文件中使用：

~~~
pod 'QCloudCOSXML'
~~~

##### 使用打包好的动态库导入

将我们提供的**QCloudCOSXML.framework和QCloudCore.framework**拖入到工程中：

![](http://ericcheung-1253653367.cosgz.myqcloud.com/%E4%B8%A4%E4%B8%AAframework%E6%88%AA%E5%9B%BE.png)

并添加以下依赖库：

1. CoreTelephony
2. Foundation
3. SystemConfiguration
4. libstdc++.tbd

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。

![参数配置](http://ericcheung-1253653367.cosgz.myqcloud.com/WechatIMG24.jpeg)

我们的SDK使用的是HTTP协议。为了在iOS系统上可以运行，您需要开启允许通过HTTP传输。具体操作步骤是在工程info.plist文件中添加App Transport Security Settings 类型，然后在App Transport Security Settings下添加Allow Arbitrary Loads 类型Boolean,值设为YES。或者您可以在集成SDK的APP的info.plist中需要添加如下代码：
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

在使用SDK的功能之前，我们需要导入一些必要的头文件和进行一些初始化工作。


> <font size=4 color=red> 引入头文件用代码格式？</font>
> by stongdong


引入上传 SDK 的头文件 *QCloudCore.h,    
QCloudCOSXML/QCloudCOSXML.h*，    
 使用 SDK 操作时，需要先实例化 *QCloudCOSXMLService* 和 *QCloudCOSTransferManagerService* 对象。实例化这两个对象之前我们要实例化一个云服务配置对象*QCloudServiceConfiguration*。

#### 方法原型
```
 QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
 configuration.appID = @""//项目ID;
```

```
+ (QCloudCOSXMLService*) registerDefaultCOSXMLWithConfiguration:(QCloudServiceConfiguration*)configuration;
```

```
+ (QCloudCOSTransferMangerService*) registerDefaultCOSTransferMangerWithConfiguration:(QCloudServiceConfiguration*)configuration;
```

#### QCloudServiceConfiguration参数说明

| 参数名称   | 类型         | 是否必填 | 说明                                       |
| ------ | ---------- | ---- | ---------------------------------------- |
| appID  | NSString * | 是    | 项目ID，即APP ID。                            |


#### 初始化示例

> <font size=4 color=red> 关键的数据appid region secretId 和 secretKey从哪里获取，要写出来，并给出链接</font>
> by stongdong


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

这里演示的上传和下载的基本流程，更多细节可以参考demo；在进行这一步之前必须在腾讯云控制台上申请COS业务的appid；

> <font size=4 color=red>  把Demo的地址附上来，可以引导用户去demo里面查看</font>
> by stongdong


### STEP - 1 初始化

#### 示例

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

需要注意的是QCloudServiceConfiguration的signatureProvider对象需要实现QCloudSignatureProvider协议。
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

在这里我们假设您已经申请了自己业务bucket。事实上，SDK所有的请求对应了相应的Request类，只要生成相应的请求，设置好相应的属性，然后将请求交给QCloudCOSXMLService对象，就可以完成相应的动作。其中，request的body部分传入需要上传的文件在本地的URL（NSURL* 类型）。    

上传文件的接口需要用到签名来进行身份认证，我们的请求会自动向初始化时指定的遵循QCloudSignatureProvider协议的对象去请求签名。签名如何生成可以参考下一章节中的生成签名。

需要留意的是，URL所对应的文件在上传过程中是不能进行变更的，否则会导致出错。


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

#### QCloudCOSXMLUploadObjectRequest参数含义    

| 参数名称   | 类型         | 是否必填 | 说明                                |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | NSString * | 是    | 上传文件（对象）的文件名，也是对象的key          |
|bucket|NSString * |是|上传的存储桶的名称|
|body|BodyType|是|需要上传的文件的路径。填入NSURL * 类型变量|
| storageClass | QCloudCOSStorageClass | 是    |  对象的存储级别 |
|cacheControl|NSString * |否|RFC 2616中定义的缓存策略|
|contentDisposition|NSString *|否|RFC 2616中定义的文件名称|
|expect|NSString * | 否 |当使用expect=@"100-Continue"时，在收到服务端确认后才会发送请求内容|
|expires| NSString * |否 | RFC 2616中定义的过期时间|
|initMultipleUploadFinishBlock|block|否| 如果该request产生了分片上传的请求，那么在分片上传初始化完成后，会通过这个block来回调，可以在该回调block中获取分片完成后的bucket, key, uploadID,以及用于后续上传失败后恢复上传的ResumeData。|
|accessControlList|NSString * |否| 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private|
|grantRead|NSString * |否|赋予被授权者读的权限。格式： id=" ",id=" "；当需要给子账户授权时，id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"，当需要给根账户授权时，id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"  其中OwnerUin指的是根账户的ID，而SubUin指的是子账户的ID|
|grantWrite|NSString * |否| 授予被授权者写的权限。格式同上。|
|grantFullControl|NSString * |否| 授予被授权者读写权限。格式同上。|


### STEP - 3 下载文件

#### 示例

```objective-c
  QCloudGetObjectRequest* request = [QCloudGetObjectRequest new];
  //设置下载的路径URL，如果设置了，文件将会被下载到指定路径中
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

SDK中的请求需要用到签名，以确访问的用户的身份，也保障了访问的安全性。当签名不正确时，大部分COS的服务将无法访问并且返回403错误。在SDK中可以生成签名，每个请求会向QCloudServiceConfiguration对象中的signatureProvider对象来请求生成签名。我们可以将负责生成签名的对象在一开始赋值给signatureProvider，该生成签名的对象需要遵循QCloudSignatureProvider协议，并实现生成签名的方法：
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields* )fileds    
                     request:(QCloudBizHTTPRequest* )request    
                  urlRequest:(NSURLRequest* )urlRequst    
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
```
虽然我们提供在本地提供了永久的Secret ID 和Secret Key来生成签名的接口，但请注意，将永久的Secret ID 和Secret Key存储在本地是非常危险的行为，容易造成泄露引起不必要的损失。因此基于安全性的考虑，我们建议您在服务器端实现签名的过程。    

我们推荐您在自己的签名服务器内接入腾讯云的CAM（Cloud Access Manager， 访问管理）来实现整个签名流程。    

![接入CAM签名部署图](http://ericcheung-1253653367.cosgz.myqcloud.com/Logical%20View.png)        

签名服务器接入CAM系统后，当客户端去向签名服务器端请求签名时，签名服务器端会去向CAM系统请求临时证书，然后返回给客户端。CAM系统会根据您的永久Secret ID 和 Secret Key 来生成临时的 Secret ID, Secret Key 和临时Token来生成签名，可以最大限度地提高安全性。

```objective-c
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{

		/*向签名服务器请求临时的secretID,secretKey,token*/
    QCloudCredential* credential = [QCloudCredential new];
    credential.secretID = @"从CAM系统获取的临时Secret ID";
    credential.secretKey = @"从CAM系统获取的临时Secret Key";
		credential.token = @"从CAM系统返回的token，为会话ID"
		credential.expiretionDate	 = /*签名过期时间*/
    QCloudAuthentationCreator* creator = [[QCloudAuthentationCreator alloc] initWithCredential:credential];
    QCloudSignature* signature =  [creator signatureForCOSXMLRequest:request];
    continueBlock(signature, nil);
}

```

其实到这一步，您已经可以生成签名正常使用SDK里面的接口。但为了方便您实现临时签名，从服务器端获取tempSecretKey等临时签名需要的信息，我们提供了脚手架工具可供使用。您可以依照前面的代码来生成签名，也可以通过我们的脚手架工具QCloudCredentailFenceQueue来方便地获取临时签名。QCloudCredentailFenceQueue提供了栅栏机制，也就是说您使用QCloudCredentailFenceQueue去获取签名的话，所有需要获取签名的请求会等待签名完成后再执行，免去了自己管理异步过程的烦恼。   
使用QCloudCredentailFenceQueue，我们需要先生成一个实例。
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
然后调用QCloudCredentailFenceQueue的类需要遵循QCloudCredentailFenceQueueDelegate并实现协议内定义的方法：
```objective-c
- (void) fenceQueue:(QCloudCredentailFenceQueue * )queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
```
当通过QCloudCredentailFenceQueue去获取签名时，所有需要签名的SDK里的请求都会等待该协议定义的方法内拿到了签名所需的参数并生成有效的签名后执行。请看以下例子
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
