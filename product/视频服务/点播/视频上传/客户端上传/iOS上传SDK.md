对于在 iOS 平台上传视频的场景，腾讯云点播提供了 iOS 上传 DEMO 来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。

## 源代码下载
您可以在腾讯云官网更新 [ iOS 上传 demo + 源代码](http://ugcupload-1252463788.file.myqcloud.com/LiteAVSDK_UGC_Upload_iOS.zip)。
下载完的 zip 包解压后可以看到 TXUGCUploadDemo 目录，发布相关源代码在 TXUGCUploadDemo/upload 目录下。

## 集成上传库和源代码

1. 拷贝上传源代码目录 TXUGCUploadDemo/upload 到您的工程中。
2. 导入动态库QCloudCore.framework、QCloudCOSXML.framework（TXUGCUploadDemo目录下）到您的工程中。并添加以下依赖库：

    ```
    1、CoreTelephony
    2、Foundation
    3、SystemConfiguration
    4、libstdc++.tbd
    ```
    
3. 在 Build Settings 中设置 Other Linker Flags，加入参数***-ObjC***

##  简单视频上传

### 初始化一个上传对象

```objc
TXUGCPublish   *_videoPublish = [[TXUGCPublish alloc] initWithUserID:@"carol_ios"];
```

### 设置上传对象的回调

```objc
_videoPublish.delegate = self;
#pragma mark - TXVideoPublishListener
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes
{
    self.progressView.progress = (float)uploadBytes/totalBytes;
    NSLog(@"onPublishProgress [%lld/%lld]", uploadBytes, totalBytes);
}

-(void) onPublishComplete:(TXPublishResult*)result
{
    NSString *string = [NSString stringWithFormat:@"上传完成，错误码[%d]，信息[%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg];
    [self showErrorMessage:string];
    NSLog(@"onPublishComplete [%d/%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg);
}
```

### 构造上传参数

```objc
TXPublishParam *videoPublishParams = [[TXPublishParam alloc] init];

videoPublishParams.signature  = @"xxx";
videoPublishParams.videoPath  = self.uploadTempFilePath;
```
>signature 计算规则可参考[客户端上传签名](/document/product/266/9221)。

### 调用上传

```objc
[_videoPublish publishVideo:videoPublishParams];
```

## 高级功能
### 携带封面

在上传参数中带上封面图片即可。

```objc
TXPublishParam *videoPublishParams = [[TXPublishParam alloc] init];
videoPublishParams.signature  = @"xxx";
videoPublishParams.coverPath = @"xxx";
videoPublishParams.videoPath  = self.uploadTempFilePath;
```

### 取消、恢复上传

取消上传，调用 `TXUGCPublish`的 `anclePublish()`。

```objc
[_videoPublish canclePublish];
```

恢复上传，用相同的上传参数（视频路径和封面路径不变）再调用一次 `TXUGCPublish` 的 `publishVideo`。

### 断点续传

在视频上传过程中，点播支持断点续传，即当上传意外终止时，用户再次上传该文件，可以从中断处继续上传，减少重复上传时间。断点续传的有效时间是 1 天，即同一个视频上传被中断，那么 1 天内再次上传可以直接从断点处上传，超过 1 天则默认会重新上传完整视频。
上传参数中的 `enableResume` 为断点续传开关，默认是开启的。

## 接口描述

初始化上传对象 `TXUGCPublish::initWithUserID`

| 参数名称   | 参数描述               | 类型        | 必填   |
| ------ | ------------------ | --------- | ---- |
| userID | 用户 userID，用于区分不同的用户 | NSString* | 否    |

上传 `TXUGCPublish.publishVideo`

| 参数名称  | 参数描述 | 类型              | 必填   |
| ----- | ---- | --------------- | ---- |
| param | 发布参数 | TXPublishParam* | 是    |

上传参数 `TXPublishParam`

| 参数名称         | 参数描述                               | 类型        | 必填   |
| ------------ | ---------------------------------- | --------- | ---- |
| signature    | [客户端上传签名](/document/product/266/9221) | NSString* | 是    |
| videoPath    | 本地视频文件路径                           | NSString* | 是    |
| coverPath    | 封面图片本地路径，可不设置。                 | NSString*  | 否    |
| fileName     | 上传到点播系统的视频文件名称，不填默认用本地文件名  | NSString*  | 否    |
| enableResume | 是否启动断点续传，默认开启                  | BOOL      | 否    |
| enableHttps  | 是否启动 HTTPS，默认关闭                    | BOOL      | 否    |


设置上传回调 `TXUGCPublish.delegate`

| 成员变量名称   | 变量描述        | 类型                     | 必填   |
| -------- | ----------- | ---------------------- | ---- |
| delegate | 上传进度和结果回调监听 | TXVideoPublishListener | 是    |


进度回调 `TXVideoPublishListener.onPublishProgress`

| 变量名称        | 变量描述     | 类型        |
| ----------- | -------- | --------- |
| uploadBytes | 已经上传的字节数 | NSInteger |
| totalBytes  | 总字节数     | NSInteger |

结果回调 `TXVideoPublishListener.onPublishComplete`

| 变量名称   | 变量描述 | 类型               |
| ------ | ---- | ---------------- |
| result | 上传结果 | TXPublishResult* |

上传结果 `TXPublishResult`

| 成员变量名称   | 变量说明      | 类型        |
| -------- | --------- | --------- |
| retCode  | 结果码       | int       |
| descMsg  | 上传失败的错误描述 | NSString* |
| videoId  | 点播视频文件Id  | NSString* |
| videoURL | 视频存储地址    | NSString* |
| coverURL | 封面存储地址    | NSString* |


## 错误码

SDK 通过 `TXVideoPublishListener` 接口来监听视频上传相关的状态。因此，可以利用 `TXPublishResult` 中的 `retCode` 来确认视频发布的情况。

| 状态码  | 在 TVCCommon 中所对应的常量           | 含义              |
| :--: | :---------------------------- | :-------------- |
|  0   | TVC_OK                        | 上传成功            |
| 1001 | TVC_ERR_UGC_REQUEST_FAILED    | 请求上传失败，通常是客户端签名过期或者非法，需要 App 重新申请签名         |
| 1002 | TVC_ERR_UGC_PARSE_FAILED      | 请求信息解析失败        |
| 1003 | TVC_ERR_VIDEO_UPLOAD_FAILED   | 上传视频失败          |
| 1004 | TVC_ERR_COVER_UPLOAD_FAILED   | 上传封面失败          |
| 1005 | TVC_ERR_UGC_FINISH_REQ_FAILED | 结束上传请求失败        |
| 1006 | TVC_ERR_UGC_FINISH_RSP_FAILED | 结束上传响应错误        |
| 1008 | TVC_ERR_FILE_NOT_EXIST        | 上传文件不存在         |
| 1012 | TVC_ERR_INVALID_SIGNATURE     | 视频上传 signature 为空 |
| 1013 | TVC_ERR_INVALID_VIDEOPATH     | 视频文件的路径为空       |
| 1017 | TVC_ERR_USER_CANCLE           | 用户调用取消上传        |
