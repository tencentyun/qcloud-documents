>! 接入之前，请详细阅读 SDK 中的 readme 和接入指引。

以下为接入配置的步骤。

## 基础配置[](id:xx)
本文档介绍了接入 NFC OCR SDK 接口，NFC 读取证件需要 iPhone 7 及以上，iOS14.5 及以上。
1. 在苹果开发者管理平台配置 Bundle Id。
请登录苹果开发者管理平台，确认当前 bundle ID 下的 NFC Tag Reading 已经选中。
配置路径 Certificates，Identifiers & Profiles > Identifiers > 选中需要配置接入 SDK 的 App 对应的 ID。
![](https://qcloudimg.tencent-cloud.cn/raw/2e96d9cd98e30631eb60c8683248a210.png)
单击进去之后，勾选 NFC Tag Reading。
![](https://qcloudimg.tencent-cloud.cn/raw/77d96cb8b0b654202a17c3a9933d98c3.png)

2. 在 Xcode 中配置 Info.plist 文件。
**实证 NFC 配置**
在 info.plist 中添加 NFCReaderUsageDescription 和 ISO7816 application identifiers for NFC Tag Reader Session，在 item0 中填写 F049442E43484E。
![](https://qcloudimg.tencent-cloud.cn/raw/d83fb5355bd8fc73268b7ca6a668afe4.png)
**旅行证 NFC 配置**
在 http://info.plist 中添加 NFCReaderUsageDescription 和 ISO7816 application identifiers for NFC Tag Reader Session，在 item0 中填写 A0000002471001（下图配置了两个 item，同时支持身份证和旅行证件识别）。
![](https://qcloudimg.tencent-cloud.cn/raw/a09e9b36fe48cd835844b7da0e69511b.png)
3. 在 Xcode 中配置 Capabilities。
在 IDE 中，依次选择 target > Signing&Capabilities > All ，添加 Near Field Communication Tag Reading。
![](https://qcloudimg.tencent-cloud.cn/raw/6184d7e07c5de148443171c646abeb96.png)

## SDK 集成
SDK 文件目录如下：
```
.
├── NFCOCRDevDemo
├── Readme
└── WBNFCReaderService
```

- WBNFCReaderService 目录下提供了 SDK。
- NFCOCRDevDemo 目录下面提供了 SDK 开发接入的 Demo。
- Readme 是版本信息。

### Cocoapods 集成
下面介绍 Cocoapods 集成 SDK。
参考 NFCOCRDevDemo，在项目的 Podfile 中添加引用语句，并指明 SDK 的相对路径。

```
target 'NFCOCRDevDemo' do
  use_frameworks!
      # Pods for NFCOCRDevDemo
  pod 'WBNFCReaderService'，:path => '../WBNFCReaderService'
end
```
执行 pod install，便可完成 SDK 的集成。

### 手动集成[](id:xxx)
1. 将 WBNFCReaderService.xcframework 添加到项目。
将 WBNFCReaderService.xcframework 添加到项目，并勾选 Embed & Sign。
![](https://qcloudimg.tencent-cloud.cn/raw/d7f06f7c77283913fe2c7aee362cc0dc.png)
2. 配置 Build Settings。
设置 ALWAYS_EMBED_SWIFT_STANDARD_LIBRARIES为 YES. 这个配置很重要，SDK 使用 swift 语言开发，不设置的话，在低版本 iOS 系统上会出现启动 crash。
配置方式如下，Build Settings > ALWAYS_EMBED_SWIFT_STANDARD_LIBRARIES，设置为 YES。
![](https://qcloudimg.tencent-cloud.cn/raw/0ab8d4feaed2150c374ef6c626e515c8.png)
3. CoreNFC.framework 配置。
4. SDK 使用到系统库 CoreNFC.framework, 在 Build Phases > Link Binary 中添加 CoreNFC.framework。
>! status 要选 Optional，否则在不支持 CoreNFC 的低版本手机上会出现 crash。
>
![](https://qcloudimg.tencent-cloud.cn/raw/a8768442d17ae4948322b8bce723023f.png)

## SDK 调用
### 调用前准备
App 接入 SDK 前，需要获取腾讯服务分配的接入参数，通过 App 后台计算签名。
### SDK 主要 API 介绍
1. WBOCRReaderService 类提供 NFC SDK 入口和回调。
WBOCRReaderService 是 SDK 的核心类，通过这个类对外提供 NFC 证件识别能力，它是个单例类，通过 sharedInstance来实例化。
```
+ (WBOCRReaderService * _Nonnull)sharedInstance;
```
SDK 的入口方法如下, 入参通过 WBOCRReaderParam 类传入。
	- **实证 NFC 识别入口**
```
/// SDK 入口方法1 -- 身份证 NFC (带 UI 的入口)
/// - Parameters:
/// - param: 请求 SDK 的业务参数, 字段参考 `WBOCRReaderParam` 类
/// - fromVC: 跳转的 UIViewController 或者 UINavigationController, SKD 基于这个 VC 跳转
/// - loginSucceedBlock: SDK 登录成功回调, 收到这个回调之后, 即将进入 SDK 页面
/// - readSucceedBlock: SDK 识别成功回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
/// - failedBlock: SDK 异常回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
- (void)startReaderServiceWith:(WBOCRReaderParam *_Nonnull)param fromVC:(UIViewController *_Nonnull)fromVC loginSucceedBlock:(void (^ _Nonnull)(void))loginSucceedBlock readSucceedBlock:(void (^ _Nonnull)(WBOCRReaderResult *_Nonnull))readSucceedBlock failedBlock:(void (^ _Nonnull)(WBOCRReadError *_Nonnull))failedBlock SWIFT_AVAILABILITY(ios,introduced=14.5);

/// SDK 入口方法2 -- 身份证 NFC (无 UI 的入口)
/// - Parameters:
/// - param: 请求 SDK 的业务参数, 字段参考 `WBOCRReaderParam` 类
/// - loginSucceedBlock: SDK 登录成功回调, 收到这个回调之后, 即将进入 SDK 页面
/// - readSucceedBlock: SDK 识别成功回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
/// - failedBlock: SDK 异常回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
- (void)startReaderServiceWith:(WBOCRReaderParam *_Nonnull)param loginSucceedBlock:(void (^ _Nonnull)(void))loginSucceedBlock readSucceedBlock:(void (^ _Nonnull)(WBOCRReaderResult *_Nonnull))readSucceedBlock failedBlock:(void (^ _Nonnull)(WBOCRReadError * _Nonnull))failedBlock SWIFT_AVAILABILITY(ios,introduced=14.5);
```
	- **旅行证识别入口**
和身份证识别相比，旅行证识别需要额外传入三个参数：旅行证编号、出生日期和截止日期。
```
/// SDK 入口方法3 -- 旅行证识别入口（带 UI 入口）
/// - Parameters:
/// - param: 请求 SDK 的业务参数, 字段参考 `WBOCRReaderParam` 类
/// - passportNumber: 旅行证件编号
/// - dateOfBirth: 出生日期 6位数字
/// - expiryDate: 截止日期 6位数字
/// - fromVC: 跳转的 UIViewController 或者 UINavigationController, SKD 基于这个 VC 跳转
/// - loginSucceedBlock: SDK 登录成功回调, 收到这个回调之后, 即将进入 SDK 页面
/// - readSucceedBlock: SDK 识别成功回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
/// - failedBlock: SDK 异常回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
- (void)startPassportReaderServiceWith:(WBOCRReaderParam *_Nonnull)param passportNumber:(NSString *_Nonnull)passportNumber dateOfBirth:(NSString *_Nonnull)dateOfBirth expiryDate:(NSString *_Nonnull)expiryDate fromVC:(UIViewController *_Nonnull)fromVC loginSucceedBlock:(void (^ _Nonnull)(void))loginSucceedBlock readSucceedBlock:(void (^ _Nonnull)(WBOCRReaderResult *_Nonnull))readSucceedBlock failedBlock:(void (^ _Nonnull)(WBOCRReadError * _Nonnull))failedBlock;

/// SDK 入口方法4-- 旅行证识别入口
/// - Parameters:
/// - param: 请求 SDK 的业务参数, 字段参考 `WBOCRReaderParam` 类
/// - passportNumber: 旅行证件编号
/// - dateOfBirth: 出生日期 6位数字
/// - expiryDate: 截止日期 6位数字
/// - loginSucceedBlock: SDK 登录成功回调, 收到这个回调之后, 即将进入 SDK 页面
/// - readSucceedBlock: SDK 识别成功回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
/// - failedBlock: SDK 异常回调, 接收到这个回调之后, SDK 即将退出, 回到 APP 页面
- (void)startPassportReaderServiceWith:(WBOCRReaderParam *_Nonnull)param passportNumber:(NSString *_Nonnull)passportNumber dateOfBirth:(NSString *_Nonnull)dateOfBirth expiryDate:(NSString *_Nonnull)expiryDate loginSucceedBlock:(void (^ _Nonnull)(void))loginSucceedBlock readSucceedBlock:(void (^ _Nonnull)(WBOCRReaderResult *_Nonnull))readSucceedBlock failedBlock:(void (^ _Nonnull)(WBOCRReadError *_Nonnull))failedBlock;
```

通过 sdkVersion 属性来查看 SDK 的版本号。
```
@property (nonatomic，readonly，copy) NSString * _Nonnull sdkVersion;
```
2. WBOCRReaderParam 类定义 SDK 入参模板。
WBOCRReaderParam 描述了 SDK 的入参格式。
每个字段的含义以及格式如下：
```
@interface WBOCRReaderParam : NSObject
@property (nonatomic，copy) NSString * _Nonnull appId;   // appId 由腾讯服务分配的
@property (nonatomic，copy) NSString * _Nonnull version; // openAPI 接口版本号，由腾讯服务统一分配，当前传入 1.0.0
@property (nonatomic，copy) NSString * _Nonnull nonce;   // 每次请求需要的一次性nonce，一次有效
@property (nonatomic，copy) NSString * _Nonnull userId;  // 每个用户唯一的标识
@property (nonatomic，copy) NSString * _Nonnull sign;    // 签名信息，有接入方后台提供，一次有效
@property (nonatomic，copy) NSString * _Nonnull orderNo; // 订单号，长度不能超过32位的字符串
@property (nonatomic，copy) NSString * _Nonnull ocrCertId;// NFC流程唯一id，后台生成
@end
```
3. WBOCRReaderResult 类定义 SDK 返回结果模板。
SDK 识别成功之后，会通过 readSucceedBlock 将识别结果回调给 App，WBOCRReaderResult 描述了返回值格式。
```
@interface WBOCRReaderResult : NSObject
@property (nonatomic，readonly，copy) NSString * orderNo;  // 订单号
@property (nonatomic，readonly，copy) NSString * reqId;    // 卡片识别结果
@property (nonatomic，readonly，copy) NSString * ocrCertId;// NFC 流程唯一 id
@end
```
4. WBOCRReadError 类定义 SDK 异常结果模板.
SDK 异常的时候，会通过 failedBlock 将错误信息返回给 App ，并退出 SDK。
```
@interface WBOCRReadError : NSObject
@property (nonatomic) NSInteger code;                            // 错误码
@property (nonatomic，copy) NSString * _Nonnull message;         // 错误信息
@property (nonatomic，copy) NSString * _Nonnull localDescription;// 错误描述
@end
```
错误码对照表参见 **SDK 错误码**章节。

### 接入示例
1. 引入头文件。
```
#import <WBNFCReaderService/WBNFCReaderService-Swift.h>
```

2. 调起 SDK 并接收回调。
```
[[WBOCRReaderService sharedInstance] startReaderServiceWith:param
                                                     fromVC:self
                                          loginSucceedBlock:^{
                                            // 1. SDK 登录成功回调
} readSucceedBlock:^(WBOCRReaderResult * _Nonnull result) {
                                            // 2. SDK 识别成功回调
} failedBlock:^(WBOCRReadError * _Nonnull error) {
                                            // 3. SDK 识别异常回调
}];

```
详细接入代码，请参考 SDK 附的 NFCOCRDevDemo 工程。

### 常见问题 Q&A
1. dyld: Library not loaded
集成 SDK 之后的 App，在低版本手机上运行，App 启动时候，可能会报如下错误，App 表现为 crash。
```
dyld: Library not loaded: @rpath/xxx/WBNFCReaderService
dyld: Library not loaded: @rpath/WBNFCReaderService.framework/WBNFCReaderService
  Referenced from: /var/containers/Bundle/Application/07B7698F-2A05-45C5-B07B-3C9BA532CF7E/Demo.app/Demo
  Reason: image not found
```
出现这个问题，请参考 [手动集成 步骤1](#xxx) 的配置。

2. dyld: Library not loaded: @rpath/libswiftCore.dylib
```
dyld: Library not loaded: @rpath/libswiftCore.dylib
  Referenced from: /private/var/containers/Bundle/Application/D775FC77-5694-4B8B-B6D7-17F0D04DB960/Demo.app/Frameworks/WBNFCReaderService.framework/WBNFCReaderService
  Reason: image not found
```
出现这个问题，请参考 [手动集成 步骤2](#xxx) 的配置。

3. 在支持 NFC 的设备上, 报错 Device doesn't support NFC tag reading。
在 iPhone 7 及以上，iOS14.5 及以上 的设备上运行 SDK，仍然报 Device doesn't support NFC tag reading 错误。日志如下：
```
2022-06-09 16:26:57.222541+0800 Demo[11049:1234104] [CoreNFC] -[NFCHardwareManager areFeaturesSupported:outError:]:166 XPC Error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.nfcd.service.corenfc was invalidated from this process." UserInfo={NSDebugDescription=The connection to service named com.apple.nfcd.service.corenfc was invalidated from this process.}
2022-06-09 16:26:57.328858+0800 Demo[11049:1234104] [CoreNFC] -[NFCHardwareManager areFeaturesSupported:outError:]:166 XPC Error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.nfcd.service.corenfc was invalidated: failed at lookup with error 159 - Sandbox restriction."
```
请参考本文档的 [项目基础配置](#xx)  检查配置项。


