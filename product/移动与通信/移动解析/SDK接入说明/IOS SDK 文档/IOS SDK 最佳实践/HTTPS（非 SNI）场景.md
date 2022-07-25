
## 原理

在进行证书校验时，将 IP 替换成原来的域名，再进行证书验证。

## Demo 示例

### NSURLConnection 接口示例
```
#pragma mark - NSURLConnectionDelegate
- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust forDomain:(NSString *)domain {

	//创建证书校验策略
	NSMutableArray *policies = [NSMutableArray array];
	if (domain) {
		[policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
	} else {
		[policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
	}

	//绑定校验策略到服务端的证书上
	SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);

	//评估当前 serverTrust 是否可信任，
	//官方建议在 result = kSecTrustResultUnspecified 或 kSecTrustResultProceed 的情况下 serverTrust 可以被验证通过，
	//https://developer.apple.com/library/ios/technotes/tn2232/_index.html
	//关于 SecTrustResultType 的详细信息请参考 SecTrust.h    
	SecTrustResultType result;
	SecTrustEvaluate(serverTrust, &result);
	return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);
}

- (void)connection:(NSURLConnection *)connection willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge {
	if (!challenge) {
		return;
	}

	//URL 里面的 host 在使用 HTTPDNS 的情况下被设置成了 IP，此处从 HTTP Header 中获取真实域名
	NSString *host = [[self.request allHTTPHeaderFields] objectForKey:@"host"];
	if (!host) {
		host = self.request.URL.host;
	}

	//判断 challenge 的身份验证方法是否是 NSURLAuthenticationMethodServerTrust（HTTPS 模式下会进行该身份验证流程），
	//在没有配置身份验证方法的情况下进行默认的网络请求流程。
	if ([challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust]) {
		if ([self evaluateServerTrust:challenge.protectionSpace.serverTrust forDomain:host]) {        

			//验证完以后，需要构造一个 NSURLCredential 发送给发起方    
			NSURLCredential *credential = [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust];
			[[challenge sender] useCredential:credential forAuthenticationChallenge:challenge];
		} else {
			//验证失败，取消这次验证流程
			[[challenge sender] cancelAuthenticationChallenge:challenge];
		}
	} else {

		//对于其他验证方法直接进行处理流程
		[[challenge sender] continueWithoutCredentialForAuthenticationChallenge:challenge];
	}
}
```


### NSURLSession 接口示例
```
 #pragma mark - NSURLSessionDelegate
- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust forDomain:(NSString *)domain {

	//创建证书校验策略
	NSMutableArray *policies = [NSMutableArray array];
	if (domain) {
		[policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
	} else {
		[policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
	}

	//绑定校验策略到服务端的证书上
	SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);

	//评估当前 serverTrust 是否可信任，
	//官方建议在 result = kSecTrustResultUnspecified 或 kSecTrustResultProceed 的情况下 serverTrust 可以被验证通过，
	//https://developer.apple.com/library/ios/technotes/tn2232/_index.html
	//关于SecTrustResultType的详细信息请参考SecTrust.h    
	SecTrustResultType result;
	SecTrustEvaluate(serverTrust, &result);

	return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);
}

- (void)URLSession:(NSURLSession *)session task:(NSURLSessionTask *)task didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential * __nullable credential))completionHandler {
	if (!challenge) {
		return;
	}

	NSURLSessionAuthChallengeDisposition disposition = NSURLSessionAuthChallengePerformDefaultHandling;
	NSURLCredential *credential = nil;

	//获取原始域名信息
	NSString *host = [[self.request allHTTPHeaderFields] objectForKey:@"host"];
	if (!host) {
		host = self.request.URL.host;
	}
	if ([challenge.protectionSpace.authenticationMethod  isEqualToString:NSURLAuthenticationMethodServerTrust]) {
		if ([self evaluateServerTrust:challenge.protectionSpace.serverTrust forDomain:host]) {
			disposition = NSURLSessionAuthChallengeUseCredential;
			credential = [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust];
		} else {
			disposition = NSURLSessionAuthChallengePerformDefaultHandling;
		}
	} else {
		disposition = NSURLSessionAuthChallengePerformDefaultHandling;
	}

	// 对于其他的 challenges 直接使用默认的验证方案
	completionHandler(disposition,credential);
}
```

### Unity 的 WWW 接口示例
将 Unity 工程导为 Xcode 工程后，打开 Classes/Unity/**WWWConnection.mm** 文件，修改下述代码：
 ```
//const char* WWWDelegateClassName = "UnityWWWConnectionSelfSignedCertDelegate";
const char* WWWDelegateClassName = "UnityWWWConnectionDelegate";
```
调整为：
```
const char* WWWDelegateClassName = "UnityWWWConnectionSelfSignedCertDelegate";
//const char* WWWDelegateClassName = "UnityWWWConnectionDelegate";
```
