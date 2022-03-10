即时通信 IM 的离线推送功能由 [TPNS（Tencent Push Notification Service）](https://cloud.tencent.com/document/product/548/36645)提供，本文向您介绍接入 TPNS 并跑通离线推送功能的详细步骤。

>!接入 TPNS 需升级 IM Flutter SDK 至 [3.7.2及以上版本](https://cloud.tencent.com/document/product/269/36887#opensource)。
## 接入 TPNS 推送跑通离线推送功能
### 步骤1：申请苹果推送证书
离线推送依赖于苹果的原生推送通道，在配置 TPNS 推送之前，需要参见 [推送证书获取指引](https://cloud.tencent.com/document/product/548/36664)  获取苹果推送证书。

### 步骤2：TPNS 控制台配置

如果您之前没有在 IM 控制台配置过离线推送信息，请您直接登录到 [TPNS 控制台](https://console.cloud.tencent.com/tpns/product) ，按照下面的步骤配置离线推送信息。

1. 进入 **TPNS 控制台** > **产品管理** > **新增产品**, 输入名称和描述等信息。[](id:step1)
>!服务接入点的选择：
>- 需要支持境外客户，请选择新加坡或中国香港接入点。
>- 仅支持国内客户，请选择广州或上海接入点。
>
![](https://qcloudimg.tencent-cloud.cn/raw/44b868c7e3781ceed24c5e1e925ab2c3.png)
2. 在基础配置栏，选择新增的产品，输入配置应用的 BundleID。
![](https://qcloudimg.tencent-cloud.cn/raw/8ab7746b97b0dea6690ec0bdf8cb7c21.png)
3. 产品创建成功后，得到 TPNS 的 AccessID 和 AsscessKey 等参数。
![](https://qcloudimg.tencent-cloud.cn/raw/1f510d09d97d1eb25fd5f4efc51fc7cc.png)
4. 进入 **TPNS 控制台** > **选择产品** > **基础配置** > **推送证书** > **上传**，将您在 [步骤1](#step1) 中申请的苹果推送证书配置到 TPNS。
![](https://qcloudimg.tencent-cloud.cn/raw/f406d41e17ffa726bedb65e2855767ad.png)
5.  进入第三方服务授权，把 IM 应用的离线推送功能授权给 TPNS。
  1. 选择云 IM 应用授权，单击**新增授权**。
![](https://qcloudimg.tencent-cloud.cn/raw/5e6aff8a59c09303897fe7fb040f9fd1.png)
  2. 选择要授权绑定的 IM 应用，选择新建的 TPNS 产品应用，提交授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8b50ddd0eb4b1e3a734845ffd3046226.png" width=450>

>? 如果您之前已经在 IM 控制台配置了离线推送信息, 我们会自动把这些配置信息迁移到  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product)，您可以登录  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product) 修改配置信息。即时通信 IM 会继续使用这些配置信息进行离线推送。
![](https://qcloudimg.tencent-cloud.cn/raw/501fbd5af9d19961827968d608755bf3.png)

### 步骤3：Flutter TPNS 接入
1. 引入 SDK：
```yaml
tpns_flutter_plugin:
    git:
      url: https://github.com/TencentCloud/TPNS-Flutter-Plugin
      ref: V1.1.5
```

2. 通过 TPNS 获取 token：
```dart
import 'package:discuss/utils/toast.dart';
import 'package:tpns_flutter_plugin/tpns_flutter_plugin.dart';

class OfflinePush {
  static final XgFlutterPlugin tpush = XgFlutterPlugin();
  static String deviceToken = "";
  static init() {
    tpush.setEnableDebug(
      !(const bool.fromEnvironment('ISPRODUCT_ENV', defaultValue: false)),
    );
    tpush.addEventHandler(
      onRegisteredDeviceToken: (String msg) async {
        deviceToken = msg;
      },
      onRegisteredDone: (String msg) async {},
      unRegistered: (String msg) async {},
      onReceiveNotificationResponse: (Map<String, dynamic> msg) async {},
      onReceiveMessage: (Map<String, dynamic> msg) async {},
      xgPushDidSetBadge: (String msg) async {},
      xgPushDidBindWithIdentifier: (String msg) async {},
      xgPushDidUnbindWithIdentifier: (String msg) async {},
      xgPushDidUpdatedBindedIdentifier: (String msg) async {},
      xgPushDidClearAllIdentifiers: (String msg) async {},
      xgPushClickAction: (Map<String, dynamic> msg) async {},
    );
    tpush.startXg("", ""); // tpns控制台获取
  }

  static Future<String> getDeviceToken() async {
    String token = "";
    try {
      token = await XgFlutterPlugin.xgApi.getOtherPushToken();
    } catch (err) {
      Utils.log("getDeviceToken err $err");
    }
    return token;
  }
  static Future<String> getTPNSToken() async {
    String token = "";
    try {
      token = await XgFlutterPlugin.xgApi.getXgToken();
    } catch (err) {
      Utils.log("getXgToken err $err");
    }
    return token;
  }
}
OfflinePush.getDeviceToken(); // 旧版本请使用device_token
OfflinePush.getTPNSToken(); // 新版本使用getTPNSToken

```

3. 将 token 上传到 IM：
```dart
// 旧版本
setOfflinePushInfo() async {
    String token = await OfflinePush.getDeviceToken();
    if (token != "") {
      TencentImSDKPlugin.v2TIMManager
          .getOfflinePushManager()
          .setOfflinePushConfig(
            businessID: IMDiscussConfig.pushConfig['ios']!['dev']!,
            token: token,
          );
    }
  }
// 新版本
setOfflinePushInfo() async {
    String token = await OfflinePush.getTPNSToken();
    if (token != "") {
      TencentImSDKPlugin.v2TIMManager
          .getOfflinePushManager()
          .setOfflinePushConfig(
            businessID: 0,
            token: token,
        		isTPNSToken:true,
          );
    }
  }
```


### 步骤4：IM 相关接入[](id:step4)
1. 发消息时设置离线推送参数。调用 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 发送消息时，您可以通过 [OfflinePushInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_offlinePushInfo/OfflinePushInfo-class.html) 设置离线推送参数
```dart
TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(
          id: "",
          receiver: "",
          groupID: "",
          offlinePushInfo: OfflinePushInfo(title: "测试", desc: "测试消息"),
        );
```
2. 解析离线推送的消息。接入 TPNS 之后，可以在 TPNS 的回调 xgPushClickAction 中监听通知栏推送的单击，根据 [步骤4](#step4) 中通过 [OfflinePushInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_offlinePushInfo/OfflinePushInfo-class.html) 设置的离线推送格式解析并跳转。



## 常见问题

### 普通消息为什么收不到离线推送？
首先，请检查下 App 的运行环境和证书的环境是否一致，如果不一致，收不到离线推送。

### 自定义消息为什么收不到离线推送？
自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的 `desc`字段，推送的时候会默认展示 `desc` 信息。

### 如何关闭离线推送消息的接收？
如果您想关闭离线推送消息的接收，可以通过设置 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a6aecbdc0edaa311c3e4e0ed3e71495b1) 接口的 `config` 参数为 `nil` 来实现。该功能从5.6.1200版本开始支持。
