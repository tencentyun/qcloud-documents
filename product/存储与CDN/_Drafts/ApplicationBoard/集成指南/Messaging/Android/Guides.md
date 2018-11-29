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

## 获取注册令牌

您的应用初次启动时，SDK 会为客户端应用实例生成一个注册令牌。要将信息发送到特定的设备，您需要知道该设备的注册令牌。

您可以通过注册的 TACMessagingReceiver 子类中的注册回调方法中的 TACMessagingToken 来获取令牌。

```
/**
 * 注册结果回调。
 */
void onRegisterResult(Context context, int errorCode, TACMessagingToken tokenManager) {

	String token = tokenManager.getToken();
}

```

## 为客户端订阅主题

客户端应用可以订阅任何现有主题，也可创建新主题。当客户端应用订阅新的主题名称（您的 TACMessaging 项目中尚不存在的名称）时，系统会在 Messaging 中创建使用这个名称的新主题，随后任何客户端都可订阅该主题。

```
String topic = "news";
messagingService.subscribeToTopic(context, topic);
```

同时您也可以退订该主题。

```
messagingService.unsubscribeFromTopic(context, topic);
```

## 接收和处理消息

Messaging 服务的消息分为两种，分别为通知消息和应用内消息。通知消息由 SDK 进行处理，并在通知栏上显示，用户会在收到通知消息和点击通知消息时收到回调。应用内消息由用户自己处理，不会再通知栏上展示，收到应用内消息后同样会收到回调。

通知消息的回调由注册的 TACMessagingReceiver 子类来进行回调

```
/**
 * 收到通知消息。
 */
void onNotificationShowed(Context context, TACNotification notification, int notificationId);

/**
 * 通知消息被处理。
 */
void onNotificationClicked(Context context, TACNotification notification, long actionType);

```

应用内消息同样由注册的 TACMessagingReceiver 子类来进行回调。 

```
/**
 * 收到应用内消息回调。
 */
void onTextMessage(Context context, TACMessagingText message);

```






