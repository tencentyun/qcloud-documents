请按照下文兼容性配置指引进行 iOS 及 Android 手机的兼容性适配。
## iOS 接入
iPhone 的兼容性适配，需在配置里加上摄像头和麦克风的使用权限。App 的 info.plist 中加入：
```
.NSMicrophoneUsageDescription  
.NSCameraUsageDescription
```
使用 WKWebView 时，需要通过 WKWebViewConfiguration 配置允许使用相机：
```
WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];
config.allowsInlineMediaPlayback = YES;
```

## Android 接入
由于 Android 机器碎片化严重，用系统 WebView 调起系统摄像头完成视频录制可能存在很多兼容性问题，如部分机器出现调不起摄像头、调起摄像头无法录制视频等。因此整理了接入指引。H5 刷脸包括 trtc 和录制模式，合作方需要对这两种模式都做兼容性配置。
请合作方**务必**按照如下步骤顺序，实现兼容性处理：
1. 引入工具类
将 WBH5FaceVerifySDK.java 文件拷贝到项目中。该文件下载地址：`https://share.weiyun.com/1gzWlyKj`（密码请联系对接人获取）。
2. 申请权限
在 Manifest.xml 文件中增加申请以下权限：
```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```
动态申请权限：
	- 如果第三方编译的 targetSdkVersion >= 23，则需要动态申请权限。
	- 如果第三方编译的 targetSdkVersion < 23，则不需要动态申请权限。
	- 权限代码申请处理逻辑，demo 仅供参考，合作方可根据自身业务需求自行处理。
	- 一定要在动态权限申请成功后，才能去调用 WBH5FaceVerifySDK的enterOldModeFaceVerify() 录制模式或 enterTrtcFaceVerify() trtc 模式体验 h5 刷脸功能。

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
调用 WebView.loadUrl(String url) 前，WebView 必须调用 setWebChromeClient(WebChromeClient webChromeClient)，并重写 WebChromeClient 的如下2个函数：
```
/**
     *TRTC 刷脸模式配置，这里负责处理来自H5页面发出的相机权限申请
     * @param request 来自H5页面的权限请求
     */
    @Override
    public void onPermissionRequest(PermissionRequest request) {
        this.request=request;
        if (activity!=null){
            activity.requestCameraAndRecordPermissions(false,true);//申请相机和录音权限，申请权限的代码demo仅供参考，合作方可根据自身业务定制
        }
    }

    /**
     * 相机权限申请成功后，拉起H5意愿刷脸模式进行实时刷脸验证
     */
    public void enterWillFaceVerify(){
       if (Build.VERSION.SDK_INT>Build.VERSION_CODES.LOLLIPOP){ // android sdk 21以上
            if (request!=null&&request.getOrigin()!=null){
                //根据腾讯域名授权，如果合作方对授权域名无限制的话，这个if条件判断可以去掉，直接进行授权即可。
                Log.d(TAG,"enterTrtcFaceVerify getOrigin()!=null");
                if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(request.getOrigin().toString())){
                    //授权
                    request.grant(request.getResources());
                    request.getOrigin();
                 }
              }else {
                 if (request==null){
                    Log.d(TAG,"enterTrtcFaceVerify request==null");
                    if (webView!=null&&webView.canGoBack()){
                        webView.goBack();
                    }
                 }
              }
         }
    }
```
>! 
>- 如果第三方已重写以上函数，只要将如上述所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方没有重写以上函数，则直接按上述所示重写。
>- WebView 不要使用 layerType 属性，否则导致刷脸界面白屏。

5. 重写 Activity
>! 
>- 如果第三方 WebView 所属的 Activity 已重写以下函数，则将如下所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方 WebView 所属的 Activity 没有重写以下函数，则直接按以下代码重写。
>
WebView 所属的 Activity 必须重写如下函数：
```
Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        Log.d(TAG, "onActivityResult --------"+requestCode);
        super.onActivityResult(requestCode, resultCode, data);
         if (requestCode==PERMISSION_QUEST_CAMERA_RECORD_VERIFY){//录制模式中，申请权限时，从系统设置页面跳转回当前app页面的处理。由于权限申请逻辑demo仅供参考，合作方自己处理即可。
            requestCameraAndRecordPermissions(false,true);  
          }
    }
```
