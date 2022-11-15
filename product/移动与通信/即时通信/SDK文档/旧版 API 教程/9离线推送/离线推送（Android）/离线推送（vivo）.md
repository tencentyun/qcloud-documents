## 离线推送流程
实现离线消息推送的过程如下：
1. 开发者到厂商的平台注册帐号，并通过开发者认证后，申请开通推送服务。
2. 创建推送服务，并绑定应用信息，获取推送证书、密码、密钥等信息。
3. 登录 [即时通信 IM 控制台](https://console.qcloud.com/avc) 填写推送证书及相关信息，即时通信 IM 服务端会为每个证书生成不同的证书 ID。
4. 将厂商提供的推送 SDK 集成到开发者的项目工程中，并按各厂商的要求进行配置。
5. 集成即时通信 IM SDK 到项目后，将证书 ID、设备信息等上报至即时通信 IM 服务端。
6. 当客户端 App 在即时通信 IM 没有退出登录的情况下，被系统或者用户 kill 时，即时通信 IM 服务端将通过消息推送进行提醒。

## 配置离线推送

vivo 手机使用深度定制 Android 系统，对于第三方 App 自启动权限管理很严格，默认情况下第三方 App 都不会在系统的自启动白名单内，App 在后台时容易被系统 kill，因此推荐在 vivo 设备上集成 vivo 推送，vivo 推送 是 vivo 设备的系统级服务，推送到达率较高。目前，**即时通信 IM 仅支持 vivo 推送的通知栏消息**。

>!
>- 此指引文档是直接参考 vivo 推送官方文档所写，若 vivo 推送有变动，请以 [vivo 推送官网文档](https://dev.vivo.com.cn/documentCenter/doc/180) 为准。
>- 如果不需要对 vivo 设备做专门的离线推送适配，可以忽略此章节。

[](id:Step1)
### 步骤1：申请 vivo 推送证书
1. 打开 [vivo 开放平台官网](https://dev.vivo.com.cn/home) 进行注册并通过开发者认证。
 >?认证过程大约需要3天左右，请务必提前阅读 [vivo 推送服务说明](https://dev.vivo.com.cn/documentCenter/doc/180)，以免影响您的接入进度。
2. 登录 vivo 开放平台的管理中心，选择【消息推送】>【创建】>【测试推送】，创建 vivo 推送服务应用。
 vivo 推送服务应用创建完成后，在应用详情中，您可以查看详细的应用信息。
[](id:Step1_3)
3. 记录**`APP ID`**、**`APP key`**和**`APP secret`**信息。

[](id:Step2)
### 步骤2：托管证书信息到即时通信 IM
1. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【Android平台推送设置】区域的【添加证书】。
 >?如果您原来已有证书只需变更信息，可以单击对应证书区域的【编辑】进行修改更新。
 >
 ![](https://main.qcloudimg.com/raw/aaa40b3c7e43f99b7e36c8b7589e54e0.png)
3. 根据 [步骤1](#Step1_3) 中获取的信息设置以下参数：
 - **推送平台**：选择 **vivo**
 - **AppKey**：填写 vivo 推送服务应用的 **APP key**
 - **AppID**：填写 vivo 推送服务应用的 **APP ID**
 - **AppSecret**：填写 vivo 推送服务应用的 **APP secret**
 - **点击通知后**：选择点击通知栏消息后的响应操作，支持**打开应用**、**打开网页**和**打开应用内指定界面**，更多详情请参见 [配置点击通知栏消息事件](#click)
  当设置为【打开应用】或【打开应用内指定界面】操作时，支持 [透传自定义内容](#section4)。
 ![](https://main.qcloudimg.com/raw/ac890d834dd7f069f936094180634cd7.png)
4. 单击【确认】保存信息，证书信息保存后10分钟内生效。
5. 待推送证书信息生成后，记录证书的**`ID`**。
 ![](https://main.qcloudimg.com/raw/3442e00debac668c42fa4be89903ac90.png)

[](id:Step3)
### 步骤3：集成推送 SDK
>?
> - 即时通信 IM 默认推送的通知标题为`a new message`。
> - 阅读此小节前，请确保您已经正常集成并使用即时通信 IM SDK。
> - 您可以在我们的 demo 里找到 vivo 推送的实现示例，请注意： vivo 推送版本更新时有可能会有功能调整，若您发现本节内容存在差异，烦请您及时查阅 [vivo 推送官网文档](https://dev.vivo.com.cn/documentCenter/doc/155)，并将文档信息差异反馈给我们，我们会及时跟进修改。

#### 步骤3.1：下载 vivo 推送 SDK 并添加引用
1. 访问 [vivo 推送运营平台](https://dev.vivo.com.cn/documentCenter/doc/232) 下载 vivo 推送 SDK。
2. 解压 vivo 推送 SDK，获取`vivo_pushsdk_xxx.jar`库文件。
3. 将`vivo_pushsdk_xxx.jar`库文件添加到您项目的`libs`目录下，并且在项目中添加引用。


#### 步骤3.2：配置 AndroidManifest.xml 文件

添加 vivo 推送服务需要的配置：

```xml
<!-- ********vivo 推送设置 start******** -->
<service
         android:name="com.vivo.push.sdk.service.CommandClientService"
         android:exported="true" />
<activity
          android:name="com.vivo.push.sdk.LinkProxyClientActivity"
          android:exported="false"
          android:screenOrientation="portrait"
          android:theme="@android:style/Theme.Translucent.NoTitleBar" />
<meta-data
           android:name="com.vivo.push.api_key"
           android:value="a90685ff-ebad-4df3-a265-3d4bb8e3a389" />
<meta-data
           android:name="com.vivo.push.app_id"
           android:value="11178" />
<!-- ********vivo 推送设置 end******** -->
<!--这里的 com.vivo.push.app_id ，com.vivo.push.api_key 由 vivo 开放平台生成 -->
```

#### 步骤3.3：自定义一个 BroadcastReceiver 类

为了接收消息，您需要自定义一个继承自`OpenClientPushMessageReceiver`类的 BroadcastReceiver，并实现其中的`onReceiveRegId`和`onNotificationMessageClicked`方法，然后将此 receiver 注册到 AndroidManifest.xml 中。

以下为 Demo 中的示例代码：

```java
public class VIVOPushMessageReceiverImpl extends OpenClientPushMessageReceiver {
    private static final String TAG = "VIVOPushMessageReceiver";
    @Override
    public void onNotificationMessageClicked(Context context, UPSNotificationMessage upsNotificationMessage) {
        Log.i(TAG, "onNotificationMessageClicked");
    }

    @Override
    public void onReceiveRegId(Context context, String regId) {
        // vivo regId 有变化会走这个回调。根据官网文档，获取 regId 需要在开启推送的回调里面调用PushClient.getInstance(getApplicationContext()).getRegId();参考 LoginActivity
        Log.i(TAG, "onReceiveRegId = " + regId);
    }
}
```

将自定义的 BroadcastReceiver 注册到 AndroidManifest.xml：

```xml
<!--这里的 com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl 修改成您 App 中的完整类名-->
<!-- push 应用定义消息 receiver 声明 -->
<receiver android:name="com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl">
    <intent-filter>
        <!-- 接收 push 消息 -->
        <action android:name="com.vivo.pushclient.action.RECEIVE" />
    </intent-filter>
</receiver>
```

#### 步骤3.4：在 App 中注册 vivo 推送服务

如果您选择启用 vivo 离线推送，需要向 vivo 服务器注册推送服务，通过调用`PushClient.getInstance(getApplicationContext()).initialize()`来对 vivo 推送服务进行初始化。`PushClient.getInstance(getApplicationContext()).initialize()`可在任意地方调用，为了提高注册成功率，vivo 官方建议在 Application 的`onCreate`中调用。

注册成功后，需要在您的 App 主界面中获取注册结果。其中`regId`为当前设备上当前 App 的唯一标识，请记录`regId`信息。

以下为 Demo 中的示例代码：

```java
public class DemoApplication extends Application {

    private static PojoApplication instance;

    @Override
    public void onCreate() {
        super.onCreate();
        // 判断是否是在主线程
        if (SessionWrapper.isMainProcess(getApplicationContext())) {
            /**
             * TUIKit 的初始化函数
             *
             * @param context  应用的上下文，一般为对应应用的 ApplicationContext
             * @param sdkAppID 您在腾讯云注册应用时分配的 SDKAppID
             * @param configs  TUIKit 的相关配置项，一般使用默认即可，需特殊配置参考 API 文档
             */
            long current = System.currentTimeMillis();
            TUIKit.init(this, Constants.SDKAPPID, BaseUIKitConfigs.getDefaultConfigs());
            System.out.println(">>>>>>>>>>>>>>>>>>"+(System.currentTimeMillis()-current));
            // 添加自定初始化配置
            customConfig();
            System.out.println(">>>>>>>>>>>>>>>>>>"+(System.currentTimeMillis()-current));

            if(IMFunc.isBrandXiaoMi()){
                // 小米离线推送
                MiPushClient.registerPush(this, Constants.XM_PUSH_APPID, Constants.XM_PUSH_APPKEY);
            }
            if(IMFunc.isBrandHuawei()){
                // 华为离线推送
                HMSAgent.init(this);
            }
            if(MzSystemUtils.isBrandMeizu(this)){
                // 魅族离线推送
                PushManager.register(this, Constants.MZ_PUSH_APPID, Constants.MZ_PUSH_APPKEY);
            }
            if(IMFunc.isBrandVivo()){
                // vivo 离线推送
                PushClient.getInstance(getApplicationContext()).initialize();
            }
        }
        instance = this;
	}
}
```

在主界面中打开 vivo push 服务：

<pre>
if (IMFunc.isBrandVivo()) {
    // vivo 离线推送
    PushClient.getInstance(getApplicationContext()).turnOnPush(new IPushActionListener() {
        @Override
        public void onStateChanged(int state) {
            if (state == 0) {
                String regId = PushClient.getInstance(getApplicationContext()).getRegId();
                QLog.i(TAG, "vivopush open vivo push success regId = " + regId);
                ThirdPushTokenMgr.getInstance().setThirdPushToken(regId);
                ThirdPushTokenMgr.getInstance().setPushTokenToTIM();
            } else {
                // 根据 vivo 推送文档说明，state = 101表示该 vivo 机型或者版本不支持 vivo 推送，详情请参考 <a href="https://dev.vivo.com.cn/documentCenter/doc/156">vivo 推送常见问题汇总</a>
                QLog.i(TAG, "vivopush open vivo push fail state = " + state);
            }
        }
    });
</pre>

[](id:Step4)
### 步骤4：上报推送信息至即时通信 IM 服务端
若您需要通过 vivo 推送进行即时通信 IM 消息的推送通知，必须在**用户登录成功后**通过`TIMManager`中的`setOfflinePushToken`方法将您托管到即时通信 IM 控制台生成的**证书 ID** 及 vivo 推送服务返回的 **regId** 上报到即时通信 IM 服务端。
>!正确上报 regId 与证书 ID 后，即时通信 IM 服务才能将用户与对应的设备信息绑定，从而使用 vivo 推送服务进行推送通知。

以下为 Demo 中的示例代码：

- 定义证书 ID 常量：

```java
/**
 * 我们先定义一些常量信息在 Constants.java
 */
/****** vivo 离线推送参数 start ******/
// 在腾讯云控制台上传第三方推送证书后分配的证书 ID
public static final long VIVO_PUSH_BUZID = 6666;
// vivo 开放平台分配的应用 APPID 及 APPKEY
public static final String VIVO_PUSH_APPID = "1234512345123451234"; // 见清单文件
public static final String VIVO_PUSH_APPKEY = "12345abcde"; // 见清单文件
/****** vivo 离线推送参数 end ******/
```

- 上报推送的证书 ID 及 regId：

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
        if(mIsTokenSet){
            QLog.i(TAG, "setPushTokenToTIM mIsTokenSet true, ignore");
            return;
        }
        String token = ThirdPushTokenMgr.getInstance().getThirdPushToken();
        if(TextUtils.isEmpty(token)){
            QLog.i(TAG, "setPushTokenToTIM third token is empty");
            mIsTokenSet = false;
            return;
        }
        if( !mIsLogin ){
            QLog.i(TAG, "setPushTokenToTIM not login, ignore");
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

### 步骤5：离线推送

成功上报证书 ID 及 regId 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后，将消息通过 vivo 推送通知到用户端。

>?
>- vivo 推送只支持部分 vivo 手机，详情请参见 [vivo 推送常见问题汇总]( https://dev.vivo.com.cn/documentCenter/doc/156)。
>- vivo 推送并非100%必达。
>- vivo 推送可能会有一定延时，通常与 App 被 kill 的时机有关，部分情况下与 vivo 推送服务有关。
>- 若即时通信 IM 用户已经 logout 或被即时通信 IM 服务端主动下线（例如在其他端登录被踢等情况），则该设备上不会再收到消息推送。

[](id:click)
## 配置点击通知栏消息事件
您可以选择点击通知栏消息后**打开应用**、**打开网页**或**打开应用内指定界面**。

### 打开应用
默认为点击通知栏消息打开应用。
![](https://main.qcloudimg.com/raw/ac890d834dd7f069f936094180634cd7.png)

### 打开网页
您需要在 [添加证书](#Step2) 时选择【打开网页】并输入以`http://`或`https://`开头的网址，例如`https://cloud.tencent.com/document/product/269`。
![](https://main.qcloudimg.com/raw/76ebc2f58623241c685ebffab6b4c2f6.png)

### 打开应用内指定界面

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

3. 在 [添加证书](#Step2) 时选择【打开应用内指定界面】并输入上述打印结果。
    ![](https://main.qcloudimg.com/raw/1ab25b8c52b953014786682bce43c2ed.png)

[](id:section4)
## 透传自定义内容
[添加证书](#Step2) 时设置【点击通知后】为【打开应用】或【打开应用内指定界面】操作才支持透传自定义内容。

### 步骤1：发送端设置自定义内容
在发消息前设置每条消息的通知栏自定义内容。
- Android 端示例如下：

  ```
  String extContent = "ext content";
  TIMMessageOfflinePushSettings settings = new TIMMessageOfflinePushSettings();
  settings.setExt(extContent.getBytes());
  timMessage.setOfflinePushSettings(settings);
  mConversation.sendMessage(false, timMessage, callback);
  ```

- 服务端示例请参见 [OfflinePushInfo 的格式示例](https://cloud.tencent.com/document/product/269/2720#.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81-offlinepushinfo-.E8.AF.B4.E6.98.8E)。

### 步骤2：接收端获取自定义内容
点击通知栏的消息时，会触发 vivo 推送 SDK 的 `onNotificationMessageClicked(Context context, UPSNotificationMessage upsNotificationMessage)` 回调，自定义内容可以从 `upsNotificationMessage` 中获取。

  ```
  Map<String, String> paramMap = upsNotificationMessage.getParams();
  String extContent = paramMap.get("ext");
  ```

## 常见问题

### 如果应用使用了混淆，如何防止 vivo 离线推送功能异常？

如果您的应用使用了混淆，为了防止 vivo 离线推送功能异常，您需要 keep 自定义的 BroadcastReceiver，参考添加以下混淆规则：
>?以下代码为 vivo 官方示例，请根据实际情况修改后再使用。

```
# 请将 com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl 改成您 App 中定义的完整类名
# vivo 推送
-dontwarn com.vivo.push.**
-keep class com.vivo.push.**{*; }
-keep class com.vivo.vms.**{*; }
-keep class com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl{*;}
```


### 能否自定义配置推送提示音？

目前 vivo 推送不支持自定义的提示音。

### 收不到推送时，如何排查问题？
1. 任何推送都不是100%必达，厂商推送也不例外。因此，若在快速、连续的推送过程中偶现一两条推送未通知提醒，通常是由厂商推送频控的限制引起。
2. 按照推送的流程，确认 vivo 推送证书信息是否正确配置在 [即时通信 IM 控制台](https://console.qcloud.com/avc) 中。
3. 确认您的项目 [集成 vivo 推送 SDK](#Step3) 的配置正确，并正常获取到了 regId。
4. 确认您已将正确的 [推送信息上报](#Step4) 至即时通信 IM 服务端。
5. 在设备中手动 kill App，发送若干条消息，确认是否能在一分钟内接收到通知。



