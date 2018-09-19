Hybrid tracking is based on native tracking. Before getting started, make sure that MTA iOS SDK has been connected according to [iOS SDK Connection Guide](https://cloud.tencent.com/document/product/549/12858).
1. Find the libmtahybrid.a static library and the MTAHybrid.h header file in the sdk/plugin/hybrid directory of the MTA iOS SDK package.
![](//mc.qcloudimg.com/static/img/4fd0feffa51b8e14c09ff12edbd71bc6/image.png)
2. Connect the static library file to the project.
![](//mc.qcloudimg.com/static/img/d0048063f43d22daa4a8c9c52f4f77f9/image.png)
3. Add code in the project (for specific example, please see demo).
3.1 **If UIwebview is used**
Add the following code to the delegate of UIwebview:
```objc
- (BOOL)webView:(UIWebView *)webView
	shouldStartLoadWithRequest:(NSURLRequest *)request
	navigationType:(UIWebViewNavigationType)navigationType {
	// Code to process MTA hybrid tracking request
	if ([MTAHybrid handleRequest:request
		fromWebView:webView]) {
		return NO;
	}

	// Original code
	return YES;
}
```
When the UIWebView is hidden or removed from the parent view, the calling method is:
```objc
+ (void)stopWebView:(UIWebView *)webView;
```
When the UIWebView is redisplayed or re-added to the parent view, the calling method is:
```objc
+ (void)restartWebView:(UIWebView *)webView;
```
3.2 **If WKwebview is used**
Add the following code to the navagationdelegate of WKwebview:
```objc
- (void)webView:(WKWebView *)webView
	decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction
	decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler {
	// Code to process MTA hybrid tracking request
	if ([MTAHybrid handleAction:navigationAction
		fromWKWebView:webView]) {
		decisionHandler(WKNavigationActionPolicyCancel);
		return;
	}

	// Original code
	decisionHandler(WKNavigationActionPolicyAllow);
}
```
When the WKWebView is hidden or removed from the parent view, the calling method is:

```objc
+ (void)stopWKWebView:(WKWebView *)wkWebView;
```
When the WKWebView is redisplayed or re-added to the parent view, the calling method is:

```objc
+ (void)restartWKWebView:(WKWebView *)wkWebView;
```

