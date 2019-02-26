
>The API documentation applies to those who have completed initialization. It provides a detailed list of APIs and examples for illustrating how to use these APIs. It is recommended to use Control+F to find the desired API, view the API description, and use it in your project as the example illustrates.    

>If you need more features, or do not understand what the returned parameters mean, you are advised to view the comments in the code using three finger drag, Force-touch, or hovering over the variable and pressing Control+Command+D.

## Best Practices of Common Operations
This section describes the best practices of some common operations, which are available after you complete the initialization according to Getting Started.
### Uploading files
For more information, please see [Uploading Files](https://cloud.tencent.com/document/product/436/11280#step---2-.E4.B8.8A.E4.BC.A0.E6.96.87.E4.BB.B6) in Getting Started.

### Resuming upload from breakpoint
Multipart upload is used to upload a file larger than 1 MB. That is, split the file into multiple parts with each holding a size of 1 MB, and then upload these parts (4 at most) in parallel. Resuming upload from breakpoint is implemented on the basis that the uploaded parts are stored in the backend CVM.    

During multipart upload, resumeData for resuming upload is generated after you initialize multipart upload or cancel the upload. This is used to re-generate an upload request for resuming upload, which helps quicken the upload speed. The following example shows how to get ResumeData:
```objective-C
  QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
  //···Set some parameters for upload
  put.initMultipleUploadFinishBlock = ^(QCloudInitiateMultipartUploadResult * multipleUploadInitResult, QCloudCOSXMLUploadObjectResumeData resumeData) {
      //Call back the block after you initialize multipart upload, in which you can obtain resumeData for generating a multipart upload request
      QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
  };

  [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];

  //···When initialization is completed but upload is not completed
  NSError* error;
  //The following shows how resumetData is generated after the user cancels the upload
  resumeData = [put cancelByProductingResumeData:&error];
  if (resumeData) {
          QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest requestWithRequestData:resumeData];
  }
  //The generated request for resuming upload can be directly upload
  [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:request];

```
Note: A part can be stored in the backend CVM only when it is completely uploaded. Meanwhile, the upload speed is quickened. Under the following circumstances, resuming upload from breakpoint cannot be used.
- The file to upload is smaller than 1 MB and multipart upload is not used
- A simple upload API rather than QCloudCOSXMLUploadObjectRequest is used to upload files.
- Upload initialization is not completed (Failure to call back upload initialization) when you cancel generating resumeData

### Downloading files
For more information, please see [Downloading Files](https://cloud.tencent.com/document/product/436/11280#3.-.E4.B8.8B.E8.BD.BD.E6.96.87.E4.BB.B6) in Getting Started.
### Copying files
#### Notes
Initialize a QCloudCOSXMLCopyObjectRequest object, and then call CopyObject of QCloudCOSTransferMangerService. Note that multipart copy is automatically used for large files.  
#### Example
```objective-c
QCloudCOSXMLCopyObjectRequest* request = [[QCloudCOSXMLCopyObjectRequest alloc] init];

request.bucket = @"Destination bucket";
request.object = @"Destination file name";
request.sourceBucket = @"File source bucket. Public read or access to the current account is required";
request.sourceObject = @"Source file name";
request.sourceAPPID = @"Source APPID";
request.sourceRegion= @"Source region";


[request setFinishBlock:^(QCloudCopyObjectResult* result, NSError* error) {
    //Complete callback
    if (nil == error) {
      //Successful
    }
}];
[[QCloudCOSTransferMangerService defaultCOSTransferManager] CopyObject:request];
```

### Adding custom headers
Add custom headers as needed, for example, for server-side encryption. Types allowing addition of custom headers are provided with the attribute customHeaders:
```objective-c
@property (strong, nonatomic) NSDictionary* customHeaders;
```
Key-value pairs with this attribute are added to HTTP headers of the creation requests. For specific examples, please see Server side Encryption in the last section.
## Service Operation
### Listing All Bucket - Get Service
This API (Get Service) is used to obtain all Bucket lists of the requester.

#### Parameters of returned result QCloudListAllMyBucketsResult
| Parameter Name | Description | Type |
| ------ | ---------- |  ---------------------------------- |
| owner  | Bucket owner information               |  QCloudOwner * |
|buckets|All bucket information |NSArray * |
#### Example
```objective-c
    QCloudGetServiceRequest* request = [[QCloudGetServiceRequest alloc] init];
    [request setFinishBlock:^(QCloudListAllMyBucketsResult* result, NSError* error) {
      //
    }];
    [[QCloudCOSXMLService defaultCOSXML] GetService:request];
```

### Generation and use of pre-signed URLs
You can generate a pre-signed URL from the SDK or server, and then upload, download or perform other operations as needed.
#### Description
1. Create an QCloudGetPresignedURLRequest instance.
2. Enter required information such as Bucket, Object, and HTTPMethod.
3. If additional HTTP headers or parameters are required for use, call the method in QCloudGetPresignedURLRequest to add them when generating pre-signed URLs.
4. Call getPresignedURL in QCloudCOSXMLService to send requests, and obtain pre-signed URLs in results.

#### QCloudGetPresignedURLRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket using a pre-signed request |NSString*|Yes |
|object|Object using a pre-signed request. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString*| Yes |
|HTTPMethod|HTTP method of the request using a pre-signed URL. Valid values (case-sensitive): @"GET", @"PUT", @"POST", @"DELETE" |NSString*|Yes |
|contentType| This parameter is available when the request using a pre-signed URL has this header |NSString*|No |
|contentMD5| This parameter is available when the request using a pre-signed URL has this header |NSString*|No |

Note: To set the header or URL parameter of the request using a pre-signed URL, do the followings:    

```objective-c
/**
 Add the header of the request using a pre-signed request

 @param value HTTP header value
 @param requestHeader HTTP header key
 */
- (void)setValue:(NSString * _Nullable)value forRequestHeader:(NSString * _Nullable)requestHeader;

/**
 Add the URL parameter of the request using a pre-signed request

 @param value Parameter value
 @param requestParameter Parameter key
 */
- (void)setValue:(NSString * _Nullable)value forRequestParameter:(NSString *_Nullable)requestParameter;
```

#### Example on how to obtain a pre-signed URL
```objective-c
      QCloudGetPresignedURLRequest* getPresignedURLRequest = [[QCloudGetPresignedURLRequest alloc] init];
      getPresignedURLRequest.bucket = self.bucket;
      getPresignedURLRequest.HTTPMethod = @"PUT";
      getPresignedURLRequest.object = @"testUploadWithPresignedURL";
      [getPresignedURLRequest setFinishBlock:^(QCloudGetPresignedURLResult * _Nonnull result, NSError * _Nonnull error) {
        if (nil == error) {
          NSString* presignedURL = result.presienedURL;
        }
      }
      [[QCloudCOSXMLService defaultCOSXML] getPresignedURL:getPresignedURLRequest];

```
#### Example on how to use a pre-signed URL
The following example shows how to upload with a pre-signed URL.
```objective-C
     NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:[NSURL URLWithString:@"Pre-signedURL"]];
     request.HTTPMethod = @"PUT";
     request.HTTPBody = [@"file content" dataUsingEncoding:NSUTF8StringEncoding];
     [[[NSURLSession sharedSession] downloadTaskWithRequest:request completionHandler:^(NSURL * _Nullable location, NSURLResponse * _Nullable response, NSError * _Nullable error) {
         NSInteger statusCode = [(NSHTTPURLResponse*)response statusCode];
     }] resume];
```

## Bucket Operations

### Listing contents in bucket

#### Method prototype

The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudAppendObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudGetBucketRequest and enter the required parameters.    
2. Call the GetBucket method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content from QCloudListBucketResult in finishBlock of callback.   

#### QCloudGetBucketRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
| region | Indicates the prefix match, which is used to specify the prefix address of the returned file |NSString * | No |
|delimiter|Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path. It can be considered as an ending symbol. For example, if you want a string to end with A, set delimiter to A. | NSString * | No |
|encodingType|Indicates the encoding method of the returned value. Available value: url |NSString * |No |
|marker|Entries are listed using UTF-8 binary order by default, starting from the marker | NSString * | No |
|maxKeys|Maximum number of entries returned at a time. Default is 1,000|int | No |

#### Example

```objective-c
    QCloudGetBucketRequest* request = [QCloudGetBucketRequest new];
    request.bucket = @"testBucket-123456789";
    request.maxKeys = 1000;
    [request setFinishBlock:^(QCloudListBucketResult * result, NSError*   error) {
    //additional actions after finishing
    }];
    [[QCloudCOSXMLService defaultCOSXML] GetBucket:request];
```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.

### Obtaining bucket ACL (Access Control List)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudGetBucketACLRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudGetBucketACLRequest and enter the bucket whose ACL is to be obtained.    
2. Call the GetBucketACL method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content from QCloudACLPolicy in finishBlock of callback.    


#### QCloudGetBucketACLRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |

#### Parameters of returned result QCloudACLPolicy

| Parameter Name | Description | Type |
| ------ | ---------- |  ---------------------------------- |
| owner  | Bucket owner information               |  QCloudACLOwner * |
|list|Information of authorized user and permissions through accessControl|NSArray * |
#### Example

```objective-c
  QCloudGetBucketACLRequest* getBucketACl   = [QCloudGetBucketACLRequest new];
    getBucketACl.bucket = @"testbucket-123456789";
    [getBucketACl setFinishBlock:^(QCloudACLPolicy * _Nonnull result, NSError * _Nonnull error) {
        //QCloudACLPolicy contains Bucket ACL information.
    }];

    [[QCloudCOSXMLService defaultCOSXML] GetBucketACL:getBucketACl];

```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.

### Setting bucket ACL (Access Control List)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudPutBucketACLRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudPutBucketACLRequest, enter the bucket to set, and then enter the corresponding parameters according to the permission type of the bucket.    
2. Call the PutBucketACL method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain the setting result (successful or failed) from finishBlock of callback, and perform some additional operations if the setting is successful.   

#### QCloudPutBucketACLRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|accessControlList|Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead| Grants read permission to the authorized user. Format: id=" ",id=" "; <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;";<br> for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;", <br>where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grants write permission to the authorized user. The format is the same as above. | NSString * | No |
|grantFullControl| Grants read and write permissions to the authorized user. The format is the same as above. | NSString * | No |

#### Example
```objective-c
    QCloudPutBucketACLRequest* putACL = [QCloudPutBucketACLRequest new];
    NSString* appID = @"Your APP ID";
    NSString *ownerIdentifier = [NSString stringWithFormat:@"qcs::cam::uin/%@:uin/%@", appID, appID];
    NSString *grantString = [NSString stringWithFormat:@"id=\"%@\"",ownerIdentifier];
    putACL.grantFullControl = grantString;
    putACL.bucket = @"testBucket-123456789";
    [putACL setFinishBlock:^(id outputObject, NSError *error) {
    //error occucs if error != nil
    }];
    [[QCloudCOSXMLService defaultCOSXML] PutBucketACL:putACL];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


### Obtaining bucket CORS (Cross-Origin Access) configuration

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudPutBucketCORSRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudPutBucketCORSRequest and enter the bucket whose CORS is to be obtained.    
2. Call the GetBucketCORS method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain the result from finishBlock of callback. The result is encapsulated in the QCloudCORSConfiguration object whose "rules" attribute is an array containing a set of QCloudCORSRule. The specific CORS configurations are encapsulated in the QCloudCORSRule object.   

#### QCloudPutBucketCORSRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |


#### Parameters of returned result QCloudCORSConfiguration

| Parameter Name | Description | Type |
| ------ | ---------- | ---------------------------------- |
| rules | The array containing CORS. It is a QCloudCORSRule instance. | NSArray&lt;QCloudCORSRule`*` > * |

#### QCloudCORSRule parameters

| Parameter Name | Description | Type |
| ------ | ---------- | ---------------------------------- |
| identifier  | Sets rule ID |NSString *   |
|allowedMethod|Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE. |NSArray&lt;NSString`*`&gt;`*` |
|allowedOrigin|Allowed access source. The wildcard "*" is supported. Format: protocol://domain name[:port], for example, `http://www.qq.com` |NSString * |
|allowedHeader|When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |NSArray&lt;NSString`*`&gt; `*`|
|maxAgeSeconds|Sets the validity period of the results obtained by OPTIONS |int|
|exposeHeader|Sets the custom header information that can be received by the browser from the server end. |    NSString * |

#### Example
```objective-c
	QCloudGetBucketCORSRequest* corsReqeust = [QCloudGetBucketCORSRequest new];
	corsReqeust.bucket = @"testBucket-123456789";

	[corsReqeust setFinishBlock:^(QCloudCORSConfiguration * _Nonnull result, NSError * _Nonnull error) {
	    //CORS is encapsulated in result.
  	}];

	[[QCloudCOSXMLService defaultCOSXML] GetBucketCORS:corsReqeust];

```    
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Configuring bucket CORS (Cross-Origin Access)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudPutBucketCORSRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudPutBucketCORSRequest, configure the bucket, and put the required CORS into QCloudCORSRule. If there are multiple CORS configurations, you can place multiple QCloudCORSRule in an NSArray, put the array into QCloudCORSConfiguration's rules attribute, and then into the request.    
2. Call the PutBucketCORS method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain the setting result (error is empty or not) from finishBlock of callback, and perform additional operations if the setting is successful.   

#### QCloudPutBucketCORSRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|corsConfiguration|Specific parameter that encapsulates CORS |QCloudCORSConfiguration * |Yes |

#### QCloudCORSConfiguration parameters

| Parameter Name | Description | Type |
| ------ | ---------- | ---------------------------------- |
| rules  | The array containing CORS. It is a QCloudCORSRule instance. |NSArray&lt;QCloudCORSRule`*` > *  |

#### QCloudCORSRule parameters

| Parameter Name | Description | Type |
| ------ | ---------- | ---------------------------------- |
| identifier  | Sets rule ID | NSString *   |
|allowedMethod|Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE. |NSArray &lt;NSString`*`> * |
|allowedOrigin|Allowed access source. The wildcard "*" is supported. Format: protocol://domain name[:port], for example, `http://www.qq.com` |NSString * |
|allowedHeader|When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |NSArray &lt;NSString `*` > * |
|maxAgeSeconds|Sets the validity period of the results obtained by OPTIONS |int|
|exposeHeader|Sets the custom header information that can be received by the browser from the server end. |   NSString * |

#### Example

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
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Getting bucket location

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudGetBucketLocationRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudGetBucketLocationRequest and enter the Bucket name.    
2. Call the GetBucketLocation method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudGetBucketLocationRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 | NSString * |Yes |


#### Parameters of returned result QCloudBucketLocationConstraint
| Parameter Name | Description | Type |
| ------ | ---------- |  ---------------------------------- |
| locationConstraint  | The region where the Bucket resides. |NSString* |

#### Example
```objective-c

  QCloudGetBucketLocationRequest* locationReq = [QCloudGetBucketLocationRequest new];
    locationReq.bucket = @"testBucket-123456789";
    __block QCloudBucketLocationConstraint* location;
    [locationReq setFinishBlock:^(QCloudBucketLocationConstraint * _Nonnull result, NSError * _Nonnull error) {
        location = result;
    }];
    [[QCloudCOSXMLService defaultCOSXML] GetBucketLocation:locationReq];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Deleting Bucket CORS configuration

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudDeleteBucketCORSRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudDeleteBucketCORSRequest and enter the required parameters.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudDeleteBucketCORSRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
#### Example
```objective-c
 QCloudDeleteBucketCORSRequest* deleteCORS = [QCloudDeleteBucketCORSRequest new];
    deleteCORS.bucket = @"testBucket-123456789";
    [deleteCORS setFinishBlock:^(id outputObject, NSError *error) {
        //success if error == nil
    }];
    [[QCloudCOSXMLService defaultCOSXML] DeleteBucketCORS:deleteCORS];
```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Querying multipart upload in a bucket (List Bucket Multipart Uploads)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before bucket operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudListBucketMultipartUploadsRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudListBucketMultipartUploadsRequest and enter the required parameters, such as the prefix and the encoding method of the returned result.    
2. Call the ListBucketMultipartUploads method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudListBucketMultipartUploadsRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
| prefix | The returned Object key must be prefixed with Prefix. Note that the returned key will still contain Prefix when querying with prefix |NSString * | No   |
|delimiter|Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path. It can be considered as an ending symbol. For example, if you want a string to end with A, set delimiter to A. | NSString * | No |
|encodingType|Indicates the encoding method of the returned value. Available value: url |NSString * |No |
|keyMarker| Entries will be listed starting from this key value	|NSString * | No |
|uploadIDMarker|Entries will be listed starting from this UploadId value |int | No |
|maxUploads|Sets the maximum number of multipart returned. Valid values: 1-1,000 |int|No |

#### Parameters of returned result QCloudListMultipartUploadsResult

| Parameter Name | Description | Type |
| ------ | ---------- | ---- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 | NSString * |
| prefix | The returned Object key must be prefixed with Prefix. Note that the returned key will still contain Prefix when querying with prefix |NSString * |
|delimiter|Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path.|NSString * |
|encodingType|Indicates the encoding method of the returned value. Available value: url |NSString * |
|keyMarker| Entries will be listed starting from this key value	| NSString * |
|maxUploads|Sets the maximum number of multipart returned. Valid values: 1-1,000 |int|
|uploads|Information of all multipart upload operations |NSArray*|

#### Example
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
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Query whether the Head Bucket exists
The Head Bucket request is used to determine whether the Bucket and the permission to access the Bucket exist. The same permission applies to Head and Read. HTTP status code 200 will be returned if the Bucket exists, 403 if there is no permission, and 404 if the Bucket does not exist.    
#### QCloudHeadBucketRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |

#### Example
```objective-c
QCloudHeadBucketRequest* request = [QCloudHeadBucketRequest new];
 request.bucket = @"testBucket-123456789";
 [request setFinishBlock:^(id outputObject, NSError* error) {
     //Set the completion callback. If there is no error, you can access the bucket normally. Otherwise, you can get the specific failure reason by viewing the error code and message.
 }];
 [[QCloudCOSXMLService defaultCOSXML] HeadBucket:request];
```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.




### Put Bucket Tagging
#### QCloudPutBucketTaggingRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |
|taggings|An array containing the tags to be set |QCloudBucketTagging|Yes |

#### Example
```objective-c
QCloudPutBucketTaggingRequest* putTagging = [QCloudPutBucketTaggingRequest new];
   QCloudBucketTagging* tagging = [QCloudBucketTagging new];
   QCloudBucketTag* tag = [QCloudBucketTag new];
   tag.key = @"tag's key";
   tag.value = @"tag's value";
   tagging.tagset = @[tag];

   putTagging.bucket = @"testBucket-123456789";
   putTagging.taggings = tagging;

   [putTagging setFinishBlock:^(id outputObject, NSError *error) {
       //Complete callback
   }];
   [[QCloudCOSXMLService defaultCOSXML] PutBucketTagging:putTagging];
```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Delete Bucket Tagging    
#### QCloudDeleteBucketTaggingRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |


#### Example
```objective-c
QCloudDeleteBucketTaggingRequest* request = [QCloudDeleteBucketTaggingRequest new];
   request.bucket = @"testBucket-123456789";
   [request setFinishBlock:^(id outputObject, NSError* error) {
       //Delete the completion callback
   }];
   [[QCloudCOSXMLService defaultCOSXML] DeleteBucketTagging:request];
```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Get Bucket Tagging   
#### QCloudGetBucketTaggingRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |

#### Parameters of returned result QCloudBucketTagging
| Parameter Name | Description | Type |
| ------ | ---------- |  ---------------------------------- |
| tagest  |The array containing bucket tags |NSArray* |
#### Example
```objective-c
QCloudGetBucketTaggingRequest* request = [QCloudGetBucketTaggingRequest new];
   request.bucket = @"testBucket-123456789" ;

   [request setFinishBlock:^(QCloudBucketTagging* result, NSError* error) {
      //Set the completion callback
   }];
   [[QCloudCOSXMLService defaultCOSXML] GetBucketTagging:request];
```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


###  Put Bucket Lifecycle
COS allows you to to manage the lifecycle of an Object in Bucket by configuring lifecycle. The lifecycle configuration contains one or more rule sets that will be applied to a group of object rules (each rule defines an operation for COS).
These operations are divided into the following two types:

Transition: Specify the time when the storage class of an object is changed to another one. For example, you can specify that the storage class of an object is changed to STANDARD_IA (applicable to the objects that are accessed infrequently) 30 days after it is created.
Expiration: Specify the expiration time of Object. COS will automatically delete the expired objects.

This API (Put Bucket Lifecycle) is used to create a new lifecycle configuration for a Bucket. If lifecycle has been configured for the Bucket, you can use this API to create a new configuration to overwrite the existing one.
#### Parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |
|lifeCycle|Sets Bucket lifecycle configuration |QCloudLifecycleConfiguration*|Yes |   

#### QCloudLifecycleConfiguration parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|rules|An array describing a collection of rules | NSArray<QCloudLifecycleRule*> *|Yes |   

#### QCloudLifecycleRule parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|identifier|Uniquely identify the rule. Its length cannot exceed 255 characters. |NSString*|Yes |
|filter|Describe a collection of Objects that are subject to the rules. |QCloudLifecycleRuleFilter*|
|status| Indicates whether the rule is enabled. Enumerated values: Enabled, Disabled |QCloudLifecycleStatue| Yes |
|abortIncompleteMultipartUpload|Sets the maximum time length allowed for a multipart upload. |QCloudLifecycleAbortIncompleteMultipartUpload|No |
|transition|Rule transition attribute, which indicates when the Object is transited to Standard_IA or others. |QCloudLifecycleTransition*|No |
|expiration|Rule expiration attribute |QCloudLifecycleExpiration*|No |
|noncurrentVersionExpiration||Indicates when objects of non-current version expire |QCloudLifecycleExpiration*|No |
|noncurrentVersionTransition|Indicates when objects of non-current version are transited to STANDARD_IA orothers. |QCloudNoncurrentVersionExpiration*|No |
#### Example
```objective-c
QCloudPutBucketLifecycleRequest* request = [QCloudPutBucketLifecycleRequest new];
   request.bucket = @"Enter bucket name";
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
     //Set the completion callback
   }];
   [[QCloudCOSXMLService defaultCOSXML] PutBucketLifecycle:request];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Get Bucket Lifecycle

#### Parameters of returned result QCloudLifecycleConfiguration
Same with QCloudLifecycleConfiguration in the API Put Bucket Lifecycle.
#### Example
```objective-c
QCloudGetBucketLifecycleRequest* request = [QCloudGetBucketLifecycleRequest new];
   request.bucket = @"testBucket-123456789";
   [request setFinishBlock:^(QCloudLifecycleConfiguration* result,NSError* error) {
     //Set the completion callback
   }];
   [[QCloudCOSXMLService defaultCOSXML] GetBucketLifecycle:request];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



###  Delete Bucket Lifecycle

#### Parameters of returned result QCloudLifecycleConfiguration

Same with QCloudLifecycleConfiguration in the API Put Bucket Lifecycle.

#### Example
```objective-c
     QCloudDeleteBucketLifeCycleRequest* request = [[QCloudDeleteBucketLifeCycleRequest alloc ] init];
     request.bucket = @"testBucket-123456789";
     [request setFinishBlock:^(QCloudLifecycleConfiguration* result, NSError* error) {
       //Set the completion callback
     }];
     [[QCloudCOSXMLService defaultCOSXML] DeleteBucketLifeCycle:request];
```

###  Put Bucket Versioning   
Put Bucket Versioning is used to enable or suspend the version control of the Bucket. Note: this is an irreversible API, and cannot be disabled after being enabled.
#### QCloudPutBucketVersioningRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |
|configuration| Version control details |QCloudBucketVersioningConfiguration*|Yes |

#### QCloudBucketVersioningConfiguration parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|status|Indicates whether version is enabled. Enumerated values: Suspended, Enabled. |QCloudCOSBucketVersioningStatus|Yes |


#### Example
```objective-c
QCloudPutBucketVersioningRequest* request = [[QCloudPutBucketVersioningRequest alloc] init];
 request.bucket = @"testBucket-123456789";
 QCloudBucketVersioningConfiguration* configuration = [[QCloudBucketVersioningConfiguration alloc] init];
 request.configuration = configuration;
 configuration.status = QCloudCOSBucketVersioningStatusEnabled;
 [request setFinishBlock:^(id outputObject, NSError* error) {
   //Set the completion callback
 }];
 [[QCloudCOSXMLService defaultCOSXML] PutBucketVersioning:request];
```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


###  Get Bucket Versioning  

#### Parameters of returned result QCloudBucketVersioningConfiguration
| Parameter Name | Description | Type |
| ------ | ---------- | ---- |
|status|Indicates whether version is enabled. Enumerated values: Suspended, Enabled. |QCloudCOSBucketVersioningStatus|

#### Example
```objective-c
QCloudGetBucketVersioningRequest* request = [[QCloudGetBucketVersioningRequest alloc] init];
           request.bucket = @"testBucket-123456789";
           [request setFinishBlock:^(QCloudBucketVersioningConfiguration* result, NSError* error) {
             //Set the completion callback
           }];
        [[QCloudCOSXMLService defaultCOSXML] GetBucketVersioning:request];
```


###  Put Bucket Replication  
This API (Put Bucket Replication) is used to add replication configuration to the bucket for which versioning is enabled. If the bucket already has a replication configuration, the request will replace the existing configuration.    
#### QCloudPutBucketReplicationRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString*|Yes |
|configuation|QCloudBucketReplicationConfiguation*| Yes |


Note:
To use this API, version management must be enabled for the bucket. For more information on version management, please see Put Bucket Versioning.
#### Parameters of returned result

#### Example
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
       //Set the completion callback
     }];
     [[QCloudCOSXMLService defaultCOSXML] PutBucketRelication:request];
```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


###   Get Bucket Replication
This API (Get Bucket Replication) is used to read the cross-origin replication configuration information in a bucket.
#### Parameters of returned result QCloudBucketReplicationConfiguation
| Parameter Name | Description | Type |
| ------ | ---------- | ---- |
|role|Initiator ID, in the format of qcs::cam::uin/<OwnerUin>:uin/<SubUin>|NSString*|
|rule| Specific configuration information. A maximum of 1,000 rules are supported. All rules must directed to one destination bucket. |NSArray<QCloudBucketReplicationRule*> *|

#### QCloudBucketReplicationRule parameters
| Parameter Name | Description | Type |
| ------ | ---------- | ---- |
|status|Whether the Rule takes effect |QCloudQCloudCOSXMLStatus|
|identifier|Indicates the name of a specific Rule |NSString*|
|prefix|Prefix match policy. Prefixes cannot overlap, otherwise an error is returned. This is left empty for root directory. |NSString*|
|destination|Destination bucket information |QCloudBucketReplicationDestination*|
#### Example
```objective-c
    QCloudGetBucketReplicationRequest* request = [[QCloudGetBucketReplicationRequest alloc] init];
    request.bucket = @"testBucket-123456789";

    [request setFinishBlock:^(QCloudBucketReplicationConfiguation* result, NSError* error) {
      //Set the completion callback
    }];
    [[QCloudCOSXMLService defaultCOSXML] GetBucketReplication:request];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.




###  Delete Bucket Replication  
This API (Delete Bucket Replication) is used to delete the cross-origin replication configuration in a bucket.
#### Parameters

#### Parameters of returned result

#### Example
```objective-c
    QCloudDeleteBucketReplicationRequest* request = [[QCloudDeleteBucketReplicationRequest alloc] init];
      request.bucket = @"testBucket-123456789";
      [request setFinishBlock:^(id outputObject, NSError* error) {
      //Set the completion callback
      }];
    [[QCloudCOSXMLService defaultCOSXML] DeleteBucketReplication:request];
```


## File-related Operations
In COS, each file is an object. Operating on a file is actually operating on an object.
### Simple Upload (Put Object)
Simple upload only applies to files less than 20 MB, and supports uploading files from memory.

#### QCloudPutObjectRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  | NSString * | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|body|If the file is stored in the hard disk, it is the path of the file to be uploaded, and you can enter the variable of NSURL * type. If the file is stored in memory, you can enter the variable of NSData * type that contains the file binary data. |BodyType|Yes |
| storageClass | Storage class of object |QCloudCOSStorageClass | Yes    |
|cacheControl|Cache policy defined in RFC 2616 |NSString *  |No |
|contentDisposition|File name defined in RFC 2616 |NSString * |No |
|expect|When expect=@"100-Continue" is used, the request content will not be sent until the receipt of response from server. |NSString * | No |
|expires| Expiration time defined in RFC 2616 |NSString * |No |
|initMultipleUploadFinishBlock| If the request generates a multipart upload request, after the initialization of multipart upload, a callback is performed via the block. The bucket, key, and uploadID after the completion of multipart upload, and ResumeData for resuming subsequent failed upload can be obtained from this callback block. | block| No |
|accessControlList|Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead| Grants read permission to the authorized user. Format: id=" ",id=" "; For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>"; for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin>:uin/&lt;OwnerUin>", where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grants write permission to the authorized user. The format is the same as above. | NSString * | No |
|grantFullControl| Grants read and write permissions to the authorized user. The format is the same as above. | NSString * | No |    

#### Example    
```objective-C
QCloudPutObjectRequest* put = [QCloudPutObjectRequest new];
put.object = @"object-name";
put.bucket = @"bucket-12345678";
put.body =  [@"testFileContent" dataUsingEncoding:NSUTF8StringEncoding];
[put setFinishBlock:^(id outputObject, NSError *error) {
    //Complete callback
    if (nil == error) {
      //Successful
    }
}];
[[QCloudCOSXMLService defaultCOSXML] PutObject:put];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Querying object's ACL (Access Control List)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudGetObjectACLRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudGetObjectACLRequest, and enter the bucket name and the name of the object to be queried.    
2. Call the GetObjectACL method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain the specific ACL information encapsulated in the QCloudACLPolicy object obtained from finishBlock in callback.   

#### QCloudGetObjectACLRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|object| Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString * | Yes |

#### Example

```objective-c
 request.bucket = self.aclBucket;
    request.object = @"Object name";
    request.bucket = @"testBucket-123456789"
    __block QCloudACLPolicy* policy;
    [request setFinishBlock:^(QCloudACLPolicy * _Nonnull result, NSError * _Nonnull error) {
        policy = result;
    }];
    [[QCloudCOSXMLService defaultCOSXML] GetObjectACL:request];
```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


### Setting object's ACL (Access Control List)

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before object operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudPutObjectACLRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudPutObjectACLRequest, and enter the bucket name and additionally required parameters, such as authorization information.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain whether the configuration is completed from finishBlock in callback. If error is null, configuration is successful.   

#### QCloudPutObjectACLRequest parameters


| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 | NSString * |Yes |
|object|Object name |NSString * |Yes |
|accessControlList|Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead| Grants read permission to the authorized user. Format: id=" ",id=" "; <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;";<br> for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;", <br>where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grants write permission to the authorized user. The format is the same as above. |NSString * |No |
|grantFullControl| Grants read and write permissions to the authorized user. The format is the same as above. |NSString * |No |
#### Example
```objective-c
    QCloudPutObjectACLRequest* request = [QCloudPutObjectACLRequest new];
    request.object = @"Name of the object whose ACL needs to be set";
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
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.




### Downloading files

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating an instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate and enter the required parameters.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### Parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---------- | ---------------------------------- |
| bucket  |Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|object|Object name |NSString * |Yes |
|range|The specified range of file download defined in RFC 2616 (in bytes) |NSString * |No |
|ifModifiedSince| The file content is returned if the file has been modified after the specified time. Otherwise 412 is returned (not modified) |NSString * | No |
|responseContentType| Sets the Content-Type parameter in the response header |NSString * | No |
|responseContentLanguage| Sets the Content-Language parameter in the response header |NSString * | No |
|responseContentExpires| Sets the Content-Expires parameter in the response header |NSString * | No |
|responseCacheControl|Sets the Cache-Control parameter in the response header |NSString * |No |
|responseContentDisposition|Sets the Content-Disposition parameter in the response header. |NSString * |No |
|responseContentEncoding| Sets the Content-Encoding parameter in the response header |NSString * | No |

#### Example

```objective-c
  QCloudGetObjectRequest* request = [QCloudGetObjectRequest new];
  //Set the URL for download. If it has been set, the file is downloaded to the specified path. Otherwise, the file is downloaded to outputObject of finishBlock.
  request.downloadingURL = [NSURL URLWithString:QCloudTempFilePathWithExtension(@"downding")];
  request.object = @"Your Object-Key";
  request.bucket = @"testBucket-123456789";
  [request setFinishBlock:^(id outputObject, NSError *error) {
    //additional actions after finishing
}];
	[request setDownProcessBlock:^(int64_t bytesDownload, int64_t totalBytesDownload, int64_t totalBytesExpectedToDownload) {
	 //Progress of download
	}];
	[[QCloudCOSXMLService defaultCOSXML] GetObject:request];
```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Pre-request for cross-origin access configuration of objects

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudOptionsObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudOptionsObjectRequest, enter the object name and bucket name, and simulate the HTTP method of the request for cross-origin access and the access sources allowed for cross-origin access.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudOptionsObjectRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | -------|---------------------------------- |
| object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString *   | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|accessControlRequestMethod|Simulates the HTTP method of the request for cross-origin access |NSArray&lt;NSString`*`> * | Yes |
|origin|Simulates the access sources allowed for cross-origin access. The wildcard "*" is supported. Format: protocol://domain name[:port], for example, `http://www.qq.com` |NSString * | Yes |
|allowedHeader| When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |NSArray&lt;NSString `*` > * | No |

#### Example
```objective-c

 QCloudOptionsObjectRequest* request = [[QCloudOptionsObjectRequest alloc] init];
    request.bucket =@"Bucket name";
    request.origin = @"*";
    request.accessControlRequestMethod = @"get";
    request.accessControlRequestHeaders = @"host";
    request.object = @"Object name";
    __block id resultError;
    [request setFinishBlock:^(id outputObject, NSError* error) {
        resultError = error;
    }];

    [[QCloudCOSXMLService defaultCOSXML] OptionsObject:request];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Deleting a single object

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudDeleteObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudDeleteObjectRequest and enter the required parameters.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudDeleteObjectRequest parameters
| Parameter Name | Type | Required | Description |
| ------ | ---------- | -------|---------------------------------- |
| object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString *   | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
#### Example

```objective-c

QCloudDeleteObjectRequest* deleteObjectRequest = [QCloudDeleteObjectRequest new];
    deleteObjectRequest.bucket = @"testBucket-123456789";
    deleteObjectRequest.object = @"Object name";

    __block NSError* resultError;
    [deleteObjectRequest setFinishBlock:^(id outputObject, NSError *error) {
        resultError = error;
    }];
    [[QCloudCOSXMLService defaultCOSXML] DeleteObject:deleteObjectRequest];

```
### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Deleting multiple objects

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudDeleteMultipleObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudDeleteMultipleObjectRequest and enter the required parameters.    
2. Call the method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudDeleteMultipleObjectRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | -------|---------------------------------- |
| object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString *   | Yes |
|deleteObjects|Encapsulate information of multiple objects to be deleted in batches |QCloudDeleteInfo * |Yes |

#### QCloudDeleteInfo parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | -------|---------------------------------- |
| objects  |  An array containing information on the objects to be deleted  |NSArray&lt;QCloudDeleteObjectInfo `*` > *   |Yes |

#### QCloudDeleteObjectInfo parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | -------|---------------------------------- |
| key  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString *   | Yes |

#### Example
```objective-c

QCloudDeleteMultipleObjectRequest* delteRequest = [QCloudDeleteMultipleObjectRequest new];
    delteRequest.bucket = @"testBucket-123456789";

    QCloudDeleteObjectInfo* deletedObject0 = [QCloudDeleteObjectInfo new];
    deletedObject0.key = @"Name of the first object";

    QCloudDeleteObjectInfo* deleteObject1 = [QCloudDeleteObjectInfo new];
    deleteObject1.key = @"Name of the second object";

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

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



### Initializing multipart upload

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudInitiateMultipartUploadRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudInitiateMultipartUploadRequest and enter the required parameters.    
2. Call the InitiateMultipartUpload method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### Parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | The name of the file (object) to be uploaded, i.e. the key of the object. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString * | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
| storageClass | Storage class of object | QCloudCOSStorageClass | Yes    |
|cacheControl|Cache policy defined in RFC 2616 |NSString * |No |
|contentDisposition|File name defined in RFC 2616 |NSString * |No |
|expect|When `expect=@"100-continue"` is used, the request content will not be sent until the receipt of response from server. |NSString * | No |
|expires| Expiration time defined in RFC 2616 |NSString * |No |
|storageClass| Storage class of object |QCloudCOSStorageClass| No |
|accessControlList|Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead| Grants read permission to the authorized user. Format: id=" ",id=" "; <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;";<br> for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;", <br>where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grants write permission to the authorized user. The format is the same as above. |NSString * |No |
|grantFullControl| Grants read and write permissions to the authorized user. The format is the same as above. |NSString * |No |


#### Example
```objective-c

QCloudInitiateMultipartUploadRequest* initrequest = [QCloudInitiateMultipartUploadRequest new];
    initrequest.bucket = @"testBucket-123456789";
    initrequest.object = @"Object name";
    __block QCloudInitiateMultipartUploadResult* initResult;
    [initrequest setFinishBlock:^(QCloudInitiateMultipartUploadResult* outputObject, NSError *error) {
        initResult = outputObject;
    }];
    [[QCloudCOSXMLService defaultCOSXML] InitiateMultipartUpload:initrequest];

```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


### Obtaining object meta information

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudHeadObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudHeadObjectRequest and enter the required parameters.    
2. Call the HeadObject method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudHeadObjectRequest parameters

| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString * | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|ifModifiedSince| The file content is returned if the file has been modified after the specified time. Otherwise 304 is returned (not modified). |NSString * |Yes |

#### Example
```objective-c
QCloudHeadObjectRequest* headerRequest = [QCloudHeadObjectRequest new];
    headerRequest.object = @"Object name";
    headerRequest.bucket = @"testBucket-123456789";

    __block id resultError;
    [headerRequest setFinishBlock:^(NSDictionary* result, NSError *error) {
        resultError = error;
    }];

    [[QCloudCOSXMLService defaultCOSXML] HeadObject:headerRequest];

```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.


### Appending file
This API (Append Object) is used to upload an object (file) to the specified bucket via multipart upload method. An object can be uploaded using the API Append Object only when its attribute is "Appendable".
You can query the attribute of an object using Head Object operation. When you initiate Head Object request, the custom Header [x-cos-object-type] will be returned, which only contains two enumerated values: Normal or Appendable. The object created using Append Object operation is an Appendable file and the object uploaded using Put Object is a Normal file.
When an Appendable Object is operated by the request executing Put Object, the original Object will be overwritten and its attribute will change to Normal.
The recommended size for the appended Object is 1 MB to 5 GB. If the value of Position is inconsistent with the length of the current Object, COS returns a 409 error.  If a file with Normal attribute is appended, COS returns 409 ObjectNotAppendable.

#### Method prototype
The header file QCloudCOSXML/QCloudCOSXML.h needs to be imported before file operations. Before that, you need to complete the initialization in STEP-1 in Quick Start by creating a QCloudAppendObjectRequest instance and enter some additional restrictions as needed to get the approved content. The steps are as follows:    
1. Instantiate QCloudAppendObjectRequest and enter the required parameters.    
2. Call the AppendObject method in the QCloudCOSXMLService object to initiate the request.    
3. Obtain specific content in finishBlock of callback.   

#### QCloudAppendObjectRequest parameters
| Parameter Name | Description | Type | Required |
| ------ | ---------- | ---- | ---------------------------------------- |
| Object  | The name of the file (object) to be uploaded, i.e. the key of the object. Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. For more information, please see [Object Description](https://cloud.tencent.com/document/product/436/13324)  |NSString * | Yes |
|bucket|Bucket name, which can be found in [COS V5 Console](https://console.cloud.tencent.com/cos5/bucket), with a format of &lt;bucketName&gt;-&lt;APPID&gt;, such as testBucket-1253653367 |NSString * |Yes |
|position|Start point of the append operation (in bytes). position=0 for initial append. position=content-length of the current Object for subsequent append |int|Yes |
|body|The path of the file to be uploaded. Enter a variable of NSURL * type |BodyType|Yes |
| storageClass | QCloudCOSStorageClass | Yes    |  Storage class of object |
|cacheControl|Cache policy defined in RFC 2616 |NSString * |No |
|contentDisposition|File name defined in RFC 2616 |NSString * |No |
|expect|When `expect=@"100-continue"` is used, the request content will not be sent until the receipt of response from server. |NSString * | No |
|expires| Expiration time defined in RFC 2616 |NSString * |No |
|storageClass| Storage class of object |QCloudCOSStorageClass| No |
|accessControlList|Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read; Default: private |NSString * |No |
|grantRead| Grants read permission to the authorized user. Format: id=" ",id=" "; <br>For authorization to a subaccount, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;";<br> for authorization to the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;", <br>where OwnerUin refers to the ID of the root account and SubUin refers to the ID of the subaccount |NSString * |No |
|grantWrite| Grants write permission to the authorized user. The format is the same as above. |NSString * |No |
|grantFullControl| Grants read and write permissions to the authorized user. The format is the same as above. |   NSString * |No |


#### Example
```objective-c
 QCloudAppendObjectRequest* put = [QCloudAppendObjectRequest new];
    put.object = [NSUUID UUID].UUIDString;
    put.bucket = @testBucket-123456789;
    put.body =  File URL, NSURL*type
    __block NSDictionary* result = nil;
    [put setFinishBlock:^(id outputObject, NSError *error) {
        result = outputObject;
    }];
    [[QCloudCOSXMLService defaultCOSXML] AppendObject:put];

```

### Error codes
When the SDK request fails, the error returned is not empty and includes the error code, error description, and other necessary debugging information to help developers quickly solve the problem. Error codes (encapsulated in the returned error) include those returned by the device due to network problems and those returned by COS.
- Error codes generated by the device due to network problems are negative four digits, for example -1001. These error codes are defined by Apple. For more information, please see the definitions in the header file NSURLError.h or [Apple Official Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes).

- Error codes returned by COS are based on HTTP status codes, such as 404 and 503. For solutions to these error codes, please see [Error Codes](https://cloud.tencent.com/document/product/436/7730) in COS Official Documentation.



## Server-side Encryption
COS provides server-side encryption to encrypt the object uploaded to COS before storing it. When you download an object, the original encrypted data will be decrypted and returned. This process is transparent to the client and you do not need to care about the specific encryption process.

To use this feature, you need to add an additional header (key: x-cos-server-side-encryption, value: AES256) in the HTTP upload request when uploading an object. When you download the object, use GetObject as usual.

This can be achieved using the custom header feature in the SDK. That is, add the custom header to the upload request:

```objective-c
   QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
   __block NSString* object = [NSUUID UUID].UUIDString;
   put.object = @"object";
   put.bucket = @"Bucket name";
   put.body =  @"File's local URL";
   put.customHeaders = @{@"x-cos-server-side-encryption":@"AES256"};
   [put setFinishBlock:^(QCloudUploadObjectResult *result, NSError *error) {
     //Complete callback
   }];
   [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];
```

You do not need to care about the encryption and decryption process when downloading:
```objective-c
QCloudGetObjectRequest* getObjectRequest = [[QCloudGetObjectRequest alloc] init];
       getObjectRequest.bucket = self.bucket;
       getObjectRequest.object = object;
       NSURL* downloadPath = @"Path to the file downloaded to the local machine";
       getObjectRequest.downloadingURL = downloadPath;
       [getObjectRequest setFinishBlock:^(id outputObject, NSError *error) {
         //Complete callback
       }];
       [[QCloudCOSXMLService defaultCOSXML] GetObject:getObjectRequest];
```

