即时通信 IM 的离线推送功能由 [TPNS（Tencent Push Notification Service）](https://cloud.tencent.com/document/product/548/36645)提供，本文向您介绍接入 TPNS 并跑通离线推送功能的详细步骤。

>!
>- 接入 TPNS 需升级 IM SDK 至 [6.0.1975 及以上版本](https://cloud.tencent.com/document/product/269/36887)。

## 接入 TPNS 跑通离线推送功能

[](id:step1)
### 步骤一：注册应用到厂商推送平台

离线推送功能依赖厂商原始通道，您需要将自己的应用注册到各个厂商的推送平台，得到 AppID 和 AppKey 等参数。目前国内支持的手机厂商有：[小米](https://dev.mi.com/console/doc/detail?pId=68)、[华为](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060)、[OPPO](https://open.oppomobile.com/wiki/doc#id=10195)、[VIVO](https://dev.vivo.com.cn/documentCenter/doc/281)、[魅族](http://open-wiki.flyme.cn/doc-wiki/index#id?129)，海外支持 [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn)。

[](id:step2)
### 步骤二：TPNS 控制台配置 
如果您之前没有在 IM 控制台配置过离线推送信息，请您直接登录到 [TPNS 控制台](https://console.cloud.tencent.com/tpns/product) ，按照下面的步骤配置离线推送信息。
1. 创建产品：进入 **TPNS 控制台** > **产品管理** > **新增产品**，输入名称和描述等信息。
>! 服务接入点的选择：
>- 需要接入 Google FCM 支持海外客户，请选择新加坡/中国香港接入点。
>- 仅支持国内客户，请选择广州/上海接入点。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2253167ef7cdb850b22e6f603a68a6aa.png)
2. 在**基础配置**栏，选择新增的产品，输入配置应用的包名。
![](https://qcloudimg.tencent-cloud.cn/raw/eaec2f774dfe3efb552d75a043b917e4.png)
3. 产品创建成功后，得到 TPNS 的 AccessID 和 AsscessKey 等参数。
![](https://qcloudimg.tencent-cloud.cn/raw/aa8ecc7474d153afc23ba31474a8d087.png)
4. 配置厂商推送参数：进入 **TPNS 控制台** > **选择产品** > **基础配置** > **选择厂商通道** > **开启**，将您在步骤一中获取的各厂商的  AppID、AppKey、AppSecret 等参数配置给 TPNS。
<table>
<thead><tr><th>厂商</th><th>厂商推送平台</th><th>TPNS 厂商通道配置</th></tr></thead>
<tbody><tr>
<td>小米</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/235758a1895063b7b99f67cc4ef8e4f3.png" alt=""></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/4d3478e48213c849a26f05274bca2c96.png" alt=""></td>
</tr><tr>
<td>华为</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/f8c7c0c9c259919c1f93e79707ddde1d.png" alt=""></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/0b9bf72afcd07318dbd73629256e676f.png" alt=""></td>
</tr><tr>
<td>OPPO</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/051de434b51f77711e5a6aa7682abb72.png" alt=""></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/d910fa76031b8b7c7c302fd50b01eeab.png" alt=""></td>
</tr><tr>
<td>vivo</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/a764b271e3ac1de64b3c9342fa9e96b1.png"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/d15454a306afd84fd3872ac522d01140.png"></td>
</tr><tr>
<td>魅族</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/70ad94d8e843f92247c67a3ae4004c15.png" ></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/58583dd8abbcbc4b97ed958f6ff912d5.png"></td>
</tr><tr>
<td>Google FCM</td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/b344dee87f9d946e21480cd57556730d.png"></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/2fa68e5577e657f6ebabcd9a66d6f656.png"></td>
</tr>
</tbody></table>
5. 第三方服务授权：进入第三方服务授权，把 IM 应用的离线推送功能授权给 TPNS。
    1. 选择云 IM 应用授权，单击**新增授权**。
![](https://qcloudimg.tencent-cloud.cn/raw/55cf9d53a066ee9ec7c9a646c667151e.png)
    2. 选择要授权绑定的 IM 应用，选择新建的 TPNS 产品应用，提交授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/284b12d42b8035311567c1e9eb2de463.png" width=500>

>? 如果您之前已经在 IM 控制台配置了离线推送信息，我们会自动把这些配置信息迁移到  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product)，您可以登录  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product) 修改配置信息。即时通信 IM 会继续使用这些配置信息进行离线推送。
![](https://qcloudimg.tencent-cloud.cn/raw/2a9c1c81da25d94d55227e0223495111.png)

[](id:step3)
### 步骤三：TPNS 工程配置
在**配置管理**页面中， 单击**快速接入**。
1. 参照快速接入第 1 步指引，下载 `tpns-configs.json` 文件，并将其添加到您的 Android Studio 工程里。
![](https://qcloudimg.tencent-cloud.cn/raw/18e22286a9c159b75e7ac31dfefd3220.png)
2. 参照快速接入第 2 步指引，添加工程配置，分别修改项目和应用的 gradle 配置。
![](https://qcloudimg.tencent-cloud.cn/raw/12a5120ec10eeec69035f229db7c6f0c.png)

[](id:step4)
### 步骤四：配置离线推送跳转参数
收到离线推送后，通知栏会显示推送信息，如图所示，单击通知栏会打开应用并进入配置的跳转界面。请您参照下面的步骤，配置单击通知消息后跳转的 Activity。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7e6b56b3bb60bc9ccf7d5d0179eb51ea.png" width=400>
1. 在 TPNS 控制台配置跳转参数，跳转参数配置的格式是：`protocol://hostname/path/`。
 ![](https://qcloudimg.tencent-cloud.cn/raw/d85b48a8e6014a984ea83af6683e5fdb.png)
2. 在 [清单文件 AndroidManifest.xml](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/AndroidManifest.xml) 中完成离线推送跳转参数的配置。
>! 该跳转参数必须与您在 TPNS 控制台的配置保持一致。
>
```
<activity
    android:name="您应用跳转界面的完整类名"
    android:launchMode="singleTask"
    android:screenOrientation="portrait"
    android:windowSoftInputMode="adjustResize|stateHidden">

        <intent-filter>
            <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <!-- Scheme协议开发者可以自定义，格式是：protocol://hostname/path/。-->
                <data
                    android:host="您配置的 hostname"
                    android:path="您配置的 path"
                    android:scheme="您配置的协议，也就是你定义的 scheme" />
        </intent-filter>

</activity>
```
 

[](id:step5)
### 步骤五：配置 TPNS 推送规则

在 [清单文件 AndroidManifest.xml](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/AndroidManifest.xml) 中配置 TPNS 推送规则，例如 TPNS 服务接入点、TPNS 推送类等。

```
<!-- 第一步：配置 TPNS 服务接入点，参照步骤二 TPNS 控制台新建产品时选择的服务接入点。如果需要接入Google FCM支持海外客户，请选择新加坡/香港接入点；如果仅支持国内客户，TPNS 默认的服务接入点为广州，不需要额外配置：

        上海：tpns.sh.tencent.com
        新加坡：tpns.sgp.tencent.com
        中国香港：tpns.hk.tencent.com -->

<!-- 配置格式如下 -->
<meta-data
       android:name="XG_SERVER_SUFFIX"
       android:value="其他服务接入点域名" />

<!-- 第二步：TPNS receiver，离线推送接收消息和结果反馈的 Receiver，像消息透传、注册 token 回调等-->
<receiver android:name="com.tencent.qcloud.tim.demo.thirdpush.TPNSPush.TPNSMessageReceiver">
    <intent-filter>
        <!-- 接收消息透传 -->
        <action android:name="com.tencent.android.xg.vip.action.PUSH_MESSAGE" />
        <!-- 监听注册、反注册、设置/删除标签、通知被单击等处理结果 -->
        <action android:name="com.tencent.android.xg.vip.action.FEEDBACK" />
    </intent-filter>
</receiver>

<!-- 第三步：TPNS 如需兼容 Android P，需要添加使用 Apache HTTP client 库，在 AndroidManifest 的 application 节点内添加以下配置即可。-->
<uses-library android:name="org.apache.http.legacy" android:required="false"/>
```

[](id:step6)
### 步骤六：集成 TPNS SDK
请您按照下面的步骤接入 TPNS SDK，示例代码可以参照 [TPNSPushSetting](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/thirdpush/TPNSPush/TPNSPushSetting.java) 的 init() 方法。

1. 在 [gradle](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/build.gradle) 文件中添加各厂商推送 SDK，以及在步骤二中产品创建成功之后，得到 AccessID 和 AsscessKey 参数。
```
android {
    ......
    defaultConfig {
        ......

        manifestPlaceholders = [
            // 步骤二中，TPNS 控制台获取
            XG_ACCESS_ID : "注册应用的accessid",
            XG_ACCESS_KEY : "注册应用的accesskey",
        ]
        ......
    }
    ......
}

dependencies {
    ......
    // 主包
    implementation 'com.tencent.tpns:tpns:1.3.1.1-release'
    // 小米
    implementation "com.tencent.tpns:xiaomi:1.3.1.1-release"
    // 魅族
    implementation "com.tencent.tpns:meizu:1.3.1.1-release"
    // OPPO
    implementation "com.tencent.tpns:oppo:1.3.1.1-release"
    // vivo
    implementation "com.tencent.tpns:vivo:1.3.1.1-release"
    // 华为
    implementation 'com.tencent.tpns:huawei:1.3.1.1-release'
    implementation 'com.huawei.hms:push:5.0.2.300'
}
```
2. 应用启动后，注册 TPNS 服务，保存注册成功后拿到的 token。
```
final Context context = DemoApplication.instance();

XGPushConfig.enableDebug(context, true);
// 以 OPPO 为例
XGPushConfig.setOppoPushAppId(context, PrivateConstants.OPPO_PUSH_APPKEY);
XGPushConfig.setOppoPushAppKey(context, PrivateConstants.OPPO_PUSH_APPSECRET);
// 重要：开启厂商通道注册
XGPushConfig.enableOtherPush(context, true);
// 注册 TPNS 推送服务
XGPushManager.registerPush(context, new XGIOperateCallback() {
        @Override
        public void onSuccess(Object o, int i) {
            DemoLog.w(TAG, "tpush register success token: " + o);
            // 该 token 需要保存给后续流程使用
            String token = (String) o;
        }

        @Override
        public void onFail(Object o, int i, String s) {
            DemoLog.w(TAG, "tpush register failed errCode: " + i + ", errMsg: " + s);
        }
});
```
- IM 登录成功后，调用 IM SDK 的 [setOfflinePushConfig](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 接口上报 TPNS token。
>! 构造 V2TIMOfflinePushConfig 类，需设置 businessID 为0，isTPNSToken 为 true，上报注册 TPNS 获取的 token。
>
```
V2TIMOfflinePushConfig v2TIMOfflinePushConfig = null;
// 需要设置 businessID 为0，isTPNSToken 为 true，上报 token 为第2步中通过 TPNS 注册后得到的。  
v2TIMOfflinePushConfig = new V2TIMOfflinePushConfig(0, token, true);
V2TIMManager.getOfflinePushManager().setOfflinePushConfig(v2TIMOfflinePushConfig, new V2TIMCallback() {
        @Override
        public void onError(int code, String desc) {
            DemoLog.d(TAG, "setOfflinePushToken err code = " + code);
        }

        @Override
        public void onSuccess() {
            DemoLog.d(TAG, "setOfflinePushToken success");
        }
});
```
3. 在 TPNS 推送类 [TPNSMessageReceiver](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/thirdpush/TPNSPush/TPNSMessageReceiver.java) 中，监听到 TPNS token 发生变化时，请您重新上报 TPNS token。
```
/**
 *  注册回调
 * @param context
 * @param errorCode 0 为成功，其它为错误码
 */
@Override
public void onRegisterResult(Context context, int errorCode, XGPushRegisterResult message) {
  if (context == null || message == null) {
    return;
  }
  String text = "";
  if (errorCode == XGPushBaseReceiver.SUCCESS) {
    String token = message.getToken();
    text = "注册成功1. token：" + token;
    // 调用 IM SDK 的 setOfflinePushConfig 接口上报 TPNS token
    ...
  } else {
    text = message + "注册失败，错误码：" + errorCode;
  }
}

```
- 成功上报 TPNS token 后，将 IM 登录的账号与 TPNS 进行绑定，开始接收离线推送。
``` 
public void bindUserID(String userId) {
    // 重要：IM 登录用户账号时，调用 TPNS 账号绑定接口绑定业务账号，即可以此账号为目标进行 TPNS 离线推送
    XGPushManager.AccountInfo accountInfo = new XGPushManager.AccountInfo(
            XGPushManager.AccountType.UNKNOWN.getValue(), userId);
    XGPushManager.upsertAccounts(DemoApplication.instance(), Arrays.asList(accountInfo), new XGIOperateCallback() {
        @Override
        public void onSuccess(Object o, int i) {
            DemoLog.w(TAG, "upsertAccounts success");
        }

        @Override
        public void onFail(Object o, int i, String s) {
            DemoLog.w(TAG, "upsertAccounts failed");
        }
    });
}
```
- IM 账号登出时，需要与 TPNS 进行账号解绑，停止接收离线推送。
```
public void unBindUserID(String userId) {
        // TPNS 账号解绑业务账号
        XGIOperateCallback xgiOperateCallback = new XGIOperateCallback() {
            @Override
            public void onSuccess(Object data, int flag) {
                DemoLog.i(TAG, "onSuccess, data:" + data + ", flag:" + flag);
            }
            @Override
            public void onFail(Object data, int errCode, String msg) {
                DemoLog.w(TAG, "onFail, data:" + data + ", code:" + errCode + ", msg:" + msg);
            }
        };

        //XGPushManager.delAccount(context, UserInfo.getInstance().getUserId(), xgiOperateCallback);
        Set<Integer> accountTypeSet = new HashSet<>();
        accountTypeSet.add(XGPushManager.AccountType.CUSTOM.getValue());
        accountTypeSet.add(XGPushManager.AccountType.IMEI.getValue());
        XGPushManager.delAccounts(DemoApplication.instance(), accountTypeSet, xgiOperateCallback);
} 
``` 
- 如果您的应用退到后台，收到新消息时需要在手机通知栏进行展示，请您调用 IM SDK 的 [doBackground()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a2b191294ac4d68a2d69e482eae1b638f) 接口，将应用的状态同步给 IM 后台；当应用回到前台时，请您调用 IM SDK 的 [doForeground()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a4c2ff4eea609da1d0950648905fbf6aa) 接口，将应用的状态同步给 IM 后台。监听 APP 前后台切换的方案推荐您参考 [DemoApplication](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/DemoApplication.java) 的 StatisticActivityLifecycleCallback 类相关逻辑。
```
// 应用切到后台时
V2TIMManager.getOfflinePushManager().doBackground(totalCount, new V2TIMCallback() {
    @Override
    public void onError(int code, String desc) {
        DemoLog.e(TAG, "doBackground err = " + code + ", desc = " + desc);
    }

    @Override
    public void onSuccess() {
        DemoLog.i(TAG, "doBackground success");
    }
});
// 应用切回前台时
V2TIMManager.getOfflinePushManager().doForeground(new V2TIMCallback() {
    @Override
    public void onError(int code, String desc) {
        DemoLog.e(TAG, "doForeground err = " + code + ", desc = " + desc);
    }

    @Override
    public void onSuccess() {
        DemoLog.i(TAG, "doForeground success");
    }
});
```
- 完成以上配置之后，可以在 TPNS 控制台 [推送任务](https://console.cloud.tencent.com/tpns/push) 里，测试离线推送消息，确保已成功集成。
![](https://qcloudimg.tencent-cloud.cn/raw/250b5ef9c7e1fc66af4bdf028f2820fe.png)

[](id:step7)
### 步骤七：发消息时设置离线推送参数

调用 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) 发送消息时，您可以通过 V2TIMOfflinePushInfo 设置离线推送参数，可以参照 [ChatProvider](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/model/ChatProvider.java) 的 sendMessage() 方法：

```
OfflineMessageContainerBean containerBean = new OfflineMessageContainerBean();
OfflineMessageBean entity = new OfflineMessageBean();
entity.content = message.getExtra().toString();
entity.sender = message.getFromUser();
entity.nickname = chatInfo.getChatName();
entity.faceUrl = TUIChatConfigs.getConfigs().getGeneralConfig().getUserFaceUrl();
containerBean.entity = entity;
        
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
v2TIMOfflinePushInfo.setExt(new Gson().toJson(containerBean).getBytes());
// OPPO必须设置ChannelID才可以收到推送消息，这个channelID需要和控制台一致
v2TIMOfflinePushInfo.setAndroidOPPOChannelID("tuikit");

final V2TIMMessage v2TIMMessage = message.getTimMessage();
String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null,
    V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
        @Override
        public void onProgress(int progress) {

        }

        @Override
        public void onError(int code, String desc) {
            TUIChatUtils.callbackOnError(callBack, TAG, code, desc);
        }

        @Override
        public void onSuccess(V2TIMMessage v2TIMMessage) {
            TUIChatLog.v(TAG, "sendMessage onSuccess:" + v2TIMMessage.getMsgID());
            message.setMsgTime(v2TIMMessage.getTimestamp());
            TUIChatUtils.callbackOnSuccess(callBack, message);
        }
    });
```

[](id:step8)
### 步骤八：解析离线推送消息

当手机收到离线推送消息时，会在系统通知栏里展示收到的推送消息。单击通知栏的消息时，会自动跳转到您在步骤四配置的界面，您可以在该界面通过调用 `getIntent().getData()` 获取您在 [步骤七](#step7) 中配置的离线推送参数。示例代码可以参考 TUIKitDemo 的 [handleOfflinePush()](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/main/MainActivity.java) 方法。


```
private void handleOfflinePush() {
    // 根据登录状态，判断是否需要重新登录 IM
    // 1. 如果登录状态为 V2TIMManager.V2TIM_STATUS_LOGOUT，跳转到登录界面，重新登录 IM
    if (V2TIMManager.getInstance().getLoginStatus() == V2TIMManager.V2TIM_STATUS_LOGOUT) {
        Intent intent = new Intent(MainActivity.this, SplashActivity.class);
        if (getIntent() != null) {
            intent.setData(getIntent().getData());
        }
        startActivity(intent);
        finish();
        return;
    }
 
    // 2. 否则，说明 App 只是处于退后台的状态，直接解析离线推送参数
    final OfflineMessageBean bean = OfflineMessageDispatcher.parseOfflineMessage(getIntent());
    if (bean != null) {
        setIntent(null);
        NotificationManager manager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        if (manager != null) {
            manager.cancelAll();
        }

        if (bean.action == OfflineMessageBean.REDIRECT_ACTION_CHAT) {
            if (TextUtils.isEmpty(bean.sender)) {
                return;
            }
            TUIKit.startChat(bean.sender, bean.nickname, bean.chatType);
        } else if (bean.action == OfflineMessageBean.REDIRECT_ACTION_CALL) {
            IBaseLiveListener baseCallListener = TUIKitLiveListenerManager.getInstance().getBaseCallListener();
            if (baseCallListener != null) {
                baseCallListener.handleOfflinePushCall(bean);
            }
        }
    }
}
    
```


## 常见问题
### Android 手机离线推送怎么自定义推送的声音？
目前大部分厂商都不支持离线推送声音的设置，因此 IM SDK 暂时不支持。

### OPPO 手机为什么收不到离线推送？
OPPO 手机收不到推送一般有以下几种情况：

- 按照 OPPO 推送官网要求，在 Android 8.0 及以上系统版本的 OPPO 手机上必须配置 ChannelID，否则推送消息无法展示。配置方法可请参见 [OPPO 推送配置](https://cloud.tencent.com/document/product/269/44516#oppo-.E6.8E.A8.E9.80.81)。
- 在消息中 [透传的离线推送的自定义内容](https://cloud.tencent.com/document/product/269/44516#.E9.80.8F.E4.BC.A0.E8.87.AA.E5.AE.9A.E4.B9.89.E5.86.85.E5.AE.B93) 不是 JSON 格式，会导致 OPPO 手机收不到推送。

### 自定义消息为什么收不到离线推送？

自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 的 [desc](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 字段，推送的时候会默认展示 desc 信息。

### 收不到离线推送消息?
按照文档指引流程执行后，离线推送功能即可正常运行。如果遇到收不到离线消息，可能存在如下情况：
- 首先在 IM 控制台通过 [离线测试工具](https://console.cloud.tencent.com/im-detail/tool-push-check)，或者 TPNS 控制台 [推送任务](https://console.cloud.tencent.com/tpns/push) 新建推送测试，自测下是否可以正常推送。
推送异常情况，设备状态异常，需要检查下 IM 控制台配置各项参数是否正确，再者需要检查下代码初始化注册逻辑，包括厂商推送服务注册和 IM 设置离线推送配置相关逻辑是否正确设置。
推送异常情况，设备状态正常，需要看下是否需要正确填写 channelID 或者后台服务是否正常。

- 离线推送依赖厂商能力，一些简单的字符可能会被厂商过滤不能透传推送。另外，一些厂商对通知进行分类，不同类型有不同的推送策略，会出现推送不及时或者不推送情况，该情况需要去对应厂商官网为应用申请高权限分类权益，即可高效实时推送。

### 跳转界面不成功?
单击离线推送消息的通知栏，跳转到指定界面，原理是后台根据您在控制台配置的各个厂商的跳转方式和界面参数，根据厂商接口规则，传递给厂商服务器，单击时候进行对应界面启动跳转。对应界面启动还依赖清单文件的配置，必须和控制台配置的相对应，才能正确启动和跳转。

所以，跳转界面不成功，需要重点排查下控制台和清单文件相关配置是否对应且正确，可参照 TUIKitDemo 的配置，注意部分厂商提供接口方式存在差异。

