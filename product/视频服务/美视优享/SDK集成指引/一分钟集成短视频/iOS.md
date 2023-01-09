## 集成准备[](id:ready)

1. 下载并解压 [Demo 包](https://cloud.tencent.com/document/product/616/65875)，将 Demo 工程中 `demo/XiaoShiPin/` 目录下的 xmagickit 文件夹拷贝到您的工程 podfile 文件的同一级目录下。
2. 在您的 Podfile 文件中添加以下依赖，之后执行 `pod install` 命令，完成导入。
```
pod 'xmagickit', :path => 'xmagickit/xmagickit.podspec'
```
3. 将 Bundle ID 修改成与申请的测试授权一致。

### 开发者环境要求
- 开发工具 XCode 11 及以上：App Store 或单击 [下载地址](https://developer.apple.com/xcode/resources/)。
- 建议运行环境：
  - 设备要求：iPhone 5 及以上；iPhone 6 及以下前置摄像头最多支持到 720p，不支持 1080p。
  - 系统要求：iOS 12.0 及以上。


## SDK 接口集成 [](id:step)
### 步骤一：初始化授权 [](id:step1)
在工程 AppDelegate 的 didFinishLaunchingWithOptions 中添加如下代码，其中 LicenseURL，LicenseKey 为腾讯云官网申请到授权信息，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)：
```objectivec
[TXUGCBase setLicenceURL:LicenseURL key:LicenseKey];

[TELicenseCheck setTELicense:LicenseURLkey:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) {
              if (authresult == TELicenseCheckOk) {
                   NSLog(@"鉴权成功");
               } else {
                   NSLog(@"鉴权失败");
               }
       }];
```
**鉴权 errorCode 说明**：

| 错误码 | 说明                                                    |
| :----- | :------------------------------------------------------ |
| 0      | 成功。Success                                           |
| -1     | 输入参数无效，例如 URL 或 KEY 为空                      |
| -3     | 下载环节失败，请检查网络设置                            |
| -4     | 从本地读取的 TE 授权信息为空，可能是 IO 失败引起        |
| -5     | 读取 VCUBE TEMP License文件内容为空，可能是 IO 失败引起 |
| -6     | v_cube.license 文件 JSON 字段不对。请联系腾讯云团队处理 |
| -7     | 签名校验失败。请联系腾讯云团队处理                      |
| -8     | 解密失败。请联系腾讯云团队处理                          |
| -9     | TELicense 字段里的 JSON 字段不对。请联系腾讯云团队处理  |
| -10    | 从网络解析的 TE 授权信息为空。请联系腾讯云团队处理      |
| -11    | 把 TE 授权信息写到本地文件时失败，可能是 IO 失败引起      |
| -12    | 下载失败，解析本地 asset 也失败                         |
| -13    | 鉴权失败                                                |
| 其他   | 请联系腾讯云团队处理                                    |


### 步骤二：设置 SDK 素材资源路径 [](id:step2)

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
在短视频预处理帧回调接口，构造 YTProcessInput 将 textureId 传入到 SDK 内做渲染处理。

```
 [self.xMagicKit process:inputCPU withOrigin:YtLightImageOriginTopLeft withOrientation:YtLightCameraRotation0]
```

### 步骤六：暂停/恢复 SDK [](id:step6)

```objectivec
[self.beautyKit onPause];
[self.beautyKit onResume];
```

### 步骤七：布局中添加 SDK 美颜面板 [](id:step7)
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
