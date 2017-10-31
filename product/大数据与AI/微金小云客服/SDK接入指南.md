管理人员登录 [微金小云客服管理系统](https://ics.webank.com) ，在【系统管理】>【App 接入】单击 iOS SDK 接入说明，接入指引如下：
![1](//mc.qcloudimg.com/static/img/bf757b9df4b288e777fbe8e99c224825/image.png)
1. SDK 接入(iOS)，接入前请先确保后台接入正常
1.1 接入配置
WeBankService SDK 最低支持到 iOS7.0，请在构建项目的时候注意。引用资源文件 WBCloudCustomerService.bundle 和 WBCloudCustomerService.framework 到项目。由于 SDK Required 依赖 libspeex.a，libogg.a；Optional 依赖 Photos.framework，libc++.tbd，因此需要在【BuildPhases】>【Link Binary With Libraries】中添加。
![2](//mc.qcloudimg.com/static/img/ed316933bf54032566badb7595255139/image.png)
SDK 依赖 SDWebImage 3.x，请将其源码引入工程中。
SDK 需要使用相机，相册和录音权限，请在 info.plist 中添加 Privacy -Microphone Usage Description，Privacy -Camera Usage Description，Privacy -Photo Library Usage Description
设置语言，在工程中【project】>【info】>【Localization】>【language】中 add 一个简体中文 Chinese(Simplified)
1.2 调用 SDK 接口
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
@"id_no": @"421112121100001201"            证件号,如果没有请传@"" 
@"user_name": @"张三"                       姓名,如果没有请传@"" 
@"phone_num": @"18800000000"               电话号, 如果没有请传@"" 
@"sex":@"1"                                性别：男 1 女 2,如果没有传递@"" 
@"nick_name":@"yournickname"               昵称 
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
* @param appid          合作方使用的APPID,不能为nil 
* @param nonce            每次请求使用的唯一的nonce信息,不能为nil 
* @param version       版本信息,默认使用@"1.0.0",不能为nil 
* @param sign       将nonce签名以后的信息注意,nonce和sign两个信息都必须由合作方后台传递给合作方iOS APP.不能为nil 
* @param userId          每个用户唯一标识,不能为nil 
* @param nickName         用户昵称,不能为nil 
*/ 
-(void)startCustomServcie:(nonnull NSString *)appid nonce:(nonnull NSString *)nonce version:(nonnull NSString *)version sign:(nonnull NSString *)sign userId:(nonnull NSString *)userId; 
@end 
```

具体调用 SDK 的步骤：
1）App 在希望调用 SDK 时候,在该 UIViewController 中实现 delegate 方法：

```
#pragma mark - WBServiceDelegate 
-(UIViewController *)getViewController{ 
return self; 
} 
```

2）然后设置 delegate，设置 UI 风格，设置当前 SDK 运行的模式，测试时候请使用 WBSDKEnvDebug，如果生产上线请设置 WBSDKEnvRelease。

```
[[WBCloudCustomerService sharedInstance] setWeBankSDKEnv:WBCloudCustomServiceEnvDebug]; 
[WBCloudCustomerService sharedInstance].delegate = self; 
```

3）将客户信息通过 delegate 方法传递给 SDK，具体含义见 SDK 注释。

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

4）最后将 SDK 所需要的参数通过 StartService 方法传递给单例，拉起 SDK。

```
[[WBCloudCustomerService sharedInstance] startCustomServcie:@"app的单独的id" nonce:@"xxxx" sign:@"nonce签名信息" userId:@"用户唯一标识"]; 
```

5）在 SDK 服务完成以后，会调用 delegate，并从当前页面退出，具体的回调方法是：

```
-(void)serviceWillpopViewController:(nonnull WBService *)service; 
-(void)serviceDidpopViewController:(nonnull WBService *)service; 
```

单击 Android SDK 接入说明，接入指引如下：
1. SDK 接入（Android），接入前请先确保后台接入正常
1.1 接入配置（Android Studio 版）
云客服 SDK（WeCcsSdk）最低支持到 Android API 14：Android 4.0(ICS)，请在构建项目时注意。
WeCcsSdk 将以 AAR 文件的形式提供。
需要添加下面文档中所示的依赖(将提供的两个 aar 文件加入到 App 工程的'libs'文件夹下面，并且在 **build.gradle** 中添加下面的配置：

```
android{
//...
repositories {
flatDir {
dirs 'libs' //this way we can find the .aar file in libs folder
}
}
}
//添加依赖
dependencies {
//0. appcompat-v7
compile 'com.android.support:appcompat-v7:23.1.1'
//1. 云客服SDK
compile(name: 'webank-sdk-ccs-openPro-release.aar ', ext: 'aar')
//2. WeBank图片选择器
compile(name: 'webank_image_picker-release', ext: 'aar')
// 3. 依赖的第三方jar包
compile 'com.google.code.gson:gson:2.3.1' //网络请求json解析
compile 'com.squareup.okhttp:okhttp:2.4.0' //网络请求
compile 'com.github.bumptech.glide:glide:3.7.0' //for 图片选择器
}
```
混淆配置
将 SDK 中的 webank-ccs-proguard-rules.pro 和 x5_proguard.cfg.pro 拷贝到主工程根目录下，然后通过"-include webank-ccs-proguard-rules.pro" 加入到您的混淆文件中。
2. 接口调用
SDK 代码调用的入口为：com.webank.mbank.ccs.WeCcsSdk 这个类。

```
public class WeCcsSdk {
/**
* 在Application.onCreate()的时候初始化
*/
public void init(Context app);
...
/**
* 需要打开云客服界面时调用此接口，通过Bundle进行参数传递。
*支持的参数见后面的说明
*/
public void launch(Activity ctx, Bundle data) {
// ...
}
}
```

WeCcsSdk.launch() 的第二个参数用来传递数据，可以将参数打包到 data(Bundle) 中，必须传递的参数包括：

```
//这些都是WeCcsSdk的成员常量，作为传递数据的key
KEY_USER_ID = "user_id"; //user id                   
KEY_SIGNATURE = "signature";  //签名信息
KEY_NONCE="nonce";//32位随机字符串
KEY_APP_ID = "app_id"; //APP_ID 
```

其他选填的参数被封装在 com.webank.mbank.ccs.model.User 对象中（它是一个Parcelable 对象），包括 nickName（昵称），cardNo（证件号码），userName（用户名），sex（性别：男1女2），phoneNum（手机号码）等，可以通过KEY_USER_INFO 这个名称放到 bundle 中，这些参数可以不传入。
3. 接入实例

```
# 自定义Application.onCreate()中：
WeCcsSdk.getInstance().init(this);
# 在MainActivity中点击某个按钮的代码逻辑：
Bundle bundle = new Bundle();
bundle.putString(WeCcsSdk.KEY_NONCE, "随机码xxx");
bundle.putString(WeCcsSdk.KEY_USER_ID, "UserIdxxx");
bundle.putString(WeCcsSdk.KEY_SIGNATURE, "签名信息xxx");
bundle.putString(WeCcsSdk.KEY_APP_ID,"app_id");
WeCcsSdk.getInstance().launch(MainActivity.this, bundle);    
```