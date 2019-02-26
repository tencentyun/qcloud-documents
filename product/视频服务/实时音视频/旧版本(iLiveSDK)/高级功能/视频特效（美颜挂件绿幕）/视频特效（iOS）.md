
本文将指导您在 ILiveSDK 中集成预处理插件（TXMVideoPreprocessor）实现视频特效功能。

## 效果图
美颜|滤镜|大眼/瘦脸/小鼻等|动效|绿幕
:-----:|:-----:|:-----:|:-----:|:-----:
![](https://main.qcloudimg.com/raw/37c82c24b8154081c21293f7c65ddfae.png)|![](https://main.qcloudimg.com/raw/b7b91102c419a5f7ae590215fdb0065c.png)|![](https://main.qcloudimg.com/raw/bd5ebfa2b3078061ca5f2e824db1beb5.png)|![](https://main.qcloudimg.com/raw/53a5e44a06db04fdca6b6929c63820f5.png)|![](https://main.qcloudimg.com/raw/2117efcf754bb9992a5fbc9ba62f1bce.png)

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/TXMVideoPreprocessor/IOS/3.3.1/demo_beauty_3.3.1.zip)

## 集成说明

### 引入依赖库


高级版本|基础版本
:-----:|:-----:|
![](http://dldir1.qq.com/hudongzhibo/TXMVideoPreprocessor/IOS/3.3.1/doc/advance.png)|![](http://dldir1.qq.com/hudongzhibo/TXMVideoPreprocessor/IOS/3.3.1/doc/basic.png)|
确保所有的资源都引入到Copy Bundle Resources，并且model文件夹下的资源以Create folder references方式引入||


 * 温馨提示：
 >(1) 如果不使用滤镜，可以删除 TXLiteAVVideoPreprocessorResource.bundle；
 (2) 高级版本需要申请 licence 并同步到 Copy Bundle Resources 中，licence 不能重命名，必须为 YTFaceSDK.licence；  
 (3) 下载的 TXMVideoPreprocessor.advance 中的 Pitu 子文件夹及 YoutuBeauty 子文件夹中的所有 bundle，并同步到 Copy Bundle Resources 中，否则直接 crash；  
 (4) 如果您是 AVSDK 的用户，processFrame 的 orientation 参数应该设置为 frameData.frameDesc.rotate，否则无法识别到人脸；  
 (5) 使用滤镜功能时，确保设置融合度 setFilterMixLevel，否则默认为 0；
 (6) 如需要更多动效资源，请联系商务，并将资源添加到 Resource 文件夹下；  


 ### 工程配置
 > 基础版本无须做工程配置，用默认配置即可。  


## 集成到ILiveSDK

1.对象创建

```object-c
//引入头文件
#import "TXCVideoPreprocessor.h"
//声明变量
@property (nonatomic, strong) TXCVideoPreprocessor *preProcessor;
@property (nonatomic, assign) Byte  *processorBytes;
//创建变量
self.preProcessor = [[TXCVideoPreprocessor alloc] init];
[self.preProcessor setDelegate:self];//TXIVideoPreprocessorDelegate
```

2.设置 ILiveSDK 数据回调

```object-c
// 进房前设置数据帧回调
[[ILiveRoomManager getInstance] setLocalVideoDelegate:self];//QAVLocalVideoDelegate
```

3.调用处理接口

```object-c
- (void)OnLocalVideoPreProcess:(QAVVideoFrame *)frameData
{
    //设置美颜、美白、红润等参数
    [self.preProcessor setBeautyLevel:5];
    [self.preProcessor setRuddinessLevel:8];
    [self.preProcessor setWhitenessLevel:8];
    [self.preProcessor setOutputSize:CGSizeMake(frameData.frameDesc.width, frameData.frameDesc.height)];
    //开始预处理
    [self.preProcessor processFrame:frameData.data width:frameData.frameDesc.width height:frameData.frameDesc.height    orientation:TXE_ROTATION_0 inputFormat:TXE_FRAME_FORMAT_NV12           outputFormat:TXE_FRAME_FORMAT_NV12];
    //将处理完的数据拷贝到原来的地址空间，如果是同步处理，此时会先执行（4）
    if(self.processorBytes){
        memcpy(frameData.data, self.processorBytes, frameData.frameDesc.width * frameData.frameDesc.height * 3 / 2);
    }
}
```

4.回调中保存数据

```object-c
- (void)didProcessFrame:(Byte *)bytes width:(NSInteger)width height:(NSInteger)height format:(TXEFrameFormat)format timeStamp:(UInt64)timeStamp
{
    self.processorBytes = bytes;
}
```


## API 说明

### 预处理接口调用

```object-c
/*
* 预处理数据
* @param   sampleBuffer 帧数据（420f和y420）
* @param   orientation  人脸识别方向（无需人脸识别：TXE_ROTATION_0）
* @param   outputFormat 输出数据格式
* @return  int          是否调用成功，0成功，-1失败
*/
- (int)processFrame:(CMSampleBufferRef)sampleBuffer orientation:(TXERotation)orientation outputFormat:(TXEFrameFormat)outputFormat;

/*
* 预处理数据
* @param   data         帧数据
* @param   width        宽
* @param   height       高
* @param   orientation  人脸识别方向（无需人脸识别：TXE_ROTATION_0）
* @param   inputFormat  输入数据格式
* @param   outputFormat 输出数据格式
* @return  int          是否调用成功，0成功，-1失败
*/
- (int)processFrame:(Byte *)data width:(NSInteger)width height:(NSInteger)height orientation:(TXERotation)orientation inputFormat:(TXEFrameFormat)inputFormat outputFormat:(TXEFrameFormat)outputFormat;
```

### 数据处理完回调

```object-c
/*
* 设置代理
* @param   delegate   代理
*/
- (void)setDelegate:(id<TXIVideoPreprocessorDelegate>)delegate;

/*
* 设置通知（是否识别到人脸等通知）
* @param   notify   通知
*/
- (void)setNotify:(id<TXINotifyDelegate>)notify;

@protocol TXIVideoPreprocessorDelegate <NSObject>
@optional
/*
* 添加水印前回调
* @param   texture     纹理id
* @param   width       宽
* @param   height      高
* @return  处理后纹理id
*/
- (GLuint)willAddWatermark:(GLuint)texture width:(NSInteger)width height:(NSInteger)height;

/**
* 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
*/
- (void)onTextureDestoryed;

/*
* 数据处理回调
* @param   sampleBuffer 帧数据
* @param   timeStamp    时间戳
*/
- (void)didProcessFrame:(CMSampleBufferRef)sampleBuffer timeStamp:(UInt64)timeStamp;

/*
* 数据处理回调
* @param   bytes       帧数据
* @param   width       宽
* @param   height      高
* @param   format      输出数据格式
* @param   timeStamp   时间戳
*/
- (void)didProcessFrame:(Byte *)bytes width:(NSInteger)width height:(NSInteger)height format:(TXEFrameFormat)format timeStamp:(UInt64)timeStamp;

/**
* 人脸数据回调（启用了pitu模块才有效，开启pitu模块必须是打开动效或大眼瘦脸）
* @prama points 人脸坐标
*/
- (void)onDetectFacePoints:(NSArray *)points;
@end
```


### 基础功能

> 美颜风格、美颜、美白、红润、滤镜、水印、裁剪、旋转、缩放、镜像


```object-c
/*
* 设置输入裁剪区域
*/
@property (nonatomic, assign) CGRect cropRect;

/*
* 设置裁剪后旋转角度
*/
@property (nonatomic, assign) TXERotation rotateAngle;

/*
* 设置旋转后缩放大小
*/
@property (nonatomic, assign) CGSize outputSize;

/*
* 设置缩放后是否镜像
*/
@property (nonatomic, assign) BOOL mirror;

/*
* 设置水印是否镜像
*/
@property (nonatomic, assign) BOOL waterMirror;

/*
* 设置绿幕参数
*/
@property (nonatomic, strong) TXCGreenScreenParam *greenParam;

/*
* 是否异步回调（默认NO）
*/
@property (nonatomic, assign) BOOL isAsync;

/*
* 设置美颜风格
* @param   level    设置美颜类型，默认TXE_BEAUTY_TYPE_SMOOTH
*/
- (void)setBeautyStyle:(TXEBeautyStyle)style;

/*
* 设置美颜（0-10）
* @param   level    美颜程度，0表示原图
*/
- (void)setBeautyLevel:(NSInteger)level;

/*
* 设置美白（0-10）
* @param   level    美白程度，0表示原图
*/
- (void)setWhitenessLevel:(NSInteger)level;

/*
* 设置红润（0-10）
* @param   level    红润程度，0表示原图
*/
- (void)setRuddinessLevel:(NSInteger)level;

/*
* 设置水印
* @param   view  水印view
*/
- (void)setWaterMark:(UIView *)view;

```

可以使用sdk自带的滤镜资源，也可以自定义滤镜资源，通过设置融合度调整滤镜资源和图像的融合程度。

```object-c
/*
* 设置滤镜
* @param   type  滤镜类型
*/
- (void)setFilterType:(TXEFilterType)type;

/*
* 设置滤镜
* @param   imagePath  滤镜资源路径
*/
- (void)setFilterImage:(NSString *)imagePath;

/*
* 设置滤镜
* @param   image  滤镜图片
*/
- (void)setFilterUIImage:(UIImage *)image;

/*
* 设置滤镜融合度（0-1）
* @param   level    滤镜融合度
*/
- (void)setFilterMixLevel:(CGFloat)level;
```



### 高级功能

> 大眼、瘦脸、v脸、短脸、下巴、瘦鼻、绿幕、动效。


```object-c
/*
* 设置绿幕
* @param   file  绿幕文件路径
*/
- (void)setGreenScreenFile:(NSString *)file;

/*
* 设置大眼（0-10）
* @param   level    大眼程度
*/
- (void)setEyeScaleLevel:(NSInteger)level;

/*
* 设置瘦脸（0-10）
* @param   level    瘦脸程度
*/
- (void)setFaceSlimLevel:(NSInteger)level;

/*
* 设置美型（0-10）
* @param   level    美型程度
*/
- (void)setFaceBeautyLevel:(NSInteger)level;

/*
* 设置V脸（0-10）
* @param   level    V脸程度
*/
- (void)setFaceVLevel:(NSInteger)level;

/*
* 设置下巴拉伸或收缩（-10-10，0为正常）
* @param   level    伸缩程度
*/
- (void)setChinLevel:(NSInteger)level;

/*
* 设置短脸（0-10）
* @param   level    短脸程度
*/
- (void)setFaceShortLevel:(NSInteger)level;

/*
* 设置瘦鼻（0-10）
* @param   level    瘦鼻程度
*/
- (void)setNoseSlimLevel:(NSInteger)level;

/*
* 设置动效
* @param   templatePath  动效资源路径
*/
- (void)setMotionTemplate:(NSString *)templatePath;

```

将动效资源解压在 Resource 目录下，通过资源路径设置动效。

```object-c
/*
* 设置动效
* @param   templatePath  动效资源路径
*/
- (void)setMotionTemplate:(NSString *)templatePath;
```

使用绿幕需要先准备一个用于播放的 mp4 文件，通过调用以下接口即可开启绿幕效果。

```object-c
/*
* 设置绿幕
* @param   file  绿幕文件路径
*/
- (void)setGreenScreenFile:(NSString *)file;
```

## 常见问题

#### 功能问题
sdK提供美颜、美白、红润、滤镜、大眼、瘦脸、动效贴纸、绿幕等功能，其中大眼、瘦脸、动效贴纸等以人脸识别为基础的功能是基于优图实验室的人脸识别技术和天天P图的美妆技术为基础开发的特权功能，通过跟优图和P图团队合作，将这些特效深度整合到图像处理流程中，以实现更好的视频特效。

#### 费用问题

美颜、美白、红润等基础功能是免费的。基于人脸识别的功能由于采用了优图实验室的专利技术，授权费用约 50W/年（目前国内同类图像处理产品授权均在百万左右）。如有需要可以提工单或联系我们（jerryqian QQ:364993028 ），商务同学会提供 P 图 SDK，并替您向优图实验室申请试用 License。
