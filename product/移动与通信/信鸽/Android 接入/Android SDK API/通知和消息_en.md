
XGPush service is provided in two formats: "push notification" and "in-App message command (transparently transfered message command)". The difference is as follows:

## Push Notification (Displayed in the notification bar)
It refers to the content displayed in the notification bar of the device. All operations are completed by XGPush SDK. The App can listen on the actions of opening the notification. This means that the notification delivered from the frontend does not need any processing by the App and is displayed in the notification bar by default.
After registering with XGPush service successfully, you can deliver notifications immediately without any configuration. In general, regular notifications with a custom style can satisfy most business needs. To push notifications in a more flexible manner, you can consider using message commands.

## In-App Message Command (Not displayed in the notification bar)
In-App message command (transparently transfered message command) is the content sent by the XGPush to the App. The App needs to inherit the API XGPushBaseReceiver to implement and handle all operations. That is, the delivered message is not displayed in the notification bar by default. XGPush only sends the message from its server to the App and is not responsible for the processing logic of the message. The processing of message needs to be implemented by the App itself. For more information, please refer to the MessageReceiver in Demo.
The message here refers to the text message delivered by the developer via the frontend or backend script. XGPush only pushes the message to the App, and the App is completely responsible for the processing of the message body. Such messages are highly flexible and customizable, and are therefore more suitable for the App to deal with individualized business needs, such as delivering App configuration information, customizing the storage and display of messages.
>For example: a game needs to provide different notifications for different scenarios (user upgrade notification, version update notification, campaign notification, etc.). These scenarios can be encapsulated in a JSON format in the messages, which are delivered to the App. Then the App provides different notifications based on these scenarios to meet individualized needs.

## Message Configuration
To receive messages, you need to configure the message Receiver by configuring the following information in AndroidManifest.xml. The value of Android:name needs to be modified to the Receiver implemented by the App.

```
<!-- Receiver implemented by APP for receiving messages and results -->
<!-- com.tencent.android.xgpushdemo.CustomPushReceiver needs to be modified to the App's own Receiver -->
<receiver android:name="com.tencent.android.xgpushdemo.CustomPushReceiver" >
<intent-filter>
<!-- Receive transparently transfered messages -->
<action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
<!-- Listen on the results of registration, unregistration, tag configuration/deletion, and clicks of notification -->
<action android:name="com.tencent.android.tpush.action.FEEDBACK" />
</intent-filter>
</receiver>
```
### Obtaining in-App messages
When the developer delivers a message at the frontend, the App needs to inherit the overloaded onTextMessage method of XGPushBaseReceiver to receive the message. After receiving the message successfully, the App processes the message based on the specific business scenario.
XGPushBaseReceiver also provides other related APIs for scenarios such as display of notification, result of clicks, result of registration/unregistration, etc. For more information, please see the "[XGPushBaseReceiver](https://cloud.tencent.com/document/product/548/13950#xgpushbasereceiver-.E5.B9.BF.E6.92.AD.E7.B1.BB)" section or MessageReceiver class in Demo.
Make sure that you have already registered this receiver in AndroidManifest.xml by setting YOUR_PACKAGE.XGPushBaseReceiver.

**Prototype**

```
public void onTextMessage(Context context,
XGPushTextMessage message)
```
**Parameters**

| Name | Description |
|-|-|
| context | App's current context |
| message | The message structure received |

The methods of XGPushTextMessage are listed below:

| Method Name | Returned Value | Default | Description |
|-|-|-|-|
| etContent() | String | "" | Content of the message body. Generally, you only need to deliver this field |
| getCustomContent() | String | "" | Message's custom key-value |
| getTitle()|	String | "" | Message header (Note: The description in the in-App message delivered from the frontend is not the header) |

## Local Notifications
Local notifications are customized by the user and saved locally. When the App is opened, XGPush service determines whether there is a notification every five minutes based on the network heartbeat. A local notification can only pops up after the service is enabled. There may be a delay of about five minutes (The notification pops up when the time set is earlier than the current device time).

```java
    //Create a local notification
    XGLocalMessage local_msg = new XGLocalMessage();
    //Set local message type. 1: Notification; 2: Message
    local_msg.setType(1);
    //Set message header
    local_msg.setTitle("qq");
    //Set message content
    local_msg.setContent("ww");
    //Set message date in the format of 20140502
    local_msg.setDate("20140930");
    //Set the time when the message is triggered in hh format (24-hour clock). For example, 22 is for 10 pm.
    local_msg.setHour("19");
    //Set the time when the message is triggered in mm format. For example, 05.
    local_msg.setMin("31");
    //Set message style. It defaults to 0 or is left empty.
    local_msg.setBuilderId(0);
    //Set action type: 1: Open the activity or App itself; 2: Open the browser; 3: Open the Intent; 4: Open the App via package name
    local_msg.setAction_type(1);
    //Set the page used for pulling up an App
    local_msg.setActivity("com.qq.xgdemo.SettingActivity");
    //Set URL
     local_msg.setUrl("http://www.baidu.com");
    //Set Intent
     local_msg.setIntent("intent:10086#Intent;scheme=tel;action=android.intent.action.DIAL;S.key=value;end");
    //Whether to overwrite the save settings of the original build_id. 1: Yes; 0: No.
     local_msg.setStyle_id(1);
    //Set audio resources
     local_msg.setRing_raw("mm");
    //Set key, value
     HashMap<String, Object> map = new HashMap<String, Object>();
     map.put("key", "v1");
     map.put("key2", "v2");
     local_msg.setCustomContent(map);
    //Set URL for downloading App

    local_msg.setPackageDownloadUrl("http://softfile.3g.qq.com:8080/msoft/179/1105/10753/MobileQQ1.0(Android)_Build0198.apk");
    //Add notification to local device
    XGPushManager.addLocalNotification(context,local_msg);
```

