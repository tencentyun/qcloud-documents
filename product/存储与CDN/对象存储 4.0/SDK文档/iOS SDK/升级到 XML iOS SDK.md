如果您细心对比过 JSON iOS SDK 和 XML SDK 的文档，您会发现并不是一个简单的增量更新。XML iOS SDK 不仅在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和传输性能上也做了非常大的改进。如果您想要升级到 XML iOS SDK，请参考下面的指引，一步步完成 SDK 的升级工作。

## 功能对比

下表列出了 JSON SDK 和 XML SDK 的主要功能对比：

| 功能       | XML SDK         | JSON SDK                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、二进制数据、分片上传<br>默认覆盖上传<br>智能判断上传模式<br>简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB） | 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传<br>简单上传最大支持20MB<br>分片上传最大支持64GB |
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不单独提供接口   | 创建目录<br>查询目录<br>删除目录 |

## 升级步骤
请按照下面5个步骤升级 iOS SDK。

**1. 更新 iOS SDK**
您可以通过 cocoapods 或下载打包好的动态库的方式来集成 SDK。在这里我们推荐您使用 cocoapods 的方式来进行导入。
- **使用 Cocoapods 导入（推荐）**  
在 Podfile 文件中使用：
```
  pod 'QCloudCOSXML'
```

- **使用打包好的动态库导入（手动集成方式）**  
您可以从 [realease](https://github.com/tencentyun/qcloud-sdk-ios/releases) 中选择需要的版本进行下载  
将 **QCloudCOSXML.framework, QCloudCore.framework 和 libmtasdk.a** 拖入到工程中，如下图所示：
![](https://main.qcloudimg.com/raw/14c8f5773ea19bc681b7f862dd6384fb.png)  

	并添加以下依赖库：
> - CoreTelephony
> - Foundation
> - SystemConfiguration
> - libc++.tbd

**工程配置**
完成上述步骤之后，在 Build Settings 中设置 Other Linker Flags，加入以下参数：
```shell
-ObjC
-all_load
```

如下图所示：
![参数配置](https://main.qcloudimg.com/raw/3bee5d2c3cb7e7f80b94c5f6bbe2ce5e.png)

**2. 更改 SDK 鉴权方式**

在 JSON SDK 中您需要自己在后台计算好签名，再返回客户端使用。而 XML SDK 使用了新的鉴权算法，我们强烈建议您后台接入我们的临时密钥（STS）方案。该方案您不需要了解签名计算过程，只需要在服务器端接入 CAM，将拿到的临时密钥返回到客户端，并设置到 SDK 中，SDK 会负责管理密钥和计算签名。临时密钥在一段时间后会自动失效，而永久密钥不会泄露。
您还可以按照不同的粒度来控制访问权限。具体的步骤请参考 [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068) 以及 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

如果您仍然采用后台手动计算签名，再返回客户端使用的方式，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档更新您签名的实现。

**3. 更改 SDK  初始化方式**

XML SDK 的初始化接口发生了一些变化：

- `QCloudCOSXMLService` 代替了 `COSClient`，但两者作用相同。同时增加了`QCloudServiceConfiguration`来配置更多的信息。
- 您需要在初始化时实例化一个密钥提供者 `QCloudAuthentationV5Creator`，用于提供一个有效的密钥，建议使用临时密钥。

**JSON SDK 的初始化方式如下：**

```
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:@“sh”];
```

**XML SDK 的初始化方式如下：**
>?示例代码中给出的是通过使用临时密钥的方式获取签名：强烈建议返回服务器时间作为签名的开始时间，用来避免由于用户手机本地时间偏差过大导致的签名不正确

```
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
   /*强烈建议返回服务器时间作为签名的开始时间，用来避免由于用户手机本地时间偏差过大导致的签名不正确 */
   credential.startDate = /*返回的服务器时间*/
   credential.expiretionDate	 = /*签名过期时间*/
   QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
   QCloudSignature* signature =  [creator signatureForData:urlRequst];
   continueBlock(signature, nil);

}

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


**4. 更改存储桶名称和可用区域简称**

XML SDK 的存储桶名称和可用区域简称与 JSON SDK 的不同，需要您进行相应的更改。


**存储桶 Bucket**
XML SDK 存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。例如 `exampleobject-1250000000`，其中 `exampleobject` 为用户自定义字符串，`1250000000` 为 APPID。

>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。您可通过 [腾讯云控制台](https://console.cloud.tencent.com/) 在【账号信息】查看 APPID。

在设置 Bucket 时，请参考下面的示例代码：
```
NSString *bucket = "exampleobject-1250000000";
```

**存储桶可用区域简称 Region**
XML SDK 的存储桶可用区域简称发生了变化，下表列出了不同区域在 JSON SDK 和 XML SDK 中的对应关系：

| 地域       | XML SDK 地域简称         | JSON SDK 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 香港       | ap-hongkong  | hk |
| 新加坡      | ap-singapore | sgp |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |

在初始化时，请将存储桶所在区域简称设置到 `QCloudServiceConfiguration`的 `regionName`中：

```
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

**5. 更改 API**

升级到 XML SDK之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。我们做了封装让 SDK 更加易用，具体请参考我们的示例和 [快速入门](https://cloud.tencent.com/document/product/436/11280) 文档。

API 变化有以下三点：

**1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身没有文件夹和目录的概念，对象存储不会因为上传对象 project/a.txt 而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为 project/，内容为空的对象，展示方式上模拟了传统文件夹。

例如：上传对象 project/doc/a.txt ，分隔符`/`会模拟「文件夹」的展示方式，于是可以看到控制台上出现「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含 a.txt 文件。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。

如果您的使用场景里面有文件夹的概念，需要提供创建文件夹的功能，您可以上传一个路径以 '/' 结尾的 0KB 文件。这样在您调用 `GetBucket` 接口时，就可以将这样的文件当做文件夹。


**2）QCloudCOSTransferMangerService**

在 XML SDK 中，我们封装了可以智能判断是简单上传（复制）还是分片上传（复制）的操作，命名为 `QCloudCOSTransferMangerService`，同时对 API 设计和传输性能都做了优化，建议您直接使用。`QCloudCOSTransferMangerService`的主要特性有：

* 支持断点上传。
* 支持根据文件大小智能选择简单上传（复制）还是分片上传（复制）。

使用 `QCloudCOSTransferMangerService`上传的示例代码：

```
  QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
  NSURL* url = /*文件的URL*/;
  put.object = @"文件名.jpg";
  put.bucket = @"exampleobject-1250000000";
  put.body =  url;
  [put setSendProcessBlock:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
      NSLog(@"upload %lld totalSend %lld aim %lld", bytesSent, totalBytesSent, totalBytesExpectedToSend);
  }];
  [put setFinishBlock:^(id outputObject, NSError* error) {

  }];
  [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];

```
使用 `QCloudCOSTransferMangerService`上传文件时断点续传示例代码：

```
QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
  //•••设置一些上传的参数
  put.initMultipleUploadFinishBlock = ^(QCloudInitiateMultipartUploadResult * multipleUploadInitResult, QCloudCOSXMLUploadObjectResumeData resumeData) {
	//在初始化分片上传完成以后会回调该block，在这里可以获取 resumeData，并且可以通过 resumeData 生成一个分片上传的请求
	 QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
  };

  [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];
  //•••在完成了初始化，并且上传没有完成前
  NSError* error;
  //这里是主动调用取消，并且产生 resumetData 的例子
  resumeData = [put cancelByProductingResumeData:&error];
  if (resumeData) {
    QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
  }
  //生成的用于恢复上传的请求可以直接上传
  [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:request];

```
>!按照分片上传的运行原理，只有当一个分片上传完了，那么后台服务器才会将该分片记录下来，并且叠加进度。并且以下几种情况无法进行断点续传，而是重新开始一次上传过程：
 - 上传的文件小于1M，没有进行分片上传。
 - 没有使用 QCloudCOSXMLUploadObjectRequest 类进行上传，而是直接使用简单上传接口。
 - 取消生成 resumeData 时候初始化分片上传还没有完成（完成初始化上传的回调还没有调用）。

**3）新增 API**

XML SDK 增加了很多新的 API，您可根据需求进行调用。包括：
* 存储桶的操作，如 QCloudPutBucketRequest、QCloudGetBucketRequest、QCloudListBucketRequest 等。
* 存储桶 ACL 的操作，如 QCloudPutBucketACLRequest、QCloudGetBucketACLRequest 等。
* 存储桶生命周期的操作，如 PQCloudutBucketLifecycleRequest、QCloudGetBucketLifecycleRequest 等。

具体请参考我们的 [iOS SDK 快速入门](https://cloud.tencent.com/document/product/436/11280)。
