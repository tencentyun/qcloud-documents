
## 原理

SNI（Server Name Indication）是为了解决一个服务器使用多个域名和证书的 SSL/TLS 扩展。工作原理如下：
- 在连接到服务器建立 SSL 链接之前先发送要访问站点的域名（Hostname）。
- 服务器根据这个域名返回一个合适的证书。

上述过程中，当客户端使用 HTTPDNS 解析域名时，请求 URL 中的 host 会被替换成 HTTPDNS 解析出来的 IP，导致服务器获取到的域名为解析后的 IP，无法找到匹配的证书，只能返回默认的证书或者不返回，所以会出现 SSL/TLS 握手不成功的错误。

由于 iOS 上层网络库 NSURLConnection/NSURLSession 没有提供接口进行 SNI 字段的配置，因此可以考虑使用 NSURLProtocol 拦截网络请求，然后使用 CFHTTPMessageRef 创建 NSInputStream 实例进行 Socket 通信，并设置其 kCFStreamSSLPeerName 的值。

需要注意的是，使用 NSURLProtocol 拦截 NSURLSession 发起的 POST 请求时，HTTPBody 为空。解决方案有两个：
- 使用 NSURLConnection 发 POST 请求。
- 先将 HTTPBody 放入 HTTP Header field 中，然后在 NSURLProtocol 中再取出来。

## Demo 示例

在网络请求前注册 NSURLProtocol 子类，在示例的 SNIViewController.m 中。
```
// 注册拦截请求的 NSURLProtocol
[NSURLProtocol registerClass:[MSDKDnsHttpMessageTools class]];

// 需要设置 SNI 的 URL
NSString *originalUrl = @"your url";
NSURL *url = [NSURL URLWithString:originalUrl];
NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:url];
NSArray *result = [[MSDKDns sharedInstance] WGGetHostByName:url.host];
NSString *ip = nil;
if (result && result.count > 1) {
	if (![result[1] isEqualToString:@"0"]) {
		ip = result[1];
	} else {
		ip = result[0];
	}
}
// 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
if (ip) {
	NSRange hostFirstRange = [originalUrl rangeOfString:url.host];
	if (NSNotFound != hostFirstRange.location) {
		NSString *newUrl = [originalUrl stringByReplacingCharactersInRange:hostFirstRange withString:ip];
		request.URL = [NSURL URLWithString:newUrl];
		[request setValue:url.host forHTTPHeaderField:@"host"];
	}
}

// NSURLConnection 例子
self.connection = [[NSURLConnection alloc] initWithRequest:request delegate:self];
[self.connection start];

// NSURLSession 例子
NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
NSArray *protocolArray = @[ [MSDKDnsHttpMessageTools class] ];
configuration.protocolClasses = protocolArray;
NSURLSession *session = [NSURLSession sessionWithConfiguration:configuration delegate:self delegateQueue:[NSOperationQueue mainQueue]];
self.task = [session dataTaskWithRequest:request];
[self.task resume];

// 注*：使用 NSURLProtocol 拦截 NSURLSession 发起的 POST 请求时，HTTPBody 为空。
// 解决方案有两个：
// 1. 使用 NSURLConnection 发 POST 请求。
// 2. 先将 HTTPBody 放入 HTTP Header field 中，然后在 NSURLProtocol 中再取出来。
// 下面主要演示第二种解决方案
// NSString *postStr = [NSString stringWithFormat:@"param1=%@&param2=%@", @"val1", @"val2"];
// [_request addValue:postStr forHTTPHeaderField:@"originalBody"];
// _request.HTTPMethod = @"POST";
// NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
// NSArray *protocolArray = @[ [CFHttpMessageURLProtocol class] ];
// configuration.protocolClasses = protocolArray;
// NSURLSession *session = [NSURLSession sessionWithConfiguration:configuration delegate:self delegateQueue:[NSOperationQueue mainQueue]];
// NSURLSessionTask *task = [session dataTaskWithRequest:_request];
// [task resume];
```


## 使用说明
需调用以下接口设置需要拦截域名或无需拦截的域名：
```
#pragma mark - SNI 场景，仅调用一次即可，请勿多次调用
/**
 SNI 场景下设置需要拦截的域名列表
 建议使用该接口设置，仅拦截 SNI 场景下的域名，避免拦截其它场景下的域名

 @param hijackDomainArray 需要拦截的域名列表
 */
- (void) WGSetHijackDomainArray:(NSArray *)hijackDomainArray;

/**
 SNI 场景下设置不需要拦截的域名列表

 @param noHijackDomainArray 不需要拦截的域名列表
 */
 - (void) WGSetNoHijackDomainArray:(NSArray *)noHijackDomainArray;
```
- 如设置了需要拦截的域名列表，则仅会拦截处理该域名列表中的 HTTPS 请求，其他域名不做处理。
- 如设置了不需要拦截的域名列表，则不会拦截处理该域名列表中的 HTTPS 请求。



<dx-alert infotype="notice" title="">
建议使用 WGSetHijackDomainArray 仅拦截 SNI 场景下的域名，避免拦截其他场景下的域名。
</dx-alert>



