## 集成准备

1. 下载并解压 [Demo 包](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/iOS/2.4.1vcube/TRTC-API-Example.zip)，将 Demo 工程中的 xmagic 模块（bundle，XmagicIconRes，Xmagic 文件夹）导入到实际项目工程中。
2. 导入 SDK 目录中的 `libpag.framework`，`Masonry.framework`，`XMagic.framework`，`YTCommonXMagic.framework`。
3. framework 签名 **General--> Masonry.framework** 和 **libpag.framework** 选 **Embed & Sign**。
4. 将 Bundle ID 修改成与申请的测试授权一致。

### 开发者环境要求

- 开发工具 XCode 11 及以上：App Store 或单击 [下载地址](https://developer.apple.com/xcode/resources/)。
- 建议运行环境：
  - 设备要求：iPhone 5 及以上；iPhone 6 及以下前置摄像头最多支持到 720p，不支持 1080p。
  - 系统要求：iOS 10.0 及以上。

### C/C++层开发环境

XCode 默认 C++ 环境。

<table>
<tr><th>类型</th><th>依赖库</th></tr>
<tr>
<td>系统依赖库</td>
<td><ul style="margin:0">
<li/>Accelerate
<li/>AssetsLibrary
<li/>AVFoundation
<li/>CoreMedia  
<li/>CoreFoundation
<li/>CoreML
<li/>Foundation
<li/>JavaScriptCore
<li/>libc++.tbd
<li/>libz.b
<li/>libresolv.tbd
<li/>libsqlite3.0.tbd
<li/>MetalPerformanceShaders
<li/>MetalKit
<li/>MobileCoreServices
<li/>OpneAL
<li/>OpneGLES
<li/>Security
<li/>ReplayKit
<li/>SystemConfiguration
<li/>UIKit
</ul></td>
</tr>
<tr>
<td>自带的库</td>
<td><ul style="margin:0">
<li/>YTCommon（鉴权静态库）
<li/>XMagic（美颜静态库）
<li/>libpag（视频解码动态库）
<li/>Masonry（控件布局库）
<li/>TXLiteAVSDK_Professional
<li/>TXFFmpeg
<li/>TXSoundTouch
</ul></td>
</tr>
</table>

## SDK 接口集成 

- [步骤一](#step1) 和 [步骤二](#step2) 可参考 Demo 工程中，ThirdBeautyViewController 类 viewDidLoad，buildBeautySDK 方法；AppDelegate类的application方法进行了Xmagic鉴权。
- [步骤四](#step4) 至 [步骤七](#step7) 可参考 Demo 工程的 ThirdBeautyViewController，BeautyView 类相关实例代码。

### 步骤一：初始化授权[](id:step1)

1. 首先在工程 AppDelegate 的 didFinishLaunchingWithOptions 中添加如下鉴权代码，其中 LicenseURL 和 LicenseKey 为腾讯云官网申请到授权信息，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)：
```
[TXLiveBase setLicenceURL:LicenseURL key:LicenseKey];
```
2. Xmagic 鉴权：在相关业务模块的初始化代码中设置 URL 和 KEY，触发 License 下载，避免在使用前才临时去下载。也可以在 AppDelegate 的 didFinishLaunchingWithOptions 方法里触发下载。其中，LicenseURL 和 LicenseKey 是控制台绑定 License 时生成的授权信息。
```
[TELicenseCheck setTELicense:LicenseURL key:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) {
       if (authresult == TELicenseCheckOk) {
            NSLog(@"鉴权成功");
        } else {
            NSLog(@"鉴权失败");
        }
    }];
```
**鉴权 errorCode 说明**：
<table>
<thead>
<tr>
<th>错误码</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>0</td>
<td>成功。Success</td>
</tr>
<tr>
<td>-1</td>
<td>输入参数无效，例如 URL 或 KEY 为空</td>
</tr>
<tr>
<td>-3</td>
<td>下载环节失败，请检查网络设置</td>
</tr>
<tr>
<td>-4</td>
<td>从本地读取的 TE 授权信息为空，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-5</td>
<td>读取 VCUBE TEMP License文件内容为空，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-6</td>
<td>v_cube.license 文件 JSON 字段不对。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-7</td>
<td>签名校验失败。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-8</td>
<td>解密失败。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-9</td>
<td>TELicense 字段里的 JSON 字段不对。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-10</td>
<td>从网络解析的 TE 授权信息为空。请联系腾讯云团队处理</td>
</tr>
<tr>
<td>-11</td>
<td>把TE授权信息写到本地文件时失败，可能是 IO 失败引起</td>
</tr>
<tr>
<td>-12</td>
<td>下载失败，解析本地 asset 也失败</td>
</tr>
<tr>
<td>-13</td>
<td>鉴权失败</td>
</tr>
<tr>
<td>其他</td>
<td>请联系腾讯云团队处理</td>
</tr>
</tbody></table>

### 步骤二：设置 SDK 素材资源路径[](id:step2)

```objectivec
CGSize previewSize = [self getPreviewSizeByResolution:self.currentPreviewResolution];
NSString *beautyConfigPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) lastObject];
beautyConfigPath = [beautyConfigPath stringByAppendingPathComponent:@"beauty_config.json"];
NSFileManager *localFileManager=[[NSFileManager alloc] init];
BOOL isDir = YES;
NSDictionary * beautyConfigJson = @{};
if ([localFileManager fileExistsAtPath:beautyConfigPath isDirectory:&isDir] && !isDir) {
    NSString *beautyConfigJsonStr = [NSString stringWithContentsOfFile:beautyConfigPath encoding:NSUTF8StringEncoding error:nil];
    NSError *jsonError;
	NSData *objectData = [beautyConfigJsonStr dataUsingEncoding:NSUTF8StringEncoding];
	beautyConfigJson = [NSJSONSerialization JSONObjectWithData:objectData
											options:NSJSONReadingMutableContainers
											error:&jsonError];
}
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",
                            @"root_path":[[NSBundle mainBundle] bundlePath],
                            @"tnn_"
                            @"beauty_config":beautyConfigJson
};
// Init beauty kit
self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
```

### 步骤三：添加日志和事件监听[](id:step3)

```objectivec
 // Register log
[self.beautyKit registerSDKEventListener:self];
[self.beautyKit registerLoggerListener:self withDefaultLevel:YT_SDK_ERROR_LEVEL];
```

### 步骤四：配置美颜各种效果[](id:step4)

```objectivec
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

### 步骤五：进行渲染处理[](id:step5)
在视频帧回调接口，构造 YTProcessInput 传入到 SDK 内做渲染处理，可参考 Demo 中的 ThirdBeautyViewController。
```objectivec
 [self.xMagicKit process:inputCPU withOrigin:YtLightImageOriginTopLeft withOrientation:YtLightCameraRotation0]
```

### 步骤六：暂停/恢复 SDK [](id:step6)

```objectivec
[self.beautyKit onPause];
[self.beautyKit onResume];
```

### 步骤七：布局中添加 SDK 美颜面板[](id:step7)
```objectivec
UIEdgeInsets gSafeInset;
#if __IPHONE_11_0 && __IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_11_0
if(gSafeInset.bottom > 0){
}
if (@available(iOS 11.0, *)) {
	gSafeInset = [UIApplication sharedApplication].keyWindow.safeAreaInsets;
} else
#endif
	{
		gSafeInset = UIEdgeInsetsZero;
    }

dispatch_async(dispatch_get_main_queue(), ^{
    //美颜选项界面
    _vBeauty = [[BeautyView alloc] init];
    [self.view addSubview:_vBeauty];
    [_vBeauty mas_makeConstraints:^(MASConstraintMaker *make) {
        make.width.mas_equalTo(self.view);
        make.centerX.mas_equalTo(self.view);
        make.height.mas_equalTo(254);
        if(gSafeInset.bottom > 0.0){  // 适配全面屏
            make.bottom.mas_equalTo(self.view.mas_bottom).mas_offset(0);
        } else {
            make.bottom.mas_equalTo(self.view.mas_bottom).mas_offset(-10);
        }
    }];
    _vBeauty.hidden = YES;
});
```

