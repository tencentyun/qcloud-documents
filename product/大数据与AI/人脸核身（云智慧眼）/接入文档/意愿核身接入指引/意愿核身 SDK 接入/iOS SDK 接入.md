>! 接入之前，请详细阅读 SDK 中的 readme 和接入指引。

以下为接入配置的步骤。
## 配置流程
### 使用 Cocoapod 集成
SDK 最低支持到 iOS11.0，请在构建项目时候注意，目前仅支持 Xcode11.0及更高版本编译。
以下为接入配置的步骤：
1. 将 TencentCloudHuiyanSDKFace_framework 文件夹拷贝到自己项目的 podfile 文件所在的同一目录。
2. 将 TencentCloudHuiyanSDKWill_framework 文件夹拷贝到自己项目的 podfile 文件所在的同一目录。
3. 在 podfile 使用如下配置(请注意 target 后面内容根据自己项目配置，参考 demo)：
```
target ‘WBCloudReflectionFaceVerify-Demo’ do
pod ‘TencentCloudHuiyanSDKFace_framework’, :path=>‘./ TencentCloudHuiyanSDKFace_framework’
pod ‘TencentCloudHuiyanSDKWill_framework’, :path=>‘./ TencentCloudHuiyanSDKWill_framework’
end
```
4. 使用 pod install 命令
5. SDK 需要使用相机以及麦克风权限，请在 info.plist 中添加：
```
Privacy - Camera Usage Description
Privacy - Microphone Usage Description
```

### 直接引用 framework
SDK 最低支持到 iOS11.0，请在构建项目时候注意。
以下为接入配置的步骤：
1. 引用以下资源文件到项目：
```
TencentCloudHuiyanSDKFace.framework
TencentCloudHuiyanSDKWill.framework
YTCommonLiveness.framework
YTFaceTrackerLiveness.framework
YTFaceAlignmentTinyLiveness.framework
YTPoseDetector.frameworks
YTFaceDetectorLiveness.framework      
YTFaceLiveReflect.framework
tnnliveness.framework
TuringShieldCamRisk.framework
TencentCloudHuiyanSDKFace.bundle
TencentCloudHuiyanSDKWill.bundle
face-tracker-v001.bundle
KYCGMSDK.framework
YTCv.framework
YtSDKKitFrameworkTool.framework
```
2. SDK 依赖以下系统框架,需要在 **BuildPhases > Link Binary With Libraries** 中添加，可以参考 Demo，具体依赖的系统库如下：
```
UIKit.framewrok
AVFoundation.framework
CoreVideo.framework
Security.framework
SystemConfiguration.framework
CoreMedia.framework
CoreTelephony.framework
ImageIO.framework
MediaPlayer.framework
Accelerate.framework
WebKit.framework
libc++.tbd
libz.tbd
videoToolbox.framework
```
3. SDK 需要使用相机权限，请在 info.plist 中添加：
```
Privacy - Camera Usage Description
Privacy - Microphone Usage Description
```
4. 需要在 **BuildSettings > Other Linker Flags** 中设置：`-ObjC`。

## 接口调用
### SDK 接口调用方法
SDK 的功能通过 WBFaceVerifyCustomerService 这个类的方法进行调用 ，其中 SDK 中使用的 nonce，sign 等重要信息，需要合作方从自己后台拉取，并且两者不能缓存，只能使用一次即失效，详细接口说明如下，其他的操作请参考 Demo 中的登录接口的参数说明 ：
版本号及宏定义说明：
```
#import <UIKit/UIKit.h> 
#ifndef WBFaceVerifyConst_h
#define WBFaceVerifyConst_h
#define WBCloudReflectionFaceVerifyVersion

UIKIT_EXTERN NSString *const WBCloudFaceVerifySDKVersion;

#endif /* WBFaceVerifyConst_h */

```
入口方法说明：
NONCE 类型的 ticket，其有效期为120秒，且一次性有效，即每次启动 SDK 刷脸都要重新请求 NONCE ticket，重新算sign。同时建议合作方做前端保护，防止用户连续点击，短时间内频繁启动 SDK。
```
（1）faceID +活体检测+人脸比对服务（身份证的网纹照片进行对比）
/*
意愿性SDK入口，注意传入的faceId不能为空

@param userid 用户唯一标识, 由合作方自行定义（具体要求，参考接入文档）
@param nonce  满足接入要求的32位随机数（具体要求，参考接入文档）
@param sign 满足接入要求的40位签名值（具体要求，参考接入文档）
@param appid 腾讯服务分配的appid
@param orderNo 每次人脸身份认证请求的唯一订单号: 建议为32位字符串(不超过32位)
@param apiVersion 后台api接口版本号(不是SDK的版本号),默认请填写@"1.0.0"
@param licence 腾讯给合作方派发的前端使用的licence(该licence同app当前使用的bundle id绑定)
@param faceId 合作方必须要先获取*增强级*faceId，再送入sdk，不允许为空(参考接入文档)
@param sdkConfig SDK基础配置项目
@param success 服务登录成功回调,登录成功以后开始进行活体和检测服务
@param failure 服务登录失败回调,具体参考错误码文档(参考接入文档)
*/
-(void)initWillSDKWithUserId:(NSString *)userid
                   nonce:(NSString *)nonce
                    sign:(NSString *)sign
                   appid:(NSString *)appid
                 orderNo:(NSString *)orderNo
              apiVersion:(NSString *)apiVersion
                 licence:(NSString *)licence
                  faceId:(NSString *)faceId
               sdkConfig:(WBFaceVerifySDKConfig *)sdkConfig
                 success:(void (^)())success
                 failure:(void (^)(WBFaceError * _Nonnull))failure;
/**
 以上一次的登陆结果拉起刷脸页面，必须先登录再拉起刷脸页面
 
 @return 拉起是否成功
 */
- (BOOL)startWbFaceVeirifySdk;
```

个性化参数设置：
SDK 登录接口 initSDK 方法中需要传入 WBFaceVerifySDKConfig 字段，通过该对象可以配置 SDK 中其他基础配置。
```
/**
 人脸识别SDK 基础配置类
 */
@interface WBFaceVerifySDKConfig : NSObject


#pragma mark - common
/**
 sdk中拉起人脸活体识别界面中使用UIWindow时的windowLevel配置,默认配置是1 + UIWindowLevelNormal

 如果接入放app中有其他自定义UIWindow, 为了防止界面覆盖,可以酌情设置该参数
 */
@property (nonatomic, assign) NSUInteger windowLevel;

/**
 人脸识别服务是否进行通过录像, 从而进行视频存证

 default: NO
 */
@property (nonatomic, assign) BOOL recordVideo;

/**
 是否由SDK内部处理sdk网络请求的cookie

 默认值: YES
 */
@property (nonatomic, assign) BOOL manualCookie;

/**
 是否静音
 默认值：YES
 */
@property (nonatomic, assign) BOOL mute;


/*
 送入自定义提示文案的位置
 默认：WBFaceCustomTipsLoc_Bottom
 */
@property (nonatomic, assign) WBFaceCustomTipsLoc tipsLoc;

/*
 检测过程中展示的文案
 默认为空
 */
@property (nonatomic, copy) NSString *customTipsInDetect;

/*
 上传过程中展示的文案
 默认为空
 */
@property (nonatomic, copy) NSString *customTipsInUpload;

/*
 底部提示文案，长度不超过70字
 */
@property (nonatomic, copy) NSString *bottomCustomTips;

/*
 退出二次确认UI配置
 */
@property (nonatomic, copy) NSString *exitAlertTitle; //标题
@property (nonatomic, copy) NSString *exitAlertMessage; //内容
@property (nonatomic, copy) NSString *exitAlertRight; //右边按钮
@property (nonatomic, copy) NSString *exitAlertLeft; //左边按钮

/*
 如果有使用苹果分屏模式（UIWindowScene），打开此开关
 Xcode11新建工程有使用Scene，可以参考资料自行调整
 默认为NO
 */
@property (nonatomic, assign) BOOL useWindowSecene;

/*
意愿性表达视频录制参数
*/
@property (nonatomic, assign) BOOL recordWillVideo;
@property (nonatomic, assign) BOOL checkWillVideo;

/**
 默认sdk配置
 */
+(instancetype)sdkConfig;

@end

```
## 核身结果返回
IOS SDK 中，意愿性结果返回给接入方有两种方式，两种结果回调都在 Main Thread 完成：
您可以信任前端 SDK 意愿性结果，返回中的 isSuccess 字段 YES 代表意愿性流程成功；NO 代表意愿性流程失败。意愿性 SDK 和核身后台服务之间通信采用加密方式，可以有效防止结果篡改。
1. 通过实现 WBFaceVerifyCustomerServiceDelegate 的 WBFaceVerifyCustomerServiceDelegate 方法,通过该方法返回WBFaceVerifyResult 对象。
2. 无需实现 delegate 方法，通过注册 WBFaceVerifyCustomerServiceDidFinishedNotification 通知，在接受到该通知时，进行结果处理。

WBFaceVerifyCustomerServiceDidFinishedNotification 通知中，通过获取该通知的 userInfo，获取字典中 key 为faceVerifyResult 对应的 value 对象就是 WBFaceVerifyResult。

### WBFaceVerifyResult 对象说明

| 字段名 | 类型 | 字段含义 |说明| 
|---------|---------|---------|---------|
| isSuccess	| BOOL	| 人脸核身是否成功	| YES 代表认证成功，NO 代表认证失败，具体原因参考 error 描述| 
| sign	| NSString| 	签名| 	供 App 校验意愿性结果的安全性| 
| liveRate	| NSString	| 活体检测分数| 	-| 
| similarity	| NSString	| 人脸比对分数| 	“仅活体检测” 类型不提供此分数| 
| userImageString	| NSString	| 用户人脸核身图片	| 经过 Base64编码后的用户人脸核身图片，用来做比对认证的最优图| 
| WbFaceError	| 自定义对象	| 人脸核身错误	| 意愿性成功时为 **nil**| 

### WBWillModeResult 说明
| 字段名 | 类型 | 字段含义 |说明| 
|---------|---------|---------|---------|
| faceCode	| NSString	| 人脸识别结果码| 	-| 
| faceMsg| 	NSString	| 人脸识别结果信息| 	-| 
| willCode	| NSString	| ASR 结果码| 	-| 
| willMsg| 	NSString| 	ASR 结果信息| 	-| 
| videoURL	| NSURL	| 意愿性存证视频存储地址	| 如果打开了本地存储意愿性视频开关,将在此处返回意愿性视频地址| 

### WBFaceError 对象说明
| 字段名 | 类型 | 字段含义 |说明| 
|---------|---------|---------|---------|
| domain	| NSString| 	错误发生的阶段| 只有当 domain=WBFaceErrorDomainCompareServer 时表示用户完成了刷脸，可以通过接口去拉取刷脸结果。其他 domain 表示用户刷脸中途退出或命中了风控逻辑，后端无法查询到刷脸结果| 
| code	| NSString	| 错误码| 	-| 
| desc	| NSString	| 错误描述	| 如有需求，可以展示给用户| 
| reason	| NSString	| 错误信息内容	| 错误的详细实际原因，主要用于定位问题| 

### WBFaceVerifyResult 说明
```
@interface WBFaceWillModeResult : NSObject
/*
 核身结果的对应错误码
 */
@property (nonatomic, copy, readonly) NSString *faceCode;
/*
 核身结果的对应错误描述
 */
@property (nonatomic, copy, readonly) NSString *faceMsg;
/*
 意愿性结果的对应错误码
 */
@property (nonatomic, copy, readonly) NSString *willCode;
/*
 意愿性结果的对应错误描述
 */
@property (nonatomic, copy, readonly) NSString *willMsg;

@end
/**
 人脸服务返回结果对象
 */
@interface WBFaceVerifyResult : NSObject
/**
 人脸比对结果是否通过:

 YES: 表示人脸服务通过
 NO:  表示人脸服务不通过lo
 */
@property (nonatomic, assign, readonly) BOOL isSuccess;

/**
 结果对应的订单号
 */
@property (nonatomic, copy, readonly) NSString *orderNo;

/**
 isSuccess == YES 时, sign有值,可以去后台拉取本次人脸服务的照片,视频存证
 isSuccess == NO  时, sign 无意义
 */
@property (nonatomic, copy, readonly) NSString * sign;
/**
 活体检测服务得分

 isSuccess == YES 时, liveRate 有值:
        1. liveRate 可能是 @"分数为空", 这种情况具体咨询合作方
        2. float类型的字符串, 请调用 [liveRate floatValue] 获取具体分数
 isSuccess == NO  时, liveRate 无意义
 */
@property (nonatomic, copy, readonly) NSString * liveRate;

/**
 人脸比对服务得分

 isSuccess == YES 时, similarity 有值:
         1. similarity 可能是 @"分数为空", 这种情况具体咨询合作方
         2. float类型的字符串, 请调用 [similarity floatValue] 获取具体分数
 isSuccess == NO  时, similarity 无意义
 */
@property (nonatomic, copy, readonly) NSString * similarity;

/**
 人脸比对图片之一

 isSuccess == YES 时, 该属性是上送比对图片之一UIImage的base64编码字符串(图片格式是jpg)

 isSuccess == NO  时, 如果是SDK返回的错误，该属性为nil，如果是后端返回的错误，该属性是上送比对图片之一UIImage的base64编码字符串(图片格式是jpg)
 */
@property (nonatomic, copy, readonly) NSString * userImageString;

/**
 isSuccess == YES 时候, error 无意义
 isSuccess == NO  时, error中存储的具体错误信息,参考 WBFaceError.h
 */
@property (nonatomic, strong, readonly) WBFaceError * error;

#pragma mark - 意愿性SDK返回参数
@property (nonatomic, strong, readonly) WBFaceWillModeResult *willModeResult;

#pragma mark -

-(NSString *)description;
@end

```

## 错误码描述
SDK 在登录以及返回人脸服务结果时，如果发生错误或者识别失败会返回 WBFaceError 对象，该对象的结构如下, 并且在我们判断具体错误时, 需要先根据 domain 字段判断错误发生在 sdk 服务运行中的位置, 然后根据 code 判断具体的错误：
```
*/
NS_ASSUME_NONNULL_BEGIN
/*
 错误domain划分成两类:

 出现在登录时, 通过调用startXXXX 方法的failure block进行回调返回:
 WBFaceErrorDomainInputParams, WBFaceErrorDomainLoginNetwork, WBFaceErrorDomainLoginServer

 人脸服务结果返回(封装在WBFaceVerifyResult中):
 WBFaceErrorDomainGetInfo, WBFaceErrorDomainNativeProcess, WBFaceErrorDomainCompareNetwork, WBFaceErrorDomainCompareServer
 */

/* 登录时传入参数有误 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainInputParams;
/* 登录时网络请求错误 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainLoginNetwork;
/* 登录时后台拒绝登录, 具体参考后台word版本错误码, 这里直接透传 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainLoginServer;
/* 拉取有效信息时候网络错误 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainGetInfo;
/* native本地在活体检测中, 某些原因导致错误 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainNativeProcess;
/* 上送后台比对时,网络错误 */
UIKIT_EXTERN NSString *const WBFaceErrorDomainCompareNetwork;
/* 后台比对完成,返回比对结果的错误原因*/
UIKIT_EXTERN NSString *const WBFaceErrorDomainCompareServer;

@interface WBFaceError: NSObject
/**
 错误发生的地方, 具体的发生地方由上面定义的 WBFaceErrorDomainXXXX 指定
 */
@property (nonatomic, readonly, copy) NSString *domain;
/**
 每个domain中有相应的错误代码, 具体的错误代码见
 */
@property (nonatomic, readonly, assign) NSInteger code; //错误代码
@property (nonatomic, readonly, copy) NSString *desc; //获取本地化描述
@property (nonatomic, readonly, copy) NSString *reason; // 错误出现的真实原因原因
@property (nonatomic, readonly, copy) NSDictionary * _Nullable otherInfo;// 预留接口
@end
```
以下是 Domain 为不同值时，对应的 code 和错误描述信息：
**若 Domain 为 WBFaceErrorDomainInputParams**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 12000	| 传入参数为空	| 传入的 xx 为空| 
| 12001	| 传入的 keyLicence 不可用	| 传入的 keyLicence 不可用| 
| 12002	| 身份证格式不正确	| 身份证格式不正确| 
| 12003	| 使用自带对比源，传入参数错误，非 base64	| 传入的 srcPhotoString 不是base64| 
| 12004	| 使用自带对比源，传入参数错误，超过 1 MB	| 传入的 srcPhotoString 超过 1 MB| 
| 12005| 	SDK 资源引入版本不匹配	| 没有引入资源包或者引入的资源包版本与当前 SDK 版本不匹配| 
| 12006	| 订单号不能为 0 或者超过 32 位| 	-| 
| 12007	| nonce 字符串位数不为32 位| 	-| 
| 12009     	| 定制化SDK生成参数失败	| -| 
| 12010	| 定制化参数校验错误| 	-| 

**Domain 为：WBFaceErrorDomainLoginNetwork**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 22100	| 网络异常	| 登录时网络异常（请求未到达后台）| 
| 22200	| 网络异常	| 登录时后台返回参数有误（请求到达后台）| 
| 22003	| 请勿晃动人脸，保持姿势	| 未获取到最佳图片| 

**Domain 为：WBFaceErrorDomainLoginServer**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 其他错误码	| 透传后台错误码	| 例如签名问题等| 

**Domain 为：WBFaceErrorDomainGetInfo**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 32100	| 网络异常	| 获取数字/活体类型/光线阈值，网络异常(请求未到达后台)| 
| 32200	| 网络异常	| 获取数字/活体类型/光线阈值，后台返回参数有误（请求到达后台）| 

**Domain 为：WBFaceErrorDomainNativeProcess**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 42000	| 用户取消	| 回到后台/单击 home/左上角/上传时左上角取消| 
| 42001	| 网络环境不满足认证需求	| 无网络/2g 网络| 
| 42002	| 权限异常，未获取权限	| 相机/麦克风/read phone/external/storage| 
| 42003	| 相机运行中出错| 	-| 
| 42004	| 视频录制中出错	| 不能存/启动失败/结束失败| 
| 42005	| 请勿晃动人脸，保持姿势	| 未获取到最佳图片| 
| 42006	| 视频大小不满足要求	| 视频大小不满足要求| 
| 42007	| 超时	| 预检测/动作活体| 
| 42008	| 检测中人脸移出框外	| 活体/数字/反光| 
| 42009	| 光线活体本地错误	| -| 
| 42010	| 风险控制超出次数	| 用户重试太多次| 
| 42011| 	没有检测到读数声音	| 数字活体过程中没有发声| 
| 42012 | 模型初始化失败| 	-| 
| 42015  | 	报文解密失败	| 请求报文解密失败| 
| 42101| 	音频录制中出错	| -| 
| 42102	| 没有检测到麦克风声音	| -| 
| 42103	| 播报音频文件加载失败	| -| 
| 42104	| 麦克风被占用，音频播报失败	| -| 
| 42105	| 视频录制中出错| 	
| 42106	| 音量过低，用户主动退出	| -  |  


**Domain 为：WBFaceErrorDomainCompareNetwork**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 52100	| 网络异常	| 对比时，网络异常（请求未到达后台）| 
| 52200| 	网络异常	| 对比时，后台返回参数有误（请求到达后台）| 

**Domain 为：WBFaceErrorDomainCompareServer**

| Code（错误码） | 	Description（描述） | 	Reason（详细实际原因） |
|---------|---------|---------|
| 其他错误码	| 透传后台错误码	| -| 

