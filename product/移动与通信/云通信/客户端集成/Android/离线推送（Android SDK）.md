## 1 概述
这里的离线指的是应用在没有退出登录的情况下，被系统或者用户杀掉。在这种情况下，如果还想收到ImSDK的消息提醒，可以集成云通信离线推送。

另外，ImSDK 从 2.1.0 版本开始，提供了适配小米、华为离线推送的方案。

> 注意
> 1. 对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。
> 2. 目前，离线推送只提供 [普通聊天消息](/doc/product/269/%E6%B6%88%E6%81%AF%E6%94%B6%E5%8F%91%EF%BC%88Android%20SDK%EF%BC%89#1-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 进行消息提醒，暂不提供对 [系统消息](/doc/product/269/消息收发（Android%20SDK）#5-.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF) 的消息提醒 。



## 2 设置离线推送配置

### 2.1 设置全局离线推送配置

ImSDK从2.1.0版本开始提供了设置全局离线推送配置的功能，可以设置是否开启离线推送、收到离线推送时的提示声音等。

这个设置方法是由`TIMManager`提供的`configOfflinePushSettings`。

>注意：
>1. 必须在登录成功后调用才生效。
>2. 目前仅支持应用内置的声音文件。

**原型 ：**
```
/**
 * 初始化离线推送配置，需登录后设置才生效
 * @param settings 离线推送配置信息
 */
public void configOfflinePushSettings(TIMOfflinePushSettings settings)

/**
 * 从服务器获取离线推送配置，需登录后才能获取
 * @param cb 回调，在onSuccess的参数中返回离线推送配置
 */
public void getOfflinePushSettings(final TIMValueCallBack<TIMOfflinePushSettings> cb)
```

**参数说明：**

参数|说明
---|---
settings|离线推送配置

`TIMOfflinePushSettings`说明：
```
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
 * 获取收到c2c消息的离线推送时的提醒声音
 * @return 声音文件的URI，没有设置时返回null
 */
public Uri getC2cMsgRemindSound()

/**
 * 设置收到c2c消息的离线推送时的提醒声音
 * @param c2cMsgRemindSound 声音文件的URI，恢复系统默认声音填null
 */
public void setC2cMsgRemindSound(Uri c2cMsgRemindSound)

/**
 * 获取收到群消息的离线推送时的提醒声音
 * @return 声音文件的URI，没有设置时返回null
 */
public Uri getGroupMsgRemindSound()

/**
 * 设置收到群消息的离线推送时的提醒声音
 * @param groupMsgRemindSound 声音文件的URI， 恢复系统默认声音填null
 */
public void setGroupMsgRemindSound(Uri groupMsgRemindSound)
```

**示例：**
```
TIMOfflinePushSettings settings = new TIMOfflinePushSettings();
//开启离线推送
settings.setEnabled(true);
//设置收到C2C离线消息时的提示声音，这里把声音文件放到了res/raw文件夹下
settings.setC2cMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));
//设置收到群离线消息时的提示声音，这里把声音文件放到了res/raw文件夹下
settings.setGroupMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));

TIMManager.getInstance().configOfflinePushSettings(settings);
```

### 2.2 设置单条消息的离线推送配置

ImSDK从2.2.0版本开始提供针对单独每一条消息进行离线推送配置的功能。开发者可以针对某条消息设置是否开启离线推送、收到离线推送后提醒声音、离线推送消息描述及扩展字段等。

>注意：
>1. 针对单条消息设置的离线推送配置优先级是最高的，也就是在同时设置了全局离线推送配置及单条消息离线推送配置的情况下，将以单条消息离线推送配置为准。
>2. 目前Android设备的声音仅支持应用内置的声音文件。
>3. 此章节是根据ImSDK 2.5.3来说明的，在接入低于2.5.3版本的ImSDK时，单条消息的离线推送配置请参考SDK下载包中的javadoc进行配置。

**原型：**
```
/**
 * 设置当前消息在对方收到离线推送的时候的配置（可选，发送消息时设置）
 * @param settings 离线推送配置
 */
public void setOfflinePushSettings(TIMMessageOfflinePushSettings settings)

/**
 * 获取当前消息的离线推送配置
 * @return 离线推送配置，如果发送方没有设置的情况下，返回null
 */
public TIMMessageOfflinePushSettings getOfflinePushSettings()
```

其中,
**`TIMMessageOfflinePushSettings`：**

```
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
 * @return 扩展字段内容，没有设置返回null
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
 * 获取当前消息在Android设备上的离线推送配置
 * @return Android设备上的离线推送配置
 */
public AndroidSettings getAndroidSettings()

/**
 * 设置当前消息在Android设备上的离线推送配置（可选，发送消息时设置）
 * @param androidSettings 当前消息在Android设备上的离线推送配置
 */
public void setAndroidSettings(AndroidSettings androidSettings)

/**
 * 获取当前消息在IOS设备上的离线推送配置
 * @return IOS设备上的离线推送配置
 */
public IOSSettings getIosSettings()

/**
 * 设置当前消息在IOS设备上的离线推送配置（可选，发送消息时设置）
 * @param iosSettings 当前消息在IOS设备上的离线推送配置
 */
public void setIosSettings(IOSSettings iosSettings)

```

**`TIMMessageOfflinePushSettings.AndroidSettings`：**
```
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
 * 获取当前消息在Android设备上的离线推送提示声音URI
 * @return 声音URI，没有设置则返回null
 */
public Uri getSound()

/**
 * 设置当前消息在Android设备上的离线推送提示声音（可选，发送消息时设置）
 * @param sound 声音URI，仅支持应用内部的声音资源文件
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

**`TIMMessageOfflinePushSettings.NotifyMode`:**

`NotifyMode`只是针对第三方离线推送进行设置的，比如小米、华为的离线推送。

```
/**
 * 普通通知栏消息模式，离线消息下发后，点击通知栏消息直接启动应用，不会给应用进行回调
 */
NotifyMode.Normal

/**
 * 自定义消息模式，离线消息下发后，点击通知栏消息会给应用进行回调
 */
NotifyMode.Custom
```

**`TIMMessageOfflinePushSettings.IOSSettings`：**
```
/**
 * 获取当前消息在IOS设备上的离线推送提示声音
 * @return 声音文件路径，没有设置则返回null
 */
public String getSound()

/**
 * 设置当前消息在IOS设备上的离线推送提示声音（可选，发送消息时设置）
 * @param sound 声音文件路径，当设置为{@see IOSSettings#NO_SOUND_NO_VIBRATION}时表示无提示音无振动
 */
public void setSound(String sound)

/**
 * 获取当前消息是否开启Badge计数
 * @return true - 当前消息开启Badge计数
 */
public boolean isBadgeEnabled()

/**
 * 设置当前消息是否开启Badge计数，默认开启（可选，发送消息时设置）
 * @param badgeEnabled 否开启Badge计数
 */
public void setBadgeEnabled(boolean badgeEnabled)
```

**示例：**
```
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

//设置在Android设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.AndroidSettings androidSettings = new TIMMessageOfflinePushSettings.AndroidSettings();
//ImSDK 2.5.3之前的构造方式
//TIMMessageOfflinePushSettings.AndroidSettings androidSettings = settings.new AndroidSettings();
androidSettings.setTitle("I'm title");
//推送自定义通知栏消息，接收方收到消息后点击通知栏消息会给应用回调（针对小米、华为离线推送）
androidSettings.setNotifyMode(TIMMessageOfflinePushSettings.NotifyMode.Custom);
//设置android设备收到消息时的提示音，声音文件需要放置到raw文件夹
androidSettings.setSound(Uri.parse("android.resource://" + getPackageName() + "/" +R.raw.hualala));
settings.setAndroidSettings(androidSettings);

//设置在IOS设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.IOSSettings iosSettings = new TIMMessageOfflinePushSettings.IOSSettings();
//ImSDK 2.5.3之前的构造方式
//TIMMessageOfflinePushSettings.IOSSettings iosSettings = settings.new IOSSettings();

//开启Badge计数
iosSettings.setBadgeEnabled(true);  
//设置ios收到消息时没有提示音且不振动（ImSDK 2.5.3新增特性）
//iosSettings.setSound(TIMMessageOfflinePushSettings.IOSSettings.NO_SOUND_NO_VIBRATION);
//设置IOS设备收到离线消息时的提示音
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
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }

    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.d(tag, "SendMsg ok! peer:" + peer );
    }
});

```

## 3 集成云通信离线推送

ImSDK 从1.8.0版本开始提供了离线推送的功能。

因为离线推送依赖于守护进程，所以为了保证离线推送的正常运作，需要对应用的**自启动权限**进行授权，而部分对Android系统进行了深度定制化的机型（华为、小米等）则需要将应用添加到应用白名单，保证应用被杀掉后，守护进程可以自动重启。

### 3.1 配置AndroidManifest
由于ImSDK的离线推送依赖于服务，所以需要应用在AndroidManifest.xml的`<application></application>`中添加以下配置：
```
<!--  消息收发service -->
<service
    android:name="com.tencent.qalsdk.service.QalService"
    android:exported="false" 
    android:process=":QALSERVICE" >  
</service> 
<!--  消息收发辅助service -->
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
### 3.2 设置离线推送处理
#### 3.2.1 实现自己的Application类
实现android.app.Application，假设命名为MyApplication，在AndroidManifes.xml中配置实现：
```
<!-- 应用在实现的时候请将com.tencent.imsdk.test.MyApplication替换为自己的Application -->
<application
	android:allowBackup="true"
	android:icon="@drawable/ic_launcher"
	android:label="@string/app_name"
	android:name="com.tencent.imsdk.test.MyApplication">
	
	<!-- 这里省略其他各种配置 -->
	
</application>
```

#### 3.2.2 注册离线推送监听器
在以上的准备做好后，必须注册相应的离线推送监听器才能收到消息通知。如果不需要离线消息通知，可以不进行监听器注册。
注册离线推送监听器可以通过`TIMManager`中的`setOfflinePushListener`接口进行设置。

**原型：**
```
public void setOfflinePushListener(TIMOfflinePushListener listener)
```
设置离线推送监听器，**需要保证在主进程进行设置**。

**参数说明：**

参数|说明
---|---
listener|离线推送监听器，详情请参考javadoc中类TIMOfflinePushListener的说明。

**示例：**
```
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
										
					// 这里的doNotify是ImSDK内置的通知栏提醒，应用也可以选择自己利用回调参数notification来构造自己的通知栏提醒
                    notification.doNotify(getApplicationContext(), R.drawable.ic_launcher);
                }
            });
        }
    }
}
```

### 3.3 离线推送内容说明
离线推送的内容由类`TIMOfflinePushNotification`来定义，可以通过这个类对外提供的接口来获取相应的信息，并根据需要自由组合自己的通知栏提醒。

#### 3.3.1 获取默认通知栏标题
可以通过`getTitle`接口来获取默认通知栏标题。

对于C2C消息，默认通知栏标题为发送方用户ID。

对于群消息，如果消息所在群设置了群名称，默认通知栏标题为群名称；如果该群没有设置群名称，默认通知栏标题为该群群ID。

**原型：**
```
public String getTitle()
```
获取默认通知栏标题。


#### 3.3.2 获取默认通知栏内容
可以通过`getContent`接口来获取默认通知栏内容。

对于C2C消息， 默认通知栏内容为：
```
消息内容
```
对于群消息，默认通知栏内容为：
```
发送者： 消息内容
```
其中`发送者`为消息发送方的群名片，如果发送方没有设置群名片，则为发送方的个人昵称，如果个人昵称也没有设置，则为发送方的用户ID。优先级为群名片 > 个人昵称 > 用户ID。

其中`消息内容`为消息体中的各个Elem进行相应转换后的字符串组合，不同类型的Elem，其转换规则如下：

- 文本Elem：直接显示内容
- 语音Elem：显示 [语音]
- 文件Elem：显示 [文件]
- 图片Elem：显示 [图片]
- 自定义Elem：显示 [desc字段内容]

**原型：**
```
public String getContent()
```
获取默认通知栏内容。

#### 3.3.3 获取会话ID
通过`getConversationId`可以获取到离线消息的会话ID。

对于C2C消息，会话ID为消息发送方用户ID；对于群消息，会话ID为群ID。

**原型：**
```
public String getConversationId()
```
获取会话ID，失败时返回null。

#### 3.3.4 获取会话类型

通过`getConversationType`可以获取到离线消息的会话类型。

对于C2C消息，会话类型为`TIMConversationType.C2C`；对于群消息，会话类型为`TIMConversationType.Group`。

**原型：**
```
public TIMConversationType getConversationType()
```
获取会话类型。

#### 3.3.5 获取发送方用户ID

通过`getSenderIdentifier`可以获取到消息发送方的用户ID。

**原型：**
```
public String getSenderIdentifier()
```
获取发送方用户ID，失败时返回null。

#### 3.3.6 获取发送者昵称
通过`getSenderNickName`可以获取到消息发送方的昵称。

对于C2C消息，返回null。

对于群消息，优先返回发送方的群名片，如果发送方没有设置群名片，则返回个人昵称。如果群名片和个人昵称都没有设置，则返回null。

**原型：**
```
public String getSenderNickName()
```
获取发送方昵称/群名片（群消息时，优先返回群名片，当没有群名片时，返回昵称）。

#### 3.3.7 获取群名称
在收到群消息的时候，可以通过`getGroupName`获取到群名称。

**原型：**
```
public String getGroupName()
```
获取群名称，只有在收到群消息时有效，失败时返回null。

#### 3.3.8 获取扩展字段
收到自定义消息的时候，可以通过`getExt`获取到消息扩展字段。

**原型：**
```
public byte[] getExt()
```
获取自定义消息对应的ext字段。

#### 3.3.9 应用默认通知栏提醒
可以通过`doNotify`来应用ImSDK提供的默认通知栏提醒样式。

**原型：**
```
public void doNotify(Context context, int iconID)
```
应用默认通知栏提醒。

**参数说明：**

参数|说明
---|---
context|应用上下文。
iconID|要显示在提醒中的图标的资源ID。

## 4 集成小米离线推送

由于小米ROM深度定制了安卓系统，加强了权限的控制，第三方APP默认不会在系统的自启动白名单里，APP在后台很容易被系统杀掉，或者用户手动将APP杀死， 因为没有自启动权限，APP的service无法自动重启，从而导致被杀死后无法收到消息。

为了保证APP被杀后，在小米设备上仍然能够收消息，可以集成小米推送。目前，**SDK仅支持推送通知栏消息**。

>注：
1. 收到离线消息时，默认通知标题为`a new message`。
2. 如果不需要对小米设备做专门的离线推送适配，可以忽略此章节。

### 4.1 添加小米离线推送证书

从腾讯云管理中心的 [云通信-应用列表](https://console.qcloud.com/avc) 进入相应应用的`应用配置`页面，在基本配置中根据指引添加`Android推送证书`。如何获得相应的推送证书可以参考 [Android推送证书申请](/doc/product/269/5331) 。

添加证书成功后，可以得到一个证书ID，这里可以把这个ID记录下来，后边有用。

### 4.2 配置AndroidManifest.xml文件

应用要集成小米推送，必须集成小米推送的客户端SDK。可以到 [小米开放平台](http://dev.xiaomi.com/mipush/downpage/) 进行下载。下载完成后，解压，将SDK目录下的`MiPush_SDK_client_**.jar`库文件添加到自己应用的`libs`库目录下，并添加引用。

#### 4.2.1 添加小米推送必须的权限

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.VIBRATE"/>
<permission android:name="com.tencent.imsdk.permission.MIPUSH_RECEIVE" android:protectionLevel="signature" />
<!--这里com.tencent.imsdk改成app的包名-->   
<uses-permission android:name="com.tencent.imsdk.permission.MIPUSH_RECEIVE" />
<!--这里com.tencent.imsdk改成app的包名-->
```

#### 4.2.2 配置小米推送服务需要的service和receiver

```
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
<!--注：此service必须在小米推送SDK3.0.1版本以后（包括3.0.1版本）加入-->
<service
  android:enabled="true"
  android:exported="true"
  android:name="com.xiaomi.mipush.sdk.PushMessageHandler" /> 
<service android:enabled="true"
  android:name="com.xiaomi.mipush.sdk.MessageHandleService" /> 
<!--注：此service必须在小米推送SDK2.2.5版本以后（包括2.2.5版本）加入-->
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

### 4.3 自定义一个BroadcastReceiver类

为了可以接收到推送消息，需要自定义一个继承自 `PushMessageReceiver`类的`BroadcastReceiver`，并实现其中的`onNotificationMessageClicked`，`onNotificationMessageArrived`，`onReceiveRegisterResult`方法，然后将此receiver注册到AndroidManifest.xml中。其中`onNotificationMessageClicked`用来接收服务器发来的通知栏消息（用户点击通知栏时触发），`onNotificationMessageArrived`用来接收服务器发来的通知栏消息（消息到达客户端时触发，并且可以接收应用在前台时不弹出通知的通知消息），`onReceiveRegisterResult`用来接受客户端向服务器发送注册命令消息后返回的响应。

**示例：**

```
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

将自定义的BroadcastReceiver注册到AndroidManifest.xml。
```
<receiver
  android:exported="true"
  android:name="com.tencent.imsdk.MiPushMessageReceiver">
          <!--这里com.tencent.imsdk.MiPushMessageReceiver改成app中定义的完整类名-->
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


### 4.4 注册小米推送服务

如果需要启用小米离线推送需要向小米推送服务器注册推送服务。可以调用`MiPushClient.registerPush`来进行小米推送服务初始化。注册成功后，可以在前一节里说到的自定义`BroadcastReceiver`的`onReceiveRegisterResult`中收到注册结果。其中regId即为当前设备上当前app的唯一标识，这里需要把regId记录下来，后边有用。

`MiPushClient.registerPush`可在任意地方调用，如果在Application的onCreate中调用的话，需要注意的是因为`XMPushService`在AndroidManifest.xml中设置为运行在另外一个进程，这导致本Application会被实例化两次，所以我们需要让应用的主进程对推送服务进行初始化。

**示例：**
```
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
			//请求华为推送设备token
            PushManager.requestToken(this);
        }
    }
}
```

### 4.5 上报证书ID及regId

想要ImSDK通过小米推送进行离线消息推送，必须在**登录成功后**将前面步骤拿到的**证书ID**及**regId**上报到腾讯云服务器。这一步骤可以通过`TIMManager`中的`setOfflinePushToken`方法来实现。

**目前仅支持小米、华为设备，其他厂商设备上传无效。**

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
token|用户标识，包括证书ID， regId， TMID等

`TIMOfflinePushToken`成员方法详细说明：
```
/**
 * 离线推送token配置类，目前只适用于第三方推送接入，比如小米推送、华为推送
 */
public class TIMOfflinePushToken {
    /**
     * 设置离线推送用户标识，如小米推送的regId和华为推送的TMID
     * @param token 用户标识
     */
    public void setToken(String token)
		
    /**
     * 设置业务ID，这里的业务ID是指将离线推送相关证书上传到腾讯云的时候分配的ID
     * @param bussid 业务ID
     */
    public void setBussid(long bussid)
}
```

**示例：**
```
//登录成功后，上报证书ID及设备token
TIMOfflinePushToken param = new TIMOfflinePushToken();
param.setToken(token);
param.setBussid(bussId);
TIMManager.getInstance().setOfflinePushToken(param);
```

### 4.6 混淆打包

如果使用需要混淆打包应用，为了防止小米离线推送功能异常，需要添加以下混淆规则，仅供参考。
```
#这里com.tencent.imsdk.MiPushMessageReceiver改成app中定义的完整类名
-keep com.tencent.imsdk.MiPushMessageReceiver {*;}
#可以防止一个误报的 warning 导致无法成功编译，如果编译使用的 Android 版本是 23。
-dontwarn com.xiaomi.push.**
```

## 5 集成华为离线推送

同小米设备一样，华为手机同样对安卓系统进行了深度定制，第三方APP默认不会在系统的自启动白名单中，导致APP被杀后，APP的service无法自动重启。

为了保证APP被杀后，在华为设备上仍然能够收到消息，需要集成华为推送。目前，**SDK仅支持推送通知栏消息**。

>注：
1. 收到离线消息时，默认通知标题为`a new message`。
2. 如果不需要对华为设备做专门的离线推送适配，可以忽略此章节。

### 5.1 添加华为离线推送证书

从腾讯云管理中心的 [云通信-应用列表](https://console.qcloud.com/avc) 进入相应应用的`应用配置`页面，在基本配置中根据指引添加`Android推送证书`。如何获得相应的推送证书可以参考 [Android推送证书申请](/doc/product/269/5331)。

添加证书成功后，可以得到一个证书ID，这里可以把这个ID记录下来，后边有用。

### 5.2 配置AndroidManifest.xml文件

应用要集成华为推送，必须集成华为推送的客户端SDK，可以到 [华为开发者中心](http://developer.huawei.com/cn/consumer/wiki/index.php?title=PushSDK%E4%B8%8B%E8%BD%BD) 进行下载。下载完成后，解压，将libs目录中的`HwPush_SDK_V**.jar`库文件添加到自己应用的`libs`库目录下，并添加引用。

#### 5.2.1 添加华为推送必须的权限

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

#### 5.2.2 配置化为推送服务需要的service和receiver

```
<!-- 备注：Push相关的android组件需要添加到业务的AndroidManifest.xml,
	 Push相关android组件运行在另外一个进程是为了防止Push服务异常而影响主业务 -->

<!-- PushSDK:PushSDK接收外部请求事件入口 -->
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

<!-- PushSDK:Push服务 -->
<service
	android:name="com.huawei.android.pushagent.PushService"
	android:process=":pushservice" >
</service>
```

### 5.3 自定义一个BroadcastReceiver类

为了可以接收到推送消息，需要自定义一个继承自 `PushEventReceiver`类的`BroadcastReceiver`，并实现其中的`onToken`，`onPushMsg`，`onEvent`方法，然后将此receiver注册到AndroidManifest.xml中。

**示例：**

```
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

将自定义的BroadcastReceiver注册到AndroidManifest.xml。
```
<!-- 第三方相关 :接收Push消息（注册、Push消息、Push连接状态、标签，LBS上报结果）广播 -->
<receiver android:name="com.tencent.imsdk.test.HwPushMessageReceiver" >
	<intent-filter>
		<!-- 必须,用于接收token-->
		<action android:name="com.huawei.android.push.intent.REGISTRATION" />
		<!-- 必须，用于接收消息-->
		<action android:name="com.huawei.android.push.intent.RECEIVE" />
		<!-- 可选，用于点击通知栏或通知栏上的按钮后触发onEvent回调-->
		<action android:name="com.huawei.android.push.intent.CLICK" />
		<!-- 可选，查看push通道是否连接，不查看则不需要-->
		<action android:name="com.huawei.intent.action.PUSH_STATE" />
		<!-- 可选，标签、地理位置上报回应，不上报则不需要 -->
		<action android:name="com.huawei.android.push.plugin.RESPONSE" />
	</intent-filter>
	<meta-data android:name="CS_cloud_ablitity" android:value="successRateAnalytics"/>
</receiver>
```

### 5.4 获取设备token

通过调用`PushManager.requestToken`方法向华为推送平台请求当前应用在当前设备上的唯一标识。请求成功后，可以在前面自定义的`BroadcastReceiver`的`onToken`回调中获取分配的token。把这个token记录下来，后边会用到。

`PushManager.requestToken`可在任意地方调用，如果在Application的onCreate中调用的话，需要注意的是因为`XMPushService`在AndroidManifest.xml中设置为运行在另外一个进程，这导致本Application会被实例化两次，所以我们需要让应用的主进程对推送服务进行初始化。

**示例：**
```
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
			//请求华为推送设备token
            PushManager.requestToken(this);
        }
    }
}
```

### 5.5 上报证书ID及设备token

想要ImSDK通过华为推送进行离线消息推送，必须在**登录成功后**将前面步骤拿到的**证书ID**及**设备token**上报到腾讯云服务器。这一步骤可以通过`TIMManager`中的`setOfflinePushToken`方法来实现。

**目前仅支持小米、华为设备，其他厂商设备上传无效。**

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
token|用户标识，包括证书ID， regId， TMID等

`TIMOfflinePushToken`成员方法详细说明：
```
/**
 * 离线推送token配置类，目前只适用于第三方推送接入，比如小米推送、华为推送
 */
public class TIMOfflinePushToken {
    /**
     * 设置离线推送用户标识，如小米推送的regId和华为推送的TMID
     * @param token 用户标识
     */
    public void setToken(String token)
		
    /**
     * 设置业务ID，这里的业务ID是指将离线推送相关证书上传到腾讯云的时候分配的ID
     * @param bussid 业务ID
     */
    public void setBussid(long bussid)
}
```

**示例：**
```
//登录成功后，上报证书ID及设备token
TIMOfflinePushToken param = new TIMOfflinePushToken();
param.setToken(token);
param.setBussid(bussId);
TIMManager.getInstance().setOfflinePushToken(param);
```

### 5.6 混淆打包

如果需要混淆打包应用，为了防止华为离线推送功能异常，需要添加以下混淆规则，仅供参考。

```
-keep class com.huawei.android.pushagent.**{*;}
-keep class com.huawei.android. pushselfshow.**{*;}
-keep class com.huawei.android. microkernel.**{*;}
-keep class com.baidu.mapapi.**{*;}
```