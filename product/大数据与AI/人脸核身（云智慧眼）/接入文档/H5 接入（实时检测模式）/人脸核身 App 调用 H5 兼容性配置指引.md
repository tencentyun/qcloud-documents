请按照下文**兼容性配置**指引进行 iOS 及 Android 手机的兼容性适配。

## iOS 接入
iPhone 的兼容性适配，需在配置里加上摄像头和麦克风的使用权限。App 的 info.plist 中加入：
```
.NSMicrophoneUsageDescription  
.NSCameraUsageDescription
```
**使用 WKWebView 时，需要通过 WKWebViewConfiguration 配置允许使用相机：**
```
WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];
config.allowsInlineMediaPlayback = YES;
```
 
## Android 接入
由于 Android 机器碎片化严重，用系统 WebView 调起系统摄像头完成视频录制可能存在很多兼容性问题，如部分机器出现调不起摄像头、调起摄像头无法录制视频等。因此整理了接入指引。请合作方**务必**按照如下步骤顺序，实现兼容性处理：
1. 引入工具类
 将 WBH5FaceVerifySDK.java 文件拷贝到项目中。该文件下载地址：`https://share.weiyun.com/5VTnQgj`（密码请联系对接人获取）
2. 申请权限
 - 在 Manifest.xml 文件中增加申请以下权限
```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```
 - 动态申请权限
    - 如果第三方编译的 targetSdkVersion >= 23，则需要动态申请权限。
    - 如果第三方编译的 targetSdkVersion < 23，则不需要动态申请权限。
3. 设置 WebSettings
 调用 WebView.loadUrl(String url) 前一行添加如下代码设置 WebSettings。
```
/**
* 对 WebSettings 进行设置：添加 ua 字段和适配 h5 页面布局等
* @param mWebView  第三方的 WebView 对象
* @param context  第三方上下文
*/
WBH5FaceVerifySDK.getInstance().setWebViewSettings(mWebView,getApplicationContext());
```
4. 重写 WebChromeClient
 调用 WebView.loadUrl(String url) 前，WebView 必须调用 setWebChormeClient(WebChromeClient webChormeClient)，并重写 WebChromeClient 的如下三个函数：
>!
>- 如果第三方已重写以下函数，只要将如下所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方没有重写以下函数，则直接按以下代码示重写。
>- WebView 不要使用 layerType 属性，否则导致刷脸界面白屏。
>
```
/**
 * H5_TRTC刷脸配置，这里负责处理授权来自H5界面发来的相机权限申请
 * @param request 来自h5界面的权限请求
 */
@Override
public void onPermissionRequest(PermissionRequest request) {
	if (Build.VERSION.SDK_INT>Build.VERSION_CODES.LOLLIPOP){ // android sdk 21以上
		request.grant(request.getResources());
		request.getOrigin();
	}
}
/**
* android端接收H5端发来的请求
For Android >= 3.0
*/
public void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType) {        
	if(WBH5FaceVerifySDK.getInstance().recordVideoForApiBelow21(uploadMsg, acceptType,activity))
		return;
    // TODO: 第三方有调用系统相机处理其他业务的话，将相关逻辑代码放在下面    
}
/**
* android端接收H5端发来的请求
For Android >= 4.1
*/
public void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType, String capture) {
	if(WBH5FaceVerifySDK.getInstance().recordVideoForApiBelow21(uploadMsg, acceptType,activity))
		return;
    // TODO: 第三方有调用系统相机处理其他业务的话，将相关逻辑代码放在下面
}
/**
* android端接收H5端发来的请求
For Lollipop 5.0+ Devices
*/
@Override
public boolean onShowFileChooser(WebView webView, ValueCallback<Uri[]> filePathCallback, FileChooserParams fileChooserParams) {
	if(WBH5FaceVerifySDK.getInstance().recordVideoForApi21(webView, filePathCallback,activity, fileChooserParams)){
		return true;
	}
 // TODO: 第三方有调用系统相机处理其他业务的话，将相关逻辑代码放在下面
	return true;
}
```
5. 重写 Activity
 WebView 所属的 Activity 必须重写如下函数：
>!
>- 如果第三方 WebView 所属的 Activity 已重写以下函数，则将如下所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方 WebView 所属的 Activity 没有重写以下函数，则直接按以下代码重写。
>
```
/**
*返回到WebView所属的Activity的回调
*/
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (WBH5FaceVerifySDK.getInstance().receiveH5FaceVerifyResult(requestCode,resultCode,data))
        return;
// TODO: 第三方有其他请求的返回结果要处理的话，将相关逻辑代码放在下面

}
```
