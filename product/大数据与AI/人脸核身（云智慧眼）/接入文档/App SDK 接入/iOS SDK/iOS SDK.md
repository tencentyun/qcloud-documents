腾讯云人脸核身针对 iOS 端提供 SDK，开发人员可以将相应的 SDK 添加到工程中，直接调用 SDK 中提供的 OCR 识别、活体检测和1:1人脸比对服务。
![](https://main.qcloudimg.com/raw/ba6e243fdce04a0a9aea85f26516a3e6.png)

## 业务流程
![](https://main.qcloudimg.com/raw/61e2fdb830756b993210e13ffabebc50.png)
1. 客户后端调用 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口进行核身流程开启前鉴权，获取业务流水号（BizToken）。
2. 根据客户自身需求，在对应页面调用相关函数进入人脸核身流程，开始验证。
3. 人脸核身完成后，会触发回调函数，此时客户后端即可凭借回调中提供的 BizToken 调用 [GetDetectInfo](https://cloud.tencent.com/document/api/1007/31331) 接口获取本次核身的详细信息。

## SDK 说明
本 SDK 封装了实名核身的整体流程，包括身份证 OCR 识别和活体检测功能。
### 环境依赖
本 SDK 适用于 iOS8.0以上版本。
### SDK 下载
本 SDK 暂不支持通过外部 npm 源下载，需线下对接获取该 SDK，您可以提交 [接入申请](https://cloud.tencent.com/apply/p/shcgszvmppc) 与我们取得联系。
### 文件说明
SDK 包含了以下文件：
**AuthSDK.framework**：封装了实名认证的流程，包括身份证 OCR 识别和活体检测功能。
**opencv2.framework** 和 **ULSMultitrackeriOSSDK.framework**：人脸识别引擎 SDK。
f**ace_shape.ref、ULSGPUAssets.bin、authsdk.bundle、 ULSFaceTrackerAssets.bundle**：均为资源文件
协议文件在 AuthSDK.framework/authsdk.bundle/protocol.txt 中，可以根据需要修改。其他资源文件，如首页 banner 也可根据需求替换 authsdk.bundle 中图片。

## 接入流程
### 1. 添加 framework 
1.1 将 AuthSDK.framework 拷贝到项目根目录 Frameworks 中（目录可自定义）
1.2 在 TARGETS-Build Phases-Link Binary with Libraries，单击“+”，弹出添加列表后，单击“Add Other…”
1.3 在 Framework 文件夹中，添加 AuthSDK.framework 到工程中。同理，添加 SDK 中的所有文件添加到工程中。
![](https://main.qcloudimg.com/raw/4b84912737da80a6c6cf10e100280704.png)
![](https://main.qcloudimg.com/raw/c35ba913d3c4ba1d4d2fdfd808a4c32a/20190604043849.png)
保证下图中的内部 framework 都添加到工程中。
![](https://main.qcloudimg.com/raw/24a1005a94b091559cf364d9176691a6.png)

### 2.  添加需要的编译选项
在 TARGETS-Build Settings-Other Linker Flags 中添加 -ObjC。
- C++ Language Dialect 设置为 C++11 [-std=c++11]
- C++ Standard Library 设置为 libc++
- bitCode 设置为 NO

![](https://main.qcloudimg.com/raw/0634a472dbee443542d89b9364f75515.png)

### 3. 添加权限声明
在工程 info.plist 中，增加如下字符串：
``` xml
<key>NSPhotoLibraryUsageDescription</key>
<string>需要您的同意才能读取照片库</string>
<key>NSCameraUsageDescription</key>
<string>需要您的同意才能使用摄像头</string>
<key>NSMicrophoneUsageDescription</key>
<string>需要您的同意才能使用麦克风</string>
```
Xcode9以上版本需要添加如下字符串：
``` xml
<key>NSPhotoLibraryAddUsageDescription</key>
<string>需要您的同意才能读取照片库</string>
```
如果您使用 HTTP 访问服务器，需要做如下配置（否则不需要）：
``` xml
<key>NSAppTransportSecurity</key>
<dict>
<key>NSAllowsArbitraryLoads</key>
<true/>
</dict>
```
### 4. 初始化 SDK 接口
在程序中导入 SDK，并初始化。
``` objc
#import <AuthSDK/AuthSDK.h>
```
调用 startAuthWithToken 函数， 传入 BizToken 即可开始人脸核身，每次调用都需要从 [DetectAuth](https://cloud.tencent.com/document/api/1007/31816) 接口生成新的 BizToken。
``` objc
@interface ViewController ()<AuthSDKDelegate>
@property (nonatomic) AuthSDK * sdk;
@end
_sdk = [[AuthSDK alloc] init];
[_sdk startAuthWithToken:@"--传入Biztoken--" parent:self delegate:self];
```

