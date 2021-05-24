智能扫码的 API 主要涉及 QBarCodeKit 对象，下面对其支持的 API 作出说明。

### QBarCodeKit

| API                                                          | 功能描述                                   |
| ------------------------------------------------------------ | ------------------------------------------ |
| [sharedInstance](#sharedInstance)                            | 获得 QBarCodeKit 的单例对象                  |
| [getVersion](#getVersion)                                    | 获得 SDK 的版本信息                          |
| [initQBarCodeKit](#initQBarCodeKit)                          | 初始化 SDK，并完成鉴权认证                  |
| [decodeImageWithQBar](#decodeImageWithQBar)                  | 可以识别传入图片中存在的二维码、条形码信息 |
| [qBarDecodingWithSampleBuffer](#qBarDecodingWithSampleBuffer) | 通过摄像头拍摄流进行二维码扫描             |
| [startDefaultQBarScan](#startDefaultQBarScan)                | 启动 SDK 提供的默认界面进行扫码              |
| [setViewConfig](#setViewConfig)                              | 设置界面配置信息                           |

<span id="sharedInstance"></span>
#### sharedInstance

```objective-c
+ (instancetype) sharedInstance 
```

功能描述：

获得 QBarCodeKit 的单例对象静态方法。

返回结果：

QBarCodeKit 的单例对象。


<span id="getVersion"></span>
#### getVersion

```objective-c
- (NSString *) getVersion 
```

功能描述：

获得 SDK 的版本信息。

返回结果：

当前 SDK 的版本信息。


<span id="initQBarCodeKit"></span>
#### initQBarCodeKit

```objective-c
- (void) initQBarCodeKit:(NSString *)secretId secretKey:(NSString *)secretkey teamId:(NSString *)teamId resultHandle:(resultCodeContent)handle 
```

功能描述：

初始化 SDK，并完成鉴权认证。

传入参数：

**secretId** 用户在后台申请的 secretId 信息

**secretkey** 用户在后台申请后获取的专属密钥信息

**teamId** 用户申请所填写的 development team id

**handle** 用于接收初始化与鉴权认证的结果回调，并将结果放到 [resultCodeContent](#resultCodeContent) 中


<span id="decodeImageWithQBar"></span>
#### decodeImageWithQBar

```objective-c
- (void) decodeImageWithQBar:(UIImage *)image resultHandler:(resultCodeContent)handle
```

功能描述：

可以识别传入图片中存在的二维码、条形码信息。

传入参数：

**image** 需要识别的图像信息

**handle** 用于图像识别的结果回调，并将结果放到 [resultCodeContent](#resultCodeContent) 中


<span id="qBarDecodingWithSampleBuffer"></span>
#### qBarDecodingWithSampleBuffer

```objective-c
- (void) qBarDecodingWithSampleBuffer:(CMSampleBufferRef) sampleBuffer resuldHandle:(resultCodeContent)handle
```

功能描述：

通过摄像头拍摄流进行二维码扫描。

传入参数：

**sampleBuffer** 摄像头当前拍摄的 Buffer 信息

**handle** 用于摄像头拍摄扫码的结果回调，并将结果放到 [resultCodeContent](#resultCodeContent) 中	


<span id="startDefaultQBarScan"></span>
#### startDefaultQBarScan

```objective-c
-(void)startDefaultQBarScan:(UIViewController *)vc  delegate:(id<QBarCodeKitSDKDelegate>)delegate 
```

功能描述：

启动 SDK 提供的默认界面进行扫码。

传入参数：

**vc** 启动默认扫码界面时当前界面的 UIViewController

**delegate** 接收扫码回调信息的代理 [QBarCodeKitSDKDelegate](#QBarCodeKitSDKDelegate) 对象


<span id="setViewConfig"></span>
#### setViewConfig

```objective-c
- (void) setViewConfig:(NSString *)configJson
```

功能描述：

设置界面的配置 Config 信息。

传入参数：

**configJson** 界面配置的 Json 串



### 回调以及代理说明

<span id="QBarCodeKitSDKDelegate"></span>
#### QBarCodeKitSDKDelegate

```objective-c
@protocol QBarCodeKitSDKDelegate <NSObject>

/*!
 回调函数
 @param result 返回的结果
 */
-(void)onResultBack:(NSDictionary *)result;

@end
```

其中 result 字典包含的字段为：

**errorcode** 对应结果的错误码

**errormsg** 对应结果异常的错误信息

**content** 对应存放扫码结果的 Json 字符串信息


<span id="resultCodeContent"></span>
#### resultCodeContent

```objective-c
typedef void (^resultCodeContent)(NSDictionary *resultDic);
```

其 resultDic 字典包含的字段为：

**errorcode** 对应结果的错误码

**errormsg** 对应结果异常的错误信息

**content** 对应存放扫码结果的 Json 字符串信息
