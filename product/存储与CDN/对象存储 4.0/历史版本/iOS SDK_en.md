## Preparations for Development

### Acquiring SDK

You can download iOS SDK for Cloud Object Storage (COS) from [iOS SDK](https://github.com/tencentyun/COS_iOS_SDK.git) 

For more examples, refer to [iOS Demo](https://github.com/tencentyun/COS_iOS_SDK.git). 

### Preparations for Development

-  iOS 7.0+;
-  Your mobile phone must be connected to the Internet (either via GPRS, 3G or Wi-Fi connection);
-  4. Get APP ID, SecretID, SecretKey from the console.


### Configuring SDK

#### SDK Import

iOS SDK package for COS:

- COSClientSDK.zip

In the package, there is a static library (.a file) and a Headers folder containing a header file, as shown below: The upload package is available in two versions: one supporting bitcode and the other not. You can select based on your business needs.

![Upload SDK](https://mccdn.qcloud.com/static/img/05f5a1d6768985aa11b23c3808914989/image.png)

![Download SDK](https://mccdn.qcloud.com/static/img/190e5c8c4920ba4d7334f7ba64fd3839/image.png)

When dragging the unpacked COSSDK into the project directory, Xcode will automatically add it to the list of link libraries.

![Import SDK Package](https://mccdn.qcloud.com/static/img/96dda4e5f2e4f8fab3fbda3de1cd8e25/image.png)

**Note:** You can import upload/download SDK package based on your business needs.

#### Configuring Project

Set up "Other Linker Flags" in "Build Settings" and add the parameter "-ObjC".

![Parameter Configuration](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

Add "App Transport Security Settings" to the "info.plist" file of the project, and then add the "Allow Arbitrary Loads" as "Boolean" in "App Transport Security Settings", and set its value to "YES"

### Initialization

Introduce *COSClient .h* header file of upload SDK. Directory-related operations need first instantiate COSClient object.

#### Method Prototype

```objective-c
- (instancetype)initWithAppId:(NSString*)appId  withRegion:(NSString *)region;
```

#### Parameter Description

| Parameter Name   | Type          | Required | Description                                 |
| ------ | ----------  | ---- | ---------------------------------- |
| appId  | NSString *  | Yes    | Project ID, i.e. APP ID.                       |
| region | NSString *  | Yes    | The data center region where bucket is created. For example, East China: "sh", South China: "gz", and North China: "tj" |

#### Example

```objective-c
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
```

## Quick Start

The following shows the basic process of upload and download. For details, please refer to demo. Before that, please apply for an appid for COS business on the Tencent Cloud console;

### STEP 1 Initializing COSClient

#### Example

```objective-c
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
```

### STEP 2 Uploading a File

Let's assume that you have applied for your own business bucket. All tasks of SDK correspond to appropriate "task". You can complete operations by passing corresponding "task" parameters to the client;

#### Example

```objective-c
    COSObjectPutTask *task = [COSObjectPutTask new];
    task.filePath = path;
    task.fileName = fileName;
    task.bucket = bucket;
    task.attrs = @"customAttribute";
    task.directory = dir;
    task.insertOnly = YES;
    task.sign = _sign;
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
         //sucess
        }else{}
    };
    client.progressHandler = ^(NSInteger bytesWritten,NSInteger totalBytesWritten,NSInteger totalBytesExpectedToWrite){
          //progress
    };
    [client putObject:task];
```

### STEP 3 Downloading a File

#### Example

```objective-c
 	COSObjectGetTask *cm = [[COSObjectGetTask alloc] initWithUrl:imgUrl.text];
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
		//
    };
    client.downloadProgressHandler = ^(int64_t receiveLength,int64_t contentLength){        
    };
    [client getObjectRequest:cm];
```

## Generating Signature

**Signature Types:**

| Type   | Description            |
| ---- | ------------- |
| Multiple-time | It can be used multiple times before the expiration time   |
| One-time | It is bound to the source URL and only be used once |

**Acquiring Signature:**

This is the signature used in mobile device SDK. To secure the key and other information, it is recommended that users create simple key creation and capture services. Then, the client will first request the valid signature from the server.

## Directory-related Operations

### Creating a Directory

#### Method Prototype

You can create a directory under specified bucket via this API. The steps are as follows:

1. Instantiate COSCreateDirCommand object;
2. Call createDirRequest method of COSClient and input COSCreateDirCommand object;
3. Return the result through COSCreatDirTaskRsp object

#### Parameter Description

| Parameter Name   | Type         | Required | Description                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | Yes    | Directory path (relative to bucket path) |
| bucket | NSString * | Yes    | Name of bucket to which a directory belongs     |
| sign   | NSString * | Yes    | Signature                 |
| attrs  | NSString * | No    | Custom attributes            |

#### Returned Result

The result is returned through COSCreatDirTaskRsp object.

| Attribute Name    | Type         | Description     |
| ------- | ---------- | ------ |
| retCode | int        | Task description code |
| descMsg | NSString * | Task description message |

#### Example

```objective-c

	COSCreateDirCommand *cm = [COSCreateDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _sign;
    cm.attrs = @"dirTest";
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
        }else{
			//fail
		}
    };
    [client createDir:cm];
```

### Updating Directory Attributes

#### Method Prototype

You can update the custom attributes of the directory by calling this API. The steps are as follows:

1. Instantiate COSUpdateDirCommand object;
2. Call updateDirRequest method of COSClient and input COSUpdateDirCommand object;
3. Return the result through COSUpdateDirTaskRsp object

#### Parameter Description

| Parameter Name   | Type         | Required | Description                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | Yes    | Directory path (relative to bucket path) |
| bucket | NSString * | Yes    | Name of bucket to which a directory belongs     |
| sign   | NSString * | Yes    | Signature                 |
| attrs  | NSString * | No    | Custom attributes            |

#### Returned Result

The result is returned through COSUpdateDirTaskRsp object.

| Attribute Name    | Type         | Description     |
| ------- | ---------- | ------ |
| retCode | int        | Task description code |
| descMsg | NSString * | Task description message |

#### Example

```objective-c

    COSUpdateDirCommand *cm = [COSUpdateDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _sign;//One-time signature is adopted for this business
    cm.attrs = @"dirTest";
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess
        }else{}
    };
    [client updateDir:cm];
```

### Querying Directory Attributes

#### Method Prototype

You can query the detailed attributes of the directory by calling this API. The steps are as follows:

1. Instantiate COSDirmMetaCommand object;
2. Call getDirMetaData method of COSClient and input COSDirmMetaCommand object;
3. Return the result through COSDirMetaTaskRsp object

#### Parameter Description

| Parameter Name   | Type         | Required | Description                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | Yes    | Directory path (relative to bucket path) |
| bucket | NSString * | Yes    | Name of bucket to which a directory belongs     |
| sign   | NSString * | Yes    | Signature                 |


#### Returned Result

The result is returned through COSDirmMetaCommand object.

| Attribute Name    | Type             | Description     |
| ------- | -------------- | ------ |
| retCode | int            | If the task is normal, return 0; if an error occurs, return other value and the result description |
| descMsg | NSString    *  | If the task is normal, return OK; if an error occurs, return the error description |
| data    | NSDictionary * | Return the task result data |


#### Example

```objective-c

	COSDirmMetaCommand *cm = [COSDirmMetaCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = sign;
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
		}else{}
    };
    [client getDirMetaData:cm];
```

### Deleting a Directory

#### Method Prototype

You can delete a directory under specified bucket by calling this API. But the directory with valid files or directories cannot be deleted. The steps are as follows:

1. Instantiate COSDeleteDirCommand object;
2. Call deleteDirRequest method of COSClient and input COSDeleteDirCommand object;
3. Return the result through COSdeleteDirTaskRsp object


#### Parameter Description

| Parameter Name   | Type         | Required | Description                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | Yes    | Directory path (relative to bucket path) |
| bucket | NSString * | Yes    | Name of bucket to which a directory belongs     |
| sign   | NSString * | Yes    | Signature                 |


#### Returned Result

The result is returned through COSdeleteDirTaskRsp object.

| Attribute Name    | Type            | Description     |
| ------- | ------------- | ------ |
| retCode | int           | Task description code |
| descMsg | NSString    * | Task description message |

#### Example

```objective-c

    COSDeleteDirCommand *cm = [COSDeleteDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _oneSign;//Delete one-time signature
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess;
        }else{}
    };
    [client deleteDir:cm];
```

### List of Directories

#### Method Prototype

You can list files and directories of specified directory under the bucket by calling this API. The steps are as follows:

1. Instantiate COSListDirCommand object;
2. Call listDirRequest method of COSClient and input COSListDirCommand object;
3. Return the result through COSDirListTaskRsp object

#### Parameter Description

| Parameter Name        | Type         | Required | Description                                       |
| ----------- | ---------- | ---- | ---------------------------------------- |
| path        | NSString * | Yes    | Directory path (relative to bucket path)                       |
| bucket      | NSString * | Yes    | Name of bucket to which a directory belongs                           |
| sign        | NSString * | Yes    | Signature                                       |
| num         | NSUInteger | Yes    | Number of each pull                                 |
| pageContext | NSString * | Yes    | Transparently transmitted field. If you want to query the first page, an empty string should be passed. To turn pages, please transmit context in the returned values of the previous page to the parameters in a transparent way |
| prefix      | NSString * | Yes    | Prefix query                                     |

#### Returned Result

The result is returned through TXYListDirCommandRsp object.

| Attribute Name     | Type            | Description       |
| -------- | ------------- | -------- |
| context  | NSString *    | Number of directories     |
| listover | NSString *    | Number of files     |
| infos    | NSArray  *    | List of file directory attributes |
| retCode  | int           | Task description code   |
| descMsg  | NSString    * | Task description message   |

#### Example

```objective-c

    COSListDirCommand *cm = [COSListDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _sign;
    cm.number = 100;
    cm.pageContext = @"";
    cm.prefix = @"xx";
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
          //sucess
        }else{}
    };
    [client listDir:cm];
```


## File-related Operations

### Initialization

#### Method Prototype

Like directory-related operations, file-related operations need first introduce *COSClient .h* header file of upload SDK and instantiate COSClient object.

#### Parameter Description

| Parameter Name   | Type         | Required | Description                                 |
| ------ | ---------- | ---- | ---------------------------------- |
| appId  | NSString * | Yes    | Project ID, i.e. APP ID.                       |
| region | NSString * | Yes    | The data center region where bucket is created. For example, Shanghai: "sh" and Guangzhou: "gz" |

#### Example

```objective-c
- (instancetype)initWithAppId:(NSString*)appId  withRegion:(NSString *)region;
```

### Uploading a File

#### Method Prototype

You can upload local files by calling this API. The steps are as follows:

1. Instantiate COSObjectPutTask;
2. Call putObject method of COSClient and input COSObjectPutTask object;
3. Return the result through COSObjectUploadTaskRsp object

#### Parameter Description

| Parameter Name       | Type         | Required | Description                                   |
| ---------- | ---------- | ---- | ------------------------------------ |
| filePath   | NSString * | Yes    | File path                                 |
| sign       | NSString * | Yes    | Signature                                   |
| bucket     | NSString * | Yes    | Target Bucket name                         |
| fileName   | NSString * | Yes    | The name shown after uploading cos for target files                    |
| attrs      | NSString * | No    | Custom file attributes                              |
| directory  | NSString * | Yes    | File upload directory, relative path, for example "/path"               |
| insertOnly | BOOL       | Yes    | Upload will insert and overwrite the existing files. But if you set "YES", it will not overwrite the previous upload file |

#### Returned Result

Return the result through COSObjectUploadTaskRsp object

| Attribute Name      | Type         | Description                                 |
| --------- | ---------- | ---------------------------------- |
| retCode   | int        | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg   | NSString * | Task description message                             |
| accessURL | NSString * | The CDN url of the file returned by the backend when the task succeeded                |
| sourceURL | NSString * | The origin server URL of the file returned by the backend when the task succeeded                 |

#### Example

```objective-c

    COSObjectPutTask *task = [COSObjectPutTask new];
    task.filePath = path;
    task.fileName = fileName;
    task.bucket = bucket;
    task.attrs = @"customAttribute";
    task.directory = dir;
    task.insertOnly = YES;
    task.sign = _sign;
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
         //sucess
        }else{}
    };
    client.progressHandler = ^(NSInteger bytesWritten,NSInteger totalBytesWritten,NSInteger totalBytesExpectedToWrite){
          //progress
    };
    [client putObject:task];
```

### Updating File Attributes

#### Method Prototype

You can update the custom attributes of the file by calling this API. The steps are as follows:

1. Instantiate COSObjectUpdateCommand;
2. Call updateObject method of COSClient and input COSObjectUpdateCommand object;
3. Return the result through COSObjectUpdateTaskRsp

#### Parameter Description

| Parameter Name     | Type         | Required | Description             |
| -------- | ---------- | ---- | -------------- |
| fileName | NSString * | Yes    |                |
| bucket  | NSString * | Yes    | Name of bucket to which a directory belongs |
| sign     | NSString * | Yes    | Signature             |
| attrs    | NSString * | No    | Custom attributes        |

#### Returned Result

The result is returned through TXYUpdateCommandRsp object.

| Attribute Name    | Type         | Description                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg | NSString * | Task description message                             |

#### Example

```objective-c
    COSObjectUpdateCommand *cm = [COSObjectUpdateCommand new]
	cm.fileName = file;
	cm.bucket = bucket;
	cm.sign = _oneSign;//One-time signature
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
        }else{
    };
    [client updateObject:cm];
```

### Querying File Attributes

#### Method Prototype

You can query the file attributes by calling this API. The steps are as follows:

1. Instantiate COSObjectMetaCommand;
2. Call getObjectInfo method of COSClient and input COSObjectMetaCommand object;
3. Return the result through COSObjectMetaTaskRsp


#### Parameter Description

| Parameter Name      | Type         | Required | Description                 |
| --------- | ---------- | ---- | ------------------ |
| filename  | NSString * | Yes    |                    |
| bucket    | NSString * | Yes    | Name of bucket to which a file belongs     |
| directory | NSString * | Yes    | Directory path (relative to bucket path) |
| sign      | NSString * | Yes    | Signature                 |

#### Returned Result

The result is returned through TXYStatCommandRsp object.

| Attribute Name    | Type             | Description                                 |
| ------- | -------------- | ---------------------------------- |
| retCode | int            | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg | NSString *     | Task description message                             |
| data    | NSDictionary * | File basic information when the task succeeded                          |

#### Example

```objective-c
 
    COSObjectMetaCommand *cm = [COSObjectMetaCommand new] ;
	cm.fileName = file;
	cm.bucket = bucket;
    cm.directory = dir;
	cm.sign = _oneSign;//One-time signature
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
         	//sucess
        }else{}
    };
    [client getObjectMetaData:cm];

```

### Deleting a File

#### Method Prototype

You can delete files by calling this API. The steps are as follows:

1. Instantiate COSObjectDeleteCommand;
2. Call deleteObject method of COSClient and input COSObjectDeleteCommand object;
3. Return the result through COSObjectDeleteTaskRsp

#### Parameter Description

| Parameter Name       | Type            | Required | Description                          |
| ---------- | ------------- | ---- | --------------------------- |
| filename   | NSString *    | Yes    |                             |
| bucket     | NSString *    | Yes    | Name of Bucket to which a file belongs              |
| directory  | NSString *    | Yes    | Directory path (relative to bucket path)          |
| sign       | NSString *    | Yes    | Signature                          |
| objectType | TXYObjectType | Yes    | Content type. Set as TXYObjectFile when deleting files |

#### Returned Result

Returned result via COSObjectDeleteTaskRsp

| Attribute Name    | Type         | Description                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg | NSString * | Task description message                             |

#### Example

```objective-c

    COSObjectDeleteCommand *cm = [COSObjectDeleteCommand new];
	cm.fileName = file;
	cm.bucket = bucket;
    cm.directory = dir;
	cm.sign = _oneSign;//One-time signature
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];;
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess
        }else{        }
    };
    [client deleteObject:cm];
```

### Downloading a File

#### Method Prototype

You can download files by calling this API. The steps are as follows:

1. Instantiate COSObjectGetTask;
2. Call getObjectRequest method of COSClient and input COSObjectGetTask object;
3. Return the result through COSGetObjectTaskRsp object

#### Parameter Description

| Parameter Name     | Type         | Required | Description     |
| -------- | ---------- | ---- | ------ |
| filePath | NSString * | Yes    | File download path |


#### Returned Result

Returned result via COSGetObjectTaskRsp object

| Attribute Name    | Type              | Description                                 |
| ------- | --------------- | ---------------------------------- |
| retCode | int             | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg | NSString *      | Task description message                             |
| object  | NSMutableData * | The download file                               |

#### Example

```objective-c

 	COSObjectGetTask *cm = [[COSObjectGetTask alloc] initWithUrl:imgUrl.text];
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
		//
    };
    client.downloadProgressHandler = ^(int64_t receiveLength,int64_t contentLength){        
    };
    [client getObject:cm];

```

### Uploading a File in Multipart Mode

#### Method Prototype

You can download files by calling this API. The steps are as follows:

1. Instantiate COSObjectPutTask;
2. Call putObject method of COSClient and input COSObjectPutTask object;
3. Return the result through COSObjectUploadTaskRsp object
4. When the "multipartUpload" parameter is set to "YES", the file is uploaded via multipart upload. The default is "NO";

#### Parameter Description

| Parameter Name            | Type         | Required | Description                                   |
| --------------- | ---------- | ---- | ------------------------------------ |
| filePath        | NSString * | Yes    | File path                                 |
| multipartUpload | BOOL       | No    | Indicate whether to use multipart upload for file upload                          |
| sign            | NSString * | Yes    | Signature                                   |
| bucket          | NSString * | Yes    | Target Bucket name                         |
| fileName        | NSString * | Target Bucket name    | The name shown after uploading cos for target files                    |
| attrs           | NSString * | No    | Custom file attributes                              |
| directory       | NSString * | Yes    | File upload directory, relative path, for example "/path"               |
| insertOnly      | BOOL       | Yes    | Upload will insert and overwrite the existing files. But if you set "YES", it will not overwrite the previous upload file |


#### Returned Result

The result is returned through COSObjectUploadTaskRsp object.

| Attribute Name    | Type         | Description                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | Task description code. If retCode >= 0, the task succeeded; if retCode < 0, the task failed |
| descMsg | NSString * | Task description message                             |

#### Example

```objective-c

	COSObjectPutTask *task = [[COSObjectPutTask alloc] init];
	task.multipartUpload = YES;//Multipart upload settings parameters
    task.filePath = path;
    task.fileName = fileName;
    task.bucket = bucket;
    task.attrs = @"customAttribute";
    task.directory = dir;
    task.insertOnly = YES;
    task.sign = _sign;
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];  client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
       
        if (rsp.retCode == 0) {
          //sucess
        }else{ }
    };
    client.progressHandler = ^(NSInteger bytesWritten,NSInteger totalBytesWritten,NSInteger totalBytesExpectedToWrite){
      //Progress
    };
    [client putObject:task];
```


