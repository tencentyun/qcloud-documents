This document describes how to load elements in H5 page through HTTP_DNS

### Code for Android

#### Principle
Android native system provides a system API to block network requests and introduce custom logic in WebView. By blocking various network requests of WebView, we can acquire the host requested by URL, and resolve the host by calling HttpDNS. The returned IP can be used to form a new URL for requesting network address.

#### Implementation Method
```
WebSettings webSettings = mWebView.getSettings();
// Use default cache policy and cache if it does not expire
webSettings.setCacheMode(WebSettings.LOAD_DEFAULT);
// Load web page image resources
webSettings.setBlockNetworkImage(false);
// JavaScript is supported
webSettings.setJavaScriptEnabled(true);
// Zooming is supported
webSettings.setSupportZoom(true);
mWebView.setWebViewClient(new WebViewClient() {
// Use this method for API 21 and above
@SuppressLint("NewApi")
@Override
public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
if (request != null && request.getUrl() != null && request.getMethod().equalsIgnoreCase("get")) {
String scheme = request.getUrl().getScheme().trim();
String url = request.getUrl().toString();
Logger.d("url a: " + url);
// HttpDNS resolves the network request and image request of css file
if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url .endsWith(".jif"))) {
try {
URL oldUrl = new URL(url);
URLConnection connection = oldUrl.openConnection();
// Obtain the result of HttpDNS resolution of domain name
String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
if (ips != null) { // After you obtain the IP resolved through HttpDNS, replace URL and set HOST header
Logger.d("HttpDns ips are: " + ips + " for host: " + oldUrl.getHost());
String ip;
if (ips.contains(";")) {
ip = ips.substring(0, ips.indexOf(";"));
} else {
ip = ips;
}
String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
Logger.d("newUrl a is: " + newUrl);
connection = (HttpURLConnection) new URL(newUrl).openConnection(); // Set the host field of HTTP request header
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
// Use this method for API 11 through API 20
public WebResourceResponse shouldInterceptRequest(WebView view, String url) {
if (!TextUtils.isEmpty(url) && Uri.parse(url).getScheme() != null) {
String scheme = Uri.parse(url).getScheme().trim();
Logger.d("url b: " + url);
// HttpDNS resolves the network request and image request of css file
if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
&& (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url
.endsWith(".jif"))) {
try {
URL oldUrl = new URL(url);
URLConnection connection = oldUrl.openConnection();
// Obtain the result of HttpDNS resolution of domain name
String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
if (ips != null) {
// After you obtain the IP resolved through HttpDNS, replace URL and set HOST header
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
// Set the host field of HTTP request header
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
// Load web resources
mWebView.loadUrl(targetUrl);
}
```

### Code for iOS

#### Principle
Block network requests: Block network requests of webview using iOS native NSURLProtocol. Then, filter the requests by suffix of the request network URL. Acquire the domain name of the URL filtered out, and send a request for HTTP_DNS. Then, use the returned IP address to form the original file network request.

#### Implementation Method
Implement HttpDNS resolution in the abstract method startLoading of NSURLProtocol, and replace the domain name with IP for URLConnection

```
/**
 *  Execute the blocked request, implement HttpDNS resolution, and replace the domain name with IP for URLConnection
 */
- (void)startLoading
{
	  NSMutableURLRequest *newRequest;
    NSString *fileExtension = [[self.request URL] absoluteString];

	  //Implement domain name resolution for URL of png, jpg or css file, depending on specific business requirements
	  if ([fileExtension containsString:@".png"] || [fileExtension containsString:@".jpg"] || [fileExtension containsString:@".css"])
	  {
	      // Change the request header, sync/async request
	      newRequest = [[H5ContentURLProtocol convertToNewRequest:self.request isSynchronous:NO] mutableCopy];
	  } else {
	      newRequest = [self.request mutableCopy];
	  }

    [NSURLProtocol setProperty:@YES forKey:@"MyURLProtocolHandledKey" inRequest:newRequest];

	  self.connection = [NSURLConnection connectionWithRequest:newRequest delegate:self];
}
```

