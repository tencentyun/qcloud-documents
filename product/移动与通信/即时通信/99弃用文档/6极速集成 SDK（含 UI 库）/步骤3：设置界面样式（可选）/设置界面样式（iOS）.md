本文介绍如何设置样式（iOS）
>?更多实操教学视频请参见：[设置样式（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56989)。

## 修改头像

### 修改默认头像图片

TUIKit 的界面在显示用户时，会从用户资料中读取头像地址并显示。如果用户没有设置头像，则显示默认头像。

您可以自定义默认头像的图片。
```objectivec
TUIConfig *config = [TUIConfig defaultConfig]; 
// 修改默认头像
config.defaultAvatarImage = [UIImage imageNamed:@"Your Image"];
// 修改默认群组头像
config.defaultGroupAvatarImage = [UIImage imageNamed:@"Your Image"];
```


### 修改头像类型

头像类型提供矩形直角头像、圆形头像和圆角头像三种可选类型。

```objectivec
typedef NS_ENUM(NSInteger, TUIKitAvatarType) {
    TAvatarTypeNone,             /*矩形直角头像*/
    TAvatarTypeRounded,          /*圆形头像*/
    TAvatarTypeRadiusCorner,     /*圆角头像*/
};
```

您可以自定义修改修改头像类型，方式与修改默认头像图片类似。示例代码如下：

```objectivec
TUIConfig *config = [TUIConfig defaultConfig]; 
// 修改头像类型为圆角矩形，圆角大小为5
config.avatarType = TAvatarTypeRadiusCorner;
config.avatarCornerRadius = 5.f;
```


## 配置聊天界面

聊天界面 View 的组合方式如下图所示：
![](https://main.qcloudimg.com/raw/391d26b927660d99eec807ec1fe84c3b.png)

### 设置聊天窗口背景
```objectivec
TUIC2CChatViewController *vc = ...; // 获取 C2C 聊天窗口对象
vc.messageController.view.backgroundColor = [UIColor greenColor];
```

### 配置消息

#### 设置气泡图片

气泡 Cell 显示的图片从 TUIBubbleMessageCellData 获取，该对象提供了类方法可以设置图片。

```objectivec
// 设置发送气泡，包括普通状态和选中状态；设置接收的方法类似
[TUIBubbleMessageCellData setOutgoingBubble:[UIImage imageNamed:@"bubble"]];
[TUIBubbleMessageCellData setOutgoingHighlightedBubble:[UIImage imageNamed:@"bubble_highlight"]];
```


#### 设置气泡边距

在 TUIKit 中，文字和声音都会用气泡显示，TUIMessageCellLayout 提供了类方法设置 bubbleInsets。

```objectivec
// 设置发送气泡边距；设置接收的方法类似
[TUIMessageCellLayout outgoingTextMessageLayout].bubbleInsets = UIEdgeInsetsMake(10, 10, 20, 20);
```


#### 修改消息字体和颜色

文字消息的数据来自于 TUITextMessageCellData 类，通过它的接口可以修改文字消息的字体和颜色。

```objectivec
// 设置发送文字消息的字体和颜色；设置接收的方法类似
[TUITextMessageCellData setOutgoingTextFont:[UIFont systemFontOfSize:20]];
[TUITextMessageCellData setOutgoingTextColor:[UIColor redColor]];
```


### 配置头像

头像是所有消息都包含的内容，我们首先要获取对应消息的 layout 实例，然后设置头像的大小和位置，以文本消息为例：

#### 设置头像大小

```objectivec
// 设置发送头像大小；设置接收的方法类似
[TUIMessageCellLayout outgoingTextMessageLayout].avatarSize = CGSizeMake(100, 100);
```


#### 设置头像位置

```objectivec
// 设置发送位置；设置接收的方法类似
[TUIMessageCellLayout outgoingTextMessageLayout].avatarInsets = UIEdgeInsetsMake(10, 10, 20, 20);
```

其他消息类型请获取对应的 layout 实例设置头像的大小和位置。

### 配置昵称字体和颜色

配置昵称字体和颜色与设置头像位置的方法类似，即修改 TUIMessageCellLayout 的相关属性。

```objectivec
// 设置接收消息的昵称字体；设置发送的方法类似，但默认情况下不显示发送方的昵称
[TUIMessageCellData setIncommingNameFont:[UIFont systemFontOfSize:20]];
[TUIMessageCellData setIncommingNameColor:[UIColor redColor]];
```




