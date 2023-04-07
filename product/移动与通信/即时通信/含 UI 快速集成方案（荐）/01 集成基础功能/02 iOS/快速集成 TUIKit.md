TUIKit 从 5.7.1435 版本开始支持模块化集成，您可以根据自己的需求集成所需模块。
TUIKit 从 6.9.3557 版本开始新增了全新的简约版 UI 组件，之前版本 UI 组件依旧保留，我们称之为经典版 UI 组件，您可以根据需求自由选择经典版或简约版 UI 组件。

如果您还不了解各个界面库的功能，可以查阅文档 [TUIKit 界面库介绍](https://cloud.tencent.com/document/product/269/37190)。

下文将介绍如何集成 TUIKit 组件。 

## 开发环境要求
- Xcode 10 及以上
- iOS 9.0 及以上

## CocoaPods 集成
1. 安装 CocoaPods。
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```
2. 创建 Podfile 文件。
进入项目所在路径输入以下命令行，之后项目路径下会出现一个 Podfile 文件。
```
pod init
```
3. 根据业务需求在 Podfile 中添加对应的 TUIKit 组件之间相互独立，添加或删除均不影响工程编译。  Podfile 配置示例如下：
<dx-tabs>

::: 经典版
  ```
  # Uncomment the next line to define a global platform for your project
  # ...
  
  # 防止 TUIKit 组件里的 *.xcassets 与您项目里面冲突。
  install! 'cocoapods', :disable_input_output_paths => true
  
  # 请使用您的真实项目名称替换 your_project_name
  target 'your_project_name' do
    # 从 7.1 版本开始，TUIKit 组件依赖动态库，需要开启此设置。如果您不升级到 7.1 及以后，可以保持关闭。
    use_frameworks!
    # 请按需开启 modular headers，开启后 Pod 模块才能使用 @import 导入，简化 Swift 引用 OC 的方式。
    # use_modular_headers!
    
    # 集成聊天功能
    pod 'TUIChat/UI_Classic' 
    # 集成会话功能
    pod 'TUIConversation/UI_Classic'
    # 集成关系链功能
    pod 'TUIContact/UI_Classic'
    # 集成群组功能
    pod 'TUIGroup/UI_Classic' 
    # 集成搜索功能（需要购买旗舰版套餐）
    pod 'TUISearch/UI_Classic' 
    # 集成投票插件，从 7.1 版本开始支持
    pod 'TUIPoll'
    # 集成群接龙插件，从 7.1 版本开始支持
    pod 'TUIGroupNote'
    # 集成离线推送
    pod 'TUIOfflinePush'
    # 集成音视频通话功能
    pod 'TUICallKit'
		
  end
  ```
:::

::: 简约版
  ```
  # Uncomment the next line to define a global platform for your project
  # ...
  
  # 防止 TUIKit 组件里的 *.xcassets 与您项目里面冲突。
  install! 'cocoapods', :disable_input_output_paths => true
  
  # 请使用您的真实项目名称替换 your_project_name
  target 'your_project_name' do
    # TUIKit 组件依赖了静态库，需要屏蔽此设置。
    # use_frameworks!
  
    # 开启 modular headers。请按需开启，开启后 Pod 模块才能使用 @import 导入。
    # use_modular_headers!
    
    # 集成聊天功能
    pod 'TUIChat/UI_Minimalist' 
    # 集成会话功能
    pod 'TUIConversation/UI_Minimalist'
    # 集成关系链功能
    pod 'TUIContact/UI_Minimalist'
    # 集成群组功能
    pod 'TUIGroup/UI_Minimalist' 
    # 集成搜索功能（需要购买旗舰版套餐）
    pod 'TUISearch/UI_Minimalist' 
    # 集成离线推送
    pod 'TUIOfflinePush'
    # 集成音视频通话功能
    pod 'TUICallKit'
		
  end
  ```
:::
</dx-tabs>
> ?
> 1. 如果您直接 `pod 'TUIChat'`，不指定经典版或简约版，默认会集成两套版本 UI 组件。 
> 2. 经典版和简约版 UI 不能混用，集成多个组件时，您必须同时全部选择经典版 UI 或简约版 UI。例如，经典版 TUIChat 组件必须与经典版 TUIConversation、TUIContact、TUIGroup组件搭配使用。同理，简约版 TUIChat 组件必须与简约版 TUIConversation、TUIContact、TUIGroup 组件搭配使用。
> 3. 如果您使用的是 Swift，请开启 use_modular_headers!，并将头文件引用改成 @import 模块名形式引用。
4. 执行以下命令，安装 TUIKit 组件。
```bash
pod install
```
如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。
```bash
pod repo update
```
之后执行以下命令，更新组件库的Pod版本
```bash
pod update
```
  集成全部的 TUIKit 组件后的项目结构：
  <img src="https://qcloudimg.tencent-cloud.cn/raw/42a839342ac69e1d87952a05458df0e4.png" style="zoom:50%;"/> 

## 快速搭建
常用的聊天软件都是由会话列表、聊天窗口、好友列表、音视频通话等几个基本的界面组成，参考下面步骤，您仅需几行代码即可在项目中快速搭建这些 UI 界面。

> ? 关于 TUIKit 组件模块功能：
> 1. 实操教学视频请参见：[极速集成 TUIKit（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56699)。
> 2. 如果想了解更多，您还可以 [下载并运行 TUIKitDemo 源码](https://github.com/TencentCloud/TIMSDK/tree/master/iOS)，内含常见功能示例。


### 步骤1：组件登录
登录组件后才能正常使用组件的功能。用户在 App 上点击登录时，您可以登录 TUIKit 组件。
SDKAppID 需要在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 创建并获取，userSig 需要按规则计算，详细步骤请参考文档 [快速入门](https://cloud.tencent.com/document/product/269/68228#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)。

示例代码如下所示：
```objectivec
#import "TUILogin.h"
 
- (void)loginSDK:(NSString *)userID userSig:(NSString *)sig succ:(TSucc)succ fail:(TFail)fail {
    [TUILogin login:SDKAppID userID:userID userSig:sig succ:^{
        NSLog(@"登录成功");
    } fail:^(int code, NSString *msg) {
        NSLog(@"登录失败");
    }];
}
```

### 步骤2：构建会话列表
会话列表只需要创建 `TUIConversationListController` 对象即可。会话列表会从数据库中读取最近联系人，当用户点击联系人时，`TUIConversationListController` 将事件 `didSelectConversation` 回调给上层。

示例代码如下所示：

<dx-tabs>
::: 经典版
```java
#import "TUIConversationListController.h"

// ConversationController 为您自己的 ViewController
@implementation ConversationController 
- (void)viewDidLoad {
    [super viewDidLoad];
    // TUIConversationListController
    TUIConversationListController *vc = [[TUIConversationListController alloc] init];
    vc.delegate = self;
    // 把 TUIConversationListController 添加到自己的 ViewController
    [self addChildViewController:vc];
    [self.view addSubview:vc.view];
}

- (void)conversationListController:(TUIConversationListController *)conversationController 
            didSelectConversation:(TUIConversationCell *)conversation
{
    // 会话列表点击事件，通常是打开聊天界面
}
@end
```
:::

::: 简约版
```java
#import "TUIConversationListController_Minimalist.h"

// ConversationController 为您自己的 ViewController
@implementation ConversationController
- (void)viewDidLoad {
    [super viewDidLoad];
    // TUIConversationListController_Minimalist
    TUIConversationListController_Minimalist *vc = [[TUIConversationListController_Minimalist alloc] init];
    vc.delegate = self;
    // 把 TUIConversationListController_Minimalist 添加到自己的 ViewController
    [self addChildViewController:vc];
    [self.view addSubview:vc.view];
}

- (void)conversationListController:(TUIConversationListController_Minimalist *)conversationController 
            didSelectConversation:(TUIConversationCell *)conversation
{
    // 会话列表点击事件，通常是打开聊天界面
}
@end
```
:::
</dx-tabs>

### 步骤3：构建聊天窗口
初始化聊天界面时，需要上层传入当前聊天界面对应的会话信息。

示例代码如下所示：
<dx-tabs>
::: 经典版
```java
#import "TUIC2CChatViewController.h"

// ChatViewController 为您自己的 ViewController
@implementation ChatViewController
- (void)viewDidLoad {
  // 创建会话信息
  TUIChatConversationModel *data = [[TUIChatConversationModel alloc] init];
  data.userID = @"userID";    
  // TUIC2CChatViewController
  TUIC2CChatViewController *vc = [[TUIC2CChatViewController alloc] init];  
  [vc setConversationData:data];
  // 把 TUIC2CChatViewController 添加到自己的 ViewController
  [self addChildViewController:vc];
  [self.view addSubview:vc.view];
}
@end
```
>? `TUIC2CChatViewController` 会自动拉取该用户的历史消息并展示出来。
:::

::: 简约版
```java
#import "TUIC2CChatViewController_Minimalist.h"

// ChatViewController 为您自己的 ViewController
@implementation ChatViewController
- (void)viewDidLoad {
  // 创建会话信息
  TUIChatConversationModel *data = [[TUIChatConversationModel alloc] init];
  data.userID = @"userID";    
  // 创建 TUIC2CChatViewController_Minimalist
  TUIC2CChatViewController_Minimalist *vc = [[TUIC2CChatViewController_Minimalist alloc] init];  
  [vc setConversationData:data];
  // 把 TUIC2CChatViewController 添加到自己的 ViewController
  [self addChildViewController:vc];
  [self.view addSubview:vc.view];
}
@end
```
>? `TUIC2CChatViewController_Minimalist` 会自动拉取该用户的历史消息并展示出来。
:::
</dx-tabs>

### 步骤4：构建通讯录界面
通讯录界面不需要其它依赖，只需创建对象并显示出来即可。
<dx-tabs>
::: 经典版
```java
#import "TUIContactController.h"

// ContactController 为您自己的 ViewController
@implementation ContactController
- (void)viewDidLoad {    
  // 创建 TUIContactController
  TUIContactController *vc = [[TUIContactController alloc] init];
  // 把 TUIContactController 添加到自己的 ViewController
  [self addChildViewController:vc];
  [self.view addSubview:vc.view];
}
@end
```

注意，上面代码只能将 `TUIContactController` 初始化并展示出来，其中的点击行为（例如点击好友、添加好友等），TUIKit 会通过 `TUIContactControllerListener` 抛给上层处理：
```java
@protocol TUIContactControllerListener <NSObject>
@optional
- (void)onSelectFriend:(TUICommonContactCell *)cell;
- (void)onAddNewFriend:(TUICommonTableViewCell *)cell;
- (void)onGroupConversation:(TUICommonTableViewCell *)cell;
@end
```
:::

::: 简约版
```java
#import "TUIContactController_Minimalist.h"

// ContactController 为您自己的 ViewController
@implementation ContactController
- (void)viewDidLoad {    
  // 创建 TUIContactController_Minimalist
  TUIContactController_Minimalist *vc = [[TUIContactController_Minimalist alloc] init];
  // 把 TUIContactController_Minimalist 添加到自己的 ViewController
  [self addChildViewController:vc];
  [self.view addSubview:vc.view];
}
@end
```
注意，上面代码只能将 `TUIContactController_Minimalist` 初始化并展示出来，其中的点击行为（例如点击好友、添加好友等），TUIKit 会通过 `TUIContactControllerListener_Minimalist` 抛给上层处理：
```java
@protocol TUIContactControllerListener_Minimalist <NSObject>
@optional
- (void)onSelectFriend:(TUICommonContactCell *)cell;
- (void)onAddNewFriend:(TUICommonTableViewCell *)cell;
- (void)onGroupConversation:(TUICommonTableViewCell *)cell;
@end
```
:::
</dx-tabs>

例如，点击好友后，您可以将好友信息页展示出来：
<dx-tabs>
::: 经典版
```objectivec
#import "TUIFriendProfileController.h"

- (void)onSelectFriend:(TUICommonContactCell *)cell
{
    TUICommonContactCellData *data = cell.contactData;
    // 创建好友资料 vc
    TUIFriendProfileController *vc = [[TUIFriendProfileController alloc] init];
    vc.friendProfile = data.friendProfile;
    // 展示好友资料 vc
    [self.navigationController pushViewController:(UIViewController *)vc animated:YES];
}
```
:::

::: 简约版
```objectivec
#import "TUIFriendProfileController_Minimalist.h"

- (void)onSelectFriend:(TUICommonContactCell *)cell
{
    TUICommonContactCellData *data = cell.contactData;
    // 创建好友资料 vc
    TUIFriendProfileController_Minimalist *vc = [[TUIFriendProfileController_Minimalist alloc] init];
    vc.friendProfile = data.friendProfile;
    // 展示好友资料 vc
    [self.navigationController pushViewController:(UIViewController *)vc animated:YES];
}
```
:::

</dx-tabs>

>? 您可以 [下载 TUIKitDemo 源码](https://github.com/TencentCloud/TIMSDK/tree/master/iOS)，查看更多的通讯录事件实现。

### 步骤5：构建音视频通话功能
TUI 组件支持在聊天界面对用户发起音视频通话，仅需要简单几步就可以快速集成：
<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>视频通话<br></b></th>
    <th style="text-align:center;"><b>语音通话</b><br></th>
  </tr>
  <tr>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/b9f362503d25179db6f75fc91cfd000a.jpg"/></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2f037d7de8270c0edef68c0b829465ec.png"/></td>
  </tr>
</table>

1. 开通音视频服务。
  1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
  2. 在开通腾讯实时音视频服务功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。
  3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击确认，系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。
2. 集成 TUICallKit 组件。
在 podfile 文件中添加以下内容。
```objectivec
// 集成音视频通话组件
pod 'TUICallKit'                  
```
3. 发起和接收视频或语音通话。
<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>消息页发起通话<br></b></th>
    <th style="text-align:center;" ><b>联系人页发起通话<br></b></th>
  </tr>
  <tr>
    <td><img style="width:400px" src="https://qcloudimg.tencent-cloud.cn/raw/b7b6aca5e1f3f3e5d775cfa3316e30f4.png"/></td>
    <td><img style="width:400px" src="https://qcloudimg.tencent-cloud.cn/raw/31fd1d8fb263e953825cf5531a24ffca.png"/></td>
    </tr>
</table>
<ul>
<li>集成 TUICallKit 组件后，聊天界面和联系人资料界面默认会出现 “视频通话” 和 “语音通话” 两个按钮，当用户点击按钮时，TUIKit 会自动展示通话邀请 UI，并给对方发起通话邀请请求。</li>
<li>当用户<strong>在线</strong>收到通话邀请时，TUIKit 会自动展示通话接收 UI，用户可以选择同意或者拒绝通话。</li>
<li>当用户<strong>离线</strong>收到通话邀请时，如需唤起 App 通话，就要使用到离线推送能力，离线推送的实现请参见 <a href = "https://cloud.tencent.com/document/product/269/74284">添加离线推送</a>。</li>
</ul>
4. 添加离线推送。
在使用离线推送之前，您需要开通 [IM 离线推送](https://cloud.tencent.com/document/product/269/75429) 服务。
关于 App 的配置，您可以参考文档：[集成 TUIOfflinePush 跑通离线推送功能](https://cloud.tencent.com/document/product/269/74284)。
>?配置完成后，当单击接收到的**音视频通话离线推送通知**时， TUICallKit 会自动拉起**音视频通话邀请界面**。
5. 附加增值能力
集成 TUIChat 和 TUICallkit 的组件后，在聊天界面发送语音消息时，即可**录制带 AI 降噪和自动增益的语音消息**。该功能需要购买 [音视频通话能力](https://cloud.tencent.com/document/product/1640/79968) 进阶版及以上套餐，仅 IMSDK 7.0 及以上版本支持。当套餐过期后，录制语音消息会切换到系统 API 进行录音。
下面是使用两台华为 P10 同时录制的语音消息对比：
<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>系统录制的语音消息<br></b></th>
    <th style="text-align:center;" ><b>TUICallkit 录制的带 AI 降噪和自动增益的语音消息<br></b></th>
  </tr>
  <tr>
    <td>
      <audio id="audio" controls="" preload="none" >
	<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_system_record.m4a">
      </audio>
    </td>
		
    <td>
      <audio id="audio" controls="" preload="none">
	<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_tuicallkit_record_with_agc_aidenoise.m4a">
      </audio>
    </td>
  </tr>
</table>
  
## 常见问题
#### 提示 "target has transitive dependencies that include statically linked binaries" 如何处理？
如果在 pod 过程中出现该错误，是因为 TUIKit 使用到了第三方静态库，需要在 podfile 中注释掉 `use_frameworks!`。
如果在某种情况下，需要使用 `use_frameworks!`，则请使用 cocoapods 1.9.0 及以上版本进行 `pod install`，并修改为：
```
use_frameworks! :linkage => :static
```
如果您使用的是 swift，请将头文件引用改成 @import 模块名形式引用。

#### TUICallKit 和自己集成的音视频库冲突了？
腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，建议先去掉，然后 pod 集成 `TUICallKit/Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。**如果您使用了 [LiteAV_Enterprise](https://cloud.tencent.com/document/product/647/32689#Enterprise) 音视频库，暂不支持和 TUICallKit 共存。**具体解决方案可以参考文档：[音视频常见问题](https://cloud.tencent.com/document/product/269/72441#.E5.B8.B8.E8.A7.81.E9.97.AE.E9.A2.98)。

#### 通话邀请的超时时间默认是多久？
通话邀请的默认超时时间是 30 秒。

#### 在邀请超时时间内，被邀请者如果离线再上线，能否立即收到邀请？

- 如果是单聊通话邀请，被邀请者离线再上线可以收到通话邀请，TUIKit 内部会自动唤起通话邀请界面。
- 如果是群聊通话邀请，被邀请者离线再上线后会自动拉取最近 30 秒内的邀请，TUIKit 会自动唤起群通话界面。

## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/>
