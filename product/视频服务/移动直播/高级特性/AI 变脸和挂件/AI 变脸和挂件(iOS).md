# 特效功能（大眼、瘦脸、动效、绿幕）

## 功能说明

腾讯云直播团队与优图实验室、天天P图团队进行深度合作，结合**人脸识别技术与美妆技术**，开发了**大眼、瘦脸、瘦鼻、动效贴纸、 AI 扣背、绿幕**等特效功能，并整合到 LiteAVSDK 的图像处理流程中，以实现更好的视频效果。

![](https://main.qcloudimg.com/raw/6fa6d2c76e389ddaaf2540f547061b90.jpg)

## 接入准备

### 1. 申请企业版 license

打开 [优图美视](https://cloud.tencent.com/product/x-magic) 页面，点击“立即申请”按钮，进入“优图美视”服务开通申请流程，请注意填写 iOS bundle ID （iOS 的安装包名称）和 package name（Android 的安装包名称）这两个字段，因为license 会校验您的 App 安装包名称是否跟申请时保持一致。

![](https://main.qcloudimg.com/raw/66660d7082f1615b71b37f6fcea57642.png)

### 2. 下载企业版 SDK

下载 [企业版 SDK](https://github.com/tencentyun/TRTCSDK/blob/master/SDK%E4%B8%8B%E8%BD%BD.md#%E4%BC%81%E4%B8%9A%E7%89%88-sdk-%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80) 并进行解压，解压时需要解压密码，解压密码在申请 license 成功后即可获取，解压后的目录结构如下：

| 目录名称                         | 目录内容                      |
| -------------------------------- | ----------------------------- |
| TXLiteAVSDK_Enterprise.framework | 企业版 SDK                    |
| GPUImage.framework               | 开源库                        |
| Resource                         | 企业版本 SDK 所需要的特效资源 |

### 3. 将 SDK 导入您的工程

- **3.1 打开您的 Xcode 工程项目，选择要运行的 target , 选中 Build Phases 项。**
  ![](https://main.qcloudimg.com/raw/ea12370194d3c1d1fc7b7e8275b6f1dd.jpg)
- **3.2 单击 Link Binary with Libraries 项展开，单击底下的 + 号图标去添加依赖库。**
  ![](https://main.qcloudimg.com/raw/dc76027fe15ec1bb74fd3329164bd7b3.jpg)
- **3.3 依次添加所下载的 `TXLiteAVSDK_Enterprise.framework`及其所需依赖库：**

```
libz.tbd 
libc++.tbd
libresolv.tbd
libsqlite3.tbd
Accelerate.framework
GPUImage.framework
AssetsLibrary.framwork
CoreMedia.framework
Metal.framework
```

![](https://main.qcloudimg.com/raw/cffafa84fe82b4dadb94aa22de1724a0.jpg)

- **3.4  添加链接参数：**
  在工程 Build Setting -> Other Link Flags 里，增加 -ObjC 选项。
  ![](https://main.qcloudimg.com/raw/41cb5945d9298763319e8ebba597f345.jpg)
- **3.5 添加动效资源：**
  将SDK/Resource下的文件以`groups`的形式添加到工程中：
  ![](https://main.qcloudimg.com/raw/cd4e159c5f90988e91406eebcb388475.jpg)
  这里需要注意的是`handdetect`，`handtrack`，`res18_3M`三个文件要以`folder refrence`形式添加：
  ![](https://main.qcloudimg.com/raw/f2e346478eb0b8c6077f42bc4805fb38.jpg)
  最终如下：
  ![](https://main.qcloudimg.com/raw/689140af9fb384923b81c2e08c1ced50.jpg)
  这些资源非常重要，否则切换到换脸类素材时会发生crash等问题。
- **3.6 授权摄像头和麦克风使用权限：**
  使用 SDK 的音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
  **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
  **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。
  ![](https://main.qcloudimg.com/raw/107480eac7337164e99fe803c414b754.jpg)

### 4. 给 SDK 配置 license 授权

申请企业版 license 成功后，您会获得两个字符串：其中一个字符串是 licenseURL，另一个字符串是解密 key。在您的 App 调用企业版 SDK 相关功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置：

```objc
@import TXLiteAVSDK_Enterprise;
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";
    [TXLiveBase setLicenceURL:licenceURL key:licenceKey];
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

## 功能接口

### 1. 美妆接口（大眼、瘦脸）

美妆接口的调用比较简单，只需要对指定的接口调用 0 - 9 之间的一个数值即可，0 表示关闭，数值越大，效果越明显。

```objective-c
/**
 * 设置大眼级别
 * @param eyeScaleLevel 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setEyeScaleLevel:(float)eyeScaleLevel;

// 瘦脸
- (void)setFaceScaleLevel:(float)faceScaleLevel;

// V 脸
- (void)setFaceVLevel:(float)faceVLevel;

// 调整下巴拉伸或收缩
- (void)setChinLevel:(float)chinLevel;

// 短脸
- (void)setFaceShortLevel:(float)faceShortlevel;

// 瘦鼻
- (void)setNoseSlimLevel:(float)noseSlimLevel;
```

### 2. AI 贴纸

购买商业版 license 后，您可以获得 20 个 AI 贴纸素材包。其中每一个素材包就是一个独立的目录，目录里包含了很多资源文件。每个素材包因其复杂度不同，文件数量和大小尺寸也各不相同。

为了节省安装包体积，我们建议您将素材包上传到您的服务器上，并将下载地址配置在您的 App 中，比如：

> `http://yourcompany.com/hudongzhibo/AISpecial/**/{动效名}.zip`

在 App 启动后，下载并解压素材包到 Resource 目录下，当解压完成后，即可通过以下接口开启动效效果：

```objective-c
/**
 * 选择使用哪一款 AI 动效挂件（商用企业版有效，其它版本设置此参数无效）
 *
 * @param tmplName 动效名称
 * @param tmplDir 动效所在目录
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```

### 3. 绿幕功能

如果要使用绿幕功能，需要先让主播站在一个绿色背景前。开启绿幕功能以后，SDK 会识别出图像中的绿色区域，并将其替换成视频内容。

![](https://main.qcloudimg.com/raw/f1b345135deb4c01ed2a691958ce34f2.jpg)

所以，您还需要先准备一个用于播放的 mp4 文件，之后通过调用如下接口即可开启绿幕效果：

```objective-c
/**
 * 设置绿幕背景视频（商用企业版有效，其它版本设置此参数无效）
 *
 * 此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效
 * @param file 视频文件路径。支持 MP4; nil 表示关闭特效。
 */
- (void)setGreenScreenFile:(NSURL *)file;
```

## 问题排查

### 1. 工程编译不过？  

检查`AssetsLibrary.framwork`、`CoreMedia.framework`、`Accelerate.framework`、`Metal.framework` 依赖库是否已经添加。
                 

### 2. 工程运行过程中crash？  

- 检查工程是否配置了 -ObjC
- 检查 Metal API Validation 是否设置成了Disabled

### 3. 工程特效不生效？  

- 检查是否调用了`+[TXLiveBase setLicenceURL:key:]`方法, 以及参数是否正确。
- 调用 TXLiveBase 的 getLicenseInfo() 方法，带有动效的 licence 会包含 `pituLicense` 字段。
- 检查 pitu 资源是否添加正确，尤其要注意 `handdetect`，`handtrack`，`res18_3M`三个文件夹要以folder refrence形式添加，最简单的方法就是比对自己工程添加的动效文件是否和我们demo添加的完全一致  。
- SDK 会把 licence 下载到沙盒的 Documents 目录当中, 可以在开发过程中使用 Xcode 菜单中 “Window => Devices and Simulators” 工具导出并使用 [License 校验工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)查看有效期。

> ! [License 校验工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)是一个xcode工程，目前仅支持在mac上使用， 后续会开放其他查询方式。



