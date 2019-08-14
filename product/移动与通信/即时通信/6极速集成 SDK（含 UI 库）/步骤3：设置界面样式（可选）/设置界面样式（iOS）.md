
## 头像修改

### 默认头像图片

TUIKit 的界面在显示用户时，会从用户资料中读取头像地址并显示。如果用户没有设置头像，则显示默认头像。
- 群头像默认头像：		<img src="https://main.qcloudimg.com/raw/a81959993b0073329b7dd525cb1630a1.png"  style="margin:0;">
- 个人默认头像：<img src="https://main.qcloudimg.com/raw/9ff8053cf27137b523633026c0a9f5e4.png"  style="margin:0;">

您可以自定义默认头像的图片。
```objectivec
TUIKitConfig *config = [TUIKitConfig defaultConfig]; 
// 修改默认头像
config.defaultAvatarImage = [UIImage imageNamed:@"Your Image"];
// 修改默认群组头像
config.defaultGroupAvatarImage = [UIImage imageNamed:@"Your Image"];
```


### 头像类型

头像类型提供矩形直角头像、圆形头像和圆角头像三种可选类型，默认头像为矩形直角类型。

```objectivec
typedef NS_ENUM(NSInteger, TUIKitAvatarType) {
    TAvatarTypeNone,             /*矩形直角头像*/
    TAvatarTypeRounded,          /*圆形头像*/
    TAvatarTypeRadiusCorner,     /*圆角头像*/
};
```

您可以自定义修改修改头像类型，方式与修改默认头像图片类似。示例代码如下：

```objectivec
TUIKitConfig *config = [TUIKitConfig defaultConfig]; 
// 修改头像类型为圆角矩形，圆角大小为5
config.avatarType = TAvatarTypeRadiusCorner;
config.avatarCornerRadius = 5.f;
```


## 聊天界面配置

聊天界面 View 的组合方式如下图所示：
![](https://main.qcloudimg.com/raw/391d26b927660d99eec807ec1fe84c3b.png)

```objectivec
TUIChatController *vc = ...; // 获取聊天窗口对象
vc.messageController.view.backgroundColor = [UIColor greenColor];
```

显示效果下图所示：
![](https://main.qcloudimg.com/raw/9067bc2de0cd428bdfc228b24b9dbcb8.png)


### 消息配置

#### 气泡图片

气泡`Cell`显示的图片从`TUIBubbleMessageCellData`获取，该对象提供了类方法可以设置图片。

```objectivec
// 设置发送气泡，包括普通状态和选中状态；设置接收的方法类似
[TUIBubbleMessageCellData setOutgoingBubble:[UIImage imageNamed:@"bubble"]];
[TUIBubbleMessageCellData setOutgoingHighlightedBubble:[UIImage imageNamed:@"bubble_highlight"]];
```


#### 气泡边距

在 TUIKit 中，文字和声音都会用气泡显示，`TUIMessageCellLayout`提供了类方法设置`bubbleInsets`。

```objectivec
// 设置发送气泡边距；设置接收的方法类似
[TUIMessageCellLayout outgoingTextMessageLayout].bubbleInsets = UIEdgeInsetsMake(10, 10, 20, 20);
```


#### 消息字体和颜色

文字消息的数据来自于`TUITextMessageCellData`类，通过它的接口可以修改文字消息的字体和颜色。

```objectivec
// 设置发送文字消息的字体和颜色；设置接收的方法类似
[TUITextMessageCellData setOutgoingTextFont:[UIFont systemFontOfSize:20]];
[TUITextMessageCellData setOutgoingTextColor:[UIColor redColor]];
```


### 头像配置

头像是所有消息都包含的内容，且属于`layout`配置，通过修改`TUIMessageCellLayout`可改变所有消息的头像样式。

#### 头像大小

```objectivec
// 设置发送头像大小；设置接收的方法类似
[TUIMessageCellLayout outgoingMessageLayout].avatarSize = CGSizeMake(100, 100);
```


#### 头像位置

```objectivec
// 设置发送位置；设置接收的方法类似
[TUIMessageCellLayout outgoingMessageLayout].avatarInsets = UIEdgeInsetsMake(10, 10, 20, 20);
```


### 昵称配置


#### 昵称字体和颜色

昵称位置和头像位置设置是方法类似，即修改`TUIMessageCellLayout`的相关属性。

```objectivec
// 设置接收消息的昵称字体；设置发送的方法类似，但默认情况下不显示发送方的昵称
[TUIMessageCellData setIncommingNameFont:[UIFont systemFontOfSize:20]];
[TUIMessageCellData setOutgoingTextColor:[UIColor redColor]];
```


## 更多菜单配置

单击输入框的"+"按钮，可打开更多面板，默认情况下，更多面板中有4个可选项。通过`TUIChatController`的`moreMenus`属性可以配置更多菜单。
本文以删除文件菜单为例，示例代码如下：

```objectivec
TUIChatController *vc = [[TUIChatController alloc] initWithConversation:conv];
NSMutableArray *array = [NSMutableArray arrayWithArray:vc.moreMenus]; 
[array removeLastObject]; // 删除最后一个菜单
vc.moreMenus = array; // 重新设置属性，立即生效
```
显示效果如下图所示：
![](https://main.qcloudimg.com/raw/19a34761f49c2ffc48e6452f0c1892a6.jpg)

当用户单击菜单中的按钮时，`TUIChatController`会通过回调事件通知上层。
>?用户单击默认菜单时，也会有回调通知，您可以不作处理。


