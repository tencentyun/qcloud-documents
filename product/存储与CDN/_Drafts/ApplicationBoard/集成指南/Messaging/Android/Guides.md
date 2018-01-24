# 应用云 Messaging 服务 Android 接入指南

## 注册 Messaging 服务回调

通过注册 Messaging 服务广播接收器，你可以收到 Messaging 服务的通知。你需要继承 TACMessagingReceiver 类，然后在 AndroidManifest.xml 文件中进行如下注册：

```
<receiver android:name="TACMessagingReceiver子类，如com.tencent.tac.tacmessaging.MyReceiver">
	<intent-filter>
	    <action android:name="com.tencent.tac.messaging.action.CALLBACK" />
	</intent-filter>
</receiver>

```

注册后的通知如下：

```
/**
 * 注册结果回调。
 */
void onRegisterResult(Context context, int errorCode, TACMessagingToken token);

/**
 * 收到应用内消息回调。
 */
void onTextMessage(Context context, TACMessagingText message);

/**
 * 收到通知消息。
 */
void onNotificationShowed(Context context, TACNotification notification, int notificationId);

/**
 * 通知消息被处理。
 */
void onNotificationClicked(Context context, TACNotification notification, long actionType);

/**
 * 反注册结果回调
 */
void onUnregisterResult(Context context, int code);

```

## 启动 Messaging 服务

集成好 Messaging 服务后，需要您在 Application 的 onCreate() 方法中启动服务，具体代码如下：

```
// 首先获取 TACMessagingService 实例
TACMessagingService messagingService = TACMessagingService.getInstance();

// 调用 start 接口启动 Messaging 服务，context 这里最好使用 application context。
messagingService.start(context);

```

## 停止 Messaging 服务

停止 Messaging 服务，建议在不需要接收推送的时候调用。

```
messagingService.stop(context);

```

