本文将为您介绍 App（iOS 和 Android）如何通过 Web 前端 H5 方式接入验证码。
## 前提条件
接入验证码前，需要先在 [验证码控制台](https://console.cloud.tencent.com/captcha) 中注册 AppID 和 AppSecretKey。注册完成后，您可以在控制台的基础配置中，查看 AppID 以及 AppSecretKey。
>!小程序插件 AppID 仅限 [小程序插件接入方式](https://cloud.tencent.com/document/product/1110/49319) 使用，请勿使用在 Web 前端接入。

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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
</head>
    <script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
<body>    
</body>
<script>
    var captcha = new TencentCaptcha('appId', function(res) {
        /* callback */
                if(res && res.ret === 0) {
                        // 获取票据、随机数并调用App端注入的方法传入票据、随机数，进行后台票据校验
						var result = { randstr:res.randstr, ticket:res.ticket };
					    window.jsBridge.getData(JSON.stringify(result));
                }
    });
    captcha.show(); // 显示验证码
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
    //在此处客户端得到js透传数据  并对数据进行后续操作
    parameter[@"params"]
    }
}
```


## 后续步骤
至此，验证码客户端接入已完成，验证码后台需二次核查验证码票据结果，您需要进行后台 API 接入，即 [核查验证码票据结果](https://cloud.tencent.com/document/product/1110/36926) 操作，确保验证安全性。

## 更多信息
您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击【快速咨询】，了解更多详细信息。
