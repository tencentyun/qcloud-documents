这里的离线是指在没有退出登录的情况下，应用被系统或者用户关闭。在这种情况下，如果还想收到 IM SDK 的消息提醒，可以集成云通信离线推送。另外，IM SDK 从2.1.0版本开始，提供了适配小米、华为离线推送的方案。

>!
> - 对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。
> - 目前，离线推送只提供 [普通聊天消息](/doc/product/269/%E6%B6%88%E6%81%AF%E6%94%B6%E5%8F%91%EF%BC%88Android%20SDK%EF%BC%89#1-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 进行消息提醒，暂不提供对 [系统消息](/doc/product/269/消息收发（Android%20SDK）#.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF) 的消息提醒 。

## 设置离线推送配置
### 设置全局离线推送配置
IM SDK 从2.1.0版本开始提供了设置全局离线推送配置的功能，可以设置是否开启离线推送、收到离线推送时的提示声音等。这个设置方法是由 `TIMManager` 提供的 `setOfflinePushSettings`。

>!
> - 必须在登录成功后调用才生效。
> - 目前仅支持应用内置的声音文件。

**原型 ：**

```java
/**
 * 初始化离线推送配置，需登录后设置才生效
 * @param settings 离线推送配置信息
 */
public void setOfflinePushSettings(TIMOfflinePushSettings settings)

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

**TIMOfflinePushSettings 说明：**

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

TIMManager.getInstance().setOfflinePushSettings(settings);
```

### 设置单条消息的离线推送配置
IM SDK 从2.2.0版本开始提供针对单独每一条消息进行离线推送配置的功能。开发者可以针对某条消息设置是否开启离线推送、收到离线推送后提醒声音、离线推送消息描述及扩展字段等。

>!
> - 针对单条消息设置的离线推送配置优先级是最高的，也就是在同时设置了全局离线推送配置及单条消息离线推送配置的情况下，将以单条消息离线推送配置为准。
> - 目前 Android 设备的声音仅支持应用内置的声音文件。


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

**`TIMMessageOfflinePushSettings`：**

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

**TIMMessageOfflinePushSettings.AndroidSettings：**

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

`NotifyMode` 只是针对第三方离线推送进行设置的，比如小米、华为的离线推送。
**TIMMessageOfflinePushSettings.NotifyMode：**

```java
/**
 * 普通通知栏消息模式，离线消息下发后，单击通知栏消息直接启动应用，不会给应用进行回调
 */
NotifyMode.Normal

```

**TIMMessageOfflinePushSettings.IOSSettings：**

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
//IM SDK 2.5.3之前的构造方式
//TIMMessageOfflinePushSettings.AndroidSettings androidSettings = settings.new AndroidSettings();
androidSettings.setTitle("I'm title");
//推送自定义通知栏消息，接收方收到消息后单击通知栏消息会给应用回调（针对小米、华为离线推送）
androidSettings.setNotifyMode(TIMMessageOfflinePushSettings.NotifyMode.Normal);
//设置 Android 设备收到消息时的提示音，声音文件需要放置到 raw 文件夹
androidSettings.setSound(Uri.parse("android.resource://" + getPackageName() + "/" +R.raw.hualala));
settings.setAndroidSettings(androidSettings);

//设置在 iOS 设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.IOSSettings iosSettings = new TIMMessageOfflinePushSettings.IOSSettings();
//IM SDK 2.5.3之前的构造方式
//TIMMessageOfflinePushSettings.IOSSettings iosSettings = settings.new IOSSettings();

//开启 Badge 计数
iosSettings.setBadgeEnabled(true);  
//设置 iOS 收到消息时没有提示音且不振动（IM SDK 2.5.3 新增特性）
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
IM SDK 从1.8.0版本开始提供了离线推送的功能。因为离线推送依赖于守护进程，所以为了保证离线推送的正常运作，需要对应用的**自启动权限**进行授权，而部分对 Android 系统进行了深度定制化的机型（华为、小米等）则需要将应用添加到应用白名单，保证应用被 kill 掉后，守护进程可以自动重启。

### 配置 AndroidManifest
由于 IM SDK 的离线推送依赖于服务，所以需要应用在 `AndroidManifest.xml` 的 `<application></application>` 中添加以下配置：

```xml
<!--  消息收发 service -->
<service 
    android:name="com.tencent.imsdk.session.remote.SessionService"
    android:process=":network"/>
<!--  消息收发辅助 service -->
<service
    android:name="com.tencent.imsdk.session.remote.AssistService"
    android:process=":network"/>
<service
    android:name="com.tencent.imsdk.session.remote.KeepAliveJobService"
    android:permission="android.permission.BIND_JOB_SERVICE"
    android:process=":network"/>
<!--  离线消息广播接收器 -->
<receiver android:name="com.tencent.imsdk.session.SessionBroadcastReceiver">
    <intent-filter>
        <action android:name="com.tencent.imsdk.session.boot" />
        <action android:name="android.intent.action.BOOT_COMPLETED"/>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
    </intent-filter>
</receiver>
```

### 设置离线推送处理
#### 实现自己的 Application 类

实现 `android.app.Application`，假设命名为 `MyApplication`，在 `AndroidManifes.xml` 中配置实现：

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

>!设置离线推送监听器，**需要保证在主进程进行设置**。

**原型：**
```
public void setOfflinePushListener(TIMOfflinePushListener listener)
```

**参数说明：**

参数|说明
---|---
listener|离线推送监听器。

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

					// 这里的 doNotify 是 IM SDK 内置的通知栏提醒，应用也可以选择自己利用回调参数 notification 来构造自己的通知栏提醒
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
可以通过 `getTitle` 接口来获取默认通知栏标题。

- **单聊消息：**默认通知栏标题为发送方用户 ID。
- **群消息：**如果消息所在群设置了群名称，默认通知栏标题为群名称；如果该群没有设置群名称，默认通知栏标题为该群群 ID。

**原型：**
```
public String getTitle()
```

#### 获取默认通知栏内容

可以通过 `getContent` 接口来获取默认通知栏内容。

**对于单聊消息， 默认通知栏内容为：**
```
消息内容
```
**对于群消息，默认通知栏内容为：**
```
发送者： 消息内容
```

- **发送者**为消息发送方的群名片，如果发送方没有设置群名片，则为发送方的个人昵称，如果个人昵称也没有设置，则为发送方的用户 ID。优先级为**群名片** > **个人昵称** > **用户 ID**。

- **消息内容**为消息体中的各个 Elem 进行相应转换后的字符串组合，不同类型的 Elem，其转换规则如下：
	- 文本 Elem：直接显示内容
	- 语音 Elem：显示 [语音]
	- 文件 Elem：显示 [文件]
	- 图片 Elem：显示 [图片]
	- 自定义 Elem：显示 [desc 字段内容]

**获取默认通知栏内容的原型：**

```
public String getContent()
```

#### 获取会话 ID

通过 `getConversationId` 可以获取到离线消息的会话 ID。**单聊消息**的会话 ID 为消息发送方用户 ID。**群消息**的会话 ID 为群 ID。获取会话 ID 原型如下，失败时返回 null。

**原型：**
```
public String getConversationId()
```

#### 获取会话类型

通过 `getConversationType` 可以获取到离线消息的会话类型。**单聊消息**的会话类型为 `TIMConversationType.C2C`。**群消息**的会话类型为`TIMConversationType.Group`。

**原型：**

```
public TIMConversationType getConversationType()
```

#### 获取发送方用户 ID

通过 `getSenderIdentifier` 可以获取到消息发送方的用户 ID。获取发送方用户 ID 原型如下，失败时返回 null。

**原型：**
```
public String getSenderIdentifier()
```

#### 获取发送者昵称

通过 `getSenderNickName` 可以获取到消息发送方的昵称/群名片（群消息时，优先返回群名片，当没有群名片时，返回昵称）。对于 **单聊消息**，返回 null。对于**群消息**，优先返回发送方的群名片，如果发送方没有设置群名片，则返回个人昵称。如果群名片和个人昵称都没有设置，则返回 null。

**原型：**
```
public String getSenderNickName()
```

#### 获取群名称

在收到群消息的时候，可以通过 `getGroupName` 获取到群名称。获取群名称只有在收到群消息时有效，失败时返回 null。

**原型：**

```
public String getGroupName()
```

#### 获取扩展字段

收到自定义消息的时候，可以通过 `getExt` 获取到消息扩展字段，即自定义消息对应的 `ext` 字段。

**原型：**
```
public byte[] getExt()
```

#### 应用默认通知栏提醒

可以通过 `doNotify` 来应用 IM SDK 提供的默认通知栏提醒样式。

**原型：**
```
public void doNotify(Context context, int iconID)
```

**参数说明：**

参数|说明
---|---
context|应用上下文。
iconID|要显示在提醒中的图标的资源 ID。

