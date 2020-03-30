## 集成 SDK

本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。

## 开发环境

- Xcode 9.0+
- OS X 10.10+ 的 Mac 真机
- 项目已配置有效的开发者签名

## 集成 TEduBoard SDK

您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。由于TEduBoard SDK 内部使用 TIMSDK 作为内部信令通道，您还需 CocoaPods 或手动添加 TIMSDK 依赖项。

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
platform :macos, '10.10'

target 'TICDemo' do
  pod 'TEduBoard_Mac'
  pod 'TXIMSDK_Mac'
end

```

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

1. 下载 [TEduBoard SDK](https://tic-res-1259648581.cos.ap-shanghai.myqcloud.com/sdk/macOS.zip)。

2. 打开您的 Xcode 工程项目，选择要运行的 target ，选中 Build Phases 项。

3. 单击 Link Binary with Libraries 项展开，单击底下的“+”号图标去添加依赖库。

![](https://main.qcloudimg.com/raw/f2ce73bfbd06cb34c14147475142b539.jpg)

## 使用 TEduBoard SDK

#### 1. `#import` SDK

在项目需要使用 SDK API 的文件里，引入具体的头文件

```objc
#import <TEduBoard_Mac/TEduBoard.h>
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
在 `onTEBInit`  回调方法内，回调方法内，使用如下代码获取并显示白板视图：
```objc
//（1）获取白板 NSView
NSView *boardView = [_boardController getBoardRenderView];
//（2）设置显示位置和大小
boardView.frame = CGRectMake(0, 0, width, height);
//（3）添加到父视图中
[self.view addSubview:boardView];
```

SDK 所有回调都在主线程内执行，因此可以在回调里直接执行 UI 操作。

#### 4. 白板数据同步

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK支持两种不同的数据同步模式。

**使用腾讯云 IMSDK 同步数据**

如果您在使用白板的同时使用了腾讯云 IMSDK，则只需要在初始化白板控制器时进行指定 initParam 参数的 timSync 字段为 true 即可实现数据同步。
```objc
// 使用腾讯的 IM 进行消息传递，前提是您的项目中已经集成 TIM。
// TEduBoardInitParam 的 timSync 的默认值为 YES
TEduBoardInitParam *initParam = [[TEduBoardInitParam alloc] init];
initParam.timSync = YES;
_boardController = [[TEduBoardController alloc] initWithAuthParam:authParam roomId:_classId initParam:initParam];
```

>! 您需要自行实现 IMSDK 的登录、加入群组等操作，确保白板初始化时，IMSDK 已处于所指定的群组内。

**使用自定义的数据通道同步数据**

如果使用自已的通道进行消息传递，则需要按下面步骤进行：

```objc
//（1）将 TEduBoardInitParam 的 timSync 参数初始为 NO
TEduBoardInitParam *initParam = [[TEduBoardInitParam alloc] init];
initParam.timSync = NO;
_boardController = [[TEduBoardController alloc] initWithAuthParam:authParam roomId:_classId initParam:initParam];

//（2）TEduBoard 有数据要同步给其他用户时，将调用 TEduBoardDelegate 接口中的 onTEBSyncData 函数
- (void)onTEBSyncData:(NSString *)data {
//使用自定义的通道，发送 data 数据给其他白板用户。
}

//（3）在收到其他用户的信息时，将消息传递给 TEduBoard.
[_boardController addSyncData:data];
```

>! 实时录制功能在自定义数据通道模式下不可用


