>! 接入之前，请详细阅读 SDK 中的 readme 和接入指引。

以下为接入配置的步骤。

## 基础配置
本文档介绍了接入 NFC OCR SDK 接口，NFC 读取居民身份证需要 iPhone 7 及以上，iOS14.5 及以上。
1. 在苹果开发者管理平台配置 Bundle Id。
请登录苹果开发者管理平台，确认当前 bundle ID 下的 NFC Tag Reading 已经选中。
配置路径 Certificates，Identifiers & Profiles > Identifiers > 选中需要配置接入 SDK 的 App 对应的 ID。
![](https://qcloudimg.tencent-cloud.cn/raw/2e96d9cd98e30631eb60c8683248a210.png)
单击进去之后，勾选 NFC Tag Reading。
![](https://qcloudimg.tencent-cloud.cn/raw/77d96cb8b0b654202a17c3a9933d98c3.png)

2. 在 Xcode 中配置 Info.plist 文件。
在 info.plist 中添加 NFCReaderUsageDescription 和 ISO7816 application identifiers for NFC Tag Reader Session，在 item0 中填写 F049442E43484E。
![](https://qcloudimg.tencent-cloud.cn/raw/ee94ff153ec04366850e6107dd26340a.png)
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

手动集成直接将 WBNFCReaderService/Libs 目录下的 WBNFCReaderService.xcframework 添加到项目中。
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

## SDK 调用
### 调用前准备
App 接入 SDK 前，需要获取腾讯服务分配的接入参数，通过 App 后台计算签名。
### SDK 主要 API 介绍
1. WBOCRReaderService 类提供 NFC SDK 入口和回调。
WBOCRReaderService 是 SDK 的核心类，通过这个类对外提供 NFC 身份证识别能力，它是个单例类，通过 sharedInstance来实例化。
```
+ (WBOCRReaderService * _Nonnull)sharedInstance;
```
SDK 的入口方法如下，入参通过 WBOCRReaderParam 类传入。
```
/// SDK 入口方法
/// - Parameters:
///   - param: 请求 SDK 的业务参数，字段参考 `WBOCRReaderParam` 类
///   - fromVC: 跳转的 UIViewController 或者 UINavigationController，SKD 基于这个 VC 跳转
///   - loginSucceedBlock: SDK 登录成功回调，收到这个回调之后，  即将进入 SDK 页面
///   - readSucceedBlock:  SDK 识别成功回调，接收到这个回调之后，SDK 即将退出，回到 App 页面
///   - failedBlock:       SDK 异常回调，接收到这个回调之后，SDK 即将退出，回到 App 页面

- (void)startReaderServiceWith:(WBOCRReaderParam *)param
                        fromVC:(UIViewController *)fromVC
             loginSucceedBlock:(void (^ _Nonnull)(void))loginSucceedBlock
              readSucceedBlock:(void (^ _Nonnull)(WBOCRReaderResult * _Nonnull))readSucceedBlock
                   failedBlock:(void (^ _Nonnull)(WBOCRReadError * _Nonnull))failedBlock SWIFT_AVAILABILITY(ios，introduced=14.5);
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
