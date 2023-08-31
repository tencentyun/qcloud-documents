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
由于 Android 机器碎片化严重，用系统 WebView 调起系统摄像头完成视频录制可能存在很多兼容性问题，如部分机器出现调不起摄像头、调起摄像头无法录制视频等。因此整理了接入指引。H5 刷脸包括 trtc 和录制模式，合作方需要对这两种模式都做兼容性配置。
请合作方**务必**按照如下步骤顺序，实现兼容性处理：
1. 引入工具类
将 WBH5FaceVerifySDK.java 文件拷贝到项目中。该文件下载地址：`https://share.weiyun.com/1gzWlyKj`（密码请 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取）。
2. 申请权限
 - 在 Manifest.xml 文件中增加申请以下权限
```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
```
 - 动态申请权限
    - 如果第三方编译的 targetSdkVersion >= 23，则需要动态申请权限。
    - 如果第三方编译的 targetSdkVersion < 23，则不需要动态申请权限。
    - 权限代码申请处理逻辑，demo 仅供参考，合作方可根据自身业务需求自行处理。
    - 一定要在动态权限申请成功后，才能去调用 enterOldModeFaceVerify() 录制模式或enterTrtcFaceVerify() trtc 模式体验 h5 刷脸功能。
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
调用 WebView.loadUrl(String url) 前，WebView 必须调用 setWebChromeClient(WebChromeClient webChromeClient)，并重写 WebChromeClient 的如下5个函数：
```
/**
     *TRTC 刷脸模式配置，这里负责处理来自H5页面发出的相机权限申请
     * @param request 来自H5页面的权限请求
     */
    @Override
    public void onPermissionRequest(PermissionRequest request) {
       if (request!=null&&request.getOrigin()!=null&&WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(request.getOrigin().toString())){  //判断是腾讯h5刷脸的域名
            Log.d(TAG,"onPermissionRequest 收到腾讯h5刷脸页面的相机授权");
            this.request=request;
            if (activity!=null){ 
				//申请相机权限，申请权限的代码demo仅供参考，合作方可根据自身业务定制
                activity.requestCameraPermission();
            }
        }
    }

    /**
     * 相机权限申请成功后，拉起TRTC刷脸模式进行实时刷脸验证
     */
	public void enterTrtcFaceVerify(){
		if (Build.VERSION.SDK_INT>Build.VERSION_CODES.LOLLIPOP){  // android sdk 21以上
			if (request!=null&&request.getOrigin()!=null){
				if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(request.getOrigin().toString())){  //判断是腾讯h5刷脸的域名，如果合作方对授权域名无限制的话，这个if条件判断可以去掉，直接进行授权即可。
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

     // For Android >= 4.1  录制模式中，点击h5页面的录制按钮后触发的系统方法
    public void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType, String capture) {
        if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(null,null,acceptType)){ //判断是腾讯h5刷脸的域名
            this.uploadMsg=uploadMsg;
            this.acceptType=acceptType;
            if (activity!=null){ 
                //申请系统的相机、录制、sd卡等权限
                activity.requestCameraAndSomePermissions(true,false);
            }
        }
    }

    // For Lollipop 5.0+ Devices  录制模式中，点击h5页面的录制按钮后触发的系统方法
    @TargetApi(21)
    @Override
	public boolean onShowFileChooser(WebView webView, ValueCallback<Uri[]> filePathCallback, FileChooserParams fileChooserParams) {
        if (WBH5FaceVerifySDK.getInstance().isTencentH5FaceVerify(webView,fileChooserParams,null)){ //判断是腾讯h5刷脸的域名
            this.webView=webView;
            this.filePathCallback=filePathCallback;
            this.fileChooserParams=fileChooserParams;
            if (activity!=null){
				//申请系统的相机、录制、sd卡等权限
                activity.requestCameraAndSomePermissions(false,false);
            }
		}
        return true;   
	}
	
    //录制模式中，拉起系统相机进行录制视频
    public boolean enterOldModeFaceVerify(boolean belowApi21){
        if (belowApi21){ // For Android < 5.0
            if (WBH5FaceVerifySDK.getInstance().recordVideoForApiBelow21(uploadMsg, acceptType, activity)) {
                return true;
            }
        }else { // For Android >= 5.0
            if (WBH5FaceVerifySDK.getInstance().recordVideoForApi21(webView, filePathCallback, activity,fileChooserParams)) {
                return true;
            }
        }
        return false;
    }
```
>! 
>- 如果第三方已重写以上函数，只要将如上述所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方没有重写以上函数，则直接按上述所示重写。
>- WebView 不要使用 layerType 属性，否则导致刷脸界面白屏。
>

5. 重写 Activity
 WebView 所属的 Activity 必须重写如下函数：
>!
>- 如果第三方 WebView 所属的 Activity 已重写以下函数，则将如下所示的函数体内容添加至第三方的对应函数体首行即可。
>- 如果第三方 WebView 所属的 Activity 没有重写以下函数，则直接按以下代码重写。
>
```
Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        Log.d(TAG, "onActivityResult --------"+requestCode);
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == VIDEO_REQUEST) {//录制模式中，调用系统相机录制完视频后再回到当前app页面
            if (WBH5FaceVerifySDK.getInstance().receiveH5FaceVerifyResult(requestCode, resultCode, data)) {
                return;
            }
        }else if (requestCode==PERMISSION_QUEST_TRTC_CAMERA_VERIFY){ //trtc模式中，申请相机权限时，从系统设置页面跳转回当前app页面的处理。由于权限申请逻辑demo仅供参考，合作方自己处理即可。
            requestCameraPermission();
        }else if (requestCode==PERMISSION_QUEST_CAMERA_RECORD_VERIFY){//录制模式中，申请权限时，从系统设置页面跳转回当前app页面的处理。由于权限申请逻辑demo仅供参考，合作方自己处理即可。
            requestCameraAndSomePermissions(false);
        }
    }
```

## Uniapp 接入（ Android）
1. 注册并创建 uni-app 开发环境。
uni-app 开发接⼊具体参照 uni 官⽹。
2.  下载 demo 并根据指引配置插件。
demo下 载地址：`https://share.weiyun.com/1gzWlyKj`（密码请 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取）。
	- 在 uni-app 工程 nativeplugins 目录下，放置 only android 插件以及插件的配置文件。
![](https://qcloudimg.tencent-cloud.cn/raw/b6c46471472e8deeedfd2d0adf3db5f1.png)
	- 在 uni-app 页面中调用插件方法，实现 H5 刷脸功能。
```
const h5FaceVerifyPlugin  = uni.requireNativePlugin('DC-WBH5FaceVerifyService');
        export default {
                methods: {
                        enterH5FaceVerify() {
                                let url="https://kyc.qcloud.com/s/web/h5/#/entry";//拉起h5刷脸的url
                                let thirdurl="https://www.qq.com/";//h5刷脸完成后要跳转的接入方的url，这个接入方填写自己的url
                                h5FaceVerifyPlugin.startH5FaceVerify({h5faceurl:url,
                                h5thirdurl:thirdurl},result => {
                                        console.log(result,"H5刷脸后跳转到thirdurl所在h5页面的回调");
                                        h5FaceVerifyPlugin.destroyH5Activity(null);//调用关闭插件的webView.
                                        //uniapp todo 接入方自己的逻辑
                                        
                                },result=>{
                                        //这里是终端接受h5页面的消息回调。uniapp与h5页面两者通信可通过这个回调作为中间桥接实现。
                                        //注意：约定h5页面和webView通信通过JavaScriptInterface接口和JavaScript进行交互。
                                        //在H5页面中使用window.tencentApi.postMessage的方式来调用这个方法，参数为String类型。
                                        //如果是jsonobject需要转String
                                        console.log(result,"自定义回调");
                                        //uniapp todo 接入方自己的逻辑
                                });
                                console.log("click=======意愿性刷脸====>startH5FaceVerify");
                        }
                }
        }
```
>! 调用 destroyH5Activity() 可主动关闭插件。

