## Android SDk 集成指南
<hr>
### AndroidStudio自动集成

#### 一导入依赖


```
AndroidStudio上可以使用jcenter远程仓库自动接入，不需要在项目中导入jar包和so文件；
在AndroidManifest.xml中不需要配置信鸽相关的内容，jcenter 会自动导入。
导入依赖过后修改应用配置，书写注册代码就能够实现信鸽快速接入。 
对应的依赖版本号均是，官网上最新的版本。
用户自定义的recevier.依然需要在Androidmianfest.xml配置相关节点。

在app build.gradle文件下配置 以下内容

android {
    ......
    defaultConfig {

        //信鸽官网上注册的包名.注意application ID 和当前的应用包名以及 信鸽官网上注册应用的包名必须一致。
        applicationId "你的包名" 
        ......

        ndk {
            //根据需要 自行选择添加的对应cpu类型的.so库。 
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a' 
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [

            XG_ACCESS_ID:"注册应用的accessid",
            XG_ACCESS_KEY : "注册应用的accesskey",
        ]
        ......
    }
    ......
}

dependencies {
    ......

    //完整的信鸽依赖三个都必须有，如果发生依赖冲突请根据对应的依赖版本号选择高版本的依赖。（使用jcenter自动接入请确认libs 中没有信鸽的相关jar包）



    //采集安装列表
    compile 'com.tencent.xinge:xinge:3.1.2-release' 

    //wup包 
    compile 'com.tencent.wup:wup:1.0.0.E-release'

    //mid包
    compile 'com.tencent.mid:mid:3.9.0-release'
    ......
}


***注意*** 

如果在添加以上 abiFilter 配置之后android Studio出现以下提示：

    NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.

则在 Project 根目录的gradle.properties文件中添加：

    android.useDeprecatedNdk=true
```

注 如需监听消息请参考XGBaseReceiver接口或者是demo的MessageReceiver类。自行继承XGBaseReceiver并且在配置文件中配置如下内容：

```
  <receiver android:name="完整的类名如:com.qq.xgdemo.receiver.MessageReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- 接收消息透传 -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>
```

### 手动集成

#### 注册并下载SDK

前往信鸽管理台xg.qq.com，使用QQ号码登陆，进入应用注册页，填写“应用名称”和“应用包名”（必须要跟APP一致），选择“操作系统”和“分类”，最后点击“创建应用”。

应用创建成功后，点击“应用配置”即可看到APP专属的AccessId和AccessKey等信息。

注册完成后，请下载最新版本的Android SDK到本地，并解压。

#### 工程配置
<hr>

将SDK导入到工程的步骤为：

（1）创建或打开Android工程（关于如何创建Android工程，请参照开发环境的章节）。

（2）将信鸽 SDK目录下的libs目录所有文件拷贝到工程的libs（或lib）目录下。

（3）选中libs（或lib）目录下的信鸽jar包，右键菜单中选择Build Path， 选择Add to Build Path将SDK添加到工程的引用目录中。

（4）.so文件是信鸽必须的组件，支持armeabi、armeabi-v7a、misp和x86平台，请根据自己当前.so支持的平台添加


```
 a）如果你的项目中没有使用其它.so，建议复制四个平台目录到自己工程中；

 b）如果已有.so文件，只需要复制信鸽对应目录下的文件；

 c）若是MSDK接入的游戏，通常只需要armeabi目录下的.so；

 d）若当前工程已经有armeabi，那么只需要添加信鸽的armeabi下的.so，其它目录无需添加。其它情况类似，只添 
    加当前 平台存在的平台即可。

e）若在Androidstudio中导入so文件出错（错误10004.SOERROR），在main文件目录下 添加jniLibs命名的文件 
   夹将所有的架构文件复制进去也就是SDK文档中的Other-Platform-SO下的所有文件夹。如图：
```

![](//mc.qcloudimg.com/static/img/494f08120cac80a9c350845fd5070c47/image.jpg)

（5）打开Androidmanifest.xml，添加以下配置（建议参考下载包的Demo修改），其中YOUR_ACCESS_ID和YOUR_ACCESS_KEY替换为APP对应的accessId和accessKey,请确保按照要求配置，否则可能导致服务不能正常使用。


```
<application
  <!-- 【必须】 信鸽receiver广播接收 -->
  <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
   android:process=":xg_service_v3" >
  <intent-filter android:priority="0x7fffffff" >
        <!-- 【必须】 信鸽SDK的内部广播 -->
        <action android:name="com.tencent.android.tpush.action.SDK" />
        <action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
        <!-- 【必须】 系统广播：开屏和网络切换 -->
       <action android:name="android.intent.action.USER_PRESENT" />
       <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
       <!-- 【可选】 一些常用的系统广播，增强信鸽service的复活机会，请根据需要选择。当然，你也可以添加APP自定义的一些广播让启动service -->
       <action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
       <action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
       <action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
       </intent-filter>
  </receiver>

<!-- 【可选】APP实现的Receiver，用于接收消息透传和操作结果的回调，请根据需要添加 -->
 <!-- YOUR_PACKAGE_PATH.CustomPushReceiver需要改为自己的Receiver： -->
  <receiver android:name="com.qq.xgdemo.receiver.MessageReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- 接收消息透传 -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>

   <!-- 【注意】 如果被打开的activity是启动模式为SingleTop，SingleTask或SingleInstance，请根据通知的异常自查列表第8点处理-->
   <activity
        android:name="com.tencent.android.tpush.XGPushActivity"
        android:exported="false" >
        <intent-filter>
           <!-- 若使用AndroidStudio，请设置android:name="android.intent.action"-->
            <action android:name="" />
        </intent-filter>
   </activity>

   <!-- 【必须】 信鸽service -->
   <service
       android:name="com.tencent.android.tpush.service.XGPushServiceV3"
       android:exported="true"
       android:persistent="true"
       android:process=":xg_service_v3" />


  <!-- 【必须】 提高service的存活率 -->
  <service
      android:name="com.tencent.android.tpush.rpc.XGRemoteService"
      android:exported="true">
      <intent-filter>
 <!-- 【必须】 请修改为当前APP包名 .PUSH_ACTION, 如demo的包名为：com.qq.xgdemo -->
              <action android:name="当前应用的包名.PUSH_ACTION" />
      </intent-filter>
   </service>


<!-- 【必须】 【注意】authorities修改为 包名.AUTH_XGPUSH, 如demo的包名为：com.qq.xgdemo-->
  <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       android:authorities="当前应用的包名.AUTH_XGPUSH"
       android:exported="true"/>

  <!-- 【必须】 【注意】authorities修改为 包名.TPUSH_PROVIDER, 如demo的包名为：com.qq.xgdemo-->
  <provider
       android:name="com.tencent.android.tpush.SettingsContentProvider"
       android:authorities="当前应用的包名.TPUSH_PROVIDER"
       android:exported="false" />

  <!-- 【必须】 【注意】authorities修改为 包名.TENCENT.MID.V3, 如demo的包名为：com.qq.xgdemo-->
  <provider
       android:name="com.tencent.mid.api.MidProvider"
       android:authorities="当前应用的包名.TENCENT.MID.V3"
       android:exported="true" >
  </provider>



<!-- 【必须】 请将YOUR_ACCESS_ID修改为APP的AccessId，“21”开头的10位数字，中间没空格 -->
   <meta-data
       android:name="XG_V2_ACCESS_ID"
       android:value="YOUR_ACCESS_ID" />
   <!-- 【必须】 请将YOUR_ACCESS_KEY修改为APP的AccessKey，“A”开头的12位字符串，中间没空格 -->
   <meta-data
       android:name="XG_V2_ACCESS_KEY"
       android:value="YOUR_ACCESS_KEY" />
</application>
<!-- 【必须】 信鸽SDK所需权限   -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<!-- 【常用】 信鸽SDK所需权限 -->
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />
<!-- 【可选】 信鸽SDK所需权限 -->
<uses-permission android:name="android.permission.RESTART_PACKAGES" />
<uses-permission android:name="android.permission.BROADCAST_STICKY" />
<uses-permission android:name="android.permission.KILL_BACKGROUND_PROCESSES" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BATTERY_STATS" />
```

### 注册以及部分日志输出
<hr>

1.根据手动接入或者自动接入，配置好信鸽过后，获取信鸽注册日志（接入过程中建议调用有回调的注册接口，开启信鸽的debug日志输出。AndroidStudio 建议采用jcenter自动接入，无需在配置文件中配置信鸽各个节点，全部由依赖导入）。

***开启debug日志数据***


```
 XGPushConfig.enableDebug(this,true);
```
***token注册***


```
XGPushManager.registerPush(this, new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
//token在设备卸载重装的时候有可能会变
Log.d("TPush", "注册成功，设备token为：" + data);
}
@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
}
})
```

过滤"TPush"注册成功的日志如下：

```
10-09 20:08:46.922 24290-24303/com.qq.xgdemo I/XINGE: [TPush] get RegisterEntity:RegisterEntity [accessId=2100250470, accessKey=null, token=5874b7465d9eead746bd9374559e010b0d1c0bc4, packageName=com.qq.xgdemo, state=0, timestamp=1507550766, xgSDKVersion=3.11, appVersion=1.0]
10-09 20:08:47.232 24290-24360/com.qq.xgdemo D/TPush: 注册成功，设备token为：5874b7465d9eead746bd9374559e010b0d1c0bc4
```

***设置账号***


```
XGPushManager.registerPush(getApplicationContext(), "XINGE");
```

过滤“TPush”账号注册成功的日志如下：


```
//如推送返回48账号无效，请确认账号接口调用成功
10-11 15:55:57.810 29299-29299/com.qq.xgdemo D/TPushReceiver: TPushRegisterMessage [accessId=2100250470, deviceId=853861b6bba92fb1b63a8296a54f439e, account=XINGE, ticket=0, ticketType=0, token=3f13f775079df2d54e1f82475a28bccd3bfef8c1]注册成功
```

***设置标签***


```
XGPushManager.setTag(this,"XINGE");
```
设置标签成功的日志：

```
10-09 20:11:42.558 27348-27348/com.qq.xgdemo I/XINGE: [XGPushManager] Action -> setTag with tag = XINGE
```

***收到消息日志***


```
10-16 19:50:01.065 5969-6098/com.qq.xgdemo D/XINGE: [i] Action -> handleRemotePushMessage
10-16 19:50:01.065 5969-6098/com.qq.xgdemo I/XINGE: [i] >> msg from service,  @msgId=1 @accId=2100250470 @timeUs=1508154601660412 @recTime=1508154601076 @msg.date= @msg.busiMsgId=0 @msg.timestamp=1508154601 @msg.type=1 @msg.multiPkg=0 @msg.serverTime=1508154601000 @msg.ttl=259200 @expire_time=1508154860200076 @currentTimeMillis=1508154601076
10-16 19:50:01.095 5969-6098/com.qq.xgdemo D/XINGE: [m] Action -> handlerPushMessage
10-16 19:50:01.105 5969-6098/com.qq.xgdemo I/XINGE: [m] Receiver msg from server :PushMessageManager [msgId=1, accessId=2100250470, busiMsgId=0, content={"n_id":0,"title":"XGDemo","style_id":1,"icon_type":0,"builder_id":1,"vibrate":0,"ring_raw":"","content":"token 推送","lights":1,"clearable":1,"action":{"aty_attr":{"pf":0,"if":0},"action_type":1,"activity":""},"small_icon":"","ring":1,"icon_res":"","custom_content":{}}, timestamps=1508154601, type=1, intent=Intent { act=com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE cat=[android.intent.category.BROWSABLE] pkg=com.qq.xgdemo (has extras) }, messageHolder=BaseMessageHolder [msgJson={"n_id":0,"title":"XGDemo","style_id":1,"icon_type":0,"builder_id":1,"vibrate":0,"ring_raw":"","content":"token 推送","lights":1,"clearable":1,"action":{"aty_attr":{"pf":0,"if":0},"action_type":1,"activity":""},"small_icon":"","ring":1,"icon_res":"","custom_content":{}}, msgJsonStr={"n_id":0,"title":"XGDemo","style_id":1,"icon_type":0,"builder_id":1,"vibrate":0,"ring_raw":"","content":"token 推送","lights":1,"clearable":1,"action":{"aty_attr":{"pf":0,"if":0},"action_type":1,"activity":""},"small_icon":"","ring":1,"icon_res":"","custom_content":{}}, title=XGDemo, content=token 推送, customContent=null, acceptTime=null]]
10-16 19:50:01.105 5969-6098/com.qq.xgdemo V/XINGE: [XGPushManager] Action -> msgAck(com.qq.xgdemo,1)
10-16 19:50:01.115 5969-6098/com.qq.xgdemo I/XINGE: [TPush] title encry obj:{"cipher":"YZXM+CuPhqaBn4eK0SE9ApWieHznugNT2uKo0OaXtlDDHLJiY7NlvSL2ZnlSb8E7yd7E7i9JU3g0PlFyYNLjokNp1buJuPoMYEHaJ0s6vmUMY+cq0Sv782XHxNzekV4a9mRcJ5xsOccIjH1VoskUmikfZJo3XLhZveWNYGPaoto="}
10-16 19:50:01.125 5969-6098/com.qq.xgdemo E/XINGE: [MessageInfoManager] delOldShowedCacheMessage Error! toDelTime: 1507981801138
10-16 19:50:01.145 5969-6098/com.qq.xgdemo I/XINGE: [MessageHelper] Action -> showNotification {"n_id":0,"title":"XGDemo","style_id":1,"icon_type":0,"builder_id":1,"vibrate":0,"ring_raw":"","content":"token 推送","lights":1,"clearable":1,"action":{"aty_attr":{"pf":0,"if":0},"action_type":1,"activity":""},"small_icon":"","ring":1,"icon_res":"","custom_content":{}}
```


### 消息点击事件，以及跳转页面方法

<hr>

由于目前sdk点击 消息默认会有点击事件，默认的点击事件是打开主界面。所以在终端点击消息回调onNotifactionClickedResult方法内，设置跳转操作，自定义的跳转和默认的点击事件造成冲突。反应情况是会跳转到指定界面过后再回到主界面。所以不能再onNotifactionClickedResult内设置跳转。

解决办法如下(推荐使用第一种方式)：

一.在下发消息的时候设置点击消息要跳转的页面。

a.可以直接在web端高级功能内设置deeplink包名+类名） ;

b.后台设置Messege 类中的 Action字段的 的SetActivity方法（包名+类名），通过XGPushClickedResult 可以获取到消息的相关内容。标题 ，内容，和附加参数。

后台设置跳转页面的方法如下（以javaSDK为例）：

```
        ......

        XingeApp android= new XingeApp(access ID, secret key);
          Message message_android = new Message();
          message_android.setExpireTime(86400);
          message_android.setTitle("信鸽推送");
          message_android.setType(1);
          message_android.setContent("android test2");      
          ClickAction action = new ClickAction();
          action.setActivity("com.qq.xgdemo.activity.SettingActivity");
          message_android.setAction(action);
          JSONObject ret1= android.pushSingleDevice("token",message_android);
         ......
```

终端获取Message 个参数的方法如下:


```
        //this必须为点击消息要跳转到页面的上下文。
        XGPushClickedResult clickedResult = XGPushManager.onActivityStarted(this);
        //获取消息附近参数
        String  ster= clickedResult.getCustomContent();
        //获取消息标题
        String  set = clickedResult.getTitle(); 
        //获取消息内容
        String  s= clickedResult.getContent();
```
二.发应用内消息到终端，用户自定义通知栏，采用本地通知弹出通知，设置要跳转的页面。

### 包冲突

<hr>

(1)jar包冲突：

如果提示jar包冲突，请删除冲突的包，保留一份即可，建议保留版本高的。 常见的冲突有：

a）MSDK与信鸽冲突：删除wup.jar

b）MTA与信鸽冲突：删除低版本的mid.jar

### 代码混淆
<hr>

如果你的项目中使用proguard等工具做了代码混淆，请保留以下选项，否则将导致信鸽服务不可用。


```
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {* ;}
-keep class com.tencent.mid.** {* ;}
-keep public class * extends com.qq.taf.jce.JceStruct{*;}
```

多行显示

Android多行显示特性，在2.38及以上版本已经实现并默认开启，但此功能部分机型生效。 多包名推送

目前市场上部分app针对不同渠道有不同的包名，同一款app可能会有上百个包名，这时就可以利用access id向该app的所有包名进行推送。在多包名推送模式下，设备上所有使用这个access id注册推送的app都会收到这条消息。 单应用多包名推送分为简单的三个步骤： 1）在信鸽前台注册应用，无需填写包名；若已经填好包名，也不会影响推送效果； 2）集成最新SDK在应用内； 3）在进行推送前，将推送参数 multi_pkg 设置为1；


```


```