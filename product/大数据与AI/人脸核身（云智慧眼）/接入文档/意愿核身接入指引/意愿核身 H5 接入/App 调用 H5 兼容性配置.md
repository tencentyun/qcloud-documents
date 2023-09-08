>? 接入前务必注意：请参见 [移动 H5 意愿核身接入步骤](https://cloud.tencent.com/document/product/1007/77303) 进行接入，如是 App 调用，务必按照 [App 调用 H5 兼容性配置](https://cloud.tencent.com/document/product/1007/77304) 进行兼容性适配，否则将影响正常使用。
## 兼容性说明
因网页端实时音视频技术是在2017年初次提出，对浏览器和手机系统存在兼容性要求，经过大规模测试，腾讯云 H5 实时检测意愿核身的兼容性情况如下：
<table>
<thead>
<tr>
<th >手机平台</th>
<th >应用端</th>
<th >应用端说明</th>
<th >兼容性要求</th>
<th >机型支持率</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2 >iOS</td>
<td>App</td>
<td >在客户自有 App 中使用，适用于在客户 App 中触达用户的业务场景</td>
<td>iOS 系统版本14.3+，需按照 <a href ="https://cloud.tencent.com/document/product/1007/77304">App 调用 H5 兼容性配置</a> 做适配</td>
<td>90%</td>
</tr>
<tr>
<td>浏览器</td>
<td >在手机浏览器使用，适用于通过短信或其他方式发送链接触达用户的业务场景</td>
<td>iOS 系统版本11.1.2+，支持 Safari 浏览器，浏览器版本11+</td>
<td>100%</td>
</tr>
<tr>
<td rowspan=3>Android</td>
<td>App</td>
<td >在客户自有 App 中使用，适用于在客户 App 中触达用户的业务场景</td>
<td>Android 系统版本7+，需按照 App 调用 H5 兼容性配置做适配</td>
<td>95%</td>
</tr>
<tr>
<td>自带浏览器</td>
<td >在手机系统自带浏览器使用，适用于通过短信或其他方式发送链接触达用户的业务场景</td>
<td>Android 系统版本7+ 华为、OPPO、VIVO、魅族、荣耀、三星等自带浏览器兼容性较好（支持率80%），小米自带浏览器兼容性一般（支持率30%）</td>
<td>60%</td>
</tr>
<tr>
<td>QQ 浏览器</td>
<td >在 QQ 浏览器使用，适用于通过短信或其他方式发送链接触达用户的业务场景</td>
<td>Android 系统版本7+，支持 QQ 浏览器，不支持 UC、百度浏览器</td>
<td>100%</td>
</tr>
</tbody>
</table>

- 采用达到版本要求的具有一定市场占有率的主流手机型号，测试机型共计829款。
- Android 手机测试品牌名单（按拼音排序）：HTC、OPPO、OPPO_REALME、VIVO、VIVO_IQOO、锤子-坚果、黑鲨、华硕、华为、荣耀、金立、联想、魅族、魅族-魅蓝、努比亚、努比亚-红魔、三星-GALAXY、小米、小米-红米、一加、中兴。

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
    H5意愿刷脸模式配置，这里负责处理来自H5页面发出的相机权限申请
     * @param request 来自H5页面的权限请求
     */
    @Override
    public void onPermissionRequest(PermissionRequest request) {
      if (request!=null&&request.getOrigin()!=null&&WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(request.getOrigin().toString())){ //通过url判断是腾讯意愿性h5刷脸的域名
        this.request=request;
        if (activity!=null){
            activity.requestCameraAndRecordPermissions(false,true);//申请相机和录音权限，申请权限的代码demo仅供参考，合作方可根据自身业务定制
        }
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
                if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(request.getOrigin().toString())){
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
    
    
     // For Android >= 4.1  降级为录制模式，收到h5页面发送的录制请求
    public void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType, String capture) {
        Log.d(TAG,"openFileChooser-------");
        if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(null,null,acceptType)){ //true 说明是腾讯的h5刷脸页面
            this.uploadMsg=uploadMsg;
            this.acceptType=acceptType;
            if (activity!=null){ //申请系统的相机、录制、sd卡等权限
                activity.requestCameraAndSomePermissions(true);
            }
        }

    }

    // For Lollipop 5.0+ Devices  降级为录制模式，收到h5页面发送的录制请求
    @TargetApi(21)
    @Override
    public boolean onShowFileChooser(WebView webView, ValueCallback<Uri[]> filePathCallback, FileChooserParams fileChooserParams) {
        Log.d(TAG,"onShowFileChooser-------");
        if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(webView,fileChooserParams,null)){ //true说 明是腾讯的h5刷脸页面
            this.webView=webView;
            this.filePathCallback=filePathCallback;
            this.fileChooserParams=fileChooserParams;
            if (activity!=null){ //申请系统的相机、录制、sd卡等权限
                activity.requestCameraAndSomePermissions(false);
            }
        }
        return true;

    }

    //降级为录制模式，拉起系统相机进行录制视频
    public boolean enterOldModeFaceVerify(boolean belowApi21){
        Log.d(TAG,"enterOldFaceVerify");
        if (belowApi21){ // For Android < 5.0
            if (WBH5FaceVerifySDK.getInstance().recordVideoForApiBelow21(uploadMsg, acceptType, activity)) { //腾讯的h5刷脸
                return true;
            }else {
                // todo 合作方如果其他的h5页面处理，则再次补充其他页面逻辑
            }
        }else { // For Android >= 5.0
            if (WBH5FaceVerifySDK.getInstance().recordVideoForApi21(webView, filePathCallback, activity,fileChooserParams)) {  //腾讯的h5刷脸
                return true;
            }else {
                // todo 合作方如果其他的h5页面处理，则再次补充其他页面逻辑

            }
        }
        return false;
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
         if (requestCode == 0x11) { //传统录制模式，收到录制模式调用系统相机录制完成视频的结果
            Log.d(TAG, "onActivityResult recordVideo");
            if (WBH5FaceVerifySDK.getInstance().receiveH5FaceVerifyResult(requestCode, resultCode, data)) {
                return;
            }
        } else if (requestCode == PERMISSION_QUEST_WILL_CAMERA_RECORD_VERIFY) { //意愿性刷脸模式，从设置界面返回。
            Log.d(TAG, "onActivityResult willface cameraAndRecord");
            requestCameraAndRecordPermission();
        }else if (requestCode == PERMISSION_QUEST_CAMERA_RECORD_VERIFY) { //传统录制模式，从设置界面返回。
            Log.d(TAG, "onActivityResult cameraAndSome");
            requestCameraAndSomePermissions(false);
        }
   }

```
