
## Obtaining Notifications
The delivery and display of notifications is entirely controlled by the XGPush SDK. The developers who need to store the displayed notification content locally can overload the onNotifactionShowedResult (Context, XGPushShowedResult) method of XGPushBaseReceiver. The XGPushShowedResult object provides the API for reading the notification content.

**Prototype**

```
public abstract void onNotifactionShowedResult(Context context,XGPushShowedResult notifiShowedRlt);
```
**Parameters**

| Name | Description |
|-|-|
| context | The current App's context notifiShowedRlt: the notification object displayed |

## Obtaining Message Click Result
**[2.30 or above] Listen on the notification effect and obtain custom key-value**
On the activity display page built in the XGPush SDK, the arrivals of notification/message, and clicks/actions of clearing the notification are counted by default. The developers who want to listen on these events can embed the code as follows.
>Note: To count the actions of opening the App that are caused by the push of XGPush or obtain the custom key-value delivered, developers need to call the following methods in the onResume() for all (or opened) activities.

#### Method 1:
**Prototype**

```
public abstract void onNotifactionShowedResult(Context context,XGPushShowedResult notifiShowedRlt);
```

**Parameters**

| Name | Description |
|-|-|
| activity | Context of the opened activity |

**Returned Value**
XGPushClickedResult: The object for which the notification was opened. If the activity is caused by the notification pushed from XGPush, XGPushClickedResult is returned, otherwise null is returned.
Methods of XGPushClickedResult class are as follows:

| Method Name | Returned Value | Default | Description |
|-|-|-|-|
| getMsgId() | long | 0 | Message ID |
| getTitle() | String | " " | Notification header |
| getContent() | String | " " | Notification body content |
| getActivityName() | String | " " | Name of the page that was opened |
| getCustomContent() | String | " " | Custom key-value in the form of a json string. Call the following method in Activity's onPause(). |

#### Method 2:
**Prototype**

```
public static void onActivityStoped(Activity activity)
```

**Parameters**

| Name | Description |
|-|-|
| activity | Context of the current activity |

**Example**

```
@Override
protected void onPause() {
super.onPause();
XGPushClickedResult clickedResult = XGPushManager.onActivityStarted(this);
String  customContent= clickedResult.getCustomContent();
}
```

