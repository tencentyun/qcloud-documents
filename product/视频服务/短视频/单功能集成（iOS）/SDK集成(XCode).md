## 支持平台

SDK 支持 iOS 8.0 以上系统。

## 开发环境

+ Xcode 9 或更高版本。
+ OS X 10.10 或更高版本。

## 设置步骤

### 步骤1：链接 SDK 及系统库
1. 将下载的 SDK 资源包解压，并将 SDK 文件夹中 TXLiteAVSDK\_ 开头的 framework（如 TXLiteAVSDK_UGC.framework）复制到工程所在文件夹，并拖动到工程当中。
2. 选中工程的 Target，添加以下系统库：
  - Accelerate.framework
  - SystemConfiguration.framework
  - libc++.tbd
  - libsqlite3.tbd
添加完毕后，工程库依赖如下图所示：
![](https://main.qcloudimg.com/raw/a5fe16ca046a0aad84224e1ffa766a42.jpg)
3. 选中工程的 Target，在 Build Settings 中搜索 bitcode，将 Enable Bitcode 设置为 NO。

### 步骤2：配置 App 权限
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

### 步骤3：SDK License 设置与基本信息获取
通过 [License 申请](https://cloud.tencent.com/document/product/584/20333) 的指引申请 License 后，从 [控制台](https://console.cloud.tencent.com/vod/license) 复制 key 和 url，见下图。
![](https://main.qcloudimg.com/raw/a4c1de10918d04b0b425febe9d0a009b.png)
在您的应用中使用短视频功能之前，建议在`- [AppDelegate application:didFinishLaunchingWithOptions:]`中进行如下设置：

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

>?
- 对于使用**4.7版本 License 的用户**，如果您升级了 SDK 到4.9版本，您可以登录控制台，单击下图的【切换到新版License】生成对应的 key 和 url，切换后的 License 必须使用4.9及更高的版本，切换后按照上述操作集成即可。
![](https://main.qcloudimg.com/raw/c877efe3f57e853615e68a35e20fd8b9.png)
- 企业版请参考 [动效变脸](https://cloud.tencent.com/document/product/584/13509)。

### 步骤4：Log 配置
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，相关接口如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。
- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前 App 的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将此开关打开，在重现问题后提供 log 文件，非常感谢您的支持。
- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。
``` objc
  [TXLiveBase setConsoleEnabled:YES];
  [TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```

### 步骤5：编译运行

如果前面各步骤都操作正确的话，HelloSDK 工程就可以顺利编译通过。在 Debug 模式下运行 App，Xcode 的 Console 窗格会打印出 SDK 的版本信息：
```
2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 5.2.5541
```

## 快速接入功能模块
为了方便您快速集成 SDK 各项功能，我们提供了 UGCKit。UGCKit 是在短视频 SDK 基础上构建的一套 UI 组件库。

您可以通过 [GitHub](https://github.com/tencentyun/UGSVSDK/tree/master/iOS) 或 [资源下载](https://cloud.tencent.com/document/product/584/9366) 中提供的 SDK 压缩包获取 UGCKit。UGCKit 位于压缩包 Demo/TXLiteAVDemo/UGC/UGCKit 目录下。

### UGCKit 开发环境要求
- Xcode 10 及以上。
- iOS 9.0 及以上。

### 步骤1：集成 UGCKit 
1. **导入 UGCKit 与 BeautyPannel (BeautySettingKit)**
	1. 将 `Demo/TXLiteAVDemo/UGC/UGCKit` 文件夹拷贝到工程目录中，并将 UGCKit 中的 `UGCKit.xcodeproj` 拖拽到工程中。
	2. 将 `Demo/TXLiteAVDemo/BeautySettingKit` 文件夹拷贝到工程目录中，并将 BeautySettingKit 中的`TCBeautyPanel.xcodeproj` 拖拽到工程中。
![](https://main.qcloudimg.com/raw/48fa8833ea243bba61eec09bbdb38d33.png)
2. **配置依赖关系**   
单击工程的 Target，选择 Build Phase 标签，在 Dependencies 中单击加号，选择 `UGCKit.framework`、 `UGCKitResources`、`TCBeautyPanel.framework` 和 `TCBeautyPanelResources`，单击【Add】。
![](https://main.qcloudimg.com/raw/098808d270672bd4413fbca2d92b7e4a.png )
3. **链接 UGCKit.framework, TCBeautyPannel.framework 和 SDK**
  1. 单击工程的 Target，选择 Build Phase 标签，在 Link Binary With Libraries 中单击加号，选择 `UGCKit.framework`，`TCBeautyPannel.framework` 添加。
![](https://main.qcloudimg.com/raw/ccbc89f8a0ff68ac4e9159c9388070b7.png)
  2. 在 Finder 中打开 SDK 目录，将 SDK 拖动到 Link Binary With Libraries 中，或者通过下图示例在 xcode 中找到 SDK 对应的目录，通过 Add files 添加。
![](https://main.qcloudimg.com/raw/8432ca1427b51e65ff40e10bb460bbf9.png)
  3. 将 TXLiteAVDemo/App/Resource 目录下的 `FilterResource.bundle` 拖动到工程中并勾选 App Target。
4. **导入资源**
	1. 单击工程的 Target，选择 Build Phase 标签，展开 Copy Bundle Resources。
	2. 在左侧目录中依次展开 UGCKit.xcodeproj、Products，拖动 `UGCKitResources.bundle` 到 Copy Bundle Resources 中，而后依次展开 `TCBeautyPannel.xcodeproj`，Products。
	3. 拖动 `TCBeautyPanelResources.bundle` 到 Copy Bundle Resources中。
![](https://main.qcloudimg.com/raw/6377d1c7b240e008f240d116e5363a8b.png)
5. **导入商业版资源（仅用于商业版）**
将商业版 SDK zip 包中 EnterprisePITU（在App/AppCommon目录下）文件夹拖动到工程中，选择“Create groups"并勾选您的 Target，单击【Finish】。

### 步骤2：使用 UGCKit

1. **录制**
`UGCKitRecordViewController`提供了完整的录制功能，您只需实例化这个控制器后展现在界面中即可。
<dx-codeblock>
::: XCode 
UGCKitRecordViewController *recordViewController = [[UGCKitRecordViewController alloc] initWithConfig:nil theme:nil];
[self.navigationController pushViewController:recordViewController]
```
录制后的结果将通过 completion block 回调，示例如下：
```
   recordViewController.completion = ^(UGCKitResult *result) {
       if (result.error) {
           // 录制出错
          [self showAlertWithError:error];
       } else {
           if (result.cancelled) {
               // 用户取消录制，退出录制界面
               [self.navigationController popViewControllerAnimated:YES];
          } else {
               // 录制成功, 用结果进行下一步处理
               [self processRecordedVideo:result.media];
           }
       }
   };
:::
</dx-codeblock>
2. **编辑**
`UGCKitEditViewController`提供了完整的图片转场和视频编辑功能，实例化时需要传入待编辑的媒体对象，以处理录制结果为例，示例如下：
<dx-codeblock>
::: XCode 
   - (void)processRecordedVideo:(UGCKitMedia *)media {
       // 实例化编辑控制器
       UGCKitEditViewController *editViewController = [[UKEditViewController alloc] initWithMedia:media conifg:nil theme:nil];
       // 展示编辑控制器
       [self.navigationController pushViewController:editViewController animated:YES];
```
编辑后的结果将通过 completion block 回调，示例如下：
```
       editViewController.completion = ^(UGCKitResult *result) {
       if (result.error) {
           // 出错
          [self showAlertWithError:error];
       } else {
           if (result.cancelled) {
               // 用户取消录制，退出编辑界面
               [self.navigationController popViewControllerAnimated:YES];
          } else {
               // 编辑保存成功, 用结果进行下一步处理
               [self processEditedVideo:result.path];
           }
       }
   }
:::
</dx-codeblock>
3. **从相册中选择视频或图片**
`UGCKitMediaPickerViewController`用来处理媒体的选择与合并，当选择多个视频时，将会返回拼接后的视频。示例如下：
<dx-codeblock>
::: XCode 
   // 初始化配置
   UGCKitMediaPickerConfig *config = [[UGCKitMediaPickerConfig alloc] init];
   config.mediaType = UGCKitMediaTypeVideo;//选择视频
   config.maxItemCount = 5;                //最多选5个

   // 实例化媒体选择器
   UGCKitMediaPickerViewController *mediaPickerViewController = [[UGCKitMediaPickerViewController alloc] initWithConfig:config theme:nil];
   // 展示媒体选择器
   [self presentViewController:mediaPickerViewController animated:YES completion:nil];
   ```
   选择的结果将通过 completion block 回调，示例如下：
   ```
   mediaPickerViewController.completion = ^(UGCKitResult *result) {
     if (result.error) {
         // 出错
         [self showAlertWithError:error];
     } else {
          if (result.cancelled) {
               // 用户取消录制，退出选择器界面
               [self dismissViewControllerAnimated:YES completion:nil];
          } else {
               // 编辑保存成功, 用结果进行下一步处理
               [self processEditedVideo:result.media];
          }
     }
   }
:::
</dx-codeblock>
4. **裁剪**
`UGCKitCutViewController`提供视频的裁剪功能，与编辑接口相同，在实例化时传入媒体对象，在 completion 中处理剪辑结果即可。示例如下：
<dx-codeblock>
::: XCode 
   UGCKitMedia *media = [UGCKitMedia mediaWithVideoPath:@"<#视频路径#>"];
   UGCKitCutViewController *cutViewController = [[UGCKitCutViewController alloc] initWithMedia:media theme:nil];
   cutViewController.completion = ^(UGCKitResult *result) {
        if (!result.cancelled && !result.error) {
             [self editVideo:result.media];
        } else {
             [self.navigationController popViewControllerAnimated:YES];
        }
   }
   [self.navigationController pushViewController: cutViewController]
:::
</dx-codeblock>
   

## 详细介绍
以下为 SDK 各模块的详细说明：

- [视频录制](https://cloud.tencent.com/document/product/584/9367)
- [视频编辑](https://cloud.tencent.com/document/product/584/9375)
- [视频拼接](https://cloud.tencent.com/document/product/584/9370)
- [视频上传](https://cloud.tencent.com/document/product/584/15534)
- [视频播放](https://cloud.tencent.com/document/product/584/9372)
- [动效变脸（企业版）](https://cloud.tencent.com/document/product/584/13509)
