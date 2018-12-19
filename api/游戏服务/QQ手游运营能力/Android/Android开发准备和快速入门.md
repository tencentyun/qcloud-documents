## 开发准备

### 环境依赖
适用于 JDK1.6 版本以上 。
###  安装 SDK
以下以 Eclipse 为开发的 IDE 进行范例说明：
1. 创建一个工程，把 open_sdk.jar, mta-sdk.jar 以及 mid-sdk.jar 文件拷贝到 libs（或 lib）目录下。
2. 将 open_sdk.jar, mta-sdk.jar 以及 mid-sdk.jar 加入编译路径中。

   具体的操作步骤为：选中 open_sdk.jar, mta-sdk.jar 以及 mid-sdk.jar，右键菜单中选择【Build Path】>【Add to Build  Path】。 
3. 配置 AndroidManifest：
在应用的 AndroidManifest.xml 增加配置的 **application** 节点下增加以下配置；
>**注意：**
>不配置将会导致无法调用 API。

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
 
<application>
 <activity
       android:name="com.tencent.tauth.AuthActivity"
       android:noHistory="true"
       android:launchMode="singleTask" >
    <intent-filter>
           <action android:name="android.intent.action.VIEW" />
           <category android:name="android.intent.category.DEFAULT" />
           <category android:name="android.intent.category.BROWSABLE" />
           <data android:scheme="tencent你的AppId" />
    </intent-filter>
 </activity>
<application>
```
通过以上步骤，工程就已经配置完成了。接下来就可以在代码里使用 QQ 互联的 SDK 进行开发了。
## 快速入门
### 创建实例
Tencent 是 SDK 的功能入口，所有的接口调用都得通过 Tencent 进行调用。因此调用 SDK 首先需要创建一个 Tencent 实例，其代码如下：

```
@Override
 
public void onCreate(Bundle savedInstanceState){
 
super.onCreate(savedInstanceState);
 
setContentView(R.layout.activity_main);
 
// Tencent类是SDK的主要实现类，开发者可通过Tencent类访问腾讯开放的OpenAPI。
 
// 其中APP_ID是分配给第三方应用的appid，类型为String。
 
mTencent = Tencent.createInstance(APP_ID, this.getApplicationContext());
 
// 1.4版本:此处需新增参数，传入应用程序的全局context，可通过activity的getApplicationContext方法获取
 
// 初始化视图
 
initViews();
 
}
```

如果你已经添加了 android.permission.INTERNET 和 android.permission.ACCESS_NETWORK_STATE 权限，则无需重复添加。而你的 APPID 则要替换成具体应用的 APPID，例如你的 APPID 是 222222，则 **data** 标签应该是这样的：

```
<data android:scheme="tencent222222" />
```
### 实现回调
所有的 SDK 接口调用，都会传入一个回调用以接收 SDK 返回的调用结果。回调的主要接口有两种：
- 实现回调 IUiListener：
调用 SDK 已经封装好的接口时，例如登录、快速支付登录、应用分享、应用邀请等接口，需传入该回调的实例。IUiListener 的实现示例代码如下：

```
private class BaseUiListener implements IUiListener {
 
@Override
 
public void onComplete(JSONObject response) {
 
mBaseMessageText.setText("onComplete:");
 
mMessageText.setText(response.toString());
 
doComplete(response);
 
}
 
protected void doComplete(JSONObject values) {
 
}
 
@Override
 
public void onError(UiError e) {
 
showResult("onError:", "code:" + e.errorCode + ", msg:"
 
+ e.errorMessage + ", detail:" + e.errorDetail);
 
}
 
@Override
 
public void onCancel() {
 
showResult("onCancel", "");
 
}
 
}
```
- 实现回调 IRequestListener：
使用 requestAsync、request 等通用方法调用 SDK 未封装的接口时，例如上传图片、查看相册等接口，需传入该回调的实例。IRequestListener 的实现示例代码如下：

```
private class BaseApiListener implements IRequestListener {
 
@Override
 
public void onComplete(final JSONObject response, Object state) {
 
showResult("IRequestListener.onComplete:", response.toString());
 
doComplete(response, state);
 
}
 
protected void doComplete(JSONObject response, Object state) {
 
}
 
@Override
 
public void onIOException(final IOException e, Object state) {
 
showResult("IRequestListener.onIOException:", e.getMessage());
 
}
 
@Override
 
public void onMalformedURLException(final MalformedURLException e,
 
Object state) {
 
showResult("IRequestListener.onMalformedURLException", e.toString());
 
}
 
@Override
 
public void onJSONException(final JSONException e, Object state) {
 
showResult("IRequestListener.onJSONException:", e.getMessage());
 
}
 
@Override
 
public void onConnectTimeoutException(ConnectTimeoutException arg0,
 
Object arg1) {
 
// TODO Auto-generated method stub
 
}
 
@Override
 
public void onSocketTimeoutException(SocketTimeoutException arg0,
 
Object arg1) {
 
// TODO Auto-generated method stub
 
}
 
//1.4版本中IRequestListener 新增两个异常
 
@Override
 
public void onNetworkUnavailableException(NetworkUnavailableException e, Object state){
 
// 当前网络不可用时触发此异常
 
}
 
@Override
 
public void onHttpStatusException(HttpStatusException e, Object state) {
 
// http请求返回码非200时触发此异常
 
}
 
public void onUnknowException(Exception e, Object state) {
 
// 出现未知错误时会触发此异常
 
}
 
}
```
应用在调用 SDK 提供的接口时，将实现了对应回调接口的实例传入。当 SDK 的接口调用完成后，具体如登录、应用邀请和应用分享调用完成后，会回调传入的接口实例。
>**注意：**
>应用调用 Andriod_SDK 接口时，如果要成功接收到回调，需要在调用接口的 Activity 的 onActivityResult 方法中增加如下代码：

```
@Override
 protected void onActivityResult(int requestCode, int resultCode, Intent data) {
       mTencent.onActivityResult(requestCode, resultCode, data);
 }
```
