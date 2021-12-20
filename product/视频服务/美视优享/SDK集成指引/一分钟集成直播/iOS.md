## 集成准备

1. 解压 Demo 包。
2. 将 Demo工程中的 xmagic 模块（bundle，XmagicIconRes，Xmagic文件夹）导入到实际项目工程中。
3. 导入 SDK 目录中的 libpag.framework，Masonry.framework，XMagic.framework，YTCommonXMagic.framework。
4. framework 签名 **General--> Masonry.framework** 和 **libpag.framework** 选 **Embed & Sign**。
5. 将 Bundle ID 修改成与申请的测试授权一致。

## SDK 接口集成 
- [步骤一](step1) 和 [步骤二](#step2) 可参考 Demo 工程中，ThirdBeautyViewController 类 viewDidLoad，buildBeautySDK 方法。
- [步骤四](#step4) 至 [步骤七](#step7) 可参考 Demo 工程的 ThirdBeautyViewController，BeautyView 类相关实例代码。

### 步骤一：初始化授权[](id:step1)

1. 离线授权方式。
```
NSString *licensePath = [[NSBundle mainBundle] pathForResource:@"dev_test_v2_S1-04_2022-01-17.lic1.4.1" ofType:@""];
NSLog(@"youtu auth ret0 : %@", licensePath);
int authRet = [XMagicAuthManager initAuthByFilePath:licensePath withSecretKey:@"xxxxx"];
NSString *version = [XMagicAuthManager getVersion];
NSLog(@"youtu auth ret : %i", authRet);
NSLog(@"youtu auth version : %@", version);
```
2. 线上授权方式。
首先在工程 AppDelegate 的 didFinishLaunchingWithOptions 中添加如下代码：
```
[TXLiveBase setLicenceURL:@"" key:@""];
```
授权代码可参考 Demo 中 ThirdBeautyViewController 类 viewDidLoad 中的授权代码：
```
NSString *licenseInfo = [TXUGCBase getLicenceInfo];
NSData *jsonData = [licenseInfo dataUsingEncoding:NSUTF8StringEncoding];
NSError *err = nil;
NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:jsonData
options:NSJSONReadingMutableContainers error:&err];
NSString *xmagicLicBase64Str = [dic objectForKey:@"pituLicense"];
//初始化 xmagic 授权
int authRet = [XMagicAuthManager initAuthByString:xmagicLicBase64Str withSecretKey:@""];// withSecretKey 为空字符串, 不需要填写内容
NSLog(@"xmagic auth ret : %i", authRet);
NSLog(@"xmagic auth version : %@", [XMagicAuthManager getVersion]);
```
>! key 字段为申请 lic 时提供的 SecretKey。

### 步骤二：设置 SDK 素材资源路径[](id:step2)
```
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
```
    // Register log
    [self.beautyKit registerSDKEventListener:self];
    [self.beautyKit registerLoggerListener:self withDefaultLevel:YT_SDK_ERROR_LEVEL];
```

### 步骤四：配置美颜各种效果[](id:step4)

```
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

### 步骤五：将 textureId 传入到 SDK 内做渲染处理 [](id:step5)

```
[self.xMagicKit process:inputCPU withOrigin:YtLightImageOriginTopLeft withOrientation:YtLightCameraRotation0]
```
### 步骤六：暂停/恢复 SDK [](id:step6)

```
[self.beautyKit onPause];
[self.beautyKit onResume];
```

### 步骤七：布局中添加 SDK 美颜面板 [](id:step7)

```
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

