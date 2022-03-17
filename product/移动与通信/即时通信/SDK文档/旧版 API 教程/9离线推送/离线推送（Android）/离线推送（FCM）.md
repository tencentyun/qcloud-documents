>!使用 FCM 离线推送需要手机端安装 Google Play Services 且在中国大陆地区以外使用。

## 离线推送流程

实现离线消息推送的过程如下：
1. 开发者到厂商的平台注册帐号，并通过开发者认证后，申请开通推送服务。
2. 创建推送服务，并绑定应用信息，获取推送证书、密码、密钥等信息。
3. 登录 [即时通信 IM 控制台](https://console.qcloud.com/avc) 填写推送证书及相关信息，即时通信 IM 服务端会为每个证书生成不同的证书 ID。
4. 将厂商提供的推送 SDK 集成到开发者的项目工程中，并按各厂商的要求进行配置。
5. 集成即时通信 IM SDK 到项目后，将证书 ID、设备信息等上报至即时通信 IM 服务端。
6. 当客户端 App 在即时通信 IM 没有退出登录的情况下，被系统或者用户 kill 时，即时通信 IM 服务端将通过消息推送进行提醒。

## 配置离线推送
[](id:Step1)
### 步骤1：设置 Firebase 和 FCM SDK
>?本步骤中的网址为 Firebase 官方网址，需要在中国大陆地区以外才能访问。

1. 请参考 [Firebase 云消息传递](https://firebase.google.com/docs/cloud-messaging/android/client) 设置 Firebase，集成 FCM SDK，启动应用后获取设备注册令牌 **token**。
2. 请参考 [FCM 测试指引](https://firebase.google.com/docs/cloud-messaging/android/first-message?authuser=0) 测试通知消息，确保已成功集成 FCM。
3. 登录 [Firebase 控制台](https://console.firebase.google.com)，单击您的应用卡片，进入应用配置页面。
4. 单击 Project Overview 右侧的<img src="https://main.qcloudimg.com/raw/0d062411405553c9fae29f8e0daf02ad.png"  style="margin:0;">，选择【项目设置】>【服务帐号】。
5. 单击【生成新的私钥】下载私钥文件。

[](id:Step2)
### 步骤2：托管证书信息到即时通信 IM 
1. 登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc)，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【Android平台推送设置】区域的【添加证书】。
 >?如果您原来已有证书只需变更信息，可以单击对应证书区域的【编辑】进行修改更新。
 >
 ![](https://main.qcloudimg.com/raw/aaa40b3c7e43f99b7e36c8b7589e54e0.png) 
3. 上传 [步骤1](#Step1) 中获取的私钥文件：
 ![](https://main.qcloudimg.com/raw/b18e2414561c6733b24c56cd1e866f21.png)
4. 单击【确认】保存信息，证书信息保存后10分钟内生效。
5. 待推送证书信息生成后，记录证书的**`ID`**。
 ![](https://main.qcloudimg.com/raw/2199bbf955cf52f09b78af6a97ab8122.png)

[](id:Step3)
### 步骤3：上报推送信息至即时通信 IM 服务端

在**用户登录成功后**通过`TIMManager`中的`setOfflinePushToken`方法将您托管到即时通信 IM 控制台生成的**证书 ID** 及集成 FCM 后在客户端生成的 **token** 上报到即时通信 IM 服务端。

>!正确上报 token 与证书 ID 后，即时通信 IM 服务才能将用户与对应的设备信息绑定，从而使用 FCM 进行推送通知。

以下为 Demo 中的示例代码：

定义证书 ID 常量：
```java
/****** FCM 离线推送参数 start ******/
// 使用您在即时通信 IM 控制台上 FCM 推送证书信息里的证书 ID
public static final long GOOGLE_FCM_PUSH_BUZID = 6768;
/****** FCM 离线推送参数 end ******/
```

上报推送的证书 ID 及 token：
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
  
    public String getThirdPushToken() {
        return mThirdPushToken;
    }

    public void setThirdPushToken(String mThirdPushToken) {
        this.mThirdPushToken = mThirdPushToken;  // token 在此处传值
    }

    public void setPushTokenToTIM(){
        String token = ThirdPushTokenMgr.getInstance().getThirdPushToken();
        if(TextUtils.isEmpty(token)){
            QLog.i(TAG, "setPushTokenToTIM third token is empty");
            mIsTokenSet = false;
            return;
        }
        TIMOfflinePushToken param = new TIMOfflinePushToken(Constants.GOOGLE_FCM_PUSH_BUZID, token);
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

[](id:Step4)
### 步骤4：离线推送

成功上报证书 ID 及 token 后，即时通信 IM 服务端会在该设备上的即时通信 IM 用户 logout 之前、App 被 kill 之后将消息通过 FCM 推送通知到用户端。

>?
> - FCM 推送并非100%必达。
> - FCM 推送可能会有一定延时，通常与 App 被 kill 的时机有关，部分情况下与 FCM 推送服务有关。
> - 若即时通信 IM 用户已经 logout 或被即时通信 IM 服务端主动下线（例如在其他端登录被踢等情况），则该设备上不会再收到消息推送。

## 透传自定义内容

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
当点击通知栏的消息时，客户端在相应的 `Activity` 中获取自定义内容。

  ```
  Bundle bundle = getIntent().getExtras();
  String value = bundle.getString("ext"); 
  ```

## 常见问题

### 能否自定义配置推送提示音？
目前 FCM 推送不支持自定义的提示音。

### 收不到推送时，如何排查问题？
1. 任何推送都不是100%必达，FCM 推送也不例外。因此，若在快速、连续的推送过程中偶现一两条推送未通知提醒，通常是由 FCM 推送频控的限制引起。
2. 按照推送的流程，确认 FCM 推送证书信息是否正确配置在 [即时通信 IM 控制台](https://console.qcloud.com/avc)中。
3. 确认您的 FCM 项目配置正确，并已正常获取 token。
4. 确认您已将正确的 [推送信息上报](#Step3) 至即时通信 IM 服务端。
5. 在设备中手动 kill App，发送若干条消息，确认是否能在一分钟内接收到通知。


