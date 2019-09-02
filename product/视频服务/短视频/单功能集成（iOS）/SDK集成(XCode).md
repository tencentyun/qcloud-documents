
## 工程配置
### 支持平台

+ SDK 支持 iOS 8.0 以上系统。

### 开发环境

+ Xcode 9 或更高版本；
+ OS X 10.10 或更高版本；

### 设置步骤

#### 1.链接 SDK 及系统库
1. 将下载的 SDK 资源包解压，并将 SDK 文件夹中的 TXLiteAVSDK_ 开头的 framework(如 TXLiteAVSDK_UGC.framework)复制到工程所在文件夹,并拖动到工程当中。

2. 选中当工程的 Target，添加以下系统库
    1. Accelerate.framework
    2. SystemConfiguration.farmework
    3. libc++.tbd
    4. libsqlite3.tbd

    添加完毕后，工程库依赖如下图所示：![](https://main.qcloudimg.com/raw/a5fe16ca046a0aad84224e1ffa766a42.jpg)
    
3. 选中工程的Target，在Build Settings中搜索bitcode, 将Enable Bitcode设置为NO

#### 2. 配置 App 权限
应用会需要相册及相册的访问权限，需要在 Info.plist 中添加对应项，可以通过在 Info.plist 中右键选 Open as / Source Code 粘贴并修改以下内容进行配置。
```
<key>NSAppleMusicUsageDescription</key> 
<string>视频云工具包需要访问您的媒体库权限以获取音乐，不允许则无法添加音乐</string> 
<key>NSCameraUsageDescription</key> 
<string>视频云工具包需要访问您的相机权限，开启后录制的视频才会有画面</string> 
<key>NSMicrophoneUsageDescription</key> 
<string>视频云工具包需要访问您的麦克风权限，开启后录制的视频才会有声音</string> 
<key>NSPhotoLibraryAddUsageDescription</key> 
<string>视频云工具包需要访问您的相册权限，开启后才能保存编辑的文件</string> 
<key>NSPhotoLibraryUsageDescription</key> 
<string>视频云工具包需要访问您的相册权限，开启后才能编辑视频文件</string> 
```

#### 3. SDK License 设置与基本信息获取
请参考 [License申请](https://cloud.tencent.com/document/product/584/20333) 的指引申请 License 后，从 [控制台](https://console.cloud.tencent.com/vod/license) 复制 key 和 url，见下图。
![](https://main.qcloudimg.com/raw/1124501484177029a7c0e084dfe16ed6.png)
  在您的应用中使用短视频功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置

```objc
@import TXLiteAVSDK_UGC;
@implementation AppDelegate
- (BOOL)application:(UIApplication*)applicationdidFinishLaunchingWithOptions:(NSDictinoary*)options {
    NSString * const licenceURL = @"<获取到的licnseUrl>";
    NSString * const licenceKey = @"<获取到的key>";
    [TXUGCBase setLicenceURL:licenceURL key:licenceKey];
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

- 对于使用 4.7 版本 license 的用户，如果您升级了 SDK 到 4.9 版本，您可以登录控制台，单击下图的 **切换到新版License** 按钮生成对应的 key 和 url，切换后的 License 必须使用 4.9 及更高的版本，切换后按照上述操作集成即可。
 ![](https://main.qcloudimg.com/raw/2da38ac76074377702ff383aeba50f0a.png)

- 商业版请参考 [动效变脸](https://cloud.tencent.com/document/product/584/13509)。

#### 4. Log 配置
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，相关接口如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。

- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前 App 的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将此开关打开，在重现问题后提供 log 文件，非常感谢您的支持。

- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。

  ```	objc
  [TXLiveBase setConsoleEnabled:YES];
  [TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
  ```

#### 5. 编译运行

如果前面各个步骤都操作正确的话，HelloSDK 工程就可以顺利编译通过。在 Debug 模式下运行 App，Xcode 的 Console 窗格会打印出 SDK 的版本信息。

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 5.2.5541

## 快速接入功能模块

下面讲述了如何集成短视频 SDK 的录制、编辑、拼接的功能。

文中所需要的代码及资源文件均在 [资源下载](https://cloud.tencent.com/document/product/584/9366) 中 SDK 的压缩包中提供。

### 接入步骤

1. 拷贝以下文件夹并拖动到项目里  
   - Demo/TXLiteAVDemo/Common/UGC
   - Demo/TXLiteAVDemo/Common/BeautySettingPanel
   - Demo/TXLiteAVDemo/Common/Category
   - Demo/TXLiteAVDemo/Common/Color
   - Demo/TXLiteAVDemo/Common/Resource
   - Demo/TXLiteAVDemo/Third/Masonry
   - Demo/TXLiteAVDemo/Third/AFNetworking
   - Demo/TXLiteAVDemo/Third/MBProgressHUD
   - Demo/TXLiteAVDemo/Third/QBImagePicker
   - Demo/TXLiteAVDemo/Third/V8HorizontalPickerView
   - Demo/TXLiteAVDemo/UGC
   - SDK/TXLiteAVSDK_*.framework
   
2. 打开`ViewController.m`, 在`viewDidLoad`中添加三个按钮作为功能入口：

    ```
    - (void)viewDidLoad {
        [super viewDidLoad];
        self.view.backgroundColor = [UIColor grayColor];
        UIButton *editButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [editButton setTitle:@"编辑" forState:UIControlStateNormal];
        [editButton addTarget:self action:@selector(onEdit:) forControlEvents:UIControlEventTouchUpInside];
    
        UIButton *recordButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [recordButton setTitle:@"录制" forState:UIControlStateNormal];
        [recordButton addTarget:self action:@selector(onRecord:) forControlEvents:UIControlEventTouchUpInside];
        
        UIButton *joinButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [joinButton setTitle:@"拼接" forState:UIControlStateNormal];
        [joinButton addTarget:self action:@selector(onJoin:) forControlEvents:UIControlEventTouchUpInside];
        
        CGPoint center = CGPointMake(CGRectGetMidX(self.view.bounds), 150);
        editButton.center = center;
        
        center.y += 80;
        recordButton.center = center;
        
        center.y += 80;
        joinButton.center = center;
        
        for (UIButton *button in @[editButton, recordButton, joinButton]) {
            [self.view addSubview:button];
        }
    }
    ```

3. 接下来在 ViewController 中添加几个按钮的事件处理方法：
    这里要用到 Demo 中的一些控制器， 先要在 ViewController.m 的头部导入头文件：
    ```
    #import "QBImagePickerController.h"
    #import "VideoRecordConfigViewController.h"
    #import "VideoRecordViewController.h"
    #import "VideoEditViewController.h"
    #import "VideoJoinerController.h"
    #import "VideoPreviewViewController.h"
    #import "VideoLoadingController.h"
    ```
    另外需要在 ViewController 中增加一个变量记录视频选择的上下文：
    ```
    @interface ViewController ()
    {
        ComposeMode _composeMode;
    }
    ```
    然后添加以下按钮事件处理方法：

    ```
    // 选择视频并进入编辑
    - (void)onEdit:(id)sender {
        QBImagePickerController *videoPicker = [[QBImagePickerController alloc] init];
        videoPicker.delegate = self;
        videoPicker.mediaType = QBImagePickerMediaTypeVideo;
        _composeMode = ComposeMode_Edit;
        [self presentViewController:videoPicker animated:YES completion:nil];
    }
    
    - (void)onRecord:(id)sender {
        // 实例化录制设置界面
        VideoRecordConfigViewController *configViewController = [[VideoRecordConfigViewController alloc] init];
        
        __weak VideoRecordConfigViewController *weakConfigVC = configViewController;
        // 设置界面中点击开始录制的回调
        configViewController.onTapStart = ^(VideoRecordConfig *configure) {
            VideoRecordViewController *recordVC = [[VideoRecordViewController alloc] initWithConfigure:configure];
            
            // 设置录制完成回调
            recordVC.onRecordCompleted = ^(TXUGCRecordResult *result) {
                
                // 实例化预览视图控制器
                VideoPreviewViewController* previewController = [[VideoPreviewViewController alloc] initWithCoverImage:result.coverImage videoPath:result.videoPath renderMode:RENDER_MODE_FILL_EDGE showEditButton:YES];
                
                // 设置预览界面点击编辑回调
                previewController.onTapEdit = ^(VideoPreviewViewController *previewVC){
                    // 实例化编辑视图控制器
                    VideoEditViewController *editVC = [[VideoEditViewController alloc] init];
                    // 设置要编辑的视频路径
                    [editVC setVideoPath:result.videoPath];
                    
                    // 推入界面
                    [previewVC.navigationController pushViewController:editVC animated:YES];
                };
                
                UINavigationController* nav = [[UINavigationController alloc] initWithRootViewController:previewController];
                [weakConfigVC.navigationController presentViewController:nav animated:YES completion:nil];
            };
            [weakConfigVC.navigationController pushViewController:recordVC animated:YES];
        };
        self.navigationController.navigationBar.hidden = YES;
        [self.navigationController pushViewController:configViewController animated:YES];
    }
    
    // 选择视频并进入拼接
    - (void)onJoin:(id)sender {
        QBImagePickerController *videoPicker = [[QBImagePickerController alloc] init];
        videoPicker.delegate = self;
        videoPicker.allowsMultipleSelection = YES;
        videoPicker.mediaType = QBImagePickerMediaTypeVideo;
        _composeMode = ComposeMode_Join;
        [self presentViewController:videoPicker animated:YES completion:nil];
    }

    // 录制参数设置界面会隐藏导航条，这里恢复导航的显示
    - (void)viewWillAppear:(BOOL)animated
    {
        [super viewWillAppear:animated];
        self.navigationController.navigationBar.hidden = NO;
    }
    ```

4. 添加点选照片的回调处理方法：
    先声明 ViewController 实现了 QBImagePicker 的委托方法, 将 ViewController.m 的前面修改为：

    ```
    @interface ViewController () <QBImagePickerControllerDelegate>
    @end
    ```

    然后增加以下方法：

    ```
    - (void)qb_imagePickerControllerDidCancel:(QBImagePickerController *)imagePickerController {
        [self dismissViewControllerAnimated:YES completion:nil];
    }
    
    - (void)qb_imagePickerController:(QBImagePickerController *)imagePickerController didFinishPickingAssets:(NSArray *)assets {
        VideoLoadingController *loadvc = [[VideoLoadingController alloc] init];
        loadvc.composeMode = _composeMode;
        UINavigationController *nav = [[UINavigationController alloc] initWithRootViewController:loadvc];
        [self dismissViewControllerAnimated:YES completion:^{
            [self presentViewController:nav animated:YES completion:nil];        
            [loadvc exportAssetList:assets assetType: AssetType_Video];
        }];
    }
    ```

5. 打开 AppDelegate, 在`application:didFinishLaunchingWithOptions:`中添加 license 的设置，license 的申请方法请参见 License 介绍：
     ```objc
     - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
         // 如果没有 license 可以先传两个空的字符串, 以下为示例，请填写实际申请下来的信息。
         [TXUGCBase setLicenceURL:@"https://license.vod2.myqcloud.com/xxxxxxxxxxx/TXUgcSDK.licence" key:@"xxxxxxxxxxx"];
         return YES;
     }
     ```

6. 运行项目


### 相关文件简介

#### 主功能的类及图片资源

UGC 中各界面的类如下所示：

```
UGC
├── Edit (视频编辑)
│   ├── Resources (贴纸等资源)
│   ├── VideoEditViewController (编辑主界面)
│   ├── VideoEditor.xcassets (编辑界面图片资源)
│   ├── VideoPasterViewController (贴纸编辑)
│   ├── VideoTextViewController     (字幕编辑)
│   └── Views
│       ├── BottomTabBar 编辑界面底部工具菜单
│       ├── EffectSelectView 效果选择工具栏
│       ├── FilterSettingView 编辑滤镜选择工具栏
│       ├── MusicCollectionCell 音乐选择cell
│       ├── MusicMixView        背景音乐设置工具栏界面
│       ├── PasterAddView       贴纸设置工具栏界面“贴纸选项”
│       ├── PasterSelectView    贴纸选择界面
│       ├── TXCVEFColorPalette  颜色板，用于给不同特效的时间线及按钮设定一个颜色
│       ├── TextAddView         字幕添加界面
│       ├── TextCollectionCell  字幕背景cell
│       ├── TimeSelectView      字幕背设置工具栏界面
│       ├── TransitionView      图片转场设置界面
│       ├── VideoCutView        带缩略图的视频裁剪界面，包含了视频裁剪、按时间片段染色等功能
│       ├── VideoPasterView     贴纸输入组件，包含动态/静态贴纸输入、贴纸拖动、放大、旋转、删除等功能，用于VideoPasterViewController
│       └── VideoRangeSlider    用于VideoCutView, 显示缩图、给时间段染色
├── Join
│   ├── VideoEditPrevController (视频拼接预览界面)
│   ├── VideoJoiner.xcassets     (视频拼接图片资源)
│   └── VideoJoinerController    (视频列表界面)
├── Preview
│   ├── VideoPreview.xcassets   (视频预览界面图片资源)
│   └── VideoPreviewViewController  (视频预览界面)
├── Record
│   ├── VideoRecord.xcassets  (录制界面图片资源)
│   ├── VideoRecordConfigViewController  (录制参数设置界面)
│   └── VideoRecordViewController (录制界面)
└── VideoLoading (用于从iCloud下载图片)
```

#### 使用到的公有模块
Demo 中使用到的公有模块及第三方库如下所示：

```
Common
├── BeautySettingPanel (美颜设置控件)
├── Catetory (UIKit扩展)
├── ForEnterprise (商业版AI动效资源)
├── Resource
│   ├── Common.xcassets (返回按钮等公用资源)
│   └── Filter (滤镜资源包)
├── TCHttpUtil (视频上传)
└── UGC (短视频各子模块的公有类)

Third
├── AFNetworking (HTTP网络封装，商业版用于下载动态贴纸资源)
├── MBProgressHUD (界面Toast提示)
├── Masonry (自动布局)
├── QBImagePicker (图片选取)
├── V8HorizontalPickerView (水平滚动界面，用于编辑界面滤镜选则)
└── ZipArchive  (zip封装，商业版中用于解压动态贴纸资源)
```


### 详细介绍
以下为各模块的详细说明

1. [视频录制](https://cloud.tencent.com/document/product/584/9367)；
2. [视频编辑](https://cloud.tencent.com/document/product/584/9375)；
3. [视频拼接](https://cloud.tencent.com/document/product/584/9370)；
4. [视频上传](https://cloud.tencent.com/document/product/584/15534)；
5. [视频播放](https://cloud.tencent.com/document/product/584/9372)；
6. [动效变脸(商业版)](https://cloud.tencent.com/document/product/584/13509)；
