
## 会话列表 TUIConversationListController

会话列表 Controller 用于显示最近会话，同时内部会监听会话变更通知，并根据时间做排序。


| API | 描述 |
| --- | --- |
| [delegate](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIConversationListController.html) | 委托回调，用于外部处理选中事件 |
| [viewModel](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIConversationListController.html) | 控制器的数据源 |

## 聊天界面

聊天界面由聊天控制器和输入控制器两部分组成。

### TUIChatController

TUIChatController 用于组合聊天界面的两大组件，同时对外导出接口，方便对消息做定制化。

| API | 描述 |
| --- | --- |
| [messageController](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | 主聊天 TableView 实现 |
| [inputController](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | 输入控制器 |
| [delegate](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | UI 事件和自定义 Cell 回调 |
| [moreMenus](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | 更多菜单项数据 |
| [sendMessage:](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | 发送自定义消息 |
| [saveDraft](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIChatController.html) | 保存草稿 |

### TUIMessageCell

TUIMessageCell 是每个消息的基础类，通过它可以访问消息的所有 UI 元素。

| API | 描述 |
| --- | --- |
| [avatarView](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 头像 |
| [nameLabel](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 昵称标签 |
| [container](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 消息内容主容器 |
| [indicator](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 加载活动活动指示器 |
| [retryView](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 重发视图 |
| [messageData](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 消息数据源 |
| [delegate](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 消息 UI 事件委托 |
| [fillWithData:](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCell.html) | 更新数据源 |

### TUIMessageCellData

iOS TableView 的特点是滚动时 TableViewCell 会被重用，所有消息数据不保存到 Cell 中，而是在 TUIMessageCellData 中，在显示时内部调用 fillWithData 刷新界面。

| API | 描述 |
| --- | --- |
| [identifier](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 消息发送者 ID |
| [avatarUrl](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 头像链接 |
| [avatarImage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 头像图片 |
| [name](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 昵称 |
| [showName](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 是否显示昵称 |
| [direction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 消息方向，接收消息或发送消息 |
| [status](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 消息状态 |
| [innerMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | IM SDK 使用的消息对象 |
| [nameFont](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 昵称字体 |
| [nameColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 昵称颜色 |
| [cellLayout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 消息布局，控制头像、昵称以及气泡等位置 |
| [contentSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/TUIKit/Classes/TUIMessageCellData.html) | 消息内容大小 |



