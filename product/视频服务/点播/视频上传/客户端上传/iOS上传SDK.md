对于在iOS平台上传视频的场景，腾讯云点播提供了iOS上传SDK来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。


## 集成

拷贝发布源代码(目录：TXUGCUploadDemo/upload)到您的工程中。

导入COS的动态库QCloudCore.framework、QCloudCOSXML.framework（demo根目录下）到您的工程中。

并添加以下依赖库：

```
1、CoreTelephony
2、Foundation
3、SystemConfiguration
4、libstdc++.tbd
```

在 Build Settings 中设置 Other Linker Flags，加入参数***-ObjC***

##  如何上传一个视频

###  使用示例

初始化一个发布对象

```objc
TXUGCPublish   *_videoPublish = [[TXUGCPublish alloc] initWithUserID:@"carol_ios"];
```

设置发布对象回调代理

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

调用发布

```objc
TXPublishParam *videoPublishParams = [[TXPublishParam alloc] init];
videoPublishParams.signature  = @"xxx";
videoPublishParams.coverImage = nil;
videoPublishParams.videoPath  = self.uploadTempFilePath;
[_videoPublish publishVideo:videoPublishParams];
```

###  接口描述

初始化发布对象TXUGCPublish::initWithUserID

| 参数名称   | 参数描述               | 类型        | 必填   |
| ------ | ------------------ | --------- | ---- |
| userID | 用户userID，用于区分不同的用户 | NSString* | 否    |


发布参数TXPublishParam

| 参数名称         | 参数描述                                     | 类型        | 必填   |
| ------------ | ---------------------------------------- | --------- | ---- |
| signature    | [点播签名](https://www.qcloud.com/document/product/266/9221) | NSString* | 是    |
| videoPath    | 本地视频文件路径                                 | NSString* | 是    |
| coverImage   | 封面图片，可不设置。                               | UIImage*  | 否    |
| enableResume | 是否启动断点续传，默认开启                            | BOOL      | 否    |

### 输出返回

publishVideo参数检查不通过会直接返回非0错误码。错误信息在TXUGCPublish.h中定义

发布进度回调。uploadBytes是上传字节数，totalBytes是总字节数

```objc
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes;
```

发布完成回调。如果成功，会返回视频文件fileid、url等信息；失败则返回失败错误码和错误信息。

```objc
-(void) onPublishComplete:(TXPublishResult*)result;
@interface TXPublishResult : NSObject
@property (nonatomic, assign) int                   retCode;        //错误码
@property (nonatomic, strong) NSString*             descMsg;        //错误描述信息
@property (nonatomic, strong) NSString*             videoId;        //视频文件id
@property (nonatomic, strong) NSString*             videoURL;       //视频播放地址
@property (nonatomic, strong) NSString*             coverURL;       //封面存储地址
@end
```

##  如何携带封面

在发布参数中带上封面图片；或者不设置，SDK内部会尝试自动截取封面图。

##  如何取消、恢复上传

取消上传，调用TXUGCPublish的canclePublish()。

```objc
[_videoPublish canclePublish];
```

恢复上传，用相同的发布参数（视频路径和封面路径不变）再调用一次TXUGCPublish的publishVideo。

##  如何断点续传

发布参数中的enableResume，是否开启断点续传。默认是开启的。
在断点续传开启的情况下，只要待上传的文件路径、文件内容没有发生变化，SDK内部会自己实现断点续传，外部不用做特殊处理。

断点续传是基于cos的分片上传实现的，cos的分片上传分为三个步骤：初始化分片上传->上传分片->上传完成。初始化上传会返回一个唯一的描述符（uploadId），后续的分片上传和上传完成都需要带上这个uploadId，同时cos还支持根据uploadId列出已经上传的分片信息。
断点续传内部实现：以文件路径作为关键字，缓存点播vodSessionKey(用于去点播后台获取上次上传的cos路径)和cos的uploadId。上传文件的时候根据缓存是否存在判断文件是不是上传过，如果是则走断点续传。缓存有效期1天。
需要注意：cos不会做文件一致性的检测，SDK根据文件最后修改时间做文件一致性检测。

![](https://mc.qcloudimg.com/static/img/9532c4abaf9b916505f0d69335452984/image.png)

## 错误码

SDK 通过 TXVideoPublishListener 接口来监听短视频发布相关的状态。因此，可以利用 TXPublishResult 中的 **retCode ** 来确认视频发布的情况。

| 状态码  | 在 TVCCommon 中所对应的常量           | 含义              |
| :--: | :---------------------------- | :-------------- |
|  0   | TVC_OK                        | 发布成功            |
| 1001 | TVC_ERR_UGC_REQUEST_FAILED    | 请求上传失败          |
| 1002 | TVC_ERR_UGC_PARSE_FAILED      | 请求信息解析失败        |
| 1003 | TVC_ERR_VIDEO_UPLOAD_FAILED   | 上传视频失败          |
| 1004 | TVC_ERR_COVER_UPLOAD_FAILED   | 上传封面失败          |
| 1005 | TVC_ERR_UGC_FINISH_REQ_FAILED | 结束上传请求失败        |
| 1006 | TVC_ERR_UGC_FINISH_RSP_FAILED | 结束上传响应错误        |
| 1008 | TVC_ERR_FILE_NOT_EXIST        | 上传文件不存在         |
| 1012 | TVC_ERR_INVALID_SIGNATURE     | 视频上传signature为空 |
| 1013 | TVC_ERR_INVALID_VIDEOPATH     | 视频文件的路径为空       |
| 1017 | TVC_ERR_USER_CANCLE           | 用户调用取消上传        |

1003和1004是cos上传失败了，详细的错误信息会在log里打印出来，可以查阅[COS错误码](https://cloud.tencent.com/document/product/436/7730)。

##  FAQ

### 上传后如何处理视频？
### 服务器如何知道追踪用户上传
### 如何就近上传？