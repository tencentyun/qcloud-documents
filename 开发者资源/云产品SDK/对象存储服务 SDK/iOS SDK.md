## 开发准备

### SDK 获取

对象存储服务的 iOS SDK 的下载地址：[iOS SDK](https://mc.qcloudimg.com/static/archive/a78a41f6eb769e421aa41fa607bc1501/qcloud-image-ios-v1.1.4.2.zip) 

更多示例可参考Demo：[iOS Demo](https://mc.qcloudimg.com/static/archive/abdd2f53afdbe005278e9a81d61da6d4/QcloudDemoApp.zip) 

### 开发准备

-  iOS 5.0+；
-  手机必须要有网络（GPRS、3G或Wifi网络等）；
-  从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](https://cloud.tencent.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF)。


### SDK 配置

#### SDK 导入

COS 的 iOS SDK 由上传 SDK 和下载 SDK 两个压缩包组成：

- QCloudUploadSDK.zip
- QCloudDownloadSDK.zip

每个压缩包都包含了一个 .a 静态库和一个包含头文件的文件夹 Headers，如下图所示。上传包提供了支持 bitcode 版本，与不支持 bitcode 版本，可根据业务需要进行选择。

![上传SDK](https://mccdn.qcloud.com/static/img/05f5a1d6768985aa11b23c3808914989/image.png)

![下载SDK](https://mccdn.qcloud.com/static/img/190e5c8c4920ba4d7334f7ba64fd3839/image.png)

将解压后的 QCloudUploadSDK 和 QCloudDownloadSDK 拖入工程目录，Xcode 会自动将其加入链接库列表中。

![导入 SDK 包](https://mccdn.qcloud.com/static/img/96dda4e5f2e4f8fab3fbda3de1cd8e25/image.png)

**注意：**上传/下载SDK包可根据业务需求选择性导入。

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。

![参数配置](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

#### 依赖库添加

在 build Phases -> Link Binary With Libraries 中加入下列依赖库：

- SystemConfiguration.framework
- CoreTelephony.framework

若需要使用上传SDK ，还需加入以下依赖库：

- libstdc++.6.dylib

若需要使用下载 SDK ，还需加入以下依赖库：

- MobileCoreServices.framework
- libxml2.dylib
- libz.dylib



## 签名获取

**签名类型：**

| 类型   | 含义            |
| ---- | ------------- |
| 多次有效 | 有效时间内多次始终有效   |
| 单次有效 | 与资源URL绑定，一次有效 |

**签名获取：**

移动端 SDK 中用到的签名，推荐使用 服务器端SDK，并由移动端向业务服务器请求。SIGN 的具体生成和使用请参照 [访问权限](https://cloud.tencent.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF) 。

## 目录操作

### 初始化

引入上传 SDK 的头文件 *TXYUploadManager.h*，使用目录操作时，需要先实例化 TXYUploadManager 对象。

#### 方法原型

```objective-c
- (instancetype)initWithCloudType:(TXYCloudType)cloudType 
  					persistenceId:(NSString *)persistenceId 
                      		appId:(NSString*)appId;
```

#### 参数说明

| 参数名称          | 类型           | 是否必填 | 说明                                       |
| ------------- | ------------ | ---- | ---------------------------------------- |
| cloudType     | TXYCloudType | 是    | 业务类型，COS服务设置为：TXYCloudTypeForFile        |
| persistenceId | NSString *   | 是    | TXYUploadManager 实例对应的持久化 id，此 id 必须全局唯一，persistenceId 为 nil 时，上传任务不持久化 |
| appId         | NSString *   | 是    | 项目ID，即APP ID。                            |

#### 示例

```objective-c
TXYUploadManager *uploadManager = [[TXYUploadManager alloc] 
                                        initWithCloudType(TXYCloudTypeForFile 
                                            persistenceId:@"qcloudobject" 
                                                    appId:@"10000002")];
```

### 目录创建

通过此接口在指定的 bucket 下创建目录，具体步骤如下：

1. 实例化 TXYCreateDir 对象；
2. 调用 TXYUploadManager 的 sendCommand 方法，将 TXYCreateDir 对象传入。
3. 通过TXYCreateDirCommandRsp的对象返回结果

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path 
                       bucket:(NSString*)bucket 
                         sign:(NSString*)sign 
                needOverWrite:(BOOL)overwrite 
              customAttribute:(NSString*)attrs;
```

#### 参数说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| --------- | ---------- | ---- | ------------------ |
| path      | NSString * | 是    | 目录路径（相对于bucket的路径） |
| bucket    | NSString * | 是    | 目录所属 bucket 名称     |
| sign      | NSString * | 是    | 签名                 |
| overwrite | BOOL       | 是    | 是否覆盖相同名字的目录或文件     |
| attrs     | NSString * | 否    | 用户自定义属性            |

#### 返回结果说明

通过TXYCreateDirCommandRsp的对象返回结果

| 属性名称      | 类型         | 说明       |
| --------- | ---------- | -------- |
| overwrite | BOOL       | 文件是否被覆盖  |
| ctime     | NSInteger  | 文件的创建时间  |
| accessUrl | NSString * | 文件的访问url |

#### 示例

```objective-c
TXYCreateDir *createDirCommand = [[TXYCreateDir alloc] initWithPath(path:DIRPATH 
                                                                  bucket:BUCKETNAME 
                                                                    sing:SIGN 
                                                               overwrite:YES
                                                                   attrs:ATTRS)];

[uploadManager sendCommand:createDirCommand 
				  complete:^(TXYCreateDirCommandRsp *resp) {
								if (resp.retCode >= 0 ) {
									// 创建成功
								} 
								else {
									// 创建失败
								}
							}];
```

### 目录属性更新

通过调用此接口更新目录的自定义属性，具体步骤如下：

1. 实例化 TXYUpdate 对象；
2. 调用 TXYUploadManager 的 sendCommand 方法，将 TXYUpdate 对象传入；
3. 通过TXYUpdateCommandRsp 对象返回结果

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType
				authorityType:(TXYAuthorityType)fileAuthorityType
              customAttribute:(NSString*)attrs;
```

#### 参数说明

| 参数名称              | 类型               | 是否必填 | 说明                                   |
| ----------------- | ---------------- | ---- | ------------------------------------ |
| path              | NSString *       | 是    | 目录路径（相对于bucket的路径）                   |
| bucket            | NSString *       | 是    | 目录所属 bucket 名称                       |
| sign              | NSString *       | 是    | 签名                                   |
| objectType        | TXYObjectType    | 是    | 业务类型，目录属性更新时设置为：TXYObjectDir         |
| fileAuthorityType | TXYAuthorityType | 是    | 文件权限类型，如设置文件权限和bucket相同：eInvalidAuth |
| attrs             | NSString *       | 否    | 用户自定义属性                              |
#### 返回结果说明

通过TXYUpdateCommandRsp 对象返回结果

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c
TXYUpdate *updateDirCommand = [[TXYUpdate alloc] initWithPath:DIRPATH
                                                       bucket:BUCKETNAME
                                                         sign:SIGN
                                                   objectType:TXYObjectDir
												authorityType:eInvalidAuth
                                              customAttribute:ATTRS];

[uploadManager sendCommand: updateDirCommand
				 compelete:^(TXYUpdateCommandRsp *resp) {
								if(resp.retCode >= 0) {
									// 更新成功
								}
								else {
									// 更新失败
								}
							}];
```

### 目录属性查询

通过调用此接口来查询目录的详细属性，具体步骤如下：

1.实例化 TXYStat 对象；
2.调用 TXYUploadManager 的 sendCommand 方法，将 TXYUpdate 对象传入；
3.通过TXYStatCommandRsp的对象返回结果信息；

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType;
```

#### 参数说明

| 参数名称       | 类型            | 是否必填 | 说明                       |
| ---------- | ------------- | ---- | ------------------------ |
| path       | NSString *    | 是    | 目录路径（相对于bucket的路径）       |
| bucket     | NSString *    | 是    | 目录所属 bucket 名称           |
| sign       | NSString *    | 是    | 签名                       |
| objectType | TXYObjectType | 是    | 文件属性查询是，设置为：TXYObjectDir |

#### 返回结果说明

通过TXYStatCommandRsp的对象返回结果信息

| 属性名称        | 类型                | 说明                                 |
| ----------- | ----------------- | ---------------------------------- |
| fileDirInfo | TXYFileDirInfo  * | 单个文件目录信息                           |
| retCode     | int               | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg     | NSString *        | 任务描述信息                             |


#### 示例

```objective-c
TXYStat *statCommand = [[TXYStat alloc] initWithPath:DIRPATH
                                              bucket:BUCKETNAME
                                                sign:SIGN
                                          objectType:TXYObjectDir];

[uploadManager sendCommand: statCommand
				 compelete:^(TXYStatCommandRsp *resp){
								if(resp.retCode >= 0){
									// 查询成功
								}
								else{
									// 查询失败
								}
							}];
```

### 目录删除

调用此接口，进行指定 bucket 下目录的删除，如果目录中存在有效文件或目录，将不能删除。具体步骤如下：

1. 实例化 TXYDelete 对象；
2. 调用 TXYUploadManager 的 SendCommand 命令，传入 TXYDelete 对象；
3. 通过TXYTaskRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType;
```

#### 参数说明

| 参数名称       | 类型            | 是否必填 | 说明                         |
| ---------- | ------------- | ---- | -------------------------- |
| path       | NSString *    | 是    | 目录路径（相对于bucket的路径）         |
| bucket     | NSString *    | 是    | 目录所属 bucket 名称             |
| sign       | NSString *    | 是    | 签名                         |
| objectType | TXYObjectType | 是    | 业务类型，目录删除时设置为：TXYObjectDir |

#### 返回结果说明

通过TXYTaskRsp的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c
TXYDelete *deleteCommand = [[TXYDelete alloc] initWithPath:DIRPATH
                                                    bucket:BUCKETNAME
                                                      sign:SIGN
                                                objectType:TXYObjectDir];

[uploadManager sendCommand: deleteCommand
				 compelete:^(TXYTaskRsp *resp) {
								if(resp.retCode >= 0) {
									// 删除成功
								}
								else {
									// 删除失败
								}
							}];
```

### 列举目录中的文件和目录

调用此接口可以列出 bucket 中，指定目录下的文件、目录信息，具体步骤如下：

1. 实例化 TXYListDir 对象；
2. 调用 TXYUploadManager 对象的 sendCommand 方法，将 TXYListDir 对象传入;
3. 通过TXYListDirCommandRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                       number:(NSUInteger)num
                  listPattern:(TXYListPattern)pattern
                        order:(BOOL)order
                  pageContext:(NSString*)context;
```

#### 参数说明

| 参数名称    | 类型             | 是否必填 | 说明                                       |
| ------- | -------------- | ---- | ---------------------------------------- |
| path    | NSString *     | 是    | 目录路径（相对于bucket的路径）                       |
| bucket  | NSString *     | 是    | 目录所属 bucket 名称                           |
| sign    | NSString *     | 是    | 签名                                       |
| num     | NSUInteger     | 是    | 一次拉取数目设定                                 |
| pattern | TXYListPattern | 是    | 拉取设定：TXYListBoth - 目录和文件都拉取，TXYListDirOnly - 只拉取目录，TXYListFileOnly - 只拉取文件 |
| order   | BOOL           | 是    | 排序设定，0 - 正序 1-反序                         |
| context | NSString*      | 否    | 分页浏览的上下文，第一次拉取时可以为空，后续拉取分页内容时必须填充        |

#### 返回结果说明

通过TXYListDirCommandRsp的对象返回结果信息

| 属性名称            | 类型         | 说明              |
| --------------- | ---------- | --------------- |
| dirCount        | NSUInteger | 目录个数            |
| fileCount       | NSUInteger | 文件个数            |
| fileDirInfoList | NSArray  * | 文件目录属性列表        |
| pageContext     | NSString * | 分页浏览目录的上下文，后台返回 |
| hasMore         | BOOL       | 有无下一页数据         |

#### 示例

```objective-c
// 第一次拉取目录时，context 为空
TXYListDir *listDirCommand = [[TXYListDir alloc] initWithPath:DIRPATH
                                                       bucket:BUCKETNAME
                                                         sign:SIGN
                              					 	      num:10
                                                      pattern:TXYListBoth 
                              					        order:YES
                                                      context:nil];

[uploadManager sendCommand: listDirCommand
				 compelete:^(TXYListDirCommandRsp *resp) {
								if(resp.retCode >= 0) {
									// 拉取成功
								}
								else {
									// 拉取失败
								}
							}];
```

### 列举目录下制定前缀文件&目录

通过此接口查询目录下，指定前缀的文件和目录，具体步骤如下：

1. 实例化 TXYSearch 对象；
2. 调用 TXYUploadManager 对象的 sendCommand 方法，将 TXYSearch 对象传入；
3. 通过TXYSearchCommandRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                       number:(NSUInteger)num
                  pageContext:(NSString*)context;
```

#### 参数说明

| 参数名称    | 类型         | 是否必填 | 说明                                |
| ------- | ---------- | ---- | --------------------------------- |
| path    | NSString * | 是    | 目录路径，前缀查询                         |
| bucket  | NSString * | 是    | 目录所属 bucket 名称                    |
| sign    | NSString * | 是    | 签名                                |
| num     | NSUInteger | 是    | 一次拉取数目设定                          |
| context | NSString*  | 否    | 分页浏览的上下文，第一次拉取时可以为空，后续拉取分页内容时必须填充 |

#### 返回结果说明

通过TXYSearchCommandRsp的对象返回结果信息

| 属性名称            | 类型         | 说明              |
| --------------- | ---------- | --------------- |
| dirCount        | NSUInteger | 目录个数            |
| fileCount       | NSUInteger | 文件个数            |
| fileDirInfoList | NSArray  * | 文件目录属性列表        |
| pageContext     | NSString * | 分页浏览目录的上下文，后台返回 |
| hasMore         | BOOL       | 有无下一页数据         |

#### 示例

```objective-c
// 第一次拉取目录时，context 为空
TXYSearch *listDirCommand = [[TXYSearch alloc] initWithPath:DIRPATH
                                                     bucket:BUCKETNAME
                                                       sign:SIGN
                              					 	    num:10
                                                      context:nil];

[uploadManager sendCommand: listDirCommand
				 compelete:^(TXYSearchCommandRsp *resp) {
								if(resp.retCode >= 0) {
									// 拉取成功
								}
								else {
									// 拉取失败
								}
							}];
```

## 文件操作

### 初始化

与目录操作相同，在进行文件操作之前，需引入上传 SDK 的头文件 *TXYUploadManager.h*，实例化 TXYUploadManager 对象。

#### 方法原型

```objective-c
- (instancetype)initWithCloudType:(TXYCloudType)cloudType
  					persistenceId:(NSString *)persistenceId
                      		appId:(NSString*)appId;
```

#### 参数说明

| 参数名称          | 类型           | 是否必填 | 说明                                       |
| ------------- | ------------ | ---- | ---------------------------------------- |
| cloudType     | TXYCloudType | 是    | 业务类型，COS服务设置为：TXYCloudTypeForFile        |
| persistenceId | NSString *   | 是    | TXYUploadManager 实例对应的持久化id，此id必须全局唯一，persistenceId为nil时，上传任务不持久化 |
| appId         | NSString *   | 是    | 项目ID，即APP ID。                            |

#### 示例

```objective-c
TXYUploadManager *uploadManager = [[TXYUploadManager alloc] 
                                   initWithCloudType:TXYCloudTypeForFile 
                                       persistenceId:@"qcloudobject" 
                                               appId:@"10000002"];
```

### 文件上传

调用此接口者可进行本地文件上传操作，具体步骤如下：

1. 实例化 TXYFileUploadTask对象；
2. 调用 TXYUploadManager 对象的 upload 方法，将 TXYFileUploadTask 对象传入；
3. 通过TXYFileUploadTaskRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype)initWithPath:(NSString *)filePath
                        sign:(NSString*)sign
                      bucket:(NSString *)bucket
					fileName:(NSString *)fileName
             customAttribute:(NSString *)attrs
             uploadDirectory:(NSString*)directory
                  insertOnly:(BOOL)inser;
```

#### 参数说明

| 参数名称       | 类型         | 是否必填 | 说明                                   |
| ---------- | ---------- | ---- | ------------------------------------ |
| filePath   | NSString * | 是    | 文件路径                                 |
| sign       | NSString * | 是    | 签名                                   |
| bucket     | NSString * | 是    | 目标 Bucket 名称                         |
| fileName   | NSString * | 是    | 目标 文件上传cos后显示的 名称                    |
| attrs      | NSString * | 否    | 文件自定义属性                              |
| directory  | NSString * | 是    | 文件上传目录，相对路径 ,举例“/path”               |
| insertOnly | BOOL       | 是    | 上传文件的动作是插入覆盖，举例“YES”  文件不会覆盖之前的上传的文件 |

#### 返回结果说明

通过TXYFileUploadTaskRsp的对象返回结果信息

| 属性名称      | 类型         | 说明                                 |
| --------- | ---------- | ---------------------------------- |
| retCode   | int        | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg   | NSString * | 任务描述信息                             |
| fileURL   | NSString * | 成功后，后台返回文件的 CDN url                |
| fileId    | NSString * | 成功后，后台返回文件的key（cos业务没有fileid）      |
| sourceURL | NSString * | 成功后，后台返回文件的 源站 url                 |

#### 示例

```objective-c
TXYFileUploadTask *fileTask = [[TXYFileUploadTask alloc] initWithPath:FILEPATH
																 sign:SIGN
															   bucket:BUCKETNAME
															 fileName:fileName
                                                      customAttribute:nil
													  uploadDirectory:(NSString*)directory
                                                      insertOnly:YES];

[uploadManager upload:fileTask
			 complete:^(TXYTaskRsp *resp, NSDictionary *context) {
							fileResp = (TXYFileUploadTaskRsp *)resp;
							if(fileResp.retCode >= 0) {
								//上传成功
							}
							else {
								//上传失败
							}
 						}
			 process:^(int64_t totalSize, int64_t sendSize, NSDictionary *context) {
               				// 上传进度
  						}
		 stateChange:^(TXYUploadTaskStat state, NSDictionary *context) {
           					// 上传状态变化
                  		}];
```

### 文件属性更新

调用此接口更新文件的自定义属性，具体步骤如下：

1. 实例化 TXYUpdate 对象；
2. 调用 TXYUploadManager 的 SendCommand 命令，传入 TXYUpdate  对象；
3. 通过TXYUpdateCommandRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType
				authorityType:(TXYAuthorityType)fileAuthorityType
              customAttribute:(NSString*)attrs;
```

#### 参数说明

| 参数名称              | 类型               | 是否必填 | 说明                           |
| ----------------- | ---------------- | ---- | ---------------------------- |
| path              | NSString *       | 是    | 目录路径（相对于bucket的路径）           |
| bucket            | NSString *       | 是    | 目录所属 bucket 名称               |
| sign              | NSString *       | 是    | 签名                           |
| objectType        | TXYObjectType    | 是    | 业务类型，目录属性更新时设置为：TXYObjectDir |
| fileAuthorityType | TXYAuthorityType | 是    | 文件权限类型                       |
| attrs             | NSString *       | 否    | 用户自定义属性                      |

#### 返回结果说明

通过TXYUpdateCommandRsp的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c
TXYUpdate *updateFileCommand = [[TXYUpdate alloc] initWithPath:FILEPATH
                                                        bucket:BUCKETNAME
                                                          sign:SIGN
                                                    objectType:TXYObjectFile
												 authorityType:nil
                                               customAttribute: ATTRS];

[uploadManager sendCommand: updateFileCommand
				 compelete:^(TXYUpdateCommandRsp *resp){
								if(resp.retCode >= 0){
									// 更新成功
								}
								else{
									// 更新失败
								}
							}];
```

### 文件属性查询

调用此接口可查询文件的属性信息，具体步骤如下：

1. 实例化 TXYStat 对象；
2. 调用 TXYUploadManager 的 SendCommand 命令，传入 TXYStat  对象；
3. 通过TXYStatCommandRsp类返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType;
```

#### 参数说明

| 参数名称       | 类型            | 是否必填 | 说明                        |
| ---------- | ------------- | ---- | ------------------------- |
| path       | NSString *    | 是    | 文件路径                      |
| bucket     | NSString *    | 是    | 文件所属 bucket 名称            |
| sign       | NSString *    | 是    | 签名                        |
| objectType | TXYObjectType | 是    | 文件属性查询是，设置为：TXYObjectFile |

#### 返回结果说明

通过TXYStatCommandRsp类返回结果信息

| 属性名称     | 类型            | 说明                                 |
| -------- | ------------- | ---------------------------------- |
| retCode  | int           | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg  | NSString *    | 任务描述信息                             |
| fileInfo | TXYFileInfo * | 成功时，文件基本信息                         |

#### 示例

```objective-c
TXYStat *statCommand = [[TXYStat alloc]initWithPath:FILEPATH
                                             bucket:BUCKETNAME
                                               sign:SIGN
                                         objectType:TXYObjectFile];

[uploadManager sendCommand: statCommand
				 compelete:^(TXYStatCommandRsp *resp){
								if(resp.retCode >= 0){
									// 查询成功
								}
								else{
									// 查询失败
								}
							}];
```

### 文件删除

调用此接口进行文件的删除操作，具体步骤如下：

1. 实例化 TXYDelete 对象；
2. 调用 TXYUploadManager 的 SendCommand 命令，传入 TXYDelete 对象。
3. 通过TXYTaskRsp的对象返回结果信息

#### 方法原型

```objective-c
- (instancetype) initWithPath:(NSString*)path
                       bucket:(NSString*)bucket
                         sign:(NSString*)sign
                   objectType:(TXYObjectType)objectType;
```

#### 参数说明

| 参数名称       | 类型            | 是否必填 | 说明                          |
| ---------- | ------------- | ---- | --------------------------- |
| path       | NSString *    | 是    | 要删除的文件的路径                   |
| bucket     | NSString *    | 是    | 文件所属 Bucket 名称              |
| sign       | NSString *    | 是    | 签名                          |
| objectType | TXYObjectType | 是    | 业务类型，文件删除时设置为：TXYObjectFile |

#### 返回结果说明

通过TXYTaskRsp的对象返回结果信息

| 属性名称    | 类型         | 说明                                 |
| ------- | ---------- | ---------------------------------- |
| retCode | int        | 任务描述代码，为retCode >= 0时标示成功，为负数表示为失败 |
| descMsg | NSString * | 任务描述信息                             |

#### 示例

```objective-c
TXYDelete *deleteCommand = [[TXYDelete alloc]initWithPath:FILEPATH
                                                   bucket:BUCKETNAME
                                                     sign:SIGN
                                               objectType:TXYObjectFile];

[uploadManager sendCommand: deleteCommand
				 compelete:^(TXYTaskRsp *resp){
								if(resp.retCode >= 0){
									// 删除成功
								}
								else{
									// 删除失败
								}
							}];
```

## 对象下载

### 初始化

在下载文件前，需要先实例化下载管理类 TXYDownloader，并对下载器的一些属性进行配置。

#### 方法原型

```objective-c
- (instancetype)initWithPersistenceId:(NSString *)persistenceId 
                                 type:(TXYDownloadType)type;
```

#### 参数说明

| 参数名称          | 类型              | 是否必填 | 说明                                       |
| ------------- | --------------- | ---- | ---------------------------------------- |
| persistenceId | NSString *      | 是    | persistenceId 值不同表示缓存目录不同，为nil内部会自动创建一个缓存目录统一管理 |
| type          | TXYDownloadType | 是    | 下载业务类型，COS服务设置为：TXYDownloadTypeFile      |

 #### 示例

```objective-c
TXYDownloader *downloadManager = [[TXYDownloader alloc] 	 
                            			initWithPersistenceId:@"qcloudobject"
                           					             type:TXYDownloadTypeFile];
```

**下载并发数设置：**可以指定下载器最大并发数。

方法原型：

```objective-c
- (void)setMaxConcurrent:(int)count;
```

示例：

```objective-c
[downloadManager setMaxConcurrent:10];
```

**长连接/断点续传设置：**可以设定是否开启长连接和端点续传功能。

方法原型：

```objective-c
// enable - YES 表示支持断点续传， No 表示不支持断点续传
- (void)enableHTTPRange:(BOOL)enable;
// enable - YES 表示支持 HTTP 长连接， No 表示不支持
- (void)enableKeepAlive:(BOOL)enable;
```

示例：

```objective-c
[downloadManager enableHTTPRange:YES];
[downloadManager enableKeepAlive:YES];
```


### 下载器使用

对已知 URL 的资源进行下载，异步模式进行。

#### 方法原型

```objective-c
- (void)download:(NSString *)url 
          target:(id)target 
       succBlock:(void (^)(NSString *url, NSData *data, NSDictionary *info))succBlock
       failBlock:(void (^)(NSString *url, NSError *error))failBlock 
   progressBlock:(void (^)(NSString *url, NSNumber *value))progressBlock 
           param:(NSDictionary *)param;
```

#### 参数说明

| 参数名称          | 说明                                       |
| ------------- | ---------------------------------------- |
| url           | 资源地址                                     |
| target        | 通知的对象                                    |
| succBlock     | 成功通知                                     |
| failBlock     | 失败通知                                     |
| progressBlock | 进度通知，当前下载百分比                             |
| param         | 可以指定 TXYDownloaderParam 族一系列参数,也可以用于透传使用者的参数 |

#### 返回结果说明

| 参数名称  | 说明          |
| ----- | ----------- |
| url   | 资源地址        |
| data  | 文件数据        |
| info  | 资源相关信息      |
| error | 失败信息        |
| value | 进度通知，当前下载进度 |

#### 示例

```objective-c
[downloadManager download:URL
			      target:self
 		       succBlock:^(NSString *url, NSData *data, NSDictionary *info) {
							// 下载成功
						}
				failBlock:^(NSString *url, NSError *error) {
							// 下载失败
						} 
			progressBlock:^(NSString *url, NSNumber *value) {
							// 下载进度
						} 
					param:nil];
```

### 取消下载

取消对指定URL资源的下载任务，或取消所有下载请求。

#### 方法原型

```objective-c
// 取消 target 对应的下载请求，url 为资源地址
- (void)cancel:(NSString *)url target:(id)target;
// 取消所有的下载请求
- (void)cancelAll;
```

#### 示例

```objective-c
[downloadManager cancel:URL target:self];
[downloadManager cancelAll];
```
