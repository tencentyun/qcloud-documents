# iOS API文档

腾讯特效SDK核心接口类XMagic.h，用于初始化SDK、更新美颜数值、调用动效等功能。

## Public成员函数

| API                       | 描述                                     |
| ------------------------- | :--------------------------------------- |
| initWithRenderSize        | 初始化接口                               |
| initWithGlTexture         | 初始化接口                               |
| configPropertyWithType    | 配置美颜各种效果                         |
| emitBlurStrengthEvent     | 设置后处理模糊强度（作用于所有模糊组件） |
| setRenderSize             | 设置renderSize                           |
| deinit                    | 资源释放接口                             |
| process                   | 处理数据接口                             |
| processUIImage            | 处理图片                                 |
| getConfigPropertyWithName | 获取美颜参数配置信息                     |
| registerLoggerListener    | 日志注册接口                             |
| registerSDKEventListener  | SDK事件监听接口                          |
| clearListeners            | 注册回调清理接口                         |
| getCurrentGlContext       | 获取当前GL上下文接口                     |
| onPause                   | SDK暂停接口                              |
| onResume                  | SDK恢复接口                              |

## Public成员函数说明

### initWithRenderSize

初始化接口

```objective-c
- (instancetype _Nonnull)initWithRenderSize:(CGSize)renderSize
                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

参数

| 参数       | 含义     |
| ---------- | -------- |
| renderSize | 渲染尺寸 |
| assetsDict | 资源Dict |

### initWithGlTexture

初始化接口

```objective-c
- (instancetype _Nonnull)initWithGlTexture:(unsigned)textureID
                        width:(int)width
                        height:(int)height
                        flipY:(bool)flipY
                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

参数

| 参数       | 含义         |
| ---------- | ------------ |
| textureID  | 纹理ID       |
| width      | 渲染尺寸     |
| height     | 渲染尺寸     |
| flipY      | 是否翻转图片 |
| assetsDict | 资源Dict     |

### configPropertyWithType

配置美颜各种效果

```objective-c
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

参数

| 参数          | 含义                       |
| ------------- | -------------------------- |
| propertyType  | 效果类型                   |
| propertyName  | 效果名称                   |
| propertyValue | 效果数值                   |
| extraInfo     | 预留扩展, 附加额外配置dict |

#### 配置美颜效果示例

##### 1.美颜

配置美白效果；

```objective-c
NSString *propertyType = @"beauty";        //配置美颜的效果类型，这里以美颜为例
NSString *propertyName = @"beauty.whiten"; //配置美颜的名称，这里以美白为例
NSString *propertyValue = @"60";           //配置美白的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
```

##### 2.滤镜

配置心动效果：

```objective-c
NSString *propertyType = @"lut";        //配置美颜的效果类型，这里以滤镜为例
NSString *propertyName = [@"lut.bundle/" stringByAppendingPathComponent:@"xindong_lf.png"]; //配置美颜的名称，这里以心动为例
NSString *propertyValue = @"60";           //配置滤镜的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
```

##### 3.美体

配置长腿效果：

```objective-c
NSString *propertyType = @"body";        //配置美颜的效果类型，这里以美体为例
NSString *propertyName = @"body.legStretch"; //配置美颜的名称，这里以长腿为例
NSString *propertyValue = @"60";           //配置长腿的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
```

##### 4.动效

配置2D动效的可爱涂鸦效果：

```objective-c
 NSString *motion2dResPath = [[NSBundle mainBundle] pathForResource:@"2dMotionRes" ofType:@"bundle"];//这里是2dMotionRes文件夹的绝对路径
 NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以动效为例
 NSString *propertyName = @"video_keaituya"; //配置美颜的名称，这里以2D动效的可爱涂鸦为例
 NSString *propertyValue = motion2dResPath;  //配置动效的路径
 [self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
```

##### 5.美妆

配置女团妆效果：

```objective-c
NSString *motionMakeupResPath = [[NSBundle mainBundle] pathForResource:@"makeupMotionRes" ofType:@"bundle"];//这里是makeupMotionRes文件夹的绝对路径
NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以美妆为例
NSString *propertyName = @"video_nvtuanzhuang"; //配置美颜的名称，这里以女团妆为例
NSString *propertyValue = motionMakeupResPath;  //配置动效的路径
[self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
//下面是要配置美妆的数值（上面的动效只需要调用一次，下面的配置美妆数值可以多次调用）
 NSString *propertyTypeMakeup = @"custom";         //配置美颜的效果类型，这里以美妆为例
 NSString *propertyNameMakeup = @"makeup.strength"; //配置美颜的名称，这里以女团妆为例
 NSString *propertyValueMakeup = @"60";             //配置美妆的效果数值
 [self.xmagicApi configPropertyWithType:propertyType withName:key withData:propertyValue withExtraInfo:nil];
```

##### 6.分割

配置背景模糊-强效果：

```objective-c
NSString *motionSegResPath = [[NSBundle mainBundle] pathForResource:@"segmentMotionRes" ofType:@"bundle"];//这里是segmentMotionRes文件夹的绝对路径
NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以分割为例
NSString *propertyName = @"video_segmentation_blur_75"; //配置美颜的名称，这里以背景模糊-强为例
NSString *propertyValue = motionSegResPath;  //配置动效的路径
NSDictionary *dic = @{@"bgName":@"BgSegmentation.bg.png", @"bgType":@0, @"timeOffset": @0},@"icon":@"segmentation.linjian.png"};//配置预留字段
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:dic];
```

自定义背景：

```objective-c
NSString *motionSegResPath = [[NSBundle mainBundle] pathForResource:@"segmentMotionRes" ofType:@"bundle"];//这里是segmentMotionRes文件夹的绝对路径
NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以分割为例
NSString *propertyName = @"video_empty_segmentation"; //配置美颜的名称，这里以自定义背景为例
NSString *propertyValue = motionSegResPath;  //配置动效的路径
NSString *imagePath = @"/var/mobile/Containers/Data/Application/06B00BBC-9060-450F-8D3A-F6028D185682/Documents/MediaFile/image.png"; //自定义背景图片的绝对路径。如果自定义背景选择的是视频，需要对视频进行压缩转码处理，使用压缩转码处理后的绝对路径
int bgType = 0;//自定义背景的类型。 0表示图片，1表示视频
int timeOffset = 0；//时长。图片背景时，为0；视频背景时为视频的时长
NSDictionary *dic = @{@"bgName":imagePath, @"bgType":@(bgType), @"timeOffset": @(timeOffset)},@"icon":@"segmentation.linjian.png"};//配置预留字段
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:dic];
```

### emitBlurStrengthEvent

设置后处理模糊强度（作用于所有模糊组件）

```objective-c
- (void)emitBlurStrengthEvent:(int)strength;
```

参数

| 参数     | 含义     |
| -------- | -------- |
| strength | 效果数值 |

### setRenderSize

设置renderSize

```objective-c
- (void)setRenderSize:(CGSize)size;
```

参数

| 参数 | 含义     |
| ---- | -------- |
| size | 渲染尺寸 |

### deinit

资源释放接口

```objective-c
- (void)deinit;
```

### process

处理数据接口

```objective-c
- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```

参数

| 参数  | 含义             |
| ----- | ---------------- |
| input | 输入处理数据信息 |

### processUIImage

处理图片

```objective-c
- (UIImage* _Nullable)processUIImage:(UIImage* _Nonnull)inputImage needReset:(bool)needReset;
```

参数

| 参数       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| inputImage | 输入图片建议最大尺寸 2160*4096。超过这个尺寸的图片人脸识别效果不佳或无法识别到人脸，同时容易引起OOM问题，建议把大图缩小后再传入 |
| needReset  | 1、切换图片；2、首次使用分割；3、首次使用动效；4、首次使用美妆 这几种场景needReset设置为true |

### getConfigPropertyWithName

获取美颜参数配置信息

```objective-c
- (YTBeautyPropertyInfo * _Nullable)getConfigPropertyWithName:(NSString *_Nonnull)propertyName;
```

参数

| 参数         | 含义     |
| ------------ | -------- |
| propertyName | 配置名称 |

### registerLoggerListener

日志注册接口

```objective-c
- (void)registerLoggerListener:(id<YTSDKLogListener> _Nullable)listener withDefaultLevel:(YtSDKLoggerLevel)level;
```

参数

| 参数     | 含义                     |
| -------- | ------------------------ |
| listener | 日志回调接口             |
| level    | 日志输出level，默认ERROR |

### registerSDKEventListener

SDK事件监听接口

```objective-c
- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;
```

参数

| 参数     | 含义                                                    |
| -------- | ------------------------------------------------------- |
| listener | 事件监听器回调，主要分为AI事件，Tips提示事件，Asset事件 |

### clearListeners

注册回调清理接口

```objective-c
- (void)clearListeners;
```

### getCurrentGlContext

获取当前GL上下文接口

```objective-c
- (nullable EAGLContext*)getCurrentGlContext;
```

### onPause

SDK暂停接口

```objective-c
/// @brief APP暂停时候需要调用SDK暂停接口
- (void)onPause;
```

### onResume

SDK恢复接口

```objective-c
/// @brief APP恢复时候需要调用SDK恢复接口
- (void)onResume;
```

## 静态函数

| API                | 描述                     |
| ------------------ | ------------------------ |
| isBeautyAuthorized | 获取该美颜参数的授权信息 |

## 静态函数说明

### isBeautyAuthorized

获取该美颜参数的授权信息（仅支持美颜和美体）

```objective-c
/// @param featureId 配置美颜参数
/// @return 返回对应美颜参数的授权结果
+ (BOOL)isBeautyAuthorized:(NSString * _Nullable)featureId;
```

## 回调

### YTSDKEventListener

SDK内部事件回调接口

```objective-c
@protocol YTSDKEventListener <NSObject>
```

#### 成员函数

| 返回类型 | 名称          |
| -------- | ------------- |
| void     | onYTDataEvent |
| void     | onAIEvent     |
| void     | onTipsEvent   |
| void     | onAssetEvent  |

#### 函数说明

##### onYTDataEvent

YTDataUpdate事件回调

```objective-c
/// @param event NSString*格式的回调
- (void)onYTDataEvent:(id _Nonnull)event;
```

返回JSON string结构，最多返回5个人脸信息：

```objective-c
{
 "face_info":[{
  "trace_id":5,
  "face_256_point":[
    180.0,
    112.2,
    ...
  ],
  "face_256_visible":[
    0.85,
    ...
  ],
  "out_of_screen":true,
  "left_eye_high_vis_ratio:1.0,
  "right_eye_high_vis_ratio":1.0,
  "left_eyebrow_high_vis_ratio":1.0,
  "right_eyebrow_high_vis_ratio":1.0,
  "mouth_high_vis_ratio":1.0
 },
 ...
 ]
}
```

字段含义

| 字段                         | 类型  | 值域                                | 说明                                                     |
| ---------------------------- | ----- | ----------------------------------- | -------------------------------------------------------- |
| trace_id                     | int   | [1,INF)                             | 人脸 ID，连续取流过程中，ID 相同的可以认为是同一张人脸。 |
| face_256_point               | float | [0,screenWidth] 或 [0,screenHeight] | 共512个数，人脸256个关键点，屏幕左上角为(0,0)。          |
| face_256_visible             | float | [0,1]                               | 人脸256关键点可见度。                                    |
| out_of_screen                | bool  | true/false                          | 人脸是否出框。                                           |
| left_eye_high_vis_ratio      | float | [0,1]                               | 左眼高可见度点位占比。                                   |
| right_eye_high_vis_ratio     | float | [0,1]                               | 右眼高可见度点位占比。                                   |
| left_eyebrow_high_vis_ratio  | float | [0,1]                               | 左眉高可见度点位占比。                                   |
| right_eyebrow_high_vis_ratio | float | [0,1]                               | 右眉高可见度点位占比。                                   |
| mouth_high_vis_ratio         | float | [0,1]                               | 嘴高可见度点位占比。                                     |

##### onAIEvent

AI事件回调

```objective-c
/// @param event dict格式的回调
- (void)onAIEvent:(id _Nonnull)event;
```

##### onTipsEvent

提示事件回调

```objective-c
/// @param event dict格式的回调
- (void)onTipsEvent:(id _Nonnull)event;
```

##### onAssetEvent

资源包事件回调

```objective-c
/// @param event string格式的回调
- (void)onAssetEvent:(id _Nonnull)event;
```

### YTSDKLogListener

日志监听回调

```objective-c
@protocol YTSDKLogListener <NSObject>
```

#### 成员函数

| 返回类型 | 函数名称 |
| -------- | -------- |
| void     | onLog    |

#### 函数说明

##### onLog

日志监听回调

```objective-c
/// @param loggerLevel 返回当前日志等级
/// @param logInfo 返回当前日志信息
- (void)onLog:(YtSDKLoggerLevel) loggerLevel withInfo:(NSString * _Nonnull) logInfo;
```

