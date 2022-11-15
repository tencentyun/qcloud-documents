## 设置业务基本信息

### 类型定义

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
 	IP地址类型
**/
typedef enum {
    HttpDnsAddressTypeAuto = 0, // sdk自动检测
    HttpDnsAddressTypeIPv4 = 1, // 只支持ipv4
    HttpDnsAddressTypeIPv6 = 2, // 只支持ipv6
    HttpDnsAddressTypeDual = 3, // 支持双协议栈
} HttpDnsAddressType;

/**
	配置结构体
	以下鉴权信息可在腾讯云控制台（https://console.cloud.tencent.com/httpdns/configure）开通服务后获取
**/
typedef struct DnsConfigStruct {
    NSString* appId; // 可选，应用ID，腾讯云控制台申请获得，用于灯塔数据上报（未集成灯塔时该参数无效）
    int dnsId; // 授权ID，腾讯云控制台申请后可直接在控制台查看
    NSString* dnsKey; // 加密密钥，加密方式为 AES、DES 时必传。腾讯云控制台申请后可直接在控制台查看，用于域名解析鉴权
    NSString* token; // 加密 token，加密方式为 HTTPS 时必传
    NSString* dnsIp; // HTTPDNS 服务器 IP。HTTP 协议服务地址为 `119.29.29.98`，HTTPS 协议服务地址为 `119.29.29.99`
    BOOL debug; // 是否开启Debug日志，YES：开启，NO：关闭。建议联调阶段开启，正式上线前关闭
    int timeout; // 可选，超时时间，单位ms，如设置0，则使用默认值2000ms
    HttpDnsEncryptType encryptType; // 控制加密方式
	HttpDnsAddressType addressType; // 指定返回的ip地址类型，默认为 HttpDnsAddressTypeAuto sdk自动检测
    NSString* routeIp; // 可选，DNS 请求的 ECS（EDNS-Client-Subnet）值，默认情况下 HTTPDNS 服务器会查询客户端出口 IP 为 DNS 线路查询 IP，可以指定线路 IP 地址。支持 IPv4/IPv6 地址传入
    BOOL httpOnly;// 可选，是否仅返回 httpDns 解析结果。默认 false，即当 httpDns 解析失败时会返回 LocalDNS 解析结果，设置为 true 时，仅返回 httpDns 的解析结果
    NSUInteger retryTimesBeforeSwitchServer; // 可选，切换ip之前重试次数, 默认3次
    NSUInteger minutesBeforeSwitchToMain; // 可选，设置切回主ip间隔时长，默认10分钟
    BOOL enableReport; // 是否开启解析异常上报，默认NO，不上报
} DnsConfig;
```


### 接口声明
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

/**
 * 预解析域名。建议不要设置太多预解析域名，当前限制为最多 8 个域名。仅在初始化时触发。
 *  示例代码：[[MSDKDns sharedInstance] WGSetPreResolvedDomains:@[@"dnspod.com", @"dnspod.cn"]];
 * @param domains  域名数组
 */
- (void) WGSetPreResolvedDomains:(NSArray *)domains;

/**
 * 解析缓存自动刷新, 以数组形式进行配置。当前限制为最多 8 个域名。
 * 示例代码：[[MSDKDns sharedInstance] WGSetKeepAliveDomains:@[@"dnspod.com", @"dnspod.cn"]];
 * @param domains  域名数组
 */
- (void) WGSetKeepAliveDomains:(NSArray *)domains;


/**
 * 启用IP优选，设置域名对应的端口号，对域名解析返回的IP列表进行IP探测，对返回的列表进行动态排序，以保证第一个IP是可用性最好的IP
 */
- (void) WGSetIPRankData:(NSDictionary *)IPRankData;

/**
 * 设置是否允许返回TTL过期域名的IP，默认关闭
 * 设置为true时，会直接返回缓存的解析结果，没有缓存则返回0。且在无缓存结果或缓存已过期时，会异步发起解析请求更新缓存。因异步接口逻辑在回调中始终返回未过期的解析结果，设置为true时，异步API不可使用。建议使用同步接口。
 */
- (void) WGSetExpiredIPEnabled:(BOOL)enable;

/**
 * 设置是否启用本地持久化缓存功能，默认关闭
 * 如果需要开启此功能，需要使用MSDKDns_C11包，并且需要引入WCDB包
 */
- (void) WGSetPersistCacheIPEnabled:(BOOL)enable;
```
<dx-alert infotype="notice" title="">
- HTTPDNS SDK 提供多重解析优化策略，建议根据实际情况选配，也可以组合使用，可使得解析成功率达到最优效果。
- 可以通过配置 `(void) WGSetExpiredIPEnabled:(true)enable;` 和 `(void) WGSetPersistCacheIPEnabled:(true)enable;` 来实现乐观 DNS 缓存。
  - 该功能旨在提升缓存命中率和首屏加载速度。持久化缓存会将上一次解析结果保持在本地，在 App 启动时，会优先读取到本地缓存解析结果。
  - 存在使用缓存 IP 时为过期 IP（TTL 过期），该功能启用了允许使用过期 IP，乐观的推定 TTL 过期，大多数情况下该 IP 仍能正常使用。优先返回缓存的过期结果，同时异步发起解析服务，更新缓存。
  - 乐观 DNS 缓存在首次解析域名（无缓存）时，无法命中缓存，返回0;0，同时也会异步发起解析服务，更新缓存。在启用该功能后需自行 LocalDNS 兜底。核心域名建议配置预解析服务 `(void) WGSetPreResolvedDomains:(NSArray *)domains;`。
  - 如果业务服务器 IP 变化比较频繁，务必启用缓存自动刷新 `(void) WGSetKeepAliveDomains:(NSArray *)domains;`、预解析能力 `(void) WGSetPreResolvedDomains:(NSArray *)domains;`，以确保解析结果的准确性。
</dx-alert>


### 示例代码

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


## 域名解析接口

**获取 IP 共有以下四个接口，**引入头文件，调用相应接口即可。
- 同步接口 
	-	单个查询 **WGGetHostByName:**；
	- 批量查询（返回单个 IP）**WGGetHostsByNames:**；
	- 批量查询（返回所有 IP）**WGGetAllHostsByNames:**；
- 异步接口 
	- 单个查询 **WGGetHostByNameAsync:returnIps:**；
	- 批量查询 (返回单个 IP）**WGGetHostsByNamesAsync:returnIps:**；
	- 批量查询（返回所有 IP）**WGGetAllHostsByNamesAsync:returnIps:**；

**返回的地址格式如下：**
- **单个查询**：单个查询接口返回 NSArray，固定长度为2，其中第一个值为 IPv4 地址，第二个值为 IPv6 地址。以下为返回格式的详细说明：
 - IPv4 下，仅返回 IPv4 地址，即返回格式为：[ipv4, 0]。
 - IPv6 下，仅返回 IPv6 地址，即返回格式为：[0, ipv6]。
 - 双栈网络下，返回解析到 IPv4&IPv6（如果存在）地址，即返回格式为：[ipv4, ipv6]。
 - 解析失败，返回[0, 0]，业务重新调用 WGGetHostByName 接口即可。
- **批量查询（返回单个 IP）**：批量查询接口返回 NSDictionary，key 为查询的域名，value 为 NSArray，固定长度为2，其他第一个值为 IPv4 地址，第二个值为 IPv6 地址。以下为返回格式的详细说明：
 - IPv4 下，仅返回 IPv4 地址，即返回格式为：{"queryDomain" : [ipv4, 0]}。
 - IPv6 下，仅返回 IPv6 地址，即返回格式为：{"queryDomain" : [0, ipv6]}。
 - 双栈网络下，返回解析到 IPv4&IPv6（如果存在）地址，即返回格式为：{"queryDomain" : [ipv4, ipv6]}。
 - 解析失败，返回{"queryDomain" : [0, 0]}，业务重新调用 WGGetHostsByNames 接口即可。
- **批量查询（返回所有 IP）**：批量查询接口返回 NSDictionary，key 为查询的域名，value 为 NSDictionary，包含两个 key（ipv4、ipv6），对应的 value 为 NSArray 对象，表示所有的ipv4/ipv6 解析结果 IP。以下为返回格式的详细说明：
 返回格式为：{"queryDomain" : { "ipv4": [], "ipv6": []}}。



<dx-alert infotype="notice" title="">
- 使用 IPv6 地址进行 URL 请求时，需添加方框号[ ]进行处理，例如：`http://[64:ff9b::b6fe:7475]/`。
- 如 IPv6 地址为0，则直接使用 IPv4 地址连接。
- 如 IPv4 地址为0，则直接使用 IPv6 地址连接。
- 如 IPv4 和 IPv6 地址都不为0，则由客户端决定优先使用哪个地址进行连接，但优先地址连接失败时应切换为另一个地址。 
- 使用 SDK 方式接入 HTTPDNS，若 HTTPDNS 未查询到解析结果，则通过 LocalDNS 进行域名解析，返回 LocalDNS 的解析结果。
</dx-alert>




### 同步解析接口 

#### 接口名称
WGGetHostByName、WGGetHostsByNames

#### 接口声明

```objc
/**
 域名同步解析（通用接口）
 @param domain 域名 
 @return 查询到的 IP 数组，超时（1s）或者未查询到返回[0,0]数组
*/
- (NSArray *) WGGetHostByName:(NSString *) domain;

/**
 域名批量同步解析（通用接口）
 @param domains 域名数组
 @return 查询到的 IP 字典
 */
- (NSDictionary *) WGGetHostsByNames:(NSArray *) domains;
```

#### 示例代码

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
NSDictionary *ipsDict = [[MSDKDns sharedInstance] WGGetHostsByNames: @[@"qq.com", @"dnspod.cn"]];
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

### 异步解析接口

#### 接口名称
WGGetHostByNameAsync、WGGetHostsByNamesAsync

#### 接口声明

```objc
/**
 域名异步解析（通用接口）
 @param domain  域名
 @param handler 返回查询到的 IP 数组，超时（1s）或者未查询到返回[0,0]数组
 */
 - (void) WGGetHostByNameAsync:(NSString *) domain returnIps:(void (^)(NSArray *ipsArray))handler;

 /**
 域名批量异步解析（通用接口）

 @param domains  域名数组
 @param handler 返回查询到的IP字典，超时（1s）或者未查询到返回 {"queryDomain" : [0, 0] ...}
 */
- (void) WGGetHostsByNamesAsync:(NSArray *) domains returnIps:(void (^)(NSDictionary * ipsDictionary))handler;
```

#### 示例代码

<dx-alert infotype="notice" title="">
业务可根据自身需求，任选一种调用方式。
</dx-alert>

<dx-tabs>
::: 示例1
等待完整解析过程结束后，拿到结果，进行连接操作。
 - 优点：可保证每次请求都能拿到返回结果进行接下来的连接操作。
 - 缺点：异步接口的处理较同步接口稍显复杂。


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
[[MSDKDns sharedInstance] WGGetHostsByNamesAsync:@[@"qq.com", @"dnspod.cn"] returnIps:^(NSDictionary *ipsDict) {
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

:::
::: 示例2
无需等待，可直接拿到缓存结果，如无缓存，则 result 为 nil。
   - 优点：对于解析时间有严格要求的业务，使用本示例，可无需等待，直接拿到缓存结果进行后续的连接操作，完全避免了同步接口中解析耗时可能会超过 100ms 的情况。
   - 缺点：第一次请求时，result 一定会 nil，需业务增加处理逻辑。

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
:::
</dx-tabs>
