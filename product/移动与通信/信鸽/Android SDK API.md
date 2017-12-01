## API 接口
<hr>
### 接口概览
<hr>
所有 API 接口的包名路径前缀都是：com.tencent.android.tpush，其中有以下个重要的对外提供接口的类，如下：

|类名| 说明| 
|--|--|
|XGPushManagerPush 服务|	推送|
|XGPushConfig|	Push 服务配置项接口|
|XGPushBaseReceiver	|接收消息和结果反馈的 receiver，需要开发者自己在 AndroidManifest.xml 静态注册|

####  XGPushManager 功能类

XGPushManager 提供信鸽服务的对外 API 列表，方法默认为 public static 类型。

|原型	|功能|
|-|-|
|void registerPush(Context context)void registerPush(Context context, final XGIOperateCallback callback)	|启动并注册|
|void registerPush(Context context, String account)void registerPush(Context context, String account, final XGIOperateCallback callback)|	启动并注册 APP，同时绑定账号,推荐有帐号体系的 APP 使用|
|void registerPush(Context context,String account, String ticket, int ticketType, String qua, final XGIOperateCallback callback)|	同上，仅供带登陆态的业务使用|
|void unregisterPush(Context context)|	反注册，建议在不需要接收推送的时候调用|
|void setTag(Context context,String tagName)|	设置标签|
|void deleteTag(Context context,String tagName)|	删除标签|
|XGPushClickedResult onActivityStarted(Activity activity)	Activity|被打开的效果统计；获取下发的自定义 key-value|
|void onActivityStoped(Activity activity)	|Activity 被打开的效果统计|
|void setPushNotificationBuilder(Context context, int notificationBulderId, XGPushNotificationBuilder notificationBuilder)	|自定义本地通知样式|
|long addLocalNotification(Context context, XGLocalMessage msg)|	本地通知|
|boolean isNotificationOpened(Context context)	|检测通知栏是否关闭|

#### XGPushConfig 配置类

XGPushConfig 提供信鸽服务的对外配置 API 列表，方法默认为 public static 类型，对于本类提供的 set 和 enable 方法，要在 XGPushManager 接口前调用才能及时生效。

|原型|	功能|
|-|-|
|void enableDebug(Context context,boolean debugMode)|	是否开启 debug 模式，即输出 logcat 日志重要：为保证数据的安全性，发布前必须设置为 false）|
|boolean setAccessId(Context context,long accessId)	|配置 accessId|
|boolean setAccessKey(Context context,String accessKey)	|配置 accessKey|
|String getToken(Context context)	|获取设备的 token，只有注册成功才能获取到正常的结果|
|void setReportNotificationStatusEnable(final Context context,final boolean debugMode)|	设置上报通知栏是否关闭 默认打开|
|void setReportApplistEnable(final Context context,final boolean debugMode)|	设置上报 APP 列表，用于智能推送 默认打开|
#### XGPushBaseReceiver 广播类

XGPushBaseReceiver 类提供透传消息的接收和操作结果的反馈，需要开发者继承本类，并重载相关的方法；

同时，还需要在 AndroidManifest.xml 静态注册（注意：如果是在代码动态注册，只有当前 APP 运行时才能收到消息）。

|原型	|功能|
|-|-|
|void onTextMessage(Context context,XGPushTextMessage message)	|应用内消息的回调|
|void onRegisterResult(Context context,int errorCode,XGPushRegisterResult registerMessage)|	注册回调|
|void onUnregisterResult(Context context, int errorCode)|	反注册回调|
|void onSetTagResult(Context context,int errorCode,String tagName)	|设置标签回调|
|void onDeleteTagResult(Context context, int errorCode,String tagName)	|删除标签回调|
|void onNotifactionShowedResult(Context context, XGPushShowedResult notifiShowedRlt)	|通知被展示触发的回调，可以在此保存 APP 收到的通知|
|void onNotifactionClickedResult(Context context, XGPushClickedResult message)	|通知被点击触发的回调|

### 启动与注册
<hr>
APP 只有在完成信鸽的启动与注册后才可以信鸽 SDK 提供 push 服务，在这之前请确保配置 AccessId 和 AccessKey。

新版的 SDK 已经将启动信鸽和 APP 注册统一集成在注册接口中，即只需调用注册接口便默认完成启动和注册操作。

注册成功后，会返回设备 token，token 用于标识设备唯一性，同时也是信鸽维持与后台连接的唯一身份标识。关于如何获取 token 请参考“获取 token”章节。

注册接口通常提供简版和带 callback 版本的接口，请根据业务需要决定选择接口。

#### 绑定设备注册
<hr>
普通注册只注册当前设备，后台能够针对不同的设备 token 发送推送消息，有2个版本的 API 接口。

注意：这种注册方式，不支持推送帐号。

***（1）原型***
```
public static void registerPush(Context context)
```

***（2）参数***
 
 context：当前应用上下文对象，不能为 null

***（3）示例***
```
XGPushManager.registerPush(this);
```
另外，为方便用户获取注册是否成功的状态，提供带 callback 的版本。
	
***（1）原型***
```
public static void registerPush(Context context,
final XGIOperateCallback callback)
```

***（2）参数***

context：当前应用上下文对象，不能为 null

callback：callback 调用，主要包括操作成功和失败的回调，不能为 null

***（3）示例***
```
XGPushManager.registerPush(this, new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "注册成功，设备token为：" + data);
}
@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
}
})
```

#### 1.2.2. 绑定账号注册
<hr>
绑定账号注册指的是，在绑定设备注册的基础上，使用指定的账号（一个账号可能在多个设备登陆）注册 APP，这样可以通过后台向指定的账号发送推送消息，有2个版本的API接口。

注意：这里的帐号可以是邮箱、QQ 号、手机号、用户名等任意类别的业务帐号。目前一个帐号可以绑定最多15个设备  token，超限后最新的会随机顶掉之前绑定的一个。
***（1）原型***
```
public static void registerPush(Context context, String account)
```
***（2）参数***

context：当前应用上下文对象，不能为 null

account：绑定的账号，绑定后可以针对账号发送推送消息。

如果要按别名推送，那就需要开发者在调用注册接口时把别名设置在注册请求里面的 account 字段，一台设备只允许有一个帐号别名，但一个别名下可以有最多15台设备，不能为 null

***（3）示例***

```
XGPushManager.registerPush(this, "UserAccount")
```

另外，为方便用户获取注册是否成功的状态，提供带 callback 的版本。

***（1）原型***
```
public static void registerPush(Context context, String account,
final XGIOperateCallback callback)
```

***（2）参数***

context：当前应用上下文对象，不能为 null

account：绑定的账号，绑定后可以针对账号发送推送消息。

如果要按别名推送，那就需要开发者在调用注册接口时把别名设置在注册请求里面的 account 字段，一台设备只允许有一个别名，但一个别名下可以有最多15台设备，不能为 null

callback：callback 调用，主要包括操作成功和失败的回调，不能为 null

***（3）示例***
```
XGPushManager.registerPush(this, "UserAccount",
new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "注册成功，设备token为：" + data);
}

@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
}
});
```

#### 账号解绑
<hr>
若 APP 调用 registerPush(context, account)等绑定 account 账号，需要解绑（如用户退出），可以调用以下方法。

调用
```
registerPush(context, "*")或registerPush(context, "*", xGIOperateCallback )
```

即设置 account="*"即为解除之前的账号绑定

注意

账号解绑只是解除 token 与 APP 账号的关联，若使用全量/标签/token 推送仍然能收到通知/消息。

**带登陆态的注册**
<hr>
考虑到用户的登陆态问题，比如手机 QQ 或 QZone 业务场景，我们提供了带登陆态的注册接口，方便适用该类业务的使用。

***（1）原型***

```
public static void registerPush(Context context, String account,
String ticket, int ticketType, String qua,
final XGIOperateCallback callback)



***（2）参数 ***


context：当前应用上下文对象，不能为null

callback：操作回调，主要包括操作成功和失败的回调，不能为null

account：绑定的账号，绑定后可以针对账号发送推送消息。

如果要按别名推送，那就需要开发者在调用注册接口时把别名设置在注册请求里面的account字段，一台设备只允许有一个别名，但一个别名下可以有15台设备，不能为null

ticket：登陆态票据，不能为null

ticketType：票据类型

qua：QZone专用字段，不需要时可填null

***（3）示例**

```java
XGPushManager.registerPush(this, "UserAccount", "ticket", 1, null,
new XGIOperateCallback() {
@Override
public void onSuccess(Object data, int flag) {
Log.d("TPush", "注册成功，设备 token 为：" + data);
}

@Override
public void onFail(Object data, int errCode, String msg) {
Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
}
});
```

#### 获取注册结果

<hr>

有2种途径可以获取注册是否成功。

***（1） 使用callback版本的注册接口***

XGIOperateCallback类提供注册成功或失败的处理接口，请参考注册接口里面的示例。
XGIOperateCallback的定义：


```
/**
* 操作回调接口
*/
public interface XGIOperateCallback {
/**
* 操作成功时的回调。
* @param data 操作成功的业务数据，如注册成功时的 token 信息等。
* @param flag 标记码
*/
public void onSuccess(Object data, int flag);
/**
* 操作失败时的回调
* @param data 操作失败的业务数据
* @param errCode 错误码
* @param msg 错误信息
*/
public void onFail(Object data, int errCode, String msg);
}

```

***（2）重载XGPushBaseReceiver***

可通过重载XGPushBaseReceiver的onRegisterResult方法获取。

（注意：重载的XGPushBaseReceiver需要配置在AndroidManifest.xml，请参考“消息配置”章节的相关内容）

***示例***

```
/**
* 注册结果
*
* @param context
* APP 上下文对象
* @param errorCode
* 错误码，{@link XGPushBaseReceiver#SUCCESS}表示成功，其它表示失败
* @param registerMessage
* 注册结果返回
*/

```
其中，XGPushRegisterResult提供的方法列表：

|方法名| 	返回值|  默认值|    	描述|
|-----|-----|-----|-----|
|getToken()	|String|	""|	设备的token，即设备唯一识别ID|
|getAccessId()|	long|	0	|获取注册的accessId|
|getAccount|	String|	""|	获取注册绑定的账号|
|getTicket()|	String|	""|	登陆态票据|
|getTicketType()|	short|	0|	票据类型|

### 反注册
<hr>
当用户已退出或APP被关闭，不再需要接收推送时，可以取消注册APP，即反注册。（注意一旦设备反注册，直到这个设备重新注册成功这个期间内，下发的消息该设备都无法收到)

***（1）原型***


```
public static void unregisterPush(Context context)
```
***（2）参数***


```
context： APP 的上下文对象。
```

***（3）示例***


```
XGPushManager.unregisterPush(this);
```
***反注册结果***

可通过重载XGPushBaseReceiver的onUnregisterResult方法获取。

***示例***


```
<pre class="brush:cpp;">/**
* 反注册结果
*
* @param context
* APP 上下文对象
* @param errorCode
* 错误码，{@link XGPushBaseReceiver#SUCCESS}表示成功，其它表示失败
*/
@Override
public void onUnregisterResult(Context context, int errorCode) {

}
</pre>
```
***注意***

反注册操作切勿过于频繁，可能会造成后台同步延时。

切换帐号无需反注册，多次注册自动会以最后一次为准。

### **通知和消息**
<hr>
信鸽推送服务主要提供2种推送格式： “推送通知” 和 “透传消息命令”，二者存在一定的区别。

#### **推送通知（展现在通知栏）**
指的是在设备的通知栏展示的内容，由信鸽SDK完成所有的操作，APP可以监听通知被打开的行为，也就是说在前台下发的通知不需要APP做任何处理，默认会展示在通知栏。

成功注册信鸽服务后，通常不需要任何设置便可下发通知。

通常来说，结合自定义通知样式，常规的通知能够满足大部分业务需求，如果需要更灵活的方式请考虑使用消息。

#### **应用内消息命令（消息不展示到通知栏）**
指的是由信鸽下发给APP的内容，需要APP继承XGPushBaseReceiver接口实现并自主处理所有操作过程，也就是说，下发的消息默认是不会展示在通知栏的，信鸽只负责将消息从信鸽服务器下发到APP这个过程，不负责消息的处理逻辑，需要APP自己实现。具体可参考Demo中MessageReceiver。

消息指的是由开发者通过前台或后台脚本下发的文本消息，信鸽只负责将消息传递给APP，APP完全自主负责消息体的处理。

消息具有灵活性强和高度定制性特点，因此更适合APP自主处理个性化业务需求，比如下发APP配置信息、自定义处理消息的存储和展示等。

例如：某游戏需要针对不同情景（用户升级提示、版本更新提示、活动营销提示等）提供不同的通知，可以把这些情景以json格式封装在消息，下发到APP，然后APP根据这些场景提供不同的提示，满足个性化需求。

***消息配置***

若要接收消息，需要配置消息接收Receiver，即在AndroidManifest.xml配置以下信息，其中android:name的值需要修改为APP自己实现的Receiver。

```
<!-- APP实现的Receiver，用于接收消息和结果反馈 -->
<!-- com.tencent.android.xgpushdemo.CustomPushReceiver需要改为自己的Receiver -->
<receiver android:name="com.tencent.android.xgpushdemo.CustomPushReceiver" >
<intent-filter>
<!-- 接收消息透传 -->
<action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
<!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
<action android:name="com.tencent.android.tpush.action.FEEDBACK" />
</intent-filter>
</receiver>
```
***获取应用内消息***

开发者在前台下发消息，需要APP继承XGPushBaseReceiver重载onTextMessage方法接收，成功接收后，再根据特有业务场景进行处理。

同时，XGPushBaseReceiver还提供其它相关的接口，如通知被展示、被点击的结果反馈、注册/反注册结果反馈等，请参考“XGPushBaseReceiver”章节或demo中的MessageReceiver类。

请确保在AndroidManifest.xml已经注册过该receiver，即设YOUR_PACKAGE.XGPushBaseReceiver。

***原型***

```
public void onTextMessage(Context context,
XGPushTextMessage message)
```
***参数***

context：应用当前上下文

message：接收到消息结构体，其中XGPushTextMessage的方法列表如下：

|方法名|	返回值|	默认值|	描述|
|-|-|-|-|
|etContent()|	String|	""	|消息正文内容，通常只需要下发本字段即可|
|getCustomContent()|	String|	""|	消息自定义key-value|
|getTitle()|	String|	""	|消息标题（注意：从前台下发应用内消息字中的描述不属于标题|

#### 本地通知

本地通知由用户自定义设置，保存在本地。当应用打开，信鸽service 会根据网络心跳判断当前是否有通知5分钟一次 本地通知需要service开启才能弹出，可能存在5分钟左右延时。（当设置的时间小于当前设备时间通知弹出。）

```
    ```java
    //新建本地通知
    XGLocalMessage local_msg = new XGLocalMessage();

    //设置本地消息类型，1:通知，2:消息

    local_msg.setType(1);

    // 设置消息标题

    local_msg.setTitle("qq");

    //设置消息内容

    local_msg.setContent("ww");

    //设置消息日期，格式为：20140502

    local_msg.setDate("20140930");

    //设置消息触发的小时(24小时制)，例如：22代表晚上10点

    local_msg.setHour("19");

    //获取消息触发的分钟，例如：05代表05分

    local_msg.setMin("31");

    //设置消息样式，默认为0或不设置

    local_msg.setBuilderId(0);

    //设置动作类型：1打开 activity 或 app 本身，2打开浏览器，3打开 Intent ，4通过包名打开应用

    local_msg.setAction_type(1);

    //设置拉起应用页面

    local_msg.setActivity("com.qq.xgdemo.SettingActivity");
    // 设置 URL

     local_msg.setUrl("http://www.baidu.com");

    // 设置 Intent

     local_msg.setIntent("intent:10086#Intent;scheme=tel;action=android.intent.action.DIAL;S.key=value;end");

    // 是否覆盖原先 build_id 的保存设置。1覆盖，0不覆盖

     local_msg.setStyle_id(1);

    // 设置音频资源

     local_msg.setRing_raw("mm");

    // 设置 key,value

     HashMap<String, Object> map = new HashMap<String, Object>();

     map.put("key", "v1");

      map.put("key2", "v2");

    local_msg.setCustomContent(map);

    // 设置下载应用 URL

    local_msg.setPackageDownloadUrl("http://softfile.3g.qq.com:8080/msoft/179/1105/10753/MobileQQ1.0(Android)_Build0198.apk");

    //添加通知到本地
    XGPushManager.addLocalNotification(context,local_msg);
    ```


###  自定义通知样式

用户可以根据自行需要设置通知样式，由于目前的定制 ROM 的限制，部分接口无法适配全部机型。

```
  XGCustomPushNotificationBuilder build = new  XGCustomPushNotificationBuilder();

        build.setSound(
                RingtoneManager.getActualDefaultRingtoneUri(

                        getApplicationContext(), RingtoneManager.TYPE_ALARM))

                .setDefaults(Notification.DEFAULT_VIBRATE) // 振动

                .setFlags(Notification.FLAG_NO_CLEAR); // 是否可清除

        // 设置自定义通知 layout,通知背景等可以在 layout 里设置

        build.setLayoutId(R.layout.notification);

        // 设置自定义通知内容 id

        build.setLayoutTextId(R.id.content);

        // 设置自定义通知标题 id

        build.setLayoutTitleId(R.id.title);


        // 设置自定义通知图片资源

        build.setLayoutIconDrawableId(R.drawable.logo);

        // 设置状态栏的通知小图标

        build.setIcon(R.drawable.right);

        // 设置时间 id

        build.setLayoutTimeId(R.id.time);

        // 若不设定以上自定义 layout，又想简单指定通知栏图片资源

        build.setNotificationLargeIcon(R.drawable.ic_action_search);

        // 客户端保存 build_id

        XGPushManager.setPushNotificationBuilder(this, build_id, build);
```
### 获取设备 Token
<hr>
Token 是信鸽保持与后台长连接的唯一身份标识，是识别识别的唯一 ID，只有设备注册成功后才能获取 token，可以有以下方法获。（信鸽的 token 在应用卸载重新安装的时候有可能会变。）

***（1）通过带 callback 的注册接口获取***

带 XGIOperateCallback 的注册接口的 onSuccess(Object data, int flag)方法中，参数 data 便是 token，具体可参考注册接口的相关示例。

***（2）重载 XGPushBaseReceiver***

重载 XGPushBaseReceiver 的 onRegisterResult (Context context, int errorCode, XGPushRegisterResult registerMessage)方法，通过参数 registerMessage 提供的 getToken 接口获取，具体可参考“获取注册结果”章节。

***（3） XGPushConfig.getToken(context)***

当设备一旦注册成功后，便会将token存储在本地，之后可通过 XGPushConfig.getToken(context)接口获取。

### 获取通知
<HR>
通知的下发和展示完全是由信鸽 SDK 控制的，但有的开发者需要在本地存储被展示过的通知内容，可以通过重载XGPushBaseReceiver的onNotifactionShowedResult(Context, XGPushShowedResult)方法实现。其中，XGPushShowedResult 对象提供读取通知内容的接口。


***原型***


```
public abstract void onNotifactionShowedResult(Context context,XGPushShowedResult notifiShowedRlt);
```
***参数***

context：当前应用上下文 notifiShowedRlt： 被展示的通知对象

### 获取消息点击结果
<HR>
***【2.30及以上版本】通知效果监听和自定义 key-value***

使用信鸽 SDK 内置的 activity 展示页面，默认已经统计通知/消息的抵达量、通知的点击和清除动作。但如果开发者要监听这些事件，需要按照以下方法嵌入代码。

注意：如果需要统计由信鸽推送引起的打开 APP 操作或获取下发的自定义 key-value，需要开发者在所有（或被打开）的 Activity 的 onResume()调用以下方法。

***（1）原型***


```
public abstract void onNotifactionShowedResult(Context context,XGPushShowedResult notifiShowedRlt);
```

***（2）参数***

activity：被打开 activity 上下文

***（3）返回值***

XGPushClickedResult：通知被打开的对象，如果该 activity 是由信鸽的通知引起打开动作的，返回XGPushClickedResult，否则返回 null。

XGPushClickedResult 类方法列表：

|方法名|	返回值|	默认值|	描述|
|-|-|-|-|
|getMsgId()|	long|	0|	消息 id|
|getTitle()|	String	|""	|通知标题|
|getContent()	|String|	""	|通知正文内容|
|getActivityName()|	String|	""|	被打开的页面名称|
|getCustomContent()|	String|	""	|自定义 key-value，json 字符串同时，在 Activity 的 onPause()调用以下方法|

***（1）原型***


```
public static void onActivityStoped(Activity activity)
```

***（2）参数***

activity：当前 activity 上下文

***（3）示例***


```
@Override
protected void onPause() {
super.onPause();
XGPushClickedResult clickedResult = XGPushManager.onActivityStarted(this);
String  customContent= clickedResult.getCustomContent();
}
```

### 标签
<hr>
***预置标签***

目前信鸽提供三类预置标签：

地理位置（省一级）

应用版本号

流失用户（3天or7天）

预置标签会在 SDK 内部自动上报。

***设置标签***

开发者可以针对不同的用户设置标签，然后在前台根据标签名群发通知。 一个应用最多有10000个 tag， 每个 token 在一个应用下最多100个 tag， tag 中不准包含空格。

***函数原型***


```
public static void setTag(Context context, String tagName)
```

***参数***

context：Context 对象

tagName：待设置的标签名称，不能为 null 或空。

***处理结果***

可通过重载 XGPushBaseReceiver 的 onSetTagResult 方法获取。

***示例***


```
XGPushManager.setTag(this, "male");
```

***删除标签***

开发者删除用户标签数据。

***函数原型***


```
public static void deleteTag(Context context, String tagName)
```

***参数***

context：Context 对象

tagName：待设置的标签名称，不能为 null 或空

***处理结果***

可通过重载 XGPushBaseReceiver 的 onDeleteTagResult 方法获取。

***示例***


```
XGPushManager.deleteTag (this, "male");
```
### 配置接口
<hr>
所有的配置相关接口在 XGPushConfig 类中，为了使配置及时生效，开发者需要保证配置接口在启动或注册信鸽之前被调用。

#### debug 模式

（重要：为保证数据的安全性，请在发布时确保已关闭 debug 模式！！）

***（1）函数原型***


```
public static void enableDebug(Context context, boolean debugMode)
```

***（2）参数***

context:APP 上下文对象

debugMode：默认为 false。如果要开启 debug 日志，设为 true

#### 获取 token

token（又称 MID：Mobile ID）是一个设备的身份识别 ID，由服务器根据设备属性随机产生并下发到本地，同一台设备下所有使用信鸽或 MTA（腾讯移动分析）的 APP 获取的 token 都是相同的。

使用 token 的一个好处是可以消除山寨机设备 ID 重复带来的统计影响，提高精准度。

如果您恰好正在使用最新版本的 MTA，通过 MTA 的 StatConfig.getMid()接口获取到的 mid 跟本接口是一样的。

注意：第一次注册会产生 token，之后一直存在手机里，不管以后注销注册操作，该 token 一直存在。在3.0及其以上版本，token  在卸载重装等情况下 可能会改变。

***（1）函数原型***


```
public static String getToken(Context context)
```

***（2）参数***

context：APP 上下文对象

***（3）返回值***

成功时返回正常的 token；失败时返回 null 或”0”

#### 设置 AccessID

如果已在 AndroidManifest.xml 配置过，不需要再次调用；如果2者都存在，则以本接口为准。

***（1）函数原型***


```
public static boolean setAccessId(Context context, long accessId)
```

***（2）参数***

Context 对象 accessId：前台注册得到的 accessId

***（3）返回值***

true：成功

false：失败

注意：通过本接口设置的 accessId 会同时存储在文件中

#### 设置 AccessKey

如果已在 AndroidManifest.xml 配置过，不需要再次调用；如果2者都存在，则以本接口为准。

***（1）函数原型***
```
public static boolean setAccessId(Context context, String accessKey)

```

***（2）参数***

Context 对象

accessId：前台注册得到的 accesskey

***（3）返回值***

true：成功

false：失败

注意：通过本接口设置的 accessId 会同时存储在文件中