
## 应用云 Messaging 服务 Android 接入指南

Messaging 服务是腾讯云提供的一种快速、简单的推送服务，支持 Android 平台的通知栏推送和应用内透传消息。开发者可以将指定的信息推送给需要的用户。


### 集成 Messaging 服务到你的应用

#### 添加 Messaging 服务依赖

你需要在 module 下的 build.gradle 文件中添加如下内容：

```
android {
    ......
    defaultConfig {

        // 官网上注册的包名。注意 application ID 和当前的应用包名以及官网上注册应用的包名必须一致。
        applicationId "你的包名"
        ......
    }
    ......
}

dependencies {
    ......

    compile 'com.tencent.tac:messaging:1.0.0'

}

```

### 注册 Messaging 服务回调

通过注册 Messaging 服务广播接收器，你可以收到 Messaging 服务的通知。你需要继承 TACMessagingReceiver 类，然后将子类在 manifest.xml 文件中进行如下注册：

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

### 启动 Messaging 服务

集成好 Messaging 服务后，你需要自己启动 Messaging 服务，具体代码如下：

```
// 首先获取 TACMessagingService 实例
TACMessagingService messagingService = TACMessagingService.getInstance();

// 调用 start 接口启动 Messaging 服务，context 这里最好使用 application context。
messagingService.start(context);

```

### 停止 Messaging 服务

停止 Messaging 服务，建议在不需要接收推送的时候调用。

```
messagingService.stop(context);

```

