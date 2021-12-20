对于在 iOS 平台上传视频的场景，云点播提供了 iOS 上传 SDK 。上传流程请参见 [客户端上传指引](/document/product/266/9219)。

## 源码下载
1. [单击下载](https://liteav.sdk.qcloud.com/download/ugc/LiteAVSDK_UGC_Upload_iOS.zip) iOS 上传 Demo 及源码。
2. 将下载好的压缩包解压，可以看到 TXUGCUploadDemo 目录，上传源码在`TXUGCUploadDemo/upload`目录下。

## 集成上传库和源码

1. 拷贝上传源码目录`TXUGCUploadDemo/upload`到您的工程中。
2. 导入动态库`QCloudCore.framework`、`QCloudCOSXML.framework`和静态库`libmtasdk.a`（在`TXUGCUploadDemo/upload/COSSDK/`目录下）到您的工程中，并添加以下依赖库：
    ```
    1. CoreTelephony.framework
    2. Foundation.framework
    3. SystemConfiguration.framework
    4. libc++.tbd
    ``` 
3. 在 Build Settings 中设置 Other Linker Flags，加入参数`-ObjC`。

##  简单视频上传

#### 初始化上传对象

```objc
TXUGCPublish *_videoPublish = [[TXUGCPublish alloc] initWithUserID:@"upload_video_userid"];
```

#### 设置上传对象回调

```objc
_videoPublish.delegate = self;
```

```objc
#pragma mark - TXVideoPublishListener

- (void)onPublishProgress:(NSInteger)uploadBytes totalBytes:(NSInteger)totalBytes {
    self.progressView.progress = (float)uploadBytes/totalBytes;
    NSLog(@"onPublishProgress [%ld/%ld]", uploadBytes, totalBytes);
}

- (void)onPublishComplete:(TXPublishResult*)result {
    NSString *string = [NSString stringWithFormat:@"上传完成，错误码[%d]，信息[%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg];
    [self showErrorMessage:string];
    NSLog(@"onPublishComplete [%d/%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg);
}
```

#### 构造上传参数

```objc
TXPublishParam *publishParam = [[TXPublishParam alloc] init];

publishParam.signature  = @"由您业务后台产生的签名";
publishParam.videoPath  = @"视频文件路径";
```
`signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

#### 调用上传

```objc
[_videoPublish publishVideo:publishParam];
```
>?
>- 上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。
>- 如需上传至指定子应用下，请参见 [子应用体系 - 客户端上传](https://cloud.tencent.com/document/product/266/14574#.E5.AE.A2.E6.88.B7.E7.AB.AF.E4.B8.8A.E4.BC.A0)。

## 高级功能
#### 携带封面

在上传参数中带上封面图片即可。

```objc
TXPublishParam *publishParam = [[TXPublishParam alloc] init];
publishParam.signature  = @"由您业务后台产生的签名";
publishParam.coverPath = @"封面图片文件路径";
publishParam.videoPath  = @"视频文件路径";
```

#### 取消和恢复上传

取消上传，调用`canclePublish`接口。

```objc
[_videoPublish canclePublish];
```

恢复上传，用相同的上传参数（视频路径和封面路径不变），再调用一次`TXUGCPublish`的`publishVideo`。

#### 断点续传

在视频上传过程中，云点播支持断点续传，即当上传意外终止时，用户再次上传该文件，可以从中断处继续上传，减少重复上传时间。

断点续传的有效时间是1天，即同一个视频上传被中断，那么1天内再次上传可以直接从断点处上传，超过1天默认会重新上传完整视频。

上传参数中的`enableResume`为断点续传开关，默认是开启的。


## 图片和媒体上传

```objc
// 创建对象
TXUGCPublish *_imagePublish = [[TXUGCPublish alloc] initWithUserID:@"upload_image_userid"];

// 设置回调
_imagePublish.mediaDelegate = self;

// 构造上传参数
TXMediaPublishParam *publishParam = [[TXMediaPublishParam alloc] init];
publishParam.signature  = @"由您业务后台产生的签名";
publishParam.mediaPath = @"图片文件路径";

// 上传图片或媒体文件
[_imagePublish publishMedia:publishParam];

```


## 视频上传接口描述

初始化上传对象：`TXUGCPublish::initWithUserID`

| 参数名称   | 参数描述               | 类型        | 必填   |
| ------ | ------------------ | --------- | ---- |
| userID | 用户 userID，用于区分不同的用户。 | NSString | 否    |

开始上传：`TXUGCPublish.publishVideo`

| 参数名称  | 参数描述 | 类型              | 必填   |
| ----- | ---- | --------------- | ---- |
| param | 发布参数。 | TXPublishParam | 是    |

上传参数：`TXPublishParam`

| 参数名称         | 参数描述                               | 类型        | 必填   |
| ------------ | ---------------------------------- | --------- | ---- |
| signature    | [客户端上传签名](/document/product/266/9221)。 | NSString* | 是    |
| videoPath    | 本地视频文件路径。                           | NSString* | 是    |
| coverPath    | 封面图片本地路径，可不设置。                 | NSString*  | 否    |
| fileName     | 上传到腾讯云的视频文件名称，不填默认用本地文件名。  | NSString*  | 否    |
| enableResume | 是否启动断点续传，默认开启。                  | BOOL      | 否    |
| enableHttps  | 是否启动 HTTPS，默认关闭。                    | BOOL      | 否    |


设置上传回调：`TXUGCPublish.delegate`

| 成员变量名称   | 变量描述        | 类型                     | 必填   |
| -------- | ----------- | ---------------------- | ---- |
| delegate | 上传进度和结果回调监听。 | TXVideoPublishListener | 是    |


上传进度回调：`onPublishProgress`

| 变量名称        | 变量描述     | 类型        |
| ----------- | -------- | --------- |
| uploadBytes | 已经上传的字节数。 | NSInteger |
| totalBytes  | 总字节数。     | NSInteger |

上传结果回调：`onPublishComplete`

| 变量名称   | 变量描述 | 类型               |
| ------ | ---- | ---------------- |
| result | 上传结果。 | TXPublishResult |

上传事件回调：`onPublishEvent`

| 变量名称   | 变量描述 | 类型               |
| ------ | ---- | ---------------- |
| evt | 事件，用于调试打印。 | NSDictionary |

上传结果：`TXPublishResult`

| 成员变量名称   | 变量说明      | 类型        |
| -------- | --------- | --------- |
| retCode  | 错误码。       | int       |
| descMsg  | 上传失败的错误描述。 | NSString |
| videoId  | 点播视频文件 ID。  | NSString |
| videoURL | 视频存储地址。    | NSString |
| coverURL | 封面存储地址。    | NSString |

预上传：`TXUGCPublishOptCenter.prepareUpload`
    
| 参数名称  | 参数描述                                     | 类型   | 必填 |
| --------- | -------------------------------------------- | ------ | ---- |
| signature | [客户端上传签名](/document/product/266/9221)。 | NSString | 是   |


#### 错误码

SDK 通过`TXVideoPublishListener`接口来监听视频上传相关的状态。因此，可以用`TXPublishResult`中的`retCode`来确认视频发布的情况。

| 错误码  | 在 TVCCommon 中所对应的常量           | 含义              |
| :--: | :---------------------------- | :-------------- |
|  0   | TVC_OK                        | 上传成功。            |
| 1001 | TVC_ERR_UGC_REQUEST_FAILED    | 请求上传失败，通常是客户端签名过期或者非法，需要 App 重新申请签名。         |
| 1002 | TVC_ERR_UGC_PARSE_FAILED      | 请求信息解析失败。        |
| 1003 | TVC_ERR_VIDEO_UPLOAD_FAILED   | 上传视频失败。          |
| 1004 | TVC_ERR_COVER_UPLOAD_FAILED   | 上传封面失败。          |
| 1005 | TVC_ERR_UGC_FINISH_REQ_FAILED | 结束上传请求失败。        |
| 1006 | TVC_ERR_UGC_FINISH_RSP_FAILED | 结束上传响应错误。        |



## 图片和媒体上传接口描述

初始化上传对象：`TXUGCPublish::initWithUserID`

| 参数名称   | 参数描述               | 类型        | 必填   |
| ------ | ------------------ | --------- | ---- |
| userID | 用户 userID，用于区分不同的用户。 | NSString | 否    |

开始上传：`TXUGCPublish.publishMedia`

| 参数名称  | 参数描述 | 类型              | 必填   |
| ----- | ---- | --------------- | ---- |
| param | 发布参数。 | TXMediaPublishParam | 是    |

上传参数：`TXMediaPublishParam`

| 参数名称         | 参数描述                               | 类型        | 必填   |
| ------------ | ---------------------------------- | --------- | ---- |
| signature    | [客户端上传签名](https://cloud.tencent.com/document/product/266/9221)。 | NSString* | 是    |
| mediaPath    | 本地图片/媒体文件路径。                           | NSString* | 是    |
| fileName     | 上传到腾讯云的图片/媒体文件名称，不填默认用本地文件名。  | NSString*  | 否    |
| enableResume | 是否启动断点续传，默认开启。                  | BOOL      | 否    |
| enableHttps  | 是否启动 HTTPS，默认关闭。                    | BOOL      | 否    |


设置上传回调：`TXUGCPublish.TXMediaPublishListener`

| 成员变量名称   | 变量描述        | 类型                     | 必填   |
| -------- | ----------- | ---------------------- | ---- |
| mediaDelegate | 上传进度和结果回调监听。 | TXMediaPublishListener | 是    |


上传进度回调：`onMediaPublishProgress`

| 变量名称        | 变量描述     | 类型        |
| ----------- | -------- | --------- |
| uploadBytes | 已上传的字节数。 | NSInteger |
| totalBytes  | 总字节数。     | NSInteger |

上传结果回调：`onMediaPublishComplete`

| 变量名称   | 变量描述 | 类型               |
| ------ | ---- | ---------------- |
| result | 上传结果。 | TXMediaPublishResult |

上传事件回调：`onMediaPublishEvent`

| 变量名称   | 变量描述 | 类型               |
| ------ | ---- | ---------------- |
| evt | 事件，用于调试打印。 | NSDictionary |

上传结果：`TXMediaPublishResult`

| 成员变量名称   | 变量说明      | 类型        |
| -------- | --------- | --------- |
| retCode  | 错误码。       | int       |
| descMsg  | 上传失败的错误描述。 | NSString |
| mediaId  | 图片/媒体文件 ID。  | NSString |
| mediaURL | 图片/媒体存储地址。    | NSString |

预上传：`TXUGCPublishOptCenter.prepareUpload`
    
| 参数名称  | 参数描述                                     | 类型   | 必填 |
| --------- | -------------------------------------------- | ------ | ---- |
| signature | [客户端上传签名](/document/product/266/9221)。 | NSString | 是   |


#### 错误码

SDK 通过`TXMediaPublishListener`接口来监听图片/媒体上传相关的状态。因此，可以用`TXMediaPublishResult`中的`retCode`来确认图片/媒体发布的情况。

| 错误码  | 在 TVCCommon 中所对应的常量           | 含义              |
| :--: | :---------------------------- | :-------------- |
|  0   | MEDIA_PUBLISH_RESULT_OK                        | 上传成功。            |
| 1001 | MEDIA_PUBLISH_RESULT_UPLOAD_REQUEST_FAILED    | 请求上传失败，通常是客户端签名过期或者非法，需要 App 重新申请签名。         |
| 1002 | MEDIA_PUBLISH_RESULT_UPLOAD_RESPONSE_ERROR      | 请求信息解析失败。        |
| 1003 | MEDIA_PUBLISH_RESULT_UPLOAD_VIDEO_FAILED   | 上传图片/媒体失败。          |
| 1005 | MEDIA_PUBLISH_RESULT_PUBLISH_REQUEST_FAILED | 结束上传请求失败。        |
| 1006 | MEDIA_PUBLISH_RESULT_PUBLISH_RESPONSE_ERROR | 结束上传响应错误。        |





