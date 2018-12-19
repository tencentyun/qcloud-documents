## Preparations for Development
### Obtaining SDK
Download iOS SDK resources of COS service from: [XML iOS SDK](https://github.com/tencentyun/qcloud-sdk-ios.git)
You can download the SDK in the packaged Framework format by selecting the desired version from Release.

For more examples, see Demo: [ XML iOS  SDK Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples.git). <**ECI**>

### Preparations for development
-  SDK supports iOS 8.0 or above.
-  Your mobile phone must be connected to a network (GPRS, 3G, Wi-Fi, etc.);
-   Obtain the APPID, SecretId, and SecretKey from the [COS V5 Console](https://console.cloud.tencent.com/cos5).

>  For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

### Configuring SDK
#### Importing SDK
You can integrate SDK via Cocoapods or by downloading packaged dynamic libraries. We recommend using Cocoapods for import.
-  **Importing using Cocoapods (recommended)**
In Podfile, use:
```
pod 'QCloudCOSXML'
```

-  **Importing using the packaged dynamic library (manual integration)**
Drag **QCloudCOSXML.framework and QCloudCore.framework** to your project:
![](http://mc.qcloudimg.com/static/img/7a26a0cdbfa897ca3270ecad402ae3b4/image.png)    
And add the following dependent libraries:
> 1. CoreTelephony
> 2. Foundation
> 3. SystemConfiguration
> 4. libstdc++.tbd

#### Configuring project
Set up "Other Linker Flags" in "Build Settings" and add the parameter:
```
-ObjC
-all_load
```
![Parameter Configuration](http://ericcheung-1253653367.cosgz.myqcloud.com/Screen%20Shot%202017-12-25%20at%206.32.20%20PM.png)
> **Note:**
Tencent Cloud COS XML iOS SDK uses HTTP protocol. To run the SDK on iOS, enable transfer over HTTP.
You can enable transfer over HTTP in the following two ways:
-  **Configuring manually**
Add "App Transport Security Settings" to the "info.plist" file of the project, and then add the "Allow Arbitrary Loads" as "Boolean" in "App Transport Security Settings", and set its value to "YES".
- **Configuring via code**
You can add the following code in the info.plist of the App integrating SDK:
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

### Initialization
Before using the features of SDK, import some necessary header files and perform initialization.
Import and upload the header files for SDK:
```objective-c
QCloudCore.h,    
QCloudCOSXML/QCloudCOSXML.h
```    
In addition, before using SDK, instantiate a cloud service configuration object QCloudServiceConfiguration, and then instantiate QCloudCOSXMLService and QCloudCOSTransferManagerService objects.

#### Method Prototype
Instantiate QCloudServiceConfiguration object:
```
 QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
 configuration.appID = @""//Project ID.
```
Instantiate QCloudCOSXMLService object:
```
+ (QCloudCOSXMLService*) registerDefaultCOSXMLWithConfiguration:(QCloudServiceConfiguration*)configuration;
```
Instantiate QCloudCOSTransferManagerService object:
```
+ (QCloudCOSTransferMangerService*) registerDefaultCOSTransferMangerWithConfiguration:(QCloudServiceConfiguration*)configuration;
```

#### QCloudServiceConfiguration parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | --------------|
| appID  | Project ID, i.e. APPID. | NSString * | Yes |

#### Example of initialization
The APPID, SecretId and SecretKey in the example below can be obtained from [COS V5 Console](https://console.cloud.tencent.com/cos5).
```objective-c
//AppDelegate.m

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
     QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
     configuration.appID = @"*****";
     configuration.signatureProvider = self;
     QCloudCOSXMLEndPoint* endpoint = [[QCloudCOSXMLEndPoint alloc] init];
     endpoint.regionName = @"ap-beijing";//Service region name. See the notes for available regions.
     configuration.endpoint = endpoint;

     [QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
     [QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];

}
```

## Getting Started
The examples below show the basic process of upload and download. For more information, please see [XML iOS SDK Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples). For more information on how to use each API, please see the unit test files provided in Demo.
>**Notes:**
>You must apply for the APPID of COS service on the [Tencent Cloud Console](https://console.cloud.tencent.com/cos4/secret) before proceeding with this step.

### 1. Initialization
**Note:** QCloudSignatureProvider protocol needs to be implemented for the signatureProvider object of QCloudServiceConfiguration.
#### Step 1:
```objective-c
//AppDelegate.m
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
	QCloudServiceConfiguration* configuration = [QCloudServiceConfiguration new];
	configuration.appID = @"*****";
	configuration.signatureProvider = self;
	QCloudCOSXMLEndPoint* endpoint = [[QCloudCOSXMLEndPoint alloc] init];
	endpoint.regionName = @"ap-beijing";//Service region name. See the notes for available regions.
	configuration.endpoint = endpoint;

	[QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
	[QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];
}
```

#### Step 2:
```objective-c
//AppDelegate.m
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{
//The process of implementing signature. We recommend implementing this process on the server. For more information, please see the "Generating Signature" section below.
}
```

### 2. Uploading files
The example assumes you have applied for a Bucket for your business. In fact, all SDK requests have their Request classes. When a request is generated and the relevant attributes are set, pass the request to the QCloudCOSXMLService object to complete the desired operation. For the body part of the request, enter the local URL of the file to be uploaded (NSURL\* type).    

The API for uploading files uses a signature for authentication. For a request that is sent by mistake, a signature is requested from the object specified during initialization that follows the QCloudSignatureProvider protocol. For more information on how to generate a signature, please see the [Generating Signature](#.E7.94.9F.E6.88.90.E7.AD.BE.E5.90.8D) section below.
>**Notes:**
>The file to which the URL points cannot be changed during upload, otherwise it will cause an error.

#### Example
```objective-c
  QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];

    NSURL* url = /*URL of file*/;
    put.object = @"filename.jpg";
    put.bucket = @"test-123456789";
    put.body =  url;
    [put setSendProcessBlock:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
        NSLog(@"upload %lld totalSend %lld aim %lld", bytesSent, totalBytesSent, totalBytesExpectedToSend);
    }];
    [put setFinishBlock:^(id outputObject, NSError* error) {

    }];
    [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];
```    

#### QCloudCOSXMLUploadObjectRequest parameters    

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)         | NSString * | Yes    |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|body|The path of the file to be uploaded. Enter a variable of NSURL * type |BodyType|Yes |
| storageClass | Storage class of object |QCloudCOSStorageClass | Yes    |
|cacheControl|Cache policy defined in RFC 2616 |NSString *  |No |
|contentDisposition|File name defined in RFC 2616 |NSString * |No |
|expect|When expect=@"100-Continue" is used, the request content will not be sent until the receipt of response from server. |NSString * | No |
|expires| Expiration time defined in RFC 2616 |NSString * |No |
|initMultipleUploadFinishBlock| If the request generates a multipart upload request, after the initialization of multipart upload, a callback is performed via the block. The bucket, key, and uploadID after the completion of multipart upload, and ResumeData for resuming subsequent failed upload can be obtained from this callback block. | block| No |
|accessControlList|Define the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead|Grant read permission to the authorized user. Format: id=" ",id=" "; For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>", where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grant write permission to the authorized user The format is the same as above. | NSString * | No |
|grantFullControl| Grant read and write permissions to the authorized user The format is the same as above. | NSString * | No |


### 3. Download files
#### Example
```objective-c
  QCloudGetObjectRequest* request = [QCloudGetObjectRequest new];
  //Set the URL for download. If it has been set, the file is downloaded to the specified path.
  request.downloadingURL = [NSURL URLWithString:QCloudTempFilePathWithExtension(@"downding")];
  request.object = @"YourObject-Key";
  request.bucket = @"test-123456789";
  [request setFinishBlock:^(id outputObject, NSError \*error) {
    //additional actions after finishing
}];
	[request setDownProcessBlock:^(int64_t bytesDownload, int64_t totalBytesDownload, int64_t totalBytesExpectedToDownload) {
	 //Progress of download
	}];
	[[QCloudCOSXMLService defaultCOSXML] GetObject:request];
```  

## Generating Signature
Any request in the SDK requires a signature to verify the identity of the accessing user and to ensure the security of access. When the signature is incorrect, most COS services are inaccessible and a 403 error is returned. A signature can be generated in SDK. For each request, the signature can be requested from the signatureProvider object in the QCloudServiceConfiguration object. The object for generating signature can be assigned to the signatureProvider at the beginning, and should follow the QCloudSignatureProvider protocol and implement the signature generation method:
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields* )fileds    
                     request:(QCloudBizHTTPRequest* )request    
                  urlRequest:(NSURLRequest* )urlRequst    
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
```
### Best practice: Connect to CAM system for temporary signature
Although the API for generating a signature with permanent SecretId and SecretKey are provided locally, please note that storing the permanent SecretId and SecretKey locally is very risky as it can cause the leakage to lead to unnecessary losses. Therefore, it is recommended to implement the signature on server to ensure the security.        

It is recommended to connect to Tencent Cloud's CAM (Cloud Access Manager) within your own signature server to implement the signature process.     

![Flow Chart of Connecting to CAM for Signature](http://ericcheung-1253653367.cosgz.myqcloud.com/Logical%20View.png)      

For more information on how to set up a signature server to connect to CAM system, please see [Quick Setup of Mobile Application Transfer Service](/document/product/436/9068).

After the signature server is connected to the CAM system, if the client requests a signature from the server, the server requests a temporary certificate from the CAM system and returns it to the client. The CAM system generates temporary Secret ID, Secret Key and Token to generate a signature based on your permanent SecretId and SecretKey. By this way, the security is maximized. After receiving the information of these temporary keys, the terminal builds a QCloudCredential object using the keys, generates the QCloudAuthentationCreator via the QCloudCredentail object, and then generates a QCloudSignature object containing the signature information with this Creator. The example below shows the steps.
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{
    /*Request the temporary Secret ID, Secret Key and Token from signature server*/
    QCloudCredential* credential = [QCloudCredential new];
    credential.secretID = @"The temporary Secret ID obtained from the CAM system";
    credential.secretKey = @"The temporary Secret Key obtained from the CAM system";
    credential.token = @"The Token (session ID) returned from the CAM system"
    credential.expiretionDate	 = /*Signature expiration time*/
    QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
    QCloudSignature* signature =  [creator signatureForData:urlRequst];
    continueBlock(signature, nil);
}

```

### Generate a signature using the permanent keys at the terminal (not recommended due to a great risk of leakage)
```objective-c
- (void) signatureWithFields:(QCloudSignatureFields*)fileds
                     request:(QCloudBizHTTPRequest*)request
                  urlRequest:(NSMutableURLRequest*)urlRequst
                   compelete:(QCloudHTTPAuthentationContinueBlock)continueBlock
{

    QCloudCredential* credential = [QCloudCredential new];
    credential.secretID = @"Permanent SecretID";
    credential.secretKey = @"Permanent SecretKey";
    QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
    QCloudSignature* signature =  [creator signatureForData:urlRequst];
    continueBlock(signature, nil);
}

```

### Managing asynchronous signature process using scaffolding tool
Now you can generate a signature and use the APIs in SDK. However, a scaffolding tool is provided to make it easier for you to implement a temporary signature and obtain the information necessary for temporary signature such as tempSecretKey from server. You can either generate a signature by following the above code, or obtain a temporary signature with our scaffolding tool QCloudCredentailFenceQueue. It provides a fencing mechanism, which means that if you obtain the signature using QCloudCredentailFenceQueue, any request for a signature will not be performed until the signature process is completed. This can eliminate the need to manage the asynchronous process.   
To use QCloudCredentailFenceQueue, generate an instance first.
```objective-c
//AppDelegate.m
//AppDelegate must follow QCloudCredentailFenceQueueDelegate protocol
//
- (BOOL)application:(UIApplication * )application didFinishLaunchingWithOptions:(NSDictionary * )launchOptions {
    // init step
    self.credentialFenceQueue = [QCloudCredentailFenceQueue new];
    self.credentialFenceQueue.delegate = self;
    return YES;
}
```   
Next, the class that calls QCloudCredentailFenceQueue must follow QCloudCredentailFenceQueueDelegate and implement the method defined in the protocol:
```objective-c
- (void) fenceQueue:(QCloudCredentailFenceQueue * )queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
```
When you obtain the signature using QCloudCredentailFenceQueue, all the requests in SDK that need signatures will not be performed until the parameters required for the signature are obtained via the method defined by the protocol and a valid signature is generated. See the example below:
```objective-c
//AppDelegate.m
- (void) fenceQueue:(QCloudCredentailFenceQueue * )queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
{
   QCloudCredential* credential = [QCloudCredential new];
	 //You can synchronize the process to obtain from the server the secretID, secretKey, expiretionDate and token parameters needed for the temporary signature.
   credential.secretID = @"****";
   credential.secretKey = @"****";
   credential.experationDate = [NSDate dateWithTimeIntervalSince1970:1504183628];
   credential.token = @"****";
   QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:credential];
   continueBlock(creator, nil);
}

```   
At this point, you can generate a temporary signature with the scaffolding tool we provide. You can also implement the signature process by yourself.

## User Guide on the Simplified SDK
A simplified SDK is provided for users who only use upload and download features and who can only install a small size SDK. The simplified SDK is half of the complete SDK in terms of size.  

The simplified SDK is implemented via Subspec of Cocoapods, so it can only be integrated by using Cocoapods. Add the simplified SDK into Podfile, and then you can use it.
```
pod 'QCloudCOSXML/Transfer'
```
> Note: For Mobile Line users, the simplified SDK is available only when TACStorage is **disabled** and the official source ("https://github.com/CocoaPods/Specs") of Cocoapods is placed **in front of all sources**. It is recommended to place it in the first line in Podfile. Other users can ignore this note.

The simplified SDK does not have the header file QCloudCOSXML.h. Import the following header file at the time of initialization:
```
#import <QCloudCOSXML/QCloudCOSXMLTransfer.h>
#import <QCloudCore/QCloudCore.h>
```
During initialization, the simplified SDK's APIs for upload and download must be the same with the complete SDK.

