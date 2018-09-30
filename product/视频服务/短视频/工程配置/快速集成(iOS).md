# 快速接入腾讯云短视频SDK

本篇文档讲述了如何在空的项目中集成短视频SDK的录制、编辑、拼接的功能。

文中所需要的代码及资源文件均在[资源下载](https://cloud.tencent.com/document/product/584/9366)中SDK的压缩包中提供。

## 接入步骤

1. 参考[[license介绍]], 申请license。 如果没有license依然可以完成以下步骤集成UI，但部分功能会无法使用。

2. 新建一个`Single View App`, 打开Main.storyboard, 选侧左边的`View Controller Scene`, 依次从顶部菜单栏选则`Editor -> Embeded In -> Navigation Controller`。

3. 选中工程的Target，在Build Settings中搜索bitcode, 将Enable Bitcode设置为NO

4. 选中工程的Target, 在 Build phases / Link Binary With Libraries中添加以下依赖项

   1. Accelerate.framework
   2. SystemConfiguration.framework
   3. libc++
   4. libz
   5. libsqlite

5. 在Info.plist中增加相机和相册的权限提示,  可以在Info.plist中右键选`Open as / Source Code`， 在末尾的`</dict></plist>`之前粘贴以下内容
   ```
   <key>NSAppleMusicUsageDescription</key>
   <string>视频云工具包需要访问你的媒体库权限以获取音乐，不允许则无法添加音乐</string>
   <key>NSCameraUsageDescription</key>
   <string>视频云工具包需要访问你的相机权限，开启后录制的视频才会有画面</string>
   <key>NSMicrophoneUsageDescription</key>
   <string>视频云工具包需要访问你的麦克风权限，开启后录制的视频才会有声音</string>
   <key>NSPhotoLibraryAddUsageDescription</key>
   <string>视频云工具包需要访问你的相册权限，开启后才能保存编辑的文件</string>
   <key>NSPhotoLibraryUsageDescription</key>
   <string>视频云工具包需要访问你的相册权限，开启后才能编辑视频文件</string>
   ```

6. 拷贝以下文件夹并拖动到项目里
   1. Demo/TXLiteAVDemo/Common/UGC
   2. Demo/TXLiteAVDemo/Common/BeautySettingPanel
   3. Demo/TXLiteAVDemo/Common/Category
   4. Demo/TXLiteAVDemo/Common/Color
   5. Demo/TXLiteAVDemo/Common/Resource
   6. Demo/TXLiteAVDemo/Common/Third/Masonry
   7. Demo/TXLiteAVDemo/Common/Third/AFNetworking
   8. Demo/TXLiteAVDemo/Common/Third/MBProgressHUD
   9. Demo/TXLiteAVDemo/Common/Third/QBImagePicker
   10. Demo/TXLiteAVDemo/Common/Third/V8HorizontalPickerView
   11. Demo/TXLiteAVDemo/UGC
   12. SDK/TXLiteAVSDK_*.framework
      _在VideoJoinController.m 53行有一处HelpBtnUI的未定义方法，这行需要删掉_

7. 打开`ViewController.m`, 在`viewDidLoad`中添加三个按钮做为功能入口

    ```
    - (void)viewDidLoad {
        [super viewDidLoad];
        UIButton *editButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [editButton setTitle:@"编辑" forState:UIControlStateNormal];
        [editButton addTarget:self action:@selector(onEdit:) forControlEvents:UIControlEventTouchUpInside];
    
        UIButton *recordButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [recordButton setTitle:@"录制" forState:UIControlStateNormal];
        [recordButton addTarget:self action:@selector(onRecord:) forControlEvents:UIControlEventTouchUpInside];
        
        UIButton *joinButton = [UIButton buttonWithType:UIButtonTypeCustom];
        [joinButton setTitle:@"拼接" forState:UIControlStateNormal];
        [joinButton addTarget:self action:@selector(onJoin:) forControlEvents:UIControlEventTouchUpInside];
        
        CGPoint center = CGPointMake(CGRectGetMidX(self.view.bounds), 30);
        editButton.center = center;
        
        center.y += 50;
        recordButton.center = center;
        
        center.y += 50;
        joinButton.center = center;
        
        for (UIButton *button in @[editButton, recordButton, joinButton]) {
            [self.view addSubview:button];
        }
    }
    ```

8. 接下来在ViewController中添加几个按钮的事件处理方法
    这里要用到Demo中的一些控制器， 先要在ViewController.m 的头部导入头文件
    ```
    #import "QBImagePickerController.h"
    #import "VideoRecordConfigViewController.h"
    #import "VideoRecordViewController.h"
    #import "VideoEditViewController.h"
    #import "VideoJoinerController.h"
    #import "VideoPreviewViewController.h"
    ```
    另外需要在ViewController中增加一个变量记录视频选则的上下文
    ```
    @interface ViewController ()
    {
        ComposeMode _composeMode;
    }
    ```
    然后添加以下按钮事件处理方法

    ```
    // 选则视频并进入编辑
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
                [nav presentViewController:nav animated:YES completion:nil];
            };
            [weakConfigVC.navigationController pushViewController:recordVC animated:YES];
        };
        [self.navigationController pushViewController:configViewController animated:YES];
    }
    
    // 选则视频并进入拼接
    - (void)onJoin:(id)sender {
        QBImagePickerController *videoPicker = [[QBImagePickerController alloc] init];
        videoPicker.delegate = self;
        videoPicker.allowsMultipleSelection = YES;
        videoPicker.mediaType = QBImagePickerMediaTypeVideo;
        _composeMode = ComposeMode_Join;
        [self presentViewController:videoPicker animated:YES completion:nil];
    }
    ```

9. 添加点选照片的回调处理方法
    先声明ViewController实现了QBImagePicker的委托方法, 将ViewController.m的前面修改为

    ```
    @interface ViewController () <QBImagePickerControllerDelegate>
    @end
    ```

    然后增加以下方法

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

10. 打开AppDelegate, 在`application:didFinishLaunchingWithOptions:`中添加license的设置，license的申请方法请参见[[license介绍]]
     ```objc
     - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
         // 如果没有license可以先传两个空的字符串, 以下为示例，请填写实际申请下来的信息
         [TXUGCBase setLicenceURL:@"https://license.vod2.myqcloud.com/xxxxxxxxxxx/TXUgcSDK.licence" key:@"xxxxxxxxxxx"];
         return YES;
     }
     ```

11. 运行项目



### 相关文件简介

#### 主功能的类及图片资源

UGC中各界面的类如下所示

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
Demo中使用到的公有模块及第三方库如下所示

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

1. [视频录制](https://cloud.tencent.com/document/product/584/9367)
2. [视频编辑](https://cloud.tencent.com/document/product/584/9375)
3. [视频拼接](https://cloud.tencent.com/document/product/584/9370)
4. [视频上传](https://cloud.tencent.com/document/product/584/15534)
5. [视频播放](https://cloud.tencent.com/document/product/584/9372)
6. [动效变脸(商业版)](https://cloud.tencent.com/document/product/584/13509)