
常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 创建会话列表界面

![](https://main.qcloudimg.com/raw/06883035478301c21be30a4ab15c4b94.png)

会话列表 ConversationLayout 继承自 LinearLayout，其数据的获取、同步、展示以及交互均已在 TUIKit 内部封装，会话列表 UI 的使用与 Android 的普通 View 一样方便。

<ol><li>在任意`layout.xml`中设置布局：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.tencent.qcloud.tim.uikit.modules.conversation.ConversationLayout
        android:id="@+id/conversation_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```
</li>
<li>在代码中引用：

```java
// 从布局文件中获取会话列表面板
ConversationLayout conversationLayout = findViewById(R.id.conversation_layout);
// 会话列表面板的默认UI和交互初始化
conversationLayout.initDefault();
```
</li></ol>

## 打开聊天界面

![](https://main.qcloudimg.com/raw/7eba88ed5546649c8a66ac702b495e3d.png)

<ol><li>在任意`layout.xml`中设置布局：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.tencent.qcloud.tim.uikit.modules.chat.ChatLayout
        android:id="@+id/chat_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</LinearLayout>
```

然后在代码里面引用

```java
// 从布局文件中获取聊天面板
ChatLayout chatLayout = findViewById(R.id.chat_layout);
// 单聊面板的默认UI和交互初始化
chatLayout.initDefault();
// 传入ChatInfo的实例，这个实例必须包含必要的聊天信息，一般从调用方传入
chatLayout.setChatInfo(mChatInfo);
```


## 添加通讯录界面

![](https://main.qcloudimg.com/raw/366686f4d8f1204ca58c28c27116a1a1.png)

<ol><li>在任意`layout.xml`中设置布局：
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.tencent.qcloud.tim.uikit.modules.contact.ContactLayout
        android:id="@+id/contact_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

</li>
<li>在代码中引用：

```java
// 从布局文件中获取通讯录面板
ContactLayout contactLayout = findViewById(R.id.contact_layout);
// 通讯录面板的默认UI和交互初始化
contactLayout.initDefault();
```
</li></ol>
