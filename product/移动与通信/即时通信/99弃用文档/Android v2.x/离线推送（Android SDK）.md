## 概述

**离线推送**指的是应用在没有退出登录的情况下，被系统或者用户杀掉后仍能收到 ImSDK 消息提醒。要实现离线推送功能，需要集成云通信离线推送。另外，ImSDK 从 2.1.0 版本开始，提供了适配小米、华为离线推送的方案。

> **注意：**
>- 对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。
>- 目前，离线推送只提供 [普通聊天消息](/doc/product/269/%E6%B6%88%E6%81%AF%E6%94%B6%E5%8F%91%EF%BC%88Android%20SDK%EF%BC%89#1-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 进行消息提醒，暂不提供对 [系统消息](/doc/product/269/消息收发（Android%20SDK）#.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF) 的消息提醒 。

## 设置离线推送配置

### 设置全局离线推送配置

ImSDK 从 2.1.0 版本开始提供了设置全局离线推送配置的功能，可以设置是否开启离线推送、收到离线推送时的提示声音等。这个设置方法是由 `TIMManager` 提供的 `configOfflinePushSettings`。

> **注意：**
>- 必须在登录成功后调用才生效。
>- 目前仅支持应用内置的声音文件。

**原型 ：**

```java
/**
 * 初始化离线推送配置，需登录后设置才生效
 * @param settings 离线推送配置信息
 */
public void configOfflinePushSettings(TIMOfflinePushSettings settings)
/**
 * 从服务器获取离线推送配置，需登录后才能获取
 * @param cb 回调，在 onSuccess 的参数中返回离线推送配置
 */
public void getOfflinePushSettings(final TIMValueCallBack<TIMOfflinePushSettings> cb)
```

**参数说明：**

参数|说明
---|---
settings|离线推送配置

**`TIMOfflinePushSettings` 说明：**

```java
/**
 * 获取是否开启
 * @return true - 开启， false - 不开启
 */
public boolean isEnabled()
/**
 * 设置是否开启离线推送
 * @param enabled 是否开启离线推送
 */
public void setEnabled(boolean enabled)
/**
 * 获取收到 c2c 消息的离线推送时的提醒声音
 * @return 声音文件的 URI，没有设置时返回 null
 */
public Uri getC2cMsgRemindSound()
/**
 * 设置收到 c2c 消息的离线推送时的提醒声音
 * @param c2cMsgRemindSound 声音文件的 URI，恢复系统默认声音填 null
 */
public void setC2cMsgRemindSound(Uri c2cMsgRemindSound)
/**
 * 获取收到群消息的离线推送时的提醒声音
 * @return 声音文件的 URI，没有设置时返回 null
 */
public Uri getGroupMsgRemindSound()
/**
 * 设置收到群消息的离线推送时的提醒声音
 * @param groupMsgRemindSound 声音文件的 URI， 恢复系统默认声音填 null
 */
public void setGroupMsgRemindSound(Uri groupMsgRemindSound)
```

**示例：**

```java
TIMOfflinePushSettings settings = new TIMOfflinePushSettings();
//开启离线推送
settings.setEnabled(true);
//设置收到 C2C 离线消息时的提示声音，这里把声音文件放到了 res/raw 文件夹下
settings.setC2cMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));
//设置收到群离线消息时的提示声音，这里把声音文件放到了 res/raw 文件夹下
settings.setGroupMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));
TIMManager.getInstance().configOfflinePushSettings(settings);
```

### 设置单条消息的离线推送配置

ImSDK 从 2.2.0 版本开始提供针对单独每一条消息进行离线推送配置的功能。开发者可以针对某条消息设置是否开启离线推送、收到离线推送后提醒声音、离线推送消息描述及扩展字段等。

> **注意：**
>- 针对单条消息设置的离线推送配置优先级是最高的，也就是在同时设置了全局离线推送配置及单条消息离线推送配置的情况下，将以单条消息离线推送配置为准。
>- 目前 Android 设备的声音仅支持应用内置的声音文件。
>- 此章节是根据 ImSDK 2.5.3 来说明的，在接入低于 2.5.3 版本的 ImSDK 时，单条消息的离线推送配置请参考 SDK 下载包中的 javadoc 进行配置。

**原型：**

```java
/**
 * 设置当前消息在对方收到离线推送的时候的配置（可选，发送消息时设置）
 * @param settings 离线推送配置
 */
public void setOfflinePushSettings(TIMMessageOfflinePushSettings settings)
/**
 * 获取当前消息的离线推送配置
 * @return 离线推送配置，如果发送方没有设置的情况下，返回 null
 */
public TIMMessageOfflinePushSettings getOfflinePushSettings()
```

**`TIMMessageOfflinePushSettings`说明：**

```java
/**
 * 设置当前消息在对方收到离线推送时候展示内容（可选，发送消息时设置）
 * @param descr 正文内容
 */
public void setDescr(String descr)
/**
 * 获取当前消息的离线推送展示正文内容
 * @return 正文内容
 */
public String getDescr()
/**
 * 设置当前消息的扩展字段（可选，发送消息的时候设置）
 * @param ext 扩展字段内容
 */
public void setExt(byte[] ext)
/**
 * 获取当前消息的扩展字段
 * @return 扩展字段内容，没有设置返回 null
 */
public byte[] getExt()
/**
 * 设置当前消息是否允许离线推送，默认允许推送（可选，发送消息时设置）
 * @param enabled true - 允许离线推送， false - 不允许离线推送
 */
public void setEnabled(boolean enabled)
/**
 * 获取当前消息是否允许推送
 * @return 是否允许推送标识， true - 允许推送， false - 不允许推送
 */
public boolean isEnabled()
/**
 * 获取当前消息在 Android 设备上的离线推送配置
 * @return Android 设备上的离线推送配置
 */
public AndroidSettings getAndroidSettings()
/**
 * 设置当前消息在 Android 设备上的离线推送配置（可选，发送消息时设置）
 * @param androidSettings 当前消息在 Android 设备上的离线推送配置
 */
public void setAndroidSettings(AndroidSettings androidSettings)
/**
 * 获取当前消息在 iOS 设备上的离线推送配置
 * @return iOS 设备上的离线推送配置
 */
public IOSSettings getIosSettings()
/**
 * 设置当前消息在 iOS 设备上的离线推送配置（可选，发送消息时设置）
 * @param iosSettings 当前消息在 iOS 设备上的离线推送配置
 */
public void setIosSettings(IOSSettings iosSettings)
```

**`TIMMessageOfflinePushSettings.AndroidSettings` 原型：**

```java
/**
 * 获取通知标题
 * @return 通知标题
 */
public String getTitle()
/**
 * 设置通知标题（可选，发送消息时设置）
 * @param title 通知标题
 */
public void setTitle(String title)
/**
 * 获取当前消息在 Android 设备上的离线推送提示声音 URI
 * @return 声音 URI，没有设置则返回 null
 */
public Uri getSound()
/**
 * 设置当前消息在 Android 设备上的离线推送提示声音（可选，发送消息时设置）
 * @param sound 声音 URI，仅支持应用内部的声音资源文件
 */
public void setSound(Uri sound)
/**
 * 获取当前消息的通知模式
 * @return 通知模式
 */
public NotifyMode getNotifyMode()
/**
 * 设置当前消息在对方收到离线推送时候的通知模式（可选，发送消息时设置）
 * @param mode 通知模式，默认为普通通知栏消息模式
 */
public void setNotifyMode(NotifyMode mode)
```

**`TIMMessageOfflinePushSettings.NotifyMode` 说明：**

>注：`NotifyMode` 只是针对第三方离线推送进行设置的，比如小米、华为的离线推送。

```java
/**
 * 普通通知栏消息模式，离线消息下发后，单击通知栏消息直接启动应用，不会给应用进行回调
 */
NotifyMode.Normal
/**
 * 自定义消息模式，离线消息下发后，单击通知栏消息会给应用进行回调
 */
NotifyMode.Custom
```

**`TIMMessageOfflinePushSettings.IOSSettings` 说明：**

```java
/**
 * 获取当前消息在 iOS 设备上的离线推送提示声音
 * @return 声音文件路径，没有设置则返回 null
 */
public String getSound()
/**
 * 设置当前消息在 iOS 设备上的离线推送提示声音（可选，发送消息时设置）
 * @param sound 声音文件路径，当设置为{@see IOSSettings#NO_SOUND_NO_VIBRATION}时表示无提示音无振动
 */
public void setSound(String sound)
/**
 * 获取当前消息是否开启 Badge 计数
 * @return true - 当前消息开启 Badge 计数
 */
public boolean isBadgeEnabled()
/**
 * 设置当前消息是否开启 Badge 计数，默认开启（可选，发送消息时设置）
 * @param badgeEnabled 否开启 Badge 计数
 */
public void setBadgeEnabled(boolean badgeEnabled)
```

**示例：**

```java
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加文本内容
TIMTextElem elem = new TIMTextElem();
elem.setText("a new msg from " + selfId);
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//设置当前消息的离线推送配置
TIMMessageOfflinePushSettings settings = new TIMMessageOfflinePushSettings();
settings.setEnabled(true);
settings.setDescr("I'm description");
//设置离线推送扩展信息
JSONObject object = new JSONObject();
try {
    object.put("level", 15);
    object.put("task", "TASK15");
    settings.setExt(object.toString().getBytes("utf-8"));
} catch (JSONException e) {
    e.printStackTrace();
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}
//设置在 Android 设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.AndroidSettings androidSettings = new TIMMessageOfflinePushSettings.AndroidSettings();
//ImSDK 2.5.3 之前的构造方式
//TIMMessageOfflinePushSettings.AndroidSettings androidSettings = settings.new AndroidSettings();
androidSettings.setTitle("I'm title");
//推送自定义通知栏消息，接收方收到消息后单击通知栏消息会给应用回调（针对小米、华为离线推送）
androidSettings.setNotifyMode(TIMMessageOfflinePushSettings.NotifyMode.Custom);
//设置 Android 设备收到消息时的提示音，声音文件需要放置到 raw 文件夹
androidSettings.setSound(Uri.parse("android.resource://" + getPackageName() + "/" +R.raw.hualala));
settings.setAndroidSettings(androidSettings);
//设置在 iOS 设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.IOSSettings iosSettings = new TIMMessageOfflinePushSettings.IOSSettings();
//ImSDK 2.5.3 之前的构造方式
//TIMMessageOfflinePushSettings.IOSSettings iosSettings = settings.new IOSSettings();
//开启 Badge 计数
iosSettings.setBadgeEnabled(true);  
//设置 iOS 收到消息时没有提示音且不振动（ImSDK 2.5.3 新增特性）
//iosSettings.setSound(TIMMessageOfflinePushSettings.IOSSettings.NO_SOUND_NO_VIBRATION);
//设置 iOS 设备收到离线消息时的提示音
iosSettings.setSound("/path/to/sound/file");
msg.setOfflinePushSettings(settings);
//获取一个单聊会话
TIMConversation conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.C2C,    //会话类型：单聊
        peer); 						//会话对方用户帐号
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.e(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.d(tag, "SendMsg ok! peer:" + peer );
    }
});
```

## 集成云通信离线推送

ImSDK 从 1.8.0 版本开始提供了离线推送的功能。因为离线推送依赖于守护进程，所以为了保证离线推送的正常运作，需要对应用的**自启动权限**进行授权，而部分对 Android 系统进行了深度定制化的机型（华为、小米等）则需要将应用添加到应用白名单，保证应用被杀掉后，守护进程可以自动重启。

### 配置 AndroidManifest

由于 ImSDK 的离线推送依赖于服务，所以需要应用在 `AndroidManifest.xml` 的`<application></application>`中添加以下配置：

```xml
<!--  消息收发 service -->
<service
    android:name="com.tencent.qalsdk.service.QalService"
    android:exported="false"
    android:process=":QALSERVICE" >  
</service>
<!--  消息收发辅助 service -->
<service  
    android:name="com.tencent.qalsdk.service.QalAssistService"  
    android:exported="false"
    android:process=":QALSERVICE" >
 </service>
<!--  离线消息广播接收器 -->
<receiver
    android:name="com.tencent.qalsdk.QALBroadcastReceiver"
    android:exported="false">
    <intent-filter>
        <action android:name="com.tencent.qalsdk.broadcast.qal" />
    </intent-filter>
</receiver>
<!--  系统消息广播接收器 -->
<receiver
    android:name="com.tencent.qalsdk.core.NetConnInfoCenter"  android:process=":QALSERVICE">  
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.intent.action.TIME_SET" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.intent.action.TIMEZONE_CHANGED" />
    </intent-filter>
</receiver>
```

### 设置离线推送处理

#### 实现自己的 Application 类

实现 `android.app.Application`，假设命名为 MyApplication，在 `AndroidManifes.xml` 中配置实现以下内容。

```xml
<!-- 应用在实现的时候请将 com.tencent.imsdk.test.MyApplication 替换为自己的 Application -->
<application
	android:allowBackup="true"
	android:icon="@drawable/ic_launcher"
	android:label="@string/app_name"
	android:name="com.tencent.imsdk.test.MyApplication">
	<!-- 这里省略其他各种配置 -->
</application>
```

#### 注册离线推送监听器

在以上的准备做好后，必须注册相应的离线推送监听器才能收到消息通知。如果不需要离线消息通知，可以不进行监听器注册。注册离线推送监听器可以通过 `TIMManager` 中的 `setOfflinePushListener` 接口进行设置。

> **注意：**
> 设置离线推送监听器，需要保证在主进程进行设置。

**原型：**

```
public void setOfflinePushListener(TIMOfflinePushListener listener)
```

**参数说明：**

参数|说明
---|---
listener|离线推送监听器，详情请参考 javadoc 中类 TIMOfflinePushListener 的说明。

**示例：**

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        Log.d("MyApplication", "app oncreate");
		// 只能在主进程进行离线推送监听器注册
        if(MsfSdkUtils.isMainProcess(this)) {
            Log.d("MyApplication", "main process");
			// 设置离线推送监听器
            TIMManager.getInstance().setOfflinePushListener(new TIMOfflinePushListener() {
                @Override
                public void handleNotification(TIMOfflinePushNotification notification) {
                    Log.d("MyApplication", "recv offline push");
					// 这里的 doNotify 是 ImSDK 内置的通知栏提醒，应用也可以选择自己利用回调参数 notification 来构造自己的通知栏提醒
                    notification.doNotify(getApplicationContext(), R.drawable.ic_launcher);
                }
            });
        }
    }
}
```

### 离线推送内容说明

离线推送的内容由类 `TIMOfflinePushNotification` 来定义，可以通过这个类对外提供的接口来获取相应的信息，并根据需要自由组合自己的通知栏提醒。

#### 获取默认通知栏标题

可以通过 `getTitle` 接口来获取默认通知栏标题。对于 **C2C 消息**，默认通知栏标题为发送方用户 ID。对于**群消息**，如果消息所在群设置了群名称，默认通知栏标题为群名称；如果该群没有设置群名称，默认通知栏标题为该群的群 ID。

**原型：**
```
public String getTitle()
```

#### 获取默认通知栏内容

可以通过 `getContent` 接口来获取默认通知栏内容。对于 **C2C 消息**， 默认通知栏内容为『消息内容』。对于**群消息**，默认通知栏内容为『发送者：消息内容』。其中『发送者』为消息发送方的群名片，如果发送方没有设置群名片，则为发送方的个人昵称，如果个人昵称也没有设置，则为发送方的用户 ID。优先级为『群名片』>『个人昵称』>『用户 ID』。其中 『消息内容』为消息体中的各个 `Elem` 进行相应转换后的字符串组合，不同类型的 `Elem`，其转换规则如下。

- 文本 Elem：直接显示内容
- 语音 Elem：显示 [语音]
- 文件 Elem：显示 [文件]
- 图片 Elem：显示 [图片]
- 自定义 Elem：显示 [desc 字段内容]

**原型：**

```
public String getContent()
```

#### 获取会话 ID

通过 `getConversationId` 可以获取到离线消息的会话 ID，失败时返回 null。对于 **C2C 消息**，会话 ID 为消息发送方用户 ID。对于**群消息**，会话 ID 为群 ID。

**原型：**
```
public String getConversationId()
```

#### 获取会话类型

通过 `getConversationType` 可以获取到离线消息的会话类型。对于 **C2C 消息**，会话类型为 `TIMConversationType.C2C`。对于**群消息**，会话类型为 `TIMConversationType.Group`。

**原型：**

```
public TIMConversationType getConversationType()
```

#### 获取发送方用户 ID

通过 `getSenderIdentifier` 可以获取到消息发送方的用户ID，失败时返回 null。

**原型：**

```
public String getSenderIdentifier()
```

#### 获取发送者昵称

通过 `getSenderNickName` 可以获取到消息发送方的昵称。对于 **C2C 消息**，返回 null。对于**群消息**，优先返回发送方的群名片，如果发送方没有设置群名片，则返回个人昵称。如果群名片和个人昵称都没有设置，则返回 null。

**原型：**

```
public String getSenderNickName()
```

#### 获取群名称

在收到群消息的时候，可以通过 `getGroupName` 获取到群名称。获取群名称，只有在收到群消息时有效，失败时返回 null。

**原型：**

```
public String getGroupName()
```

#### 获取扩展字段

收到自定义消息的时候，可以通过 `getExt` 获取到消息扩展字段。

**原型：**

```
public byte[] getExt()
```

#### 应用默认通知栏提醒

可以通过 `doNotify` 来应用 ImSDK 提供的默认通知栏提醒样式。

**原型：**

```
public void doNotify(Context context, int iconID)
```

**参数说明：**

参数|说明
---|---
context|应用上下文。
iconID|要显示在提醒中的图标的资源 ID。

## 集成小米离线推送

由于小米 ROM 深度定制了安卓系统，加强了权限的控制，第三方 App 默认不会在系统的自启动白名单里，App 在后台很容易被系统杀掉，或者用户手动将 App 杀死， 因为没有自启动权限，App 的 service 无法自动重启，从而导致被杀死后无法收到消息。为了保证 App 被杀后，在小米设备上仍然能够收消息，可以集成小米推送。目前，**SDK 仅支持推送通知栏消息**。

> 注：
>- 收到离线消息时，默认通知标题为 `a new message`。
>- 此指引文档是根据小米推送 SDKv3.0.3 来写的，可能不适用于新版本的小米推送 SDK，新版本的接入请直接参考小米官方文档。
>- 如果不需要对小米设备做专门的离线推送适配，可以忽略此章节。

### 添加小米离线推送证书

从腾讯云管理中心的 [云通信-应用列表](https://console.cloud.tencent.com/avc) 进入相应应用的【应用配置】页面，在基本配置中根据指引添加【Android推送证书】。如何获得相应的推送证书可以参考 [Android 推送证书申请](/doc/product/269/5331) 。添加证书成功后，可以得到一个证书 ID，这里可以把这个 ID 记录下来，以备后面使用。

### 配置 AndroidManifest.xml 文件

应用要集成小米推送，必须集成小米推送的客户端 SDK。可以到 [小米开放平台](http://dev.xiaomi.com/mipush/downpage/) 进行下载。下载完成后，解压，将 SDK 目录下的 `MiPush_SDK_client_**.jar` 库文件添加到自己应用的 `libs` 库目录下，并添加引用。

#### 添加小米推送必须的权限

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.VIBRATE"/>
<permission android:name="com.tencent.imsdk.permission.MIPUSH_RECEIVE" android:protectionLevel="signature" />
<!--这里 com.tencent.imsdk 改成 App 的包名-->   
<uses-permission android:name="com.tencent.imsdk.permission.MIPUSH_RECEIVE" />
<!--这里 com.tencent.imsdk 改成 App 的包名-->
```

#### 配置小米推送服务需要的 service 和 receiver

```xml
<service
  android:enabled="true"
  android:process=":pushservice"
  android:name="com.xiaomi.push.service.XMPushService"/>
<service
  android:name="com.xiaomi.push.service.XMJobService"
  android:enabled="true"
  android:exported="false"
  android:permission="android.permission.BIND_JOB_SERVICE"
  android:process=":pushservice" />
<!--注：此 service 必须在小米推送 SDK3.0.1 版本以后（包括 3.0.1 版本）加入-->
<service
  android:enabled="true"
  android:exported="true"
  android:name="com.xiaomi.mipush.sdk.PushMessageHandler" />
<service android:enabled="true"
  android:name="com.xiaomi.mipush.sdk.MessageHandleService" />
<!--注：此 service 必须在小米推送 SDK2.2.5 版本以后（包括 2.2.5 版本）加入-->
<receiver
  android:exported="true"
  android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver" >
  <intent-filter>
    <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
    <category android:name="android.intent.category.DEFAULT" />
  </intent-filter>
</receiver>
<receiver
  android:exported="false"
  android:process=":pushservice"
  android:name="com.xiaomi.push.service.receivers.PingReceiver" >
  <intent-filter>
    <action android:name="com.xiaomi.push.PING_TIMER" />
  </intent-filter>
</receiver>
```

### 自定义一个 BroadcastReceiver 类

为了可以接收到推送消息，需要自定义一个继承自 `PushMessageReceiver` 类的 `BroadcastReceiver`，并实现其中的`onNotificationMessageClicked`，`onNotificationMessageArrived`，`onReceiveRegisterResult` 方法，然后将此 receiver 注册到 AndroidManifest.xml 中。

**方法说明：**

| 方法 | 说明 |
| --- | --- |
| onNotificationMessageClicked | 用来接收服务器发来的通知栏消息（用户单击通知栏时触发） |
| onNotificationMessageArrived | 用来接收服务器发来的通知栏消息（消息到达客户端时触发，并且可以接收应用在前台时不弹出通知的通知消息） |
| onReceiveRegisterResult | 用来接受客户端向服务器发送注册命令消息后返回的响应 |

**示例：**

```java
public class MiPushMessageReceiver extends PushMessageReceiver {
    private final String TAG = "MiPushMessageReceiver";
    private String mRegId;
    @Override
    public void onNotificationMessageClicked(Context context, MiPushMessage message) {
        Log.d(TAG,"onNotificationMessageClicked is called. " + message.toString());
        Log.d(TAG, getSimpleDate() + " " + message.getContent());
    }
    @Override
    public void onNotificationMessageArrived(Context context, MiPushMessage message) {
        Log.d(TAG,"onNotificationMessageArrived is called. " + message.toString());
        Log.d(TAG, getSimpleDate() + " " + message.getContent());
    }
    @Override
    public void onReceiveRegisterResult(Context context, MiPushCommandMessage message) {
        Log.d(TAG, "onReceiveRegisterResult is called. " + message.toString());
        String command = message.getCommand();
        List<String> arguments = message.getCommandArguments();
        String cmdArg1 = ((arguments != null && arguments.size() > 0) ? arguments.get(0) : null);
        Log.d(TAG, "cmd: " + command + " | arg: " + cmdArg1
                + " | result: " + message.getResultCode() + " | reason: " + message.getReason());
        if (MiPushClient.COMMAND_REGISTER.equals(command)) {
            if (message.getResultCode() == ErrorCode.SUCCESS) {
                mRegId = cmdArg1;
            }
        }
        Log.d(TAG, "regId: " + mRegId);
    }
    @SuppressLint("SimpleDateFormat")
    private static String getSimpleDate() {
        return new SimpleDateFormat("MM-dd hh:mm:ss").format(new Date());
    }
}
```

**将自定义的 `BroadcastReceiver` 注册到 `AndroidManifest.xml`：**

```xml
<receiver
  android:exported="true"
  android:name="com.tencent.imsdk.MiPushMessageReceiver">
          <!--这里 com.tencent.imsdk.MiPushMessageReceiver 改成 App 中定义的完整类名-->
  <intent-filter>
    <action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE" />
  </intent-filter>
    <intent-filter>
    <action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED" />
  </intent-filter>
  <intent-filter>
    <action android:name="com.xiaomi.mipush.ERROR" />
  </intent-filter>
</receiver>
```


### 注册小米推送服务

如果需要启用小米离线推送需要向小米推送服务器注册推送服务。可以调用 `MiPushClient.registerPush` 来进行小米推送服务初始化。注册成功后，可以在前一节里说到的自定义 `BroadcastReceiver` 的 `onReceiveRegisterResult` 中收到注册结果。其中 `regId` 即为当前设备上当前 App 的唯一标识，这里需要把 `regId` 记录下来，以备后面使用。`MiPushClient.registerPush` 可在任意地方调用，如果在 Application 的 `onCreate` 中调用的话，需要注意的是因为 `XMPushService` 在 `AndroidManifest.xml` 中设置为运行在另外一个进程，这导致本 Application 会被实例化两次，所以我们需要让应用的主进程对推送服务进行初始化。

**示例：**

```java
public class MyApplication extends Application {
    private String MIPUSH_APPID = "your_appid";
    private String MIPUSH_APPKEY = "your_appkey";
    @Override
    public void onCreate() {
        super.onCreate();
        Log.d("MyApplication", "app oncreate");
        if(MsfSdkUtils.isMainProcess(this)) {
            Log.d("MyApplication", "main process");
            registerPush();
        }
    }
    public void registerPush(){
        String vendor = Build.MANUFACTURER;
        if(vendor.toLowerCase(Locale.ENGLISH).contains("xiaomi")) {
			//注册小米推送服务
            MiPushClient.registerPush(this, MIPUSH_APPID, MIPUSH_APPKEY);
        }else if(vendor.toLowerCase(Locale.ENGLISH).contains("huawei")) {
			//请求华为推送设备 token
            PushManager.requestToken(this);
        }
    }
}
```

### 上报证书 ID 及 regId

想要 ImSDK 通过小米推送进行离线消息推送，必须在**登录成功后**将前面步骤拿到的**证书 ID** 及 **regId** 上报到腾讯云服务器。这一步骤可以通过 `TIMManager` 中的 `setOfflinePushToken` 方法来实现。

> ** 注意：**
> 目前仅支持小米、华为设备，其他厂商设备上传无效。

**原型：**
```java
/**
 * 设置第三方推送用户标识，需登录后设置才生效
 * @param token 用户标识
 */
public void setOfflinePushToken(TIMOfflinePushToken token)
```

**参数说明：**

参数|说明
---|---
token|用户标识，包括证书 ID， regId， TMID 等

**`TIMOfflinePushToken`成员方法详细说明：**

```
/**
 * 离线推送 token 配置类，目前只适用于第三方推送接入，比如小米推送、华为推送
 */
public class TIMOfflinePushToken {
    /**
     * 设置离线推送用户标识，如小米推送的 regId 和华为推送的 TMID
     * @param token 用户标识
     */
    public void setToken(String token)
    /**
     * 设置业务 ID，这里的业务 ID 是指将离线推送相关证书上传到腾讯云的时候分配的 ID
     * @param bussid 业务 ID
     */
    public void setBussid(long bussid)
}
```

**示例：**

```java
//登录成功后，上报证书 ID 及设备 token
TIMOfflinePushToken param = new TIMOfflinePushToken();
param.setToken(token);
param.setBussid(bussId);
TIMManager.getInstance().setOfflinePushToken(param);
```

### 混淆打包

如果使用需要混淆打包应用，为了防止小米离线推送功能异常，需要添加以下混淆规则，仅供参考。**示例：**

```
#这里 com.tencent.imsdk.MiPushMessageReceiver 改成 App 中定义的完整类名
-keep com.tencent.imsdk.MiPushMessageReceiver {*;}
#可以防止一个误报的 warning 导致无法成功编译，如果编译使用的 Android 版本是 23。
-dontwarn com.xiaomi.push.**
```

## 集成华为离线推送

同小米设备一样，华为手机同样对安卓系统进行了深度定制，第三方 App 默认不会在系统的自启动白名单中，导致 App 被杀后，App 的 service 无法自动重启。为了保证 App 被杀后，在华为设备上仍然能够收到消息，需要集成华为推送。目前，**SDK 仅支持推送通知栏消息**。

>注：
>- 收到离线消息时，默认通知标题为 `a new message`。
>- 此文档是根据华为推送 SDKv2705 来编写的，可能不适用于后续的新版本推送 SDK，新版本华为推送 SDK 的接入请直接参考华为官方文档。
>- 如果不需要对华为设备做专门的离线推送适配，可以忽略此章节。

### 添加华为离线推送证书

从腾讯云管理中心的 [云通信-应用列表](https://console.cloud.tencent.com/avc) 进入相应应用的【应用配置】页面，在基本配置中根据指引添加【Android推送证书】。如何获得相应的推送证书可以参考 [Android 推送证书申请](/doc/product/269/5331)。添加证书成功后，可以得到一个证书 ID，这里可以把这个 ID 记录下来，以备后面使用。

### 配置 AndroidManifest.xml 文件

应用要集成华为推送，必须集成华为推送的客户端 SDK，可以到 [华为开发者中心](http://developer.huawei.com/consumer/cn/service/hms/catalog/huaweipush.html?page=hmssdk_huaweipush_sdkdownload) 进行下载。下载完成后，解压，将 `libs` 目录中的 `HwPush_SDK_V**.jar` 库文件添加到自己应用的 `libs` 库目录下，并添加引用。

#### 添加华为推送必须的权限

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

#### 配置化为推送服务需要的 service 和 receiver

```xml
<!-- 备注：Push 相关的 Android 组件需要添加到业务的 AndroidManifest.xml,
	 Push 相关 Android 组件运行在另外一个进程是为了防止 Push 服务异常而影响主业务 -->
<!-- PushSDK:PushSDK 接收外部请求事件入口 -->
<receiver
	android:name="com.huawei.android.pushagent.PushEventReceiver"
	android:process=":pushservice" >
	<intent-filter>
		<action android:name="com.huawei.android.push.intent.REFRESH_PUSH_CHANNEL" />
		<action android:name="com.huawei.intent.action.PUSH" />
		<action android:name="com.huawei.intent.action.PUSH_ON" />
		<action android:name="com.huawei.android.push.PLUGIN" />
	</intent-filter>
</receiver>
<receiver
	android:name="com.huawei.android.pushagent.PushBootReceiver"
	android:process=":pushservice" >
	<intent-filter>
		<action android:name="com.huawei.android.push.intent.REGISTER" />
	</intent-filter>
	<meta-data
		android:name="CS_cloud_version"
		android:value="\u0032\u0037\u0030\u0035" />
</receiver>
<!-- PushSDK:Push 服务 -->
<service
	android:name="com.huawei.android.pushagent.PushService"
	android:process=":pushservice" >
</service>
```

### 自定义一个 BroadcastReceiver 类

为了可以接收到推送消息，需要自定义一个继承自 `PushEventReceiver` 类的 `BroadcastReceiver`，并实现其中的 `onToken`，`onPushMsg`，`onEvent` 方法，然后将此 receiver 注册到 `AndroidManifest.xml` 中。

**示例：**

```java
public class HwPushMessageReceiver extends PushEventReceiver{
	private final String TAG = "HwPushMessageReceiver";
	private String mToken = "";
	@Override
	public void onToken(Context context, String token, Bundle extras){
		String belongId = extras.getString("belongId");
		String content = "获取token和belongId成功，token = " + token + ",belongId = " + belongId;
		mToken = token;
		Log.e(TAG, content);
	}
	@Override
	public boolean onPushMsg(Context context, byte[] msg, Bundle bundle) {
		try {
			String content = "收到一条Push消息： " + new String(msg, "UTF-8");
			Log.e(TAG, content);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return false;
	}
	@Override
	public void onEvent(Context context, Event event, Bundle extras) {
		if (Event.NOTIFICATION_OPENED.equals(event) || Event.NOTIFICATION_CLICK_BTN.equals(event)) {
			int notifyId = extras.getInt(BOUND_KEY.pushNotifyId, 0);
			if (0 != notifyId) {
				NotificationManager manager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
				manager.cancel(notifyId);
			}
			String content = "收到通知附加消息： " + extras.getString(BOUND_KEY.pushMsgKey);
			Log.e(TAG, content);
		}
	}
}
```

**将自定义的 `BroadcastReceiver` 注册到 `AndroidManifest.xml`：**

```xml
<!-- 第三方相关 :接收 Push 消息（注册、Push 消息、Push 连接状态、标签，LBS 上报结果）广播 -->
<receiver android:name="com.tencent.imsdk.test.HwPushMessageReceiver" >
	<intent-filter>
		<!-- 必须,用于接收 token-->
		<action android:name="com.huawei.android.push.intent.REGISTRATION" />
		<!-- 必须，用于接收消息-->
		<action android:name="com.huawei.android.push.intent.RECEIVE" />
		<!-- 可选，用于单击通知栏或通知栏上的按钮后触发 onEvent 回调-->
		<action android:name="com.huawei.android.push.intent.CLICK" />
		<!-- 可选，查看 push 通道是否连接，不查看则不需要-->
		<action android:name="com.huawei.intent.action.PUSH_STATE" />
		<!-- 可选，标签、地理位置上报回应，不上报则不需要 -->
		<action android:name="com.huawei.android.push.plugin.RESPONSE" />
	</intent-filter>
	<meta-data android:name="CS_cloud_ablitity" android:value="successRateAnalytics"/>
</receiver>
```

### 获取设备 token

通过调用 `PushManager.requestToken` 方法向华为推送平台请求当前应用在当前设备上的唯一标识。请求成功后，可以在前面自定义的 `BroadcastReceiver` 的 `onToken` 回调中获取分配的 token。把这个 token 记录下来，以备后面使用。`PushManager.requestToken` 可在任意地方调用，如果在 Application 的 `onCreate` 中调用的话，需要注意的是因为 `XMPushService` 在 `AndroidManifest.xml` 中设置为运行在另外一个进程，这导致本 Application 会被实例化两次，所以我们需要让应用的主进程对推送服务进行初始化。

**示例：**

```java
public class MyApplication extends Application {
    private String MIPUSH_APPID = "your_appid";
    private String MIPUSH_APPKEY = "your_appkey";
    @Override
    public void onCreate() {
        super.onCreate();
        Log.d("MyApplication", "app oncreate");
        if(MsfSdkUtils.isMainProcess(this)) {
            Log.d("MyApplication", "main process");
            registerPush();
        }
    }
    public void registerPush(){
        String vendor = Build.MANUFACTURER;
        if(vendor.toLowerCase(Locale.ENGLISH).contains("xiaomi")) {
			//注册小米推送服务
            MiPushClient.registerPush(this, MIPUSH_APPID, MIPUSH_APPKEY);
        }else if(vendor.toLowerCase(Locale.ENGLISH).contains("huawei")) {
			//请求华为推送设备 token
            PushManager.requestToken(this);
        }
    }
}
```

### 上报证书 ID 及设备 token

想要 ImSDK 通过华为推送进行离线消息推送，必须在**登录成功后**将前面步骤拿到的**证书 ID** 及**设备 token** 上报到腾讯云服务器。这一步骤可以通过 `TIMManager` 中的 `setOfflinePushToken` 方法来实现。

> **注意：**
> 目前仅支持小米、华为设备，其他厂商设备上传无效。

**原型：**

```
/**
 * 设置第三方推送用户标识，需登录后设置才生效
 * @param token 用户标识
 */
public void setOfflinePushToken(TIMOfflinePushToken token)
```

**参数说明：**

参数|说明
---|---
token|用户标识，包括证书 ID， regId， TMID 等

**`TIMOfflinePushToken` 成员方法详细说明：**

```java
/**
 * 离线推送 token 配置类，目前只适用于第三方推送接入，比如小米推送、华为推送
 */
public class TIMOfflinePushToken {
    /**
     * 设置离线推送用户标识，如小米推送的 regId 和华为推送的 TMID
     * @param token 用户标识
     */
    public void setToken(String token)
    /**
     * 设置业务 ID，这里的业务 ID 是指将离线推送相关证书上传到腾讯云的时候分配的 ID
     * @param bussid 业务 ID
     */
    public void setBussid(long bussid)
}
```

**示例：**

```
//登录成功后，上报证书 ID 及设备 token
TIMOfflinePushToken param = new TIMOfflinePushToken();
param.setToken(token);
param.setBussid(bussId);
TIMManager.getInstance().setOfflinePushToken(param);
```

### 混淆打包

如果需要混淆打包应用，为了防止华为离线推送功能异常，需要添加以下混淆规则，仅供参考。**示例：**

```
-keep class com.huawei.android.pushagent.**{*;}
-keep class com.huawei.android. pushselfshow.**{*;}
-keep class com.huawei.android. microkernel.**{*;}
-keep class com.baidu.mapapi.**{*;}
```

## 集成魅族离线推送

魅族推送（Push）是魅族公司向开发者提供的消息推送服务，通过在云端与客户端之间建立一条稳定，可靠的长连接，为开发者提供向客户端应用实时推送消息的服务，通过推送消息，魅族推送服务能有效地帮助开发者拉动用户活跃度，改善产品体验。只能在 Flyme OS 的设备上使用。为了保证 App 被杀后，在魅族设备上仍然能够收到消息，需要集成魅族推送。目前，**SDK 仅支持推送通知栏消息**。

> 注：
>- 收到离线消息时，默认通知标题为 `a new message`。
>- 魅族官方建议在 Flyme OS 5.0 以上设备上获得最佳效果。
>- 此文档是根据魅族推送 PushSDK3.6 来编写的，可能不适用于后续的新版本推送 SDK，新版本推送 SDK 的接入请直接参考 [魅族官方接入文档](https://github.com/MEIZUPUSH/PushDemo)。
>- 如果不需要对华为设备做专门的离线推送适配，可以忽略此章节。

### 添加魅族离线推送证书

从腾讯云管理中心的 [云通信-应用列表](https://console.cloud.tencent.com/avc) 进入相应应用的【应用配置】页面，在基本配置中根据指引添加【Android推送证书】。如何获得相应的推送证书可以参考 [Android推送证书申请](/doc/product/269/5331)。添加证书成功后，可以得到一个证书 ID，这里可以把这个 ID 记录下来，以备后面使用。

### PushSDK 引用配置

集成魅族推送，需要引入魅族推送 SDK，目前魅族推荐使用 gradle 的方式引用 aar。需要在 `buld.gradle` 里添加以下语句。

```
dependencies {
    compile 'com.meizu.flyme.internet:push-internal:3.6.+@aar'
}
```

> 注：如果您需要使用 JAR，请参考 [Eclipse 接入方式](https://comsince.github.io/2017/02/21/mzpushsdk-eclipse/)。

### 兼容 Flyme 5.0 以下版本推送兼容配置

因为魅族推送在 Flyme 5.0 以上系统的设备上才会有最佳的效果，但是也可能存在系统版本比较低的设备，所以可以做一下相应的兼容，以最大概率保证正常收到推送。

> 注：Flyme 5.0 以下的系统无法保证 100% 可以收到消息推送。

**在 `AndroidManifest.xml` 中添加以下配置：**

```
  <!-- 兼容 Flyme5.0 以下版本，魅族内部集成 pushSDK 必填，不然无法收到消息-->
  <uses-permission android:name="com.meizu.flyme.push.permission.RECEIVE"></uses-permission>
  <permission android:name="包名.push.permission.MESSAGE" android:protectionLevel="signature"/>
  <uses-permission android:name="包名.push.permission.MESSAGE"></uses-permission>
  <!--  兼容 Flyme3.0 配置权限-->
  <uses-permission android:name="com.meizu.c2dm.permission.RECEIVE" />
  <permission android:name="您的包名.permission.C2D_MESSAGE"
                    android:protectionLevel="signature"></permission>
  <uses-permission android:name="您的包名.permission.C2D_MESSAGE"/>
```

### 自定义 BroadcastReceiver 类

想要接收到离线推送的消息，需要自定义一个继承 `MzPushMessageReceiver` 的 `BroadcastReceiver`， 并实现其中的几个相关的接口，主要关注 `onRegisterStatus` 和 `onNotificationClicked` 两个接口。然后将此 receiver 注册到 `AndroidManifest.xml` 中。

```java
public class MyPushMsgReceiver extends MzPushMessageReceiver {
    private static final String TAG = MeizuPushMessageReceiver.class.getSimpleName();
    private static final int busiid = 3443;
    /**
     * 已废弃接口，不建议使用
     */
    @Override
    public void onRegister(Context context, String pushId) {
    }
    /**
     * 已废弃接口，不建议使用
     */
    @Override
    public void onUnRegister(Context context, boolean success) {
    }
    /**
     * Push 开关状态回调
     */
    @Override
    public void onPushStatus(Context context, PushSwitchStatus pushSwitchStatus) {
    }
    /**
     * 订阅状态回调, 可以在这个接口获取 PushId
     */
    @Override
    public void onRegisterStatus(Context context, RegisterStatus registerStatus) {
        Log.d(TAG, "pushId: " + registerStatus.getPushId() + "|Expiretime: " + registerStatus.getExpireTime() + "|str: " + registerStatus.toString());
        //上报 busiid 和 pushid 到腾讯云，需要在登录成功后进行上报
        TIMOfflinePushToken token = new TIMOfflinePushToken();
        token.setBussid(busiid);
        token.setToken(registerStatus.getPushId());
        TIMManager.getInstance().setOfflinePushToken(token, new TIMCallBack() {
            @Override
            public void onError(int i, String s) {
                Log.e(TAG, "setOfflinePushToken failed, code: " + i + "|msg: " + s);
            }
            @Override
            public void onSuccess() {
                Log.i(TAG, "setOfflinePushToken succ");
            }
        });
    }
    /**
     * 反订阅回调
     */
    @Override
    public void onUnRegisterStatus(Context context, UnRegisterStatus unRegisterStatus) {
    }
    /**
     * 标签状态回调
     */
    @Override
    public void onSubTagsStatus(Context context, SubTagsStatus subTagsStatus) {
    }
    /**
     * 别名状态回调
     */
    @Override
    public void onSubAliasStatus(Context context, SubAliasStatus subAliasStatus) {
    }
    /**
     * 通知栏单击回调
     */
    @Override
    public void onNotificationClicked(Context context, MzPushMessage mzPushMessage) {
        // 消息正文内容
        String content = mzPushMessage.getContent();
        // 消息扩展内容
        String ext = mzPushMessage.getSelfDefineContentString();
        Log.i(TAG, "onNotificationClicked content: " + content + "|selfDefined ext: " + ext);
    }
}
```

**将这个自定义的 `BroadcastReceiver` 注册到 `AndroidManifest.xml` 中：**

```xml
<!--mz push-->
<!-- push 应用定义消息 receiver 声明 -->
<receiver android:name="包名.MyPushMsgReceiver">
    <intent-filter>
        <!-- 接收 push 消息 -->
        <action android:name="com.meizu.flyme.push.intent.MESSAGE" />
        <!-- 接收 register 消息 -->
        <action android:name="com.meizu.flyme.push.intent.REGISTER.FEEDBACK" />
        <!-- 接收 unregister 消息-->
        <action android:name="com.meizu.flyme.push.intent.UNREGISTER.FEEDBACK"/>
        <!-- 兼容低版本 Flyme3 推送服务配置 -->
        <action android:name="com.meizu.c2dm.intent.REGISTRATION" />
        <action android:name="com.meizu.c2dm.intent.RECEIVE" />
        <category android:name="包名"></category>
    </intent-filter>
</receiver>
```

### 注册魅族推送服务

以上步骤都已经准备好了之后，就可以**在登录 IM 成功**后，开始向魅族服务器注册魅族推送服务了。注册魅族推送服务需要调用魅族 PushSDK 提供的 `register` 方法。

> **注意：**
>  魅族推送只适用于 Flyme 系统，因此可以先行判断是否为魅族机型，再进行订阅，避免在其他机型上出现兼容性问题。

```java
//魅族推送只适用于 Flyme 系统,因此可以先行判断是否为魅族机型，再进行订阅，避免在其他机型上出现兼容性问题
if(MzSystemUtils.isBrandMeizu()){
    com.meizu.cloud.pushsdk.PushManager.register(this, APP_ID, APP_KEY);
}
```

### 上报证书 ID 及设备 token

如果注册魅族推送服务成功，则会通过之前自定义 `BroadcastReceiver` 的 `onRegisterStatus` 接口回调当前设备的 `PushId` 等信息。这个时候就已经可以收到魅族推送控制台进行推送的消息了。不需要如果想要收到腾讯云推送的消息，还需要最后一步，就是上报证书 ID 和设备 token（这里设备 token 就是回调中的 PushId）。

**示例：**

```java
/*
* 订阅状态回调, 可以在这个接口获取 PushId，并进行上报
*/
@Override
public void onRegisterStatus(Context context, RegisterStatus registerStatus) {
    Log.d(TAG, "pushId: " + registerStatus.getPushId() + "|Expiretime: " + registerStatus.getExpireTime() + "|str: " + registerStatus.toString());
    //上报 busiid 和 pushid 到腾讯云，需要在登录成功后进行上报
    TIMOfflinePushToken token = new TIMOfflinePushToken();
    token.setBussid(busiid);
    token.setToken(registerStatus.getPushId());
    TIMManager.getInstance().setOfflinePushToken(token, new TIMCallBack() {
        @Override
        public void onError(int i, String s) {
            Log.e(TAG, "setOfflinePushToken failed, code: " + i + "|msg: " + s);
        }
        @Override
        public void onSuccess() {
            Log.i(TAG, "setOfflinePushToken succ");
        }
    });
}
```
