管理人员登录 [微金小云客服管理系统](https://ics.webank.com) ，在【系统管理】>【App 接入】单击 iOS SDK 接入说明，接入指引如下：
![1](//mc.qcloudimg.com/static/img/12192f1261eba091584e07ee1cef6f96/image.png)
### SDK 接入(iOS)
接入前请先确保后台接入正常，接入配置为 iOS。
WeBankService SDK 最低支持到 iOS7.0，请在构建项目的时候注意。
引用资源文件 WBCloudCustomerService.bundle 到项目
引用 WBCloudCustomerService.framework 到项目
SDK Required 依赖 libspeex.a，libogg.a；Optional 依赖 Photos.framework，libc++.tbd.需要在【BuildPhases】>【Link Binary With Libraries】中添加。
![2](//mc.qcloudimg.com/static/img/ed316933bf54032566badb7595255139/image.png)
SDK 依赖 SDWebImage 3.x，请将其源码引入工程中。
SDK 需要使用相机，相册和录音权限，请在 info.plist 中添加 Privacy -Microphone Usage Description，Privacy -Camera Usage Description，Privacy -Photo Library Usage Description
设置语言，在工程中【project】>【info】>【Localization】>【language】中 add 一个简体中文 Chinese(Simplified)
### 调用 SDK 接口
SDK 的功能通过 WBService 这个类的方法进行调用，详细接口说明如下：

```
//第三方合作方只需要设置Debug模式或者Release模式,分别对应测试环境和生产环境 
typedef NS_ENUM(NSInteger, WBCloudCustomServiceEnv) { 
WBCloudCustomServiceEnvDebug = 0,//测试环境 
WBCloudCustomServiceEnvRelease, //生产环境 
}; 
@class WBCloudCustomerService; 
@protocol WBCloudCustomServiceDelegate<NSObject> 
@required 
/** 
拉起需要在哪一个页面拉起云客服页面 
*/ 
-(nonnull UIViewController *)getViewController; 
@optional 
-(void)serviceWillpopViewController:(nonnull WBCloudCustomerService *)service; 
-(void)serviceDidpopViewController:(nonnull WBCloudCustomerService *)service; 
/** 
需要传入的是用户信息具体的传递方法直接使用 
@"id_no": @"421112121100001201" 证件号,如果没有请传@"" 
@"user_name": @"张三" 姓名,如果没有请传@"" 
@"phone_num": @"18800000000" 电话号, 如果没有请传@"" 
@"sex":@"1" 性别：男1 女2,如果没有传递@"" 
@"nick_name":@"yournickname" 昵称 
例: 
-(NSDictionary *)getUserInfo{ 
return @{ 
@"id_no":@"421112121100001201", 
@"user_name":@"张三", 
@"phone_num":@"18800000000", 
@"sex":@"1", 
@"nick_name":@"brownfeng"}; 
} 
*/ 
-(nullable NSDictionary *)getUserInfo; 
@end 
@interface WBCloudCustomerService : NSObject 
@property (nonatomic, nullable, weak) id<WBCloudCustomServiceDelegate> delegate; 
/** 
* WBCloudCustomerService全局单例 
*/ 
+(nonnull instancetype)sharedInstance; 
/** 
* 第三方合作方只需要设置Debug模式或者Release模式,分别对应测试环境和生产环境 
* 设置SDK是Release模式还是Debug模式 
* 
* @param env 
*/ 
-(void)setWeBankSDKEnv:(WBCloudCustomServiceEnv)env; 
/** 
* 云客服sdk拉起页面的接口,需要传入以下参数.在调用该方法以前,需要首先通过[WBCloudCustomerService sharedInstance].delegate = xxx;设置代理 
* 
* @param appid 合作方使用的APPID,不能为nil 
* @param nonce 每次请求使用的唯一的nonce信息,不能为nil 
* @param version 版本信息,默认使用@"1.0.0",不能为nil 
* @param sign 将nonce签名以后的信息注意,nonce和sign两个信息都必须由合作方后台传递给合作方iOS APP.不能为nil 
* @param userId 每个用户唯一标识,不能为nil 
* @param nickName 用户昵称,不能为nil 
*/ 
-(void)startCustomServcie:(nonnull NSString *)appid nonce:(nonnull NSString *)nonce version:(nonnull NSString *)version sign:(nonnull NSString *)sign userId:(nonnull NSString *)userId; 
@end 

```
具体调用 SDK 的步骤：
1. App 在希望调用 SDK 的时候，在该 UIViewController 中实现 delegate 方法。
```
#pragma mark - WBServiceDelegate 
-(UIViewController *)getViewController{ 
return self; 
} 
```
2. 设置 delegate、UI 风格、当前 SDK 运行的模式，测试的时候请使用 WBSDKEnvDebug，如果生产上线请设置 WBSDKEnvRelease。
```
[[WBCloudCustomerService sharedInstance] setWeBankSDKEnv:WBCloudCustomServiceEnvDebug]; 
[WBCloudCustomerService sharedInstance].delegate = self;
```

3. 将客户信息通过 delegate 方法传递给 SDK，具体含义见 SDK 注释。
```
-(NSDictionary *)getUserInfo{ 
return @{ 
@"id_no":@"421112121100001201", 
@"user_name":@"张三", 
@"phone_num":@"18800000000", 
@"sex":@"1", 
@"nick_name":@"brownfeng"}; 
} 
```

4. 最后将 SDK 所需要的参数通过 StartService 方法传递给单例，拉起 SDK。
```
[[WBCloudCustomerService sharedInstance] startCustomServcie:@"app的单独的id" nonce:@"xxxx" sign:@"nonce签名信息" userId:@"用户唯一标识"]; 
```
5. 在 SDK 服务完成以后，会调用 delegate，并从当前页面退出，具体的回调方法是：
```
-(void)serviceWillpopViewController:(nonnull WBService *)service; 
-(void)serviceDidpopViewController:(nonnull WBService *)service; 
```
