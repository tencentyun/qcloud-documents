## 1. 快速集成

`TICSDK`支持 iOS8+ 系统，集成方式分为 Cocoapods 集成（推荐）和手动集成，集成完之后还需进行相应的工程配置。

#### Cocoapods 集成（推荐）

在 Podfile 文件中加入：

```
pod 'TICSDK'    
```

安装：

```
pod install // 由于SDK源文件较大，这步可能需要等待几分钟
```
  
如果无法安装 SDK 最新版本，运行以下命令更新本地的 CocoaPods 仓库列表。

```
pod repo update
```
#### 手动集成
[下载 TICSDK](http://dldir1.qq.com/hudongzhibo/TICSDK/iOS/TICSDK.zip) ，将其拖进工程中，并添加以下依赖库：

|需添加依赖库|
|---|
|Accelerate.framework|
|AssetsLibrary.framework|
|AVFoundation.framework|
|CoreGraphics.framework|
|CoreMedia.framework|
|CoreTelephony.framework|
|CoreVideo.framework|
|ImageIO.framework|
|JavaScriptCore.framework|
|OpenAL.framework|
|OpenGLES.framework|
|QuartzCore.framework|
|SystemConfiguration.framework|
|VideoToolbox.framework|
|libbz2.tbd|
|libc++.tbd|
|libiconv.tbd|
|libicucore.tbd|
|libprotobuf.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libstdc++.6.tbd|
|libstdc++.tbd|
|libz.tbd|
|libstdc++.6.0.9.tbd|

#### 工程配置
为了工程能够正常编译，需要修改以下工程配置：

* 在`Build Settings` > `Other Linker Flags`里添加选项 `-ObjC`。

* 在`Build Settings` 中将 `Allow Non-modular includes in Framework Modules`设置为`YES`。

* 在`Build Settings` 中将 `Enable Bitcode`设置为`NO`。

* 由于要用到手机的相机和麦克风，所以别忘了在项目的`info.plist`文件中增加`Privacy - Camera Usage Description`和`Privacy - Microphone Usage Description`两项。

* 由于腾讯云对象存储使用的是 HTTP 协议。为了确保在 iOS 系统上可以运行，您需要开启允许通过 HTTP 传输。
您可以通过以下两种方式开启允许通过 HTTP 传输：

    - 手动设置

    在项目的`info.plist`文件中增加以下配置：
    
    ![](https://main.qcloudimg.com/raw/0204a82988bb42696b7bcbe1d47e5c8c.png)
    
    - 代码设置

    在项目的`info.plist`文件中增加以下代码：
    
    ```xml
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSExceptionDomains</key>
        <dict>
            <key>myqcloud.com</key>
            <dict>
                <key>NSIncludesSubdomains</key>
                <true/>
                <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
                <true/>
            </dict>
        </dict>
    </dict>
    ```

#### 集成验证
在`appdelegate.m`中导入头文件`<TICSDK/TICSDK.h>`，该头文件包含了`TICSDK`中所有公开的头文件，调用`getVersion`方法获取版本号：

```objc
#import <TICSDK/TICSDK.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSLog(@"%@",[TICSDK getVersion]);
    return YES;
}
```
 如果集成没问题，控制台就能打印出`TICSDK`的版本号。
 
## 2. 使用详解
集成成功之后，就可以进一步了解 TICSDK 的使用方法了，为了方便开发者的集成使用，我们开发了一个面向开发者的 Demo，开发者可以参照该 Demo 使用TICSDK，[单击下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/iOS/TICSDK_Demo.zip)。

> 开发者 Demo 的主要主要为向开发者展示 TICSDK 的基本使用方法，所以简化了很多不必要的 UI 代码，使开发者更加专注于了解 TICSDK 的使用方法。

### 2.1 头文件概览

先总体说明下 SDK 中暴露的公开头文件的主要功能：

类名 | 主要功能
--------- | ---------
TICSDK.h | 整个 SDK 的入口类，提供 SDK【初始化】以及【获取版本号】的方法。
TICManager.h | 互动课堂管理类，互动课堂SDK对外主要接口类，提供了【添加白板】、【登录/登出SDK】、【创建/加入/销毁课堂】、【音视频操作】、【IM操作】等接口。
TICClassroomOption.h | 加入课堂时的课堂配置类，主要用来配置加入课堂时的角色（学生 or 老师）、是否自动开启摄像头，麦克风等，另外课堂配置对象还带有两个可选的代理对象，一个是复制监听课堂内部事件，另一个则负责监听课堂内的 IM 消息。
TICFileManager.h | 文件管理类，内部封装了腾讯云对象云存储 COSSDK，负责文件（PPT、wrod、Excel、pdf、图片等）的上传、下载、在线转码预览等（移动端目前只支持上传和下载）。

> **注意：**
> 由于在线课堂场景下老师主要在PC端进行操作，所以移动端 TICSDK 暂时不提供文档管理相关功能。

### 2.2 使用流程

TICSDK 使用的一般流程如下：

<img src="https://main.qcloudimg.com/raw/ad9baefa8be1c7da8d82e98508bda4a0.png" width = 60% height = 60% alt="使用流程" align=center />


<!--```flow
st=>start: 1. 初始化【initSDK:accountType:】
op0=>operation: 2. 配置COS云存储（可选）【configCOS:】
op1=>operation: 3. 登录【loginWithUid:userSig:】
op2=>operation: 4. 创建课堂【createClassroomWithRoomID:】
op3=>operation: 5. 加入课堂（设置课堂事件代理和 IM 消息代理）【joinClassroom:option:】
op4=>subroutine: 6.1 创建并添加白板，进行白板相关操作【addBoardView:】
op5=>subroutine: 6.2 音视频相关操作
op6=>subroutine: 6.3 IM 相关操作
op7=>operation: 7. 退出课堂【quitClassroomSucc:】
e=>end: 8. 登出【logout:】


st->op0->op1->op2->op3->op4->op5->op6->op7->e

```-->
 
> **注意：**
> 步骤 2 为可选步骤，如果您的 App 中需要上传课件，图片等功能，则需要配置 COS 云存储；
> 步骤 4 为老师端特有步骤，学生在得知课堂 ID 之后，可直接加入课堂；
> 步骤 6.1、6.2、6.3 代表课堂内操作，顺序不固定。


### 2.3 初始化 SDK
要使用`TICSDK`，首先得进行初始化，初始化方法位于`TICSDK`单例类中，先导入头文件`<TICSDK/TICSDK.h>`该头文件包含了 TICSDK 中所有公开的头文件，所以只需导入这一个文件。

```objc
> TICSDK.h (该行表示方法所处文件名，下同)

// 导入头文件
#import <TICSDK/TICSDK.h>

/**
@brief 初始化SDK

@param SDKAppID    腾讯云控制台注册的应用ID
@param accountType 腾讯云控制台注册的应用的账号类型
@return 初始化结果，0代表成功，其他代表失败(返回错误码 8021，表示参数无效)
*/
- (int)initSDK:(NSString *)SDKAppID accountType:(NSString *)accountType;

```
初始化方法很简单，但是开发者在初始化之前必须保证已经在 [腾讯云后台](https://console.cloud.tencent.com/rav) 注册成功，并创建了应用，这样才能拿到腾讯云后台分配的 SDKAppID 和 accountType。

### 2.4 COS配置及文档上传下载
COS 为 [腾讯云对象存储](https://cloud.tencent.com/document/product/436/6225)，如果您的 App 中需要用到上传图片、文档到白板上展示的功能，则需要用到COS，TICSDK 内部会将调用 SDK 接口上传的图片，文件上传到 COS 的存储桶中。

开发者可以使用我们维护的公共账号（每个客户对应一个存储桶，推荐），也可以自己申请配置COS账号并自行维护。

具体接口如下（COS文档相关操作封装于TXBoardSDK的TXFileManager类中）：

```objc
> TXBoardSDK/TXFileManager.h

/**
 @brief 初始化COS（使用COS上传文件前必须先初始化）

 @param sdkAppID 腾讯云控制台注册的应用ID
 @param config COS配置对象（传nil，表示使用腾讯云的公共账号）
 @see TXCosConfig
 @return 0 配置成功，否则配置失败(返回错误码 8021，表示参数无效)
 */
- (int)initCosWithSDKAppID:(NSString *)sdkAppID config:(TXCosConfig *)config;
```

如选择使用COS公共账号，`config` 参数传入 `nil` 即可。

如使用自己申请的COS账号，则需配置 `config` 参数：

```objc
/**
 COS 配置类，其属性参数都可从腾讯云 COS 控制台获取到
 */
@interface TICCosConfig : NSObject

/// @brief COS服务的appId，用以标识资源
@property (nonatomic, copy) NSString *cosAppID;
/// @brief 存储桶名称
@property (strong, nonatomic) NSString *bucket;
/// @brief 服务地域名称
@property (nonatomic, copy) NSString *region;
/// @brief 开发者拥有的项目身份识别 ID，用以身份认证
@property (nonatomic, copy) NSString *secretID;
/// @brief 开发者拥有的项目身份密钥
@property (nonatomic, copy) NSString *secretKey;

@end
```

文档的上传下载相关接口参见 `TXBoardSDK/TXFileManager.h` 类。

### 2.5 登录/登出
初始化完成之后，因为涉及到 IM 消息的收发，所以必须先登录：

```objc
> TICManager.h

/**
 @brief 登录 SDK
 
 @param uid    用户id
 @param userSig    用户签名（由腾讯云后台生成）
 */
- (void)loginWithUid:(NSString *)uid userSig:(NSString *)userSig succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```
该方法需要传入两个参数，uid 和 userSig，uid 为用户 ID，userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并传给客户端用于登录，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

> **注意：**
> - 开发调试阶段， 开发者可以使用腾讯云实时音视频控制台的开发辅助工具来生成临时的uid和userSig用于开发测试
> - 如果此用户在其他终端被踢，登录将会失败，返回错误码（ERR_IMSDK_KICKED_BY_OTHERS：6208）。为了保证用户体验，建议开发者进行登录错误码 ERR_IMSDK_KICKED_BY_OTHERS 的判断，在收到被踢错误码时，提示用户是否重新登录。
> - 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，login 将会返回 70001 错误码，开发者可根据错误码进行票据更换。
> - 关于以上错误的详细描述，参见 [用户状态变更](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。


登出方法比较简单，如下：

```objc
> TICManager.h

/**
 @brief 登出SDK
 */
- (void)logout:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

### 2.6 课堂管理

* 创建课堂

登录成功之后，就可以创建或者加入课堂了，创建课堂接口如下，创建课堂时需要传入一个`roomID`参数（roomID 是一个课堂的唯一标识）：

```objc
> TICManager.h

 /**
 @brief 创建课堂
 
 @param roomID 课堂ID，课堂唯一标识（必须为正整数）
 */
- (void)createClassroomWithRoomID:(int)roomID Succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

创建课堂接口，只是根据传进去的 roomID 创建了一个 IM 群组，并进行了一些准备工作，老师端创建课堂后还需调用`加入课堂`方法加入课堂。

* 加入课堂

```objc
> TICManager.h


/**
 @brief 加入指定roomID的课堂

 @param configOption 加入课堂配置项
 @see TICClassroomOption
 @discussion 注意：TICClassroomOption的 controlRole 参数必填，该参数代表进房之后使用什么规格音视频参数，参数具体值为客户在腾讯云实时音视频控制台画面设定中配置的角色名（例如：默认角色名为user, 可设置controlRole = @"user"）
 */
- (void)joinClassroomWithOption:(TICClassroomOption * (^)(TICClassroomOption *option))configOption succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```
该接口需要传入一个配置 block `configOption`，该 block 接收一个方法内部创建好的`TICClassroomOption`默认配置对象，开发者需在该 block 中修改自定义配置，然后将修改后的 option 返回，`TICClassroomOption`类如下：

```objc
/**
 课堂配置类
 */
@interface TICClassroomOption : ILiveRoomOption
@property (nonatomic, assign) int roomID; // 课堂ID，课堂的唯一标识（必须为正整数）
@property (nonatomic, assign) TICClassroomRole role; // 课堂内角色枚举（老师 or 学生）
@property (nonatomic, weak) id<TICClassroomEventListener> eventListener; // 课堂事件监听对象
@property (nonatomic, weak) id<TICClassroomIMListener> imListener; // IM事件监听对象

@end
```
`roomID`即为课堂的唯一标识；`role`表示加入课堂后的角色身份（老师或学生，一般创建课堂的人为老师，其他人应该以学生身份加入课堂）。

另外该类还有两个代理对象，用来监听课堂内的一些事件，这个我们后面再说。

为了保证课堂内的正常逻辑和事件都能被监听到，进房时`TICClassroomOption`的这些属性都是必填参数，另外还有两个父类的参数必须填写：**controlRole** 和 **privateMapKey**。

* **controlRole**：该参数代表进房之后使用哪些音视频参数，参数具体值为客户在[腾讯云实时音视频控制台](https://console.cloud.tencent.com/rav) -> 画面设定 中配置的角色名（例如：默认角色名为 user, 可设置 controlRole = @"user"）
* **privateMapKey**：该参数相当于一个进入房间的钥匙，进房时必须填写，privateMapKey 需要在开发者的业务后台生成传给客户端，生成方法见 [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey) 。

实例代码如下：

```objc
[[TICManager sharedInstance] joinClassroomWithOption:^TICClassroomOption *(TICClassroomOption *option) {
    option.roomID = #房间号#;
    option.role = kClassroomRoleStudent;
    option.eventListener = #课堂事件监听对象#;
    option.imListener = #课堂消息监听对象#;
    option.controlRole = @“user”;
    option.avOption.privateMapKey = #开发者业务后台生成的privateMapKey#
    return option;
} succ:^{
    NSLog(@"进房成功");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"进房失败：%d %@", errId, errMsg);
}];

```

* 退出课堂

```objc
> TICManager.h

/**
 @brief 退出课堂
 @discussion 在创建该课堂的老师退出课堂后，课堂相关的音视频房间、IM群组将会被销毁
 */
- (void)quitClassroomSucc:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

学生退出课堂时，只是本人退出了课堂，老师调用`退出课堂`方法退出课堂时，该课堂将会被销毁，另外退出课堂成功后，课堂内的资源包括课堂的`roomID`将会被回收，所以开发者应尽量保证在加入另一个课堂前，已经退出了前一个课堂。

### 2.7 白板相关操作

TICSDK 中只有一个关于白板的接口，就是添加一个白板视图对象：

```objc
> TICManager.h

/**
 @brief 添加白板到 TICManager【使用白板必调】
 @discussion 方法内部不会对 TXBoardView 对象进行强引用，只是将boardView的代理设置为 TICManager
 
 @param boardView 用户创建的白板对象
 */
- (void)addBoardView:(TXBoardView *)boardView;
```
该方法只是将传进来的白板视图参数与 TICSDK 进行了绑定（但是不会强引用），将 boardView 的代理对象设置为了 TICManager，并实现了其代理方法，外部无需关心。

开发者使用时，应该创建一个 boardView 对象，并将其添加到 TICManager 中（同时只能添加一个，重复添加以后添加的为准），然后直接调用 TXBoardView 中的接口来操作白板即可，详见 [TXBoardView 白板 SDK 使用手册](/document/product/680/17890)。


### 2.8 IM 相关操作

IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，同样，TICSDK 中也只封装了一些常用接口：

```objc
/**
 @brief 向当前课堂发送群聊文本消息
 
 @param text 文本内容
 */
- (void)sendGroupTextMessage:(NSString *)text succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 向当前课堂发送群聊自定义消息
 
 @param data 自定义data
 */
- (void)sendGroupCustomMessage:(NSData *)data succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 发送C2C（单聊）文本消息
 
 @param identifer 消息接收者
 @param text 发送的文本内容
 */
- (void)sendC2CTextMessage:(NSString *)identifer text:(NSString *)text succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 发送C2C（单聊）自定义消息
 
 @param identifer 消息接收者
 @param data 自定义data
 */
- (void)sendC2CCustomMessage:(NSString *)identifer context:(NSData *)data succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```
课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听代理 `id<TICClassroomIMListener> imListener;`，一端发送 IM 消息时，另一端就可以在课堂内 IM 消息回调对应方法中得到通知:

```objc
/**
 课堂内IM消息回调方法
 */
@protocol TICClassroomIMListener <NSObject>

@optional

/**
 @brief 收到群聊文本消息
 
 @param fromId 消息发送方的ID
 @param text 自定义消息内容
 */
- (void)onRecvGroupTextMsg:(NSString *)fromId text:(NSString *)text;


/**
 @brief 收到群聊自定义消息
 
 @param fromId 消息发送方的ID
 @param data 自定义消息内容
 */
- (void)onRecvGroupCustomMsg:(NSString *)fromId context:(NSData *)data;

/**
 @brief 收到C2C单聊文本消息

 @param fromId 消息发送方的ID
 @param text 文本消息内容
 */
- (void)onRecvC2CTextMsg:(NSString *)fromId text:(NSString *)text;

/**
 @brief 收到C2C单聊自定义消息

 @param fromId 消息发送方的ID
 @param data 自定义消息内容
 */
- (void)onRecvC2CCustomMsg:(NSString *)fromId context:(NSData *)data;

@end
```

这 4 个代理方法，分别对应了前面 4 个消息发送的方法，对应类型的消息会在对应类型的代理方法中回调给课堂内所有成员（发消息本人除外），其他端收到后可以将消息展示在界面上。

TICSDK 只是对`IMSDK`一些基础接口进行了封装，如果开发者需要用到`IMSDK`的其他功能，可直接调用`IMSDK`的接口。

### 2.9 音视频相关操作

这部分功能封装于腾讯云实时音视频 SDK `ILiveSDK`，TICSDK 中只封装了一些常用的接口：打开/关闭摄像头、麦克风、扬声器、切换当前相机方向等，如下：

```objc
/**
 @brief 打开/关闭 摄像头
 
 @param cameraPos 摄像头位置枚举
 @param isEnable YES:打开 NO:关闭
 */
- (void)enableCamera:(cameraPos)cameraPos enable:(BOOL)isEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 切换当前相机方向（前置切到后置，后置切到前置）
 */
- (void)switchCamera:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 打开/关闭 麦克风
 
 @param isEnable YES:打开 NO:关闭
 */
- (void)enableMic:(BOOL)isEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;

/**
 @brief 打开/关闭 扬声器
 
 @param isEnable YES:打开 NO:关闭
 */
- (void)enableSpeaker:(BOOL)isEnable succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

课堂内成员在进行打开/关闭摄像头、麦克风操作时，会触发音视频事件，如果在加入课堂前设置了课堂事件监听代理 `id<TICClassroomEventListener> eventListener`，一端进行音视频操作时，另一端就可以在课堂内音视频事件回调中得到通知：

```objc

@protocol TICClassroomEventListener <NSObject>
@optional
/**
 * @brief 课堂内音视频事件回调（注意该回调中的进出房间通知不准确，已废弃进出房间事件通知）
 * @param  event   事件类型
 * @param  users   用户ID数组
 */
- (void)onUserUpdateInfo:(QAVUpdateEvent)event users:(NSArray *)users;
...

@end
```
课堂内的音视频事件都会通过该方法回调到其他端（包括操作者的），event 表示事件类型（开关摄像头等），user 表示触发事件的用户 ID，其他段触发回调之后，可以根据事件类型，进行相应的处理，比如，收到开摄像头事件，就添加一个对应用户的渲染视图，收到关摄像头时间，就移除对应用户的渲染视图（详细用法可以参照 Demo）。

TICSDK 只是对`iLiveSDK`一些基础接口进行了封装，如果开发者需要用到`iLiveSDK`的其他功能，可直接调用`iLiveSDK`的接口。

### 2.10 课堂内其他事件监听

进入课堂的配置对象中的课堂事件监听代理还有一些其他的协议方法：

```objc
/**
 *  @brief 有人加入课堂时的通知回调
 *
 *  @param members 加入成员的identifier（NSString*）列表
 */
-(void)onMemberJoin:(NSArray*)members;

/**
 *  @brief 有人退出课堂时的通知回调
 *
 *  @param members 退出成员的identifier（NSString*）列表
 */
-(void)onMemberQuit:(NSArray*)members;

/**
 * @brief 课堂被解散通知
 * @discussion 老师端主动解散课堂时，老师端不会收到该通知，还在课堂内的学生端会收到；只有后台解散课堂时，老师端才有可能收到
 */
-(void)onClassroomDestroy;
```

以上协议方法分别代表有人加入课堂，有人退出课堂和课堂被解散的回调，开发者可以根据自己的业务需求，对回调事件进行相应的处理，比如：在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可以弹出一个提示框，提示学生课堂已经结束。




