
常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 预期效果
<img style="width:800px" src="https://qcloudimg.tencent-cloud.cn/raw/f9fca44d78f0793ddc1ae292d8306e5a.jpg"  />

## 集成指南 
### 步骤一：组件登录
```objectivec
#import "TUILogin.h"
// 您可以在程序启动的时候初始化 TUI 组件
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [TUILogin initWithSdkAppID:SDKAppID]; // SDKAppID 可以在 即时通信 IM 控制台中获取
}

// 您可以在用户 UI 点击登录的时候登录 UI 组件
- (void)login:(NSString *)identifier userSig:(NSString *)sig succ:(TSucc)succ fail:(TFail)fail
{
    [TUILogin login:identifier userSig:sig succ:^{
        NSLog(@"-----> 登录成功");
    } fail:^(int code, NSString *msg) {
        NSLog(@"-----> 登录失败");
    }];
}
```

### 步骤二：构建会话列表

会话列表只需要创建 `TUIConversationListController` 对象即可。会话列表会从数据库中读取最近联系人，当用户点击联系人时，`TUIConversationListController` 将该事件回调给上层。

```java
@implementation ConversationController // 您自己的 ViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    // 创建 TUIConversationListController
    TUIConversationListController *conv = [[TUIConversationListController alloc] init];
    conv.delegate = self;
    // 把 TUIConversationListController 添加到自己的 ViewController
    [self addChildViewController:conv];
    [self.view addSubview:conv.view];
}

- (void)conversationListController:(TUIConversationListController *)conversationController didSelectConversation:(TUIConversationCell *)conversation
{
    // 会话列表点击事件，通常是打开聊天界面
}
@end
```


### 步骤三：构建聊天窗口

初始化聊天界面时，上层需要传入当前聊天界面对应的会话信息，示例代码如下：

```java
@implementation ChatViewController // 您自己的 ViewController
- (void)viewDidLoad {
   // 创建会话信息
   TUIChatConversationModel *data = [[TUIChatConversationModel alloc] init];
   data.userID = @"userID";    
   // 创建 TUIC2CChatViewController
   TUIC2CChatViewController *vc = [[TUIC2CChatViewController alloc] init];  
   [vc setConversationData:data];
   // 把 TUIC2CChatViewController 添加到自己的 ViewController
   [self addChildViewController:conv];
   [self.view addSubview:conv.view];
}
@end
```
`TUIC2CChatViewController` 会自动拉取该用户的历史消息并展示出来。



### 步骤四：构建通讯录界面

通讯录界面不需要其它依赖，只需创建对象并显示出来即可。

```java
@implementation ContactController // 您自己的 ViewController
- (void)viewDidLoad {    
   // 创建 TUIContactController
   TUIContactController *vc = [[TUIContactController alloc] init];
   // 把 TUIContactController 添加到自己的 ViewController
   [self addChildViewController:conv];
   [self.view addSubview:conv.view];
}
@end
```

