Hybrid tracking is based on native tracking. Before getting started, make sure that MTA Android SDK configuration and initialization process have been connected according to [Android SDK Connection Guide](https://cloud.tencent.com/document/product/549/12863).
### Initializing Hybrid Module
After calling the basic tracking API for initializing MTA in onCreate of Application or MainActivity, you need also to call the following APIs to initialize the Hybrid module. Developers can choose one of these initialization APIs depending on whether to use the same AppKey as that of the native App.

```java
/**
* Initialize the Hybrid module using configurations of native App such as appkey and channel by default.
* @param context Context object
*/
public static void init(Context context);

/**
* Initialize the Hybrid module using the specified appkey and channel information
* @param context Context object
* @param appkey The Appkey used by Hybrid tracking
* @param channel The channel used by Hybrid tracking
*/
public static void init(Context context, String appkey, String channel);
```
#### Example

```java
public class MyApp extends Application{
	public static Application application = null;
	@Override
	public void onCreate() {
		super.onCreate();
		// Other code

		// Initialize the Hybrid module using default Appkey
		StatHybridHandler.init(this);
	}
}
```
### Configuring WebView
Call the following method for initialization in a WebView component that requires Hybrid tracking.
#### Initializing WebSettings

```java
/**
* Initialize WebSettings
* @param webSettings The webSettings to be initialized
*/
public static void initWebSettings(WebSettings webSettings)
```
#### Example

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

### Configuring WebViewClient
Natiive interacts with H5 by using the method for blocking redirection of MTA-specific URL. Therefore, you must call the SDK API in the shouldOverrideUrlLoading method of WebViewClient for URL blocking.
```java
/**
* Block redirection of MTA-specific URL
* @param webView Current WebView
* @param url i Current URL
* Returned value. true: The URL is the one specific to MTA and needs to be processed; false: Other URLs and needs further processing
*/
public static boolean handleWebViewUrl(WebView webView, String url);
```
#### Example
```java
public class MyWebViewClient extends WebViewClient {
	@Override
	public boolean shouldOverrideUrlLoading(WebView view, String url) {
		// Keep it on the first line if possible
		if(StatHybridHandler.handleWebViewUrl(view, url)){
			return true;
		}		
		super.shouldOverrideUrlLoading(view, url);
		return true;
	}
}

// If it cannot be processed on the first line, process it as follows:
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
				// Processing logic for other URLs
			}
		}catch (UnsupportedEncodingException ex){
		}		
		return super.shouldOverrideUrlLoading(view, url);
	}
}

```

