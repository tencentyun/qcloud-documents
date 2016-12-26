## 开发准备

### SDK 获取

对象存储服务的 iOS SDK 的下载地址：[iOS SDK](https://mc.qcloudimg.com/static/archive/a78a41f6eb769e421aa41fa607bc1501/qcloud-image-ios-v1.1.4.2.zip) 

更多示例可参考Demo：[iOS Demo](https://mc.qcloudimg.com/static/archive/abdd2f53afdbe005278e9a81d61da6d4/QcloudDemoApp.zip) 

### 开发准备

-  iOS 8.0+；
-  手机必须要有网络（GPRS、3G或Wifi网络等）；
-  从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](https://www.qcloud.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF)。


### SDK 配置

#### SDK 导入

CI 的 iOS SDK压缩包组成：

- CIClientSDK.zip

压缩包中都包含了一个 .a 静态库和一个包含头文件的文件夹 Headers，如下图所示。上传包提供了支持 bitcode 版本，与不支持 bitcode 版本，可根据业务需要进行选择。

![上传SDK](https://mccdn.qcloud.com/static/img/05f5a1d6768985aa11b23c3808914989/image.png)

![下载SDK](https://mccdn.qcloud.com/static/img/190e5c8c4920ba4d7334f7ba64fd3839/image.png)

将解压后的 CISDK 拖入工程目录，Xcode 会自动将其加入链接库列表中。

![导入 SDK 包](https://mccdn.qcloud.com/static/img/96dda4e5f2e4f8fab3fbda3de1cd8e25/image.png)

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 -ObjC。

![参数配置](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

在工程info.plist文件中添加App Transport Security Settings 类型，然后在App Transport Security Settings下添加Allow Arbitrary Loads 类型Boolean,值设为YES

## 签名获取

**签名类型：**

| 类型   | 含义            |
| ---- | ------------- |
| 多次有效 | 有效时间内多次始终有效   |
| 单次有效 | 与资源URL绑定，一次有效 |

**签名获取：**

移动端 SDK 中用到的签名，推荐使用 服务器端SDK，并由移动端向业务服务器请求。SIGN 的具体生成和使用请参照 [访问权限](https://www.qcloud.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF) 。


## 初始化

引入上传 SDK 的头文件 *CIClient .h*，使用目录操作时，需要先实例化 CIClient  对象。

#### 方法原型

```objective-c
- (instancetype)initWithAppId:(NSString*)appId ;
```

#### 参数说明

| 参数名称          | 类型           | 是否必填 | 说明                                       |
| ------------- | ------------ | ---- | ---------------------------------------- |
| appId         | NSString *   | 是    | 项目ID，即APP ID。                            		|


#### 示例

```objective-c
CIClient *client= [[CIClient alloc] initWithAppId:appId];
```


## 快速入门

这里演示的对比身份证照片的基本流程，更多细节可以参考demo；在进行这一步之前必须在腾讯云控制台上申请万象业务的appid；

### STEP - 1初始化CIClient

#### 示例

```objective-c
CIClient *client= [[CIClient alloc] initWithAppId:appId];
```
### STEP - 2 初始化对比身份证照片的task

在这里我们假设您已经申请了自己业务bucket。SDK所有的任务对应了相应的task，只要把相应的task参数传递给client，就可以完成相应的动作；这里以创建人任务来演示

#### 示例

```objective-c

    CIIDCardCompareTask *task = [CIIDCardCompareTask new];
    task.filePath = path;
    task.bucket = bucket;
    task.idcardNumber = number;
    task.idcardName = name;
    task.sign = _sign;
    CIClient *client= [[CIClient alloc] initWithAppId:appId];
    client.completionHandler = ^(CIITaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
         //sucess
        }else{}
    };
    client.progressHandler = ^(NSInteger bytesWritten,NSInteger totalBytesWritten,NSInteger totalBytesExpectedToWrite){
          //progress
    };
    [client IDCardCompare:task]；
```

###  对比身份证照片

自带人脸识别数据库，可实时为国内公民提供在线的身份证照片比对，具体步骤如下：

1. 实例化 CIIDCardCompareTask  对象；
2. 调用 CIClient 的 IDCardCompare 方法，将 CIIDCardCompareTask 对象传入。
3. 通过CITaskRsp 的对象返回结果

#### CIICreatPersonTask的属性说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| ----------- | ---------- | ---- | ------------------ |
| filePath         | NSString * | 是    | 图片的路径 |
| photoUrl         | NSString * | 是    | 图片的url, filePath和photoUrl只提供一个即可,如果都提供,只使用url |
| idcardNumber  	  | NSString * | 是    | 用户身份证号码          |
| idcardName  	  | NSString * | 否    | 用户身份证姓名            |
| bucket      | NSString * | 是    | 目录所属 bucket 名称     |
| sign        | NSString * | 是    | 签名                 |
| sessionId  	  | NSString * | 否    | 相应请求的session标识符，可用于结果查            |

#### 返回结果说明

通过CITaskRsp 的对象返回结果

| 属性名称      | 类型         | 说明       |
| --------- | ---------- | -------- |
| retCode 	| 	 int    | 任务描述代码  |
| descMsg   | NSString *| 任务描述信息  |
| data   | NSDictionary *| 任务请求返回数据  |

#### 示例

```objective-c

  CIIDCardCompareTask *cm = [CIIDCardCompareTask new];
    task.filePath = path;
    task.bucket = bucket;
    task.idcardNumber = number;
    task.idcardName = name;
    task.sign = _sign;
    CIClient *client= [[CIClient alloc] initWithAppId:appId ];
    client.completionHandler = ^(CIITaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
        }else{
			//fail
		}
    };
    [client IDCardCompare:cm];
```

### 获取唇语

通过调用此接口获取一个唇语验证字符串，用于用户录制视频时使用，具体步骤如下：

1. 实例化 CIGetLipIdentificationStringTask  对象；
2. 调用 CIClient  的 getLipIdentificationString 方法，将 CIGetLipIdentificationStringTask 对象传入；
3. 通过CITaskRsp 对象返回结果

#### CIGetLipIdentificationStringTask参数说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| ----------- | ---------- | ---- | ------------------ |
| seq         | NSString * | 否    | 标识请求序列号|
| bucket      | NSString * | 是    | 目录所属 bucket 名称     |
| sign        | NSString * | 是    | 签名                 |

#### 返回结果说明

通过CITaskRsp 的对象返回结果

| 属性名称      | 类型         | 说明       |
| --------- | ---------- | -------- |
| retCode 	| 	 int    | 任务描述代码  |
| descMsg   | NSString *| 任务描述信息  |          
| data   | NSDictionary *| 任务请求返回数据  |                

#### 示例

```objective-c

    CIIDCardCompareTask *cm = [CIIDCardCompareTask new];
    cm.bucket = bucket;
    cm.sign = _sign;/
    CIClient *client= [[CIClient alloc] initWithAppId:appId];
    client.completionHandler = ^(CIITaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess
        }else{}
    };
    [client getLipIdentificationString:cm];
```

###  人脸核身验证

通过调用此接口根据用户上传的照片和视频，进行人脸核身验证，具体步骤如下：

1.实例化 CILipIdentificationCompareTask  对象；
2.调用 CIClient  的 lipIdentificationCompare 方法，将 CILipIdentificationCompareTask 对象传入；
3.通过CITaskRsp的对象返回结果信息；

#### CILipIdentificationCompareTask参数说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| ----------- | ---------- | ---- | ------------------ |
| videoPath         | NSString * | 是    | 视频的路径 |
| photoPath         | NSString * | 是    | 与视频对比的图片 |
| validate  	  | NSString * | 是    | 执行CIGetLipIdentificationStringTask 返回的唇语验证数据         |
| bucket      | NSString * | 是    | 目录所属 bucket 名称     |
| sign        | NSString * | 是    | 签名                 |
| compareFlag  	  | NSString * | 否    | 录制的视频是否和图片作对比，yes 是对比，no 不做对比           |
| seq        | NSString * | 是    | 相应请求的session标识符，可用于结果查             |


#### 返回结果说明

通过CIITaskRsp的对象返回结果信息

| 属性名称      | 类型         | 说明       |
| --------- | ---------- | -------- |
| retCode 	| 	   int       | 任务描述代码  |
| descMsg   | 	NSString    *| 任务描述信息  |    
| data	    |  NSDictionary *| 任务返回业务信息 |     


#### 示例

```objective-c

  CILipIdentificationCompareTask *cm = [CILipIdentificationCompareTask new];
    cm.videoPath = path;
    cm.validate= validate;
    cm.compareFlag= flag;  
    cm.bucket = bucket;
    cm.sign = sign;
    CIClient *client= [[CIClient alloc] initWithAppId:appId];
    client.completionHandler = ^(CIITaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
			//sucess
		}else{}
    };
    [client lipIdentificationCompare:cm];
```

### 高清身份证照片比对

调用此接口自可实时为国内公民提供在线的身份证照片比对。根据用户的身份证号、姓名，与用户上传的图像进行人脸相似度对比。具体步骤如下：

1. 实例化 CIIDNumbeVideoComparTask  对象；
2. 调用 CIClient  的 IDCardCompareVideo 命令，传入 CIIDNumbeVideoComparTask  对象；
3. 通过CITaskRsp 的对象返回结果信息


#### CIIDNumbeVideoComparTask 参数说明

| 参数名称      | 类型         | 是否必填 | 说明                 |
| ----------- | ---------- | ---- | ------------------ |
| videoPath         | NSString * | 是    | 视频的路径 |
| validate  	  | NSString * | 是    | 执行CIGetLipIdentificationStringTask 返回的唇语验证数据         |
| idcardNumber  	  | NSString * | 是    | 用户身份证号码          |
| idcardName  	  | NSString * | 否    | 用户身份证姓名            |
| faceList         | NSArray * | 是    | 删除人脸id的列表） |
| bucket      | NSString * | 是    | 目录所属 bucket 名称     |
| sign        | NSString * | 是    | 签名                 |
| seq        | NSString * | 是    | 相应请求的session标识符，可用于结果查        


#### 返回结果说明

通过CITaskRsp的对象返回结果信息

| 属性名称      | 类型         | 说明       |
| --------- | ---------- | -------- |
| retCode 	| 	   int       | 任务描述代码  |
| descMsg   | 	NSString    *| 任务描述信息  |    
| data	    |  NSDictionary *| 任务返回业务信息 |  

#### 示例

```objective-c

    CIIDNumbeVideoComparTask *cm = [CIIDNumbeVideoComparTask new];
    cm.videoPath = path;
    cm.validate= validate;
    cm.compareFlag= flag;  
    cm.bucket = bucket;
    cm.sign = sign;

    CIClient *client= [[CIClient alloc] initWithAppId:appId];
    client.completionHandler = ^(CIITaskRsp *resp, NSDictionary *context){
        if (resp.retCode == 0) {
            //sucess;
        }else{}
    };
    [client IDCardCompareVideo:cm];
```
