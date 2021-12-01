



## 前提条件
接入验证码前，进入[图形验证](https://console.cloud.tencent.com/captcha/graphical)  页完成新建验证。可在**验证列表**查看 验证码接入所需的 CaptchaAppId 及 AppSecretKey。
![](https://main.qcloudimg.com/raw/a15105526bbcf8c0b51b5cdafeefb92c.png)

## 接入步骤
以下为 App 端接入流程，适用于每次都需要进行人机验证的场景（如登录、注册、下发短信、活动等），App（iOS 和 Android） 皆使用 Web 前端 H5 方式进行接入。

### Android 接入
#### **Android 接入主要流程如下：**
1. 在 Android 端利用 WebView 加载，需要接入滑动验证码组件的页面。
2. 通过 JS 调用代码，并把验证码 SDK 返回的参数值传到 Android App 的业务端。
3. Android 代码中获取票据后，把相关数据传入业务侧后端服务进行验证。

#### **Android 接入的详细操作步骤如下：**
1. 在项目的工程中，新建一个 Activity 并导入 WebView 组件所需的包。
```
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebViewClient;
import android.webkit.WebChromeClient;
```
2. 添加相关权限，如开启网络访问权限以及允许 App 进行非 HTTPS 请求等。
```
<uses-permission android:name="android.permission.INTERNET"/>
<application android:usesCleartextTraffic="true">...</application>
```
3. 在 Activity 的布局文件中，添加 WebView 组件。
```
<WebView
android:id="@+id/webview"
android:layout_height="match_parent"
android:layout_width="match_parent"
/>
```
4. 在项目的工程中，添加自定义 JavascriptInterface 文件，并定义一个方法用来获取相关数据。
```
import android.webkit.JavascriptInterface;
public class JsBridge {
@JavascriptInterface
public void getData(String data) {
System.out.println(data);
}
}
```
5. 在 Activity 文件中，加载相关 H5 业务页面。
```
public class MainActivity extends AppCompatActivity {
private WebView webview;
private WebSettings webSettings;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
initView();
}

private void initView() {
webview = (WebView) findViewById(R.id.webview);
webSettings = webview.getSettings();
webSettings.setUseWideViewPort(true);
webSettings.setLoadWithOverviewMode(true);
// 禁用缓存
webSettings.setCacheMode(WebSettings.LOAD_NO_CACHE);
webview.setWebViewClient(new WebViewClient(){
@Override
public boolean shouldOverrideUrlLoading(WebView view, String url) {
view.loadUrl(url);
return true;
}
});
// 开启js支持
webSettings.setJavaScriptEnabled(true);
webview.addJavascriptInterface(new JsBridge(), "jsBridge");
// 也可以加载本地html(webView.loadUrl("file:///android_asset/xxx.html"))
webview.loadUrl("https://x.x.x/x/");
}
}
```
6. 在 H5 业务页面中，集成验证码 SDK，并通过 JS 调用 SDK 获取验证码相关数据，最后使用 JSBridge 传回数据给具体业务端。
>!如需隐藏验证码帮助按钮等功能，请参见 [Web 前端接入](https://cloud.tencent.com/document/product/1110/36841) 文档。
>
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web 前端接入示例</title>
    <!-- 验证码程序依赖(必须)。请勿修改以下程序依赖，如使用本地缓存，或通过其他手段规避加载，会影响程序的正常使用。 -->
    <script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
</head>

<body>
    <!--点击此元素会自动激活验证码, 此例使用的button元素, 也可以使用div、span等-->
    <!--id :            (不可变) 元素的 ID, 值必须是 'TencentCaptcha'-->
    <!--data-appid :    (必须) 验证码CaptchaAppId, 从腾讯云的验证码控制台中获取, 验证码控制台页面内【图形验证】>【验证列表】进行查看 。如果未新建验证，请根据业务需求选择适合的验证渠道、验证场景进行新建-->
    <!--data-cbfn :     (必须) 回调函数名, 函数名要与 data-cbfn 相同-->
    <!--data-biz-state :(可选) 业务自定义透传参数, 会在回调函数内获取到 （res.bizState）-->
    <button id="TencentCaptcha" data-appid="你的验证码CaptchaAppId" data-cbfn="callbackName" data-biz-state="data-biz-state"
        type="button">验证</button>
</body>

<script>
    // 回调函数需要放在全局对象window下
    window.callbackName = function (res) {
        // 返回结果
        // ret         Int       验证结果，0：验证成功。2：用户主动关闭验证码。
        // ticket	  String	验证成功的票据，当且仅当 ret = 0 时 ticket 有值。
        // CaptchaAppId	   String	验证码应用ID。
        // bizState	Any	   自定义透传参数。
        // randstr	 String	本次验证的随机串，请求后台接口时需带上。
        console.log('callback:', res);


        // res（用户主动关闭验证码）= {ret: 2, ticket: null}
        // res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
        if (res.ret === 0) {
                // 获取票据、随机数并调用App端注入的方法传入票据、随机数，进行后台票据校验
                var result = { randstr:res.randstr, ticket:res.ticket };
                window.jsBridge.getData(JSON.stringify(result));
        }
    }
</script>
</html>
```


### iOS 接入
#### **iOS 接入主要流程如下：**
1. 在 iOS 中打开 WebView，通过 JSBridge 触发 HTML 页面 ，同时注入方法，供 HTML 调用传入票据结果。
2. 在 HTML 页面中，接入示例代码，滑动验证码后，需要在回调函数中判断票据，并调用 iOS 注入的方法传入票据结果。
3. 需要回调数据通过 JSBridge 返回到 iOS，需要把票据传入业务侧后端服务。

#### **iOS 接入的详细操作步骤如下：**
1. 在控制器或 view 中导入 WebKit 库。
```
#import <WebKit/WebKit.h>
```
2. 创建 WebView 并渲染。
```
-(WKWebView *)webView{
if(_webView == nil){    
    //创建网页配置对象
    WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];
    // 创建设置对象
    WKPreferences *preference = [[WKPreferences alloc]init];
    //设置是否支持 javaScript 默认是支持的
    preference.javaScriptEnabled = YES;
    // 在 iOS 上默认为 NO，表示是否允许不经过用户交互由 javaScript 自动打开窗口
    preference.javaScriptCanOpenWindowsAutomatically = YES;
    config.preferences = preference;      
    //这个类主要用来做 native 与 JavaScript 的交互管理
    WKUserContentController * wkUController = [[WKUserContentController alloc] init];
    //注册一个name为jsToOcNoPrams的js方法 设置处理接收JS方法的对象
    [wkUController addScriptMessageHandler:self  name:@"jsToOcNoPrams"];
    [wkUController addScriptMessageHandler:self  name:@"jsToOcWithPrams"]; 
    config.userContentController = wkUController;     
    _webView = [[WKWebView alloc] initWithFrame:CGRectMake(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT) configuration:config];
    // UI 代理
    _webView.UIDelegate = self;
    // 导航代理
    _webView.navigationDelegate = self;        
    //此处即需要渲染的网页
    NSString *path = [[NSBundle mainBundle] pathForResource:@"JStoOC.html" ofType:nil];
    NSString *htmlString = [[NSString alloc]initWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil];
    [_webView loadHTMLString:htmlString baseURL:[NSURL fileURLWithPath:[[NSBundle mainBundle] bundlePath]]];       
}
return _webView;
}
[self.view addSubview:self.webView];
```
3. 代理方法，处理一些响应事件。
```
// 页面开始加载时调用
-(void)webView:(WKWebView *)webView didStartProvisionalNavigation:(WKNavigation *)navigation {
}
// 页面加载失败时调用
-(void)webView:(WKWebView *)webView didFailProvisionalNavigation:(null_unspecified WKNavigation *)navigation withError:(NSError *)error {
[self.progressView setProgress:0.0f animated:NO];
}
// 当内容开始返回时调用
-(void)webView:(WKWebView *)webView didCommitNavigation:(WKNavigation *)navigation {
}
// 页面加载完成之后调用
-(void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation {
[self getCookie];
}
//提交发生错误时调用
-(void)webView:(WKWebView *)webView didFailNavigation:(WKNavigation *)navigation withError:(NSError *)error {
[self.progressView setProgress:0.0f animated:NO];
}
// 接收到服务器跳转请求即服务重定向时之后调用
-(void)webView:(WKWebView *)webView didReceiveServerRedirectForProvisionalNavigation:(WKNavigation *)navigation {
}
```
4. JS 将参数传给 OC。
```
<p style="text-align:center"> <button id="btn2" type = "button" onclick = "jsToOcFunction()"> JS调用OC：带参数  </button> </p>
function jsToOcFunction()
{
window.webkit.messageHandlers.jsToOcWithPrams.postMessage({"params":"res.randstr"});
}
```
5. 将渲染好的 WebView 展示在视图上，调用验证码服务，将数据传给客户端。
>!如需隐藏验证码帮助按钮等功能，请参见 [Web 前端接入](https://cloud.tencent.com/document/product/1110/36841#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 文档。
>
```
-(void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message{
此处message.body即传给客户端的json数据
//用message.body获得JS传出的参数体
NSDictionary * parameter = message.body;
//JS调用OC
if([message.name isEqualToString:@"jsToOcWithPrams"]){
//在此处客户端得到js透传数据 并对数据进行后续操作
parameter[@"params"]
}
}
```
>!验证码客户端接入完成后，验证码后台需二次核查验证码票据结果，请进行 [后台 API 接入](https://console.cloud.tencent.com/api/explorer?Product=captcha&Version=2019-07-22&Action=DescribeCaptchaResult&SignVersion=) 操作，确保验证安全性。更多详情请参见 [核查验证码票据文档](https://cloud.tencent.com/document/product/1110/36926) 。


## 热点问题
#### Android 使用 Web 前端 H5 方式进行接入，调试过程中先弹出空白背景，后弹出验证码页面如何调整？
- 调试过程中，正常情况下会首先调起 webview 加载网页，然后弹出验证码页面。
- 如果出现先弹出空白背景，后弹出图形验证页面的现象。形成原因如下：
    - 加载验证码 js 的时间导致白屏。
    - 空白层形成原因是页面没有内容时，加载的 webview 就显示出来，需要等待 ready 事件触发后再进行 webview 展示。
- 因此，Android 需要先加载页面但不进行展示，等待 ready 回调后，再通知 Android 进行展示。ready 配置说明，请参见 [Web 前端接入-配置参数](https://cloud.tencent.com/document/product/1110/36841#.3Ca-id.3D.22pzcs.22.3E.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0.3C.2Fa.3E) 文档。
```
options={ready: function(size){
  // 与Android通信
}}
new TencentCaptcha(appId, callback, options);
```

####  App 端接入验证码显示不完整如何调整？
验证码根据容器宽高进行居中显示，验证码显示不完整可能由于容器本身设置较宽，导致展示的验证码被截断，该情况需要对客户端的弹框进行调整。此外随意加载其他 webview 都可能会出现截断的情况。

####  验证码是否支持使用 uni-app 原生插件进行接入？
验证码 App 端（iOS 和 Android）皆使用 Web 前端 H5 方式进行接入，暂不支持使用 uni-app 原生插件进行接入。


## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**，了解更多详细信息。

