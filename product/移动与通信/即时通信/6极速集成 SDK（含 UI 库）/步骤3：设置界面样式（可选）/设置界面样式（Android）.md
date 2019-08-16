
## 设置会话列表
会话列表 Layout 由标题区 TitleBarLayout 与列表区 ConversationListLayout 组成，每部分都提供了 UI 样式以及事件注册的接口可供修改。
![会话列表](https://main.qcloudimg.com/raw/8adef6cec9f943958bbcbd0959130ce6.png)

### 修改标题区 TitleBarLayout 样式

标题区除了本身作为 View 所具有的属性功能之外，还包含左、中、右三块区域，如下图所示：
![标题区结构](https://main.qcloudimg.com/raw/832fd209cbc6061b47ff5434740b210c.png)

您可以参考 [ITitleBarLayout](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/base/ITitleBarLayout.html) 进行自定义修改。
例如，在 ConversationLayout 中，隐藏左边的 LeftGroup，设置中间的标题，隐藏右边的文本和图片按钮，代码如下：

```java
// 获取 TitleBarLayout
TitleBarLayout titleBarLayout = mConversationLayout.findViewById(R.id.conversation_title);
// 设置标题
titleBarLayout.setTitle(getResources().getString(R.string.conversation_title), TitleBarLayout.POSITION.MIDDLE);
// 隐藏左侧 Group
titleBarLayout.getLeftGroup().setVisibility(View.GONE);
// 设置右侧的菜单图标
titleBarLayout.setRightIcon(R.drawable.conversation_more);
```

效果如下图所示：
![标题区效果](https://main.qcloudimg.com/raw/b4d5c63dac1fa602830574ea4096c89f.png)

另外，您也可以定制点击事件：

```java
// 菜单类
mMenu = new Menu(getActivity(), titleBarLayout, Menu.MENU_TYPE_CONVERSATION);
// 响应菜单按钮的点击事件
titleBarLayout.setOnRightClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        if (mMenu.isShowing()) {
            mMenu.hide();
        } else {
            mMenu.show();
        }
    }
});
```

 
### 修改列表区 ConversationListLayout 样式

列表区的自定义 layout 继承自 RecyclerView，登录后 TUIKit 会根据用户名从 SDK 读取该用户的会话列表。
会话列表提供一些常用功能定制，例如，头像是否圆角、背景、字体大小、点击与长按事件等。示例代码如下：

```java
public static void customizeConversation(final ConversationLayout layout) {
    // 从CoversationLayout获取会话列表
    ConversationListLayout listLayout = layout.getConversationList();
    listLayout.setItemTopTextSize(16); // 设置 item 中 top 文字大小
    listLayout.setItemBottomTextSize(12);// 设置 item 中 bottom 文字大小
    listLayout.setItemDateTextSize(10);// 设置 item 中 timeline 文字大小
    listLayout.enableItemRoundIcon(true);// 设置 item 头像是否显示圆角，默认是方形
    listLayout.disableItemUnreadDot(false);// 设置 item 是否不显示未读红点，默认显示
    // 长按弹出菜单
    listLayout.setOnItemLongClickListener(new ConversationListLayout.OnItemLongClickListener() {
        @Override
        public void OnItemLongClick(View view, int position, ConversationInfo conversationInfo) {
            startPopShow(view, position, conversationInfo);
        }
    });
}
```

更多详细信息请参见 [ConversationLayoutHelper.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/helper/ConversationLayoutHelper.java)。


### 设置头像

IM SDK 不做头像存储，需要集成者有头像图床接口获取头像 URL，这里 TUIKit 通过随机头像接口进行演示，如何设置头像。
首先您需要在个人资料页面中，上传头像图片，调用修改资料接口。

```
HashMap<String, Object> hashMap = new HashMap<>();
// 头像，mIconUrl 就是您上传头像后的 URL，可以参考 Demo 中的随机头像作为示例
if (!TextUtils.isEmpty(mIconUrl)) {
   hashMap.put(TIMUserProfile.TIM_PROFILE_TYPE_KEY_FACEURL, mIconUrl);
}
TIMFriendshipManager.getInstance().modifySelfProfile(hashMap, new TIMCallBack() {
   @Override
   public void onError(int i, String s) {
       DemoLog.e(TAG, "modifySelfProfile err code = " + i + ", desc = " + s);
       ToastUtil.toastShortMessage("Error code = " + i + ", desc = " + s);
   }
   @Override
   public void onSuccess() {
       DemoLog.i(TAG, "modifySelfProfile success");
   }
});
```

会话列表设置头像在 ConversationCommonHolder.java 中进行获取展示：

```
if (!TextUtils.isEmpty(conversation.getIconUrl())) {
   List<String> urllist = new ArrayList<>();
   urllist.add(conversation.getIconUrl());
   conversationIconView.setIconUrls(urllist);
   urllist.clear();
}
```


## 设置聊天窗口
聊天窗口包含标题区 TitleBarLayout，用法与会话列表相同。除此之外，聊天窗口还包含三个区域，从上到下为通知区 NoticeLayout、消息区 MessageLayout 和输入区 InputLayout，如下图所示：
![聊天界面组成](https://main.qcloudimg.com/raw/8b6e650af731fffc4a816fbf54920970.png)
效果如下图所示：
![聊天界面含更多功能](https://main.qcloudimg.com/raw/5953198d2a5249d1b18f218b319cdd2c.png)

```java
/**
 * 获取聊天窗口 Message 区域 Layout
 * @return
 */
NoticeLayout getNoticeLayout();

/**
 * 获取聊天窗口 Notice 区域 Layout
 * @return
 */
MessageLayout getMessageLayout();

/**
 * 获取聊天窗口 Input 区域 Layout
 * @return
 */
InputLayout getInputLayout();
```


### 修改通知区域 NoticeLayout 样式

通知区域由两个 TextView 组成，如下图所示：
![通知区域组成](https://main.qcloudimg.com/raw/1a34baf21414ffe9671a31a7223c6377.png)
效果如下图所示：
![通知效果图](https://main.qcloudimg.com/raw/406ce089eccc51524e559e0a9f69c1f6.png)

```java
// 从 ChatLayout 里获取 NoticeLayout
NoticeLayout noticeLayout = layout.getNoticeLayout();
// 可以使通知区域一致展示
noticeLayout.alwaysShow(true);
// 设置通知主题
noticeLayout.getContent().setText("现在插播一条广告");
// 设置通知提醒文字
noticeLayout.getContentExtra().setText("参看有奖");
// 设置通知的点击事件
noticeLayout.setOnNoticeClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        ToastUtil.toastShortMessage("赏白银五千两");
    }
});
```

### 修改消息区域 MessageLayout 样式

MessageLayout 继承自 RecyclerView ，本文提供自定义修改聊天背景、气泡、文字、是否显示昵称等常见的用法，更多详情请参见 [IMessageProperties](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/chat/interfaces/IMessageProperties.html)。
![消息区域](https://main.qcloudimg.com/raw/063933c9ace8f762695af5a75a70c4b8.png)

#### 修改聊天背景

您可以自定义设置聊天背景。
![更换聊天背景](https://main.qcloudimg.com/raw/fbab3a9bc355b4ba47ee2d864c7a8bf5.png)

```java
// 从ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
////// 设置聊天背景 //////
messageLayout.setBackground(new ColorDrawable(0xB0E2FF00));
```


#### 修改头像相关属性

TUIKit 的界面在显示用户时，会从用户资料中读取头像地址并显示。
![换头像](https://main.qcloudimg.com/raw/16ba2fdf5bd410efc19ad88f056f9022.png)

```
// 聊天界面设置头像和昵称
TIMUserProfile profile = TIMFriendshipManager.getInstance().queryUserProfile(msg.getFromUser());
  if (profile == null) {
      usernameText.setText(msg.getFromUser());
  } else {
      usernameText.setText(!TextUtils.isEmpty(profile.getNickName()) ? profile.getNickName() : msg.getFromUser());
  if (!TextUtils.isEmpty(profile.getFaceUrl()) && !msg.isSelf()) {
      List<String> urllist = new ArrayList<>();
      urllist.add(profile.getFaceUrl());
      leftUserIcon.setIconUrls(urllist);
      urllist.clear();
  }
}
TIMUserProfile selfInfo = TIMFriendshipManager.getInstance().queryUserProfile(TIMManager.getInstance().getLoginUser());
  if (profile != null && msg.isSelf()) {
       if (!TextUtils.isEmpty(selfInfo.getFaceUrl())) {
       List<String> urllist = new ArrayList<>();
       urllist.add(profile.getFaceUrl());
       rightUserIcon.setIconUrls(urllist);
       urllist.clear();
  }
}
```

如果用户没有设置头像会显示默认头像，您可以自定义设置默认头像、头像是否圆角以及头像大小等。

```java
// 从 ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
////// 设置头像 //////
// 设置默认头像，默认与朋友与自己的头像相同
messageLayout.setAvatar(R.drawable.ic_chat_input_file);
// 设置头像圆角，不设置则默认不做圆角处理
messageLayout.setAvatarRadius(50);
// 设置头像大小
messageLayout.setAvatarSize(new int[]{48, 48});
```


#### 修改气泡
左边为对方的气泡，右边为自己的气泡，您可以自定义设置双方的气泡背景。
![换气泡](https://main.qcloudimg.com/raw/670e40297978817012d9cd81524e73e7.png)

```java
// 从 ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
// 设置自己聊天气泡的背景
messageLayout.setRightBubble(context.getResources().getDrawable(R.drawable.chat_opposite_bg));
// 设置朋友聊天气泡的背景
messageLayout.setLeftBubble(context.getResources().getDrawable(R.drawable.chat_self_bg));
```


#### 修改昵称样式
您可以自定义设置昵称的字体大小与颜色等，但双方昵称样式必须保持一致。
![换昵称](https://main.qcloudimg.com/raw/df0ab81eccc1c2f65804c20964b76419.png)

```java
// 从 ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
////// 设置昵称样式（对方与自己的样式保持一致）//////
messageLayout.setNameFontSize(12);
messageLayout.setNameFontColor(0x8B5A2B00);
```


#### 修改聊天内容样式
您可以自定义设置聊天内容的字体大小、双方字体颜色等，但双方字体大小必须保持一致。
![换聊天内容](https://main.qcloudimg.com/raw/6b86269ecef12ba43762d917f596a51c.png)

```java
// 从 ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
// 设置聊天内容字体大小，朋友和自己用一种字体大小
messageLayout.setChatContextFontSize(15);
// 设置自己聊天内容字体颜色
messageLayout.setRightChatContentFontColor(0xA9A9A900);
// 设置朋友聊天内容字体颜色
messageLayout.setLeftChatContentFontColor(0xA020F000);
```


#### 修改聊天时间线样式

您可以自定义设置聊天时间线的背景、字体大小以及字体颜色等。
![换时间线](https://main.qcloudimg.com/raw/278f58e24d1cf05601d789a45b840fc0.png)

```java
// 从 ChatLayout 里获取 MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
// 设置聊天时间线的背景
messageLayout.setChatTimeBubble(new ColorDrawable(0x8B691400));
// 设置聊天时间的字体大小
messageLayout.setChatTimeFontSize(20);
// 设置聊天时间的字体颜色
messageLayout.setChatTimeFontColor(0xEE00EE00);
```


#### 修改聊天的提示信息样式

您可以自定义设置提示信息的背景、字体大小以及字体颜色等。
![换提示消息](https://main.qcloudimg.com/raw/a59d9b24ec12abea73c78996d912976e.png)

```java
// 从ChatLayout里获取MessageLayout
MessageLayout messageLayout = layout.getMessageLayout();
// 设置提示的背景
messageLayout.setTipsMessageBubble(new ColorDrawable(0xA020F000));
// 设置提示的字体大小
messageLayout.setTipsMessageFontSize(20);
// 设置提示的字体颜色
messageLayout.setTipsMessageFontColor(0x7CFC0000);
```


### 设置输入区域 InputLayout
输入区域 InputLayout，包含语音输入、文字输入、表情输入以及更多的"+"输入。
![输入区域](https://main.qcloudimg.com/raw/262f09005c939b5004e437df58112056.png)

#### 隐藏不要的功能

您可以自定义隐藏或展示更多"+"面板的图片、拍照、摄像以及发送文件的功能。

```java
// 从 ChatLayout 里获取 InputLayout
InputLayout inputLayout = layout.getInputLayout();
// 隐藏拍照并发送
inputLayout.disableCaptureAction(true);
// 隐藏发送文件
inputLayout.disableSendFileAction(true);
// 隐藏发送图片
inputLayout.disableSendPhotoAction(true);
// 隐藏摄像并发送
inputLayout.disableVideoRecordAction(true);
```

#### 增加自定义的功能
您可以自定义新增更多"+"面板的动作单元实现相应的功能。
![增加自定义的功能](https://main.qcloudimg.com/raw/727056dd0e975dbaea86927040b385ab.gif)
本文以隐藏发送文件，增加一个动作单元且该动作单元会发送一条消息为例，示例代码如下：

```java
// 从 ChatLayout 里获取 InputLayout
InputLayout inputLayout = layout.getInputLayout();
// 隐藏发送文件
inputLayout.disableSendFileAction(true);
// 定义一个动作单元
InputMoreActionUnit unit = new InputMoreActionUnit();
unit.setIconResId(R.drawable.default_user_icon); // 设置单元的图标
unit.setTitleId(R.string.profile); // 设置单元的文字标题
unit.setOnClickListener(new View.OnClickListener() { // 定义点击事件
    @Override
    public void onClick(View v) {
        ToastUtil.toastShortMessage("自定义的更多功能");
        MessageInfo info = MessageInfoUtil.buildTextMessage("我是谁");
        layout.sendMessage(info, false);
    }
});
// 把定义好的单元增加到更多面板
inputLayout.addAction(unit);
```


#### 替换点击“+”的事件
您可以自定义替换更多"+"面板的各个动作单元的功能。
![替换事件](https://main.qcloudimg.com/raw/5acf471b7a36cd8be511b1b44c0abdbf.gif)

```java
// 从 ChatLayout 里获取 InputLayout
InputLayout inputLayout = layout.getInputLayout();
// 可以用自定义的事件来替换更多功能的入口
inputLayout.replaceMoreInput(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        ToastUtil.toastShortMessage("自定义的更多功能按钮事件");
        MessageInfo info = MessageInfoUtil.buildTextMessage("自定义的消息");
        layout.sendMessage(info, false);
    }
});
```


#### 替换点击“+”弹出的面板
您可以自定义更多"+"面板的样式、各个动作单元以及其对应的功能。

```java
// 从 ChatLayout 里获取 InputLayout
InputLayout inputLayout = layout.getInputLayout();
// 可以用自定义的 fragment 来替换更多功能
inputLayout.replaceMoreInput(new CustomInputFragment());
```

新面板 CustomInputFragment 的实现和普通的 Fragment 没有区别，在 onCreateView 时 inflate 自己的 View ，设置事件即可。本文以添加两个按钮 ，点击时弹出 toast 为例，示例代码如下：

```java
public static class CustomInputFragment extends BaseInputFragment {
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        View baseView = inflater.inflate(R.layout.test_chat_input_custom_fragment, container, false);
        Button btn1 = baseView.findViewById(R.id.test_send_message_btn1);
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ToastUtil.toastShortMessage("发送一条超链接消息");
            }
        });
        Button btn2 = baseView.findViewById(R.id.test_send_message_btn2);
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ToastUtil.toastShortMessage("发送一条视频文字混合消息");
            }
        });
        return baseView;
    }
}
```
效果如下图所示：
![替换面板](https://main.qcloudimg.com/raw/d347f9e12358fb00d0c517e6a7aa44a6.gif)
