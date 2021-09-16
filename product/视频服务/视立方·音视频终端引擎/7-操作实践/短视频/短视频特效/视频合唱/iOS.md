本篇教程向大家介绍如何从零开始完成合唱的基础功能。
## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 过程简介

1. 在界面上放两个 View， 一个用来播放，一个用来录制。
2. 再放一个按钮和进度条来开始录制和显示进度。
3. 录制与源视频相同的时长后停止。
4. 把录好的视频与源视频左右合成。
5. 预览合成好的视频。

## 界面搭建
1. **开始工程的创建**：打开 Xcode，【File】>【New】>【Project】，然后起好工程名创建工程（后续称为 Demo）。因为要录像，所以需要相机和麦克风的权限，在 Info 中配置一下增加以下两项：
```
Privacy - Microphone Usage Description
Privacy - Camera Usage Description
```
> ? 该配置项可自定义，例如"录制视频"。
2. **配置一个简单的录制界面**：打开 `Main.storyboard`，拖进去两个 UIView，配置宽度为 superview 的0.5倍，长宽比16:9。
   ![ ](https://main.qcloudimg.com/raw/757835bb36355f7e702a364d9740eb1e.png)
3. **加上进度条**：在 `ViewController.m` 中设置 IBOutlet 绑定界面，并设置好按钮的 IBAction。因为录制好后还要跳转到预览界面，还需要一个导航。单击黄色 VC 图标，在菜单栏依次进入【Editor】>【Embeded In】，单击【Navigation Controller】给 ViewController 套一层 Navigation Controller。完成基本 UI 的搭建。
      ![ ](https://main.qcloudimg.com/raw/cbdc197ae0ac5856413efb956dd5893d.png)


## 代码部分

对于合唱功能主要使用三大块功能：播放、录制、以及录制后和原视频进行合成，这三个功能对应到 SDK 的类为： TXVideoEditer、TXUGCRecord、TXVideoJoiner。

[](id:step1)
### 1. 配置 License

在使用前要配置腾讯云视立方短视频 UGSV SDK 的 Licence，打开 `AppDelegate.m` 在里面添加以下代码：

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [TXUGCBase setLicenceURL:@"<Licence的URL>" key:@"<Licence的Key>"];
    return YES;
}
```

> ? Licence 参数需要到 [视立方控制台](https://console.cloud.tencent.com/vcube) 去申请。申请审核通过后，页面上即可出现相关的 Licence 信息。

[](id:step2)
### 2. 声明与初始化
1. 打开 ViewContorller.m，引用 SDK 并声明上述三个类的实例。另外这里播放、录制和合成视频都是异步操作，需要监听他们的事件，所以要加上实现 TXVideoJoinerListener、TXUGCRecordListener、TXVideoPreviewListener 这三个协议的声明。加好后如下所示：
    <dx-codeblock>
    ::: ios objective-c
    #import "ViewController.h"
    @import TXLiteAVSDK_UGC;

    @interface ViewController () <TXVideoJoinerListener, TXUGCRecordListener, TXVideoPreviewListener>
    {
        TXVideoEditer *_editor;
        TXUGCRecord   *_recorder;
        TXVideoJoiner *_joiner;

        TXVideoInfo    *_videoInfo;
        
        NSString       *_recordPath;
        NSString       *_resultPath;
    }

    @property (weak, nonatomic) IBOutlet UIView *cameraView;
    @property (weak, nonatomic) IBOutlet UIView *movieView;
    @property (weak, nonatomic) IBOutlet UIButton *recordButton;
    @property (weak, nonatomic) IBOutlet UIProgressView *progressView;

    - (IBAction)onTapButton:(UIButton *)sender;
      @end
      :::
      </dx-codeblock>
2. 准备好成员变量和接口实现声明后，我们在 viewDidLoad 中对上面的成员变量进行初始化。
<dx-codeblock>
::: ios objective-c
    - (void)viewDidLoad {
        [super viewDidLoad];
        // 这里找一段 mp4 视频放到了工程里，或者用手机录制的 mov 格式视频也可以
        NSString *mp4Path = [[NSBundle mainBundle] pathForResource:@"demo" ofType:@"mp4"];
        _videoInfo = [TXVideoInfoReader getVideoInfo:mp4Path];
        TXAudioSampleRate audioSampleRate = AUDIO_SAMPLERATE_48000;
        if (_videoInfo.audioSampleRate == 8000) {
            audioSampleRate = AUDIO_SAMPLERATE_8000;
        }else if (_videoInfo.audioSampleRate == 16000){
            audioSampleRate = AUDIO_SAMPLERATE_16000;
        }else if (_videoInfo.audioSampleRate == 32000){
            audioSampleRate = AUDIO_SAMPLERATE_32000;
        }else if (_videoInfo.audioSampleRate == 44100){
            audioSampleRate = AUDIO_SAMPLERATE_44100;
        }else if (_videoInfo.audioSampleRate == 48000){
            audioSampleRate = AUDIO_SAMPLERATE_48000;
        }
        
        // 设置录像的保存路径
        _recordPath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"record.mp4"];
        _resultPath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"result.mp4"];
        
       // 播放器初始化
        TXPreviewParam *param = [[TXPreviewParam alloc] init];
        param.videoView = self.movieView;
        param.renderMode = RENDER_MODE_FILL_EDGE;
        _editor = [[TXVideoEditer alloc] initWithPreview:param];
        [_editor setVideoPath:mp4Path];
        _editor.previewDelegate = self;
       
        // 录像参数初始化
        _recorder = [TXUGCRecord shareInstance];
        TXUGCCustomConfig *recordConfig = [[TXUGCCustomConfig alloc] init];
        recordConfig.videoResolution = VIDEO_RESOLUTION_720_1280;
        //这里保证录制视频的帧率和合唱视频的帧率一致，否则可能出现音画不同步的现象
        //注意：这里获取的合唱视频的帧率是平均帧率，有可能为小数，做一下四舍五入操作
        recordConfig.videoFPS = (int)(_videoInfo.fps + 0.5);
        //这里保证录制视频的音频采样率和合唱视频的音频采样率一致，否则可能出现音画不同步的现象
        recordConfig.audioSampleRate = audioSampleRate;
        recordConfig.videoBitratePIN = 9600;
        recordConfig.maxDuration = _videoInfo.duration;
        _recorder.recordDelegate = self;
       
        // 启动相机预览
        [_recorder startCameraCustom:recordConfig preview:self.cameraView];
       
        // 视频拼接
        _joiner = [[TXVideoJoiner alloc] initWithPreview:nil];
        _joiner.joinerDelegate = self;
        [_joiner setVideoPathList:@[_recordPath, mp4Path]];
        }
:::
</dx-codeblock> 

[](id:step3)
### 3. 录制
录制部分，只要响应用户单击按钮调用 SDK 方法就可以了，为了方便起见，这里复用了这个按钮来显示当前状态。另外加上在进度条上显示进度的逻辑。
<dx-codeblock>
::: ios objective-c
    - (IBAction)onTapButton:(UIButton *)sender {
        [_editor startPlayFromTime:0 toTime:_videoInfo.duration];
        if ([_recorder startRecord:_recordPath coverPath:[_recordPath stringByAppendingString:@".png"]] != 0) {
            NSLog(@"相机启动失败");
        }
        [sender setTitle:@"录像中" forState:UIControlStateNormal];
        sender.enabled = NO;
         }

    #pragma mark TXVideoPreviewListener
    -(void) onPreviewProgress:(CGFloat)time
    {
        self.progressView.progress = time / _videoInfo.duration;    
    }
:::
</dx-codeblock>   

[](id:step4)
### 4. 拼接
录制好后开始完成拼接部分, 此处需要指定两个视频在结果中的位置，这里设置一左一右。
<dx-codeblock>
::: ios objective-c
    -(void)onRecordComplete:(TXUGCRecordResult*)result;
    {
        NSLog(@"录制完成，开始合成");
        [self.recordButton setTitle:@"合成中..." forState:UIControlStateNormal];
        
        //获取录制视频的宽高
        TXVideoInfo *videoInfo = [TXVideoInfoReader getVideoInfo:_recordPath];
        CGFloat width = videoInfo.width;
        CGFloat height = videoInfo.height;
        
        //录制视频和原视频左右排列
        CGRect recordScreen = CGRectMake(0, 0, width, height);
        CGRect playScreen = CGRectMake(width, 0, width, height);
        [_joiner setSplitScreenList:@[[NSValue valueWithCGRect:recordScreen],[NSValue valueWithCGRect:playScreen]] canvasWidth:width * 2 canvasHeight:height];
        [_joiner splitJoinVideo:VIDEO_COMPRESSED_720P videoOutputPath:_resultPath];
    }
:::
</dx-codeblock>  

[](id:step5)
### 5. 显示进度条
实现合成进度的委托方法, 在进度条中显示进度。

<dx-codeblock>
::: ios objective-c
    -(void) onJoinProgress:(float)progress
    {
        NSLog(@"视频合成中%d%%",(int)(progress * 100));
        self.progressView.progress = progress;
    }
:::
</dx-codeblock>  

[](id:step6)
### 6. 预览
实现合成完成的委托方法，并切换到预览界面。

<dx-codeblock>
::: ios objective-c
    #pragma mark TXVideoJoinerListener
    -(void) onJoinComplete:(TXJoinerResult *)result
    {
        NSLog(@"视频合成完毕");
        VideoPreviewController *controller = [[VideoPreviewController alloc] initWithVideoPath:_resultPath];
        [self.navigationController pushViewController:controller animated:YES];
    }
:::
</dx-codeblock>  

此就制作完成了，上面提到了一个视频预览的 `VideoPreviewController` 代码如下：
- **`VideoPreviewController.h`：**
  <dx-codeblock>
  ::: ios objective-c
    #import <UIKit/UIKit.h>

    @interface VideoPreviewController : UIViewController
    - (instancetype)initWithVideoPath:(NSString *)path;
      @end
      :::
      </dx-codeblock>  
- **`VideoPreviewController.m`：**
<dx-codeblock>
::: ios objective-c
    @import TXLiteAVSDK_UGC;

    @interface VideoPreviewController () <TXVideoPreviewListener>
    {
        TXVideoEditer *_editor;
    }
    @property (strong, nonatomic) NSString *videoPath;
    @end
  
    @implementation VideoPreviewController
  
    - (instancetype)initWithVideoPath:(NSString *)path {
        if (self = [super initWithNibName:nil bundle:nil]) {
            self.videoPath = path;
        }
        return self;
         }
    
    - (void)viewDidLoad {
        [super viewDidLoad];
        TXPreviewParam *param = [[TXPreviewParam alloc] init];
        param.videoView = self.view;
        param.renderMode = RENDER_MODE_FILL_EDGE;
    
        _editor = [[TXVideoEditer alloc] initWithPreview:param];
        _editor.previewDelegate = self;
        [_editor setVideoPath:self.videoPath];
        [_editor startPlayFromTime:0 toTime:[TXVideoInfoReader getVideoInfo:self.videoPath].duration];
         }
  
    -(void) onPreviewFinished
    {
        [_editor startPlayFromTime:0 toTime:[TXVideoInfoReader getVideoInfo:self.videoPath].duration];
    }
    @end
:::
</dx-codeblock>  

至此就完成了全部合唱的基础功能，功能更加丰富的示例请参见 [小视频源码](https://cloud.tencent.com/document/product/1449/56977#video_app)。
