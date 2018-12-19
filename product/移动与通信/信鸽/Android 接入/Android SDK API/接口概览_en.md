All APIs have the same prefix of package path: com.tencent.android.tpush. The following are important classes which provide APIs:

| Class Name | Description | 
|--|--|
| XGPushManagerPush Service | Push messages |
| XGPushConfig | API for Push service's configuration items |
| XGPushBaseReceiver | The receiver to receive messages and results. Developers need to register it statically in AndroidManifest.xml. |

## XGPushManager Functional Class

XGPushManager provides a list of APIs of XGPush service. The method defaults to public static.

| Prototype | Feature |
|-|-|
| void registerPush(Context context)void registerPush(Context context,final XGIOperateCallback callback) | Launch and register with App |
| void registerPush(Context context,String account)void registerPush(Context context,String account,final XGIOperateCallback callback) | Launch and register with App, and bind account to the App. This is recommended for Apps with an account system. |
| void registerPush(Context context,String account,String ticket,int ticketType,String qua,final XGIOperateCallback callback) | Same as above. This is suitable for the business with a login status. |
| void unregisterPush(Context context) | Unregistration. This is suitable for the scenarios where there is no need to receive pushed messages. |
| void setTag(Context context,String tagName) | Set tags |
| void deleteTag(Context context,String tagName) | Delete tags |
| XGPushClickedResult onActivityStarted(Activity activity) | Statistics of Activities that have been opened; obtain the custom key-value |
| void onActivityStoped(Activity activity) | Statistics of Activities that have been opened |
| void setPushNotificationBuilder(Context context,int notificationBulderId,XGPushNotificationBuilder notificationBuilder) | Custom style of local notifications |
| long addLocalNotification(Context context,XGLocalMessage msg) | Local notifications |
| boolean isNotificationOpened(Context context) | Check whether the notification bar is closed |

## XGPushConfig Configuration Class

XGPushConfig provides a list of XGPush configuration APIs. The method defaults to public static. The "set" and "enable" methods provided by this class must be called before the XGPushManager API to take effect in time.

| Prototype | Feature |
|-|-|
| void enableDebug(Context context,boolean debugMode) | Whether to enable debug mode, that is, to output logcat log. Note: To ensure data security, it must be set to false before publishing. |
| boolean setAccessId(Context context,long accessId) | Configure accessId |
| boolean setAccessKey(Context context,String accessKey) | Configure accessKey |
| String getToken(Context context) | Obtain the device token. A normal result can only be returned for a successful registration. |
| void setReportNotificationStatusEnable(final Context context,final boolean debugMode) | Whether to enable the report notification bar. It is enabled by default. |
| void setReportApplistEnable(final Context context,final boolean debugMode) | Whether to enable the report App list (used for smart push). It is enabled by default. |
## XGPushBaseReceiver Broadcast Class

The XGPushBaseReceiver class provides the receipt and operation results of messages transfered transparently. Developers need to inherit this class and overload the relevant methods.

In addition, developers need to implement static registration in AndroidManifest.xml. (Note: For dynamic registration in code, the messages can only be received when the current API is running.)

| Prototype | Feature |
|-|-|
| void onTextMessage(Context context,XGPushTextMessage message) | Callback for in-App messages |
| void onRegisterResult(Context context,int errorCode,XGPushRegisterResult registerMessage) | Callback for registration |
| void onUnregisterResult(Context context,int errorCode) | Callback for unregistration |
| void onSetTagResult(Context context,int errorCode,String tagName) | Callback for tagging |
| void onDeleteTagResult(Context context,int errorCode,String tagName) | Callback for tag deletion |
| void onNotifactionShowedResult(Context context,XGPushShowedResult notifiShowedRlt) | Callback triggered when the notification is displayed. The notification received by App can be saved in it. |
| void onNotifactionClickedResult(Context context,XGPushClickedResult message) | Callback triggered when the notification is clicked. |


