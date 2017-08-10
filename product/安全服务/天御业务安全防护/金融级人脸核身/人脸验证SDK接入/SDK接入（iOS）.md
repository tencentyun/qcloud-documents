### 1.接入配置
   **WeBankService SDK最低支持到iOS8.0(iOS7系统可以编译但是无法使用),请在构建项目时候注意.**
1)引用资源文件WBFaceV2Pics.bundle,ufa.bundle,youtubeauty.bundle到项目
2)引用WBCloudFaceVerifySDK.framework, YTFaceSDK.framework, NextCV.framework到项目
3)SDK依赖系统的以下框架: `libz.tbd`,`Security.framework`,`MobileCoreServices.framework`,`Accelerate.framework`,`SystemConfiguration.framework`,`libc++.tbd`,`CoreTelephony.framework`,`AVFoundation.framework`,`AudioToolbox.framework`, `CoreMedia.framework`. 需要在`BuildPhases->Link Binary With Libraries`中添加,可以参考Demo
4)SDK需要使用相机,相册和录音权限,请在info.plist中添加Privacy - Microphone Usage Description, Privacy - Camera Usage Description,Privacy - Photo Library Usage Description
5)
6)需要在BuildSettings->Other Linker Flags中设置
-ObjC
-force_load
$(PROJECT_DIR)/该sdk在项目中的具体路径/NextCV.framework/NextCV
$(PROJECT_DIR)/该sdk在项目中的具体路径/YTFaceSDK.framework/YTFaceSDK

### 2.调用SDK接口
SDK的功能通过WBFaceVerifyCustomerService这个类的方法进行调用 ,<font color=red>其中SDK中使用的nonce, sign等重要信息,需要合作方从自己后台拉取,并且两者不能缓存,只能使用一次即失效</font color=red>, 详细接口说明如下, 其他的操作请参考Demo:
```
// SDK版本号
UIKIT_EXTERN NSString *const WBCloudFaceVerifySDKVersion;

// SDK界面风格等配置字段key值
UIKIT_EXTERN NSString *const WBFaceExternalIsShowSuccessPageKey;//BOOL
UIKIT_EXTERN NSString *const WBFaceExternalIsShowFailurePageKey;// BOOL
UIKIT_EXTERN NSString *const WBFaceExternalIsLightnessKey; // BOOL
UIKIT_EXTERN NSString *const WBFaceExternalIsShowGuidePageKey; //BOOL

// SDK自带比对源功能相关配置参数
UIKIT_EXTERN NSString *const WBFaceExternalIsUsingSourceImageKey; //BOOL
UIKIT_EXTERN NSString *const WBFaceExternalIsUsingHDImageKey; //BOOL (图像是否为高清图像/或者公安网文图像)
UIKIT_EXTERN NSString *const WBFaceExternalSourceImageKey; //UIImage(自带比对源图片大小不能超过2M)

// SDK在运行结束退出时候会发出通知. 具体的通知内容可以见delegate方法wbfaceVerifyCustomerServiceDidFinished:中的注释
UIKIT_EXTERN NSString *const WBFaceVerifyCustomerServiceDidFinishedNotification;

//登录的错误码
typedef NS_ENUM(NSInteger, WBFaceVerifyLogin) {
    WBFaceVerifyLogin_ERROR = -10000, // 登录请求返回报错
    WBFaceVerifyLogin_PARAMS_ERROR = -20000,// 登录请求传入参数有误
    WBFaceVerifyLogin_NORESPONSE_ERROR = -30000 // 登录请求网络错误
};

typedef NS_ENUM(NSInteger, WBFaceVerifySDKErrorCode) {
    WBFaceVerifySDKErrorCode_SUCESS = 0,// 身份认证成功
    WBFaceVerifySDKErrorCode_FAILURE = 1,// 身份认证出错
    WBFaceVerifySDKErrorCode_CANCELLED = 2,// 用户取消认证
};

typedef NS_ENUM(NSInteger,WBFaceVerifyType){
    WBFaceVerifyTypeSimple, // 暂时不要使用Simple模式
    WBFaceVerifyTypeMiddle,
    WBFaceVerifyTypeAdvanced,
};

typedef void (^WBFaceLoginSuccessBlock)(void);
//登录过程中 loginCode  细分错误码 ---  -2 表示登录时网络错误, -1 表示登录时webank后台返回出错, 0 表示登录通用默认码, 其他数字透传webank后台错误码(请参考后台文档)
typedef void (^WBFaceLoginFailureBlock)(WBFaceVerifyLogin errorCode, NSString *loginCode, NSString *message);

@interface WBFaceUserInfo : NSObject
@property (nonatomic,copy) NSString *orderNo; // 订单号（合作方上送，每次唯一）
@property (nonatomic,copy) NSString *name;    // 姓名
@property (nonatomic,copy) NSString *idType;  // 证件类型
@property (nonatomic,copy) NSString *idNo;    // 证件号码

/**
 判断UserInfo信息是否满足要求,内部只判断属性是否有nil
 */
-(BOOL)isPropertyRight;
@end

/**
   处理刷脸回调
 */
@class WBFaceVerifyCustomerService;
@protocol WBFaceVerifyCustomerServiceDelegate  <NSObject>

/**
 注意:
 1. 如果实现该代理方法(wbfaceVerifyServiceGetViewController:),则向WBFaceVerifyCustomerService SDK中通过代理传入一个ViewController,在sdk登录成功以后会在该viewController通过presentViewControllerxxxx方法拉起人脸认证页面.

 2. 如果没有实现该代理方法(wbfaceVerifyServiceGetViewController:), 那么SDK会创建一个UIWindow覆盖在当前界面,并在新创建的UIWindow界面进行人脸认证,并且可以通过实现 wbfaceVerifyServiceGetWindowLevel 代理方法,传入创建的UIWindow的windowLevel, 传入的windowLevel必须是1~999, 默认情况如果不实现 wbfaceVerifyServiceGetWindowLevel 方法,windowLevel = UIWindowLevelNormal + 1

 */
@optional
- (UIViewController *)wbfaceVerifyServiceGetViewController:(WBFaceVerifyCustomerService *)service;
@optional
- (NSUInteger)wbfaceVerifyServiceGetWindowLevel;

/**
 *  刷脸身份认证的回调方法,带结果签名sign的回调
 *
 *  @param errorCode iOS SDK定义的概要错误码 -- 重要信息: 身份认证成功与失败都在这里显示
 *  @param faceCode  细分错误码 ---  -2 表示网络错误, -1 表示webank后台返回出错, 0 表示通用默认码, 其他数字透传webank后台错误码(请参考后台文档)
 *  @param faceMsg   身份认证错误的相关提示信息
 *  @param sign      当前身份认证结果的签名信息
 
 
   注意!!!!!!!!!!!!!

   可以不实现该sdk方法,通过注册WBFaceVerifyCustomerServiceDidFinishedNotification这个通知,通过通知的n.userInfo同样可以拿到errorCode, faceCode, faceMsg, sign 以及 orderNo(之前传入sdk的订单号)等刷脸结果返回的信息.
 */
@optional
-(void)wbfaceVerifyCustomerServiceDidFinished:(WBFaceVerifySDKErrorCode)errorCode faceCode:(NSString *)faceCode faceMsg:(NSString *)faceMsg sign:(NSString *)sign;

/**
 *  SDK扩展字段
 *  WBFaceExternalIsShowSuccessPageKey BOOL 表示是否显示身份认证成功的结果页(默认情况显示 - YES)
 *  WBFaceExternalIsShowFailurePageKey BOOL 表示是否显示身份认证失败的结果页(默认情况显示 - YES)
 *  WBFaceExternalIsLightnessKey       BOOL 表示是否使用明亮主题的人脸验证界面风格(默认状态是暗黑主题页面风格)
 *  WBFaceExternalIsShowGuidePageKey   BOOL 表示是否显示身份认证前的引导页(默认情况显示 - YES)
 *
 *  在delegate实现中实现该方法
 -(NSDictionary *)wbfaceVerifyServiceGetExternalParams:(WBFaceVerifyCustomerService *)service{
     return @{
         WBFaceExternalIsShowFailurePageKey : @(YES),
         WBFaceExternalIsShowSuccessPageKey : @(YES),
         WBFaceExternalIsLightnessKey: @(YES),
         WBFaceExternalIsShowGuidePageKey, @(YES),
         WBFaceExternalIsUsingSourceImageKey, @(NO),
    };
 }
 
 注意: 该方法和 -(void)startWBFaceServiceWithUserid:(NSString *)userid nonce:(NSString *)nonce sign:(NSString *)sign appid:(NSString *)appid userInfo:(WBFaceUserInfo *)userInfo apiVersion:(NSString *)apiVersion faceverifyType:(WBFaceVerifyType)type licence:(NSString *)licence success:(WBFaceLoginSuccessBlock)success failure:(WBFaceLoginFailureBlock)failure externalParams:(NSDictionary *)extenalParams; 方法中的最后一个参数extenalParams功能一致, 可以不用设置delegate, 直接使用该StartWBFaceServiceXXXX方法,在最后一个参数extenalParams传入配置参数.
 */
@optional
-(NSDictionary *)wbfaceVerifyServiceGetExternalParams:(WBFaceVerifyCustomerService *)service;

/**
 *********************************************************************
 ***************************** 废弃接口 *******************************
 *********************************************************************
- (UIViewController *)getViewController NS_DEPRECATED_IOS(2_0, 2_0, "该回调方法是前向兼容方法,请使用 wbfaceVerifyServiceGetViewController: 方法");
-(void)wbfaceVerifyCustomerServiceDidFinished:(WBFaceVerifySDKErrorCode)errorCode faceCode:(NSString *)faceCode faceMsg:(NSString *)faceMsg NS_DEPRECATED_IOS(2_0, 2_0, "该回调方法是前向兼容方法方法,请使用 wbfaceVerifyCustomerServiceDidFinished:faceCode:faceMsg:sign: 方法");
 */
@end

@interface WBFaceVerifyCustomerService : NSObject
@property (nullable,nonatomic,weak) id<WBFaceVerifyCustomerServiceDelegate> delegate;

/*
 * SDK全局单例,请使用此单例.不要使用init创建对象
 */
+ (instancetype)sharedInstance;

/**
 *  调用SDK服务核心方法 1
 *
 *  @param userid     userid 每个用户唯一的标识
 *  @param nonce      每次请求需要的一次性nonce
 *  @param sign       对nonce,userid等重要信息的签名数据
 *  @param appid      每个与webank合作分配的appid
 *  @param userInfo   用户信息对象,请参考前面定义的内容
 *  @param apiVersion 后台api接口版本号(不是SDK的版本号),默认请填写@"1.0.0"
 *  @param type       身份认证的类型- 简单模式,中级模式,高级模式
 *  @param licence    webank给合作方派发的licence
 *  @param success    调用sdk登录成功回调.请在该回调方法中关闭loading,并且在success block执行以后,sdk为拉起人脸认证页面
 *  @param failure    调用sdk登录失败时回调.请在该回调方法中关闭loading,处理错误逻辑.
 */
-(void)startWBFaceServiceWithUserid:(NSString *)userid
                              nonce:(NSString *)nonce
                               sign:(NSString *)sign
                              appid:(NSString *)appid
                           userInfo:(WBFaceUserInfo *)userInfo
                         apiVersion:(NSString *)apiVersion
                     faceverifyType:(WBFaceVerifyType)type
                            licence:(NSString *)licence
                            success:(WBFaceLoginSuccessBlock)success
                            failure:(WBFaceLoginFailureBlock)failure;


/**
 *  调用SDK服务核心方法2
 *
 *  @param userid     userid 每个用户唯一的标识
 *  @param nonce      每次请求需要的一次性nonce
 *  @param sign       对nonce,userid等重要信息的签名数据
 *  @param appid      每个与webank合作分配的appid
 *  @param userInfo   用户信息对象,请参考前面定义的内容
 *  @param apiVersion 后台api接口版本号(不是SDK的版本号),默认请填写@"1.0.0"
 *  @param type       身份认证的类型- 简单模式,中级模式,高级模式
 *  @param licence    webank给合作方派发的licence
 *  @param success    调用sdk登录成功回调.请在该回调方法中关闭loading,并且在success block执行以后,sdk为拉起人脸认证页面
 *  @param failure    调用sdk登录失败时回调.请在该回调方法中关闭loading,处理错误逻辑.
 *  @param extenalParams  
 *                  参数与"-(NSDictionary *)wbfaceVerifyServiceGetExternalParams:(WBFaceVerifyCustomerService *)service"接口提供的返回参数功能相同
                    传入字典如下:
                     @{
                         WBFaceExternalIsShowFailurePageKey : @(YES),
                         WBFaceExternalIsShowSuccessPageKey : @(YES),
                         WBFaceExternalIsLightnessKey: @(YES),
                         WBFaceExternalIsShowGuidePageKey, @(YES),
                     }
 */
-(void)startWBFaceServiceWithUserid:(NSString *)userid
                              nonce:(NSString *)nonce
                               sign:(NSString *)sign
                              appid:(NSString *)appid
                           userInfo:(WBFaceUserInfo *)userInfo
                         apiVersion:(NSString *)apiVersion
                     faceverifyType:(WBFaceVerifyType)type
                            licence:(NSString *)licence
                            success:(WBFaceLoginSuccessBlock)success
                            failure:(WBFaceLoginFailureBlock)failure
                     externalParams:(NSDictionary *)extenalParams;
@end
```

### 3.接口参数说明
| 参数 | 说明 |类型 |长度 | 是否必输 |
|---------|---------|---------|---------|---------|
| userid | 用户唯一的标识 | NSString |30 |必输，必须保证全局唯一|
| nonce | 32位随机字符串| NSString |32 |必输(生成方式参考后台文档) |
| sign    | 合作方后台服务器通过ticket计算出来的签名信息 | NSString |40 |必输(生成方式参考后台文档)|
| appid | 腾讯服务分配的app_id | NSString |腾讯服务分配 |必输|
| apiVersion | 接口版本号 | NSString |默认填1.0.0 |必输|
| licence | 腾讯给合作方派发的licence | NSString |绑定bundleid |必输 |
| userInfo | 用户信息 | WBFaceUserInfo |Class类型 |必输 |
| orderNo | 订单号 |  NSString |32位 |必输(参考后台文档)|
| name | 客户姓名 | NSString |20 |必输(身份证姓名) |
| idType | 证件类型 | NSString |2 |01为身份证必输 |
| idNo | 18位身份证号 | NSString |18 |必输 |
| Type | 模式类型 | WBFaceVerifyType | |中级模式：<br>WBFaceVerifyTypeMiddle,<br>高级模式：<br>WBFaceVerifyTypeAdvanced,|


### 4.个性化参数设置
WBFaceVerifyCustomerServiceDelegate的回调方法中,有如下扩展配置选项,直接参考sdk头文件注释即可

```
@optional
/**
 *  SDK扩展字段
 *  WBFaceExternalIsShowSuccessPageKey BOOL 表示是否显示身份认证成功的结果页
 *  WBFaceExternalIsShowFailurePageKey BOOL 表示是否显示身份认证失败的结果页(默认情况显示 – YES)
 *  WBFaceExternalIsLightnessKey       BOOL 表示是否使用明亮主题的人脸验证界面风格(默认状态是暗黑主题页面风格)
 *  WBFaceExternalIsShowGuidePageKey    BOOL 表示是否展示引导页页面
 *  在delegate实现中实现该方法
 -(NSDictionary *)wbfaceVerifyServiceGetExternalParams:(WBFaceVerifyCustomerService *)service{
     return @{
         WBFaceExternalIsShowSuccessPageKey : @(YES),
         WBFaceExternalIsShowFailurePageKey: @(YES),
         WBFaceExternalIsLightnessKey: @(YES),
         WBFaceExternalIsShowGuidePageKey: @(YES),
     };
 }
 */
-(NSDictionary *)wbfaceVerifySerivceGetExternalParamsWBFaceVerifyCustomerService:)service;
```