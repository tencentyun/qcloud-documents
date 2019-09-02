The value of "message" parameter should be a json string with a total length of not more than 4,096 bytes as described below.

## Definition and Example of Push Notification
Push notification: It displays in the notification bar of a mobile or device by default.
```
{"content":"this is content","title":"this is title", "vibrate":1}
```
### Complete Definition

```
{
"title ":"xxx", // Title (required)
"content ":"xxxxxxxxx", // Content (required)
"accept_time": // The period when messages are allowed to be pushed to users (optional)
[
{
"start":{"hour":"13","min":"00"},
"end": {"hour":"14","min":"00"}
},
{
"start":{"hour":"00","min":"00"},
"end": {"hour":"09","min":"00"}
}
],
"n_id": 0, // Notification ID (optional). If it is greater than 0, the previous notification with the same ID is overwritten; if it is 0, this notification is displayed without affecting other notifications; if it is -1, only this notification is displayed and all the previous notifications are cleared. Default is 0.
"builder_id": 0, // Style of local notification (required)
"ring": 1, // Whether to ring (optional). 0: No; 1: Yes. (The same below) Default: 1. 
"ring_raw":"ring", // Specify the sound (ring.mp3) in the App (optional)
"vibrate": 1, // Whether to vibrate (optional). Default: 1.
"lights": 1// Whether breathing light is enabled (optional). 0: No; 1: Yes. Default: 1.
"clearable": 1, // Whether the notification bar can be cleared (optional). Default is 1.
"icon_type": 0 // Specify that the notification bar icon is an icon built in the App or an uploaded one (optional). 0: built-in icon; 1: uploaded icon. Default: 0.
"icon_res": "xg",// Name of the built-in icon file (xg.png) or url to download icon (optional)
"style_id": 1 // Specify whether the notification style with this ID is overridden on Web (optional). 0: No; 1: Yes. Default: 1.
"small_icon": "xg" // Specify the small icon (xg.png) in the status bar (optional)
"action": { // Action (optional). Default is to open the App
"action_type ": 1, // Action type, 1: open the activity or App; 2: open browser; 3: open Intent
"activity ": "xxx"
"aty_attr ": // The attribute of activity (only available when action_type=1)
{
"if": 0, // The attribute of intent when you create a notification, such as intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
"pf": 0, // The attribute of PendingIntent, such as PendingIntent.FLAG_UPDATE_CURRENT
}
"browser": {"url": "xxxx ","confirm": 1}, // url: the opened url; confirm: whether user confirmation is required
"intent": "xxx"
},
"custom_content":{ // User-defined key-value (optional)
"key1": "value1",
"key2": "value2"
}
}
```
## Definition and Example of Transparently Transferred Message
Transparently transferred message: Any transparently transferred message command that can be identified by the App, which is more flexible than push notification.
```
{"content":"this is content","title":"this is title"}
```
### Complete Definition

```
{
"title": "xxx", // Title (optional)
"content ": "xxxxxxxxx", // Content (optional)
"accept_time": // The period when messages are allowed to be pushed to users (optional)
[
{
"start":{"hour":"13","min":"00"},
"end": {"hour":"14","min":"00"}
},
{
"start":{"hour":"00","min":"00"},
"end": {"hour":"09","min":"00"}
}
],
"custom_content":{ // User-defined key-value (optional)
"key1": "value1",
"key2": "value2"
}
}
```

