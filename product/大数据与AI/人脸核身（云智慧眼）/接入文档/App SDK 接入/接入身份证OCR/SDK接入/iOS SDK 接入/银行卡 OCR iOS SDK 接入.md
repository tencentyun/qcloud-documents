## 配置流程
>! 接入之前，请详细阅读 SDK 中的 readme 和接入指引。

以下为接入配置的步骤：
### 1. SDK 集成
SDK 支持 cocoapods 和手动两种方式集成。

#### 1.1 SDK pod 集成
如果您的项目已经支持 cocoapods ，可以使用本方式集成 SDK，本示例使用的 cocoapods 为 1.7.2。
下载的 OCR SDK 文件夹目录结构如下：
```
├── OCR_private_pod
│ ├── LICENSE
│ ├── Libs
│ └── WBOCRService.podspec
├── README
├── WBOCRDemo
│ ├── Podfile
│ ├── Podfile.lock
│ ├── Pods
│ ├── WBOCRDemo
│ ├── WBOCRDemo.xcodeproj
│ └── WBOCRDemo.xcworkspace
└── 接入指引.md

```
OCR_private_pod 文件夹下面是 OCR SDK 的 pod 仓库，这个仓库名称为 WBOCRService ，WBOCRDemo 文件夹下是示例 demo，通过 pod 方式集成，需要完成以下 3 个步骤：
1. 将 OCRprivatepod 文件夹移动到指定的位置（这个位置可以依据您项目文件的布局而定）。
2. 在 podfile 中引用 pod。
3. 执行 pod install 完成安装。

#### 1.2 SDK 手动集成
- 下载 OCR SDK，找到 OCRprivatepod/Lib 文件夹，SDK 文件在这个文件夹下。
- 拖拽 SDK 文件到 Xcode 工程内 (请勾选Copy items if needed选项) ，其中包括WBOCRService.bundle、WBOCRService.framework、YTCommon.framework、YTImageRefiner.framework 以及 tiny_opencv2.framework。
```
├── WBOCRService.bundle
├── WBOCRService.framework
├── YTCommon.framework
├── YTImageRefiner.framework
└── tiny_opencv2.framework
```

- 在Build Phases -> link with libraries 下加入如下依赖。
```
CoreTelephony.framework
CoreServices.framework
CoreMedia.framework
AssetsLibrary.framework
AVFoundation.framework
SystemConfiguration.framework
WebKit.framework
libc++.tbd
```

- Build Setting --> Linking --> Other Linker Flag 设置 增加 -ObjC 和 -lz linker flag

### 2. 集成过程中注意事项
**cocoapods 集成时 `:path` 参数说明**
使用 `:path` 参数，在指定路径下加载 pods ，这个路径是本质上是 WBOCRService.podspec 相对 podfile 的路径。在示例 WBOCRDemo 中，如下：
```
target 'WBOCRDemo' do
pod 'WBOCRService',:path => '../OCR_private_pod'
end
```
## 接口调用
SDK 中需要使用 camera，需要在 Info.plist 中为 NSCameraUsageDescription 添加描述信息。
### 1. 概述
OCR SDK 对外提供以下两类证件的识别能力：
- 身份证识别
- 银行卡识别

SDK 提供以下接入方式：标准模式接入。传统的接入方式，SDK 完成整个识别流程，给用户返回识别结果。
在 SDK 附的 demo 中，有提供以上接入方式的接入示例，详细接入请参考 demo 工程中的示例代码。

### 2. SDK 头文件说明
SDK 一共对外暴露了 4 个头文件，如下所示：
```
├── Headers
│   ├── WBBankCardInfoModel.h
│   ├── WBIDCardInfoModel.h
│   ├── WBOCRConfig.h
│   ├── WBOCRService.h
```

这些头文件可以大致分为三类：
- 模型类（WBBankCardInfoModel 和 WBIDCardInfoModel ），这些模型类分别对应银行卡和身份证的识别结果字段。
- 配置类（WBOCRConfig），这个类提供了 SDK 的配置选项。
- 入口类（WBOCRService），这个类提供 SDK 的入口和回调。

#### 2.1 模型类说明
模型类对外暴露识别结果，以身份证识别为例，WBIDCardInfoModel 类的实例返回身份证识别结果，结果中包含如下字段：
```
• idcard 公民身份号码
• name 姓名
• sex 性别
• nation 民族
• address 住址
• birth 出生
• authority 签发机关
• validDate 有效期限
• frontFullImg 国徽面截图
• backFullImg 人像面截图
• orderNo 每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
• sign 签名信息
• warning 识别结果警告信息
• multiWarning 多重告警码，人像面是 frontMultiWarning，国徽面对应 backMultiWarning
• clarity  图片清晰度，人像面是 frontClarity，国徽面对应 backClarity
```
开发者按需获取需要的信息。
其余证件识别与之类似，详情参考类头文件的字段注释。

#### 2.2 配置类说明
WBOCRConfig 对外提供配置接口，下面的内容逐一介绍其核心接口。
WBOCRConfig 是一个单例，开发者必须通过制定的初始化方法 sharedConfig 初始化。支持的主要配置项如下：
```
/// default NO, 设置成 YES 之后, 识别结果没有告警才判定为识别成功.
@property (nonatomic, assign) BOOL checkWarnings;
/**
 * @brief 设置识别超时时间，默认是20.0s
 */
@property (nonatomic) NSTimeInterval timeoutInterval;
/**
 * @brief 是否需要录制视频。此功能目前仅适用于身份证识别，默认为NO，即不录制；设置为 YES，识别成功之后，会返回长度不超过 3s 的视频地址
 */
@property (nonatomic) BOOL needRecordVideo ;
/**
 * @brief 控制身份证识别是否返回切边图, BOOL类型，默认值为 NO
 * 当这个值设置为 YES 的时候,进行身份证人像面识别时, 切边图会在 frontCrop 字段返回; 进行身份证国徽面识别时,切边图会在 backCrop 字段返回
 * 当这个值设置为 NO  的时候,进行身份证识别的时候, frontCrop 和 backCrop 返回 nil
 */
@property (nonatomic) BOOL retCrop;
```

#### 2.3 标准模式入口类说明
WBOCRService 是 SDK 的入口类，需要通过制定的初始化方法 sharedService 进行初始化。
```
/**
 * @brief WBOCRService 单例方法，通过调用该方法实例化 WBOCRService对象
 *
 * @return WBOCRService对象
 */
 + (nonnull instancetype) sharedService;

SDK支持身份证证件识别，提供 3 种识别模式，通过 WBOCRCardType 来定义。
/// * @brief  OCR SDK 提供证件的识别能力：身份证识别
///
/// WBOCRCardType 定义 SDK 不同的识别模式，下面描述这些模式：
/// 1. 身份证识别（识别身份证人像面和国徽面）
///     - WBOCRSDKTypeIDCardFrontSide: 身份证人像面识别模式，在 SDK 中完成人像面识别，识别完成之后，将本次识别结果返回第三方APP
///     - WBOCRSDKTypeIDCardBackSide: 身份证国徽面识别模式，在 SDK 中完成国徽面识别，识别完成之后，将本次识别结果返回第三方APP
///     - WBOCRSDKTypeIDCardContinuous:  身份证识别连拍模式，在 SDK 中完成人像面 + 国徽面识别，识别完成之后，将本次识别结果返回第三方APP

typedef NS_ENUM(NSInteger, WBOCRCardType) {
    WBOCRSDKTypeIDCardFrontSide = 1,
    WBOCRSDKTypeIDCardBackSide = 2,
    WBOCRSDKTypeIDCardContinuous = 7,
    WBOCRSDKTypeIDCardNormal NS_ENUM_DEPRECATED_IOS(9_0, 12_0,"User WBOCRSDKTypeIDCardContinuous") = 0,
};
```
SDK 接入分为两个步骤：
- init SDK，调用 init 接口完成 SDK 登录。
- startService，init 成功之后，调用这个接口开始识别。

>! init 和 startService 接口一一对应。

init SDK 接口如下：
```
/// 标准版本 SDK 登录接口, 这个接口完成 SDK 登录
/// @param sdkType     本次识别的卡证类型,详细参考 `WBOCRCardType`
/// @param appId       人脸核身控制台内申请的 WBappid
/// @param nonce       每次请求需要的一次性nonce，一次有效
/// @param userId      每个用户唯一的标识
/// @param sign        签名信息，由接入方后台提供，一次有效
/// @param orderNo     每次OCR识别请求的唯一订单号: 建议为32位字符串(不超过32位)
/// @param version     openAPI接口版本号,默认为1.0.0
/// @param license     由腾讯服务分配的,和 bundle id 关联****
/// @param succeed      SDK 登录成功
/// @param failed        SDK 登录失败
- (void)initSDKWithSDKType:(WBOCRCardType)sdkType
                     appId:(nonnull NSString *)appId
                     nonce:(nonnull NSString *)nonce
                    userId:(nonnull NSString *)userId
                      sign:(nonnull NSString *)sign
                   orderNo:(nonnull NSString *)orderNo
                   version:(nonnull NSString *)version
                   license:(nonnull NSString *)license
                   succeed:(nonnull WBOCRServiceInitSucceedBlock)succeed
                    failed:(nonnull WBOCRServiceFailedBlock)failed;
startService 接口如下, 通过 recognizeSucceed 接收识别成功回调，通过 failed 接收识别失败回调。
/// 标准版本 SDK 识别接口
/// @warning 调用这个接口前, 需要完成 SDK 登录, 即需要调用 initSDK 接口,并收到 succeed 回调
/// @param recognizeSucceed 识别成功回调
/// @param failed           识别失败回调
- (void) startOCRService:(nonnull WBOCRServiceRecognizeSuccessBlock)recognizeSucceed
                  failed:(nonnull WBOCRServiceFailedBlock)failed;
```


### 3. 接入示例
具体接入示例，请参考 demo 工程。

### 4. 识别结果处理
SDK 入口方法提供了三个回调 block ，通过这几个 block 来捕获识别结果或者异常状况。

#### 4.1 WBOCRServiceInitSucceedBlock（成功进入 SDK 回调）
进入这个回调，说明当前用户已经通过 SDK 鉴权，应用成功进入 SDK 界面了。

#### 4.2 WBOCRServiceRecognizeSuccessBlock（识别成功，即将退出 SDK 回调）
进入这个回调，说明 SDK 已经识别成功，即将退出，回到 App 中的界面，这里面有两个参数 resultModel 和 extension。
- resultModel 是对识别结果的封装，如果当前识别的是身份证，就会返回一个 WBIDCardInfoModel 类型的实例；如果当前识别的是银行卡，返回的是一个 WBBankCardInfoModel 类型的实例。关于每个字段的详细含义，请参考 WBOCRService.h 头文件。
- extension 是一个扩展字段，备用，目前版本为空，不需要处理。

#### 4.3 WBOCRServiceFailedBlock（SDK 异常，即将退出 SDK 回调）
进入这个回调，说明 SDK 发生异常，SDK 即将退出，可以通过这个回调获取失败信息，这里面有两个参数 error 和 extension。
- error 是一个 NSError 类型的实例，里面会封装错误码和错误描述，下面代码展示了一条错误码为200101的 error 信息，具体的错误码对照表请参考 [OCR iOS 错误码](https://cloud.tencent.com/document/product/1007/35856) 文档。
```
NSError *error = [NSError errorWithDomain:@"com.ocr.error" code:200101 userInfo:@{NSLocalizedDescriptionKey:@"用户取消操作"}];
```
- extension 是一个扩展字段，备用，目前版本为空，不需要处理。

## OCR iOS 错误码

|返回码 | 返回信息 | 处理措施|
|------- |--------- |----------|
|100100|传入 SDK 参数不合法|检查传入参数是否合法|
|100101 | 无网络，请确认 | 确认网络正常|
|100102 | 不支持 2G 网络 | 更换网络环境|
|100103 | 无相机权限 | -|
|200101 | 用户取消操作 | 用户主动退出操作|
|200102 | 识别超时 | 用户在身份证正反面识别过程中超过设定的阈值（20S）无法识别，提示超时|


### 多重告警码描述
在 OCR SDK 2.2.0版本，引入了多重告警码：
- 银行卡识别时，在 WBBankCardInfoModel 类的头文件中，增加了三个字段：清晰度 clarity 字段，多重警告码 multiWarningCode 和多重警告码描述 multiWarningMsg 字段。
- 身份证人像面识别时，在 WBIDCardInfoModel 类的头文件中，增加了两个字段：清晰度 frontClarity 字段，多重警告码 frontMultiWarning 字段。
- 身份证国徽面识别时，在 WBIDCardInfoModel 类的头文件中，增加了两个字段：清晰度 backClarity 字段，多重警告码 backMultiWarning 字段。

识别成功的时候，在 recognizeSucceed 的回调中，通过获取 resultModel 中的相应字段来获取多重告警码。


