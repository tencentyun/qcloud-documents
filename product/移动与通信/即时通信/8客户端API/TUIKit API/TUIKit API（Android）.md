## 会话列表界面 ConversationLayout

会话列表窗口 ConversationLayout 由标题区 TitleBarLayout 与列表区 ConversationListLayout 组成，每部分都会提供 UI 样式以及事件注册的接口可供修改。

| API | 描述 |
| --- | --- |
| [getConversationList](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/conversation/interfaces/IConversationLayout.html#getconversationlist) | 获取会话列表 List。 |
| [setConversationTop](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/conversation/interfaces/IConversationLayout.html#setconversationtop) | 置顶会话。 |
| [deleteConversation](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/conversation/interfaces/IConversationLayout.html#deleteconversation) | 删除会话。 |


## 聊天界面 ChatLayout

聊天窗口 ChatLayout 提供消息的展示与发送等功能，界面布局从上到下分为以下四个部分，每个区域都提供多样化的方法以满足定制需求。
- 标题区 TitleBarLayout
- 提醒区 NoticeLayout
- 消息区 MessageLayout
- 输入区 InputLayout

| API | 描述 |
| --- | --- |
| [getInputLayout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#getinputlayout) | 获取聊天窗口 Input 区域 Layout。 |
| [getMessageLayout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#getmessagelayout) | 获取聊天窗口 Message 区域 Layout。 |
| [getNoticeLayout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#getnoticelayout) | 获取聊天窗口 Notice 区域 Layout。 |
| [setChatInfo](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#setchatinfo) | 设置当前的会话 ID，会话面板会依据该 ID 加载会话所需的相关信息，例如消息记录、用户（群）信息等。 |
| [exitChat](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#exitchat) | 退出聊天，释放相关资源（一般在 activity finish 时调用）。 |
| [initDefault](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#initdefault) | 初始化参数。 |
| [loadMessages](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#loadmessages) | 加载聊天消息。 |
| [sendMessage](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IChatLayout.html#sendmessage) | 发送消息。 |


### 通知区域 NoticeLayout

通知区域 NoticeLayout 位置固定，只能显示或隐藏，位置不会随聊天内容的滚动而变化，可以用来展示待处理的群消息或者广播等。该区域分为两部分，可以用来展示内容主题以及辅助主题。可以设置点击事件来响应用户操作。

| API | 描述 |
| --- | --- |
| [getContent](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/INoticeLayout.html#getcontent) | 获取通知的主题信息 View。 |
| [getContentExtra](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/INoticeLayout.html#getcontentextra) | 获取通知的进一步操作 View。 |
| [setOnNoticeClickListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/INoticeLayout.html#setonnoticeclicklistener) | 设置通知的点击事件。 |
| [alwaysShow](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/INoticeLayout.html#alwaysshow) | 设置通知区域是否一直显示。 |


### 消息展示区域 MessageLayout

消息区域 MessageLayout 继承自 RecyclerView，提供消息的展示功能。本类提供了大量的方法以满足定制需求，包括外观设置、点击事件以及自定义消息的展示等。

#### 设置头像
| API | 描述 |
| --- | --- |
| [setAvatar](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setavatar) | 设置默认头像，默认左右双方的头像相同。 |
| [getAvatar](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getavatar) | 获取默认头像。 |
| [setAvatarRadius](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setavatarradius) | 设置头像圆角。 |
| [getAvatarRadius](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getavatarradius) | 获取头像圆角。 |
| [setAvatarSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setavatarsize) | 设置头像大小。 |
| [getAvatarSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getavatarsize) | 获得头像大小。 |


#### 设置昵称样式
| API | 描述 |
| --- | --- |
| [setNameFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setnamefontsize) | 设置昵称文字大小。 |
| [getNameFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getnamefontsize) | 获得昵称文字大小。 |
| [setNameFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setnamefontcolor) | 设置昵称文字颜色。 |
| [getNameFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getnamefontcolor) | 获取昵称文字颜色。 |
| [setLeftNameVisibility](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setleftnamevisibility) | 设置左边昵称是否显示。 |
| [getLeftNameVisibility](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getleftnamevisibility) | 获取左边昵称显示状态。 |
| [setRightNameVisibility](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setrightnamevisibility) | 设置右边昵称是否显示。 |
| [getRightNameVisibility](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getrightnamevisibility) | 获取右边昵称显示状态。 |


#### 设置气泡
| API | 描述 |
| --- | --- |
| [setRightBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setrightbubble) | 设置右边聊天气泡的背景。 |
| [getRightBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getrightbubble) | 获取右边聊天气泡的背景。 |
| [setLeftBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setleftbubble) | 设置左边聊天气泡的背景。 |
| [getLeftBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getleftbubble) | 获取左边聊天气泡的背景。 |


#### 设置聊天内容
| API | 描述 |
| --- | --- |
| [setChatContextFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setchatcontextfontsize) | 设置聊天内容字体大小。 |
| [getChatContextFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getchatcontextfontsize) | 获取聊天内容字体大小。 |
| [setRightChatContentFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setrightchatcontentfontcolor) | 设置右边聊天内容字体颜色。 |
| [getRightChatContentFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getrightchatcontentfontcolor) | 获取右边聊天内容字体颜色。 |
| [getLeftChatContentFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getleftchatcontentfontcolor) | 获取左边聊天内容字体颜色。 |
| [setLeftChatContentFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setleftchatcontentfontcolor) | 设置左边聊天内容字体颜色。 |


#### 设置聊天时间
| API | 描述 |
| --- | --- |
| [setChatTimeBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setchattimebubble) | 设置聊天时间的背景。 |
| [getChatTimeBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getchattimebubble) | 获取聊天时间的背景。 |
| [setChatTimeFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setchattimefontsize) | 设置聊天时间的字体大小。 |
| [getChatTimeFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getchattimefontsize) | 获取聊天时间的文字大小。 |
| [setChatTimeFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#setchattimefontcolor) | 设置聊天时间的字体颜色。 |
| [getChatTimeFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#getchattimefontcolor) | 获取聊天时间的字体颜色。 |


#### 设置聊天的提示信息
| API | 描述 |
| --- | --- |
| [setTipsMessageBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#settipsmessagebubble) | 设置聊天提示信息的背景。 |
| [getTipsMessageBubble](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#gettipsmessagebubble) | 获取聊天提示信息的背景。 |
| [setTipsMessageFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#settipsmessagefontsize) | 设置聊天提示信息的文字大小。 |
| [getTipsMessageFontSize](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#gettipsmessagefontsize) | 获取聊天提示信息的文字大小。 |
| [setTipsMessageFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#settipsmessagefontcolor) | 设置聊天提示信息的文字颜色。 |
| [getTipsMessageFontColor](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html#gettipsmessagefontcolor) | 获取聊天提示信息的文字颜色。 |


#### 设置其他信息
| API | 描述 |
| --- | --- |
| [setAdapter](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#setadapter) | 设置消息列表的适配器 MessageListAdapter。 |
| [setOnItemClickListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#setonitemclicklistener) | 设置消息列表的事件监听器 MessageLayout.OnItemClickListener。 |
| [getOnItemClickListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#getonitemclicklistener) | 获得消息列表的点击事件。 |
| [getPopActions](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#getpopactions) | 获取 PopMenu 的 Action 列表。 |
| [addPopAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#addpopaction) | 给 PopMenu 加入一条自定义 action。 |
| [setOnCustomMessageDrawListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageLayout.html#setoncustommessagedrawlistener) | 设置自定义的消息渲染时的回调，当 TUIKit 内部在刷新自定义消息时会调用这个回调。 |


### 输入区域 InputLayout

输入区域 InputLayout 实现一般消息的输入，包括文本、表情、图片、音频、视频与文件等，配合 MessageLayout.setOnCustomMessageDrawListener 使用可以实现自定义消息的发送与展示。同时，您可以根据实际业务需求隐藏、替换或新增输入区域的功能入口。

| API | 描述 |
| --- | --- |
| [disableAudioInput](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disableaudioinput) | disable 语音输入后，会隐藏按钮。 |
| [disableEmojiInput](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disableemojiinput) | disable 表情输入后，会隐藏按钮。 |
| [disableMoreInput](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disablemoreinput) | disable 更多功能后，会隐藏按钮。 |
| [replaceMoreInput](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#replacemoreinput) | 替换单击“+”弹出的面板。 |
| [replaceMoreInput](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#replacemoreinput2) | 替换单击“+”响应的事件。 |
| [disableSendPhotoAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disablesendphotoaction) | disable 发送图片后，会隐藏更多面板上的按钮。 |
| [disableCaptureAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disablecaptureaction) | disable 拍照后，会隐藏更多面板上的按钮。 |
| [disableVideoRecordAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disablevideorecordaction) | disable 录像后，会隐藏更多面板上的按钮。 |
| [disableSendFileAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#disablesendfileaction) | disable 发送文件后，会隐藏更多面板上的按钮。 |
| [addAction](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IInputLayout.html#addaction) | 增加更多面板上的事件单元。 |


## 标题区 TitleBarLayout

会话列表窗口 ConversationLayout、聊天窗口 ChatLayout 等都自带标题栏。标题栏设计分为左中右三部分，其中，左边和右边都可以为图片 + 文字，中间只能为文字，这些区域返回的都是标准的 Android View，您可以根据实际业务需要对这些 View 进行交互响应处理。

| API | 描述 |
| --- | --- |
| [setLeftIcon](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#setlefticon) | 设置左边标题的图片。 |
| [setRightIcon](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#setrighticon) | 设置右边标题的图片。 |
| [setOnLeftClickListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#setonleftclicklistener) | 设置左边标题的点击事件。 |
| [setOnRightClickListener](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#setonrightclicklistener) | 设置右边标题的点击事件。 |
| [setTitle](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#settitle) | 设置文字标题，根据`position`参数指定文字所在位置。 |
| [getLeftGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getleftgroup) | 返回左边标题区域。 |
| [getRightGroup](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getrightgroup) | 返回右边标题区域。 |
| [getLeftIcon](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getlefticon) | 返回左边标题的图片。 |
| [getRightIcon](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getrighticon) | 返回右边标题的图片。 |
| [getLeftTitle](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getlefttitle) | 返回左边标题的文字。 |
| [getMiddleTitle](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getmiddletitle) | 返回中间标题的文字。 |
| [getRightTitle](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html#getrighttitle) | 返回右边标题的文字。 |



