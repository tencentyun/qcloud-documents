## 简介
### 腾讯云 TUIKit

TUIKit 是基于腾讯云 IM SDK 的一款 UI 组件库，里面提供了一些通用的 UI 组件，开发者可通过该组件库选取自己所需要的组件快速的搭建一个 IM 应用。
IM 软件都具备一些通用的 UI 界面，如会话列表，聊天界面等。TUIKit 提供了这一类的组件，并提供了灵活的 UI 和交互扩展接口，方便用户做个性化开发。

### IM SDK 与 TUIKit 的结合
腾讯云 IM SDK 提供了 IM 通信所需的各种基础能力，如通信网络，消息收发、存储，好友关系链，用户资料等。 TUIKit 中的组件在实现 UI 功能的同时调用 IM SDK 相应的接口实现了 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或做一些个性化的扩展即可。
下面我们将指导您如何快速的接入和使用 TUIKit。

## 帐号相关的基本概念

这里我们先来了解帐号相关的几个概念。

- **用户标识（userId）**:
userId（用户标识）用于在一个 IM 应用中唯一标识一个用户，即我们通常所说的帐号。这个一般由开发者自己的服务生成，即用户信息的生成（注册）需由开发者实现。

- **用户签名（userSig）**:
userSig（用户签名）是用于对一个用户进行鉴权认证，确认用户是否真实的。即用户在开发者的服务里注册一个帐号后，开发者的服务需要给该帐号配置一个 usersig，后续用户登录 IM 的时候需要带上 usersig 让 IM 服务器进行校验。用户签名生成方法可参考 [生成签名](https://cloud.tencent.com/document/product/647/17275) 文档。

了解了前面的概念后，您可以通过下图了解集成了 IM SDK 应用的注册/登录流程。
![](https://main.qcloudimg.com/raw/5d79dfdd3830476ac767731bb5ad8461.jpg)

首先用户的终端需要向您的服务器注册帐号（userid），您的服务器在进行注册业务处理时，按照用户签名文档中的方法生成一个该用户的 usersig，并返回给客户端。客户端再通过该 userid 和 usersig 到 IM SDK 进行登录操作。
为方便开发者接入开发测试，我们在腾讯云控制台提供了快速生成 usersig 的工具（在这之前您需要先在腾讯云创建自己的 IM 应用，可参考 [云通信 IM 入门](https://cloud.tencent.com/product/im/getting-started)）。登录控制台后选择-【云通信】>【应用列表】（选择您当前在使用的应用）>【应用配置】>【开发辅助工具】，参考上面说明即可生成 usersig。

## 集成 TUIKit

首先开发者需在自身主工程的 build.gradle 文件的依赖配置中添加 TUIKit 的引用及 ABI 架构限定。同时在 <a href="https://github.com/tencentyun/TIMSDK">项目 </a>中 TIMSDK/Android/tuikit/libs/ 目录下，下载最新的 TUIKit 组件。

**集成步骤：**

1. 将下载的 aar 文件拷贝到您工程的 app/libs 目录下。
2. 在 app 的 build.gradle 中加入以下配置：
<pre>
repositories {    
    flatDir {        
        dirs 'libs'   // aar 目录
      }
}
</pre>
3. 在 dependencies 中加入 aar 引用
<pre>
dependencies {
    ...
    implementation(name: 'tuikit-4.3.118', ext: 'aar')  //版本号请替换成线上 <a href="https://github.com/tencentyun/TIMSDK">最新的实际版本号</a>
}
</pre>

TUIKit 会自动加载所需的 IM SDK。

## 初始化 TUIKit

通常情况下 TUIKit 的初始化非常简单，只需调用下面接口初始化默认配置即可。

```java
/**
 * TUIKit 的初始化函数
 *
 * @param context  应用的上下文，一般为对应应用的 ApplicationContext
 * @param sdkAppID 您在腾讯云注册应用时分配的 SDKAppID
 * @param configs  TUIKit 的相关配置项，一般使用默认即可，需特殊配置参考 API 文档
 * @param customFaceGroupConfigs 聊天自定义表情相关配置，可以参考 PojoApplication.java 文件，传 null 表示无聊天自定义表情相关配置
 */
TUIKit.init(context, sdkAppId, BaseUIKitConfigs.getDefaultConfigs(), customFaceGroupConfigs);
```

建议 TUIKit 的初始化在 Application 的 OnCreate 方法中调用（或应用其它初始化相关函数里）。TUIKit 初始化已自行完成 IM SDK 的初始化相关工作。如果您需对 IM SDK 和 TUIKit 的初始化做自定义配置，可以参考 [高级进阶-IM SDK的初始化扩展](#iminit)、[高级进阶-TUIKit的初始化扩展](#configs)。


## 登录

用户首先要完成自己的登录逻辑，在登录成功拿到您服务器派发的 userSig 后。您还需要在客户端代码里调用 IM SDK 的 login，将 userSig 参数传入。

调用 IM SDK 的 login 可参考下面的代码。

```java
    /**
     * 在收到服务器颁发的 userSig 后，调用 IM SDK 的 login 接口
     * userId 用户帐号
     * userSig 您服务器给这个用户账号颁发的 IM SDk 鉴权认证
     */
    private void onRecvUserSig(String userId,String userSig) {
          TUIKit.login(userId, userSig, new IUIKitCallBack() {
            @Override
            public void onSuccess(Object data) {
                /**
                 * IM 登录成功后的回调操作，一般为跳转到应用的主页（这里的主页内容为下面章节的会话列表）
                 */
                Intent intent = new Intent(MyLoginActivity.this, MainActivity.class);
                startActivity(intent);
            }
            @Override
              public void onError(String module, int errCode, String errMsg) {
                Log.e("imlogin fail", errMsg);
            }
        });
    }
}
```


## 会话列表（SessionPanel）

一个聊天的发起可以理解成一个会话，IM SDK 中会话分为两种：
1. **C2C 会话**：表示单聊情况下自己与对方建立的对话，读取消息和发送消息都是通过会话完成。
2. **群会话**：表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。

会话列表用来展示用户的所有会话记录。SessionPanel 是 TUIKit 提供的和 IM SDK 业务关联，且 UI 交互可扩展的会话列表面板。您调用 initDefault() 即可实现 SessionPanel 的通用的交互功能。SessionPanel 内部已与 IM SDK 关联，实现了会话记录的拉取和更新，您可无需关注。
![](http://dldir1.qq.com/hudongzhibo/im/session.jpg)

**使用方法:**

1. 在 Activity 或 Fragment（Demo 示例为创建一个 Fragment，即下面代码的 SessionFragment）的布局文件里引用 SessionPanel。

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
   >

    <com.tencent.qcloud.uikit.business.session.view.SessionPanel
        android:id="@+id/session_panel"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

2. 添加完 SessionPanel 后，需对 SessionPanel 进行初始化操作。

```java
public class SessionFragment extends BaseFragment {

    private View baseView;
    private SessionPanel sessionPanel;
    
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        baseView = inflater.inflate(R.layout.fragment_session, container, false);
        initView();
        return baseView;
    }

    private void initView() {
        // 获取会话列表组件
        sessionPanel = baseView.findViewById(R.id.session_panel);
        // 会话面板初始化默认功能
        sessionPanel.initDefault();
        // 这里设置会话列表单击的跳转逻辑，告诉添加完 SessionPanel 后会话被单击后该如何处理
        sessionPanel.setSessionClick(new SessionClickListener() {
            @Override
            public void onSessionClick(SessionInfo session) {
                //此处为 demo 的实现逻辑，更根据会话类型跳转到相关界面，开发者可根据自己的应用场景灵活实现
                if (session.isGroup()) {
                    //如果是群组，跳转到群聊界面
                    ChatActivity.startGroupChat(getActivity(), session.getPeer());
                } 
                else {
                    //否则跳转到C2C单聊界面
                    ChatActivity.startC2CChat(getActivity(), session.getPeer());
            
                }
            }
        });

    }
}
```

3. SessionPanel 提供了 UI 及交互的扩展功能，可参考 [高级进阶-会话面板 UI 扩展](#sessionPanelExtra)。



## 聊天面板 

在会话列表里单击会话条目后应跳转到相应的聊天界面。聊天界面是一个非常复杂的交互，所以 TUIKit 为您提供了聊天面板供您直接使用。聊天面板分为 C2C 单聊面板和群聊面板，分别对应单聊和群聊的使用场景。

- C2C 单聊面板
![](http://dldir1.qq.com/hudongzhibo/im/c2c.jpg)
- 群聊面板
![](http://dldir1.qq.com/hudongzhibo/im/groupnew.jpg)
- 群聊内嵌的群管理面板
![](http://dldir1.qq.com/hudongzhibo/im/groupinfo.jpg)

### 单聊面板（C2CChatPanel）使用

1. 在 Activity 或 Fragment（Demo 示例为创建一个 Fragment，即下面代码的 PersonalChatFragment）的布局文件里引用 C2CChatPanel。

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.tencent.qcloud.uikit.business.chat.c2c.view.C2CChatPanel
        android:id="@+id/chat_panel"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>

```

2. 添加完 C2CChatPanel 后，需对 C2CChatPanel 进行初始化操作。

```java

public class PersonalChatFragment extends BaseFragment {
    private View mBaseView;
    private C2CChatPanel chatPanel;
    private String chatId;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        mBaseView = inflater.inflate(R.layout.chat_fragment_personal, container, false);
        Bundle datas = getArguments();
        chatId = datas.getString(Constants.INTENT_DATA);
        initView();
        return mBaseView;
    }

    private void initView() {
        //从布局文件中获取聊天面板组件
        chatPanel = mBaseView.findViewById(R.id.chat_panel);
        //单聊组件的默认UI和交互初始化
        chatPanel.initDefault();
        /*
         * 需要指定会话 ID（即聊天对象的 identify，具体可参考 IM SDK 接入文档）来加载聊天消息。在上一章节 SessionClickListener 中回调函数的参数 SessionInfo 对象中持有每一会话的会话 ID，所以在会话列表单击时都可传入会话ID。
        * 特殊的如果用户应用不具备类似会话列表相关的组件，则需自行实现逻辑获取会话 ID 传入。
        */
        chatPanel.setBaseChatId(chatId);
    }
}
```

3、聊天面板组件提供的可扩展的事件和 UI 处理，具体可参考 [高级进阶—聊天面板 UI 扩展](#chatPanelExtra)。


### 群聊面板（GroupChatPanel）使用

群聊面板与单聊面板的使用基本一致，在 Activity 或 Fragment（Demo 示例为创建一个 Fragment，即下面代码的 GroupChatFragment）的布局文件里引用GroupChatPanel

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
>
    <com.tencent.qcloud.uikit.business.chat.group.view.GroupChatPanel
        android:id="@+id/chat_panel"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>

```

添加完 GroupChatPanel 后，需对 GroupChatPanel 进行初始化操作。

```java
public class GroupChatFragment extends BaseFragment {
    private View mBaseView;
    private GroupChatPanel chatPanel;
    private String groupChatId;

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        mBaseView = inflater.inflate(R.layout.chat_fragment_group, container, false);
        Bundle datas = getArguments();
        //由会话列表传入的群组 ID
        groupChatId = datas.getString(Constants.INTENT_DATA);
        initView();
        return mBaseView;
    }

    private void initView() {
        //从布局文件中获取聊天面板组件
        chatPanel = mBaseView.findViewById(R.id.chat_panel);
        //单聊组件的默认UI和交互初始化
        chatPanel.initDefault();
        /*
         * GroupChatPanel 在初始化完成后需要入会话 ID（即群组 ID，具体可参考 IM SDK 接入文档）来加载聊天消息。在上一章节 SessionClickListener 中回调函数的参数SessionInfo对象中持有每一会话的会话 ID，如果是群会话则为群组 ID，所以在会话列表单击时都可传入会话 ID。

        * 特殊的如果用户应用不具备类似会话列表相关的组件，则在使用群聊面板时需自行实现逻辑获取群组 ID 传入。
        */
        chatPanel.setBaseChatId(groupChatId);
       
    }

```
3. 同样的，群聊面板组件也提供了可扩展的事件和 UI 处理，具体可参考 [高级进阶—聊天面板UI扩展](#chatPanelExtra)。




## 高级进阶
前面介绍了 TUIKit 一些基本的使用流程，大多数情况下开发者使用默认配置即可完成相关业务的实现。
此外 TUIKit 也提供了丰富的组件和扩展功能，供开发着实现自己在相关功能及 UI 交互上的特殊需求。


- <span id="configs">IM SDK 的版本指定</span>
目前 TUIKit 所依赖的 IM SDK 版本为 V4.3.118。在 TIMSDK/Android/tuikit/libs/ 目录下，可以获取最新发布的 IM SDK 版本。


- <span id="iminit">和已有的 IM SDK 相结合</span>
目前 TUIKit 初始化已经内部实现了 IM SDK 的初始化（详细的 IM SDK 初始化可参考  [IM SDK初始化](https://cloud.tencent.com/document/product/269/9229)），并注册了 IM 相关的事件监听和回调。
如果您是在已使用 IM SDK 的应用中新用到 TUIKit，亦或是需要在对 IM SDK 某些回调做定制化处理，则需实现 IMEventListener，并通过 BaseUIKitConfigs.setIMEventListener() 将自定义的回调设置给 IM SDK。

>?如果您已有的项目中有 IM SDK 的初始化或事件注册代码，需废弃掉，使用 TUIKit 的初始化和 IM 事件注册。
如下面事件注册相关的老代码：

```java
//原有的初始化代码
TIMSdkConfig config = new TIMSdkConfig(Constants.SDKAPPID).setLogLevel(TIMLogLevel.DEBUG);
TIMManager.getInstance().init(getApplicationContext(), config);

//应替换成（BaseUIKitConfigs 的配置请看后面章节）
TUIKit.init(this, Constants.SDKAPPID, BaseUIKitConfigs.getDefaultConfigs().setTIMSdkConfig(config));
       
//原有的事件监听相关代码
TIMManager.getInstance().setOfflinePushListener(***);
TIMUserConfig userConfig = new TIMUserConfig(***);
userConfig.setUserStatusListener(***);
userConfig.setConnectionListener(***）

//替换成 IMEventListener，在替换成 IMEventListener 实现相关事件回调处理
TUIKit.getBaseConfigs().setIMEventListener(new IMEventListener(){***}）
```
IMEventListener 是一个 TUIKit 封装的 IM 事件缺省的类，您只需实现自己需要使用的回调接口即可。

```java
public abstract class IMEventListener {
    private final static String TAG = IMEventListener.class.getSimpleName();

    /**
     * 被踢下线时回调
     */
    public void onForceOffline(){
        QLog.d(TAG, "recv onForceOffline");
    }

    /**
     * 用户票据过期
     */
    public void onUserSigExpired(){
        QLog.d(TAG, "recv onUserSigExpired");
    }

    /**
     * 连接建立
     */
    public void onConnected(){
        QLog.d(TAG, "recv onConnected");
    }

    /**
     * 连接断开
     *
     * @param code 错误码
     * @param desc 错误描述
     */
    public void onDisconnected(int code, String desc){
        QLog.d(TAG, "recv onDisconnected, code " + code + "|desc " + desc);
    }

    /**
     * Wi-Fi 需要验证
     *
     * @param name Wi-Fi 名称
     */
    public void onWifiNeedAuth(String name){
        QLog.d(TAG, "recv onWifiNeedAuth, wifi name " + name);
    }

    /**
     * 部分会话刷新（包括多终端已读上报同步）
     * @param conversations 需要刷新的会话列表
     */
    public void onRefreshConversation(List<TIMConversation> conversations){
        QLog.d(TAG, "recv onRefreshConversation, size " + (conversations != null ? conversations.size() : 0));
    }

    /**
     * 收到新消息回调
     * @param msgs 收到的新消息
     */
    void onNewMessages(List<TIMMessage> msgs){
        QLog.d(TAG, "recv onNewMessages, size " + (msgs != null ? msgs.size() : 0));
    }

    /**
     * 群 Tips 事件通知回调
     *
     * @param elem 群 Tips 消息
     */
    void onGroupTipsEvent(TIMGroupTipsElem elem){
        QLog.d(TAG, "recv onGroupTipsEvent, groupid: "+ elem.getGroupId() + "|type: " + elem.getTipsType());
    }
}
```

- <span id="configs">TUIKit 的初始化配置</span>
目前 TUIKit 初始化提供了一个配置类 BaseUIKitConfigs，开发者可对下面的配置项进行配置。


|配置项|描述|类型|
| --- | --- | --- |
|setAppCacheDir|配置 App 保存图片/语音/文件/log 等数据缓存的目录；默认为 /sdcard/{packageName} |String|
|setInputTextMaxLength|文本消息最大输入字符数目|int|
|setAudioRecordMaxTime|语音消息的最大时长|int|
|setVideoRecordMaxTime|视频消息的摄像时长|int|
|setFaceConfigs|自定义表情配置|ArrayList&lt;CustomFaceGroupConfigs&gt;|
|setTIMSdkConfig|自定义 TIMSdkConfig（可参考 [IM SDK 初始化](https://cloud.tencent.com/document/product/269/9229)）|TIMSdkConfig|

配置类本身为建造者模式，可以一行代码完成配置。

```
BaseUIKitConfigs.getDefaultConfigs().setAppCacheDir("xxxxx").setAudioRecordMaxTime(60).setMaxInputTextLength(120)...
```


- <span id="sessionPanelExtra">会话列表面板（SessionPanel）UI 扩展</span>
SessionPanel 对外暴露了相关的子组件，开发者可自行对其进行相关 UI 的修改。

|组件名称|描述|类型|
| --- | --- | --- |
|mTitleBar|一般用来控制组件的跳转和标题栏的单击，开发者可自行修改和控制，详见 [通用标题栏](#pageTitleBar)<br>会话面板的标题栏默认实现了右边菜单栏的单击 |PageTitleBar|
|mSessionList|会话列表 ListView|SessionListView|
|mSessionPopList|会话 Item 长按弹框 List|ListView|
|mPopMenuList|标题栏右边单击弹框 List|ListView|

除对外开放的UI子组件外，SessionPanel 实现了 ISessionPanel 接口，该接口的将一些常用的定制化处理函数抽离处理。开发者可通过 ISessionPanel 教直观的操作 SessionPanel。

```
public interface ISessionPanel {

    /**
     * 设置会话面板的 Listview 的适配器，若用户想完全开发一套自己UI风格的会话列表，实现一个基于 ISessionAdapter 的适配器即可
     *
     * @param adapter
     */
    void setSessionAdapter(ISessionAdapter adapter);


    /**
     * 设置会话列表单击回调事件，控制会话单击时的界面跳转
     *
     * @param clickListener
     */
    void setSessionClick(SessionClickListener clickListener);


    /**
     * 设置更多弹框的 Action，开发者可调用该接口修改默认的更多弹框操作
     *
     * @param actions PopMenuAction 集合
     * @param isAdd   是否为添加，ture 为在默认的弹框集合上添加新的 item，false 再替换默认的
     */
    public void setMorePopActions(List<PopMenuAction> actions, boolean isAdd);


    /**
     * 设置会话长按弹框的 Action，开发者可调用该接口修改默认的会话长按操作
     *
     * @param actions PopMenuAction 集合
     * @param isAdd   是否为添加，ture 为在默认的弹框集合上添加新的 item，false 再替换默认的
     */
    public void setSessionPopActions(List<PopMenuAction> actions, boolean isAdd);

    /**
     * 设置会话列表其它事件（除单击事件外）监听器，不设置则用默认实现
     *
     * @param {SessionListEvent} event
     */
    public void setSessionListEvent(SessionListEvent event);


    /**
     * 依据数据源强行刷新会话面板界面
     */
    void refresh();

    /**
     * 开放会话头像编辑功能，开发者可在头像的布局里添加元素（如添加挂件，头衔等）
     *
     * @param dynamicIconView
     */
    void setSessionIconInvoke(DynamicSessionIconView dynamicIconView);

    /**
     * SessionPanel 的默认初始化设置，会初始化弹框，长按事件等
     */
    void initDefault();


}
```

- <span id="chatPanelExtra">聊天面板（ChatPanel）UI 扩展 SessionPanel</span>
单聊 C2CChatPanel，群聊 GroupChatPanel 都继承自 ChatPanel。针对业务的差异性，组件内的相关逻辑和交互也所有区别。TUIKit 内部已经处理了相关差异性。开发者可无需关注。
C2CChatPanel 和 GroupChatPanel 对外暴露了相关的子组件是一致的，开发者可自行对相关 UI 进行修改。

|组件名称|描述|类型|
| --- | --- | --- |
|mTitleBar|一般用来控制组件的跳转和标题栏的单击，开发者可自行修改和控制，详见 [通用标题栏](#pageTitleBar)<br>聊天面板的标题栏默认实现了左边返回按钮单击（群聊面板实现了边群信息 Icon 单击的跳转）|PageTitleBar|
|mChatList|消息面板 List|ChatListView|
|mInputGroup|聊天面板底部输入控件|ChatBottomInputGroup|
|mItemPopMenuList|消息长按弹框 List|ListView|

除对外开放的 UI 子组件外，ChatPanel 实现了 IChatPanel 接口，该接口的将聊天面板常用的一些 UI 相关的处理封装成 API。开发者可通过 IChatPanel 较直观高效的操作 ChatPanel。

```
public interface IChatPanel {

    /**
     * 设置当前的会话 ID，会话面板会依据该 ID 加载会话所需的相关信息，如消息记录，用户（群）信息等
     *
     * @param chatId
     */
    void setBaseChatId(String chatId);

    /**
     * 设置聊天面板的消息适配器，若开发者想完全替换 TUIKit 的消息风格，自行开发一个实现了 IChatAdapter 的适配器，通过该函数设置即可
     *
     * @param adapter
     */
    void setChatAdapter(IChatAdapter adapter);

    /**
     * 设置聊天列表的事件监听器
     *
     * @param event
     */
    void setChatListEvent(ChatListEvent event);

    /**
     * 设置底部更多消息操作集合，如图片消息操作，摄像消息操作等，开发者可定制化
     *
     * @param units 消息操作集合
     * @param isAdd 是否为添加，true 为在默认实现后添加，false 为覆盖
     */
    void setMoreOperaUnits(List<MessageOperaUnit> units, boolean isAdd);


    /**
     * 设置长按消息时弹框列表
     *
     * @param actions 弹框事件集合
     * @param isAdd   是否为添加，true 为添加事件，false 为覆盖组件以定义事件
     */
    void setMessagePopActions(List<PopMenuAction> actions, boolean isAdd);

    /**
     * 依据当前的聊天数据主动刷新聊天界面
     */
    void refreshData();


    /**
     * 退出聊天时的回调
     */
    void exitChat();

    /**
     * 使用初始化配置（即使用 UIKIT sdk 中聊天面板的默认配置）
     */
    void initDefault();
}
```

- <span id="pageTitleBar">通用标题栏 PageTitleBar</span>
![](	http://dldir1.qq.com/hudongzhibo/im/titlebar.jpg)
一般的界面都有一个标题栏，如上图中的标红区域，包含返回单击按钮，标题，右边跳转按钮等，TUIKit 提供了一个内部通用的标题栏（SessionPanel，ChatPanel 都有集成该组件），开发者可根据自己的使用场景做定制修改，包括文案、图标修改、跳转控制等。

|组件名称|描述|类型|
| --- | --- | --- |
|mLeftGroup|左边区域，一般用来设置单击事件（如 mLeftGroup.setOnClickListener(...)）|LinearLayout|
|mRightGroup|右边区域，一般用来设置单击事件（如 mRightGroup.setOnClickListener(...)|LinearLayout|
|mLeftTitle|左边标题，如果标题栏左边需要文案，可通过此属性来设置|TextView|
|mRightTitle|右边标题，如果标题栏右边需要文案，可通过此属性来设置|TextView|
|mCenterTitle|中间边标题，如果标题栏右边需要文案，可通过此属性来设置|TextView|
|mLeftIcon|左边 icon，如果标题栏左边需要设置自己的 icon，可通过此属性来设置|ImageView|
|mRightIcon|右边 icon，如果标题栏右边需要设置自己的 icon，可通过此属性来设置|ImageView|

## 快速体验

欢迎扫码体验我们的 DEMO，后续会继续完善。更多最新资讯请关注 [这里](https://github.com/zhaoyang21cn/IMTUIkit_android)。

![](https://main.qcloudimg.com/raw/fe3ef4a58c3efa5388e57a653133f392.png)


