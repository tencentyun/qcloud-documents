## iOS SDK接入

### 概述
移动解析 HTTPDNS 的主要功能是为了有效避免由于运营商传统 LocalDNS 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。

### 前期准备
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


### 安装包结构
- SDK 最新版本包 [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSLibs)。
- SDK 开源 [仓库地址](https://github.com/DNSPod/httpdns-sdk-ios)。

| 名称       | 适用说明           |
| ------------- |-------------|
| MSDKDns.xcframework | 适用 “Build Setting->C++ Language Dialect” 配置为 **“GNU++98”**，“Build Setting->C++ Standard Library” 为 **“libstdc++(GNU C++ standard library)”** 的工程。 |
| MSDKDns_C11.xcframework | 适用于该两项配置分别为 **“GNU++11”** 和 **“libc++(LLVM C++ standard library with C++11 support)”** 的工程。 |


### SDK 集成
移动解析 HTTPDNS 提供两种集成方式供 iOS 开发者选择：
- 通过 CocoaPods 集成。
- 手动集成。

手动集成可以参考以下案例：
- Objective-C Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSDemo)。
- Swift Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSSwiftDemo)。


#### 通过 CocoaPods 集成
在工程的 Podfile 里面添加以下代码：
```
# 适用“Build Setting->C++ Language Dialect”配置为**“GNU++98”**，“Build Setting->C++ Standard Library”为**“libstdc++(GNU C++ standard library)”**的工程。
  pod 'MSDKDns'
# 适用于该两项配置分别为**“GNU++11”**和**“libc++(LLVM C++ standard library with C++11 support)”**的工程。
# pod 'MSDKDns_C11'
```
保存并执行 `pod install`，再使用后缀为 `.xcworkspace` 的文件打开工程。

>?关于 `CocoaPods` 的更多信息，请查看 [CocoaPods 官方网站](https://cocoapods.org/)。

#### 手动集成

##### 已接入灯塔（Beacon）的业务（可选）
>?灯塔（beacon）SDK 是腾讯灯塔团队开发的用于移动应用统计分析的 SDK，HTTPDNS SDK 使用灯塔（beacon）SDK 收集域名解析质量数据，辅助定位问题。
>
仅需引入位于 HTTPDNSLibs 目录下的 MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）即可。

##### 未接入灯塔（Beacon）的业务（可选）
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


### 接入验证
#### 日志验证
开启 SDK 调试日志（设置 DnsConfig 中 debug 为 YES），找到打印的 `ReportingEvent, name:HDNSGetHostByName, events: { ... }` 日志，并检查 LocalDns（日志上为 ldns_ip）和 HTTPDNS（日志上为 hdns_ip）相关日志，可以确认接入是否成功。
- key 为 ldns_ip 的是 LocalDNS 的解析结果。
- key 为 hdns_ip 的是 HTTPDNS A 记录的解析结果。
- key 为 hdns_4a_ips 的是 HTTPDNS AAAA 记录的解析结果。
- 如果 hdns_ip 或 hdns_4a_ips 不为空，则说明接入成功。


### 注意事项
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

