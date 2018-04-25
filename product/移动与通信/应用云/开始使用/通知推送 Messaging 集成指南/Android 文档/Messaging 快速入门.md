## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件（已完成请跳过）

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 messaging 服务依赖：

```
dependencies {
    // 增加这两行
    compile 'com.tencent.tac:tac-core:1.1.0'
    compile 'com.tencent.tac:tac-messaging:1.1.0'
}
```
> `'com.tencent.tac:tac-messaging:1.1.0' ` 默认引入了厂商通道推送包，如果不需要集成厂商推送，您可以改用 `'com.tencent.tac:tac-messaging-lite:1.1.0'`

## 第四步：注册回调

在启动 messaging 服务前，您必须注册 messaging 服务回调接口，用于接收消息在不同状态下的通知：

#### 继承 `TACMessagingReceiver` 类

您必须创建一个 `TACMessagingReceiver` 子类用于接收我们的消息回调：

```
public class MyReceiver extends TACMessagingReceiver {

    // 启动 Messaging 服务后，会自动向 Messaging 后台注册，注册完成后会回调此接口。
    @Override
    public void onRegisterResult(Context context, int errorCode, TACMessagingToken token) {

        Toast.makeText(context, "注册结果返回：" + token, Toast.LENGTH_SHORT).show();
        Log.i("messaging", "MyReceiver::OnRegisterResult : code is " + errorCode + ", token is " + token.getTokenString());
    }

    // 反注册后回调此接口。
    @Override
    public void onUnregisterResult(Context context, int code) {

        Toast.makeText(context, "取消注册结果返回：" + code, Toast.LENGTH_SHORT).show();
        Log.i("messaging", "MyReceiver::onUnregisterResult : code is " + code);
    }

    // 收到透传消息后回调此接口。
    @Override
    public void onMessageArrived(Context context, TACMessagingText tacMessagingText, PushChannel channel) {

        Toast.makeText(context, "收到透传消息：" + tacMessagingText, Toast.LENGTH_LONG).show();
        Log.i("messaging", "MyReceiver::OnTextMessage : message is " + tacMessagingText+ " pushChannel " + channel);
    }

    // 收到通知栏消息后回调此接口。
    @Override
    public void onNotificationArrived(Context context, TACNotification tacNotification, PushChannel pushChannel) {

        Toast.makeText(context, "收到通知消息：" + pushChannel, Toast.LENGTH_LONG).show();
        Log.i("messaging", "MyReceiver::onNotificationArrived : notification is " + tacNotification + " pushChannel " + pushChannel);

    }

    // 点击通知栏消息后回调此接口。
    @Override
    public void onNotificationClicked(Context context, TACNotification tacNotification, PushChannel pushChannel) {

        Log.i("messaging", "MyReceiver::onNotificationClicked : notification is " + tacNotification + " pushChannel " + pushChannel);

    }

    // 删除通知栏消息后回调此接口
    @Override
    public void onNotificationDeleted(Context context, TACNotification tacNotification, PushChannel pushChannel) {

        Log.i("messaging", "MyReceiver::onNotificationDeleted : notification is " + tacNotification + " pushChannel " + pushChannel);

    }
    
    // 绑定标签回调
    @Override
    public void onBindTagResult(Context context, int code, String tag) {
        Toast.makeText(context, "绑定标签成功：tag = " + tag, Toast.LENGTH_LONG).show();
        Log.i("messaging", "MyReceiver::onBindTagResult : code is " + code + " tag " + tag);

    }

    // 解绑标签回调
    @Override
    public void onUnbindTagResult(Context context, int code, String tag) {
        Toast.makeText(context, "解绑标签成功：tag = " + tag, Toast.LENGTH_LONG).show();
        Log.i("messaging", "MyReceiver::onUnbindTagResult : code is " + code + " tag " + tag);
    }


}

```

#### 在 `AndroidManifest.xml` 文件中注册

在创建好 `TACMessagingReceiver` 的子类后，您需要在工程的 AndroidManifest.xml 文件中注册该类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    ...>
    ...
    <!-- 这里替换成你自己的 TACMessagingReceiver 子类 -->
    <receiver android:name=".MyReceiver">
      <intent-filter>
          <action android:name="com.tencent.tac.messaging.action.CALLBACK" />
      </intent-filter>
    </receiver>
    
  </application>
</manifest>

```

## 验证服务

### 查看服务启动情况

app 启动后，会自动在 Messaging 后台进行注册，注册成功后回调您在 `AndroidManifest.xml` 中注册的 `TACMessagingReceiver` 子类的 `onRegisterResult()` 方法。这里在 `MyReceiver` 中打印了推送的 token，启动后会打印如下信息：

```
I/messaging: MyReceiver::OnRegisterResult : code is 0, token is 495689dbfda473ef44de899cf45111fd83031156
``` 
> 这里日志打印的 token 信息标识推送时的唯一 ID，您可以通过 token 信息给该设备发送通知。

如果没有打印以上日志，请查看 [常见问题](https://cloud.tencent.com/document/product/666/14825)。

### 在控制台上发送通知栏消息

打开 [MobileLine 控制台](https://console.cloud.tencent.com/tac)，选择【创建推送】下的【通知栏消息】，并填写好 **通知标题** 和 **通知内容**，然后选择单选框中的【单个设备】，然后将注册成功后回调时打印的设备唯一标识 token 信息拷贝到编辑框中（示例这里为 495689dbfda473ef44de899cf45111fd83031156 ），然后点击【确认推送】。

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/Messaging/console_push_notification_simple.png)

> 您也可以通过我们的后台接口来发送消息，具体请参考 [Rest API 使用指南](https://cloud.tencent.com/document/product/666/15584) 或者 [服务端 SDK](https://cloud.tencent.com/document/product/666/15606)

### 查看回调信息

在控制台上发送通知栏消息后，当 SDK 接收到该消息时会回调 `onNotificationArrived()` 方法，示例 `MyReceiver` 会打印如下日志：

```
I/messaging: MyReceiver::onNotificationArrived : notification is TACNotification [msgId=1463713536, title=AndroidDemo, content=content, customContent={}, activity=com.android.demo.MainActivity, notificationActionType1] pushChannel XINGE
```
如果您的应用收到了通知栏通知，并且打印了如上日志，则说明您已经成功将 Messaging 服务集成到您的应用中，否则请参考 [常见问题](https://cloud.tencent.com/document/product/666/14825)。
