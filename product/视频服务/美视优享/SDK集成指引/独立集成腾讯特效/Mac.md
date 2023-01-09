## 集成准备
### 开发者环境要求

- 开发工具 XCode 11 及以上：App Store 或单击 [下载 Demo](https://cloud.tencent.com/document/product/616/65875)。
- 建议运行环境：
  - 设备要求：macOS系统设备。
  - 系统要求：macOS 10.10 及以上。

### 导入SDK

您可以先将 SDK 下载到本地，再将其手动导入到您当前的项目中。

#### 下载SDK并手动导入

1. 下载并解压 SDK 和美颜资源，Libs 文件夹里面是 `sdk`、`resources` 文件夹里面是美颜的 bundle 资源。
2. 打开您的 Xcode 工程项目，把Libs文件夹里面的 Xmagic_Mac.framework、libLightSDKMac 添加到实际工程中，选择要运行的 target , 选中 **General** 项，单击 **Frameworks,Libraries,and Embedded Content** 项展开，将 libLightSDKMac 的 Embed 改成 `Embed&Sign`。![](https://qcloudimg.tencent-cloud.cn/raw/554950d12b796ca6c82f8c8d3fda9f79.png)
3. 选择对应的 target，选中Build Settings,找到Other Linker Flags添加**-lstdc++**。
4. 在项目里找到 `xxx(项目名).entitlements` 文件，增加如下 key-value：
```objc
<key>com.apple.security.cs.allow-dyld-environment-variables</key>
    <true/>
```
5. 把 resources 夹里面的美颜资源添加到实际工程中。
4. 将 Bundle ID 修改成与申请的测试授权一致。

#### 动态下载集成
为了减少包大小，您可以将 SDK 所需的模型资源和动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。
动态下载的详细指引，请参见 [SDK 包体瘦身（iOS）](https://cloud.tencent.com/document/product/616/76029)。

### 配置权限
在 Info.plist 文件中添加相应权限的说明，否则程序在 iOS 10 系统上会出现崩溃。请在 Privacy - Camera Usage Description 中开启相机权限，允许 App 使用相机。Privacy - Microphone Usage Description开启麦克风权限，允许使用麦克风。在target-->signing & Capabilities--> Hardened Runtime 勾选**Audio Input、Camera**。

## 集成步骤
[](id:step1)
### 步骤一：鉴权
1. 申请授权，得到 LicenseURL 和 LicenseKEY，请参见 [License 指引](https://cloud.tencent.com/document/product/616/65879)。
> ! 正常情况下，只要 App 成功联网一次，就能完成鉴权流程，因此您**不需要**把 License 文件放到工程的工程目录里。但是如果您的 App 在从未联网的情况下也需要使用 SDK 相关功能，那么您可以把 License 文件下载下来放到工程目录，作为保底方案，此时 License 文件名必须是 `v_cube.license`。
2. 在相关业务模块的初始化代码中设置 URL 和 KEY，触发 License 下载，避免在使用前才临时去下载。也可以在 AppDelegate 的 didFinishLaunchingWithOptions 方法里触发下载。其中，LicenseURL 和 LicenseKey 是控制台绑定 License 时生成的授权信息。
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

[](id:step2)
### 步骤二：加载 SDK（XMagic.framework）
使用腾讯特效 SDK 生命周期大致如下：
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
// demo层
// 在摄像头回调传入帧数据
- (void)captureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer fromConnection:(AVCaptureConnection *)connection;

// 获取原始数据，处理每帧的渲染信息
- (void)mycaptureOutput:(AVCaptureOutput *)captureOutput didOutputSampleBuffer:(CMSampleBufferRef)inputSampleBuffer fromConnection:(AVCaptureConnection *)connection originImageProcess:(BOOL)originImageProcess;

// 使用CPU处理数据
- (YTProcessOutput*)processDataWithCpuFuc:(CMSampleBufferRef)inputSampleBuffer;

// 使用GPU处理数据
- (YTProcessOutput*)processDataWithGpuFuc:(CMSampleBufferRef)inputSampleBuffer;

// sdk接口调用
// 腾讯特效 SDK处理数据接口
/// @param input 输入处理数据信息
/// @return 输出处理后的数据信息
- (YTProcessOutput* _Nonnull)process:(YTProcessInput * _Nonnull)input;
```
4. 给 SDK 设置特效。
```
/// @brief 配置美颜各种效果
/// @param propertyType 效果类型 字符串：beauty, lut, motion
/// @param propertyName 效果名称
/// @param propertyValue 效果数值
/// @param extraInfo 预留扩展, 附加额外配置dict
/// @return 成功返回0，失败返回其他
/// @note 具体说明
/**
| 效果类型 | 效果名称 | 效果值 | 说明  | 备注 |
| :---- | :---- |:---- | :---- | :---- |
|  beauty  | 美颜id名称 | 美颜效果强度数值 |美颜类型配置接口 | 无 |
|  lut  | 滤镜路径+滤镜名称 | 滤镜强度数值 | 滤镜类型配置接口 | 无 |
|  motion  | 动效路径名称 | 动效路径 | 动效类型配置接口| **注意**：如果资源中有zip，请确保传入动效路径为可写路径，否则跟app包走需要手动unzip才可以使用 |
**/
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```
参数的设置和说明，请参见 [参数设置说明](https://cloud.tencent.com/document/product/616/79252)。
5. 释放腾讯特效 SDK。
```
deinit (XMagic)
// 在需要释放SDK资源的地方调用
[self.beautyKit deinit]
```

