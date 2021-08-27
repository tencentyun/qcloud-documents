目前，仅原移动直播企业版 SDK，短视频企业版 SDK 以及短视频企业版 Pro SDK 支持高级美颜特效，需要购买原 [移动直播企业版 License](https://cloud.tencent.com/document/product/454/8008)、[短视频企业版 License 或短视频企业版 Pro License](https://cloud.tencent.com/document/product/584/9368) 后，使用对应的功能。


## 功能说明

腾讯云直播团队与优图实验室、天天 P 图团队进行深度合作，结合 **AI 技术与美妆技术**，开发了**大眼**、**瘦脸**、**瘦鼻**、**动效贴纸**、**AI 抠背**以及**绿幕**等特效功能，并整合到 LiteAVSDK 的图像处理流程中，以实现更好的视频效果。
![](https://main.qcloudimg.com/raw/55b969c713b9d96f496bcab3d72e3850.png)


## 接入准备

### 1. 申请企业版 License

登录腾讯云，进入 [美颜特效服务开通申请页](https://cloud.tencent.com/product/x-magic)，如实填写相关信息并完成申请。
请着重检查 **iOS bundle ID** 和 **Android 应用包名称（package name）**信息是否填写正确，License 需要校验您的 App 安装包名称是否跟申请时一致。

![](https://main.qcloudimg.com/raw/b817277d40d37fcb6bdd86e851ad5caa.png)

### 2. 下载企业版 SDK

下载并解压 [企业版 SDK](https://github.com/tencentyun/TRTCSDK/blob/master/SDK%E4%B8%8B%E8%BD%BD.md#%E4%BC%81%E4%B8%9A%E7%89%88-sdk-%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80) ，解压时需要解压密码，解压密码在申请 License 成功后即可获取，解压后的目录结构如下：

| 目录名称                         | 目录内容                      |
| -------------------------------- | ----------------------------- |
| TXLiteAVSDK_Enterprise.framework | 企业版 SDK                    |
| Resource                         | 企业版本 SDK 所需要的特效资源 |

### 3. 将 SDK 导入您的工程

1. 打开您的 Xcode 工程项目，选择要运行的 target，选中【Build Phases】。
    ![](https://main.qcloudimg.com/raw/ea12370194d3c1d1fc7b7e8275b6f1dd.jpg)
2. 单击【Link Binary with Libraries】展开，单击【+】添加依赖库。
    ![](https://main.qcloudimg.com/raw/dc76027fe15ec1bb74fd3329164bd7b3.jpg)
3. 依次添加所下载的`TXLiteAVSDK_Enterprise.framework`及其所需依赖库：
```
libz.tbd 
libc++.tbd
libresolv.tbd
libsqlite3.tbd
Accelerate.framework
AssetsLibrary.framwork
CoreMedia.framework
Metal.framework
```

4. 添加链接参数：
    在工程【Build Setting】>【Other Link Flags】中，增加【-ObjC】选项。
    ![](https://main.qcloudimg.com/raw/41cb5945d9298763319e8ebba597f345.jpg)
5. 添加动效资源：
>!请正确添加下述资源，否则切换到换脸类素材时会发生 Crash 等问题。

  将 SDK/Resource 下的文件以`groups`的形式添加到工程中。
 ![](https://main.qcloudimg.com/raw/222ead2a8eef518ab7d0893a233715cb.png)
  添加完成后，效果如图所示：
  ![](https://main.qcloudimg.com/raw/36848f4b6b7cb1a34368c9bc38b11ffe.jpg)

6. 授权摄像头和麦克风使用权限：
    在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
  - **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
  - **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。
  
 ![](https://main.qcloudimg.com/raw/107480eac7337164e99fe803c414b754.jpg)

### 4. 给 SDK 配置 License 授权

申请企业版 License 成功后，您会获得两个字符串：licenseURL 和解密 key。在您的 App 调用企业版 SDK 相关功能前需进行如下设置：
>?建议配置在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中。

```objc
@import TXLiteAVSDK_Enterprise;
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的 licenseURL>";
    NSString * const licenceKey = @"<获取到的 licenceKey>";
    [TXLiveBase setLicenceURL:licenceURL key:licenceKey];
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

## 功能调用

### 高级美颜接口（大眼、瘦脸等）
美妆接口的设置对象可以通过 TXLivePusher 的 [getBeautyManager](https://cloud.tencent.com/document/product/454/34772#getbeautymanager) 方法获取。
美妆接口的调用比较简单，只需要对指定的接口调用0 - 9之间的一个数值即可，0表示关闭，数值越大，效果越明显。
<dx-codeblock>
::: bjective-c bjective-c
/**
 * 设置美颜（磨皮）算法
 *
 * SDK 内部集成了两套风格不同的磨皮算法，一套我们取名叫“光滑”，适用于美女秀场，效果比较明显。
 * 另一套我们取名“自然”，磨皮算法更多地保留了面部细节，主观感受上会更加自然。
 *
 * @param beautyStyle 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。
 */
- (void)setBeautyStyle:(TXBeautyStyle)beautyStyle;

/**
 * 设置美颜级别
 * @param level 美颜级别，取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setBeautyLevel:(float)level;

/**
 * 设置美白级别
 *
 * @param level 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setWhitenessLevel:(float)level;

/**
 * 设置红润级别
 *
 * @param level 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setRuddyLevel:(float)level;

/**
 * 设置大眼级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setEyeScaleLevel:(float)level;

/**
 * 设置瘦脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 瘦脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceSlimLevel:(float)level;

/**
 * 设置V脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level V脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceVLevel:(float)level;

/**
 * 设置下巴拉伸或收缩（企业版有效，其它版本设置此参数无效）
 *
 * @param level 下巴拉伸或收缩级别，取值范围-9 - 9；0 表示关闭，小于0表示收缩，大于0表示拉伸。
 */
- (void)setChinLevel:(float)level;
/**
 * 设置短脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceShortLevel:(float)level;

/**
 * 设置瘦鼻级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setNoseSlimLevel:(float)level;

/**
 * 设置亮眼 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 亮眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setEyeLightenLevel:(float)level;

/**
 * 设置白牙 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 白牙级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setToothWhitenLevel:(float)level;

/**
 * 设置祛皱 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 祛皱级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setWrinkleRemoveLevel:(float)level;

/**
 * 设置祛眼袋 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 祛眼袋级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setPounchRemoveLevel:(float)level;

/**
 * 设置法令纹 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 法令纹级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setSmileLinesRemoveLevel:(float)level;

/**
 * 设置发际线 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 发际线级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。
 */
- (void)setForeheadLevel:(float)level;

/**
 * 设置眼距 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 眼距级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setEyeDistanceLevel:(float)level;

/**
 * 设置眼角 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 眼角级别，取值范围-9 - 9；0表示关闭，小于0表示降低，大于0表示抬高。
 */
- (void)setEyeAngleLevel:(float)level;

/**
 * 设置嘴型 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 嘴型级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setMouthShapeLevel:(float)level;

/**
 * 设置鼻翼 （企业版有效，其它版本设置此参数无效）
 *
 * @param level 鼻翼级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setNoseWingLevel:(float)level;

/**
 * 设置鼻子位置 （企业版有效，其它版本设置此参数无效）
 * @param level 鼻子位置级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。
 */
- (void)setNosePositionLevel:(float)level;

/**
 * 设置嘴唇厚度 （企业版有效，其它版本设置此参数无效）
 * @param level 嘴唇厚度级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setLipsThicknessLevel:(float)level;

/**
 * 设置脸型（企业版有效，其它版本设置此参数无效）
 * @param   level 美型级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceBeautyLevel:(float)level;
:::
</dx-codeblock>

[](id:beauty_dynamic)
### 美颜动效（动效贴纸、AI抠图、美妆、手势）
美颜动效接口的设置对象可以通过 TXLivePusher 的 [getBeautyManager](https://cloud.tencent.com/document/product/454/34772#getbeautymanager) 方法获取。
购买美颜动效素材后，您可以获得对应效果的素材包。每一个素材包就是一个独立的目录，目录里包含了很多资源文件。每个素材包因其复杂度不同，文件数量和大小尺寸也各不相同。

为了节省安装包体积，我们建议您将素材包上传到您的服务器上，并将下载地址配置在您的 App 中，例如：`http://yourcompany.com/hudongzhibo/AISpecial/**/{动效名}.zip`。
在 App 启动后，下载并解压素材包到 Resource 目录下。完成解压后，即可通过以下接口开启动效效果：


```objective-c
/**
 * 选择使用哪一款 AI 动效挂件（企业版有效，其它版本设置此参数无效）
 *
 * @param tmplName 动效名称
 * @param tmplDir 动效所在目录
 */
- (void)setMotionTmpl:(nullable NSString *)tmplName inDir:(nullable NSString *)tmplDir;
```

### 绿幕功能
绿幕接口的设置对象可以通过 TXLivePusher 的 [getBeautyManager](https://cloud.tencent.com/document/product/454/34772#getbeautymanager) 方法获取。
如果要使用绿幕功能，需要先让主播站在一个绿色背景前。开启绿幕功能以后，SDK 会识别出图像中的绿色区域，并将其替换成视频内容。
![](https://main.qcloudimg.com/raw/8a5038bcd30151d6a7224a8450d1525a.png)
您需要先准备一个用于播放的 mp4 文件，然后通过调用如下接口即可开启绿幕效果：

```objective-c
/**
 * 设置绿幕背景视频（企业版有效，其它版本设置此参数无效）
 *
 * 此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效
 * @param file 视频文件路径，支持 MP4。nil 表示关闭特效。
 */
- (void)setGreenScreenFile:(NSURL *)file;
```

## 问题排查

### 工程编译不过？  
检查`AssetsLibrary.framwork`、`CoreMedia.framework`、`Accelerate.framework`和`Metal.framework`依赖库是否已添加成功。
                 

### 工程运行过程中 Crash？  
- 检查工程是否已配置 -ObjC。
- 检查 Metal API Validation 是否被设置为 Disabled。

如果您出现如下提示，请检查以上配置：
```
[UIDevice wmcUniqueGlobalDeviceIdentifier]: unrecognized selector sent to instance
```
### 工程特效不生效？  
- 检查是否已调用 `+[TXLiveBase setLicenceURL:key:]` 方法，以及参数是否正确。
- 调用 TXLiveBase 的 getLicenseInfo() 方法，带有动效的 Licence 会包含`pituLicense`字段。
- 检查 pitu 资源是否添加正确，尤其要注意 `handdetect`，`handtrack`，`res18_3M`三个文件夹要以 folder refrence 形式添加，最简单的方法就是比对您工程中添加的动效文件是否和 demo 添加的完全一致  。
- SDK 会把 Licence 下载到沙盒的 Documents 目录当中, 可以在开发过程中使用 Xcode 菜单中 “Window > Devices and Simulators” 工具导出并使用 [License 校验工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 查看有效期。

> ! [License 校验工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 是一个 xcode 工程，目前仅支持在 Mac 上使用， 后续会开放其他查询方式。
