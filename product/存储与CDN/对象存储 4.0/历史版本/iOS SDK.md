## 温馨提示
请注意这是历史版本（V4，基于 JSON API 封装的 SDK），**已经不再推荐使用**。

对于新接入SDK的用户，我们推荐使用最新的V5版本[基于 XML API 封装的 SDK](https://cloud.tencent.com/document/product/436/11280)。如果因为种种原因确实仍然需要需要使用基于 JSON API 封装的 SDK ,那么推荐使用我们基于历史版本重构后的[基于 JSON API 封装的 SDK](https://github.com/tencentyun/qcloud-sdk-ios/tree/master/QCloudNewCOSV4) 。

## 开发准备

### SDK 获取

对象存储服务的 iOS SDK 的下载地址：[iOS SDK](https://github.com/tencentyun/COS_iOS_SDK.git)
更多示例可参考Demo：[iOS Demo](https://github.com/tencentyun/COS_iOS_SDK.git)
（本版本 SDK 基于 JSON API 封装组成）

### 开发准备

-  iOS 8.0+；
-  手机必须要有网络（GPRS、3G或Wifi网络等）；
-  从控制台获取APP ID、SecretID、SecretKey。


### SDK 配置

#### SDK 导入

##### 使用Cocoapods导入

在Podfile文件中使用：

~~~
pod "QCloudCOSV4"
~~~

##### 使用静态库导入
```
git clone https://github.com/tencentyun/COS_iOS_SDK.git
```

将目录**coslib**下面的文件拖入到工程中即可：

![](https://ws3.sinaimg.cn/large/006tNc79gy1fgm77ref66j30l0094dgv.jpg)


将目录**coslib**下面的文件拖入到工程拖入工程目录，Xcode 会自动将其加入链接库列表中。

并添加以下依赖库：

- CoreTelephony.framework    
- Foundation.framework
- SystemConfiguration.framework

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。

![参数配置](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

在工程info.plist文件中添加App Transport Security Settings 类型，然后在App Transport Security Settings下添加Allow Arbitrary Loads 类型Boolean,值设为YES。

如果想要在程序中使用HTTPS协议，请做如下设置：
```objective-c
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:@"sh";//@“sh”bucket所在机房
[client openHttpsRequest:YES];
```


### 初始化

引入上传 SDK 的头文件 *COSClient .h*，使用目录操作时，需要先实例化 COSClient  对象。

#### 方法原型

```objective-c
- (instancetype)initWithAppId:(NSString*)appId  withRegion:(NSString *)region;
```

#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                                       |
| ------ | ---------- | ---- | ---------------------------------------- |
| appId  | NSString * | 是    | 项目ID，即APP ID。                            |
| region | NSString * | 是    | bucket被创建的时候机房区域，比如华东园区：“sh” ，华南园区："gz"，华北园区："tj" |

#### 示例

```objective-c
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:@“sh”];
```

## 快速入门

这里演示的上传和下载的基本流程，更多细节可以参考demo；在进行这一步之前必须在腾讯云控制台上申请COS业务的appid；

### STEP - 1 初始化COSClient

#### 示例

```objective-c
COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
```

### STEP - 2 上传文件

在这里我们假设您已经申请了自己业务bucket。SDK所有的任务对应了相应的task，只要把相应的task参数传递给client，就可以完成相应的动作；

#### 示例

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

### STEP - 3 下载文件

#### 示例

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

## 生成签名

**签名类型：**

| 类型   | 含义            |
| ---- | ------------- |
| 多次有效 | 有效时间内多次始终有效   |
| 单次有效 | 与资源URL绑定，一次有效 |

**签名获取：**

移动端 SDK 中用到的签名，推荐使用 服务器端SDK，并由移动端向业务服务器请求。

## 目录操作

### 目录创建

#### 方法原型

通过此接口在指定的 bucket 下创建目录，具体步骤如下：

1. 实例化 COSCreateDirCommand  对象；
2. 调用 COSClient 的 createDirRequest 方法，将 COSCreateDirCommand 对象传入。
3. 通过COSCreatDirTaskRsp 的对象返回结果

#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | 是    | 目录路径（相对于bucket的路径） |
| bucket | NSString * | 是    | 目录所属 bucket 名称     |
| sign   | NSString * | 是    | 签名                 |
| attrs  | NSString * | 否    | 用户自定义属性            |

#### 返回结果说明

通过COSCreatDirTaskRsp 的对象返回结果

| 属性名称    | 类型         | 说明     |
| ------- | ---------- | ------ |
| retCode | int        | 任务描述代码 |
| descMsg | NSString * | 任务描述信息 |

#### 示例

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

### 目录属性更新

#### 方法原型

通过调用此接口更新目录的自定义属性，具体步骤如下：

1. 实例化 COSUpdateDirCommand  对象；
2. 调用 COSClient  的 updateDirRequest 方法，将 COSUpdateDirCommand 对象传入；
3. 通过COSUpdateDirTaskRsp 对象返回结果

#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | 是    | 目录路径（相对于bucket的路径） |
| bucket | NSString * | 是    | 目录所属 bucket 名称     |
| sign   | NSString * | 是    | 签名                 |
| attrs  | NSString * | 否    | 用户自定义属性            |

#### 返回结果说明

通过COSUpdateDirTaskRsp 的对象返回结果

| 属性名称    | 类型         | 说明     |
| ------- | ---------- | ------ |
| retCode | int        | 任务描述代码 |
| descMsg | NSString * | 任务描述信息 |

#### 示例

```objective-c

    COSUpdateDirCommand *cm = [COSUpdateDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _sign;//本业务使用一次性签名
    cm.attrs = @"dirTest";
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess
        }else{}
    };
    [client updateDir:cm];
```

### 目录属性查询

#### 方法原型

通过调用此接口来查询目录的详细属性，具体步骤如下：

1. 实例化 COSDirmMetaCommand  对象；
2. 调用 COSClient  的 getDirMetaData 方法，将 COSDirmMetaCommand 对象传入；
3. 通过COSDirMetaTaskRsp的对象返回结果信息；

#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | 是    | 目录路径（相对于bucket的路径） |
| bucket | NSString * | 是    | 目录所属 bucket 名称     |
| sign   | NSString * | 是    | 签名                 |


#### 返回结果说明

通过COSDirmMetaCommand的对象返回结果信息

| 属性名称    | 类型             | 说明     |
| ------- | -------------- | ------ |
| retCode | int            | 任务描述代码 |
| descMsg | NSString    *  | 任务描述信息 |
| data    | NSDictionary * | 任务描述信息 |


#### 示例

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

### 目录删除

#### 方法原型

调用此接口，进行指定 bucket 下目录的删除，如果目录中存在有效文件或目录，将不能删除。具体步骤如下：

1. 实例化 COSDeleteDirCommand  对象；
2. 调用 COSClient  的 deleteDirRequest 命令，传入 COSDeleteDirCommand  对象；
3. 通过COSdeleteDirTaskRsp 的对象返回结果信息


#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                 |
| ------ | ---------- | ---- | ------------------ |
| dir    | NSString * | 是    | 目录路径（相对于bucket的路径） |
| bucket | NSString * | 是    | 目录所属 bucket 名称     |
| sign   | NSString * | 是    | 签名                 |


#### 返回结果说明

通过COSdeleteDirTaskRsp的对象返回结果信息

| 属性名称    | 类型            | 说明     |
| ------- | ------------- | ------ |
| retCode | int           | 任务描述代码 |
| descMsg | NSString    * | 任务描述信息 |

#### 示例

```objective-c

    COSDeleteDirCommand *cm = [COSDeleteDirCommand new];
    cm.directory = dir;
    cm.bucket = bucket;
    cm.sign = _oneSign;//删除使用一次性签名
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess;
        }else{}
    };
    [client deleteDir:cm];
```

### 目录列表

#### 方法原型

调用此接口可以列出 bucket 中，指定目录下的文件、目录信息，具体步骤如下：

1. 实例化 COSListDirCommand 对象；
2. 调用 COSClient 对象的 listDirRequest 方法，将 COSListDirCommand 对象传入;
3. 通过COSDirListTaskRsp 的对象返回结果信息

#### 参数说明

| 参数名称        | 类型         | 是否必填 | 说明                                       |
| ----------- | ---------- | ---- | ---------------------------------------- |
| path        | NSString * | 是    | 目录路径（相对于bucket的路径）                       |
| bucket      | NSString * | 是    | 目录所属 bucket 名称                           |
| sign        | NSString * | 是    | 签名                                       |
| num         | NSUInteger | 是    | 一次拉取数目设定                                 |
| pageContext | NSString * | 是    | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中 |
| prefix      | NSString * | 是    | 前缀查询                                     |

#### 返回结果说明

通过TXYListDirCommandRsp的对象返回结果信息

| 属性名称     | 类型            | 说明       |
| -------- | ------------- | -------- |
| context  | NSString *    | 目录个数     |
| listover | NSString *    | 文件个数     |
| infos    | NSArray  *    | 文件目录属性列表 |
| retCode  | int           | 任务描述代码   |
| descMsg  | NSString    * | 任务描述信息   |

#### 示例

```objective-c

    COSListDirCommand *cm = [COSListDirCommand new]；
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


## 文件操作

### 初始化

#### 方法原型

与目录操作相同，在进行文件操作之前，需引入上传 SDK 的头文件 *COSClient .h*，实例化 COSClient 对象。

#### 参数说明

| 参数名称   | 类型         | 是否必填 | 说明                                 |
| ------ | ---------- | ---- | ---------------------------------- |
| appId  | NSString * | 是    | 项目ID，即APP ID。                      |
| region | NSString * | 是    | bucket被创建的时候机房区域，比如上海：“sh” 广州："gz" |

#### 示例

```objective-c
- (instancetype)initWithAppId:(NSString*)appId  withRegion:(NSString *)region;
```

### 文件上传

#### 方法原型

调用此接口者可进行本地文件上传操作，具体步骤如下：

1. 实例化 COSObjectPutTask ；
2. 调用 COSClient 对象的 putObject 方法，将 COSObjectPutTask  对象传入；
3. 通过COSObjectUploadTaskRsp的对象返回结果信息

#### 参数说明

| 参数名称       | 类型         | 是否必填 | 说明                                   |
| ---------- | ---------- | ---- | ------------------------------------ |
| filePath   | NSString * | 是    | 文件路径                                 |
| sign       | NSString * | 是    | 签名                                   |
| bucket     | NSString * | 是    | 目标 Bucket 名称                         |
| fileName   | NSString * | 是    | 目标 文件上传cos后显示的 名称                    |
| attrs      | NSString * | 否    | 文件自定义属性                              |
| directory  | NSString * | 是    |文件上传目录，相对路径 ,举例:@"path", 注意directory的首尾不要加上多余的/，SDK内部在生成请求URL时会加上/拼成完整的路径。              |


#### 返回结果说明

通过COSObjectUploadTaskRsp的对象返回结果信息

| 属性名称      | 类型         | 说明                                 |
| --------- | ---------- | ---------------------------------- |
| retCode   | int        | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg   | NSString * | 任务描述信息                             |
| sourceURL | NSString * | 成功后，后台返回文件的 CDN url                |
| sourceURL | NSString * | 成功后，后台返回文件的 源站 url                 |

#### 示例

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

### 文件属性更新

#### 方法原型

调用此接口更新文件的自定义属性，具体步骤如下：

1. 实例化 COSObjectUpdateCommand  对象；
2. 调用 COSClient 的 updateObject 命令，传入 COSObjectUpdateCommand   对象；
3. 通过COSObjectUpdateTaskRsp的对象返回结果信息

#### 参数说明

| 参数名称     | 类型         | 是否必填 | 说明             |
| -------- | ---------- | ---- | -------------- |
| fileName | NSString * | 是    |                |
| bucket   | NSString * | 是    | 目录所属 bucket 名称 |
| sign     | NSString * | 是    | 签名             |
| attrs    | NSString * | 否    | 用户自定义属性        |

#### 返回结果说明

通过TXYUpdateCommandRsp的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c
    COSObjectUpdateCommand *cm = [COSObjectUpdateCommand new]
	cm.fileName = file;
	cm.bucket = bucket;
	cm.sign = _oneSign;//单次签名
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
        }else{
    };
    [client updateObject:cm];
```

### 文件属性查询

#### 方法原型

调用此接口可查询文件的属性信息，具体步骤如下：

1. 实例化 COSObjectMetaCommand  对象；
2. 调用 COSClient 的 getObjectInfo 命令，传入 COSObjectMetaCommand   对象；
3. 通过COSObjectMetaTaskRsp 类返回结果信息


#### 参数说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| --------- | ---------- | ---- | ------------------ |
| filename  | NSString * | 是    |                    |
| bucket    | NSString * | 是    | 文件所属 bucket 名称     |
| directory | NSString * | 是    | 目录路径（相对于bucket的路径） |
| sign      | NSString * | 是    | 签名                 |

#### 返回结果说明

通过TXYStatCommandRsp类返回结果信息

| 属性名称    | 类型             | 说明                                 |
| ------- | -------------- | ---------------------------------- |
| retCode | int            | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg | NSString *     | 任务描述信息                             |
| data    | NSDictionary * | 成功时，文件基本信息                         |

#### 示例

```objective-c

    COSObjectMetaCommand *cm = [COSObjectMetaCommand new] ;
	cm.fileName = file;
	cm.bucket = bucket;
    cm.directory = dir;
	cm.sign = _oneSign;//单次签名
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
         	//sucess
        }else{}
    };
    [client getObjectMetaData:cm];

```

### 文件删除

#### 方法原型

调用此接口进行文件的删除操作，具体步骤如下：

1. 实例化 COSObjectDeleteCommand  对象；
2. 调用 COSClient  的 deleteObject 命令，传入 COSObjectDeleteCommand  对象。
3. 通过COSObjectDeleteTaskRsp的对象返回结果信息

#### 参数说明

| 参数名称       | 类型            | 是否必填 | 说明                          |
| ---------- | ------------- | ---- | --------------------------- |
| filename   | NSString *    | 是    |                             |
| bucket     | NSString *    | 是    | 文件所属 Bucket 名称              |
| directory  | NSString *    | 是    | 目录路径（相对于bucket的路径）          |
| sign       | NSString *    | 是    | 签名                          |
| objectType | TXYObjectType | 是    | 业务类型，文件删除时设置为：TXYObjectFile |

#### 返回结果说明

通过COSObjectDeleteTaskRsp的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c

    COSObjectDeleteCommand *cm = [COSObjectDeleteCommand new]；
	cm.fileName = file;
	cm.bucket = bucket;
    cm.directory = dir;
	cm.sign = _oneSign;//单次签名
    COSClient *client= [[COSClient alloc] initWithAppId:appId withRegion:[Congfig instance].region];;
    client.completionHandler = ^(COSTaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess
        }else{        }
    };
    [client deleteObject:cm];
```

### 文件下载

#### 方法原型

调用此接口进行文件的下载操作，具体步骤如下：

1. 实例化 COSObjectGetTask 对象；
2. 调用 COSClient  的 getObjectRequest 命令，传入 COSObjectGetTask  对象。
3. 通过COSGetObjectTaskRsp 的对象返回结果信息

#### 参数说明

| 参数名称     | 类型         | 是否必填 | 说明     |
| -------- | ---------- | ---- | ------ |
| filePath | NSString * | 是    | 文件下载地址 |


#### 返回结果说明

通过 通过COSGetObjectTaskRsp 的对象返回结果信息

| 属性名称    | 类型              | 说明                                 |
| ------- | --------------- | ---------------------------------- |
| retCode | int             | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg | NSString *      | 任务描述信息                             |
| object  | NSMutableData * | 下载文件                               |

#### 示例

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

### 文件分片上传

#### 方法原型

调用此接口进行文件的下载操作，具体步骤如下：

1. 实例化 COSObjectPutTask  对象；
2. 调用 COSClient  的 putObject 命令，传入 COSObjectPutTask   对象。
3. 通过COSObjectUploadTaskRsp  的对象返回结果信息
4. 当multipartUpload 参数设置为YES 的时候上传文件上传的方式为分片上传，该参数默认为NO；

#### 参数说明

| 参数名称            | 类型         | 是否必填 | 说明                                   |
| --------------- | ---------- | ---- | ------------------------------------ |
| filePath        | NSString * | 是    | 文件路径                                 |
| multipartUpload | BOOL       | 否    | 文件上传是否使用分片上传                         |
| sign            | NSString * | 是    | 签名                                   |
| bucket          | NSString * | 是    | 目标 Bucket 名称                         |
| fileName        | NSString * | 是    | 目标 文件上传cos后显示的 名称                    |
| attrs           | NSString * | 否    | 文件自定义属性                              |
| directory       | NSString * | 是    | 文件上传目录，相对路径 ,举例:@"path", 注意directory的首尾不要加上多余的/，SDK内部在生成请求URL时会加上/拼成完整的路径。              |



#### 返回结果说明

通过COSObjectUploadTaskRsp 的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c

	COSObjectPutTask *task = [[COSObjectPutTask alloc] init];
	task.multipartUpload = YES;//分片上传设置参数
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
      //进度
    };
    [client putObject:task];
```
### 文件断点续传

#### 方法原型

调用此接口进行文件的上传操作，具体步骤如下：

1. 实例化 COSObjectPutTask ；
2. 调用 COSClient 对象的 putObject 方法，将 之前上传过的 COSObjectPutTask 对象传入；
3. 通过 COSObjectUploadTaskRsp 的对象返回结果信息

#### 参数说明

| 参数名称       | 类型         | 是否必填 | 说明                                   |
| ---------- | ---------- | ---- | ------------------------------------ |
| filePath   | NSString * | 是    | 文件路径                                 |
| sign       | NSString * | 是    | 签名                                   |
| bucket     | NSString * | 是    | 目标 Bucket 名称                         |
| fileName   | NSString * | 是    | 目标 文件上传cos后显示的 名称                    |
| attrs      | NSString * | 否    | 文件自定义属性                              |
| directory  | NSString * | 是    | 文件上传目录，相对路径 ,举例:@"path", 注意directory的首尾不要加上多余的/，SDK内部在生成请求URL时会加上/拼成完整的路径。               |


#### 返回结果说明

通过COSObjectUploadTaskRsp的对象返回结果信息

| 属性名称      | 类型         | 说明                                 |
| --------- | ---------- | ---------------------------------- |
| retCode   | int        | 任务描述代码，为retCode == 0时标示成功，为负数表示为失败，20000以上的返回码为 SDK 内部错误 |
| descMsg   | NSString * | 任务描述信息                             |
| sourceURL | NSString * | 成功后，后台返回文件的 CDN url                |
| sourceURL | NSString * | 成功后，后台返回文件的 源站 url                 |

#### 示例

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
