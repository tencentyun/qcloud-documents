通过注册 Messaging 服务广播接收器，您可以收到 Messaging 服务的通知，您需要继承 `TACMessagingReceiver` 类，然后在 `AndroidManifest.xml` 文件中进行如下注册：

```
<receiver android:name="com.yourpackage.MessagingReceiver">
	<intent-filter>
	    <action android:name="com.tencent.tac.messaging.action.CALLBACK" />
	</intent-filter>
</receiver>

```

`TACMessagingReceiver` 的回调方法说明如下，您可以根据业务需求，在回调时执行业务逻辑。


### 注册结果回调

```
	/**
     * 注册结果回调。
     *
     * <p>
     * 用户可以在这里获取注册的状态，如果注册成功，则会返回 token 。
     * </p>
     *
     * @param context 上下文
     * @param errorCode 错误码
     * @param token 设备标识
     */
    void onRegisterResult(Context context, int errorCode, TACMessagingToken token);
```

注册成功后，可以获得设备标识 `TACMessagingToken `。

相关错误码说明请看文档最后的列表。

### 反注册结果回调

```
	 /**
     * 反注册结果回调
     *
     * @param context 上下文
     * @param code 错误码
     */
    void onUnregisterResult(Context context, int code);
```

相关错误码说明请看文档最后的列表。

### 收到通知消息

```
	 /**
     * 收到通知消息。
     *
     * <p>
     * SDK 会自动帮用户处理通知消息的所有逻辑。
     * </p>
     *
     * @param context 上下文
     * @param notification 通知消息
     * @param notificationId 通知消息对应的notification id
     */
    void onNotificationShowed(Context context, TACNotification notification, int notificationId);

```

`TACNotification ` 代表一个通知栏消息，消息的属性说明如下：

```
long id = notification.getId();	// 消息的id

String activity = notification.getActivity();   // 获取消息点击会启动的activity名

TACMessagingText text = notification.getText();   // 获取消息内容

int actionType = notification.getNotificationActionType();  // 消息点击后的动作类型
```

`actionType` 有几种类型：

```
	/**
     * notification 点击后，启动 Activity
     */
    public static final int NOTIFICATION_ACTION_ACTIVITY = 1;

    /**
     * notification 点击后，启动浏览器
     */
    public static final int NOTIFICATION_ACTION_URL = 2;

    /**
     * notification 点击后，启动 Intent
     */
    public static final int NOTIFICATION_ACTION_INTENT = 3;

    /**
     * notification 点击后，启动 Application
     */
    public static final int NOTIFICATION_ACTION_PACKAGE = 4;
``` 

`TACMessagingText` 代表一个消息的内容，消息的属性说明如下：

```
String title = text.getTitle();   // 获取消息标题

String content = text.getContent();   // 获取消息内容

String customContent = text.getCustomContent();   // 获取自定义内容

```

### 收到应用内消息回调

```
	 /**
     * 收到应用内消息回调。
     *
     * <p>
     * 接收到应用内消息后，用户自己自定义处理逻辑。
     * </p>
     *
     * @param context 上下文
     * @param message 应用内消息
     */
    void onTextMessage(Context context, TACMessagingText message);
```

### 通知栏消息被点击的回调

```
	/**
     * 通知消息被处理。
     *
     * <p>
     * 通知处理的方式一般分为点击和删除两种。
     * </p>
     *
     * @param context 上下文
     * @param notification 通知消息
     * @param actionType 用户处理的方式
     */
    void onNotificationClicked(Context context, TACNotification notification, long actionType);

```

`actionType` 的定义在 `TACNotification` 中，说明如下：

```
public static final int NOTIFICATION_CLICKED_TYPE = 0;  // 用户点击了通知
public static final int NOTIFICATION_DELETED_TYPE = 2;  // 用户清除了通知
```
