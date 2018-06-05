##  概述
目前域名解析普遍存在域名劫持的情况，这给我们的运维和安全带来不少挑战，为解决这个问题，我们引入 HttpDNS 功能。为保证能获取 DNS，该功能共分为两个层级：HttpDNS、LocalDNS。HttpDNS 获取成功，直接返回 HttpDNS 的值；HttpDNS 获取失败时，则返回 LocalDNS 的值；若两种情况都获取失败，则返回空值。
您可以通过以下方式获取智营解析 Android SDK：
[从 Github 获取最新版本SDK >>](https://github.com/tencentyun/httpdns-android-sdk)

## 接入 
### 步骤 1：AndroidMainfest 配置
```
    <uses-permission android:name="android. permission. ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android. permission. ACCESS_WIFI_STATE" />
    <uses-permission android:name="android. permission. CHANGE_WIFI_STATE" />
    <uses-permission android:name="android. permission. READ_PHONE_STATE" />
    <uses-permission android:name="android. permission. INTERNET" />
    <! -- DNS接收网络切换广播 -->
    <receiver
        android:name="com.tencent.msdk.dns. HttpDnsCache$ConnectivityChangeReceiver"
        android: label="NetworkConnection" >
        <intent-filter>
            <action android:name= “android.net. conn. CONNECTIVITY_CHANGE" />
        </intent-filter>
</receiver>
```

### 步骤 2：接入 HttpDns 库
将`HttpDnsLibs\httpdns_xxxx.jar`库文件拷贝至工程 libs 相应的位置，将`HttpDnsLibs\dnsconfig.ini`配置文件拷贝到应用`Android\assets`目录下；
> **注意：**
拷贝`dnsconfig.ini`文件前，先修改此文件里的相关配置，但不要改变文件原有的编码格式。
具体修改方法如下：
> 
| 修改项 | 修改字段 | 修改方法 |
|---------|---------|---------|
| 外部厂商和内部厂商开关 | IS_COOPERATOR | true |
|外部厂商测试开关 | IS_COOPERATOR_TEST |测试环境填"true"，使用正式环境填"false"，正式上线时必须为”false” |
| 厂商上报 appID | COOPERATOR_APPID | 云官网注册获得 |
| HttpDns SDK 日志开关 | IS_DEBUG | true 为打开日志开关，false 为关闭开关 |
| 服务端分配的 ID | DNS_ID | 腾讯云官网注册获得 |
| 服务端分配的 KEY |DNS_KEY | 腾讯云官网注册获得 |

### 步骤 3：接入依赖库
> **注意：**
> 已经接入了腾讯灯塔 ( beacon) 组件的应用请忽略此步骤 。

将`HttpDnsLibs\ beacon_android_vxxxx.jar`灯塔库拷贝至游戏 libs 相应的位置。

### 步骤 4：HttpDns Java 接口调用
调用命令如下：
```
// 初始化灯塔：如果已经接入MSDK或者IMSDK或者单独接入了腾讯灯塔(Beacon)则不需再初始化该接口
try {
// ***注意：这里业务需要输入自己的灯塔AppKey
UserAction.setAppKey("0I000LT6GW1YGCP7");
UserAction.initUserAction(MainActivity.this);
} catch (Exception e) {
	Logger.e("init beacon error:" + e.getMessage());
}

/**
* 初始化HttpDns：如果接入了MSDK，需要初始化完MSDK后再初始化HttpDns
* @param Activity  传入当前Activity
*/
MSDKDnsResolver.getInstance(). init (MainActivity.this);

/**
* 设置OpenId，已接入MSDK业务直接传MSDK OpenId，其它业务传“NULL”
* 注意：该接口返回值是布尔型，在Unity或者Cocos下调用请注意处理返回类型
* @param String openId
*/
MSDKDnsResolver.getInstance().WGSetDnsOpenId("10000");


/**
* HttpDns同步解析接口，首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求，解析
* 完成返回最新解析结果，若解析失败返回空对象
* @param domain 域名(如www.qq.com)，注意：domain只能传入域名不能传入IP，返回结果需要做非空
* 判断
* @return 域名对应的解析IP结果集合
*/
	String ips = MSDKDnsResolver.getInstance(). getAddrByName(domain);
```

## 注意事项
- 建议调用 HttpDns 同步接口时最好在子线程调用 getAddrByName(domain) 接口。
- 如果客户端的业务已与 Host 绑定，例如绑定了 Host 的 HTTP 服务或 CDN 服务。那么在用 HTTPDNS 返回的 IP 替换掉 URL 中的域名以后，还需要指定下 HTTP 头的 Host 字段。
 - 以 URLConnection 为例： 
```
		URL oldUrl = new URL(url); 
        URLConnection connection = oldUrl.openConnection(); 
        // 获取HttpDns域名解析结果 
        String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost()); 
        if (ips != null) { // 通过HTTPDNS获取IP成功，进行URL替换和Host头设置 
            String ip; 
            if (ips.contains(";")) { 
                ip = ips.substring(0, ips.indexOf(";")); 
            } else { 
                ip = ips; 
            } 
            String newUrl = url.replaceFirst(oldUrl.getHost(), ip); 
            connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置HTTP请求头Host域名 
            connection.setRequestProperty("Host", oldUrl.getHost()); 
        } 
```
 - 以 curl 为例：
假设您要访问`www.qq.com`通过 HTTPDNS 解析出来的 IP 为 192.168.0.111，那么通过这个方式来调用即可： 
```
curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt.
```

## 实践场景
### Unity 接入说明
#### 1. 初始化 HttpDns 和灯塔接口。
> **注意：**
若已接入了腾讯灯塔则不需要初始化灯塔。

```
private static AndroidJavaObject m_dnsJo;
	private static AndroidJavaClass sGSDKPlatformClass;
	public static void Init() {
		AndroidJavaClass jc = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
		if (jc == null)
			return;
			
		AndroidJavaObject joactivety = jc.GetStatic<AndroidJavaObject>("currentActivity");
		if (joactivety == null)
			return;
		AndroidJavaObject context = joactivety.Call<AndroidJavaObject>("getApplicationContext");
		// 初始化HttpDns
		AndroidJavaObject joDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
		Debug.Log(" WGGetHostByName ===========" + joDnsClass);
		if (joDnsClass == null)
			return;
		m_dnsJo = joDnsClass.CallStatic<AndroidJavaObject>("getInstance");
			Debug.Log(" WGGetHostByName ===========" + m_dnsJo);
		if (m_dnsJo == null)
			return;
		m_dnsJo.Call("init", context);
	}
```

#### 2. 调用 HttpDns 接口解析域名。
```
// 该操作建议在子线程中处理
public static string GetHttpDnsIP( string strUrl ) {
		string strIp = string.Empty;
		// 解析得到IP配置集合
		strIp = m_dnsJo.Call<string>("getAddrByName", strUrl);
		Debug.Log( strIp );
		if( strIp != null )
		{
		    // 取第一个
			string[] strIps = strIp.Split(';');
			strIp = strIps[0];
		}
		return strIp;
	}
```
### H5 页面内元素 HTTP_DNS 加载
原理：
Android 原生系统提供了系统 API 以实现 WebView 中的网络请求拦截与自定义逻辑注入，我们可以通过上述拦截 WebView 的各类网络请求，截取 URL 请求的 host，然后调用 HttpDns 解析该 host，通过得到的 IP 组成新的 URL 来请求网络地址。
实现方法：
```
 WebSettings webSettings = mWebView.getSettings(); 
// 使用默认的缓存策略，cache没有过期就用cache 
webSettings.setCacheMode(WebSettings.LOAD_DEFAULT); 
// 加载网页图片资源 
webSettings.setBlockNetworkImage(false); 
// 支持JavaScript脚本 
webSettings.setJavaScriptEnabled(true); 
// 支持缩放 
webSettings.setSupportZoom(true); 
mWebView.setWebViewClient(new WebViewClient() { 
// API 21及之后使用此方法 
@SuppressLint("NewApi") 
@Override 
public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) { 
if (request != null && request.getUrl() != null && request.getMethod().equalsIgnoreCase("get")) { 
String scheme = request.getUrl().getScheme().trim(); 
String url = request.getUrl().toString(); 
Logger.d("url a: " + url); 
// HttpDns解析css文件的网络请求及图片请求 
if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https")) 
&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url 
.endsWith(".gif"))) { 
try { 
URL oldUrl = new URL(url); 
URLConnection connection = oldUrl.openConnection(); 
// 获取HttpDns域名解析结果 
String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost()); 
if (ips != null) { // 通过HTTPDNS获取IP成功，进行URL替换和HOST头设置 
Logger.d("HttpDns ips are: " + ips + " for host: " + oldUrl.getHost()); 
String ip; 
if (ips.contains(";")) { 
ip = ips.substring(0, ips.indexOf(";")); 
} else { 
ip = ips; 
} 
String newUrl = url.replaceFirst(oldUrl.getHost(), ip); 
Logger.d("newUrl a is: " + newUrl); 
connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置HTTP请求头Host域 
connection.setRequestProperty("Host", oldUrl.getHost()); 
} 
Logger.d("ContentType a: " + connection.getContentType()); 
return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream()); 
} catch (MalformedURLException e) { 
e.printStackTrace(); 
} catch (IOException e) { 
e.printStackTrace(); 
} 
} 
} 
return null; 
} 
// API 11至 API 20 使用此方法 
public WebResourceResponse shouldInterceptRequest(WebView view, String url) { 
if (!TextUtils.isEmpty(url) && Uri.parse(url).getScheme() != null) { 
String scheme = Uri.parse(url).getScheme().trim(); 
Logger.d("url b: " + url); 
// HttpDns解析css文件的网络请求及图片请求 
if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https")) 
&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url 
.endsWith(".gif"))) { 
try { 
URL oldUrl = new URL(url); 
URLConnection connection = oldUrl.openConnection(); 
// 获取HttpDns域名解析结果 
String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost()); 
if (ips != null) { 
// 通过HTTPDNS获取IP成功，进行URL替换和HOST头设置 
Logger.d("HttpDns ips are: " + ips + " for host: " + oldUrl.getHost()); 
String ip; 
if (ips.contains(";")) { 
ip = ips.substring(0, ips.indexOf(";")); 
} else { 
ip = ips; 
} 
String newUrl = url.replaceFirst(oldUrl.getHost(), ip); 
Logger.d("newUrl b is: " + newUrl); 
connection = (HttpURLConnection) new URL(newUrl).openConnection(); 
// 设置HTTP请求头Host域 
connection.setRequestProperty("Host", oldUrl.getHost()); 
} 
Logger.d("ContentType b: " + connection.getContentType()); 
return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream()); 
} catch (MalformedURLException e) { 
e.printStackTrace(); 
} catch (IOException e) { 
e.printStackTrace(); 
} 
} 
} 
return null; 
} 
}); 
// 加载Web资源 
mWebView.loadUrl(targetUrl); 
}
```
### OkHttp + HttpDns 场景
```
    // 方案仅做参考
    String url = "http://www.qq.com";
    Uri uri = Uri.parse(url);
    String ip = MSDKDnsResolver.getInstance().getAddrByName("www.qq.com"); // HttpDns解析域名
    if (ip != null) {
	    if (ip.contains(";")) {
	        ip = ip.substring(0, ip.indexOf(";"));
	}
    } else {
	    return;
    }
    String mURL = uri.toString().replaceFirst(uri.getHost(), ip);

    // OkHttp GET Method
    try {
	    String mGetURL = mURL; // 根据业务自己的服务器地址来封装
	    Request request = new Request.Builder().url(mGetURL).build();
	    OkHttpClient client = new OkHttpClient();
	    Response response = client.newCall(request).execute();
	    String mGetResult = response.body().string();
	    System.out.println("OkHttp Get Method result:" + mGetResult);
    } catch (Exception e) {
	    e.printStackTrace();
    }

    // OkHttp POST Method
    try {
        String mPostURL = mURL; // 根据业务自己的服务器地址来封装
	    MediaType mType = MediaType.parse("application/json; charset=utf-8");
	    // 封装请求参数，根据业务实际情况封装
	    JSONObject jsonData = new JSONObject();
	    jsonData.put("os", "Android");
	    jsonData.put("api_version", 23);
	    jsonData.put("version", "0.0.1");
	    ......
	    String data = jsonData.toString();
	    RequestBody body = RequestBody.create(mType, data);
	    Request request = new Request.Builder().url(mPostURL).post(body).build();
	    OkHttpClient client = new OkHttpClient();
	    Response response = client.newCall(request).execute();
	    String mPostResult = response.body().string();
	    System.out.println("OkHttp POST Method result:" + mPostResult);
    } catch (Exception e) {
	    e.printStackTrace();
    }
```

### HTTPS 场景
#### 普通 HTTPS 场景
```
  String url = "https://httpdns域名解析得到的IP/d?dn=&clientip=1&ttl=1&id=128"; // 业务自己的请求连接
	HttpsURLConnection connection = (HttpsURLConnection) new URL(url).openConnection();
	connection.setRequestProperty("Host", "原解析的域名");
	connection.setHostnameVerifier(new HostnameVerifier() {
	@Override
	public boolean verify(String hostname, SSLSession session) {
		return HttpsURLConnection.getDefaultHostnameVerifier().verify("原解析的域名", session);
	}
	});
	connection.setConnectTimeout(mTimeOut); // 设置连接超时
	connection.setReadTimeout(mTimeOut); // 设置读流超时
	connection.connect();
```

#### HTTPS SNI（单 IP 多 HTTPS 证书）场景
```
	 String url = "https://" + ip + "/pghead/xxxxxxx/140"; // 用HttpDns解析得到的IP封装业务的请求URL
		HttpsURLConnection sniConn = null;
		try {
			sniConn = (HttpsURLConnection) new URL(url).openConnection();
			// 设置HTTP请求头Host域
			sniConn.setRequestProperty("Host", "原解析的域名");
			sniConn.setConnectTimeout(3000);
			sniConn.setReadTimeout(3000);
			sniConn.setInstanceFollowRedirects(false);
			// 定制SSLSocketFactory来带上请求域名 ***关键步骤
			SniSSLSocketFactory sslSocketFactory = new SniSSLSocketFactory(sniConn);
			sniConn.setSSLSocketFactory(sslSocketFactory);
			// 验证主机名和服务器验证方案是否匹配？
			HostnameVerifier hostnameVerifier = new HostnameVerifier() {
				@Override
				public boolean verify(String hostname, SSLSession session) {
					return HttpsURLConnection.getDefaultHostnameVerifier().verify("原解析的域名", session);
				}
			};
			sniConn.setHostnameVerifier(hostnameVerifier);
			int code = sniConn.getResponseCode();// Network block
			if (code >= 300 && code < 400) {
				// 临时重定向和永久重定向location的大小写有区分
				String location = sniConn.getHeaderField("Location");
				if (location == null) {
					location = sniConn.getHeaderField("location");
				}
				if (!(location.startsWith("http://") || location.startsWith("https://"))) {
					URL originalUrl = new URL(url);
					location = originalUrl.getProtocol() + "://" + "原解析的域名" + location;
				}
				showSniHttpsDemo(location, "原解析的域名");
			} else {
				// 业务自己处理服务端响应结果
				DataInputStream dis = new DataInputStream(sniConn.getInputStream());
				int len;
				byte[] buff = new byte[4096];
				StringBuilder response = new StringBuilder();
				while ((len = dis.read(buff)) != -1) {
					response.append(new String(buff, 0, len));
				}
				dis.close();
				Log.d("WGGetHostByName", "response: " + response.toString());
			}
		} catch (Exception e) {
			Log.w("WGGetHostByName", e.getMessage());
		} finally {
			if (sniConn != null) {
				sniConn.disconnect();
			}
		}
		
定制SSLSocketFactory：
    class SniSSLSocketFactory extends SSLSocketFactory {
	private HttpsURLConnection conn;

	public SniSSLSocketFactory(HttpsURLConnection conn) {
		this.conn = conn;
	}

	@Override
	public Socket createSocket() throws IOException {
		return null;
	}

	@Override
	public Socket createSocket(String host, int port) throws IOException, UnknownHostException {
		return null;
	}

	@Override
	public Socket createSocket(String host, int port, InetAddress localHost, int localPort) throws IOException, UnknownHostException {
		return null;
	}

	@Override
	public Socket createSocket(InetAddress host, int port) throws IOException {
		return null;
	}

	@Override
	public Socket createSocket(InetAddress address, int port, InetAddress localAddress, int localPort) throws IOException {
		return null;
	}

	@Override
	public String[] getDefaultCipherSuites() {
		return new String[0];
	}

	@Override
	public String[] getSupportedCipherSuites() {
		return new String[0];
	}

	@Override
	public Socket createSocket(Socket socket, String host, int port, boolean autoClose) throws IOException {
		String mHost = this.conn.getRequestProperty("Host");
		if (mHost == null) {
			mHost = host;
		}
		Log.i("WGGetHostByName", "customized createSocket host is: " + mHost);
		InetAddress address = socket.getInetAddress();
		if (autoClose) {
			socket.close();
		}
		SSLCertificateSocketFactory sslSocketFactory = (SSLCertificateSocketFactory) SSLCertificateSocketFactory.getDefault(0);
		SSLSocket ssl = (SSLSocket) sslSocketFactory.createSocket(address, port);
		ssl.setEnabledProtocols(ssl.getSupportedProtocols());

		if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
			Log.i("WGGetHostByName", "Setting SNI hostname");
			sslSocketFactory.setHostname(ssl, mHost);
		} else {
			Log.d("WGGetHostByName", "No documented SNI support on Android <4.2, trying with reflection");
			try {
				java.lang.reflect.Method setHostnameMethod = ssl.getClass().getMethod("setHostname", String.class);
				setHostnameMethod.invoke(ssl, mHost);
			} catch (Exception e) {
				Log.w("WGGetHostByName", "SNI not useable", e);
			}
		}
		// verify hostname and certificate
		SSLSession session = ssl.getSession();
		HostnameVerifier mHostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();
		if (!mHostnameVerifier.verify(mHost, session))
			throw new SSLPeerUnverifiedException("Cannot verify hostname: " + mHost);
		Log.i("WGGetHostByName",
				"Established " + session.getProtocol() + " connection with " + session.getPeerHost() + " using " + session.getCipherSuite());
		return ssl;
	}
    }

```

### 代理使用场景
请检测本地是否使用了 HTTP 代理，如果使用了 HTTP 代理，建议不要使用 HTTPDNS 做域名解析。

```
    String host = System.getProperty("http.proxyHost");
    String port= System.getProperty("http.proxyPort");
    if (host != null && port != null) {
	    // 使用了本地代理模式
	}
```
