## 集成准备
### 开发者环境要求
- 开发工具XCode 11 及以上：App Store 或 [下载地址](https://developer.apple.com/xcode/resources/) 。
- 建议运行环境：
    - 设备要求：iPhone 5 及以上；iPhone 6 及以下前置摄像头最多支持到 720p，不支持 1080p
    - 系统要求：iOS 10.0 及以上。

### C/C++层开发环境
XCode 默认 C++ 环境。
<table>
<tr><th>类型</th><th>依赖库</th></tr>
<tr>
<td>系统依赖库</td>
<td><ul style="margin:0">
<li/>AVFoundation
<li/>Accelerate
<li/>AssetsLibrary
<li/>CoreML
<li/>JavaScriptCore
<li/>CoreFoundation
<li/>MetalPerformanceShaders
<li/>libc++.tbd
</ul></td>
</tr>
<tr>
<td>自带的库</td>
<td><ul style="margin:0">
<li/>YTCommon（鉴权静态库）
<li/>XMagic（美颜静态库）
<li/>libpag（视频解码动态库）
</ul></td>
</tr>
</table>

## 导入资源

### 资源
- 必需资源包：`LightCore.bundle`
- 分割功能包：`LightSegmentPlugin.bundle`
- 手势功能包：`LightHandPlugin.bundle`
- 3D 功能包：`Light3DPlugin.bundle`

### 导入方法
- **方法一**：加入到工程资源中即可。
- **方法二**：如果需要指定路径 `initWithRenderSize:assetsDict: (XMagic)` 可通过这里的 `assetsDict` 配置每个资源路径。

### 配置权限
在 Info.plist 文件中添加相应权限的说明，否则程序在 iOS 10 系统上会出现崩溃。请在 Privacy - Camera Usage Description 中开启相机权限，允许 App 使用相机。

## 集成步骤

### 步骤一：签名准备
framework 签名可以直接在 General-->Masonry.framework 和 libpag.framework 选 Embed & Sign。

### 步骤二：鉴权
1. 获取鉴权证书，将申请 License 过程获得的授权文件加入项目中，并确保添加到 Bundle Resources。
2. 加载鉴权库 `YTCommon.framework`，并对腾讯特效 SDK 进行鉴权。
<dx-tabs>
::: 离线授权
```
NSString *licensePath = [[NSBundle mainBundle] pathForResource:@"pitumotiondemo_S1-04_2021-07-24" ofType:@"lic"];
int authRet = [YTAuthManager initAuthByFilePath:licensePath withSecretKey:@""];
NSLog(@"youtu auth ret : %i", authRet);
```
:::
::: 线上授权（X - Magic 版本 2.4.0 + 支持线上授权方式）
```
[TESign setKeyUrl:@"key" url:@"url"];
NSString* lic = [TESign getLicenceInfo];
int authRet = 0;
NSError* error = noErr;
NSData * getJsonData = [lic dataUsingEncoding:NSUTF8StringEncoding];
NSDictionary * getDict = [NSJSONSerialization JSONObjectWithData:getJsonData options:NSJSONReadingMutableContainers error:&error];
authRet = [XMagicAuthManager initAuthByString:[getDict objectForKey:@"TELicense"] withSecretKey:@""];
NSLog(@"errorCode: %@, authRet: %d", error, authRet);
if(authRet!=0){
	NSLog(@"licenseInfo: %@", lic);
	UIAlertView * alert = [[UIAlertView alloc] initWithTitle:@"提醒" message:@"授权失败" delegate:nil cancelButtonTitle:@"取消" otherButtonTitles: nil];
	[alert show];
	return;
}
```
:::
</dx-tabs>

### 步骤三：加载 SDK：XMagic.framework

使用腾讯特效 SDK 生命周期大致如下:
1. 加载美颜相关资源。
```
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",
	@"root_path":[[NSBundle mainBundle] bundlePath]
};
```
2. 初始化美颜 SDK。
```
initWithRenderSize:assetsDict: (XMagic)
self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
```
3. 美颜 SDK 处理每帧数据并返回相应处理结果。
```
process: (XMagic)
```
```
// 在摄像头回调传入帧数据
- (void)captureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer fromConnection:(AVCaptureConnection *)connection;

// 获取原始数据，处理每帧的渲染信息
- (void)mycaptureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)inputSampleBuffer fromConnection:(AVCaptureConnection *)connection originImageProcess:(BOOL)originImageProcess;

// 使用CPU处理数据
- (YTProcessOutput*)processDataWithCpuFuc:(CMSampleBufferRef)inputSampleBuffer;

// 使用GPU处理数据
- (YTProcessOutput*)processDataWithGpuFuc:(CMSampleBufferRef)inputSampleBuffer;

// 美颜SDK处理数据接口
/// @param input 输入处理数据信息
/// @return 输出处理后的数据信息
- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```
4. 释放美颜 SDK。
```
deinit (XMagic)
// 在需要释放SDK资源的地方调用
[self.beautyKit deinit]
```



> ? 完成上述步骤后，用户即可根据自己的实际需求控制展示时机以及其他设备相关环境。



## 常见问题
###  编译报错：“unexpected service error: build aborted due to an internal error: unable to write manifest to-xxxx-manifest.xcbuild': mkdir(/data, S_IRWXU | S_IRWXG | S_IRWXO): Read-only file system (30):”？
1. 前往 **File** > **Project settings** > **Build System** 选择 **Legacy Build System**。
2. Xcode 13.0++  需要在 **File** > **Workspace Settings**  勾选 **Do not show a diagnostic issue about build system deprecation**。

### iOS 导入资源运行后报错：“Xcode 12.X 版本编译提示 Building for iOS Simulator, but the linked and embedded framework '.framework'...”？
将 **Buil Settings** > **Build Options** > **Validate Workspace** 改为 Yes，再单击**运行**。
>?  Validate Workspace 改为 Yes 之后编译完成，再改回 No，也可以正常运行，所这里有这个问题注意下即可。

### 滤镜设置没反应？
检查下设置的值是否正确，范围为 0-100，可能值太小了效果不明显。
	 
	 
	 
	 
	 
	 
	 
	 