智能扫码的 API 主要涉及 QBarCodeKit 对象，下面对其支持的 API 作出说明。

## QBarCodeKit

| API                                                          | 功能描述                                   |
| ------------------------------------------------------------ | ------------------------------------------ |
| [sharedInstance](#sharedInstance)                            | 获得 QBarCodeKit 的单例对象                  |
| [getVersion](#getVersion)                                    | 获得 SDK 的版本信息                          |
| [initQBarCodeKit](#initQBarCodeKit)                          | 初始化 SDK，并完成鉴权认证                  |
| [decodeImageWithQBar](#decodeImageWithQBar)                  | 可以识别传入图片中存在的二维码、条形码信息 |
| [qBarDecodingWithSampleBuffer](#qBarDecodingWithSampleBuffer) | 通过摄像头拍摄流进行二维码扫描             |
| [startDefaultQBarScan](#startDefaultQBarScan)                | 启动 SDK 提供的默认界面进行扫码              |
| [setViewConfig](#setViewConfig)                              | 设置界面配置信息                           |



[](id:sharedInstance)
### sharedInstance

```objective-c
+ (instancetype) sharedInstance 
```

- 功能描述：
获得 QBarCodeKit 的单例对象静态方法。
- 返回结果：
QBarCodeKit 的单例对象。


[](id:getVersion)
### getVersion

```objective-c
- (NSString *) getVersion 
```

- 功能描述：
获得 SDK 的版本信息。
- 返回结果：
当前 SDK 的版本信息。


[](id:initQBarCodeKit)
### initQBarCodeKit

```objective-c
- (void) initQBarCodeKit:(NSString *)secretId secretKey:(NSString *)secretkey teamId:(NSString *)teamId resultHandle:(resultCodeContent)handle;
```

- 功能描述：
初始化 SDK，并完成鉴权认证。
- 传入参数：
	- **secretId** 用户在后台申请的 secretId 信息
	- **secretkey** 用户在后台申请后获取的专属密钥信息
	- **teamId** 用户申请所填写的 development team id
	- **handle** 用于接收初始化与鉴权认证的结果回调，并将结果放到 [QBarResultCodeContent](#QBarResultCodeContent) 中	


[](id:decodeImageWithQBar)
### decodeImageWithQBar

```objective-c
- (void) decodeImageWithQBar:(UIImage *)image resultHandler:(resultCodeContent)handle
```

- 功能描述：
可以识别传入图片中存在的二维码、条形码信息。
- 传入参数：
 - **image** 需要识别的图像信息
 - **handle** 用于图像识别的结果回调，并将结果放到 [QBarResultCodeContent](#QBarResultCodeContent) 中	


[](id:qBarDecodingWithSampleBuffer)
### qBarDecodingWithSampleBuffer

```objective-c
- (void) qBarDecodingWithSampleBuffer:(CMSampleBufferRef) sampleBuffer resuldHandle:(QBarResultCodeContent)handle
```

- 功能描述：
通过摄像头拍摄流进行二维码扫描。
- 传入参数：
 -	**sampleBuffer** 摄像头当前拍摄的 Buffer 信息
 - **handle** 用于摄像头拍摄扫码的结果回调，并将结果放到 [QBarResultCodeContent](#QBarResultCodeContent) 中	


[](id:startDefaultQBarScan)
### startDefaultQBarScan

```objective-c
-(void)startDefaultQBarScan:(UIViewController *)vc withResult:(QBarResultCodeContent)resultDict;
```

- 功能描述：
启动SDK提供的默认界面进行扫码。
- 传入参数：
**vc** 启动默认扫码界面时当前界面的 ViewController


[](id:setViewConfig)
### setViewConfig

```objective-c
- (void) setViewConfig:(QBarSDKUIConfig *)qBarSDKUIConfig
```

- 功能描述：
设置界面的配置 Config 信息。
- 传入参数：
**QBarSDKUIConfig** 

| 属性              | 含义           |
| ----------------- | -------------- |
| naviBarHidde      | 导航栏是否隐藏 |
| naviBarBgColor    | 导航栏背景色   |
| naviBarTitle      | 导航栏标题     |
| naviBarTitleColor | 导航栏标题颜色 |
| scanTips          | 提示语         |
| scanTipsColor     | 提示语文字颜色 |
| statusBarHidde    | 是否隐藏状态栏 |



## 回调说明

[](id:QBarResultCodeContent)
### QBarResultCodeContent

```objective-c
typedef void (^qBarResultCodeContent)(NSDictionary *resultDic);
```

其中 resultDic 字典包含的字段为：
- **errorcode** number 类型 对应结果的错误码
- **errormsg**  NSString 类型 对应结果异常的错误信息
- **content** NSArray 类型 对应存放扫码结果信息 (NSArray 内部是NSSting json 对象)

```
NSArray *content = resultDic[CONTENT];
NSLog(@"content %@",content);

```

