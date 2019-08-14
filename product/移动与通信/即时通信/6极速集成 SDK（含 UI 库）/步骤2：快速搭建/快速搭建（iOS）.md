
常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 创建会话列表界面

会话列表只需要创建`TUIConversationListController`对象即可。会话列表会从数据库中读取最近联系人，当用户点击联系人时，`TUIConversationListController`将该事件回调给上层。

在任意`layout.xml`中设置布局：
```objectivec
// 创建会话列表
TUIConversationListController *vc = [[TUIConversationListController alloc] init];
vc.delegate = self;
[self.navigationController pushViewController:vc animated:YES];


- (void)conversationListController:(TUIConversationListController *)conversationController didSelectConversation:(TUIConversationCell *)conversation
{
	// 会话列表点击事件，通常是打开聊天界面
}
```


## 打开聊天界面

初始化聊天界面时，上层需要传入当前聊天界面对应的会话信息，即`TIMConversation`。
`TIMConversation`对象通过`ImSDK`底层方法获取。

以创建一个与用户`abc`的 C2C 会话为例，示例代码如下：

```objectivec
TIMConversation *conv = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"abc"];
TUIChatController *vc = [[TUIChatController alloc] initWithConversation:conv];
[self.navigationController pushViewController:vc animated:YES];
```
`TUIChatController`会自动拉取该用户的的历史消息并展示出来。



## 添加通讯录界面

通讯录界面不需要其它依赖，只需创建对象并显示出来即可。

```objectivec
TUIContactController *vc = [[TUIContactController alloc] init];
[self.navigationController pushViewController:vc animated:YES];
```

