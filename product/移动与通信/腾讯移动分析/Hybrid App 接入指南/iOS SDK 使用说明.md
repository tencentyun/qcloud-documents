Hybrid 统计是在原生统计基础上进行的，在开始之前请确保已按照 [iOS SDK 接入指南](https://cloud.tencent.com/document/product/549/12858) 正常接入 MTA iOS SDK 。
1.在 MTA iOS SDK 包中的 sdk/plugin/hybrid 目录下找到 libmtahybrid.a  静态库和 MTAHybrid.h 头文件；
![](//mc.qcloudimg.com/static/img/4fd0feffa51b8e14c09ff12edbd71bc6/image.png)
2.将静态库文件连接至工程中；
![](//mc.qcloudimg.com/static/img/d0048063f43d22daa4a8c9c52f4f77f9/image.png)
3.在工程中添加代码（具体例子可以参考 demo）。
3.1 **如果使用的是 UIwebview**
在 UIwebview 的 delegate 中添加以下代码：
```objc
- (BOOL)webView:(UIWebView *)webView
	shouldStartLoadWithRequest:(NSURLRequest *)request
	navigationType:(UIWebViewNavigationType)navigationType {
	// 处理MTA混合统计请求的代码
	if ([MTAHybrid handleRequest:request
		fromWebView:webView]) {
		return NO;
	}

	// 原有的代码
	return YES;
}
```
在 UIWebView 被隐藏或者从父 view 移除时 ，调用方法为：
```objc
+ (void)stopWebView:(UIWebView *)webView;
```
在 UIWebView 重新被显示，或者重新被添加到父 view 上时，调用方法为：
```objc
+ (void)restartWebView:(UIWebView *)webView;
```
3.2 **如果使用的是 WKwebview**
在 WKwebview 的 navagationdelegate 中添加以下代码：
```objc
- (void)webView:(WKWebView *)webView
	decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction
	decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler {
	// 处理MTA混合统计请求的代码
	if ([MTAHybrid handleAction:navigationAction
		fromWKWebView:webView]) {
		decisionHandler(WKNavigationActionPolicyCancel);
		return;
	}

	// 原有的代码
	decisionHandler(WKNavigationActionPolicyAllow);
}
```
在 WKWebView 被隐藏或者从父 view 移除时，调用方法为：

```objc
+ (void)stopWKWebView:(WKWebView *)wkWebView;
```
在 WKWebView 重新被显示，或者重新被添加到父 view 上时，调用方法为：

```objc
+ (void)restartWKWebView:(WKWebView *)wkWebView;
```
