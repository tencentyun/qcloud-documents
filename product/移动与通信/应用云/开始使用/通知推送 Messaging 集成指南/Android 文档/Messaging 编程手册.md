
## 订阅 tag

您可以针对不同的用户订阅 tag，然后在前台根据 tag 群发通知。 一个应用最多有10000个 tag， 每个 token 在一个应用下最多100个 tag， tag 中不准包含空格。

### 订阅 tag

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.subscribeToTopic(Context context, String tag);
```

### 取消订阅 tag

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.unsubscribeFromTopic(Context context, String tag);
```

## 停止 Messaging 服务

停止 Messaging 服务，建议在不需要接收推送的时候调用：

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.stop(context);
```

## 获取通知是否可用

用户可以通过设置关闭应用的通知权限，您可以检查是否有权限弹出通知栏通知：

```
TACMessagingService messagingService = TACMessagingService.getInstance();

boolean isNotificationEnable = messagingService.isNotificationEnable(Context);
```

## 获取设备唯一标识

设备唯一标识是一串字符串，可以在注册成功的回调中通过 `TACMessagingToken ` 获取：

```
TACMessagingToken messagingToken...
String tokenString = messagingToken.getgetTokenString();  // 获取设备唯一标识
```



## 设置通知样式

您可以根据自行需要设置通知样式，然后在后台推送通知的时候，可以设置样式的 ID。由于目前的定制 ROM 的限制，部分接口无法适配全部机型。

下面是设置样式的示例代码：

```
		TACMessagingNotificationBuilder build = new  TACMessagingNotificationBuilder();

        build.setSound(
                RingtoneManager.getActualDefaultRingtoneUri(

                        getApplicationContext(), RingtoneManager.TYPE_ALARM))

                .setDefaults(Notification.DEFAULT_VIBRATE) // 振动

                .setFlags(Notification.FLAG_NO_CLEAR); // 是否可清除

        // 设置自定义通知layout,通知背景等可以在layout里设置

        build.setLayoutId(R.layout.notification);

        // 设置自定义通知内容id

        build.setLayoutTextId(R.id.content);

        // 设置自定义通知标题id

        build.setLayoutTitleId(R.id.title);


        // 设置自定义通知图片资源

        build.setLayoutIconDrawableId(R.drawable.logo);

        // 设置状态栏的通知小图标

        build.setIcon(R.drawable.right);

        // 设置时间id

        build.setLayoutTimeId(R.id.time);

        // 若不设定以上自定义layout，又想简单指定通知栏图片资源

        build.setNotificationLargeIcon(R.drawable.ic_action_search);
```

然后，在控制台选择设置好的 ID 来推送通知。其中 的 `NotificationBuilderId` 是样式的 ID。

```
		// notificationBuilderId 是样式的 id

		TACMessagingService messagingService = TACMessagingService.getInstance();
		messagingService.addNotificationBuilder(Context, notificationBuilderId, build);
```

## 本地通知

您可以自定义本地通知，保存在本地。当应用打开，Messaging 服务会根据网络心跳判断当前是否有通知5分钟一次本地通知需要服务启动才能弹出，可能存在一定延迟。

```
	//新建本地通知
    TACMessagingLocalMessage localMsg = new TACMessagingLocalMessage();

    //设置本地消息类型，1:通知，2:消息

    localMsg.setType(1);

    // 设置消息标题

    localMsg.setTitle("qq");

    //设置消息内容

    localMsg.setContent("ww");

    //设置消息日期，格式为：20140502

    localMsg.setDate("20140930");

    //设置消息触发的小时(24小时制)，例如：22代表晚上10点

    localMsg.setHour("19");

    //获取消息触发的分钟，例如：05代表05分

    localMsg.setMin("31");

    //设置消息样式，默认为0或不设置

    localMsg.setBuilderId(0);

    //设置动作类型：1打开activity或app本身，2打开浏览器，3打开Intent ，4通过包名打开应用

    localMsg.setAction_type(1);

    //设置拉起应用页面

    localMsg.setActivity("com.qq.xgdemo.SettingActivity");
    
    // 设置URL

    localMsg.setUrl("http://www.baidu.com");

    // 设置Intent

    localMsg.setIntent("intent:10086#Intent;scheme=tel;action=android.intent.action.DIAL;S.key=value;end");

    // 是否覆盖原先build_id的保存设置。1覆盖，0不覆盖

    localMsg.setStyle_id(1);

    // 设置音频资源

    localMsg.setRing_raw("mm");

    // 设置key,value

    HashMap<String, Object> map = new HashMap<String, Object>();
    map.put("key", "v1");
    map.put("key2", "v2");
    localMsg.setCustomContent(map);

    // 设置下载应用URL

    localMsg.setPackageDownloadUrl("http://softfile.3g.qq.com:8080/msoft/179/1105/10753/MobileQQ1.0(Android)_Build0198.apk");

    //添加通知到本地

	TACMessagingService messagingService = TACMessagingService.getInstance();
	messagingService.addLocalNotification(Context, localMsg);
```

