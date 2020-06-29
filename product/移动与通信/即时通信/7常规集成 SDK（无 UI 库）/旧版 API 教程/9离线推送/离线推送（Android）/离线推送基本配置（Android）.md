## 概述

即时通信 IM 的终端用户需要随时都能够得知最新的消息，而由于移动端设备的性能与电量有限，当 App 处于后台时，为了避免维持长连接而导致的过多资源消耗，即时通信 IM 推荐您使用各厂商提供的系统级推送通道来进行消息通知，系统级的推送通道相比第三方推送拥有更稳定的系统级长连接，可以做到随时接受推送消息，且资源消耗大幅降低。

即时通信 IM 目前已经支持了 APNs、小米推送、华为推送、魅族推送、vivo 推送、OPPO 推送等厂商推送，具体如下：

<table> 
   <tr> 
     <th nowrap="nowrap">推送通道</th> 
     <th nowrap="nowrap">系统要求</th> 
     <th>条件说明</th> 
   </tr> 
   <tr> 
     <td><a href="https://cloud.tencent.com/document/product/269/9154" target="_blank">APNs</a></td> 
     <td>iOS</td> 
     <td>iOS 系统推送通道，也是唯一的 iOS 推送通道</td> 
   </tr> 
   <tr> 
     <td><a href="https://cloud.tencent.com/document/product/269/35000" target="_blank">小米推送</a></td> 
     <td>MIUI</td> 
     <td>使用小米推送 MiPush_SDK_Client_3_6_12.jar</td> 
   </tr> 
   <tr> 
     <td><a href="https://cloud.tencent.com/document/product/269/34999" target="_blank">华为推送</a></td> 
     <td>EMUI</td> 
     <td>华为移动服务版本 20401300 以上，SDK 版本 push:2.6.3.301</td> 
   </tr> 
   <tr> 
     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/269/37317" target="_blank">Google FCM 推送</a></td> 
     <td nowrap="nowrap">Android 4.1 及以上</td> 
     <td>手机端需安装 Google Play Services 且在中国大陆地区以外使用。</td> 
   </tr> 
   <tr> 
     <td><a href="https://cloud.tencent.com/document/product/269/35001" target="_blank">魅族推送</a></td> 
     <td>Flyme</td> 
     <td>使用魅族推送 push-internal:3.6.+</td> 
   </tr> 
   <tr> 
     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/269/37729" target="_blank">OPPO 推送</a></td> 
     <td>ColorOS</td> 
     <td>并非所有 OPPO 机型和版本都支持使用 OPPO 推送，SDK 版本 mcssdk-2.0.2.jar</td> 
   </tr>  
   <tr> 
     <td nowrap="nowrap"><a href="https://cloud.tencent.com/document/product/269/34998" target="_blank">vivo 推送</a></td> 
     <td nowrap="nowrap">FuntouchOS</td> 
     <td>并非所有 vivo 机型和版本都支持使用 vivo 推送，SDK 版本 vivo_pushsdk_v2.3.1.jar</td> 
   </tr> 
</table>


这里的离线是指在没有退出登录的情况下，应用被系统或者用户关闭。在这种情况下，如果还想收到 IM SDK 的消息提醒，可以集成即时通信 IM 离线推送。

>!
> - 对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。
> - 目前，离线推送只提供 [普通聊天消息](/doc/product/269/%E6%B6%88%E6%81%AF%E6%94%B6%E5%8F%91%EF%BC%88Android%20SDK%EF%BC%89#1-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 进行消息提醒，暂不提供对 [系统消息](/doc/product/269/消息收发（Android%20SDK）#.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF) 的消息提醒。

## IM SDK 离线推送基本配置
### 设置全局离线推送配置
IM SDK 提供了设置全局离线推送配置的功能，可以设置是否开启离线推送、收到离线推送时的提示声音等。这个设置方法是由 `TIMManager` 提供的 `setOfflinePushSettings`。

>!
> - 必须在登录成功后调用才生效。
> - 目前仅支持 APNs 自定义提示音，声音文件需应用内置。

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

|参数|说明|
|---|---|
|settings|离线推送配置|

**TIMOfflinePushSettings 说明：**

```java
/**
 * 获取是否开启
 * @return true 表示开启， false 表示不开启
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
//设置收到 C2C 离线消息时的提示声音，以把声音文件放在 res/raw 文件夹下为例
settings.setC2cMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));
//设置收到群离线消息时的提示声音，以把声音文件放在 res/raw 文件夹下为例
settings.setGroupMsgRemindSound(Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.dudulu));

TIMManager.getInstance().setOfflinePushSettings(settings);
```

### 针对单条消息设置离线推送
IM SDK 提供针对单独每一条消息进行离线推送配置的功能。开发者可以针对指定的某一条消息设置是否开启离线推送、收到离线推送后提醒声音、离线推送消息描述及扩展字段等。

>!
> - 针对单条消息设置的离线推送配置优先级是最高的，也就是在同时设置了全局离线推送配置及单条消息离线推送配置的情况下，将以单条消息离线推送配置为准。
> - 目前仅支持 APNs 自定义提示音，声音文件需应用内置。


**原型：**

```java
/**
 * 设置当前消息在对方收到离线推送的时候的配置（可选，发送消息时设置）
 * @param settings 离线推送配置
 */
public void setOfflinePushSettings(TIMMessageOfflinePushSettings settings)

/**
 * 获取当前消息的离线推送配置
 * @return 离线推送配置，如果发送方没有设置的，返回 null
 */
public TIMMessageOfflinePushSettings getOfflinePushSettings()
```

**`TIMMessageOfflinePushSettings`：**

```java
/**
 * 离线 Push 展示标题，针对 iOS 和 Android 平台都生效，如果您需要分平台单独设置，请设置 IOSSettings -> title 和 AndroidSettings -> title
 *
 * @param title 通知栏标题
 * @return
 */
public TIMMessageOfflinePushSettings setTitle(String title)

/**
 * 离线 Push 展示文本，针对 iOS 和 Android 平台都生效，如果您需要分平台单独设置，请设置 IOSSettings -> desc 和 AndroidSettings -> desc
 * @param descr 正文内容
 */
public TIMMessageOfflinePushSettings setDescr(String descr)

/**
 * 获取当前消息的离线推送展示正文内容
 * @return 正文内容
 */
public String getDescr()

/**
 * 设置当前消息的扩展字段（可选，发送消息的时候设置）
 * @param ext 扩展字段内容
 */
public TIMMessageOfflinePushSettings setExt(byte[] ext)

/**
 * 获取当前消息的扩展字段
 * @return 扩展字段内容，没有设置返回 null
 */
public byte[] getExt()

/**
 * 设置当前消息是否允许离线推送，默认允许推送（可选，发送消息时设置）
 * @param enabled true 表示允许离线推送， false 表示不允许离线推送
 */
public TIMMessageOfflinePushSettings setEnabled(boolean enabled)

/**
 * 获取当前消息是否允许推送
 * @return 是否允许推送标识， true 表示允许推送， false 表示不允许推送
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
public TIMMessageOfflinePushSettings setAndroidSettings(AndroidSettings androidSettings)

/**
 * 获取当前消息在 iOS 设备上的离线推送配置
 * @return iOS 设备上的离线推送配置
 */
public IOSSettings getIosSettings()

/**
 * 设置当前消息在 iOS 设备上的离线推送配置（可选，发送消息时设置）
 * @param iosSettings 当前消息在 iOS 设备上的离线推送配置
 */
public TIMMessageOfflinePushSettings setIosSettings(IOSSettings iosSettings)

```

**TIMMessageOfflinePushSettings.AndroidSettings：**

```java
/**
 * 获取通知标题
 * @return 通知标题
 */
public String getTitle()

/**
 * 设置离线 Push 展示标题
 
 * @param title 通知标题
 */
public AndroidSettings setTitle(String title)

/**
 * 设置离线 Push 展示自定义文本
 *
 * @param desc 通知显示内容
 */
public AndroidSettings setDesc(String desc)

/**
 * 获取当前消息在 Android 设备上的离线推送提示声音 URI
 * @return 声音 URI，没有设置则返回 null
 */
public Uri getSound()

/**
 * 设置当前消息在 Android 设备上的离线推送提示声音（可选，发送消息时设置）
 * @param sound 声音 URI，仅支持应用内部的声音资源文件
 */
public AndroidSettings setSound(Uri sound)

/**
 * 获取当前消息的通知模式
 * @return 通知模式
 */
public NotifyMode getNotifyMode()

/**
 * 设置当前消息在对方收到离线推送时候的通知模式（待废弃，可以不设置）。
 * 
 * @param mode 通知模式，默认为普通通知栏消息模式
 */
public AndroidSettings setNotifyMode(NotifyMode mode)
```

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
 * 设置离线 Push 展示标题
 *
 * @param title 通知标题
 */
public IOSSettings setTitle(String title)

/**
 * 设置离线 Push 展示自定义文本
 *
 * @param desc
 */
public IOSSettings setDesc(String desc)

/**
 * 获取当前消息在 iOS 设备上的离线推送提示声音
 *
 * @return 声音文件路径，没有设置则返回 null
 */
public String getSound()

/**
 * 设置当前消息在 iOS 设备上的离线推送提示声音（可选，发送消息时设置）
 *
 * @param sound 声音文件路径，当设置为{@see IOSSettings#NO_SOUND_NO_VIBRATION}时表示无提示音无振动
 */
public void setSound(String sound)

/**
 * 获取当前消息是否开启 Badge 计数
 *
 * @return true 表示当前消息开启 Badge 计数
 */
public boolean isBadgeEnabled()

/**
 * 设置当前消息是否开启 Badge 计数，默认开启（可选，发送消息时设置）
 *
 * @param badgeEnabled 否开启 Badge 计数
 */
public IOSSettings setBadgeEnabled(boolean badgeEnabled)
```

**示例：**

```java
// 构造一条消息
TIMMessage msg = new TIMMessage();

// 添加文本内容
TIMTextElem elem = new TIMTextElem();
elem.setText("a new msg from " + selfId);
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}

// 设置当前消息的离线推送配置
TIMMessageOfflinePushSettings settings = new TIMMessageOfflinePushSettings();
settings.setEnabled(true);
// 设置 iOS 和 Android 通知栏消息的标题和内容。如果想要两个平台通知栏展示的标题和内容不同，可以通过 AndroidSettings 和 IOSSettings 分别设置。
settings.setTitle("I'm title");
settings.setDescr("I'm description");
// 设置离线推送扩展信息
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

// 设置在 Android 设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.AndroidSettings androidSettings = new TIMMessageOfflinePushSettings.AndroidSettings();
// IM SDK 2.5.3之前的构造方式
// TIMMessageOfflinePushSettings.AndroidSettings androidSettings = settings.new AndroidSettings();
// 设置 Android 通知栏消息的标题和内容
// androidSettings.setTitle("I'm title for android");
// androidSettings.setDesc("I'm desc for android");
// 设置 Android 设备收到消息时的提示音，声音文件需要放置到 raw 文件夹
androidSettings.setSound(Uri.parse("android.resource://" + getPackageName() + "/" +R.raw.hualala));
settings.setAndroidSettings(androidSettings);

//设置在 iOS 设备上收到消息时的离线配置
TIMMessageOfflinePushSettings.IOSSettings iosSettings = new TIMMessageOfflinePushSettings.IOSSettings();
//IM SDK 2.5.3之前的构造方式
//TIMMessageOfflinePushSettings.IOSSettings iosSettings = settings.new IOSSettings();
// 设置 iOS 通知栏消息的标题和内容
// iosSettings.setTitle("I'm title for iOS");
// iosSettings.setDesc("I'm desc for iOS");

// 开启 Badge 计数
iosSettings.setBadgeEnabled(true);  
// 设置 iOS 收到消息时没有提示音且不振动（IM SDK 2.5.3新增特性）
//iosSettings.setSound(TIMMessageOfflinePushSettings.IOSSettings.NO_SOUND_NO_VIBRATION);
// 设置 iOS 设备收到离线消息时的提示音
iosSettings.setSound("/path/to/sound/file");

msg.setOfflinePushSettings(settings);

// 获取一个单聊会话
TIMConversation conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.C2C,    // 会话类型：单聊
        peer); 						// 会话对方用户帐号

// 发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {// 发送消息回调
    @Override
    public void onError(int code, String desc) {// 发送消息失败
        // 错误码 code 和错误描述 desc，可用于定位请求失败原因
        // 错误码 code 列表请参见错误码表
        Log.e(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }

    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.d(tag, "SendMsg ok! peer:" + peer );
    }
});
```



