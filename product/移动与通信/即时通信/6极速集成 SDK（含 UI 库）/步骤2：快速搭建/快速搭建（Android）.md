
常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 创建会话列表界面

会话列表 ConversationLayout 继承自 LinearLayout，其数据的获取、同步、展示以及交互均已在 TUIKit 内部封装，会话列表 UI 的使用与 Android 的普通 View 一样方便。
![会话列表](https://main.qcloudimg.com/raw/8adef6cec9f943958bbcbd0959130ce6.png)

<ol><li>在任意 layout.xml 中设置布局：

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
// 初始化聊天面板
conversationLayout.initDefault();
```
</li></ol>

## 打开聊天界面
![聊天界面](https://main.qcloudimg.com/raw/2bcadde944cf0d7fcdd9ae3c9466e60d.png)

<ol><li>在任意 layout.xml 中设置布局：

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

</li>
<li>在代码中引用：

<pre>
// 从布局文件中获取聊天面板
ChatLayout chatLayout = findViewById(R.id.chat_layout);
// 单聊面板的默认 UI 和交互初始化
chatLayout.initDefault();
// 传入 ChatInfo 的实例，这个实例必须包含必要的聊天信息，一般从调用方传入
// 构造 mChatInfo 可参考 <a href="https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/menu/StartC2CChatActivity.java">StartC2CChatActivity.java</a> 的方法 startConversation
chatLayout.setChatInfo(mChatInfo);
</pre>
</li></ol>

## 添加通讯录界面
![通讯录](https://main.qcloudimg.com/raw/1fd48a0db51cfa4a9de5853cf538a0ec.png)

<ol><li>在任意 layout.xml 中设置布局：
    
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
// 通讯录面板的默认 UI 和交互初始化
contactLayout.initDefault();
```
</li></ol>
