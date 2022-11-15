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
