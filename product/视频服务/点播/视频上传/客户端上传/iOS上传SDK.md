对于在iOS平台上传视频的场景，腾讯云点播提供了iOS上传SDK来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。


## iOS接入

### 集成

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

## 如何上传一个视频

### 使用示例

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

### 接口描述

初始化发布对象TXUGCPublish::initWithUserID

| 参数名称   | 参数描述               | 类型        | 必填   |
| ------ | ------------------ | --------- | ---- |
| userID | 用户userID，用于区分不同的用户 | NSString* | 否    |


发布参数TXPublishParam

| 参数名称         | 参数描述                                     | 类型        | 必填   |
| ------------ | ---------------------------------------- | --------- | ---- |
| signature    | 点播签名 | NSString* | 是    |
| videoPath    | 本地视频文件路径                                 | NSString* | 是    |
| coverImage   | 封面图片，可不设置。不设置SDK会自动截取封面图                 | UIImage*  | 否    |
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

### 如何携带封面

在发布参数中带上封面图片；或者不设置，SDK内部会尝试自动截取封面图。

### 如何取消、恢复上传

取消上传，调用TXUGCPublish的canclePublish()。

```objc
[_videoPublish canclePublish];
```

恢复上传，用相同的发布参数（视频路径和封面路径不变）再调用一次TXUGCPublish的publishVideo。

### 如何断点续传

发布参数中的enableResume，是否开启断点续传。默认是开启的。
在断点续传开启的情况下，只要待上传的文件路径、文件内容没有发生变化，SDK内部会自己实现断点续传，外部不用做特殊处理。
