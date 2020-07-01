## 概述

即时通信 IM 的终端用户需要随时都能够得知最新的消息，而由于移动端设备的性能与电量有限，当 App 处于后台时，为了避免维持长连接而导致的过多资源消耗，即时通信 IM 推荐您使用各厂商提供的系统级推送通道来进行消息通知，系统级的推送通道相比第三方推送拥有更稳定的系统级长连接，可以做到随时接受推送消息，且资源消耗大幅降低。

即时通信 IM 目前已经支持了小米推送、华为推送、魅族推送、vivo 推送、OPPO 推送、Google FCM推送，具体如下：

<table> 
   <tr> 
     <th nowrap="nowrap">推送通道</th> 
     <th nowrap="nowrap">系统要求</th> 
     <th>条件说明</th> 
   </tr> 
   <tr> 
     <td>小米推送</td> 
     <td>MIUI</td> 
     <td>使用小米推送 MiPush_SDK_Client_3_6_12.jar</td> 
   </tr> 
   <tr> 
     <td>华为推送</td> 
     <td>EMUI</td> 
     <td>华为移动服务版本 20401300 以上，SDK 版本 push:2.6.3.301</td> 
   </tr> 
   <tr> 
     <td nowrap="nowrap">Google FCM 推送</td> 
     <td nowrap="nowrap">Android 4.1 及以上</td> 
     <td>手机端需安装 Google Play Services 且在中国大陆地区以外使用。</td> 
   </tr> 
   <tr> 
     <td>魅族推送</td> 
     <td>Flyme</td> 
     <td>使用魅族推送 push-internal:3.6.+</td> 
   </tr> 
   <tr> 
     <td nowrap="nowrap">OPPO 推送</td> 
     <td>ColorOS</td> 
     <td>并非所有 OPPO 机型和版本都支持使用 OPPO 推送，SDK 版本 mcssdk-2.0.2.jar</td> 
   </tr>  
   <tr> 
     <td nowrap="nowrap">vivo 推送</td> 
     <td nowrap="nowrap">FuntouchOS</td> 
     <td>并非所有 vivo 机型和版本都支持使用 vivo 推送，SDK 版本 vivo_pushsdk_v2.3.1.jar</td> 
   </tr> 
</table>

这里的离线是指在没有退出登录的情况下，应用被系统或者用户关闭。在这种情况下，如果还想收到 IM SDK 的消息提醒，可以集成即时通信 IM 离线推送。

>!对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。

实现离线消息推送的过程如下：

1. 开发者到厂商的平台注册账号，开通推送服务并创建应用，得到AppID、AppKey、AppSecret 等信息。
2. 将厂商提供的推送 SDK 集成到开发者的项目工程中，并在厂商控制台测试通知消息，确保成功集成。
3. 登录 [即时通信 IM 控制台](https://console.qcloud.com/avc) 填写推送证书及相关信息，即时通信 IM 服务端会为每个证书生成不同的证书 ID。
4. 集成即时通信 IM SDK 到项目后，将证书 ID、设备信息等上报至即时通信 IM 服务端。

当客户端 App 在即时通信 IM 没有退出登录的情况下被系统或者用户 kill 时，即时通信 IM 服务端会将其他账号发来的消息通过厂商的通道推送下去。

## 小米推送

### 配置推送证书

<span id="xiaomiStep1_1"></span>

1. 打开 [小米开放平台官网](https://dev.mi.com/console/) 进行注册并通过开发者认证。登录小米开放平台的管理控制台，选择【应用服务】>【PUSH服务】，创建小米推送服务应用，记录**`主包名`**、**`AppID`**、**`AppSecret`**信息。
   ![](https://main.qcloudimg.com/raw/7a291196c6f4800d5d1c9b9e23aed617.jpg)
   <span id="xiaomiStep1_2"></span>
2. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。根据 [步骤1](#Step1_1) 中获取的信息设置以下参数：

 - **推送平台**：选择**小米**
 - **应用包名称**：填写小米推送服务应用的**主包名**
 - **AppID**：填写小米推送服务应用的 **AppID**
 - **AppSecret**：填写小米推送服务应用的 **AppSecret**
 - **点击通知后**：选择点击通知栏消息后的响应操作， 支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#xiaomi_click)
   当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#xiaomi_custom)。
    ![](https://main.qcloudimg.com/raw/b9acf23fb00144aa86be20dba7627699.png)
   单击【确认】保存信息，记录证书的**`ID`**。证书信息保存后10分钟内生效。
    ![](https://main.qcloudimg.com/raw/2a28ec48998579c84a3f3786c9a4b667.png)

### 集成推送 SDK

1. 请参考[小米推送集成指南](https://dev.mi.com/console/doc/detail?pId=41) 集成 SDK，并在小米控制台测试通知消息，确保已成功集成。
2. 通过调用 `MiPushClient.registerPush` 来对小米推送服务进行初始化，注册成功后您将在自定义的 `BroadcastReceiver` 的 `onReceiveRegisterResult` 中收到注册结果。其中 `regId` 为当前设备上当前 App 的唯一标识。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **regId** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过小米推送通知到用户端。

<span id="xiaomi_click"></span>

### 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

#### 打开应用

设置为点击通知栏消息打开应用时，会回调小米的 onNotificationMessageClicked 方法，App 可以在此方法中自行处理打开应用。
![](https://main.qcloudimg.com/raw/fa0fbe98e40da37808a1d646b313783c.png)

#### 打开网页

您需要在 [添加证书](#xiaomiStep1_2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/bb336d3e2bd799b4dfe443833782e322.png)

#### 打开应用内指定界面

1. 在 manifest 中配置需要打开的 Activity 的`intent-filter`，示例代码如下：

   ```
   <activity
   	android:name="com.tencent.qcloud.tim.demo.chat.ChatActivity"
   	android:launchMode="singleTask"
   	android:screenOrientation="portrait"
   	android:windowSoftInputMode="adjustResize|stateHidden">
   	<intent-filter>
   		<action android:name="android.intent.action.VIEW" />
   		<data
   			android:host="com.tencent.qcloud.tim"
   			android:path="/detail"
   			android:scheme="pushscheme" />
   	</intent-filter>
   </activity>
   ```

2. 获取 intent URL，方式如下：

   ```
   Intent intent = new Intent(this, ChatActivity.class);
   intent.setData(Uri.parse("pushscheme://com.tencent.qcloud.tim/detail"));
   intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
   String intentUri = intent.toUri(Intent.URI_INTENT_SCHEME);
   Log.i(TAG, "intentUri = " + intentUri);
   
   // 打印结果
   intent://com.tencent.qcloud.tim/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.chat.ChatActivity;end
   ```

3. 在 [添加证书](#xiaomiStep1_2) 时选择【打开应用内指定界面】并输入上述打印结果。
   ![](https://main.qcloudimg.com/raw/26a2bb370cfb5525f3eb1ddeef47c490.png)

<span id="xiaomi_custom"></span>

### 透传自定义内容

[添加证书](#Step2) 时设置【点击通知后】为【打开应用】或【打开应用内指定界面】操作才支持透传自定义内容。

**步骤1：发送端设置自定义内容**
在发消息前设置每条消息的通知栏自定义内容。

- Android 端示例：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, userID, null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E) 

**步骤2：接收端获取自定义内容**

- 若 [添加证书](#xiaomiStep1_2) 时设置【点击通知后】的操作为【打开应用】，当点击通知栏的消息时，会触发小米推送 SDK 的  `onNotificationMessageClicked(Context context, MiPushMessage miPushMessage)` 回调，自定义内容可以从 `miPushMessage` 中获取。

  ```
  Map extra = miPushMessage.getExtra();
  String extContent = extra.get("ext");
  ```

- 若 [添加证书](#xiaomiStep1_2) 时设置【点击通知后】的操作为【打开应用内指定界面】，封装消息的 `MiPushMessage` 对象通过 `Intent` 传到客户端，客户端在相应的 `Activity` 中获取自定义内容。

  ```
    Bundle bundle = getIntent().getExtras(); 
    MiPushMessage miPushMessage = (MiPushMessage)bundle.getSerializable(PushMessageHelper.KEY_MESSAGE); 
    Map extra = miPushMessage.getExtra(); 
    String extContent = extra.get("ext");
  ```

## 华为推送

### 配置推送证书

<span id="huaweiStep1_1"></span>

1. 打开 [华为开发者联盟官网](https://developer.huawei.com/consumer/cn/) 进行注册并通过开发者认证。进入管理中心，选择【应用服务】>【开发服务】>【PUSH】，创建华为推送服务应用。记录**`包名`**、**`APP ID`**、**`APP SECRET`**信息。
   ![](https://main.qcloudimg.com/raw/50d36c2cfb7a32acefd8ace44e1ef71f.png)
   <span id="huaweiStep1_2"></span>
2. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。根据 [步骤1](#huaweiStep1_1) 中获取的信息设置以下参数：

 - **推送平台**：选择**华为**
 - **应用包名称**：填写华为推送服务应用的**包名**
 - **AppID**：填写华为推送服务应用的 **APP ID**
 - **AppSecret**：填写华为推送服务应用的 **APP SECRET**
 - **角标参数**：填写应用入口完整 `Activity` 类名，用作华为桌面应用角标显示，请参考 [华为桌面角标开发指导书](https://developer.huawei.com/consumer/cn/doc/development/system-References/30802)
 - **点击通知后**：选择点击通知栏消息后的响应操作， 支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#huawei_click)
   当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#huawei_custom)。
    ![](https://main.qcloudimg.com/raw/852b40d2a8a5aacd4327f94130976563.png)
   单击【保存】保存信息，记录证书的**`ID`**。证书信息保存后10分钟内生效。
   ![](https://main.qcloudimg.com/raw/4f4b2a5c01c524d13434f0b5ca4c4b2c.png)

### 集成推送 SDK

1. 请参考[华为推送集成指南](https://developer.huawei.com/consumer/cn/doc/development/HMS-3-Guides/push-Preparations)集成 SDK，并在华为控制台测试通知消息，确保已成功集成。
2. 通过调用华为 `HmsInstanceId.getToken` 接口向服务端请求应用的唯一标识 Push Token，`Push Token` 为当前设备上当前 App 的唯一标识。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **Push Token** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过小米推送通知到用户端。

<span id="xiaomi_click"></span>

### 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

#### 打开应用

默认为点击通知栏消息打开应用。

#### 打开网页

您需要在 [添加证书](#huaweiStep1_2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/bb336d3e2bd799b4dfe443833782e322.png)

#### 打开应用内指定界面

1. 在 manifest 中配置需要打开的 Activity 的`intent-filter`，示例代码如下：

   ```
   <activity
   	android:name="com.tencent.qcloud.tim.demo.chat.ChatActivity"
   	android:launchMode="singleTask"
   	android:screenOrientation="portrait"
   	android:windowSoftInputMode="adjustResize|stateHidden">
   	<intent-filter>
   		<action android:name="android.intent.action.VIEW" />
   		<data
   			android:host="com.tencent.qcloud.tim"
   			android:path="/detail"
   			android:scheme="pushscheme" />
   	</intent-filter>
   </activity>
   ```

2. 获取 intent URL，方式如下：

   ```
   Intent intent = new Intent(this, ChatActivity.class);
   intent.setData(Uri.parse("pushscheme://com.tencent.qcloud.tim/detail"));
   intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
   String intentUri = intent.toUri(Intent.URI_INTENT_SCHEME);
   Log.i(TAG, "intentUri = " + intentUri);
   
   // 打印结果
   intent://com.tencent.qcloud.tim/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.chat.ChatActivity;end
   ```

3. 在 [添加证书](#huaweiStep1_2) 时选择【打开应用内指定界面】并输入上述打印结果。

<span id="huawei_custom"></span>

### 透传自定义内容

由于华为推送的兼容性问题在某些机器上获取不到透传的信息，因此这里没有给出示例。我们会积极跟华为的相关人员沟通，解决后即刻上线。
	

## OPPO 推送

### 配置推送证书

<span id="oppoStep1_1"></span>

1. 打开 [OPPO PUSH 服务开启指南](https://open.oppomobile.com/wiki/doc#id=10195) 开通 PUSH 服务。在 [OPPO 推送平台](https://push.oppo.com/) >【配置管理】>【应用配置】页面，您可以查看详细的应用信息，记录 `AppId`、`AppKey`、`AppSecret`和`MasterSecret`信息。
   <span id="oppoStep1_2"></span>

2. 按照 OPPO 官网要求，在 OPPO Android 8.0 及以上系统版本必须配置 ChannelID，否则推送消息无法展示。您需要先在 App 中创建对应的 ChannelID（例如 `tuikit`）：

   ```
   public void createNotificationChannel(Context context) {
   				// Create the NotificationChannel, but only on API 26+ because
   				// the NotificationChannel class is new and not in the support library
   				if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
   						CharSequence name = "oppotest";
   						String description = "this is opptest";
   						int importance = NotificationManager.IMPORTANCE_DEFAULT;
   						NotificationChannel channel = new NotificationChannel("tuikit", name, importance);
   						channel.setDescription(description);
   						// Register the channel with the system; you can't change the importance
   						// or other notification behaviors after this
   						NotificationManager notificationManager = context.getSystemService(NotificationManager.class);
   						notificationManager.createNotificationChannel(channel);
   				}
   		}
   ```

   <span id="oppoStep1_3"></span>

3. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。根据 [步骤1](#oppoStep1_1) 中获取的信息设置以下参数：

 - **推送平台**：选择**OPPO**
 - **AppKey**：填写 OPPO 推送服务应用的 **AppKey**
 - **AppID**：填写 OPPO 推送服务应用的 **AppId**
 - **MasterSecret**：填写 OPPO 推送服务应用的 **MasterSecret**
 - **ChannelID**：填写您在 App 中创建的 **ChannelID**
 - **点击通知后**：选择点击通知栏消息后的响应操作， 支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#oppo_click)
   当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#oppo_custom)。
    ![](https://main.qcloudimg.com/raw/8b94fde206c9fa8cd0dee774e12df0ac.png)
   单击【确认】保存信息，记录证书的**`ID`**。证书信息保存后10分钟内生效。
    ![](https://main.qcloudimg.com/raw/23dc3500472be773bf5499299e511444.png)

### 集成推送 SDK

1. 请参考 [OPPO PUSH SDK 接口文档](https://open.oppomobile.com/wiki/doc#id=10196) 集成 SDK，并在 OPPO 控制台测试通知消息，确保已成功集成。
2. 通过调用 OPPO SDK 中的`PushManager.getInstance().register(…)`初始化 Opush 推送服务。
   注册成功后，您可以在 `PushCallback` 的 `onRegister` 回调方法中得到`regId`，`regId` 为当前设备上当前 App 的唯一标识。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **regId** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过小米推送通知到用户端。

<span id="oppo_click"></span>

### 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

#### 打开应用

默认为点击通知栏消息打开应用。

#### 打开网页

您需要在 [添加证书](#oppoStep1_3) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/bb336d3e2bd799b4dfe443833782e322.png)

#### 打开应用内指定界面

打开应用内指定界面有以下几种方式：

**Activity**（推荐）
  该方式比较简单，填入打开的 Activity 的完整类名即可，例如 `com.tencent.qcloud.tim.demo.SplashActivity`

**Intent action**

1. 在 AndroidManifest 要打开的 Activity 中做如下配置，并且必须加上 category 且不能有 data 数据。

```
<intent-filter>
		<action android:name="android.intent.action.VIEW" />
		<category android:name="android.intent.category.DEFAULT" />
</intent-filter>
```

2. 在控制台上填入 `android.intent.action.VIEW`。

<span id="oppo_custom"></span>

### 透传自定义内容

[添加证书](#oppoStep1_3) 时设置【点击通知后】为【打开应用】或【打开应用内指定界面】操作支持透传自定义内容。

**步骤1：发送端设置自定义内容**
在发消息前设置每条消息的通知栏自定义内容。

- Android 端示例：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, userID, null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E) 

**步骤2：接收端获取自定义内容**
当点击通知栏的消息时，客户端在启动的 `Activity` 中获取自定义内容。

```
Bundle bundle = intent.getExtras();
	Set<String> set = bundle.keySet();
	if (set != null) {
			for (String key : set) {
				// 其中 key 和 value 分别为发送端设置的 extKey 和 ext content
					String value = bundle.getString(key);
					Log.i("oppo push custom data", "key = " + key + ":value = " + value);
			}
	}
```

## vivo 推送

### 配置推送证书

<span id="vivoStep1_1"></span>

1. [vivo 开放平台官网](https://dev.vivo.com.cn/home) 进行注册并通过开发者认证。登录其开放平台的管理中心，选择【消息推送】>【创建】>【测试推送】，创建 vivo 推送服务应用。记录**APP ID**、**APP key**和**APP secret**信息。
   <span id="vivoStep1_2"></span>
2. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。根据 [步骤1](#vivoStep1_1) 中获取的信息设置以下参数：

 - **推送平台**：选择 **vivo**
 - **AppKey**：填写 vivo 推送服务应用的 **APP key**
 - **AppID**：填写 vivo 推送服务应用的 **APP ID**
 - **AppSecret**：填写 vivo 推送服务应用的 **APP secret**
 - **点击通知后**：选择点击通知栏消息后的响应操作， 支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#vivo_click)
   当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#vivo_custom)。
    ![](https://main.qcloudimg.com/raw/ac890d834dd7f069f936094180634cd7.png)
   单击【确认】保存信息，记录证书的**ID**。证书信息保存后10分钟内生效。
    ![](https://main.qcloudimg.com/raw/3442e00debac668c42fa4be89903ac90.png)

### 集成推送 SDK

1. 请参考 [vivo 推送集成指南](https://dev.vivo.com.cn/documentCenter/doc/233#w2-08354405) 集成 SDK，并在 vivo 控制台测试通知消息，确保已成功集成。
2. 通过调用 `PushClient.getInstance(getApplicationContext()).initialize()` 来对 vivo 推送服务进行初始化，并调用 `PushClient.getInstance(getApplicationContext()).turnOnPush()` 启动推送，成功后您将在自定义的 `BroadcastReceiver` 的 `onReceiveRegId` 中收到 `regId`，`regId` 为当前设备上当前 App 的唯一标识。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom11tencent11imsdk11v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **regId** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过小米推送通知到用户端。

<span id="vivo_click"></span>

### 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

#### 打开应用

默认为点击通知栏消息打开应用。

#### 打开网页

您需要在 [添加证书](#vivoStep1_2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/bb336d3e2bd799b4dfe443833782e322.png)

#### 打开应用内指定界面

1. 在 manifest 中配置需要打开的 Activity 的`intent-filter`，示例代码如下：

   ```
   <activity
   	android:name="com.tencent.qcloud.tim.demo.chat.ChatActivity"
   	android:launchMode="singleTask"
   	android:screenOrientation="portrait"
   	android:windowSoftInputMode="adjustResize|stateHidden">
   	<intent-filter>
   		<action android:name="android.intent.action.VIEW" />
   		<data
   			android:host="com.tencent.qcloud.tim"
   			android:path="/detail"
   			android:scheme="pushscheme" />
   	</intent-filter>
   </activity>
   ```

2. 获取 intent URL，方式如下：

   ```
   Intent intent = new Intent(this, ChatActivity.class);
   intent.setData(Uri.parse("pushscheme://com.tencent.qcloud.tim/detail"));
   intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
   String intentUri = intent.toUri(Intent.URI_INTENT_SCHEME);
   Log.i(TAG, "intentUri = " + intentUri);
   
   // 打印结果
   intent://com.tencent.qcloud.tim/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.chat.ChatActivity;end
   ```

3. 在 [添加证书](#vivoStep1_2) 时选择【打开应用内指定界面】并输入上述打印结果。

<span id="vivo_custom"></span>

### 透传自定义内容

[添加证书](#vivoStep1_2) 时设置【点击通知后】为【打开应用】或【打开应用内指定界面】操作支持透传自定义内容。

**步骤1：发送端设置自定义内容**
在发消息前设置每条消息的通知栏自定义内容。

- Android 端示例：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, userID, null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E) 

**步骤2：接收端获取自定义内容**
点击通知栏的消息时，会触发 vivo 推送 SDK 的 `onNotificationMessageClicked(Context context, UPSNotificationMessage upsNotificationMessage)` 回调，自定义内容可以从 `upsNotificationMessage` 中获取。

```
Map<String, String> paramMap = upsNotificationMessage.getParams();
String extContent = paramMap.get("ext");
```

## 魅族推送

### 配置推送证书

<span id="meizuStep1_1"></span>

1. 打开 [魅族开放平台官网](http://open.flyme.cn) 进行注册并通过开发者认证。登录其控制台，选择【开发服务】>【Flyme推送】，创建魅族推送服务应用。记录**`应用包名`**、**`App ID`**、**`App Secret`**信息。
   ![](https://main.qcloudimg.com/raw/e0674cc1bca92fd549c03a3523b2144c.png)
   <span id="meizuStep1_2"></span>
2. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。根据 [步骤1](#meizuStep1_1) 中获取的信息设置以下参数：

 - **推送平台**：选择**魅族**
 - **应用包名称**：填写魅族推送服务应用的**应用包名**
 - **AppID**：填写魅族推送服务应用的 **App ID**
 - **AppSecret**：填写魅族推送服务应用的 **App Secret**
 - **点击通知后**：选择点击通知栏消息后的响应操作， 支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#meizu_click)
   当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#meizu_custom)。
    ![](https://main.qcloudimg.com/raw/7151cfff6d8e82a41bfb9b718a49bf2f.png)
   单击【确认】保存信息，记录证书的**`ID`**。证书信息保存后10分钟内生效。
    ![](https://main.qcloudimg.com/raw/b8701c4c69847ae711055df0727f01ab.png)

### 集成推送 SDK

1. 请参考[魅族推送接入](http://open-wiki.flyme.cn/doc-wiki/index#id?129) 集成 SDK，并在其控制台测试通知消息，确保已成功集成。
2. 通过调用 `PushManager.register` 来对魅族推送服务进行初始化，注册成功后您将在自定义的 `BroadcastReceiver` 的 `onRegisterStatus` 中收到注册结果。其中 `registerStatus.getPushId()` 为当前设备上当前 App 的唯一标识。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **PushId** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过小米推送通知到用户端。

<span id="meizu_click"></span>

### 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

#### 打开应用

默认为点击通知栏消息打开应用。

#### 打开网页

您需要在 [添加证书](#meizuStep1_2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/bb336d3e2bd799b4dfe443833782e322.png)

#### 打开应用内指定界面

您需要在 [添加证书](#meizuStep1_2) 时选择【打开应用内指定界面】并输入需要打开的 Activity 的完整类名，例如 `com.tencent.qcloud.tim.demo.chat.ChatActivity`。
![](https://main.qcloudimg.com/raw/64d67e324cc53b0ff0631586d9ec1ef5.png)

<span id="meizu_custom"></span>

### 透传自定义内容

[添加证书](#meizuStep1_2) 时设置【点击通知后】为【打开应用】或【打开应用内指定界面】操作才支持透传自定义内容。

**步骤1：发送端设置自定义内容**
在发消息前设置每条消息的通知栏自定义内容。

- Android 端示例：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, userID, null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E) 

**步骤2：接收端获取自定义内容**

点击通知栏的消息时，会触发魅族推送 SDK 的  `onNotificationClicked(Context context, MzPushMessage mzPushMessage)` 回调 ，自定义内容可以从 `mzPushMessage` 中获取。

```
String extContent = mzPushMessage.getSelfDefineContentString();
```

另外，客户端也可以在打开的 `Activity` 中获取自定义内容。

```
Bundle bundle = getIntent().getExtras();
String extContent = bundle.getString("ext"); 
```

## Google FCM 推送

### 集成 SDK

<span id="fcmStep1_1"></span>
1. 打开 [Firebase 云消息传递](https://firebase.google.com) 注册账号并创建应用。
<span id="fcmStep1_2"></span>
2. 登录 [Firebase 控制台](https://console.firebase.google.com)，单击您的应用卡片，进入应用配置页面。单击 Project Overview 右侧的 <img src="https://main.qcloudimg.com/raw/0d062411405553c9fae29f8e0daf02ad.png"  style="margin:0;">，选择【项目设置】>【服务帐号】，单击【生成新的私钥】下载私钥文件。
<span id="fcmStep1_3"></span>
3. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面，单击【Android平台推送设置】区域的【添加证书】。上传 [步骤2](#fcmStep1_2) 中获取的私钥文件。
 ![](https://main.qcloudimg.com/raw/b18e2414561c6733b24c56cd1e866f21.png)
4. 单击【确认】保存信息，记录证书的**`ID`**。证书信息保存后10分钟内生效。
 ![](https://main.qcloudimg.com/raw/2199bbf955cf52f09b78af6a97ab8122.png)

### 集成推送 SDK

1. 请参考 [Firebase 云消息传递](https://firebase.google.com/docs/cloud-messaging/android/client) 设置 Firebase，集成 FCM SDK。参考 [FCM 测试指引](https://firebase.google.com/docs/cloud-messaging/android/first-message?authuser=0) 测试通知消息，确保已成功集成 FCM。
2. 调用 `FirebaseInstanceId.getInstance().getInstanceId()` 后，在回调里获取当前 App 的唯一标识 token。当登录 IM SDK 成功后，需要调用 [setOfflinePushConfig](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 将**证书 ID** 和 **token** 上报到即时通信 IM 服务端。

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过 FCM 推送通知到用户端。

<span id="fcm_custom"></span>

### 透传自定义内容

**步骤1：发送端设置自定义内容**
在发消息前设置每条消息的通知栏自定义内容。

- Android 端示例：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, userID, null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E) 

**步骤2：接收端获取自定义内容**
当点击通知栏的消息时，客户端在相应的 `Activity` 中获取自定义内容。

```
Bundle bundle = getIntent().getExtras();
String value = bundle.getString("ext"); 
```

## 自定义 iOS 推送提示音

请在调用 [sendMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 发送消息的时候使用 `V2TIMOfflinePushInfo` 中的 [setIOSSound](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#acffd09150398b06c3d7eb42baee5aee1) 接口来设置 iOS 端的推送声音。

## 自定义离线推送展示

请在调用  [sendMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 发送消息的时候使用 `V2TIMOfflinePushInfo` 中的 [setTitle](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a7d4a73d6a1db487dd96f658bdbc98ae9) 和 [setDesc](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 接口来分别设置通知栏消息的标题和内容。

## 自定义离线推送点击跳转逻辑

请在调用 [sendMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 发送消息时使用 `V2TIMOfflinePushInfo` 中的 [setExt](https://docs-1252463788.cos.ap-shanghai.myqcloud.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a9346ecab2e35ff516b24c27b0584a9a2) 接口设置自定义内容，当用户点击通知栏消息启动 APP 时，可以根据获取到 `ext` 字段内容跳转到指定的 UI 界面。

我们以 “denny 给 vinson 发送消息” 的场景为例。

- 发送方：denny 要在发送消息的时候设置推送扩展字段 ext：

  ```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("action", "jump to denny");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();
  V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
  v2TIMOfflinePushInfo.setExt(extContent.getBytes());
  
  V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, "vinson", null, V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false,  v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
  	@Override
  	public void onError(int code, String desc) {}
  	@Override
  	public void onSuccess(V2TIMMessage v2TIMMessage) {}
  	@Override
  	public void onProgress(int progress) {}
  });
  ```

- 接收方：vinson 的 App 虽然不在线，但可以接收到手机厂商（我们以 OPPO 手机为例）的离线推送，当 vinson 点击推送消息时会启动 App：

  ```
  // vinson 启动 APP 后在打开的 Activity 中获取自定义内容
  Bundle bundle = intent.getExtras();
  Set<String> set = bundle.keySet();
  if (set != null) {
  	for (String key : set) {
  		// 其中 key 和 value 分别为发送端设置的 extKey 和 ext content
  		String value = bundle.getString(key);
  		if (value.equals("jump to denny")) {
  			// 跳转到和 denny 的聊天界面
  			...
  		}
  	}
  }
  ```

## 常见问题

### Android 手机离线推送怎么自定义推送的声音？

目前大部分厂商都不支持离线推送声音的设置，因此 IM SDK 暂时不支持。

### OPPO 手机为什么收不到离线推送？

OPPO 手机收不到推送一般有以下几种情况：

- 按照 OPPO 推送官网要求，在 Android 8.0 及以上系统版本的 OPPO 手机上必须配置 ChannelID，否则推送消息无法展示。配置方法可以参考 [OPPO 推送配置](#oppoStep1_2)。
- 在消息中 [透传的离线推送的自定义内容](#oppo_custom) 不是 JSON 格式，会导致 OPPO 手机收不到推送。

### 自定义消息为什么收不到离线推送？

自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 的时候设置 [offlinePushInfo](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 的 [desc](http://doc.qcloudtrtc.com/im/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 字段，推送的时候会默认展示 desc 信息。

