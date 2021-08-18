
常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。
>?更多实操教学视频请参见：[极速集成 TUIKit（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56699)。

## 创建会话列表界面

会话列表只需要创建 TUIConversationListController 对象即可。会话列表会从数据库中读取最近联系人，当用户点击联系人时，TUIConversationListController 将该事件回调给上层。


```objectivec
// 设置会话监听
[[TUIKitListenerManager sharedInstance] addConversationListControllerListener:self];
// 创建会话列表
TUIConversationListController *vc = [[TUIConversationListController alloc] init];
[self.navigationController pushViewController:vc animated:YES];


- (void)conversationListController:(TUIConversationListController *)conversationController didSelectConversation:(TUIConversationCell *)conversation
{
    // 会话列表点击事件，通常是打开聊天界面
}
```


## 打开聊天界面

初始化聊天界面时，上层需要传入当前聊天界面对应的会话信息，示例代码如下：

```objectivec
TUIConversationCellData *data = [[TUIConversationCellData alloc] init];
data.groupID = @"groupID";  // 如果是群会话，传入对应的群 ID
data.userID = @"userID";    // 如果是单聊会话，传入对方用户 ID
TUIChatController *vc = [[TUIChatController alloc] initWithConversation:data];
[self.navigationController pushViewController:vc animated:YES];
```
TUIChatController 会自动拉取该用户的历史消息并展示出来。



## 添加通讯录界面

通讯录界面不需要其它依赖，只需创建对象并显示出来即可。

```objectivec
TUIContactController *vc = [[TUIContactController alloc] init];
[self.navigationController pushViewController:vc animated:YES];
```

