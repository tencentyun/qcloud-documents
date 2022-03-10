## 流程说明
实现离线消息推送的过程如下：
1. 开发者到厂商的平台注册帐号，并通过开发者认证后，申请开通推送服务。
2. 创建推送服务，并绑定应用信息，获取推送证书、密码、密钥等信息。
3. 登录 [即时通信 IM 控制台](https://console.qcloud.com/avc) 填写推送证书及相关信息，即时通信 IM 服务端会为每个证书生成不同的证书 ID。
4. 将厂商提供的推送 SDK 集成到开发者的项目工程中，并按各厂商的要求进行配置。
5. 集成即时通信 IM SDK 到项目后，将证书 ID、设备信息等上报至即时通信 IM 服务端。
6. 当客户端 App 在即时通信 IM 没有退出登录的情况下，被系统或者用户 kill 时，即时通信 IM 服务端将通过消息推送进行提醒。

## 操作步骤

OPPO 手机使用深度定制 Android 系统，对于第三方 App 自启动权限管理很严格，默认情况下第三方 App 都不会在系统的自启动白名单内，App 在后台时容易被系统 kill，因此推荐在 OPPO 设备上集成 OPPO 推送，OPPO 推送是 OPPO 设备的系统级服务，推送到达率较高。目前，**即时通信 IM 仅支持 OPPO 推送的通知栏消息**。

>!
>- 此指引文档是直接参考 OPPO 推送官方文档所写，若 OPPO 推送有变动，请以 [OPPO 推送官网文档](https://open.oppomobile.com/wiki/doc#id=10194) 为准。
>- 如果不需要对 OPPO 设备做专门的离线推送适配，可以忽略此章节。

[](id:Step1)
### 步骤1：申请 OPPO 推送证书
1. 请参考 [OPPO PUSH 服务开启指南](https://open.oppomobile.com/wiki/doc#id=10195) 开通 PUSH 服务。
2. 在 [OPPO 推送平台](https://push.oppo.com/) >【配置管理】>【应用配置】页面，您可以查看详细的应用信息。
[](id:Step1_3)
3. 记录`AppId`、`AppKey`、`AppSecret`和`MasterSecret`信息。

[](id:Step2)
### 步骤2：创建 ChannelID

按照 OPPO 官网要求，在 OPPO Android 8.0 及以上系统版本必须配置 ChannelID，否则推送消息无法展示。您需要先在 App 中创建对应的 ChannelID（例如 `tuikit`）：

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
	
[](id:Step3)
### 步骤3：托管证书信息到即时通信 IM
1. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【Android平台推送设置】区域的【添加证书】。
 >?如果您原来已有证书只需变更信息，可以单击【Android平台推送设置】区域的【编辑】进行修改更新。
 >
 ![](https://main.qcloudimg.com/raw/aaa40b3c7e43f99b7e36c8b7589e54e0.png)
3. 根据 [步骤1](#Step1_3) 和 [步骤2](#Step2) 中获取的信息设置以下参数：
 - **推送平台**：选择 **OPPO**
 - **AppKey**：填写 OPPO 推送服务应用的 **AppKey**
 - **AppID**：填写 OPPO 推送服务应用的 **AppId**
 - **MasterSecret**：填写 OPPO 推送服务应用的 **MasterSecret**
 - **ChannelID**：填写您在 App 中创建的 **ChannelID**
 - **点击后续操作**：选择点击通知栏消息后的响应操作，支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#click)
  当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#Trans)。
![](https://main.qcloudimg.com/raw/8b94fde206c9fa8cd0dee774e12df0ac.png)
4. 单击【确认】保存信息，证书信息保存后10分钟内生效。
5. 待推送证书信息生成后，记录证书的**`ID`**。
 ![](https://main.qcloudimg.com/raw/23dc3500472be773bf5499299e511444.png)

[](id:Step4)
### 步骤4：集成推送 SDK

1. 请参考  [OPPO PUSH SDK 接口文档](https://open.oppomobile.com/wiki/doc#id=10196) 集成 SDK，并在 OPPO 控制台测试通知消息，确保已成功集成。
2. 通过调用 OPPO SDK 中的`PushManager.getInstance().register(…)`初始化 Opush 推送服务。
 注册成功后，您可以在 `PushCallback` 的 `onRegister` 回调方法中得到`regId`。
3. 记录`regId`信息。

[](id:Step5)
### 步骤5：上报推送信息至即时通信 IM 服务端

若您需要通过 OPPO 推送进行即时通信 IM 消息的推送通知，必须在**用户登录成功后**通过`TIMManager`中的`setOfflinePushToken`方法将您托管到即时通信 IM 控制台生成的**证书 ID** 及 OPPO 推送服务返回的 **regId** 上报到即时通信 IM 服务端。
>!正确上报 regId 与证书 ID 后，即时通信 IM 服务才能将用户与对应的设备信息绑定，从而使用 OPPO 推送服务进行推送通知。

定义证书 ID 常量示例代码：

```java
/****** OPPO 离线推送参数 start ******/
// 在腾讯云控制台上传第三方推送证书后分配的证书 ID
public static final long OPPO_PUSH_BUZID = 7005;
/****** OPPO 离线推送参数 end ******/
```

上报推送的证书 ID 及 regId 示例代码：

```java
/**
 * 在 ThirdPushTokenMgr.java 中对推送的证书 ID 及设备信息进行上报操作
 */
public class ThirdPushTokenMgr {
    private static final String TAG = "ThirdPushTokenMgr";
    private String mThirdPushToken;
   
    public static ThirdPushTokenMgr getInstance () {
        return ThirdPushTokenHolder.instance;
    }
    private static class ThirdPushTokenHolder {
        private static final ThirdPushTokenMgr instance = new ThirdPushTokenMgr();
    }

    public void setThirdPushToken(String mThirdPushToken) {
        this.mThirdPushToken = mThirdPushToken;  // regId 在此处传值，结合上文自定义 BroadcastReciever 类文档说明
    }
    public void setPushTokenToTIM(){
        String token = ThirdPushTokenMgr.getInstance().getThirdPushToken();
        if(TextUtils.isEmpty(token)){
            QLog.i(TAG, "setPushTokenToTIM third token is empty");
            mIsTokenSet = false;
            return;
        }
        TIMOfflinePushToken param = null;
        if(IMFunc.isBrandXiaoMi()){     // 判断厂商品牌，根据不同厂商选择不同的推送服务
            param = new TIMOfflinePushToken(Constants.XM_PUSH_BUZID, token);
        }else if(IMFunc.isBrandHuawei()){
            param = new TIMOfflinePushToken(Constants.HW_PUSH_BUZID, token);
        }else if(IMFunc.isBrandMeizu()){
            param = new TIMOfflinePushToken(Constants.MZ_PUSH_BUZID, token);
        }else if(IMFunc.isBrandOppo()){
            param = new TIMOfflinePushToken(Constants.OPPO_PUSH_BUZID, token);
        }else if(IMFunc.isBrandVivo()){
            param = new TIMOfflinePushToken(Constants.VIVO_PUSH_BUZID, token);
        }else{
            return;
        }
        TIMManager.getInstance().setOfflinePushToken(param, new TIMCallBack() {
            @Override
            public void onError(int code, String desc) {
                Log.d(TAG, "setOfflinePushToken err code = " + code);
            }
            @Override
            public void onSuccess() {
                Log.d(TAG, "setOfflinePushToken success");
                mIsTokenSet = true;
            }
        });
    }
}
```

### 步骤6：离线推送

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过 OPPO 推送通知到用户端。

>?
>- OPPO 推送的常见问题请参见 [OPPO PUSH FAQ]( https://open.oppomobile.com/wiki/doc#id=10200)。
>- 若即时通信 IM 用户已经 logout 或被即时通信 IM 服务端主动下线（例如在其他端登录被踢等情况），则该设备上不会再收到消息推送。

[](id:click)
## 配置点击通知栏消息事件

您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

[](id:App)
### 打开应用

默认为点击通知栏消息打开应用。

[](id:Webpage)
### 打开网页

您需要在 [添加证书](#Step2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。

[](id:AppInterface)
### 打开应用内指定界面

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


[](id:Trans)
## 透传自定义内容

### 步骤1：发送端设置自定义内容
在发消息前设置每条消息的通知栏自定义内容。
>!OPPO 要求自定义的数据必须是 json 格式。

- Android 端示例如下：
```
  JSONObject jsonObject = new JSONObject();
  try {
  	jsonObject.put("extKey", "ext content");
  } catch (JSONException e) {
  	e.printStackTrace();
  }
  String extContent = jsonObject.toString();

  TIMMessageOfflinePushSettings settings = new TIMMessageOfflinePushSettings();
  settings.setExt(extContent.getBytes());
  timMessage.setOfflinePushSettings(settings);
  mConversation.sendMessage(false, timMessage, callback);
```
	
- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E)。


### 步骤2：接收端获取自定义内容

在控制台选择设置点击通知 [打开应用](#App) 、 [打开应用内指定界面](#AppInterface) 的 Intent action 选项或者 Activity 选项后，当点击通知栏的消息时，客户端在相应的 `Activity` 中获取自定义内容。
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

## 常见问题


### 能否自定义配置推送提示音？

目前 OPPO 推送不支持自定义的提示音。

### 收不到推送时，如何排查问题？
1. 任何推送都不是100%必达，厂商推送也不例外。因此，若在快速、连续的推送过程中偶现一两条推送未通知提醒，通常是由厂商推送频控的限制引起。
2. 按照推送的流程，确认 OPPO 推送证书信息是否正确配置在 [即时通信 IM 控制台](https://console.qcloud.com/avc) 中。
3. 确认您的项目 [集成 OPPO 推送 SDK](#Step4) 的配置正确，并正常获取到了 regId。
4. 确认您已将正确的 [推送信息上报](#Step5) 至即时通信 IM 服务端。
5. 在设备中手动 kill App，发送若干条消息，确认是否能在一分钟内接收到通知。



