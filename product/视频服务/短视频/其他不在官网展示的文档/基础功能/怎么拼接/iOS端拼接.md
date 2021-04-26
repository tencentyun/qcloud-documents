## 功能概览
视频拼接功能可以前两段视频前后拼接，也可以将两段视频以制定的位置合并到一起。

## 相关类介绍

| 类名           | 功能  |
| ------------- | --------- |
| `TXVideoJoiner.h`| 视频合成类 |

## 使用说明
视频拼接的基本使用流程如下
1. 实例化拼接对象
2. 传入被合并或者拼接的多段视频
3. 开始拼接
4. 监听拼接合成事件获取进度及完成情况

示例
```
// 如果需要预览，这里要先配置预览参数，如果无需预览，直接传nil即可，这里以Demo中的Common/UGC/VideoPreview来做预览的视图为例子
#import "VideoPreview.h"
@implementation JoinViewController
{
   TXVideoJoiner *videoJoin;
   VideoPreview *_videoPreview;
}
- (void)viewDidLoad {
   [super viewDidLoad];
   _videoPreview = [[VideoPreview alloc] initWithFrame:self.view.bounds]
   [self.view addSubview:_videoPreview];

   TXPreviewParam *param = [[TXPreviewParam alloc] init];
   param.videoView = _videoPreview.renderView;
   param.renderMode = PREVIEW_RENDER_MODE_FILL_EDGE;

   // 1. 实例化拼接对象
   videoJoin = [[TXVideoJoiner alloc] initWithPreview:param];

   // 2. 传入要拼接的多段视频, 这里假设已经加载了两段视频(AVAsset) videoAsset0, videoAsset1 
   [videoJoin setVideoList: @[videoAsset0, videoAsset1]];

   // 3. 设置预回调委托，开始执行拼接
   videoJoin.joinerDelegate = self;
   NSString *outputPath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"temp.mp4"];
   [videoJoin joinVideo:VIDEO_COMPRESSED_540P videoOutputPath:outputPath];
}

- (void) onJoinProgress:(float)progress {
    // 4. 监听拼接进度
}

- (void)onJoinComplete:(TXJoinerResult *)result {
   // 4. 监听拼接完成事件
   if (result.retCode == 0) {
      // 拼接成功
   } else {
      // 拼接错误，错误码参见 TXJoinerResultCode
   }
}
```

## 设置视频列表
Demo中使用了QBImagePicker来实现从相册选取多视频的功能, 可以参考工具包Demo中MainViewController中的示例代码。

```

/** 使用文件路径设置视频文件列表 
 * @param videoPathList  视频路径列表
 * @return  0 成功；
 *         -1 视频列表文件不存在
 *         -2 视频列表里面有一个或则几个视频不存在
 *         -3 视频列表里面有不支持合成的视频 (声道数>2 , 视频无声音数据暂不支持合成)
*/
- (int)setVideoPathList:(NSArray *)videoPathList;

/** 使用AVAsset设置视频文件列表
 * @param videoAssetList 视频AVAsset对象列表,从本地相册loading出视频列表后，可以直接传入对应的视频属性列表，会极大的降低视频从相册loading的时间，具体请参考demo用法
 * @return  0 成功；
 *         -1 视频属性asset列表不存在
 *         -2 视频列表里面有一个或则几个视频不存在
 *         -3 视频列表里面有不支持合成的视频 (声道数大于2, 或者没有声音数据的视频暂不支持合成)
 */
- (int)setVideoAssetList:(NSArray<AVAsset *> *)videoAssetList;
```

## 预览播放控制
设置好预览view同时传入待合成的视频文件数组后，可以开始播放预览，合成模块提供了一组接口来做视频的播放预览：
```
/// 开启视频播放，会从视频的起始位置开始播放 （需要在setVideoPathList之后调用）
- (void)startPlay;

/// 暂停播放
- (void)pausePlay;

/// 继续播放
- (void)resumePlay;

/// 停止播放
- (void)stopPlay;
```

设置获取播放状态的代理对象
```
/// 预览的回调委托对象
/// @see TXVideoPreviewListener
@property (nonatomic ,weak) id<TXVideoPreviewListener> previewDelegate;
```
## 视频前后拼接
视频拼接可以将一组视频前拼接成一段长视频，通过调用以下接口开始执行操作
```
/**
 * SDK内部会自动判断视频是否可以快速合成，如果可以，会优先走快速合成逻辑
 * 调用后在TXVideoComposeListener里面监听结果回调
 * 注意：需要合成的视频列表中，每个视频必须要有video data 和 audio data 数据
 * @param videoCompressed 视频压缩质量
 * @param videoOutputPath 生成新的视频存储路径
 */
- (void)joinVideo:(TXVideoCompressed)videoCompressed  videoOutputPath:(NSString *)videoOutputPath;
```

## 视频同屏合成(合唱)
### 1. 设置多个视频的坐标
```
/** 设置分屏合成坐标
 * 使用方法详见demo示例
 * @param rects  需要合成视频的矩形区域, 宽高的最大值为canvasWidth, canvasHeight
 * @param canvasWidth 画布宽度，也是分屏合成之后视频的宽度
 * @param canvasHeight 画布高度，也是分屏合成之后视频的高度
 */
- (void)setSplitScreenList:(NSArray <NSValue *> *)rects  canvasWidth:(int)canvasWidth canvasHeight:(int)canvasHeight;
```
### 2. 开始合成
```
/** 分屏合成
 * @param videoCompressed 视频压缩质量
 * @param videoOutputPath 生成新的视频存储路径
 */
- (void)splitJoinVideo:(TXVideoCompressed)videoCompressed  videoOutputPath:(NSString *)videoOutputPath;
```


## 生成最终文件

预览效果满意后调用生成接口即可生成合成后的文件，视频合成步骤及调用接口如下：
### 1 设置视频合成进度回调

```
/// 合成的回调委托对象
/// @see TXVideoJoinerListener
@property (nonatomic ,weak) id<TXVideoJoinerListener>  joinerDelegate;
```
### 2. 监听回调事件
```
/**
 * 短视频合成完成
 * @param progress  合成视频进度百分比
 */
-(void) onJoinProgress:(float)progress;
```
```
/**
 * 短视频合成完成
 * @param result 合成结果
 * @see TXJoinerResult
 */
-(void) onJoinComplete:(TXJoinerResult *)result;

/// 视频合成结果错误码定义
typedef NS_ENUM(NSInteger, TXJoinerResultCode)
{
    /// 合成成功
    JOINER_RESULT_OK                                = 0,         
    /// 合成失败
    JOINER_RESULT_FAILED                            = -1,  
    /// licence 验证失败
    JOINER_RESULT_LICENCE_VERIFICATION_FAILED       = -5,           
};
```
