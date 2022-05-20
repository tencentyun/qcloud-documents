## 集成准备

### 开发者环境要求

- 开发工具 XCode 11 及以上：App Store 或单击 [下载 Demo](https://cloud.tencent.com/document/product/616/65875)。
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
<li/>AVFoundation
<li/>Accelerate
<li/>AssetsLibrary
<li/>CoreML
<li/>JavaScriptCore
<li/>CoreFoundation
<li/>MetalPerformanceShaders
<li/>CoreTelephony
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

[](id:step1)
### 步骤一：签名准备
framework 签名可以直接在 General-->Masonry.framework 和 libpag.framework 选 Embed & Sign。
[](id:step2)
### 步骤二：鉴权
1. 申请授权，得到 LicenseURL 和 LicenseKEY，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)。
> ! 正常情况下，只要app成功联网一次，就能完成鉴权流程，因此您**不需要**把 License 文件放到工程的工程目录里。但是如果您的app在从未联网的情况下也需要使用SDK相关功能，那么您可以把license文件下载下来放到工程目录，作为保底方案，此时license文件名必须是v_cube.license。
2. 在相关业务模块的初始化代码中设置 URL 和 KEY，触发 license 下载，避免在使用前才临时去下载。也可以在 AppDelegate 的 didFinishLaunchingWithOptions 方法里触发下载。其中，LicenseURL 和 LicenseKey 是控制台绑定 License 时生成的授权信息。
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
</tr><tr>
<td>-3</td>
<td>下载环节失败，请检查网络设置</td>
</tr><tr>
<td>-4</td>
<td>从本地读取的 TE 授权信息为空，可能是 IO 失败引起</td>
</tr><tr>
<td>-5</td>
<td>读取 VCUBE TEMP License文件内容为空，可能是 IO 失败引起</td>
</tr><tr>
<td>-6</td>
<td>v_cube.license 文件 JSON 字段不对。请联系腾讯云团队处理</td>
</tr><tr>
<td>-7</td>
<td>签名校验失败。请联系腾讯云团队处理</td>
</tr><tr>
<td>-8</td>
<td>解密失败。请联系腾讯云团队处理</td>
</tr><tr>
<td>-9</td>
<td>TELicense 字段里的 JSON 字段不对。请联系腾讯云团队处理</td>
</tr><tr>
<td>-10</td>
<td>从网络解析的TE授权信息为空。请联系腾讯云团队处理</td>
</tr><tr>
<td>-11</td>
<td>把 TE 授权信息写到本地文件时失败，可能是IO失败引起</td>
</tr><tr>
<td>-12</td>
<td>下载失败，解析本地 asset 也失败</td>
</tr><tr>
<td>-13</td>
<td>鉴权失败</td>
</tr><tr>
<td>其他</td>
<td>请联系腾讯云团队处理</td>
</tr>
</tbody></table>

[](id:step3)
### 步骤三：加载 SDK（XMagic.framework）
使用腾讯特效 SDK 生命周期大致如下:
1. 加载美颜相关资源。
```
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",
	@"root_path":[[NSBundle mainBundle] bundlePath]
};
```
2. 初始化腾讯特效 SDK。
```
initWithRenderSize:assetsDict: (XMagic)
self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
```
3. 腾讯特效 SDK 处理每帧数据并返回相应处理结果。
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

// 腾讯特效 SDK处理数据接口
/// @param input 输入处理数据信息
/// @return 输出处理后的数据信息
- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```
4. 释放腾讯特效 SDK。
```
deinit (XMagic)
// 在需要释放SDK资源的地方调用
[self.beautyKit deinit]
```

> ? 完成上述步骤后，用户即可根据自己的实际需求控制展示时机以及其他设备相关环境。

## 常见问题

[](id:que1)
### 问题1：编译报错：“unexpected service error: build aborted due to an internal error: unable to write manifest to-xxxx-manifest.xcbuild': mkdir(/data, S_IRWXU | S_IRWXG | S_IRWXO): Read-only file system (30):”？

1. 前往 **File** > **Project settings** > **Build System** 选择 **Legacy Build System**。
2. Xcode 13.0++  需要在 **File** > **Workspace Settings**  勾选 **Do not show a diagnostic issue about build system deprecation**。

[](id:que2)
### 问题2：iOS 导入资源运行后报错：“Xcode 12.X 版本编译提示 Building for iOS Simulator, but the linked and embedded framework '.framework'...”？

将 **Buil Settings** > **Build Options** > **Validate Workspace** 改为 Yes，再单击**运行**。
> ?  Validate Workspace 改为 Yes 之后编译完成，再改回 No，也可以正常运行，所这里有这个问题注意下即可。

[](id:que3)
### 问题3：滤镜设置没反应？
检查下设置的值是否正确，范围为 0-100，可能值太小了效果不明显。

[](id:que4)
### 问题4：iOS Demo 编译，生成 dSYM 时报错？
```
PhaseScriptExecution CMake\ PostBuild\ Rules build/XMagicDemo.build/Debug-iphoneos/XMagicDemo.build/Script-81731F743E244CF2B089C1BF.sh
    cd /Users/zhenli/Downloads/xmagic_s106
    /bin/sh -c /Users/zhenli/Downloads/xmagic_s106/build/XMagicDemo.build/Debug-iphoneos/XMagicDemo.build/Script-81731F743E244CF2B089C1BF.sh

Command /bin/sh failed with exit code 1
```
- 问题原因： `libpag.framework和Masonary.framework` 重签名失败。
- 解决方法：
	1. 打开 `demo/copy_framework.sh`。
	2. 用下述命令查看本机 cmake 的路径，将 `$(which cmake)` 改为本地 cmake 绝对路径。
```
which cmake
```
	3. 用自己的签名替换所有 `Apple Development: ......` 。
