## Message Click Event and Page Redirect Method
In SDK, a click of message can trigger a click event, which is to open the main page. Therefore, if redirect action is configured in the "on Notification Clicked Result" callback method for click of message on terminal, there is a conflict between the custom redirect and the default click event, and the user will be redirected to the specified page first and then return to the main page. For this reason, you cannot set redirect in "on Notification Clicked Result".
The solutions are as follows (the first is recommended):
**Method 1:**
When sending a message, set the page to which the user will be redirected upon a click of message.
1. Set deeplink (package name+class name) directly in the Web-based advanced feature;
2. Set the SetActivity method (package name+class name) of the Action field in Message class at the backend, and get the content of message (header, content, and additional parameters) via XGPushClickedResult.

The method for setting the redirect page at backend is as follows (taking Java SDK as an example):

```
        ......

        XingeApp android= new XingeApp(access ID, secret key);
          Message message_android = new Message();
          message_android.setExpireTime(86400);
          message_android.setTitle("XGPush");
          message_android.setType(1);
          message_android.setContent("android test2");      
          ClickAction action = new ClickAction();
          action.setActivity("com.qq.xgdemo.activity.SettingActivity");
          message_android.setAction(action);
          JSONObject ret1= android.pushSingleDevice("token",message_android);
         ......
```

The method for obtaining the Message parameters at terminal is as follows:


```
        //This must be the context of the page to which the user will be redirected when clicking the message.
        XGPushClickedResult clickedResult = XGPushManager.onActivityStarted(this);
        //Obtain additional parameters of message
        String  ster= clickedResult.getCustomContent();
        //Obtain message header
        String  set = clickedResult.getTitle(); 
        //Obtain message content
        String  s= clickedResult.getContent();
```
**Method 2:**
Send in-App messages to the terminal. The notification bar is customized by the user. Use pop-up notification for local notifications, and set the page to which the user will be redirected.

## Package Conflict
jar package conflict:
If a message appears indicating a jar package conflict, keep one package and delete the other one. It is recommended to keep the one with a higher version. Common conflicts include:
1. Conflict between MSDK and XGPush: Delete wup.jar.
2. Conflict between MTA and XGPush: Delete the lower version of mid.jar.

## Obfuscated Code
If you apply obfuscated code using tools such as proguard in your project, keep the following options, otherwise it will make the XGPush service unavailable.

```
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {* ;}
-keep class com.tencent.mid.** {* ;}
-keep public class * extends com.qq.taf.jce.JceStruct{*;}
```

## Multi-line Display
Android multi-line display feature has been implemented in version 2.38 or above and is enabled by default, but it only takes effect on some models.

## Multi-package-name Push
Some Apps have different package names for different channels. A single App may have hundreds of package names. In this case, you can push messages to all package names of the App using access id. In the multi-package-name push mode, all Apps on the device that are registered with push service using this access id will receive the messages.
Before pushing messages:
1. Set the push parameter multi_pkg to 1 in case of a push on server.
2. Enable multi-package-name push in advanced features in case of a push on Web.




