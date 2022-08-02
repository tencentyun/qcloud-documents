## HTTPDNS SDK 接入 HTTP 网络访问

将 HTTPDNS SDK 的域名解析能力接入到业务的 HTTP（HTTPS）网络访问流程中，总的来说可以分为以下两种方式：

- **方式1：替换 URL**
替换 URL 中的 Host 部分得到新的 URL，并使用新的 URL 进行网络访问。
  这种实现方案下，URL 丢掉了域名的信息，对于需要使用到域名信息的网络请求，需进行较多的兼容性工作。
- **方式2：替换 DNS**
将 HTTPDNS 的域名解析能力注入到网络访问流程中，替换掉原本网络访问流程中的 LocalDNS 来实现。
  - 这种实现方案下，不需要逐个对请求的 URL 进行修改，同时由于没有修改 URL，无需进行额外的兼容性工作，但需要业务侧使用的网络库支持 DNS 实现替换。
  - DNS 替换也可以通过 Hook 系统域名解析函数的方式来实现，但 HTTPDNS SDK 内部已经使用系统的域名解析函数，Hook 系统域名解析函数可能会造成递归调用直到栈溢出。

不同网络库具体的接入方式，可以参见对应的接入文档（当前目录下）及参考使用 Sample（HttpDnsSample 目录）。


## 替换 URL 接入方式兼容
如前文所述，对于需要使用到域名信息的网络请求（一般是多个域名映射到同一个 IP 的情况），需要进行额外兼容。以下从协议层面阐述具体的兼容方式，具体的实现方式需要视网络库的实现而定。

- **HTTP 兼容**
对于 HTTP 请求，需要通过指定报文头中的 Host 字段来告知服务器域名信息。Host 字段详细介绍参见 [Host](https://tools.ietf.org/html/rfc2616#page-128)。
- **HTTPS 兼容**[](id:HTTPS)
 - HTTPS 是基于 TLS 协议之上的 HTTP 协议的统称。对于 HTTPS 请求，同样需要设置 Host 字段。
 - 在 HTTPS 请求中，需要先进行 TLS 的握手。TLS 握手过程中，服务器会将自己的数字证书发给我们用于身份认证，因此，在 TLS 握手过程中，也需要告知服务器相关的域名信息。在 TLS 协议中，通过 SNI 扩展来指明域名信息。SNI 扩展的详细介绍参见 [Server Name Indication](https://tools.ietf.org/html/rfc6066#page-6)。


## 本地使用 HTTP 代理[](id:local)

<dx-alert infotype="explain" title="">
本地使用 HTTP 代理情况下，建议**不要使用 HTTPDNS** 进行域名解析。
</dx-alert>

以下区分两种接入方式并进行分析：

- **替换 URL 接入**
根据 HTTP/1.1 协议规定，在使用 HTTP 代理情况下，客户端侧将在请求行中带上完整的服务器地址信息。详细介绍可以参见 [origin-form](https://tools.ietf.org/html/rfc7230#page-42)。
这种情况下（本地使用了 HTTP 代理，业务侧使用替换 URL 方式接入了 HTTPDNS SDK，且已经正确设置了 Host 字段），HTTP 代理接收到的 HTTP 请求中会包含服务器的 IP 信息（请求行中）以及域名信息（Host 字段中），但具体 HTTP 代理会如何向真正的目标服务器发起 HTTP 请求，则取决于 HTTP 代理的实现，可能会直接丢掉我们设置的 Host 字段使得网络请求失败。
- **替换 DNS 实现**
以 OkHttp 网络库为例，在本地启用 HTTP 代理情况下，OkHttp 网络库不会对一个 HTTP 请求 URL 中的 Host 字段进行域名解析，而只会对设置的 HTTP 代理的 Host 进行域名解析。在这种情况下，启用 HTTPDNS 没有意义。

您可通过以下代码，**判断本地是否使用 HTTP 代理**：
```kotlin
val host = System.getProperty("http.proxyHost")
val port = System.getProperty("http.proxyPort")
if (null != host && null != port) {
    // 本地使用了 HTTP 代理
}
```

## 实践场景

### OkHttp
OkHttp 提供了 DNS 接口，用于向 OkHttp 注入 DNS 实现。得益于 OkHttp 的良好设计，使用 OkHttp 进行网络访问时，实现 DNS 接口即可接入 HTTPDNS 进行域名解析，在较复杂场景（HTTP/HTTPS/WebSocket + SNI）下也不需要做额外处理，侵入性极小。示例如下：


```Java
mOkHttpClient =
    new OkHttpClient.Builder()
        .dns(new Dns() {
            @NonNull
            @Override
            public List<InetAddress> lookup(String hostname) {
                Utils.checkNotNull(hostname, "hostname can not be null");
                String ips = MSDKDnsResolver.getInstance().getAddrByName(hostname);
                String[] ipArr = ips.split(";");
                if (0 == ipArr.length) {
                    return Collections.emptyList();
                }
                List<InetAddress> inetAddressList = new ArrayList<>(ipArr.length);
                for (String ip : ipArr) {
                    if ("0".equals(ip)) {
                        continue;
                    }
                    try {
                        InetAddress inetAddress = InetAddress.getByName(ip);
                        inetAddressList.add(inetAddress);
                    } catch (UnknownHostException ignored) {
                    }
                }
                return inetAddressList;
            }
        })
        .build();
```

<dx-alert infotype="notice" title="">
实现 DNS 接口，即表示所有经由当前 OkHttpClient 实例处理的网络请求都会经过 HTTPDNS。如果您只有少部分域名是需要通过 HTTPDNS 进行解析，建议您在调用 HTTPDNS 域名解析接口之前先进行过滤。
</dx-alert>


###  Retrofit + OkHttp
Retrofit 实际上是一个基于 OkHttp，对接口做了一层封装桥接的 lib。因此只需要仿 OkHttp 的接入方式，定制 Retrofit 中的 OkHttpClient，即可方便地接入 HTTPDNS。示例如下：

```Java
mRetrofit =
    new Retrofit.Builder()
        .client(mOkHttpClient)
        .baseUrl(baseUrl)
        .build();
```

### WebView

Android 系统提供了 API 以实现 WebView 中的网络请求拦截与自定义逻辑注入。我们可以通过该 API 拦截 WebView 的各类网络请求，截取 URL 请求的 HOST，调用 HTTPDNS 解析该 HOST，通过得到的 IP 组成新的 URL 来进行网络请求。示例如下：
<dx-alert infotype="notice" title="">
由于 shouldInterceptRequest(WebView view, WebResourceRequest request) 中 WebResourceRequest 没有提供请求 body 信息，所以只能成功拦截 get 请求，无法拦截 post 请求。
</dx-alert>


```Java
mWebView.setWebViewClient(new WebViewClient() {
    // API 21及之后使用此方法
    @SuppressLint("NewApi")
    @Override
    public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
        if (request != null && request.getUrl() != null && request.getMethod().equalsIgnoreCase("get")) {
            String scheme = request.getUrl().getScheme().trim();
            String url = request.getUrl().toString();
            Log.d(TAG, "url:" + url);
            // HTTPDNS 解析 css 文件的网络请求及图片请求
            if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
            && (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url .endsWith(".gif"))) {
                try {
                    URL oldUrl = new URL(url);
                    URLConnection connection = oldUrl.openConnection();
                    // 获取 HTTPDNS 域名解析结果
                    String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
                    String[] ipArr = ips.split(";");
                    if (2 == ipArr.length && !"0".equals(ipArr[0])) { // 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
                        String ip = ipArr[0];
                        String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
                        connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置 HTTP 请求头 Host 域名
                        connection.setRequestProperty("Host", oldUrl.getHost());
                    }
                    Log.d(TAG, "contentType:" + connection.getContentType());
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

    // API 11至 API20使用此方法
    public WebResourceResponse shouldInterceptRequest(WebView view, String url) {
        if (!TextUtils.isEmpty(url) && Uri.parse(url).getScheme() != null) {
            String scheme = Uri.parse(url).getScheme().trim();
            Log.d(TAG, "url:" + url);
            // HTTPDNS 解析 css 文件的网络请求及图片请求
            if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
            && (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url.endsWith(".gif"))) {
                try {
                    URL oldUrl = new URL(url);
                    URLConnection connection = oldUrl.openConnection();
                    // 获取 HTTPDNS 域名解析结果
                    String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
                    String[] ipArr = ips.split(";");
                    if (2 == ipArr.length && !"0".equals(ipArr[0])) { // 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
                        String ip = ipArr[0];
                        String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
                        connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置 HTTP 请求头 Host 域名
                        connection.setRequestProperty("Host", oldUrl.getHost());
                    }
                    Log.d(TAG, "contentType:" + connection.getContentType());
                    return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                }
            }
        }
        return null;
    }});
// 加载web资源
mWebView.loadUrl(targetUrl);
```

### HttpURLConnection

- HTTPS 证书校验示例如下：
```Java
 // 以域名为 www.qq.com，HTTPDNS 解析得到的 IP 为192.168.0.1为例
String url = "https://192.168.0.1/"; // 业务自己的请求连接
 HttpsURLConnection connection = (HttpsURLConnection) new URL(url).openConnection();
 connection.setRequestProperty("Host", "www.qq.com");
 connection.setHostnameVerifier(new HostnameVerifier() {
 	@Override
 	public boolean verify(String hostname, SSLSession session) {
 		return HttpsURLConnection.getDefaultHostnameVerifier().verify("www.qq.com", session);
 	}
 });
 connection.setConnectTimeout(mTimeOut); // 设置连接超时
 connection.setReadTimeout(mTimeOut); // 设置读流超时
 connection.connect();
```
- HTTPS + SNI 示例如下：
```Java
 // 以域名为 www.qq.com，HttpDNS 解析得到的 IP 为192.168.0.1为例
 String url = "https://192.168.0.1/"; // 用 HTTPDNS 解析得到的 IP 封装业务的请求 URL
 HttpsURLConnection sniConn = null;
 try {
 	sniConn = (HttpsURLConnection) new URL(url).openConnection();
 	// 设置HTTP请求头Host域
 	sniConn.setRequestProperty("Host", "www.qq.com");
 	sniConn.setConnectTimeout(3000);
 	sniConn.setReadTimeout(3000);
 	sniConn.setInstanceFollowRedirects(false);
 	// 定制SSLSocketFactory来带上请求域名 ***关键步骤
 	SniSSLSocketFactory sslSocketFactory = new SniSSLSocketFactory(sniConn);
 	sniConn.setSSLSocketFactory(sslSocketFactory);
 	// 验证主机名和服务器验证方案是否匹配
 	HostnameVerifier hostnameVerifier = new HostnameVerifier() {
 		@Override
 		public boolean verify(String hostname, SSLSession session) {
 			return HttpsURLConnection.getDefaultHostnameVerifier().verify("原解析的域名", session);
 		}
 	};
 	sniConn.setHostnameVerifier(hostnameVerifier);
 	...
 } catch (Exception e) {
 	Log.w(TAG, "Request failed", e);
 } finally {
 	if (sniConn != null) {
 		sniConn.disconnect();
 	}
 }

 class SniSSLSocketFactory extends SSLSocketFactory {
 
 	private HttpsURLConnection mConn;

 	public SniSSLSocketFactory(HttpsURLConnection conn) {
 		mConn = conn;
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
 		String realHost = mConn.getRequestProperty("Host");
 		if (realHost == null) {
 			realHost = host;
 		}
 		Log.i(TAG, "customized createSocket host is: " + realHost);
 		InetAddress address = socket.getInetAddress();
 		if (autoClose) {
 			socket.close();
 		}
 		SSLCertificateSocketFactory sslSocketFactory = (SSLCertificateSocketFactory) SSLCertificateSocketFactory.getDefault(0);
 		SSLSocket ssl = (SSLSocket) sslSocketFactory.createSocket(address, port);
 		ssl.setEnabledProtocols(ssl.getSupportedProtocols());
 		if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
 			Log.i(TAG, "Setting SNI hostname");
 			sslSocketFactory.setHostname(ssl, realHost);
 		} else {
 			Log.d(TAG, "No documented SNI support on Android < 4.2, trying with reflection");
 			try {
 				Method setHostnameMethod = ssl.getClass().getMethod("setHostname", String.class);
 				setHostnameMethod.invoke(ssl, realHost);
 			} catch (Exception e) {
 				Log.w(TAG, "SNI not useable", e);
 			}
 		}
 		// verify hostname and certificate
 		SSLSession session = ssl.getSession();
 		HostnameVerifier hostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();
 		if (!hostnameVerifier.verify(realHost, session)) {
 			throw new SSLPeerUnverifiedException("Cannot verify hostname: " + realHost);
 		}			
 		Log.i(TAG, "Established " + session.getProtocol() + " connection with " + session.getPeerHost() + " using " + session.getCipherSuite());
 		return ssl;
 	}
 }
```



### Unity
- 初始化 HTTPDNS 和灯塔接口。
<dx-alert infotype="notice" title="">
若已接入 msdk 或者单独接入了腾讯灯塔则不用初始化灯塔。
</dx-alert> 示例如下：
```C#
 private static AndroidJavaObject sHttpDnsObj;
 public static void Init() {
 	AndroidJavaClass unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
 	if (unityPlayerClass == null) {
 		return;
 	}	
 	AndroidJavaObject activityObj = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
 	if (activityObj == null) {
 		return;
 	}
 	AndroidJavaObject contextObj = activityObj.Call<AndroidJavaObject>("getApplicationContext");
 	// 初始化 HTTPDNS
 	AndroidJavaObject httpDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
 	if (httpDnsClass == null) {
 		return;
 	}
 	sHttpDnsObj = httpDnsClass.CallStatic<AndroidJavaObject>("getInstance");
 	if (sHttpDnsObj == null) {
 		return;
 	}
 	sHttpDnsObj.Call("init", contextObj, appkey, dnsid, dnskey, debug, timeout);
 }
```
- 调用 getAddrByName 接口解析域名。示例如下：
```C#
// 该操作建议在子线程中或使用 Coroutine 处理
// 注意在子线程中调用需要在调用前后做 AttachCurrentThread 和 DetachCurrentThread 处理 
public static string GetHttpDnsIP(string url) {
	string ip = string.Empty;
	AndroidJNI.AttachCurrentThread(); // 子线程中调用需要加上
	// 解析得到 IP 配置集合
	string ips = sHttpDnsObj.Call<string>("getAddrByName", url);
	AndroidJNI.DetachCurrentThread(); // 子线程中调用需要加上
	if (null != ips) {
		string[] ipArr = ips.Split(';');
        if (2 == ipArr.Length && !"0".Equals(ipArr[0]))
		ip = ipArr[0];
	}
	return ip;
}
```



	
	

