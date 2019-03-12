##  概述

目前域名解析普遍存在域名劫持的情况，这给我们的运维和安全带来不少挑战，为解决这个问题，我们引入 HttpDNS 功能。为保证能获取 DNS，该功能共分为两个层级：HttpDNS、LocalDNS。HttpDNS 获取成功，直接返回 HttpDNS 的值；HttpDNS 获取失败时，则返回 LocalDNS 的值；若两种情况都获取失败，则返回空值。

您可以通过以下方式获取智营解析 Android SDK：
[从 Github 获取最新版本 SDK >>](https://github.com/tencentyun/httpdns-android-sdk)

## GitHub 目录结构说明

| 目录名称       | 说明           | 适用范围  |
| ------------- |-------------| -------------|
| HttpDnsLibs | HttpDns Android SDK 库目录 | 所有业务 |
| HttpDns Android客户端接入文档（腾讯内部业务专用）.pdf | HttpDns Android 客户端接入文档（腾讯内部业务专用） | 腾讯内部业务 |
| HttpDns Android客户端接入文档（腾讯云客户专用）.pdf | HttpDns Android 客户端接入文档（腾讯云客户专用） | 腾讯云客户 |
| README.md | HttpDns Android 客户端接入文档 | 腾讯云客户 |
| VERSION.md | HttpDns Android SDK 历史版本修改记录 | SDK 开发维护人员 |
| 数据报表申请方法.pdf | 数据报表申请方法 | SDK 开发维护人员 |

## 功能介绍

由于运营商传统 LocalDns 解析导致的无法访问最佳接入点，提出了 HttpDns 解决方案。其原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。


## 接入

### AndroidMainfest 配置

```xml
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />

<!-- 灯塔 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

### 接入 HttpDns

将 HttpDnsLibs\HttpDns_xxxx.jar 拷贝至应用 libs 相应位置。

### 接入灯塔

将 HttpDnsLibs\beacon_android_xxxx.jar 拷贝至应用 libs 相应位置。
>! 已经接入了腾讯灯塔(beacon)组件的应用忽略此步

### 接口调用

```
// 初始化灯塔：如果已经接入MSDK或者IMSDK或者单独接入了腾讯灯塔(Beacon)则不需再初始化该接口
try {
    // 注意：这里业务需要输入自己的灯塔appkey
    UserAction.setAppKey("0I000LT6GW1YGCP7");
    UserAction.initUserAction(MainActivity.this.getApplicationContext());
} catch (Exception e) {
    Log.e(TAG, "Init beacon failed", e);
}

/**
 * 初始化HttpDns：如果接入了MSDK，建议初始化MSDK后再初始化HttpDns
 * 
 * @param context 应用上下文，最好传入ApplicationContext
 * @param appkey 业务appkey，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权ID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权ID对应的key(加密密钥),腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param debug 是否开启debug日志，true为打开，false为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, debug, timeout); 
	
/**
 * 设置OpenId，已接入MSDK业务直接传MSDK OpenId，其它业务传“NULL”
 * 
 * @param String openId
 */
MSDKDnsResolver.getInstance().WGSetDnsOpenId("10000");

/**
 * HttpDns同步解析接口
 * 注意：domain只能传入域名不能传入IP
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成返回最新解析结果，解析结果有多个IP则以“;”分隔
 * 
 * @param domain 域名(如www.qq.com)
 * @return 域名对应的解析IP结果集合
 */
String ips = MSDKDnsResolver.getInstance().getAddrByName(domain);
```

### 接入验证

将 init 接口中的 debug 参数传入 true，过滤 TAG 为 “WGGetHostByName” 的日志。若查看到 LocalDns（日志上为  ldns_ip）和 HttpDns（日志上为 hdns_ip）相关日志，则可以确认接入无误。

### 注意事项

- getAddrByName 是耗时同步接口，须在子线程调用。
- 如果客户端的业务与 host 绑定，例如绑定了 host 的 HTTP 服务或者是 CDN 的服务，那么在用 HttpDns 返回的 IP 替换掉 URL 中的域名后，还需要指定 HTTP 头的 host 字段。
	- 以 URLConnection 为例：
```
		URL oldUrl = new URL(url); 
    	URLConnection connection = oldUrl.openConnection(); 
		// 获取HttpDns域名解析结果 
		String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
		if (null != ips) { // 通过HTTPDNS获取IP成功，进行URL替换和Host头设置 
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
	假设您要访问 `www.qq.com`，通过 HttpDns 解析得到的 IP 为192.168.0.111，那么您可以通过以下方式访问。
	`curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt`
- 检测本地是否使用了 HTTP 代理，如果使用了 HTTP 代理，建议**不要使用** HttpDns 做域名解析。
	示例如下：
```
	String host = System.getProperty("http.proxyHost");
	String port= System.getProperty("http.proxyPort");
	if (null != host && null != port) {
		// 使用了本地代理模式
	}
```

## 实践场景

### OkHttp

OkHttp 提供了 DNS 接口，用于向 OkHttp 注入 DNS 实现。得益于 OkHttp 的良好设计，使用 OkHttp 进行网络访问时，实现 DNS 接口即可接入 HttpDns 进行域名解析，在较复杂场景（HTTP/HTTPS + SNI）下也不需要做额外处理，侵入性极小。
示例如下：
```
mOkHttpClient =
    new OkHttpClient.Builder()
        .dns(new Dns() {
            @NonNull
            @Override
            public List<InetAddress> lookup(String hostname) {
                Utils.checkNotNull(hostname, "hostname can not be null");
                // HttpDns是对HttpDns接口处理的简单封装类
                String ip = HttpDns.getAddrByName(hostname);
                if (null == ip) {
                    return Collections.emptyList();
                }
                try {
                    InetAddress inetAddress = InetAddress.getByName(ip);
                    List<InetAddress> inetAddressList = new ArrayList<>();
                    inetAddressList.add(inetAddress);
                    return inetAddressList;
                } catch (UnknownHostException e) {
                    Log.d(TAG, "lookup failed", e);
                    return Collections.emptyList();
                }
            }
        })
        .build();
```

>! 实现 DNS 接口，即表示所有经由当前 OkHttpClient 实例处理的网络请求都会经过 HttpDns。如果业务只有少部分域名是需要通过 HttpDns 进行解析的，建议您在调用 HttpDns 域名解析接口之前先进行过滤。

### Retrofit + OkHttp

Retrofit 实际上是一个基于 OkHttp，对接口做了一层封装桥接的 lib。因此，您只需要仿 OkHttp 的接入方式，定制 Retrofit 中的 OkHttpClient，即可方便地接入 HttpDns。
示例如下：
```
mRetrofit =
	new Retrofit.Builder()
		.client(mOkHttpClient)
		.baseUrl(baseUrl)
		.build();
```

### WebView

Android 系统提供了 API 以实现 WebView 中的网络请求拦截与自定义逻辑注入。首先，我们通过该 API 拦截 WebView 的各类网络请求，截取 URL 请求的 host；其次，调用 HttpDns 解析该 host，通过得到的 IP 组成新的 URL 来进行网络请求。
```
mWebView.setWebViewClient(new WebViewClient() { 
	// API 21及之后使用此方法 
	@SuppressLint("NewApi") 
	@Override 
	public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) { 
		if (request != null && request.getUrl() != null && request.getMethod().equalsIgnoreCase("get")) { 
			String scheme = request.getUrl().getScheme().trim(); 
			String url = request.getUrl().toString(); 
			Log.d(TAG, "url:" + url); 
			// HttpDns解析css文件的网络请求及图片请求 
			if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https")) 
			&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url .endsWith(".gif"))) { 
				try { 
					URL oldUrl = new URL(url); 
					URLConnection connection = oldUrl.openConnection(); 
					// 获取HttpDns域名解析结果 
					String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
					if (null != ips) { // 通过HTTPDNS获取IP成功，进行URL替换和HOST头设置 
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

	// API 11至API20使用此方法 
	public WebResourceResponse shouldInterceptRequest(WebView view, String url) { 
		if (!TextUtils.isEmpty(url) && Uri.parse(url).getScheme() != null) { 
			String scheme = Uri.parse(url).getScheme().trim(); 
			Log.d(TAG, "url:" + url); 
			// HttpDns解析css文件的网络请求及图片请求 
			if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https")) 
	&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url.endsWith(".gif"))) { 
				try { 
					URL oldUrl = new URL(url); 
					URLConnection connection = oldUrl.openConnection();
					// 获取HttpDns域名解析结果
					String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
					if (null != ips) { // 通过HTTPDNS获取IP成功，进行URL替换和HOST头设置
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
	}}); 
// 加载web资源 
mWebView.loadUrl(targetUrl); 
```

### HttpURLConnection

- HTTPS
	示例如下：
```
	// 以域名为www.qq.com，HttpDns解析得到的IP为192.168.0.1为例
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
- HTTPS + SNI
	示例如下：
```
	// 以域名为www.qq.com，HttpDns解析得到的IP为192.168.0.1为例
	String url = "https://192.168.0.1/"; // 用HttpDns解析得到的IP封装业务的请求URL
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

### HttpClient

HttpClient 接入 HttpDns 方式和 HttpURLConnection 类似，但涉及 HTTPS 情况则有所不同。以下以 HTTPS + SNI 场景为例（示例也适用于 HTTPS 场景）：
```
@Nullable
private HttpClient mHttpClient = null;

{
    try {
        KeyStore trustStore = KeyStore.getInstance(KeyStore.getDefaultType());
        trustStore.load(null, null);
        SchemeRegistry schemeRegistry = new SchemeRegistry();
        schemeRegistry.register(new Scheme("http", PlainSocketFactory.getSocketFactory(), 80));
        schemeRegistry.register(new Scheme("https", new SniSSLSocketFactory(trustStore), 443));
        HttpParams httpParams = new BasicHttpParams();
        mHttpClient = new DefaultHttpClient(new ThreadSafeClientConnManager(httpParams, schemeRegistry), httpParams);
    } catch (Exception e) {
        Log.d(TAG, "set HttpClient failed", e);
    }
}

private static final class SniSSLSocketFactory extends SSLSocketFactory {

    private SSLContext mSSLContext;

    {
        try {
            mSSLContext = SSLContext.getInstance("TLS");
            mSSLContext.init(null, new TrustManager[] {
                new X509TrustManager() {
                    @Override
                    public void checkClientTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
                    }

                    @Override
                    public void checkServerTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
                    }

                    @Override
                    public X509Certificate[] getAcceptedIssuers() {
                        return null;
                    }
                }
            }, null);
        } catch (NoSuchAlgorithmException e) {
            // might never reach
            Log.d(TAG, "get SSLContext failed", e);
            mSSLContext = null;
        }
    }

    public SniSSLSocketFactory(KeyStore truststore) throws NoSuchAlgorithmException, KeyManagementException, KeyStoreException, UnrecoverableKeyException {
        super(truststore);
    }

    @Override
    public Socket createSocket(Socket socket, String host, int port, boolean autoClose) throws IOException, UnknownHostException {
        if (null == mSSLContext) {
            // might never reach
            Log.d(TAG, "null == mSSLContext");
            return socket;
        }
        Log.i(TAG, "host:" + host);
        // HttpDns是对HttpDns接口处理的简单封装类
        String ip = HttpDns.getAddrByName(host);
        if (null == ip) {
            Log.d(TAG, "null == ip");
            throw new UnknownHostException(host);
        }
        Log.d(TAG, "ip:" + ip);
        InetAddress inetAddress = InetAddress.getByName(ip);
        if (autoClose) {
            socket.close();
        }
        javax.net.ssl.SSLSocketFactory sslSocketFactory = mSSLContext.getSocketFactory();
        SSLSocket sslSocket = (SSLSocket) sslSocketFactory.createSocket(inetAddress, port);
        sslSocket.setEnabledProtocols(sslSocket.getSupportedProtocols());
        try {
            Method setHostnameMethod = sslSocket.getClass().getMethod("setHostname", String.class);
            setHostnameMethod.invoke(sslSocket, host);
        } catch (Exception e) {
            Log.w(TAG, "set sni failed", e);
        }
        return sslSocket;
    }
}
```

### Unity

- 初始化 HttpDns 和灯塔接口
	>! 若已接入 MSDK 或者单独接入了腾讯灯塔则不用初始化灯塔。
	>
	示例如下：
	```
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
		// 初始化HttpDns
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
- 调用 getAddrByName 接口解析域名
	示例如下：
```
	// 该操作建议在子线程中或使用Coroutine处理
	// 注意在子线程中调用需要在调用前后做AttachCurrentThread和DetachCurrentThread处理 
	public static string GetHttpDnsIP(string strUrl) {
		string strIp = string.Empty;
		AndroidJNI.AttachCurrentThread(); // 子线程中调用需要加上
		// 解析得到IP配置集合
		strIp = sHttpDnsObj.Call<string>("getAddrByName", strUrl);
		AndroidJNI.DetachCurrentThread(); // 子线程中调用需要加上
		if (null != strIp) {
			string[] strIps = strIp.Split(';');
			strIp = strIps[0];
		}
		return strIp;
	}
```
