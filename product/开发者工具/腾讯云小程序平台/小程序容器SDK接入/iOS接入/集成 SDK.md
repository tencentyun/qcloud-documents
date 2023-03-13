## 前置条件

#### 环境要求
- iOS >= 9.0

- Xcode >= 10.0


#### 组件依赖
- tars

- MQQTcc

- MQQComponents

- TMFSSL

- TMFShark

- TMFProfile

- SSZipArchive

- PromiseObjC

- MJRefresh

- Masonry

- SocketRocket


## 集成方式

TMFMiniAppSDK 的集成方式有以下2种，可选择其一进行集成：
- CocoaPods 集成 SDK

- 手动集成 SDK


### CocoaPods 集成 SDK
1. 在您项目中的 Podfile 文件里添加tmf源及小程序依赖模块：

   ``` html
   #TMF Pods 仓库
   source 'https://e.coding.net/tmf-work/tmf/tmf-repo.git'
   
   target 'YourTarget' do
        # ――― Applet -----―――――――――――――――――――――――――――――――――――――――――――――――――――――--- #
        pod 'TMFMiniAppSDK'
        pod 'TMFMiniAppExtScanCode'
        pod 'TMFMiniAppExtMedia'
   
   end
   ```

   其中，`YourTarget `为您的项目需要引入 `TMFApplet `的 target 的名字。

2. Terminal cd 到 Podfile 文件所在目录，并执行 pod install 进行组件安装。

   ``` html
   $ pod install
   ```   

   > **说明：**
   > 

   > 如果报 `Couldn't determine repo type for URL: 'https: //e.coding.net/tmf-work/tmf/tmf-repo.git':`错误，则需要在执行`pod install`前执行 `pod repo add specs https://e.coding.net/tmf-work/tmf/tmf-repo.git`
   > 


### 手动集成 SDK
1. **添加 SDK**


   将 `TMFApplet `组件的目录添加到您项目的 Xcode Project 中的合适位置，并选择合适的 target。


   您可以把组件的目录从 Finder 直接拖动到 Xcode Project 中，以进行快捷添加。![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/55a01d4ab8f211eda534525400c56988.png?q-sign-algorithm=sha1&q-ak=AKIDkErxCt46-YIJDXw0E97WqR_RVeLQIFdulLz4M-OEVUMfB4ZAtvkz-JTL497HH6a7&q-sign-time=1678688906;1678692506&q-key-time=1678688906;1678692506&q-header-list=&q-url-param-list=&q-signature=dc87e37c2d8d8b87b1b5af6df9482044fbeb2613&x-cos-security-token=5qJ7cubgkNU53ncrOzOtkv478OD7pUja934728aa9fae183b89b1674ec8c1e7bfY51bK3q3b9-GLry9lxRQZoFMohHvaE-kNNc6XaH9UNswPeDPvshXlaNcHn0VREB5qKZ6ukE5EC5EbwomKHKIpH0o3gHxnELVBDniusrvzwoaN0rh5lEryaV4GK7kyo5yM8dF8uZaNxKjf76-ldDNzMh8kKv4Dg4ucwZ5W_jixve5FTArXi8EPOd6jgoNrB1-QaMV40tzjuw2yZAbpzpG0KHSNlY-qPuwPq2OnjqNRxN3PgEywAxjFDVAqWEwqAhKHvtlHcXFckvaM1urpJAFvZ5w4GWfLX0s8DvP_gGf4Bzy0mBUQq9drbhKCHMYgrbIl57Xpc6Hr5bIFln1VsHMZAxP-c2ig4RSmNpqani3_WCuhJqbj1qKynM6_2prJkpP)

2. **添加依赖的 SDK**


   把 TMFApplet 依赖的所有组件添加到项目中，依赖的组件列表，请参见前置条件中的 [组件依赖](https://write.woa.com/document/88668420206325760)。

3. **添加依赖的系统库**


   把 TMFApplet 依赖的系统库添加到项目中，在 Xcode 中打开 project 设置页，选中相关的 target，单击 **General**，在“Linked Frameworks and Libraries”中进行添加。


#### 系统库依赖
- Foundation.framework

- UIKit.framework

- CoreGraphics.framework

- Security.framework

- libbz2.1.0.tdb

- libz.tdb


#### project 设置

添加 TMFApplet 后，需要进行相关的 Project 设置。在 Xcode 中打开 Project 设置页，选中相关的 target，进行以下设置：

选择 **Build Settings **> **Linking **> **Other Linker Flags**，增加：`-ObjC`。

### Demo 获取

[Demo 获取地址](https://e.coding.net/tmf-work/tmf-demo/tmf-ios-applet-demo.git)。

按以上步骤获取配置文件，替换后运行，项目 BundleId 需与运营平台设置的 BundleId 保持一致。