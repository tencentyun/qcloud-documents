Hybrid 统计是在原生统计基础上进行的，在开始之前请确保已按照 [Android SDK 接入指南](https://cloud.tencent.com/document/product/549/12863) 正常接入 MTA Android SDK 配置和初始化流程。
### 初始化 Hybrid 模块
在 Application 或 MainActivity 的 onCreate 初始化 MTA 基础统计接口后，需要额外调用以下接口，初始化 Hybrid 模块，开发者可根据是否使用与原生 App 一致的 Appkey 来决定灵活使用哪个初始化接口。

```java
/**
* 初始化Hybrid模块，默认使用原生App的appkey、渠道等配置信息
* @param context 上下文对象
*/
public static void init(Context context);

/**
* 初始化Hybrid模块，使用指定的appkey和渠道信息
* @param context 上下文对象
* @param appkey Hybrid统计所使用的Appkey
* @param channel Hybrid统计所使用的渠道
*/
public static void init(Context context, String appkey, String channel);
```
#### 示例

```java
public class MyApp extends Application{
	public static Application application = null;
	@Override
	public void onCreate() {
		super.onCreate();
		// 其它代码

		// 使用默认Appkey初始化Hybrid模块
		StatHybridHandler.init(this);
	}
}
```
### 配置 WebView
在需要使用 Hybrid 统计的 WebView 组件，调用以下方法进行初始化。
#### 初始化 WebSettings

```java
/**
* 初始化WebSettings
* @param webSettings 待初始化的webSettings
*/
public static void initWebSettings(WebSettings webSettings)
```
#### 示例

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
	super.onCreate(savedInstanceState);
	webView = (WebView) findViewById(R.id.webview);
	webSettings.setJavaScriptEnabled(true);
	StatHybridHandler.initWebSettings(webSettings);
	webView.setWebViewClient(new MyWebViewClient());
}
```

### 配置 WebViewClient
Natiive 使用拦截 MTA 专用的 url 跳转方式与 H5 交互，因此需在 WebViewClient 的 shouldOverrideUrlLoading 方法调用 SDK 接口，进行 url 拦截。
```java
/**
* 拦截MTA专用url跳转
* @param webView 当前WebView
* @param url i当前url
* 返回值 true：该url为mta特有url并处理；false：其它url，需要继续处理
*/
public static boolean handleWebViewUrl(WebView webView, String url);
```
#### 示例
```java
public class MyWebViewClient extends WebViewClient {
	@Override
	public boolean shouldOverrideUrlLoading(WebView view, String url) {
		// 尽量保证放在第一行
		if(StatHybridHandler.handleWebViewUrl(view, url)){
			return true;
		}		
		super.shouldOverrideUrlLoading(view, url);
		return true;
	}
}

// 如果不能保证放在第一行处理，请按照以下方式处理
public class MyWebViewClient extends WebViewClient {
	@Override
	public boolean shouldOverrideUrlLoading(WebView view, String url) {
		try {
			String decodedURL = java.net.URLDecoder.decode(url, "UTF-8");
			if (!TextUtils.isEmpty(decodedURL) && 
			url.toLowerCase().startsWith(StatHybridHandler.URI_PREFIX.toLowerCase()){
				StatHybridHandler.handleWebViewUrl(view, url);
				return true;
			}else{
				// 其它url的处理逻辑
			}
		}catch (UnsupportedEncodingException ex){
		}		
		return super.shouldOverrideUrlLoading(view, url);
	}
}

```
