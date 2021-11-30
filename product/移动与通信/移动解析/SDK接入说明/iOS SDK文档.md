## 概述
移动解析 HTTPDNS 的主要功能是为了有效避免由于运营商传统 LocalDns 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。

## 前期准备
1. 首先需要开通移动解析 HTTPDNS 服务，请前往 [移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 开通。具体操作请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。
2. 开通移动解析 HTTPDNS 服务后，您需在移动解析 HTTPDNS 控制台添加解析域名后才可正常使用。具体操作请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。
4. 已在移动解析 HTTPDNS 控制台 [开通 SDK](https://cloud.tencent.com/document/product/379/12544)。
5. 开通服务后，移动解析 HTTPDNS 将为您分配授权 ID、AES 和 DES 加密密钥及 HTTPS Token 等配置信息。使用 iOS SDK 需求获取的配置如下：
![](https://main.qcloudimg.com/raw/0a4481963d31b07e20a3136021fb4743.png)
 - **授权 ID**：使⽤移动解析 HTTPDNS 服务中，开发配置的唯⼀标识。SDK中 `dnsId` 参数，用于域名解析鉴权。
 - **DES 加密密钥**：SDK 中 `dnsKey` 参数，加密方式为 DES 时传入此项。
 - **AES 加密密钥**：SDK 中 `dnsKey` 参数，加密方式为 AES 时传入此项。
 - **HTTPS 加密 Token**：SDK 中 `token` 参数，加密方式为 HTTPS 时传入此项。
 -  **IOS APPID**： [IOS 端 SDK](https://cloud.tencent.com/document/product/379/17669) 的 `appId（应用 ID）` 鉴权信息。


## 安装包结构
- SDK 最新版本包 [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSLibs)。
- SDK 开源 [仓库地址](https://github.com/DNSPod/httpdns-sdk-ios)。

| 名称       | 适用说明           |
| ------------- |-------------|
| MSDKDns.xcframework | 适用 “Build Setting->C++ Language Dialect” 配置为 **“GNU++98”**，“Build Setting->C++ Standard Library” 为 **“libstdc++(GNU C++ standard library)”** 的工程。 |
| MSDKDns_C11.xcframework | 适用于该两项配置分别为 **“GNU++11”** 和 **“libc++(LLVM C++ standard library with C++11 support)”** 的工程。 |


## SDK 集成
移动解析 HTTPDNS 提供两种集成方式供 iOS 开发者选择：
- 通过 CocoaPods 集成。
- 手动集成。

手动集成可以参考以下案例：
- Objective-C Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSDemo)。
- Swift Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSSwiftDemo)。


### 通过 CocoaPods 集成
在工程的 Podfile 里面添加以下代码：
```
# 适用“Build Setting->C++ Language Dialect”配置为**“GNU++98”**，“Build Setting->C++ Standard Library”为**“libstdc++(GNU C++ standard library)”**的工程。
  pod 'MSDKDns'
# 适用于该两项配置分别为**“GNU++11”**和**“libc++(LLVM C++ standard library with C++11 support)”**的工程。
# pod 'MSDKDns_C11'
```
保存并执行 `pod install`，再使用后缀为 `.xcworkspace` 的文件打开工程。

>?关于 `CocoaPods` 的更多信息，请查看 [CocoaPods 官方网站](https://cocoapods.org/)。

### 手动集成

#### 已接入灯塔（Beacon）的业务（可选）
>?灯塔（beacon）SDK 是腾讯灯塔团队开发的用于移动应用统计分析的 SDK，HTTPDNS SDK 使用灯塔（beacon）SDK 收集域名解析质量数据，辅助定位问题。
>
仅需引入位于 HTTPDNSLibs 目录下的 MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）即可。

#### 未接入灯塔（Beacon）的业务（可选）
- 引入依赖库（位于 HTTPDNSLibs 目录下）：
	- BeaconAPI_Base.framework
	- MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）
- 引入系统库：
	- libz.tbd
	- libsqlite3.tbd
	- libc++.tbd
	- Foundation.framework
	- CoreTelephony.framework
	- SystemConfiguration.framework
	- CoreGraphics.framework
	- Security.framework
- 并在 `application:didFinishLaunchingWithOptions:` 加入注册灯塔代码：
```
//已正常接入灯塔的业务无需关注以下代码，未接入灯塔的业务调用以下代码注册灯塔
//******************************
[BeaconBaseInterface setAppKey:@"0000066HQK3XNL5U"];
[BeaconBaseInterface enableAnalytics:@"" gatewayIP:nil];
//******************************
```
>!请在 Other linker flag 里加入 -ObjC 标志。

## API 及使用示例

### 设置业务基本信息

#### 类型定义

```c++

/**
	加密方式
**/
typedef enum {
    HttpDnsEncryptTypeDES = 0, // DES 加密
    HttpDnsEncryptTypeAES = 1, // AES 加密
    HttpDnsEncryptTypeHTTPS = 2 // HTTPS 加密
} HttpDnsEncryptType;

/**
	配置结构体
	以下鉴权信息可在腾讯云控制台（https://console.cloud.tencent.com/httpdns/configure）开通服务后获取
**/
struct DnsConfig {
    NSString* appId; // 应用ID，腾讯云控制台申请获得，用于上报
    int dnsId; // 授权ID，用于域名解析鉴权
    NSString* dnsKey; // 加密密钥，加密方式为 AES、DES 时必传
    NSString* token; // 加密方式为 HTTPS 时必传
    NSString* dnsIp; // HTTPDNS 服务器 IP
    BOOL debug; // 是否开启Debug日志，YES：开启，NO：关闭。建议联调阶段开启，正式上线前关闭
    int timeout; // 超时时间，单位ms，如设置0，则设置为默认值2000ms
    HttpDnsEncryptType encryptType; // 控制加密方式
    NSString* routeIp; // 查询线路 IP 地址
};
```

#### 接口声明

```objc
/**
 设置业务基本信息（腾讯云业务使用）

 @param config 业务配置结构体
 @return YES:设置成功 NO:设置失败
 */
- (BOOL) initConfig:(DnsConfig *)config;

/**
 * 通过 Dictionary 配置，字段参考 DnsConfig 结构，用于兼容 swift 项目，解决 swift 项目中无法识别 DnsConfig 类型的问题
 *
 * @param config  配置
 * @return YES：设置成功 NO：设置失败
 */
- (BOOL) initConfigWithDictionary:(NSDictionary *)config;
```
#### 示例代码

接口调用示例：
- 在 Objective-C 项目中。
```objc
	DNSConfig *config = new DnsConfig();
	config->dnsIp = @"HTTPDNS 服务器IP";
	config->dnsId = @"dns授权id";
	config->dnsKey = @"加密密钥";
	config->encryptType = HttpDnsEncryptTypeDES;
	config->debug = YES;
	config->timeout = 2000;
	config->routeIp = @"查询线路ip";
	[[MSDKDns sharedInstance] initConfig: config];
```

- 在 Swift 项目中。
```swift
let msdkDns = MSDKDns.sharedInstance() as? MSDKDns;
msdkDns?.initConfig(with: [
		"dnsIp": "HTTPDNS 服务器IP",
		"dnsId": "dns授权id",
		"dnsKey": "加密密钥",
		"encryptType": 0, // 0 -> des，1 -> aes，2 -> https
]);
```
### 域名解析接口

**获取 IP 共有以下四个接口，**引入头文件，调用相应接口即可。
- 同步接口 
	-	单个查询 **WGGetHostByName:**；
	- 批量查询 **WGGetHostsByNames:**；
- 异步接口 
	- 单个查询 **WGGetHostByNameAsync:returnIps:**；
	- 批量查询 **WGGetHostsByNamesAsync:returnIps:**；

**返回的地址格式如下：**
- **单个查询**：单个查询接口返回 NSArray，固定长度为2，其中第一个值为 IPv4 地址，第二个值为 IPv6 地址。以下为返回格式的详细说明：
 - IPv4 下，仅返回 IPv4 地址，即返回格式为：[ipv4, 0]。
 - IPv6 下，仅返回 IPv6 地址，即返回格式为：[0, ipv6]。
 - 双栈网络下，返回解析到 IPv4&IPv6（如果存在）地址，即返回格式为：[ipv4, ipv6]。
 - 解析失败，返回[0, 0]，业务重新调用 WGGetHostByName 接口即可。
- **批量查询**：批量查询接口返回 NSDictionary，key 为查询的域名，value 为 NSArray，固定长度为2，其他第一个值为 IPv4 地址，第二个值为 IPv6 地址。以下为返回格式的详细说明：
 - IPv4 下，仅返回 IPv4 地址，即返回格式为：{"queryDomain" : [ipv4, 0]}。
 - IPv6 下，仅返回 IPv6 地址，即返回格式为：{"queryDomain" : [0, ipv6]}。
 - 双栈网络下，返回解析到 IPv4&IPv6（如果存在）地址，即返回格式为：{"queryDomain" : [ipv4, ipv6]}。
 - 解析失败，返回{"queryDomain" : [0, 0]}，业务重新调用 WGGetHostByNames 接口即可。

>!
>- 使用 IPv6 地址进行 URL 请求时，需添加方框号[ ]进行处理，例如：`http://[64:ff9b::b6fe:7475]/`。
>- 如 IPv6 地址为0，则直接使用 IPv4 地址连接。
>- 如 IPv4 地址为0，则直接使用 IPv6 地址连接。
>- 如 IPv4 和 IPv6 地址都不为0，则由客户端决定优先使用哪个地址进行连接，但优先地址连接失败时应切换为另一个地址。 
>- 使用 SDK 方式接入 HTTPDNS，若 HTTPDNS 未查询到解析结果，则通过 LocalDNS 进行域名解析，返回 LocalDNS 的解析结果。

#### 同步解析接口：WGGetHostByName、WGGetHostByNames

##### 接口声明

```objc
/**
 域名同步解析（通用接口）
 @param domain 域名 
 @return 查询到的 IP 数组，超时（1s）或者未未查询到返回[0,0]数组
*/
- (NSArray *) WGGetHostByName:(NSString *) domain;

/**
 域名批量同步解析（通用接口）
 @param domains 域名数组
 @return 查询到的 IP 字典
 */
- (NSDictionary *) WGGetHostsByNames:(NSArray *) domains;
```
##### 示例代码

接口调用示例：

```objc
// 单个域名查询
NSArray *ipsArray = [[MSDKDns sharedInstance] WGGetHostByName: @"qq.com"];
if (ipsArray && ipsArray.count > 1) {
	NSString *ipv4 = ipsArray[0];
	NSString *ipv6 = ipsArray[1];
	if (![ipv6 isEqualToString:@"0"]) {
		//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，IPv6 需加方框号[]进行处理，例如：http://[64:ff9b::b6fe:7475]/
	} else if (![ipv4 isEqualToString:@"0"]){
		//使用 IPv4 地址进行连接
	} else {
		//异常情况返回为0,0，建议重试一次
	}
}

// 批量域名查询
NSDictionary *ipsDict = [[MSDKDns sharedInstance] WGGetHostByNames: @[@"qq.com", @"dnspod.cn"]];
NSArray *ips = [ipsDict objectForKey: @"qq.com"];
if (ips && ips.count > 1) {
	NSString *ipv4 = ips[0];
	NSString *ipv6 = ips[1];
	if (![ipv6 isEqualToString:@"0"]) {
		//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，IPv6 需加方框号[]进行处理，例如：http://[64:ff9b::b6fe:7475]/
	} else if (![ipv4 isEqualToString:@"0"]){
		//使用 IPv4 地址进行连接
	} else {
		//异常情况返回为0,0，建议重试一次
	}
}
```
#### 异步解析接口：WGGetHostByNameAsync、WGGetHostByNamesAsync

##### 接口声明

```objc
/**
 域名异步解析（通用接口）
 @param domain  域名
 @param handler 返回查询到的 IP 数组，超时（1s）或者未未查询到返回[0,0]数组
 */
 - (void) WGGetHostByNameAsync:(NSString *) domain returnIps:(void (^)(NSArray *ipsArray))handler;

 /**
 域名批量异步解析（通用接口）

 @param domains  域名数组
 @param handler 返回查询到的IP字典，超时（1s）或者未查询到返回 {"queryDomain" : [0, 0] ...}
 */
- (void) WGGetHostsByNamesAsync:(NSArray *) domains returnIps:(void (^)(NSDictionary * ipsDictionary))handler;
```
##### 示例代码
>!业务可根据自身需求，任选一种调用方式。
 - 示例1：
     - 优点：可保证每次请求都能拿到返回结果进行接下来的连接操作。
     - 缺点：异步接口的处理较同步接口稍显复杂。
 - 示例2：
     - 优点：对于解析时间有严格要求的业务，使用本示例，可无需等待，直接拿到缓存结果进行后续的连接操作，完全避免了同步接口中解析耗时可能会超过 100ms 的情况。
     - 缺点：第一次请求时，result 一定会 nil，需业务增加处理逻辑。

- 接口调用示例1：等待完整解析过程结束后，拿到结果，进行连接操作。
```objc
// 单个域名查询
[[MSDKDns sharedInstance] WGGetHostByNameAsync:@"qq.com" returnIps:^(NSArray *ipsArray) {
	//等待完整解析过程结束后，拿到结果，进行连接操作
	if (ipsArray && ipsArray.count > 1) {
		NSString *ipv4 = ipsArray[0];
		NSString *ipv6 = ipsArray[1];
		if (![ipv6 isEqualToString:@"0"]) {
			//使用建议：当 IPv6 地址存在时，优先使用ipv6地址
			//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，IPv6 需加方框号[]进行处理，例如：http://[64:ff9b::b6fe:7475]/
		} else if (![ipv4 isEqualToString:@"0"]){
			//使用 IPv4 地址进行连接
		} else {
			//异常情况返回为0,0，建议重试一次
		}
	}
}];
// 批量域名查询
[[MSDKDns sharedInstance] WGGetHostByNamesAsync:@[@"qq.com", @"dnspod.cn"] returnIps:^(NSDictionary *ipsDict) {
	//等待完整解析过程结束后，拿到结果，进行连接操作
	NSArray *ips = [ipsDict objectForKey: @"qq.com"];
	if (ips && ips.count > 1) {
		NSString *ipv4 = ips[0];
		NSString *ipv6 = ips[1];
		if (![ipv6 isEqualToString:@"0"]) {
			//使用建议：当ipv6地址存在时，优先使用ipv6地址
			//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，IPv6 需加方框号[]进行处理，例如：http://[64:ff9b::b6fe:7475]/
		} else if (![ipv4 isEqualToString:@"0"]){
			//使用 IPv4 地址进行连接
		} else {
			//异常情况返回为0,0，建议重试一次
		}
	}
}];
```

-  接口调用示例2：无需等待，可直接拿到缓存结果，如无缓存，则 result 为 nil。
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




## 注意事项
1. 如果客户端的业务是与 host 绑定的，例如绑定了 host 的 HTTP 服务或者是 cdn 的服务，那么在用 HTTPDNS 返回的 IP 替换掉 URL 中的域名以后，还需要指定下 HTTP 头的 host 字段。
 - 以 NSURLConnection 为例：
```
NSURL *httpDnsURL = [NSURL URLWithString:@"使用解析结果ip拼接的URL"];
float timeOut = 设置的超时时间;
NSMutableURLRequest *mutableReq = [NSMutableURLRequest requestWithURL:httpDnsURL cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval: timeOut];
[mutableReq setValue:@"原域名" forHTTPHeaderField:@"host"];
NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest:mutableReq delegate:self];
[connection start];
```
 - 以 NSURLSession 为例：  
 ```
NSURL *httpDnsURL = [NSURL URLWithString:@"使用解析结果ip拼接的URL"];
float timeOut = 设置的超时时间;
NSMutableURLRequest *mutableReq = [NSMutableURLRequest requestWithURL:httpDnsURL cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval: timeOut];
[mutableReq setValue:@"原域名" forHTTPHeaderField:@"host"];
NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
NSURLSession *session = [NSURLSession sessionWithConfiguration:configuration delegate:self delegateQueue:[NSOperationQueue currentQueue]];
NSURLSessionTask *task = [session dataTaskWithRequest:mutableReq];
[task resume];
 ```
 - 以 curl 为例：  
假设您要访问 www.qq.com，通过 HTTPDNS 解析出来的 IP 为192.168.0.111，那么通过这个方式来调用即可：
```
curl -H "host:www.qq.com" http://192.168.0.111/aaa.txt.
```
 - 以 Unity 的 WWW 接口 为例：  
```    
string httpDnsURL = "使用解析结果ip拼接的URL";
Dictionary<string, string> headers = new Dictionary<string, string> ();
headers["host"] = "原域名";
WWW conn = new WWW (url, null, headers);
yield return conn;
if (conn.error != null) {
	print("error is happened:"+ conn.error);
} else {
	print("request ok" + conn.text);
}
```
2. 检测本地是否使用了 HTTP 代理，如果使用了 HTTP 代理，建议不要使用 HTTPDNS 做域名解析。
  - 检测是否使用了 HTTP 代理：
```
	- (BOOL)isUseHTTPProxy {
		CFDictionaryRef dicRef = CFNetworkCopySystemProxySettings();
		const CFStringRef proxyCFstr = (const CFStringRef)CFDictionaryGetValue(dicRef, (const void*)kCFNetworkProxiesHTTPProxy);
		NSString *proxy = (__bridge NSString *)proxyCFstr;
		if (proxy) {
			return YES;
		} else {
			return NO;
		}
	}
```
 - 检测是否使用了 HTTPS 代理：
```
	- (BOOL)isUseHTTPSProxy {
		CFDictionaryRef dicRef = CFNetworkCopySystemProxySettings();
		const CFStringRef proxyCFstr = (const CFStringRef)CFDictionaryGetValue(dicRef, (const void*)kCFNetworkProxiesHTTPSProxy);
		NSString *proxy = (__bridge NSString *)proxyCFstr;
		if (proxy) {
			return YES;
		} else {
			return NO;
		}
	}
```

## 实践场景 
### Unity 工程接入

1. 将 HTTPDNSUnityDemo/Assets/Plugins/Scripts 下的 **HttpDns.cs** 文件拷贝到 Unity 对应 Assets/Plugins/Scripts 路径下。
2. 在需要进行域名解析的部分，调用 HttpDns.GetAddrByName(string domain) 或者 HttpDns.GetAddrByNameAsync(string domain) 方法。
	- 如使用同步接口 **HttpDns.GetAddrByName**，直接调用接口即可。
	- 如果使用异步接口 **HttpDns.GetAddrByNameAsync**，还需设置回调函数 **onDnsNotify(string ipString)**，函数名可自定义。
	 并建议添加如下处理代码：
``` 
string[] sArray=ipString.Split(new char[] {';'}); 
if (sArray != null && sArray.Length > 1) {
	if (!sArray[1].Equals("0")) {
		//使用建议：当 IPv6 地址存在时，优先使用 IPv6 地址
		//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
	} else if(!sArray [0].Equals ("0")) {
		//使 IPv4 地址进行连接
	} else {
		//异常情况返回为0,0，建议重试一次
		HttpDns.GetAddrByName(domainStr);
	}
}
```
3. 将 unity 工程打包为 xcode 工程后，引入所需依赖库。
4. 将 HTTPDNSUnityDemo 下的 MSDKDnsUnityManager.h 及 MSDKDnsUnityManager.mm 文件导入到工程中，注意以下地方需要与 Unity 中对应的 GameObject 名称及回调函数名称一致。如下图所示：
![](https://main.qcloudimg.com/raw/f9a10fb9306f73cfd99c6dde705fc956.jpg)
![](https://main.qcloudimg.com/raw/5e34886a01bb50d17df72be53db03984.jpg)

### HTTPS 场景下（非 SNI）使用 HTTPDNS 解析结果

#### 原理

在进行证书校验时，将 IP 替换成原来的域名，再进行证书验证。

#### Demo 示例

 - **以 NSURLConnection 接口为例：**
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
 - **以 NSURLSession 接口为例：**
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
 - **以 Unity 的 WWW 接口为例：**
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

### SNI（单 IP 多 HTTPS 证书）场景下使用 HTTPDNS 解析结果

SNI（Server Name Indication）是为了解决一个服务器使用多个域名和证书的 SSL/TLS 扩展。它的工作原理如下：
- 在连接到服务器建立 SSL 链接之前先发送要访问站点的域名（Hostname）。
- 服务器根据这个域名返回一个合适的证书。

上述过程中，当客户端使用 HTTPDNS 解析域名时，请求 URL 中的 host 会被替换成 HTTPDNS 解析出来的 IP，导致服务器获取到的域名为解析后的 IP，无法找到匹配的证书，只能返回默认的证书或者不返回，所以会出现 SSL/TLS 握手不成功的错误。

由于 iOS 上层网络库 NSURLConnection/NSURLSession 没有提供接口进行 SNI 字段的配置，因此可以考虑使用 NSURLProtocol 拦截网络请求，然后使用 CFHTTPMessageRef 创建 NSInputStream 实例进行 Socket 通信，并设置其 kCFStreamSSLPeerName 的值。

需要注意的是，使用 NSURLProtocol 拦截 NSURLSession 发起的 POST 请求时，HTTPBody 为空。解决方案有两个：
- 使用 NSURLConnection 发 POST 请求。
- 先将 HTTPBody 放入 HTTP Header field 中，然后在 NSURLProtocol 中再取出来。

具体示例参见 Demo，部分代码如下：
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
#### 使用说明
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
- 如设置了需要拦截的域名列表，则仅会拦截处理该域名列表中的 HTTPS 请求，其它域名不做处理。
- 如设置了不需要拦截的域名列表，则不会拦截处理该域名列表中的 HTTPS 请求。

>!建议使用 WGSetHijackDomainArray 仅拦截 SNI 场景下的域名，避免拦截其它场景下的域名。

