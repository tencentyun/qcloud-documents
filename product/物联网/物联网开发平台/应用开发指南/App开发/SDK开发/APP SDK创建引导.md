## APP SDK创建引导

**开发前准备**

- 请获取在 [物联网开发平台](https://cloud.tencent.com/product/iotexplorer) 创建应用时生成的 **APP Key**。<u>***App Key 和 App Secret 用于访问应用端 API 时生成签名串，参见[应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773)。签名算法务必在服务端实现，腾讯连连 App 开源版的使用方式仅为演示，请勿将 App Key 和 App Secret 保存在客户端，避免泄露***</u>。
- iOS部分下载所需的 [APP SDK](https://github.com/tencentyun/iot-link-ios/tree/master/Source)

- Android SDK [源码下载](https://github.com/tencentyun/iot-link-android/tree/master/sdk)

  

**iOS安装环境**

- 安装工具 [Xcode开发工具](https://apps.apple.com/cn/app/xcode/id497799835?mt=12)

- 集成SDK方式

  - pod方式集成

    `pod TIoTLinkKit`

  - Framework方式集成

    `打开工程，将下载的Framework拖动到工程中，检查TARGETS-> Build Phases-> Link Binary With Libaries 中是否已包含添加的FrameWork`



**Android安装环境**

* 安装 [Android Studio](https://developer.android.google.cn/studio/) 开发工具

* 集成 SDK 方式

  * 依赖 maven 远程构建

    ``` gr
    implementation 'com.tencent.iot.explorer:explorer-link-android:+'
    ```

  * 依赖本地 aar 构建

    下载最新的 **explorer-link-android.aar** 添加至应用模块的 **libs** 目录，修改应用模块的 **build.gradle**，使应用模块自动依赖 libs 目录下后缀为 aar 的 sdk，示例如下

    ```gr
    implementation fileTree(dir: 'libs', include: ['*.aar', '*.jar'])
    ```

    

**使用说明**

1. 倒入配置，初始化SDK 

   ```objective-c
   ###iOS部分：打开 Appdelegate.m 文件，引入SDK头文件 ,并添加SDK配置。###
   
   #import <QCFoundation/TIoTCoreFoundation.h>
   - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
       // Override point for customization after application launch.
       
       [[TIoTCoreServices shared] setAppKey:@"您的Key"];
       [TIoTCoreServices shared].logEnable = YES;
       
       self.window.rootViewController = [[UINavigationController alloc]initWithRootViewController:[UIViewController new]];
       }
       
       return YES;
   } 
   
   
   ###Android部分：选择sdkdemo/src/main/java/com/tencent/iot/explorer/link/core/demo/App.java，配置 App key###
   
   class App : Application() {
   
       companion object {
           val data = AppData.instance
       }
   
       private val APP_KEY = "物联网平台申请的 App key"
   
       override fun onCreate() {
           super.onCreate()
           L.isLog = true
           //需要打印日志时要在IoTAuth.init(APP_KEY)之前调用
           // 否则看不到"The SDK initialized successfully"的日志
           IoTAuth.openLog(true)
           IoTAuth.init(APP_KEY)
           IoTAuth.addLoginExpiredListener(object : LoginExpiredListener {
               override fun expired(user: User) {
                   L.d("用户登录过期")
               }
           })
       }
   
       override fun onTerminate() {
           IoTAuth.destroy()
           super.onTerminate()
       }
   }
   ```

2. APP SDK 功能划分说明

   | iOS对应模块    | 实现相关功能                                |
   | -------------- | ------------------------------------------- |
   | QCDeviceCenter | 配网模块                                    |
   | QCAPISets      | 设备控制、消息相关、家庭管理、账户管理等api |
   | QCFoundation   | 工具类                                      |

   

   | Android子模块 | 实现相关功能                                |
   | ------------- | ------------------------------------------- |
   | link          | 配网模块                                    |
   | auth          | 设备控制、消息相关、家庭管理、账户管理等api |
   | utils         | 工具类                                      |
   | log           | 日志模块                                    |

   

3. 账户相关接口，包含手机号、邮箱注册，登录登出，密码操作，用户信息操作。此处仅为Demo演示功能，***<u>强烈推荐遵从官方建议自建账户后台服务后，由自建服务接入物联网平台服务，保证 AppSecret 不被泄露</u>***。账户详细接口请参考 [官方文档](https://cloud.tencent.com/document/product/1081/40774) 或者 APP SDK 文件[iOS文件 （TIoTCoreAccountSet.h）](https://github.com/tencentyun/iot-link-ios/blob/master/Source/LinkSDK/QCAPISets/Public/TIoTCoreAccountSet.h)/[Android文件（ IoTAuth.kt）](https://github.com/tencentyun/iot-link-android/blob/master/sdk/src/main/java/com/tencent/iot/explorer/link/core/auth/IoTAuth.kt)

   
   
4. 详细功能请参考 [APP SDK接入指南](https://github.com/tencentyun/iot-link-ios/blob/master/doc/SDK开发/APP%20SDK接入指南.md)