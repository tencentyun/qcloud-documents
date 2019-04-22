## 接入要求
开发环境：Android 系统2.3以上。

## 开发步骤
1. 将 VerifySDK.jar 拷贝到 libs 目录下关联到工程。
[Android SDK 下载](https://mc.qcloudimg.com/static/archive/48720dad0a66293a8837a60b88ceef4e/archive.zip)
2. 如 AndroidManifest.xml 未声明以下权限，则添加声明。
```
<uses-permission android:name="android.permission.INTERNET" />
```
3. AndroidManifest.xml 中添加声明。
```
<--说明com.example.verifydemo业务可替换成自己包名，VerifyFullScreenActivity为全屏显示验证码，VerifyPopupActivity为弹框显示验证码-->
<activity android:name="com.example.verifydemo.VerifyFullScreenActivity"></activity> 
<activity android:name="com.example.verifydemo.VerifyPopupActivity" android:theme="@style/dialog"></activity> 
```
4. 需要下发验证码前从后台获取 jsurl（参考[服务端开发获取验证码 JSURL 的接口](https://cloud.tencent.com/document/product/283/33222)）。
5. 据业务需要实现全屏验证码界面 VerifyFullScreenActivity 或弹框验证码界面 VerifyPopupActivity。
```
//VerifyPopupActivity onCreate实现实例： @Override protected void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); this.requestWindowFeature(Window.FEATURE_NO_TITLE);
        String jsurl = getIntent().getStringExtra("jsurl"); if (jsurl == null) {
            finish(); return;
        }
        WindowManager manager = getWindowManager();
        DisplayMetrics metrics = new DisplayMetrics();
        manager.getDefaultDisplay().getMetrics(metrics);
        mDensity = metrics.density; int windowWidth = metrics.widthPixels;
        /*
        * 以滑动拼图弹框验证码为例，取弹框验证码宽度为屏幕宽度0.7
        * 滑动拼图标准宽18.2*16dp，标准高16.1*16dp,最大缩放比例2 ----capType=7
        * 图中点字标准宽18.2*16dp，标准高19.6*16dp,最大缩放比例2 ----capType=4,6
        * */ int iframeWidthPX = (int) (windowWidth * mScale); int iframeWidthDP = (int) (iframeWidthPX/mDensity); if (iframeWidthDP >= (int) (F_DEFAULT_POPUP_IFRAME_WIDTH*F_MAX_IFRAME_WIDTH_SCALE)){
            iframeWidthDP = (int) (F_DEFAULT_POPUP_IFRAME_WIDTH*F_MAX_IFRAME_WIDTH_SCALE);
            iframeWidthPX = (int) (iframeWidthDP*mDensity);
        }
        //根据验证码类型和弹框宽度，获取验证码弹框高度 int iframeHeightDP = VerifyCoder.getPopupIframeHeightByWidthAndCaptype(iframeWidthDP,F_CAP_TYPE_SLIDE_PUZZLE); int iframeHeightPX = (int) (iframeHeightDP * mDensity);
        //设置主题色，弹框验证码，弹框宽度
        VerifyCoder verifyCoder = VerifyCoder.getVerifyCoder();
        verifyCoder.setJson("themeColor:'ff0000',type:'popup',fwidth:"+iframeWidthDP);
        mWebView = verifyCoder.getWebView(getApplicationContext(), jsurl, mListener);
        mWebView.requestFocus();
        mWebView.forceLayout();
        //业务可根据自己需要实现不同的loading展现
        setContentView(R.layout.activity_verify_popup);
        mContainer = (RelativeLayout)findViewById(R.id.container);
        mProgressBar = (ProgressBar)findViewById(R.id.progressBar);
        mWebView.setVisibility(View.INVISIBLE);
        mContainer.addView(mWebView);
        android.view.WindowManager.LayoutParams attributes = getWindow().getAttributes();
        attributes.width = iframeWidthPX;
        attributes.height = iframeHeightPX;
        getWindow().setAttributes(attributes);
}
//回调VerifyListener实例
private VerifyListener mListener = new VerifyListener() {
                @Override
                public void onVerifySucc(String ticket, String randstr) {
                                //验证成功回调
                                Intent it = new Intent();
                                it.putExtra("ticket", ticket);
                                it.putExtra("randstr", randstr);
                                setResult(Activity.RESULT_OK, it);
                                finish();
                }
                @Override
                public void onVerifyFail() {
                                //验证不成功回调，如用户单击返回或关闭按钮
                                setResult(Activity.RESULT_CANCELED);
                                finish();
                }
                @Override
                public void onIframeLoaded(int state, String info) {
                                //收到验证码页面(包括图片)加载完成回调时，把Loading隐藏，WebView显示
                                mProgressBar.setVisibility(View.INVISIBLE);
                                mWebView.setVisibility(View.VISIBLE);
                }
                @Override
                public void onIFrameResize(float width, float height) {
                                //验证码弹框宽度，高度发生变化时回调
                                android.view.WindowManager.LayoutParams attributes = getWindow().getAttributes();
                                attributes.width = (int)(width*mDensity);
                                attributes.height = (int)(height*mDensity);
                                getWindow().setAttributes(attributes);
                }
}; 
```
6. 获取到 jsurl 后调用 startVerifyActivityForResult(Context context,String jsurl,int requestCode) 并实现 onActivityResult 来接收是否验证成功的通知。
```
Intent intent = new Intent(this,VerifyFullScreenActivity.class);
intent.putExtra("jsurl", jsurl); startActivityForResult(it,requestCode); //onActivityResult实现实例： @Override protected void onActivityResult(int requestCode, int resultCode, Intent data) { if (requestCode == 1) {//此处对应startVerifyActivityForResult的参数值 if(resultCode==Activity.RESULT_OK){
                Log.e("onActivityResult", "verifysucc");
                Toast.makeText(MainActivity.this, "验证成功",2000).show();
            } else{
                Toast.makeText(MainActivity.this, "未验证成功",2000).show();
            }
        }
    } 
```
7. 如有混淆，需要添加脚本。
```
<arg value="-libraryjars ${lib}/VerifySDK.jar"/>
<arg value="-keep public class com.token.verifysdk{*; }" />
```

## 其它接口说明
```		  
public static VerifyCoder getVerifyCoder() //获取单例 
public void release() //重置参数，释放资源
public void setShowtitle(boolean showtitle) //是否显示验证码页面标题栏
public void setJson(String json) //用于扩展参数，如实现自定义样式等 
public WebView getWebView(Context context,String jsurl,VerifyListener listener) //获取验证码WebView
public static int getPopupIframeHeightByWidth(int width)//根据滑动拼图弹框验证码宽度(单位dp)获取弹框验证码高度
public static int getPopupIframeHeightByWidthAndCaptype(int width, int capType)//根据弹框验证码宽度(单位dp)和验证码类型获取弹框验证码高度，图中点字类型4或6，滑动拼图类型7 
```

