本文主要介绍在项目中如何快速集成互动课堂组件。
![](https://main.qcloudimg.com/raw/a27a44948393333f80c8b347bf56b7c8.jpg)
## <span id="jump">调用参数</span>

参数 ID|参数类型|解释|获取方式
:--:|:--:|:--:|:--
company_id|int|机构码：获取机构的信息（机构名称，应用图标等）的唯一标识。|申请 SaaS 服务邮件获取。具体请参见 [开通指南](https://cloud.tencent.com/document/product/680/41461)。
class_id|int|课堂编号：获取课堂信息的唯一标识。|通过云 API 预约课堂获取。具体请参见 [云 API](https://cloud.tencent.com/document/product/680/37540)。
user_id|string|用户帐号。|通过云 API 创建账号获取。具体请参见 [云 API](https://cloud.tencent.com/document/product/680/37540)。
user_token|string|用户签名。|通过云 API 创建账号获取。具体请参见 [云 API](https://cloud.tencent.com/document/product/680/37540)。
user_sig|string|腾讯云签名，登录必要的腾讯云模块用。|1. 如果用户把私钥托管给我们，则不用填。<br>2. 如果没有托管，请使用 IMSDK 私钥自行计算。具体请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。

## 各端接入流程
### 桌面端组件接入流程
业务方通过云 API 对课堂、用户、课件进行管理。互动课堂组件只负责上课环节，是一个纯课中页面。目前组件页面只支持定制组件名称和图标，页面布局后期会通过云 API 方式逐步开放。

####  下载组件
- Windows 平台组件下载：[单击下载](http://dldir1.qq.com/hudongzhibo/Saas/TClass-win.zip)。    
- Mac 平台组件下载：[单击下载](http://dldir1.qq.com/hudongzhibo/Saas/TClass-mac.zip)。

用户组件下载完成后，将对应压缩包解压到自身应用路径中，在对应解压目录中通过系统命令拉起组件。
 1. 命令行拉起
```javascript
//WIN平台 
TClass company_id class_id user_id user_token user_sig
//MAC平台   
open TClass.app --args company_id class_id user_id user_token user_sig
```
参数获取请参考 [调用参数](#jump)。

2. 单击启动进入课堂
桌面端组件实际是一个可执行程序，也支持单击启动的方式。

###  Web 组件接入流程
与 Windows/Mac 桌面端类似，Web 端组件提供完整的上课页面交互和业务能力，是一个可直接打开的网页。

#### 下载组件
Web 平台组件下载：[单击下载](https://tic-res-1259648581.cos.ap-shanghai.myqcloud.com/saas/component/component.zip)。

#### 部署
- 组件代码需要部署到自己的服务器上。
- Web 端组件是一个纯静态的 Web 项目，您可以使用 `nginx/apache/nodejs` 来搭建 web 服务，并将组件代码解压后部署到 web 服务上。
- 由于浏览器对音视频能力的安全限制，正常使用时必须要通过 HTTPS 访问（开发阶段通过 `http://localhost` 可绕过此限制）。

#### 拼接链接进入课堂
- URL 启动。“:”表示是变量，拼接地址时可省略。
```
https://yourdomain.com/component.html#/:class_id/:user_id/:user_sig/:user_token
```
示例如下：
```
https://tedu.qcloudtrtc.com/component.html#/1000713668/zhangsan/encryptusersighere...../usertokenhere.....
如果 IM 私钥已经通过控制台托管过给我们，则后面两个不用填
https://tedu.qcloudtrtc.com/component.html#/1000713668/zhangsan
```
- 参数描述。参数获取请参考 [调用参数](#jump)。

### iOS 端组件接入流程

#### 快速接入
TIC_SaaS_SDK（互动课堂 SaaS 组件）支持 iOS 8 及以上系统，支持 Cocoapods 集成，集成完后还需进行相应的工程配置。

**pod 集成**
在项目 Podfile 文件中加入：
```
pod 'TIC_SaaS_SDK'    
```
安装：
```
pod install
```
如遇到“无法找到 SDK”或“无法安装 SDK 最新版本”问题，尝试运行以下命令更新本地的 CocoaPods 仓库：
```
pod repo update
```
TIC_SaaS_SDK 依赖以下 pod 库，在执行`pod install`命令时会自动安装。如果您的 App 中也用到了这些 pod 库，可以直接删除，用 TIC_SaaS_SDK 依赖安装的即可。
```
pod 'Masonry'
pod 'YYModel'
pod 'TXLiteAVSDK_TRTC'
pod 'TXIMSDK_iOS'
pod 'AFNetworking'
pod 'MJRefresh'
pod 'Bugly'
pod 'MBProgressHUD'
```

#### 工程配置
因为互动课堂组件具备音视频直播互动功能，所以要用到 iPhone 或 iPad 的相机和麦克风，需要在项目的`info.plist`文件中增加`Privacy - Camera Usage Description`和`Privacy - Microphone Usage Description`两项，并设置相应的中文描述。

####  集成验证
在`appdelegate.m`中导入头文件`<TIC_SaaS_SDK/TIC_SaaS_SDK.h>`，该头文件包含了`TIC_SaaS_SDK`中所有公开的头文件，可调用`TICManager`的`getVersion`方法获取版本号。如果集成无误，控制台即可打印出`TICSDK`的版本号。
```objc
#import <TIC_SaaS_SDK/TIC_SaaS_SDK.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSLog(@"%@",[TICManager getVersion]);
    return YES;
}
```


#### 使用详解
- **头文件概览**
SDK 中暴露的公开头文件如下表：
<table>
<tr>
<th>类名</th>
<th>主要功能</th>
</tr>
<tr>
<td>TIC_SaaS_SDK.h</td>
<td>SDK 总头文件类，包含了开发者可能用到的所有头文件，开发者集成时，只需导入该头文件即可。</td>
</tr>
<tr>
<td>TICManager.h</td>
<td>互动课堂管理类，互动课堂 SDK 对外主要接口类，提供了【初始化】、【加入课堂】、【获取版本】等接口。</td>
</tr>
<tr>
<td>TICClassroomViewController.h</td>
<td>课堂主页视图控制器，承载了课堂主页的 UI 和逻辑。</td>
</tr>
</table>

- **使用流程**
使用互动课堂 SaaS 组件只需要两步：**初始化**和**加入课堂**。
 - **初始化**
调用`TICManager`中的 `initWithSdkAppId:callback:`方法，传入腾讯云应用程序标识，进行 SDK 的初始化。
```objc
 /**
   初始化，默认开启 bugly，建议 App 启动时调用
   @param sdkAppId 腾讯云应用程序标识
   @param callback 回调
   */
   - (void)initWithSdkAppId:(int)sdkAppId callback:(void (^)(int code, NSString *desc))callback;
```
互动课堂 SaaS 组件中用到了 [腾讯 bugly](https://bugly.qq.com/v2/) 服务，初始化后默认开启。**如果您的 App 也用到了腾讯 bugly，可调用以下接口，`isOpen`参数传值为`NO`，关闭组件中的 bugly 服务。**
```objc
 /**
   初始化【建议 App 启动时调用】
  @param sdkAppId 腾讯云应用程序标识
  @param isOpen 是否开启 SDK 内 bugly 模块
  @param callback 回调
  @discussion 如用户自己的 App 也用到了 bugly，建议关闭 SDK 内的 bug
  */
   - (void)initWithSdkAppId:(int)sdkAppId openBugly:(BOOL)isOpen callback:(void (^)(int code, NSString *desc))callback;
```
 - **加入课堂**
调用接口如下：
```objc
/**
 加入课堂
 @param config 课堂配置
 @param succ 成功回调
 @param failed 失败回调
 */
(void)joinClassroomWith:(TICClassroomConfig *)config succ:(void (^)(void))succ failed:(void (^)(int code, NSString *errMsg))failed;
```
该接口接入一个课堂配置参数，其原型为`TICClassroomConfig`类。
```objc
/**
 课堂配置类，加入课堂时需传入这些信息
 */
@interface TICClassroomConfig : NSObject
@property (nonatomic, copy) NSString *classID;  // 课堂编号
@property (nonatomic, copy) NSString *userID;   // 账号
@property (nonatomic, copy) NSString *userToken;// 密码
@property (nonatomic, strong) NSNumber *companyID;  // 机构码（腾讯云互动课堂后台为每个注册企业的分配唯一标识码）
@property (nonatomic, copy) NSString *userSig;  // 用户签名（没有在腾讯云互动课堂后台设置 IM 私钥的，必填；设置了 IM 私钥的填 nil）
@end
```
同时，开发者还需要在加入课堂接口的成功回调中唤起课堂主页控制器 `TICClassroomViewController`，示例代码如下：
```objc
// 设置课堂配置信息
TICClassroomConfig *config = [[TICClassroomConfig alloc] init];;
config.classID = classID;
config.userID = userID ;
config.userToken = userToken;
config.companyID = companyID;
config.userSig = userSig;
// 调用加入课堂接口，加入课堂，传入 config 对象
[[TICManager sharedInstance] joinClassroomWith:config succ:^{
    // 加入课堂成功，唤起课堂主页控制器
    TICClassroomViewController *vc = [[TICClassroomViewController alloc] initWithClassId:classID];
    [controller presentViewController:vc animated:YES completion:nil];
} failed:^(int code, NSString * _Nonnull errMsg) {
      // 加入课堂失败
    NSLog(@"加入课堂失败：%d %@", code, errMsg);
}];
```
>!`TICClassroomViewController`要使用指定的初始化方法进行初始化`initWithClassId:`并传入课堂编号。`TICClassroomViewController` 课堂主页控制器只支持横屏展示。
>
成功唤起课堂主页控制器后，即可使用课堂内的业务和功能。

### Android 组件接入流程
#### 开发环境
* Android studio 3.0+
* Android 4.4（API 19）及以上系统

#### 快速集成 SDK
在项目中快速集成 TICSaaS 组件，TICSaaS 组件已发布到 jcenter，您可以通过配置 gradle 自动下载更新。使用 Android Studio 打开需要集成 SDK 的工程，然后通过简单的三个步骤修改`app/build.gradle`文件，即可完成 SDK 集成。
1. 添加 SDK 依赖。在`dependencies`中添加 TICSaaS 以及其它模块的依赖。
```groovy
 dependencies {
    // TIC SaaS 组件
    implementation "com.tencent.ticsaas:core:1.2.0.1"
    // 实时音视频
    implementation "com.tencent.liteav:LiteAVSDK_TRTC:6.8.8003"
    // 即时通信 IM SDK
    implementation "com.tencent.imsdk:imsdk:4.6.51"
    // 腾讯云互动白板
    implementation "com.tencent.teduboard:TEduBoardSdk:2.4.0.292"
}
```
TICSaaS 组件默认引用普通版 TRTC。如果您需要集成专业版 TRTC，首先要把 TICSaaS 组件依赖的 TRTC 剔除掉，然后集成专业版 TRTC。具体可参考以下示例：
```groovy
 dependencies {
    // TIC SaaS 组件
    implementation("com.tencent.ticsaas:core:1.2.0.1") {
        exclude group: 'com.tencent.liteav', module: 'LiteAVSDK_TRTC'
    }
    // 实时音视频
    implementation "com.tencent.liteav:LiteAVSDK_Professional:6.8.8003"
    // 即时通信 IM SDK
    implementation "com.tencent.imsdk:imsdk:4.6.51"
    // 腾讯云互动白板
    implementation "com.tencent.teduboard:TEduBoardSdk:2.4.0.292"
}
```

2. 指定 App 使用架构。在`defaultConfig`中，指定 App 使用的 CPU 架构（目前 TICSaaS 支持`armeabi`和`armeabi-v7a`）。
```groovy
  defaultConfig {
      ndk {
          abiFilters "armeabi", "armeabi-v7a"
      }
  }
```
3. 使用 JDK 1.8 编译。
```groovy
compileOptions {
    sourceCompatibility 1.8
    targetCompatibility 1.8
}
```
4. 同步 SDK。单击【Sync Now】，如果您的网络连接 jcenter 正常，SDK 就会自动下载集成到工程中。

#### 使用方法
1. 在 Application 的 onCreate() 中初始化。
```java
        // 主进程初始化
        if (SessionWrapper.isMainProcess(this)) {
            ClassroomManager.getInstance().init(this);
        }
```
2. 在 onTerminate() 中反初始化。
```java
        // 主进程反初始化
        if (SessionWrapper.isMainProcess(this)) {
            ClassroomManager.getInstance().unInit();
        }
```

#### 申请必要权限（Android 6.0 以上）
Android 6.0 以上系统，拉起组件前，需动态申请麦克风录音、摄像头和写存储器权限。
```java
Manifest.permission.RECORD_AUDIO
Manifest.permission.CAMERA
Manifest.permission.WRITE_EXTERNAL_STORAGE
```

#### 调起 SaaS 组件
只需传递5个参数就可调起 SaaS 组件主页面，分别为机构编号、课堂编号、账号、密码和用户签名。
```java
    private void launchInActivity(int companyID, int classID, String userID, String userToken, String userSig) {
        Intent intent = new Intent(this, InClassActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        Bundle bundle = new Bundle();
        bundle.putInt(Constants.KEY_CLASS_COMPANY_ID, companyID);
        bundle.putInt(Constants.KEY_CLASS_CLASS_ID, classID);
        bundle.putString(Constants.KEY_CLASS_USER_ID, userID);
        bundle.putString(Constants.KEY_CLASS_USER_TOKEN, userToken);
        bundle.putString(Constants.KEY_CLASS_USER_SIG, userSig);

        intent.putExtras(bundle);
        startActivity(intent);
    }
```

#### 全屏显示
为了达到更好的视觉效果，推荐 App 使用全屏模式，例如使用 NoActionBar 类主题。
```xml
    <style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
        <!-- Customize your theme here. -->
        ...
    </style>
```
