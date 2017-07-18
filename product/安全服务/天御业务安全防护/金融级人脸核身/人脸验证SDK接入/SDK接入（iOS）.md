### 1.接入配置
   **WeBankService SDK最低支持到iOS8.0(iOS7系统可以编译但是无法使用),请在构建项目时候注意.**
1)引用资源文件WBFaceV2Pics.bundle,ufa.bundle,youtubeauty.bundle到项目
2)引用WBCloudFaceVerifySDK.framework, YTFaceSDK.framework, NextCV.framework到项目
3)SDK依赖系统的以下框架: `libz.tbd`,`Security.framework`,`MobileCoreServices.framework`,`Accelerate.framework`,`SystemConfiguration.framework`,`libc++.tbd`,`CoreTelephony.framework`,`AVFoundation.framework`,`AudioToolbox.framework`, `CoreMedia.framework`. 需要在`BuildPhases->Link Binary With Libraries`中添加,可以参考Demo
4)SDK需要使用相机,相册和录音权限,请在info.plist中添加Privacy - Microphone Usage Description, Privacy - Camera Usage Description,Privacy - Photo Library Usage Description
5)需要在BuildSettings->Other Linker Flags中设置-ObjC

### 2.调用SDK接口
SDK的功能通过WBFaceVerifyCustomerService这个类的方法进行调用 ,<font color=red>其中SDK中使用的nonce, sign等重要信息,需要合作方从自己后台拉取,并且两者不能缓存,只能使用一次即失效</font color=red>, 详细接口说明如下, 其他的操作请参考Demo:
```
// 参考WBFaceGetExternalParams delegate方法
UIKIT_EXTERN NSString *const WBCloudFaceVerifySDKVersion;//版本号

UIKIT_EXTERN NSString *const WBFaceExternalIsShowSuccessPageKey;//配置参数:是否显示人脸认证成功页面
UIKIT_EXTERN NSString *const WBFaceExternalIsShowFailurePageKey;//配置参数:是否显示人脸认证失败页面
UIKIT_EXTERN NSString *const WBFaceExternalIsLightnessKey;//配置参数:是否使用明亮主题
UIKIT_EXTERN NSString *const WBFaceExternalIsShowGuidePageKey;//配置参数:是否显示引导页
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

typedef void (^WBFaceLoginSuccessBlock)(void);
//faceCode : -2 表示网络原因出错, -1 表示后台返回参数有误  0 正常位
typedef void (^WBFaceLoginFailureBlock)(WBFaceVerifyLogin errorCode, NSString *faceCode, NSString *message);

// 现有的刷脸类型
typedef NS_ENUM(NSInteger,WBFaceVerifyType){
    WBFaceVerifyTypeMiddle,
    WBFaceVerifyTypeAdvanced,
};

@interface WBFaceUserInfo : NSObject
@property (nonnull,nonatomic,copy) NSString *orderNo; // 订单号（合作方上送，每次唯一）
@property (nonnull,nonatomic,copy) NSString *name;    // 姓名
@property (nonnull,nonatomic,copy) NSString *idType;  // 证件类型,身份证请填写01
@property (nonnull,nonatomic,copy) NSString *idNo;    // 证件号码
/**
 判断UserInfo信息是否满足要求,内部只判断属性是否有nil

 */
-(BOOL)isPropertyRight;
@end

@class WBFaceVerifyCustomerService;
/**
   处理刷脸回调
 */
@protocol WBFaceVerifyCustomerServiceDelegate  <NSObject>

@required


/*
 *  @param errorCode iOS SDK定义的概要错误码 -- 重要信息: 身份认证成功与失败都在这里显示
 *  @param faceCode  细分错误码
 *                      -2 表示网络错误, 
 *                      -1 表示腾讯后台返回出错, 
 *                      0  表示通用默认码
 *                     其他数字透传腾讯后台错误码(请参考后台文档)
 *  @param faceMsg   身份认证错误的相关提示信息
 *  @param sign      当前身份认证结果的签名信息(可以用于后台查询当前订单号人脸认证结果)
 *
 */
-(void)wbfaceVerifyCustomerServiceDidFinished:(WBFaceVerifySDKErrorCode)errorCode faceCode:(NSString *)faceCode faceMsg:(NSString *)faceMsg sign:(NSString *)sign;

/**
 *  向WBFaceVerifyCustomerService传入一个ViewController,在sdk登录成功以后会在该viewController通过presentViewControllerxxxx方法拉起人脸认证页面.
 *
 */
- (UIViewController *)wbfaceVerifyServiceGetViewController:(WBFaceVerifyCustomerService *)service;

@optional
/**
 *  SDK扩展字段
 *  WBFaceExternalIsShowSuccessPageKey BOOL 表示是否显示身份认证成功的结果页
 *  WBFaceExternalIsShowFailurePageKey BOOL 表示是否显示身份认证失败的结果页(默认情况显示 - YES)
 *  WBFaceExternalIsLightnessKey       BOOL 表示是否使用明亮主题的人脸验证界面风格(默认状态是暗黑主题页面风格)
 *  WBFaceExternalIsShowGuidePageKey   BOOL 表示是否展示引导页页面
 * 
 *  在delegate实现中实现该方法 – 例如
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
@end

@interface WBFaceVerifyCustomerService : NSObject
@property (nullable,nonatomic,weak) id<WBFaceVerifyCustomerServiceDelegate> delegate;

/*
 * SDK全局单例,请使用此单例.不要使用init创建对象
 */
+ (instancetype)sharedInstance;


/**
 *  调用SDK服务核心方法
 *
 *  @param userid     userid 每个用户唯一的标识(参考后台文档)
 *  @param nonce      每次请求需要的一次性nonce(参考后台文档)
 *  @param sign       对nonce,userid等重要信息的签名数据(参考后台文档)
 *  @param appid      每个与腾讯合作分配的appid
 *  @param userInfo   用户信息对象,请参考前面定义的内容
 *  @param apiVersion 后台api接口版本号(不是SDK的版本号),默认请填写@"1.0.0"
 *  @param type       身份认证的类型- 中级模式,高级模式
 *  @param licence    腾讯给合作方派发的licence
 *  @param success    调用sdk登录成功回调.请在该回调方法中关闭loading,
 *                          并且在success block执行以后,sdk会拉起人脸认证页面
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
@end
```

### 3.接口参数说明
| 参数 | 说明 |类型 |长度 | 是否必输 |
|---------|---------|---------|---------|---------|
| userid | 用户唯一的标识 | NSString |30 |必输，必须保证全局唯一|
| nonce | 32位随机字符串| NSString |32 |必输(生成方式参考后台文档) |
| sign    | 合作方后台服务器通过ticket计算出来的签名信息 | NSString |40 |必输(生成方式参考后台文档)|
| appid | 腾讯服务分配的app_id | NSString |腾讯服务分配 |必输|
| apiVersion | 接口版本号 | NSString |默认填1.0.0 |必输，腾讯服务分配的app_id |
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