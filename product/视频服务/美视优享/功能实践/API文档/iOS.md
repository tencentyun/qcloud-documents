腾讯特效 SDK 核心接口类 `XMagic.h`，用于初始化 SDK、更新美颜数值、调用动效等功能。

## Public 成员函数

| API   | 描述  |
| ------------- | ------------- |
| [initWithRenderSize](#initwithrendersize) | 初始化接口 |
| [initWithGlTexture](#initwithgltexture) | 初始化接口 |
| [configPropertyWithType](#configpropertywithtype) | 配置美颜各种效果 |
| [emitBlurStrengthEvent](#emitblurstrengthevent) | 设置后处理模糊强度（作用于所有模糊组件） |
| [setRenderSize](#setrendersize) | 设置 renderSize |
| [deinit](#deinit) | 资源释放接口 |
| [process](#process) | 处理数据接口 |
| [processUIImage](#processuiimage) | 处理图片 |
| [getConfigPropertyWithName](#getconfigpropertywithname) | 获取美颜参数配置信息 |
| [registerLoggerListener](#registerloggerlistener) | 日志注册接口 |
| [registerSDKEventListener](#registersdkeventlistener)   | SDK 事件监听接口 |
| [clearListeners](#clearlisteners) | 注册回调清理接口 |
| [getCurrentGlContext](#getcurrentglcontext) | 获取当前 GL 上下文接口 |
| [onPause](#onpause) | SDK 暂停接口 |
| [onResume](#onresume) | SDK 恢复接口 |

### initWithRenderSize
初始化接口
```objectivec
- (instancetype _Nonnull)initWithRenderSize:(CGSize)renderSize
                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

**参数**

| 参数       | 含义     |
| ---------- | -------- |
| renderSize | 渲染尺寸 |
| assetsDict | 资源 Dict |

### initWithGlTexture
初始化接口

```objectivec
- (instancetype _Nonnull)initWithGlTexture:(unsigned)textureID
                        width:(int)width
                        height:(int)height
                        flipY:(bool)flipY
                        assetsDict:(NSDictionary* _Nullable)assetsDict;
```

**参数**

| 参数       | 含义         |
| ---------- | ------------ |
| textureID  | 纹理 ID      |
| width      | 渲染尺寸     |
| height     | 渲染尺寸     |
| flipY      | 是否翻转图片 |
| assetsDict | 资源 Dict    |

### configPropertyWithType

配置美颜各种效果

```objectivec
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

**参数**

| 参数          | 含义                        |
| ------------- | --------------------------- |
| propertyType  | 效果类型                    |
| propertyName  | 效果名称                    |
| propertyValue | 效果数值                    |
| extraInfo     | 预留扩展, 附加额外配置 Dict |

#### 配置美颜效果示例

- **美颜：**配置美白效果
```objectivec
NSString *propertyType = @"beauty";        //配置美颜的效果类型，这里以美颜为例
NSString *propertyName = @"beauty.whiten"; //配置美颜的名称，这里以美白为例
NSString *propertyValue = @"60";           //配置美白的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:nil];
```
- **滤镜**：配置心动效果
```objectivec
NSString *propertyType = @"lut";        //配置美颜的效果类型，这里以滤镜为例
NSString *propertyName = [@"lut.bundle/" stringByAppendingPathComponent:@"xindong_lf.png"]; //配置美颜的名称，这里以心动为例
NSString *propertyValue = @"60";           //配置滤镜的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:nil];
```
- **美体**：配置长腿效果
```objectivec
NSString *propertyType = @"body";        //配置美颜的效果类型，这里以美体为例
NSString *propertyName = @"body.legStretch"; //配置美颜的名称，这里以长腿为例
NSString *propertyValue = @"60";           //配置长腿的效果数值
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:nil];
```
- **动效**：配置2D动效的可爱涂鸦效果
```objectivec
 NSString *motion2dResPath = [[NSBundle mainBundle] pathForResource:@"2dMotionRes" ofType:@"bundle"];//这里是2dMotionRes文件夹的绝对路径
 NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以动效为例
 NSString *propertyName = @"video_keaituya"; //配置美颜的名称，这里以2D动效的可爱涂鸦为例
 NSString *propertyValue = motion2dResPath;  //配置动效的路径
 [self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:nil];
```
- **美妆**：配置女团妆效果
```objectivec
NSString *motionMakeupResPath = [[NSBundle mainBundle] pathForResource:@"makeupMotionRes" ofType:@"bundle"];//这里是makeupMotionRes文件夹的绝对路径
NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以美妆为例
NSString *propertyName = @"video_nvtuanzhuang"; //配置美颜的名称，这里以女团妆为例
NSString *propertyValue = motionMakeupResPath;  //配置动效的路径
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:nil];
//下面是要配置美妆的数值（上面的动效只需要调用一次，下面的配置美妆数值可以多次调用）
 NSString *propertyTypeMakeup = @"custom";         //配置美颜的效果类型，这里以美妆为例
 NSString *propertyNameMakeup = @"makeup.strength"; //配置美颜的名称，这里以女团妆为例
 NSString *propertyValueMakeup = @"60";             //配置美妆的效果数值
 [self.xmagicApi configPropertyWithType:propertyTypeMakeup withName:propertyNameMakeup withData:propertyValueMakeup withExtraInfo:nil];
```
- **分割**：配置背景模糊（强效果）
```objectivec
NSString *motionSegResPath = [[NSBundle mainBundle] pathForResource:@"segmentMotionRes" ofType:@"bundle"];//这里是segmentMotionRes文件夹的绝对路径
NSString *propertyType = @"motion";         //配置美颜的效果类型，这里以分割为例
NSString *propertyName = @"video_segmentation_blur_75"; //配置美颜的名称，这里以背景模糊-强为例
NSString *propertyValue = motionSegResPath;  //配置动效的路径
NSDictionary *dic = @{@"bgName":@"BgSegmentation.bg.png", @"bgType":@0, @"timeOffset": @0},@"icon":@"segmentation.linjian.png"};//配置预留字段
[self.xmagicApi configPropertyWithType:propertyType withName:propertyName withData:propertyValue withExtraInfo:dic];
```
- **自定义背景**：
```objectivec
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

```objectivec
- (void)emitBlurStrengthEvent:(int)strength;
```

**参数**

| 参数     | 含义     |
| -------- | -------- |
| strength | 效果数值 |

### setRenderSize

设置 renderSize

```objectivec
- (void)setRenderSize:(CGSize)size;
```

**参数**

| 参数 | 含义     |
| ---- | -------- |
| size | 渲染尺寸 |

### deinit

资源释放接口

```objectivec
- (void)deinit;
```

### process

处理数据接口

```objectivec
- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```

**参数**

| 参数  | 含义             |
| ----- | ---------------- |
| input | 输入处理数据信息 |

### processUIImage

处理图片
```objectivec
- (UIImage* _Nullable)processUIImage:(UIImage* _Nonnull)inputImage needReset:(bool)needReset;
```

**参数**

| 参数       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| inputImage | 输入图片建议最大尺寸 2160×4096。超过这个尺寸的图片人脸识别效果不佳或无法识别到人脸，同时容易引起 OOM 问题，建议把大图缩小后再传入 |
| needReset  | 以下场景中 needReset 需设置 为 true：<ul style="margin:0"><li>切换图片</li><li>首次使用分割</li><li>首次使用动效</li><li>首次使用美妆</li></ul> |

### getConfigPropertyWithName

获取美颜参数配置信息

```objectivec
- (YTBeautyPropertyInfo * _Nullable)getConfigPropertyWithName:(NSString *_Nonnull)propertyName;
```

**参数**

| 参数         | 含义     |
| ------------ | -------- |
| propertyName | 配置名称 |

### registerLoggerListener

日志注册接口

```objectivec
- (void)registerLoggerListener:(id<YTSDKLogListener> _Nullable)listener withDefaultLevel:(YtSDKLoggerLevel)level;
```

**参数**

| 参数     | 含义                       |
| -------- | -------------------------- |
| listener | 日志回调接口               |
| level    | 日志输出 level，默认 ERROR |

### registerSDKEventListener

SDK 事件监听接口

```objectivec
- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;
```

**参数**

| 参数     | 含义                                                        |
| -------- | ----------------------------------------------------------- |
| listener | 事件监听器回调，主要分为 AI 事件，Tips 提示事件，Asset 事件 |

### clearListeners

注册回调清理接口

```objectivec
- (void)clearListeners;
```

### getCurrentGlContext

获取当前 GL 上下文接口

```objectivec
- (nullable EAGLContext*)getCurrentGlContext;
```

### onPause

SDK 暂停接口

```objectivec
/// @brief APP暂停时候需要调用SDK暂停接口
- (void)onPause;
```

### onResume

SDK 恢复接口

```objectivec
/// @brief APP恢复时候需要调用SDK恢复接口
- (void)onResume;
```

## 静态函数

| API                                       | 描述                     |
| ----------------------------------------- | ------------------------ |
| [isBeautyAuthorized](#isbeautyauthorized) | 获取该美颜参数的授权信息 |

### isBeautyAuthorized

获取该美颜参数的授权信息（仅支持美颜和美体）

```objectivec
/// @param featureId 配置美颜参数
/// @return 返回对应美颜参数的授权结果
+ (BOOL)isBeautyAuthorized:(NSString * _Nullable)featureId;
```

## 回调

| API                                       | 描述                 |
| ----------------------------------------- | -------------------- |
| [YTSDKEventListener](#ytsdkeventlistener) | SDK 内部事件回调接口 |
| [YTSDKLogListener](#ytsdkloglistener)     | 日志监听回调         |


### YTSDKEventListener

SDK 内部事件回调接口
```objectivec
@protocol YTSDKEventListener <NSObject>
```

#### 成员函数
| 返回类型 | 名称                            |
| -------- | ------------------------------- |
| void     | [onYTDataEvent](#onytdataevent) |
| void     | [onAIEvent](#onaievent)         |
| void     | [onTipsEvent](#ontipsevent)     |
| void     | [onAssetEvent](#onassetevent)   |

#### 函数说明

##### onYTDataEvent
YTDataUpdate 事件回调

```objectivec
/// @param event NSString*格式的回调
- (void)onYTDataEvent:(id _Nonnull)event;
```

返回  JSON string 结构，最多返回5个人脸信息：

```objectivec
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

**字段含义**

| 字段                         | 类型  | 值域                                | 说明                                                   |
| ---------------------------- | ----- | ----------------------------------- | ------------------------------------------------------ |
| trace_id                     | int   | [1,INF)                             | 人脸 ID，连续取流过程中，ID 相同的可以认为是同一张人脸 |
| face_256_point               | float | [0,screenWidth] 或 [0,screenHeight] | 共512个数，人脸256个关键点，屏幕左上角为(0,0)          |
| face_256_visible             | float | [0,1]                               | 人脸256关键点可见度                                    |
| out_of_screen                | bool  | true/false                          | 人脸是否出框                                           |
| left_eye_high_vis_ratio      | float | [0,1]                               | 左眼高可见度点位占比                                   |
| right_eye_high_vis_ratio     | float | [0,1]                               | 右眼高可见度点位占比                                   |
| left_eyebrow_high_vis_ratio  | float | [0,1]                               | 左眉高可见度点位占比                                   |
| right_eyebrow_high_vis_ratio | float | [0,1]                               | 右眉高可见度点位占比                                   |
| mouth_high_vis_ratio         | float | [0,1]                               | 嘴高可见度点位占比                                     |

##### onAIEvent
AI 事件回调

```objectivec
/// @param event dict格式的回调
- (void)onAIEvent:(id _Nonnull)event;
```

##### onTipsEvent
提示事件回调

```objectivec
/// @param event dict格式的回调
- (void)onTipsEvent:(id _Nonnull)event;
```

##### onAssetEvent
资源包事件回调

```objectivec
/// @param event string格式的回调
- (void)onAssetEvent:(id _Nonnull)event;
```

### YTSDKLogListener

日志监听回调

```objectivec
@protocol YTSDKLogListener <NSObject>
```

#### 成员函数

| 返回类型 | 函数名称 |
| -------- | -------- |
| void     | onLog    |

#### 函数说明

##### onLog

日志监听回调

```objectivec
/// @param loggerLevel 返回当前日志等级
/// @param logInfo 返回当前日志信息
- (void)onLog:(YtSDKLoggerLevel) loggerLevel withInfo:(NSString * _Nonnull) logInfo;
```

