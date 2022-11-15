## 概述
移动解析 HTTPDNS 的主要功能是为了有效避免由于运营商传统 LocalDNS 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。


## 前期准备
1. 开通移动解析 HTTPDNS 服务，详情请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。
2. 服务开通后，您需在移动解析 HTTPDNS 控制台添加解析域名才可正常使用，详情请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。
4. 在移动解析 HTTPDNS 控制台申请接入 SDK，详情请参见 [开通 SDK](https://cloud.tencent.com/document/product/379/12544)。
5. SDK 开通后，移动解析 HTTPDNS 将为您分配授权 ID、AES 和 DES 加密密钥及 HTTPS Token 等配置信息。您可前往 [开发配置](https://console.cloud.tencent.com/httpdns/configure) 页面查看，如下图所示：
![](https://main.qcloudimg.com/raw/0a4481963d31b07e20a3136021fb4743.png)
使用 iOS SDK 需求获取的配置如下：
 - **授权 ID**：使⽤移动解析 HTTPDNS 服务中，开发配置的唯⼀标识。SDK 中 `dnsId` 参数，用于域名解析鉴权。
 - **DES加密密钥**：SDK 中 `dnsKey` 参数，加密方式为 DES 时传入此项。
 - **AES加密密钥**：SDK 中 `dnsKey` 参数，加密方式为 AES 时传入此项。
 - **HTTPS加密Token**：SDK 中 `token` 参数，加密方式为 HTTPS 时传入此项。
 -  **IOS APPID**： [IOS 端 SDK](https://cloud.tencent.com/document/product/379/77756) 的 `appId（应用 ID）` 鉴权信息。


## 安装包结构
- SDK 最新版本包 [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSLibs)。
- SDK 开源 [仓库地址](https://github.com/DNSPod/httpdns-sdk-ios)。

| 名称       | 适用说明           |
| ------------- |-------------|
| MSDKDns.xcframework | 适用 “Build Setting->C++ Language Dialect” 配置为 **“GNU++98”**，“Build Setting->C++ Standard Library” 为 **“libstdc++(GNU C++ standard library)”** 的工程。 |
| MSDKDns_C11.xcframework | 适用于该两项配置分别为 **“GNU++11”** 和 **“libc++(LLVM C++ standard library with C++11 support)”** 的工程。 |

<dx-alert infotype="notice" title="">
MSDKDns_C11 从 V1.6.0 版本开始增加本地数据存储，需引入 WCDB 包。具体操作请参见 [如何接入 WCDB](https://github.com/Tencent/wcdb/wiki#%E5%AE%89%E8%A3%85)。
MSDKDns 不支持本地数据持久化功能，如果需要使用该功能，请更换到 MSDKDns_C11。
</dx-alert>



## SDK 集成
移动解析 HTTPDNS 提供以下两种集成方式供 IOS 开发者选择：
- 通过 CocoaPods 集成。
- 手动集成。


### 通过 CocoaPods 集成
1. 在工程的 Podfile 里面添加以下代码：
```shellsession
# 适用“Build Setting->C++ Language Dialect”配置为**“GNU++98”**，“Build Setting->C++ Standard Library”为**“libstdc++(GNU C++ standard library)”**的工程。
  pod 'MSDKDns'
# 适用于该两项配置分别为**“GNU++11”**和**“libc++(LLVM C++ standard library with C++11 support)”**的工程。
# pod 'MSDKDns_C11'
```
2. 保存并执行 `pod install`，再使用后缀为 `.xcworkspace` 的文件打开工程。


<dx-alert infotype="explain" title="">
关于 `CocoaPods` 的更多信息，请查看 [CocoaPods 官方网站](https://cocoapods.org/)。
</dx-alert>



### 手动集成
手动集成可以参考以下案例：
 - Objective-C Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSDemo)。
 - Swift Demo [下载地址](https://github.com/tencentyun/httpdns-ios-sdk/tree/master/HTTPDNSSwiftDemo)。

**（可选）**您可根据业务是否接入灯塔（Beacon），执行以下步骤：
<dx-alert infotype="explain" title="">
灯塔（beacon）SDK 是腾讯灯塔团队开发的用于移动应用统计分析的 SDK，HTTPDNS SDK 使用灯塔（beacon）SDK 收集域名解析质量数据，辅助定位问题。
</dx-alert>
<dx-tabs>
::: 已接入灯塔（Beacon）的业务

仅需引入位于 HTTPDNSLibs 目录下的 MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）即可。
:::
::: 未接入灯塔（Beacon）的业务

1. 引入依赖库（位于 HTTPDNSLibs 目录下）：
	 - BeaconAPI_Base.framework
	 - MSDKDns.framework（或 MSDKDns_C11.framework，根据工程配置选其一）
2. 引入系统库：
	 - libz.tbd
	 - libsqlite3.tbd
	 - libc++.tbd
	 - Foundation.framework
	 - CoreTelephony.framework
	 - SystemConfiguration.framework
	 - CoreGraphics.framework
	 - Security.framework
3. 在 `application:didFinishLaunchingWithOptions:` 加入注册灯塔代码：
```
//已正常接入灯塔的业务无需关注以下代码，未接入灯塔的业务调用以下代码注册灯塔
//******************************
[BeaconBaseInterface setAppKey:@"0000066HQK3XNL5U"];
[BeaconBaseInterface enableAnalytics:@"" gatewayIP:nil];
//******************************
```
<dx-alert infotype="notice" title="">
请在 Other linker flag 里加入 -ObjC 标志。
</dx-alert>



:::
</dx-tabs>


## SDK 初始化

接口调用示例：
- 在 Objective-C 项目中。
```objc
	DnsConfig *config = new DnsConfig();
	config->dnsIp = @"HTTPDNS 服务器IP";
	config->dnsId = dns授权id;
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


## 接入验证

### 日志验证
开启 SDK 调试日志（设置 DnsConfig 中 debug 为 YES），找到打印的 `ReportingEvent, name:HDNSGetHostByName, events: { ... }` 日志，并检查 LocalDns（日志上为 ldns_ip）和 HTTPDNS（日志上为 hdns_ip）相关日志，可以确认接入是否成功。
- key 为 ldns_ip 的是 LocalDNS 的解析结果。
- key 为 hdns_ip 的是 HTTPDNS A 记录的解析结果。
- key 为 hdns_4a_ips 的是 HTTPDNS AAAA 记录的解析结果。
- 如果 hdns_ip 或 hdns_4a_ips 不为空，则说明接入成功。


## 注意事项
- 如客户端的业务与 host 绑定，例如绑定了 host 的 HTTP 服务或者是 cdn 的服务，那么在用 HTTPDNS 返回的 IP 替换掉 URL 中的域名以后，还需要指定下 HTTP 头的 host 字段。示例如下：
<dx-tabs>
::: NSURLConnection
```
NSURL *httpDnsURL = [NSURL URLWithString:@"使用解析结果ip拼接的URL"];
float timeOut = 设置的超时时间;
NSMutableURLRequest *mutableReq = [NSMutableURLRequest requestWithURL:httpDnsURL cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval: timeOut];
[mutableReq setValue:@"原域名" forHTTPHeaderField:@"host"];
NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest:mutableReq delegate:self];
[connection start];
```

:::
::: NSURLSession
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
 
:::
::: curl
假设您要访问 www.qq.com，通过 HTTPDNS 解析出来的 IP 为192.168.0.111，那么通过以下方式调用即可：
```
curl -H "host:www.qq.com" http://192.168.0.111/aaa.txt.
```
:::
::: Unity 的 WWW 接口
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

:::
</dx-tabs>
- 检测本地是否使用了 HTTP 代理。如使用了 HTTP 代理，建议不要使用 HTTPDNS 做域名解析。
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

