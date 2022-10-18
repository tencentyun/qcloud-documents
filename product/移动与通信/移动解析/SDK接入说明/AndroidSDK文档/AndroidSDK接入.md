## 概述
移动解析 HTTPDNS 作为移动互联网时代 DNS 优化的一个通用解决方案，主要解决了以下几类问题：
- LocalDNS 劫持/故障
- LocalDNS 调度不准确

移动解析 HTTPDNS 的 Android SDK，主要提供了基于移动解析 HTTPDNS 服务的域名解析和缓存管理能力：
- SDK 在进行域名解析时，优先通过移动解析 HTTPDNS 服务得到域名解析结果，极端情况下如果移动解析 HTTPDNS 服务不可用，则使用 LocalDNS 解析结果。
- 移动解析 HTTPDNS 服务返回的域名解析结果会携带相关的 TTL 信息，SDK 会使用该信息进行移动解析 HTTPDNS 解析结果的缓存管理。


<dx-alert infotype="explain" title="">
移动解析 HTTPDNS 服务的详细介绍请参见 [全局精确流量调度新思路-HTTPDNS 服务详解](https://cloud.tencent.com/developer/article/1035562)。
</dx-alert>



## 前期准备
1. 开通移动解析 HTTPDNS 服务，详情请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。
2. 服务开通后，您需在移动解析 HTTPDNS 控制台添加解析域名后才可正常使用，详情请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。
3. 在移动解析 HTTPDNS 控制台申请接入 SDK，详情请参见 [开通 SDK](https://cloud.tencent.com/document/product/379/12544)。
4. SDK 开通后，移动解析 HTTPDNS 将为您分配授权 ID、AES 和 DES 加密密钥及 HTTPS Token 等配置信息。您可前往 [开发配置](https://console.cloud.tencent.com/httpdns/configure) 页面查看，如下图所示：
![](https://main.qcloudimg.com/raw/9de378622bacb7ce9f67bcf77e4a602f.png)
使用 Android SDK 需求获取的配置如下：
 - **授权 ID**：使⽤移动解析 HTTPDNS 服务中，开发配置的唯⼀标识。SDK中 `dnsId` 参数，用于域名解析鉴权。
 - **DES加密密钥**：SDK中 `dnsKey` 参数，加密方式为 DES 时传入此项。
 - **AES 加密密钥**：SDK中 `dnsKey` 参数，加密方式为 AES 时传入此项。
 - **HTTPS 加密 Token**：SDK中 `token` 参数，加密方式为 HTTPS 时传入此项。
 -  **Android APPID**： [Android 端 SDK](https://cloud.tencent.com/document/product/379/78133) 的 `appkey` 鉴权信息。


## SDK 接入

### 接入 HTTPDNS SDK

1. 获取 [移动解析 Android SDK](https://github.com/tencentyun/httpdns-android-sdk)。
2. aar 包引入，将 HttpDNSLibs\HTTPDNS_ANDROID_SDK_xxxx.aar 拷贝至应用 libs 相应位置。
3. 在 App module的build.gradle 文件中，添加如下配置：
```xml
android {

    // ...

    repositories {
        flatDir {
            dirs 'libs'
        }
    }
}

dependencies {

    // ...

    implementation(name: 'HTTPDNS_Android_xxxx', ext: 'aar')

    // V4.3.0版本开始增加了本地数据存储，需增加room依赖引入
    implementation 'android.arch.persistence.room:rxjava2:2.1.1'
}
```

### 权限配置

```xml
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.INTERNET" />

<!-- 用于获取手机imei码进行数据上报，非必须 -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />

<!-- 灯塔 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

### 网络安全配置兼容

App targetSdkVersion ≥ 28(Android 9.0)的情况下，系统默认不允许 HTTP 网络请求，详情请参见 [Opt out of cleartext traffic](https://developer.android.com/training/articles/security-config#Opt%20out%20of%20cleartext%20traffic)。
这种情况下，业务侧需要将 HTTPDNS 请求使用的 IP 配置到域名白名单中。配置如下：
- AndroidManifest 文件中配置。
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest ... >
    <application android:networkSecurityConfig="@xml/network_security_config"
                    ... >
        ...
    </application>
</manifest>
```
- XML 目录下添加 network_security_config.xml 配置文件。
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="false">119.29.29.98</domain>
        <domain includeSubdomains="false">119.28.28.98</domain>
    </domain-config>
</network-security-config>
```



### 接入灯塔（可选）

将 HttpDNSLibs\beacon_android_xxxx.jar 拷贝至应用 libs 相应位置。

<dx-alert infotype="notice" title="">
- 若您已经接入了腾讯灯塔（beacon）组件的应用，请忽略此步骤。
- 灯塔（beacon）SDK 是由腾讯灯塔团队开发，用于移动应用统计分析，HTTPDNS SDK 使用灯塔（beacon）SDK 收集域名解析质量数据，辅助定位问题。
</dx-alert>

#### 接口调用
```Java

// 初始化灯塔：没使用灯塔可以忽略下面

try {
    // 注意：这里业务需要输入自己的灯塔 appkey
    UserAction.setAppKey("0I000LT6GW1YGCP7");
    UserAction.initUserAction(MainActivity.this.getApplicationContext());
} catch (Exception e) {
    Log.e(TAG, "Init beacon failed", e);
}

/**
 * 设置OpenId，已接入MSDK业务直接传 MSDK OpenId，其它业务传“NULL”
 *
 * @param String openId
 */
MSDKDnsResolver.getInstance().WGSetDnsOpenId("10000");
```
 
 
## SDK 初始化

### 初始化配置服务（4.0.0版本开始支持）
<dx-alert infotype="notice" title="">
- HTTPDNS SDK 提供多重解析优化策略，建议根据实际情况选配，也可以组合使用，可使得解析成功率达到最优效果。
- 可以通过配置 `setUseExpiredIpEnable(true)` 和 `setCachedIpEnable(true)` 来实现乐观 DNS 缓存。
  - 该功能旨在提升缓存命中率和首屏加载速度。持久化缓存会将上一次解析结果保持在本地，在 App 启动时，会优先读取到本地缓存解析结果。
  - 存在使用缓存 IP 时为过期 IP（TTL 过期），该功能启用了允许使用过期 IP，乐观的推定 TTL 过期，大多数情况下该 IP 仍能正常使用。优先返回缓存的过期结果，同时异步发起解析服务，更新缓存。
  - 乐观 DNS 缓存在首次解析域名（无缓存）时，无法命中缓存，返回0;0，同时也会异步发起解析服务，更新缓存。在启用该功能后需自行 LocalDNS 兜底。核心域名建议配置预解析服务 `preLookupDomains(String... domainList)`。
  - 如果业务服务器 IP 变化比较频繁，务必启用缓存自动刷新 `persistentCacheDomains(String... domainList)`、预解析能力 `preLookupDomains(String... domainList)`，以确保解析结果的准确性。
</dx-alert>
在获取服务实例之前，可通过初始化配置，设置服务的一些属性在 SDK 初始化时进行配置项传入。
```Java
DnsConfig dnsConfigBuilder = DnsConfig.Builder()
    //（必填）dns 解析 id，即授权 id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
    .dnsId("xxx")
    //（必填）dns 解析 key，即授权 id 对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
    .dnsKey("xxx")
    //（必填）Channel为desHttp()或aesHttp()时使用 119.29.29.98（默认填写这个就行），channel为https()时使用 119.29.29.99
    .dnsIp("xxx")
    //（可选）channel配置：基于 HTTP 请求的 DES 加密形式，默认为 desHttp()，另有 aesHttp()、https() 可选。（注意仅当选择 https 的 channel 需要选择 119.29.29.99 的dnsip并传入token，例如：.dnsIp('119.29.29.99').https().token('....') ）。
    .desHttp()
    //（可选，选择 https channel 时进行设置）腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于 HTTPS 校验。仅当选用https()时进行填写
    .token("xxx")
    //（可选）日志粒度，如开启Debug打印则传入"Log.VERBOSE"
    .logLevel(Log.VERBOSE)
    //（可选）预解析域名，填写形式："baidu.com", "qq.com"，建议不要设置太多预解析域名，当前限制为最多 10 个域名。仅在初始化时触发。
    .preLookupDomains("baidu.com", "qq.com")
    //（可选）解析缓存自动刷新, 以域名形式进行配置，填写形式："baidu.com", "qq.com"。配置的域名会在 TTL * 75% 时自动发起解析请求更新缓存，实现配置域名解析时始终命中缓存。此项建议不要设置太多域名，当前限制为最多 10 个域名。与预解析分开独立配置。
    .persistentCacheDomains("baidu.com", "qq.com")
    // (可选) IP 优选，以 IpRankItem(hostname, port) 组成的 List 配置, port（可选）默认值为 8080。例如：IpRankItem("qq.com", 443)。sdk 会根据配置项进行 socket 连接测速情况对解析 IP 进行排序，IP 优选不阻塞当前解析，在下次解析时生效。当前限制为最多 10 项。
    .ipRankItems(ipRankItemList)
    //（可选）手动指定网络栈支持情况，仅进行 IPv4 解析传 1，仅进行 IPv6 解析传 2，进行 IPv4、IPv6 双栈解析传 3。默认为根据客户端本地网络栈支持情况发起对应的解析请求。
    .setCustomNetStack(3)
    //（可选）设置是否允许使用过期缓存，默认false，解析时先取未过期的缓存结果，不满足则等待解析请求完成后返回解析结果。
    // 设置为true时，会直接返回缓存的解析结果，没有缓存则返回0;0，用户可使用localdns（InetAddress）进行兜底。且在无缓存结果或缓存已过期时，会异步发起解析请求更新缓存。因异步API（getAddrByNameAsync，getAddrsByNameAsync）逻辑在回调中始终返回未过期的解析结果，设置为true时，异步API不可使用。建议使用同步API （getAddrByName，getAddrsByName）。
    .setUseExpiredIpEnable(true)
    //（可选）设置是否启用本地缓存（Room），默认false
    .setCachedIpEnable(true)
    //（可选）设置域名解析请求超时时间，默认为1000ms
    .timeoutMills(1000)
    //（可选）是否开启解析异常上报，默认false，不上报
    .enableReport(true)
    // 以build()结束
    .build();
    
MSDKDnsResolver.getInstance().init(this, dnsConfigBuilder);
```

### 旧版本初始化
  - HTTP 协议服务地址为 `119.29.29.98`，HTTPS 协议服务地址为 `119.29.29.99`（仅当采用自选加密方式并且 `channel` 为 `Https` 时使用 `99` 的 IP）。
  - 新版本 API 更新为使用 `119.29.29.99/98` 接入，同时原移动解析 HTTPDNS 服务地址 `119.29.29.29` 仅供开发调试使用，无 SLA 保障，不建议用于正式业务，请您尽快将正式业务迁移至 `119.29.29.99/98`。
  - 具体以 [API 说明](https://cloud.tencent.com/document/product/379/54976) 提供的 IP 为准。
  - 使用 SDK 方式接入 HTTPDNS，若 HTTPDNS 未查询到解析结果，则通过 LocalDNS 进行域名解析，返回 LocalDNS 的解析结果。


### 默认使用 DES 加密
- **默认不进行解析异常上报**
```Java
// 以下鉴权信息可在腾讯云控制台（https://console.cloud.tencent.com/httpdns/configure）开通服务后获取

/**
 * 初始化 HTTPDNS（默认为 DES 加密）：如果接入了 MSDK，建议初始化 MSDK 后再初始化 HTTPDNS
 *
 * @param context 应用上下文，最好传入 ApplicationContext
 * @param appkey 业务 appkey，即 SDK AppID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权id对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnsIp 由外部传入的dnsIp，可选："119.29.29.98"，以腾讯云文档（https://cloud.tencent.com/document/product/379/54976）提供的 IP 为准
 * @param debug 是否开启 debug 日志，true 为打开，false 为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, dnsIp, debug, timeout);
```
- **手动开启异常解析上报**
```Java
// 以下鉴权信息可在腾讯云控制台（https://console.cloud.tencent.com/httpdns/configure）开通服务后获取

/**
 * 初始化 HTTPDNS（默认为 DES 加密）：如果接入了 MSDK，建议初始化 MSDK 后再初始化 HTTPDNS
 *
 * @param context 应用上下文，最好传入 ApplicationContext
 * @param appkey 业务 appkey，即 SDK AppID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权id对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnsIp 由外部传入的dnsIp，可选："119.29.29.98"（仅支持 http 请求，channel 为 DesHttp 和 AesHttp 时选择），"119.29.29.99"（仅支持 https 请求，channel为 Https 时选择）以腾讯云文档（https://cloud.tencent.com/document/product/379/54976）提供的 IP 为准
 * @param debug 是否开启 debug 日志，true 为打开，false 为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 * @param enableReport 是否开启解析异常上报，默认 false，不上报
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, dnsIp, debug, timeout, enableReport);
```
- **自选加密方式（DesHttp, AesHttp, Https）**
```Java
/**
 * 初始化 HTTPDNS（自选加密方式）：如果接入了 MSDK，建议初始化 MSDK 后再初始化 HTTPDNS
 *
 * @param context 应用上下文，最好传入 ApplicationContext
 * @param appkey 业务 appkey，即 SDK AppID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权id对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnsIp 由外部传入的dnsIp，可选："119.29.29.98"（仅支持 http 请求，channel 为 DesHttp 和 AesHttp 时选择），"119.29.29.99"（仅支持 https 请求，channel 为 Https 时选择）以腾讯云文档（https://cloud.tencent.com/document/product/379/54976）提供的 IP 为准
 * @param debug 是否开启 debug 日志，true 为打开，false 为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 * @param channel 设置 channel，可选：DesHttp（默认）, AesHttp, Https
 * @param token 腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于 HTTPS 校验
 * @param enableReport 是否开启解析异常上报，默认 false，不上报
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, dnsIp, debug, timeout, channel, token, true);
```


## SDK 接入业务方式

将 HTTPDNS SDK 的域名解析能力接入到业务的 HTTP（HTTPS）网络访问流程中，总的来说可以分为以下两种方式：

- **方式1：替换 URL**
替换 URL 中的 Host 部分得到新的 URL，并使用新的 URL 进行网络访问。
  这种实现方案下，URL 丢掉了域名的信息，对于需要使用到域名信息的网络请求，需进行较多的兼容性工作。
- **方式2：替换 DNS**
将 HTTPDNS 的域名解析能力注入到网络访问流程中，替换掉原本网络访问流程中的 LocalDNS 来实现。
  - 这种实现方案下，不需要逐个对请求的 URL 进行修改，同时由于没有修改 URL，无需进行额外的兼容性工作，但需要业务侧使用的网络库支持 DNS 实现替换。
  - DNS 替换也可以通过 Hook 系统域名解析函数的方式来实现，但 HTTPDNS SDK 内部已经使用系统的域名解析函数，Hook 系统域名解析函数可能会造成递归调用直到栈溢出。

不同网络库具体的接入方式，可以参见对应的接入文档（当前目录下）及参考使用 Sample（HttpDnsSample 目录）。


### 替换 URL 接入方式兼容
如前文所述，对于需要使用到域名信息的网络请求（一般是多个域名映射到同一个 IP 的情况），需要进行额外兼容。以下从协议层面阐述具体的兼容方式，具体的实现方式需要视网络库的实现而定。

- **HTTP 兼容**
对于 HTTP 请求，需要通过指定报文头中的 Host 字段来告知服务器域名信息。Host 字段详细介绍参见 [Host](https://tools.ietf.org/html/rfc2616#page-128)。
- **HTTPS 兼容**[](id:HTTPS)
 - HTTPS 是基于 TLS 协议之上的 HTTP 协议的统称。对于 HTTPS 请求，同样需要设置 Host 字段。
 - 在 HTTPS 请求中，需要先进行 TLS 的握手。TLS 握手过程中，服务器会将自己的数字证书发给我们用于身份认证，因此，在 TLS 握手过程中，也需要告知服务器相关的域名信息。在 TLS 协议中，通过 SNI 扩展来指明域名信息。SNI 扩展的详细介绍参见 [Server Name Indication](https://tools.ietf.org/html/rfc6066#page-6)。


### 本地使用 HTTP 代理[](id:local)

<dx-alert infotype="explain" title="">
本地使用 HTTP 代理情况下，建议**不要使用 HTTPDNS** 进行域名解析。
</dx-alert>

以下区分两种接入方式并进行分析：

- **替换 URL 接入**
根据 HTTP/1.1 协议规定，在使用 HTTP 代理情况下，客户端侧将在请求行中带上完整的服务器地址信息。详细介绍可以参见 [origin-form](https://tools.ietf.org/html/rfc7230#page-42)。
这种情况下（本地使用了 HTTP 代理，业务侧使用替换 URL 方式接入了 HTTPDNS SDK，且已经正确设置了 Host 字段），HTTP 代理接收到的 HTTP 请求中会包含服务器的 IP 信息（请求行中）以及域名信息（Host 字段中），但具体 HTTP 代理会如何向真正的目标服务器发起 HTTP 请求，则取决于 HTTP 代理的实现，可能会直接丢掉我们设置的 Host 字段使得网络请求失败。
- **替换 DNS 实现**
以 OkHttp 网络库为例，在本地启用 HTTP 代理情况下，OkHttp 网络库不会对一个 HTTP 请求 URL 中的 Host 字段进行域名解析，而只会对设置的 HTTP 代理的 Host 进行域名解析。在这种情况下，启用 HTTPDNS 没有意义。

您可通过以下代码，**判断本地是否使用 HTTP 代理**：
```kotlin
val host = System.getProperty("http.proxyHost")
val port = System.getProperty("http.proxyPort")
if (null != host && null != port) {
    // 本地使用了 HTTP 代理
}
```


## 接入验证

### 日志验证

当 init 接口中 debug 参数传入 true，过滤 TAG 为 “HTTPDNS” 的日志，并查看到 LocalDns（日志上为 ldns_ip）和 HTTPDNS（日志上为 hdns_ip）相关日志时，可以确认接入无误。
- key 为 ldns_ip 的是 LocalDNS 的解析结果。
- key 为 hdns_ip 的是 HTTPDNS A 记录的解析结果。
- key 为 hdns_4a_ips 的是 HTTPDNS AAAA 记录的解析结果。
- key 为 a_ips 的是域名解析接口返回的 IPv4 集合。
- key 为 4a_ips 的是域名解析接口返回的 IPv6 集合。


### 模拟 LocalDNS 劫持

模拟 LocalDNS 劫持情况下，若 App 能够正常工作，可以证明 HTTPDNS 已经成功接入。
<dx-alert infotype="notice" title="">
由于 LocalDNS 存在缓存机制，模拟 LocalDNS 进行接入验证时，请尽量保证 LocalDNS 的缓存已经被清理。您可以通过重启机器，切换网络等方式，尽量清除 LocalDNS 的解析缓存。验证时，请注意对照启用 LocalDNS 和启用 HTTPDNS 的效果。
</dx-alert>

- 修改机器 Hosts 文件。
  - LocalDNS 优先通过读取机器 Hosts 文件方式获取解析结果。
  - 通过修改 Hosts 文件，将对应域名指向错误的 IP，可以模拟 LocalDNS 劫持。
  - Root 机器可以直接修改机器 Hosts 文件。
- 修改 DNS 服务器配置。
  - 通过修改 DNS 服务器配置，将 DNS 服务器指向一个不可用的 IP（如局域网内的另一个 IP），可以模拟 LocalDNS 劫持。
  - 机器连接 Wi-Fi 情况下，在当前连接的 Wi-Fi 的高级设置选项中修改 IP 设置为静态设置，可以修改 DNS 服务器设置（不同机器具体的操作路径可能略有不同）。
  - 借助修改 DNS 的 App 来修改 DNS 服务器配置（通常是通过 VPN 篡改 DNS 包的方式来修改 DNS 服务器配置）。


### 抓包验证

以下以接入 HTTP 网络访问为例进行说明：
<dx-alert infotype="notice" title="">
常用的移动端 HTTP/HTTPS 抓包工具（例如 Charles/Fiddler），是通过 HTTP 代理方式进行抓包，不适用于抓包验证 HTTPDNS 服务是否生效，相关说明请参见 [本地使用 HTTP 代理](https://cloud.tencent.com/document/product/379/78134#local)。
</dx-alert>

- 使用 **tcpdump** 进行抓包。
 - Root 机器可以通过 tcpdump 命令抓包。
 - 非 Root 机器上，系统可能内置有相关的调试工具，可以获取抓包结果（不同机器具体的启用方式不同）。
- 通过 **WireShark** 观察抓包结果。
 - 对于 HTTP 请求，我们可以观察到明文信息，通过对照日志和具体的抓包记录，可以确认最终发起请求时使用的 IP 是否和 SDK 返回的一致。如下图所示：
 <img src="https://main.qcloudimg.com/raw/63464903e3861007c1c9cb2130781701.png"/>
从抓包上看，`xw.qq.com` 的请求最终发往了 IP 为 `183.3.226.35` 的服务器。
 - 对于 HTTPS 请求，TLS 的握手包实际上是明文包，在设置了 SNI 扩展（请参见 <a href="https://cloud.tencent.com/document/product/379/78134#HTTPS">HTTPS 兼容</a>）情况下，通过对照日志和具体的抓包记录，可以确认最终发起请求时使用的 IP 是否和 SDK 返回的一致。如下图所示：
 <img src="https://main.qcloudimg.com/raw/544370c87fb2d09029699fb1f0db30d9.png"/>
从抓包上看，`xw.qq.com` 的请求最终发往了 IP 为 `183.3.226.35` 的服务器。



### 注意事项

- getAddrByName 是耗时同步接口，应当在子线程调用。
- 如果客户端的业务与 HOST 绑定，例如客户端的业务绑定了 HOST 的 HTTP 服务或者是 CDN 的服务，那么您将 URL 中的域名替换成 HTTPDNS 返回的 IP 之后，还需要指定下 HTTP 头的 HOST 字段。
 - 以 URLConnection 为例：
```Java
URL oldUrl = new URL(url);
URLConnection connection = oldUrl.openConnection();
// 获取HTTPDNS域名解析结果 
String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
String[] ipArr = ips.split(";");
if (2 == ipArr.length && !"0".equals(ipArr[0])) { // 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
    String ip = ipArr[0];
    String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
    connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置 HTTP 请求头 Host 域名
    connection.setRequestProperty("Host", oldUrl.getHost());
}
```
 - 以 curl 为例，假设您想要访问 `www.qq.com`，通过 HTTPDNS 解析出来的 IP 为 `192.168.0.111`，则访问方式如下：
```shell
curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt
```
- 检测本地是否使用了 HTTP 代理。如果使用了 HTTP 代理，建议**不要使用 HTTPDNS** 做域名解析。示例如下：
```Java
String host = System.getProperty("http.proxyHost");
String port= System.getProperty("http.proxyPort");
if (null != host && null != port) {
    // 使用了本地代理模式
}
```
