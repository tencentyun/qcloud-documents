## 集成 SDK

本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。如果您使用互动课堂方案，请前往 [互动课堂集成文档](https://github.com/tencentyun/TIC/blob/master/iOS/%E6%8E%A5%E5%85%A5%E6%96%87%E6%A1%A3.md)。

## 开发环境

- Xcode 9.0+
- OS X 10.10+ 的 Mac 真机
- 项目已配置有效的开发者签名

## 集成 TEduBoard SDK

您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。由于 TEduBoard SDK 内部使用 IMSDK 作为内部信令通道，您还需 CocoaPods 或手动添加 IMSDK 依赖项。

### CocoaPods
#### 1. 安装 CocoaPods
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```
#### 2. 创建 Podfile 文件
进入项目所在路径，输入以下命令行之后项目路径下会出现一个 Podfile 文件。
```
pod init
```
#### 3. 编辑 Podfile 文件
编辑 Podfile 文件，支持选择版本号
```
platform :ios, '8.0'

target 'TICDemo' do
  pod 'TEduBoard_iOS'
  pod 'TXIMSDK_iOS'
  pod 'TIWLogger_iOS'
end
```
互动白板默认使用 IMSDK 作为信令通道，如果您有独立的信令通道，无需集成 IMSDK。

#### 4. 更新并安装 SDK
在终端窗口中输入如下命令以更新本地库文件，并安装 TEduBoard SDK：
```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```
pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。


### 手动集成
1. 前往 [版本信息](https://cloud.tencent.com/document/product/1137/43151)，下载 SDK。
2. 前往 [即时通讯官网](https://cloud.tencent.com/document/product/269/36887) 下载 IMSDK。互动白板默认使用 IMSDK 作为信令通道，如果您有独立的信令通道，请跳过此步。
3. 打开您的 Xcode 工程项目，选择要运行的 target ，选中 Build Phases 项。
4. 单击 Link Binary with Libraries 项展开，单击底下的“+”号图标去添加依赖库。
![](https://main.qcloudimg.com/raw/18551cb8b0c0da49f258d133e1e7dd3a.jpg)

## 使用 TEduBoard SDK
#### 1. `#import` SDK
在项目需要使用 SDK API 的文件里，引入具体的头文件
```objc
#import <TEduBoard/TEduBoard.h>
```

#### 2. 创建白板控制器

使用如下代码创建并初始化白板控制器：
```objc
// 创建并初始化白板控制器
//（1）鉴权配置
TEduBoardAuthParam *authParam = [[TEduBoardAuthParam alloc] init];
authParam.sdkAppId = _sdkAppId;
authParam.userId = _userId;
authParam.userSig = _userSig;
//（2）白板默认配置
TEduBoardInitParam *initParam = [[TEduBoardInitParam alloc] init];
_boardController = [[TEduBoardController alloc] initWithAuthParam:authParam roomId:_classId initParam:initParam];
//（3）添加白板事件回调
[_boardController addDelegate:self];
```

其中 `_sdkAppId`、`_userId`、`_userSig`、`_classId`为需要您自己填写的参数。

#### 3. 白板窗口获取及显示
在 `onTEBInit`  或 `onTEBHistroyDataSyncCompleted` 回调方法内，使用如下代码获取并显示白板视图。

```objc
- (void)onTEBHistroyDataSyncCompleted
{
  //（1）获取白板 UIView
  UIView *boardView = [_boardController getBoardRenderView];
  //（2）设置显示位置和大小
  boardView.frame = CGRectMake(0, 0, width, height);
  //（3）添加到父视图中
  [self.view addSubview:boardView];
}
```

>!1. `onTEBInit` 表示白板创建并鉴权完成。<br>2. `onTEBHistroyDataSyncCompleted` 表示历史数据加载完成，此时可调用白板的相关接口。<br>3. SDK 所有回调都在主线程内执行，因此可以在回调里直接执行 UI 操作。

#### 4. 监听白板关键事件
在 `onTEBError`和`onTEBWarning` 回调方法内监听白板事件

- [onTEBError 错误详情](https://cloud.tencent.com/document/product/1137/60711#.E9.94.99.E8.AF.AF.E4.BA.8B.E4.BB.B6)
- [onTEBWarning 警告详情](https://cloud.tencent.com/document/product/1137/60711#.E8.AD.A6.E5.91.8A.E4.BA.8B.E4.BB.B6)

```objc
// 监听白板错误事件
- (void)onTEBError:(TEduBoardErrorCode)code msg:(NSString *)msg
{

}

// 监听白板告警事件
- (void)onTEBWarning:(TEduBoardWarningCode)code msg:(NSString *)msg
{

}
```

#### 5. 白板数据同步
白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 默认使用 IMSDK 作为信令通道，您需要自行实现 IMSDK 的初始化、登录、加入群组操作，确保白板初始化时，IMSDK 已处于所指定的群组内。
步骤1：初始化 IMSDK
```objc
TIMSdkConfig *config = [[TIMSdkConfig alloc] init];
config.sdkAppId = sdkAppId;
[[TIMManager sharedInstance] initSdk:config];
```
如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，请在 `AppDelegate` 的 `application:didFinishLaunchingWithOptions` 方法中初始化 IMSDK，否则请在登录前初始化 IMSDK，在登出后反初始化 IMSDK。
步骤2：登录 IMSDK
```objc
TIMLoginParam *loginParam = [TIMLoginParam new];
loginParam.identifier = userId;
loginParam.userSig = userSig;
loginParam.appidAt3rd = [@(_sdkAppId) stringValue];
__weak typeof(self) ws = self;
[[TIMManager sharedInstance] login:loginParam succ:^{
  // 登录 IMSDK 成功
} fail:^(int code, NSString *msg) {
  // 登录 IMSDK 失败
}];
```
步骤3：加入群组
登录 IMSDK 成功后加入白板所在的群组。
```objc
[[TIMGroupManager sharedInstance] joinGroup:group msg:nil succ:^{
  // 加入 IM 群组成功
  // 此时可以调用白板初始化接口创建白板
} fail:^(int code, NSString *msg) {
  // 加入 IM 群组失败
}];
```

如果 IM 群组不存在，请先创建群组。

```objc
TIMCreateGroupInfo *groupInfo = [[TIMCreateGroupInfo alloc] init];
NSString *roomIdStr = [@(classId) stringValue];
groupInfo.group = roomIdStr;
groupInfo.groupName = roomIdStr;
groupInfo.groupType = @"Public";
groupInfo.setAddOpt = YES;
groupInfo.addOpt = TIM_GROUP_ADD_ANY;
__weak typeof(self) ws = self;
[[TIMGroupManager sharedInstance] createGroup:groupInfo succ:^(NSString *groupId) {
        [ws report:TIC_REPORT_CREATE_GROUP_END];
  // 创建 IM 群组成功
} fail:^(int code, NSString *msg) {
  // 创建 IM 群组失败
}];
```

>!1. 推荐业务后台使用 [IM REST API](https://cloud.tencent.com/document/product/269/1615) 提前创建群组。<br>2. 不同的群组类型，群组功能以及成员数量有所区别，具体请查看 [IM 群组系统](https://cloud.tencent.com/document/product/269/1502)。

#### 6. 销毁白板
调用 `unInit` 方法后，内部将彻底销毁白板并停止计费，请您确保此接口的调用。
```objc
[_boardController unInit];
```
如果您使用 IMSDK 作为信令通道，请根据业务的需要决定是否退出群组、退出登录并反初始化。
步骤1：退出群组
```objc
[[TIMGroupManager sharedInstance] quitGroup:group succ:^{
  // 退出 IM 群组成功
} fail:^(int code, NSString *msg) {
  // 退出 IM 群组失败
}];
```
步骤2：登出 IMSDK
```objc
[[TIMManager sharedInstance] logout:^{
  // 登出 IMSDK 成功
} fail:^(int code, NSString *msg) {
  // 登出 IMSDK 失败
}];
```
步骤3：反初始化 IMSDK
```objc
[[TIMManager sharedInstance] unInit];
```
如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，无需调用此接口。
