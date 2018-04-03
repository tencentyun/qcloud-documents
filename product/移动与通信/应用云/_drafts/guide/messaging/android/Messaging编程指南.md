## 手动集成

如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Messaging 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-messaging-1.0.0.zip)，并解压。

### 2. 集成 jar 包 和 so 包

* 将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。
* 如果您是采用 Eclipse 开发，将资源文件中的 `jni` 目录下的内容 拷贝到您工程您工程的 `libs` 目录。
* 如果您是采用 Android Studio 开发，将资源文件中的 `jni` 目录下的内容 拷贝到 app 模块的 `main` 文件夹下的 `jniLibs` 目录下 。如果不存在该目录，请新建一个。

### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件：

```
<!-- Messaging 所需权限   -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />

<application
  <!-- 消息receiver广播接收 -->
  <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
   	android:process=":xg_service_v3" >
  	<intent-filter android:priority="0x7fffffff" >
  	
      	<action android:name="com.tencent.android.tpush.action.SDK" />
      	<action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
      	
      	<action android:name="android.intent.action.USER_PRESENT" />
     	<action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
     	<action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
      	<action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
      	<action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
  	</intent-filter>
  </receiver>

  <!-- Messaging receiver，用于接收消息透传和操作结果的回调 -->
  <receiver android:name="com.tencent.tac.messaging.TACMessagingXGReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- 接收消息透传 -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>

   <!-- 接受通知的activity -->
   <activity
            android:name="com.tencent.android.tpush.XGPushActivity"
            android:exported="false"
            android:theme="@android:style/Theme.Translucent" >
            <intent-filter>	
                <action android:name="android.intent.action" />
            </intent-filter>
   </activity>

   <service
       android:name="com.tencent.android.tpush.service.XGPushServiceV3"
       android:exported="true"
       android:persistent="true"
       android:process=":xg_service_v3" />


  <service
      android:name="com.tencent.android.tpush.rpc.XGRemoteService"
      android:exported="true">
      <intent-filter>
          <action android:name="[您的应用包名].PUSH_ACTION" />
      </intent-filter>
   </service>


  <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       android:authorities="[您的应用包名].AUTH_XGPUSH"
       android:exported="true"/>

  <provider
       android:name="com.tencent.android.tpush.SettingsContentProvider"
       android:authorities="[您的应用包名].TPUSH_PROVIDER"
       android:exported="false" />

  <provider
       android:name="com.tencent.mid.api.MidProvider"
       android:authorities="[您的应用包名].TENCENT.MID.V3"
       android:exported="true" >
  </provider>
  
</application>
```

## 注册 Messaging 服务回调

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

## 启动 Messaging 服务

集成好 Messaging 服务后，需要您在 `Application` 的 `onCreate` 方法中启动服务，具体代码如下：

```
// 首先获取 TACMessagingService 实例
TACMessagingService messagingService = TACMessagingService.getInstance();

// 调用 start 接口启动 Messaging 服务，context 这里最好使用 application context。
messagingService.start(context);

```

## 停止 Messaging 服务

停止 Messaging 服务，建议在不需要接收推送的时候调用：

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.stop(context);
```

## 订阅主题

您可以针对不同的用户订阅主题，然后在前台根据主题群发通知。 一个应用最多有10000个 tag， 每个 token 在一个应用下最多100个 tag， tag 中不准包含空格。

### 订阅主题

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.subscribeToTopic(Context context, String topic);
```

### 取消订阅主题

```
TACMessagingService messagingService = TACMessagingService.getInstance();
messagingService.unsubscribeFromTopic(Context context, String topic);
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

## 错误码

### 服务端返回码

| 值| 	含义| 	解决方法| 
| :---: | :----: | :---- |
|0	|调用成功||
|-1	|参数错误|	检查参数配置|
|-2	|请求时间戳不在有效期内	|检查设备当前时间|
|-3	|recv 失败	|稍后重试|
|-5	|Action 处理超时|	稍后重试|
|2	|非法参数	|检查参数配置|
|5	|与 CMEM 通讯失败|	稍后重试（推送超时）|
|6	|设备 token 未成功注册|	请检查终端设备注册是否成功
|7	|通用错误，账号超限	|删除其他未使用的账号(调用账号解绑）|
|14	|token 非法	|Token 长度为 40 位|
|15|	信鸽逻辑服务器繁忙	|稍后重试|
|16	|系统繁忙	|稍后重试|
|19	|操作时序错误。例如进行 tag 操作前未获取到 deviceToken|	没有获取到 deviceToken 的原因：1. 没有注册信鸽或者苹果推送 2. provisioning  profile制作不正确|
|20	|鉴权错误，可能是由于 Access ID 和 Access Key 不匹配|	检查 Access ID 和 Access Key （注意空格）|
|21|	鉴权失败	|检查 Access ID 和 Access Key|
|40	|推送的 token 没有在信鸽中注册	|检查 token 是否注册|
|48	|推送的账号没有绑定 token	|检查 account 和 token 是否有绑定关系见推送指南：绑定/设置账号见热门问题解答：账号和设备未绑定的解答|
|53	|设备未注册	|反注册后重新注册|
|75	|消息体格式不符合 json 格式	|检查消息体即 message 字段内容|
|76	|请求过于频繁，请稍后再试	|全量广播限频为每3秒一次|
|78	|循环任务参数错误	|检查 loop time|
|90	|设备离线	|重新打开应用|
|91	|设备 tag 过多	|清理不使用的 tag|
|92	|apptag 过多	|清理不使用的 tag|
|-101	|参数错误|	请检查参数|
|-102|	请求 timestamp 字段超过了时间过期|	请使用当前系统时间戳，确保时间同步|
|-103|	sign 不合法|	检查签名生成流程，生成 sign 是 METHOD 必须与请求时所使用的一致|
|-105|	请求过于频繁|	稍后重试|
|-106	|证书错误|	证书错误|
|-111|	缺少公共参数：access_id\timestamp\sign|	检查公共参数 access_id\timestamp\sign|
|-112	|参数取值非法	|检查参数取值|
|其他	|信鸽内部错误	|稍后重试，如出现为标明且必现错误请及时与我们取得联系|

### 客户端返回码


| 值| 	原因以及解决办法| 
| :---: | :---- |
|0	|调用成功|
|2	|参数错误，例如绑定了单字符的别名，或是 ios 的 token长度不对，应为64个字符|
|20	|鉴权错误,access id 或者 access key 配置错误|
|10000	|起始错误|
|10001	|操作类型错误码，例如参数错误时将会发生该错误|
|10002	|正在执行注册操作时，又有一个注册操作到来，则回调此错误码|
|10003|	权限配错或者缺少所需权限|
|10004	|so 库没有正确导入（Androidstudio 可在 main 文件目录下 添加 jniLibs 命名的文件夹将 SDK 文档中的 Other-Platform-SO 下的7个 so 库文件夹添加至该目录）|
|10005	|AndroidManifest 文件的 XGRemoteService 节点没有配置或者的该节点的 action 包名配错|
|10008	|jce JAR 错误或者缺少 jce JAR（如果是混淆打包过后出现,请检查混淆代码）|
|10101	|创建链路失败（切换网络重试）|
|10102	|请求处理过程中， 链路被主动关闭（切换网络重试）|
|10103	|请求处理过程中，服务器关闭链接（切换网络重试）|
|10104	|请求处理过程中，客户端产生异常（切换网络重试）|
|10105	|请求处理过程中，发送或接收报文超时（切换网络重试）|
|10106	|请求处理过程中， 等待发送请求超时（切换网络重试）|
|10107	|请求处理过程中， 等待接收请求超时（切换网络重试）|
|10108	|服务器返回异常报文|
|10109	|未知异常，切换网络 或者 重启设备）|
|10110	|创建链路的 handler 为 null|
|其他|	如出现其他未知错误 请记录错误日志 与我们取得联系|

