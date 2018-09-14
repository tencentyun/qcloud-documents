## 功能介绍
HttpDns 的主要功能是为了有效的避免由于运营商传统 LocalDns 解析导致的无法访问最佳接入点的方案。原理是为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。
您可以通过以下方式获取智营解析 iOS SDK：
[从 Github 获取最新版本 SDK >>](https://github.com/tencentyun/httpdns-ios-sdk)

## 安装包结构
压缩文件中包含 demo 工程，其中包含：
- `MSDKDns.framework`适用 “Build Setting->C++ Language Dialect” 配置为 GNU++98，“Build Setting->C++ Standard Library” 为 “libstdc++ (GNU C++ standard library)” 的工程。
- `MSDKDns_C11.framework`适用于该两项配置分别为 “GNU++11” 和 “libc++ (LLVM C++ standard library with C++11 support)” 的工程。

## 接入步骤
### 步骤 1： 引入依赖库
**已接入灯塔（Beacon）的业务**
仅需引入位于 HTTPDNSLibs 目录下的 `MSDKDns.framework`（或  `MSDKDns_C11.framework`，根据工程配置选其一）即可。

**未接入灯塔（Beacon）的业务**
- 引入依赖库（位于 HTTPDNSLibs 目录下）：
  - BeaconAPI_Base.framework
  - MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）
- 引入系统库：
  - libz.tdb
  - libsqlite3.tdb
  - libstdc++.tdb
  - libstdc++.6.0.9.tdb
  - libc++.tdb
  - Foundation.framework
  - CoreTelephony.framework
  - SystemConfiguration.framework
  - CoreGraphics.framework
  - Security.framework
- 并在`application:didFinishLaunchingWithOptions:`加入注册灯塔代码：
```
//已正常接入灯塔的业务无需关注以下代码，未接入灯塔的业务调用以下代码注册灯塔
//******************************
NSString *plistPath = [[NSBundle mainBundle] pathForResource:@"Info" ofType:@"plist"];
NSDictionary *dic = [NSDictionary dictionaryWithContentsOfFile:plistPath];
NSString *appid = dic[@"COOPERATOR_APPID"];
[BeaconBaseInterface setAppKey:appid];
[BeaconBaseInterface enableAnalytics:@"" gatewayIP:nil];
 //******************************
```

> **注意：**
> 需要在 Other linker flag 里加入 -ObjC 标志。

### 步骤 2： 配置文件
在` info.plist `中进行配置如下：

| Key | Type | Value |
|---------|---------|---------|
| IS_COOPERATOR | Boolean | YES |
| COOPERATOR_APPID | String | 接入时由系统或者管理员分配 |
| TIME_OUT | Number | 请求 HttpDns 的超时设定时间单位：ms ; 如未设置，默认为 1000 ms |
| DNS_ID |String | 接入时由系统或者管理员分配 |
| DNS_KEY | String | 接入时由系统或者管理员分配 |
| Debug | Boolean | 日志开关配置：YES 为打开 HttpDns 日志；No 为关闭 HttpDns 日志 |

## API 及使用示例
获取 IP 共有两个接口：**同步接口 WGGetHostByName** 和 **异步接口 WGGetHostByNameAsync**。引入头文件，调用相应接口即可。返回的地址格式为 NSArray，固定长度为 2。其中第一个值为 IPv4 地址，第二个值为 IPv6 地址。
返回格式的详细说明如下：
- [IPv4, 0]：一般业务使用的情景中，绝大部分均会返回这种格式的结果，即不存在 IPv6 地址，仅返回 IPv4 地址给业务；

- [IPv4, IPv6]：发生在 IPv6 环境下，IPv6 及 IPv4 地址均会返回给业务；

- [0, 0]：在极其少数的情况下，会返回该格式给业务，此时 HttpDNS 与 LocalDNS 请求均超时，业务重新调用 WGGetHostByName 接口即可。

> **注意：**
> 使用 IPv6 地址进行 URL 请求时，需加方框号 [ ] 进行处理，例如：
```
http://[64:ff9b::b6fe:7475]/*********
```
>**使用建议：**
1. IPv6 为 0，直接使用 IPv4 地址连接；
2. IPv6 地址不为 0，优先使用 IPv6 连接，如果 IPv6 连接失败，再使用 IPv4 地址进行连接。

### 获取 IP
#### 同步接口 WGGetHostByName
```
/**
*  同步接口
*  @param domain 域名
*  @return 查询到的 IP 数组，超时（1s）或者未未查询到返回[0,0]数组
*/
- (NSArray*) WGGetHostByName:(NSString*) domain;
```

**接口调用示例代码：**

```
NSArray* ipsArray = [[MSDKDns sharedInstance] WGGetHostByName: @"www.qq.com"];
if (ipsArray && ipsArray.count > 1){
NSString* ipv4 = ipsArray[0];
NSString* ipv6 = ipsArray[1];
if (![ipv6 isEqualToString:@"0"]) {
//使用建议：当 IPv6 地址存在时，优先使用 IPv6 地址
//TODO 使用 IPv6 地址进行连接，注意格式，IPv6 需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
} else if (![ipv4 isEqualToString:@"0"]) {
//使用 IPv4 地址进行连接
} else {
//异常情况返回为 0,0 建议重试一次
} 
}
```

#### 异步接口 WGGetHostByNameAsync
```
/**
*  异步接口
*  @param domain 域名
*  @return 查询到的IP数组，超时（1s）或者未未查询到返回[0,0]数组
*/
- (void) WGGetHostByNameAsync:(NSString*) domain returnIps:(void (^)(NSArray* ipsArray))handler;
```

**示例代码：**
- 接口调用示例 1：等待完整解析过程结束后，拿到结果，进行连接操作。
```
[[MSDKDns sharedInstance] WGGetHostByNameAsync:domain returnIps:^(NSArray *ipsArray) {
if (ipsArray && ipsArray.count > 1) {
NSString* ipv4 = ipsArray[0];
NSString* ipv6 = ipsArray[1];
if (![ipv6 isEqualToString:@"0"]) {
//使用建议：当 IPv6 地址存在时，优先使用 IPv6 地址
//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，IPv6 需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
} else if (![ipv4 isEqualToString:@"0"]){
//使用 IPv4 地址进行连接
} else {
//异常情况返回为 0,0 建议重试一次
}
	}
}];
```

- 接口调用示例 2：无需等待，可直接拿到缓存结果，如无缓存，则 result 为 nil。
```
__block NSArray* result;
[[MSDKDns sharedInstance] WGGetHostByNameAsync:domain returnIps:^(NSArray *ipsArray) {
result = ipsArray;
}];
//无需等待，可直接拿到缓存结果，如无缓存，则 result 为 nil
if (result) {
//拿到缓存结果，进行连接操作
} else {
//本次请求无缓存，业务可走原始逻辑
}
```

您可根据自身业务需求，任选一种调用方式：
示例 1：
 - 优点：可保证每次请求都能拿到返回结果进行接下来的连接操作；
 - 缺点：异步接口的处理较同步接口稍显复杂。

示例 2：
- 优点：对于解析时间有严格要求的业务，使用本示例，无需等待，可直接拿到缓存结果进行后续的连接操作，完全避免了同步接口中解析耗时可能会超过 100 ms 的情况；
- 缺点：第一次请求时，result 一定会 nil，需业务增加处理逻辑。

###  控制台日志
用户可以通过 **WGOpenMSDKDnsLog 接口** 控制是否打印 HttpDns 相关的 Log。
```
	/**
	 *  Log开关
	 *  @param enabled YES:打开 NO:关闭
	 */
	- (void) WGOpenMSDKDnsLog:(BOOL) enabled;
```
#### 接口调用示例代码：

```
[[MSDKDns sharedInstance] WGOpenMSDKDnsLog: YES];
```
## 注意事项
如果客户端的业务已与 Host 绑定，例如绑定了 Host 的 HTTP 服务或 CDN 的服务，那么在用 HTTPDNS 返回的 IP 替换掉 URL 中的域名以后，还需要指定下 HTTP 头的 Host 字段。
- 以 NSURLConnection 为例：
```
NSURL* httpDnsURL = [NSURL URLWithString:@”使用解析结果 IP 拼接的 URL ”];
float timeOut = 设置的超时时间;
NSMutableURLRequest* mutableReq = [NSMutableURLRequest requestWithURL:httpDnsURL cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval: timeOut];
[mutableReq setValue:@"原域名" forHTTPHeaderField:@"host"];
NSURLConnection* connection = [[NSURLConnection alloc] initWithRequest:mutableReq delegate:self];
[connection start];
```
- 以 curl 为例：
假设您要访问 www.qq.com， 通过 HTTPDNS 解析出来的 IP 为 192.168.0.111，那么通过这个方式来调用即可：
```
curl -H "host:www.qq.com" http://192.168.0.111/aaa.txt.
```
- 以 Unity 的 WWW 接口为例：
```
string httpDnsURL = "使用解析结果 IP 拼接的 URL";
Dictionary<string, string> headers = new Dictionary<string, string> ();
headers["host"] = "原域名";
WWW conn = new WWW (url, null, headers);
yield return conn;
if (conn.error != null)  
{  
	print("error is happened:"+ conn.error);      
} else  
{  
	print("request ok" + conn.text); 
}  
```

## 实践场景
###  Unity 工程接入
#### 1. 在 cs 文件中进行接口声明：
```
#if UNITY_IOS
[DllImport("__Internal")]
private static extern string WGGetHostByName(string domain);
[DllImport("__Internal")]
private static extern void WGGetHostByNameAsync(string domain);
#endif
```

#### 2. 在需要进行域名解析的部分，调用 WGGetHostByName (string domain) 或者 WGGetHostByNameAsync (string domain) 方法
- 如使用同步接口 **WGGetHostByName**，直接调用接口即可；
- 如果使用异步接口 **WGGetHostByNameAsync**，还需设置回调函数 **onDnsNotify(string ipString)**，函数名可自定义
并建议添加如下处理代码：

```
string ips = HttpDns.GetHostByName(domainStr);
string[] sArray=ips.Split(new char[] {';'}); 
if (sArray != null && sArray.Length > 1) {
if (!sArray[1].Equals("0")) {
//使用建议：当 IPv6 地址存在时，优先使用 IPv6 地址
//TODO 使用 ipv6 地址进行 URL 连接时，注意格式，需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
				
} else if(!sArray [0].Equals ("0")) {
//使用 IPv4 地址进行连接
				
} else {
//异常情况返回为0,0 建议重试一次
HttpDns.GetHostByName(domainStr);
}
}
```

#### 3. 将 unity 工程打包为 xcode 工程后，引入所需依赖库；
#### 4. 将 HTTPDNSUnityDemo 下的 `MSDKDnsUnityManager.h`及`MSDKDnsUnityManager.mm`文件导入到工程中，注意以下地方需要与 Unity 中对应的 GameObject 名称及回调函数名称一致：
![](https://main.qcloudimg.com/raw/dc203ca596d0873427504b6b70fba912.jpg)
![](https://main.qcloudimg.com/raw/a33039bb68f478895516dd4352a19aa6.jpg)

### 普通 HTTPS 场景
原理：在进行证书校验时，将 IP 替换成原来的域名，再进行证书验证。
**Demo 示例**
#### 1. 以 NSURLConnection 接口为例，实现以下两个方法：

```
- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust forDomain:(NSString *)domain        
{
/*
* 创建证书校验策略
*/
NSMutableArray *policies = [NSMutableArray array];
if (domain) {
[policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
} else {
[policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
}
/*
* 绑定校验策略到服务端的证书上
*/
SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);
/*
* 评估当前serverTrust是否可信任，
* 官方建议在result = kSecTrustResultUnspecified 或 kSecTrustResultProceed的情况下serverTrust可以被验证通过
*  https://developer.apple.com/library/ios/technotes/tn2232/_index.html
* 关于SecTrustResultType的详细信息请参考SecTrust.h
*/
SecTrustResultType result;
SecTrustEvaluate(serverTrust, &result);
return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);        
}
```

```
-(void)connection:(NSURLConnection*)connection willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge        
{
if (!challenge) {
return;
}   
/*
* URL里面的 host 在使用 HTTPDNS 的情况下被设置成了 IP，此处从 HTTP Header 中获取真实域名
*/
NSString* host = [[self.request allHTTPHeaderFields] objectForKey:@"host"];
if (!host) {
host = self.request.URL.host;
}        

/*
* 判断 challenge 的身份验证方法是否是 NSURLAuthenticationMethodServerTrust（HTTPS模式下会进行该身份验证流程），
* 在没有配置身份验证方法的情况下进行默认的网络请求流程。
*/
if([challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust])
{
if([self evaluateServerTrust:challenge.protectionSpace.serverTrust 
forDomain:host]) {
/*
* 验证完以后，需要构造一个 NSURLCredential 发送给发起方
*/
NSURLCredential *credential = [NSURLCredential 
credentialForTrust:challenge.protectionSpace.serverTrust];
[[challenge sender] useCredential:credential forAuthenticationChallenge:challenge];
} else {
/*
* 验证失败，取消这次验证流程
*/
[[challenge sender] cancelAuthenticationChallenge:challenge];
}
} else {
/*
* 对于其他验证方法直接进行处理流程
*/
[[challenge sender] continueWithoutCredentialForAuthenticationChallenge:challenge];
}
}
```
#### 2. 以 NSURLSession 接口为例，实现以下两个方法：

```
- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust forDomain:(NSString *)domain        
{
/*
* 创建证书校验策略
*/
NSMutableArray *policies = [NSMutableArray array];
if (domain) {
[policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
} else {
[policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
}
/*
* 绑定校验策略到服务端的证书上
*/
SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);
/*
* 评估当前 serverTrust 是否可信任，
* 官方建议在 result = kSecTrustResultUnspecified 或 kSecTrustResultProceed 的情况下 serverTrust 可以被验证通过
*  https://developer.apple.com/library/ios/technotes/tn2232/_index.html
* 关于 SecTrustResultType 的详细信息请参考 SecTrust.h
*/
SecTrustResultType result;
SecTrustEvaluate(serverTrust, &result);
return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);        
}
```

```
- (void)URLSession:(NSURLSession *)session task:(NSURLSessionTask *)task
didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential * __nullable credential))completionHandler
{
if (!challenge) {
return;
}
NSURLSessionAuthChallengeDisposition disposition = NSURLSessionAuthChallengePerformDefaultHandling;
NSURLCredential *credential = nil;
/*
* 获取原始域名信息。
*/
NSString* host = [[self.request allHTTPHeaderFields] objectForKey:@"host"];
if (!host) {
host = self.request.URL.host;
}
if ([challenge.protectionSpace.authenticationMethod
isEqualToString:NSURLAuthenticationMethodServerTrust]) {
if ([self evaluateServerTrust:challenge.protectionSpace.serverTrust 
forDomain:host]) {
disposition = NSURLSessionAuthChallengeUseCredential;
		credential = [NSURLCredential 
credentialForTrust:challenge.protectionSpace.serverTrust];
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
#### 3. 以 Unity 的 WWW 接口为例：
将 Unity 工程导为 Xcode工程后，打开`Classes/Unity/WWWConnection.mm`文件，修改下述代码：
```
//const char* WWWDelegateClassName = "UnityWWWConnectionSelfSignedCertDelegate";
const char* WWWDelegateClassName = "UnityWWWConnectionDelegate";
```
为：
```
const char* WWWDelegateClassName = "UnityWWWConnectionSelfSignedCertDelegate";
//const char* WWWDelegateClassName = "UnityWWWConnectionDelegate";
```

### HTTPS SNI（单 IP 多 HTTPS 证书）场景
SNI（Server Name Indication）是为了解决一个服务器使用多个域名和证书的 SSL/TLS 扩展。它的工作原理如下：

- 在连接到服务器建立 SSL 链接之前先发送要访问站点的域名（Hostname）。
- 服务器根据这个域名返回一个合适的证书。

上述过程中，当客户端使用 HttpDns 解析域名时，请求 URL 中的 host 会被替换成 HttpDns 解析出来的 IP，导致服务器获取到的域名为解析后的 IP，无法找到匹配的证书，只能返回默认的证书或者不返回，所以会出现 SSL/TLS 握手不成功的错误。

由于 iOS 上层网络库 NSURLConnection/NSURLSession 没有提供接口进行 SNI 字段的配置，因此可以考虑使用 NSURLProtocol 拦截网络请求，然后使用 CFHTTPMessageRef 创建 NSInputStream 实例进行 Socket 通信，并设置其 kCFStreamSSLPeerName 的值。
需要注意的是，使用 NSURLProtocol 拦截 NSURLSession 发起的 POST 请求时，HTTPBody 为空。解决方案有两个：
1. 使用 NSURLConnection 发 POST 请求。
2. 先将 HTTPBody 放入 HTTP Header field 中，然后在 NSURLProtocol 中再取出来。

具体示例参见 Demo，部分代码如下：
在网络请求前注册 NSURLProtocol 子类，在示例的 `SNIViewController.m `中。
```
// 注册拦截请求的 NSURLProtocol
[NSURLProtocol registerClass:[MSDKDnsHttpMessageTools class]];

// 需要设置 SNI 的 URL
NSString *originalUrl = @"your url";
NSURL* url = [NSURL URLWithString:originalUrl];
NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:url];
NSArray* result = [[MSDKDns sharedInstance] WGGetHostByName:url.host];
NSString* ip = nil;
if (result && result.count > 1) {
    if (![result[1] isEqualToString:@"0"]) {
        ip = result[1];
    } else {
        ip = result[0];
    }
}
```

```
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
// 解决方案有两个：1. 使用 NSURLConnection 发 POST 请求。
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
#### 使用说明：
可在`info.plist`中配置需要拦截域名和无需拦截的域名：

| Key| Type | Value |
|---------|---------|---------|
|HijackDomain | Array | 需要拦截的域名列表 |
|NotHijack_Domain |Array | 不需要拦截的域名列表 |

- 如设置了需要拦截的域名列表，则仅会拦截处理该域名列表中的 HTTPS 请求，其它域名不做处理；
- 如设置了不需要拦截的域名列表，则不会拦截处理该域名列表中的 HTTPS 请求；

建议使用 Hijack_Domain 仅拦截 SNI 场景下的域名，避免拦截其它场景下的域名。
