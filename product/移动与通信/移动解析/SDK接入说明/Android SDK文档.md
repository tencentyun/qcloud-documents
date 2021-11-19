## 概述
总的来说，移动解析 HTTPDNS 作为移动互联网时代 DNS 优化的一个通用解决方案，主要解决了以下几类问题：
- LocalDNS 劫持/故障
- LocalDNS 调度不准确

移动解析 HTTPDNS 的 Android SDK，主要提供了基于移动解析 HTTPDNS 服务的域名解析和缓存管理能力：
- SDK 在进行域名解析时，优先通过移动解析 HTTPDNS 服务得到域名解析结果，极端情况下如果移动解析 HTTPDNS 服务不可用，则使用 LocalDNS 解析结果。
- 移动解析 HTTPDNS 服务返回的域名解析结果会携带相关的 TTL 信息，SDK 会使用该信息进行移动解析 HTTPDNS 解析结果的缓存管理。

移动解析 HTTPDNS 服务的详细介绍可以参见文章 [全局精确流量调度新思路-HTTPDNS 服务详解](https://cloud.tencent.com/developer/article/1035562)。
智营解析 Android SDK 的获取方式：[点此获取](https://github.com/tencentyun/httpdns-android-sdk)。

## 前期准备
1. 首先需要开通移动解析 HTTPDNS 服务，请前往 [移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 开通。具体操作请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。
2. 开通移动解析 HTTPDNS 服务后，您需在移动解析 HTTPDNS 控制台添加解析域名后才可正常使用。具体操作请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。
3. 已在移动解析 HTTPDNS 控制台 [开通 SDK](https://cloud.tencent.com/document/product/379/12544)。
4. 开通服务后，移动解析 HTTPDNS 将为您分配授权 ID、AES 和 DES 加密密钥及 HTTPS Token 等配置信息。使用 Android SDK 需求获取的配置如下：
![](https://main.qcloudimg.com/raw/9de378622bacb7ce9f67bcf77e4a602f.png)
 - **授权 ID**：使⽤移动解析 HTTPDNS 服务中，开发配置的唯⼀标识。SDK中 `dnsId` 参数，用于域名解析鉴权。
 - **DES 加密密钥**：SDK中 `dnsKey` 参数，加密方式为 DES 时传入此项。
 - **AES 加密密钥**：SDK中 `dnsKey` 参数，加密方式为 AES 时传入此项。
 - **HTTPS 加密 Token**：SDK中 `token` 参数，加密方式为 HTTPS 时传入此项。
 -  **Android APPID**： [Android 端 SDK](https://cloud.tencent.com/document/product/379/17655) 的 `appkey` 鉴权信息。

## 接入
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

App targetSdkVersion >= 28(Android 9.0)情况下，系统默认不允许 HTTP 网络请求，详细信息参见 [Opt out of cleartext traffic](https://developer.android.com/training/articles/security-config#Opt%20out%20of%20cleartext%20traffic)。
这种情况下，业务侧需要将 HTTPDNS 请求使用的 IP 配置到域名白名单中：
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
        <domain includeSubdomains="false">119.29.29.99</domain>
        <domain includeSubdomains="false">119.29.29.98</domain>
    </domain-config>
</network-security-config>
```

### 接入 HTTPDNS
将 HttpDNSLibs\HTTPDNS_ANDROID_SDK_xxxx.aar 拷贝至应用 libs 相应位置。

### 接入灯塔（可选）

将 HttpDNSLibs\beacon_android_xxxx.jar 拷贝至应用 libs 相应位置。
>! 
>- 若您已经接入了腾讯灯塔（beacon）组件的应用，请忽略此步骤。
>- 灯塔（beacon）SDK 是由腾讯灯塔团队开发，用于移动应用统计分析，HTTPDNS SDK 使用灯塔（beacon）SDK 收集域名解析质量数据，辅助定位问题。

### 接口调用
```Java

// 初始化灯塔：如果已经接入 MSDK 或者 IMSDK 或者单独接入了腾讯灯塔（Beacon）则不需再初始化该接口
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
 
### SDK 初始化

>?
- HTTP 协议服务地址为 `119.29.29.98`，https 协议服务地址为 `119.29.29.99`。
- 新版本 API 更新为使用 `119.29.29.99/98` 接入，同时原移动解析 HTTPDNS 服务地址 `119.29.29.29` 仅供开发调试使用，无 SLA 保障，不建议用于正式业务，请您尽快将正式业务迁移至 `119.29.29.99/98`。
- 具体以 [API 说明](https://cloud.tencent.com/document/product/379/54976) 提供的 IP 为准。
- 使用 SDK 方式接入 HTTPDNS，若 HTTPDNS 未查询到解析结果，则通过 LocalDNS 进行域名解析，返回 LocalDNS 的解析结果。

#### 默认使用 DES 加密

```Java
// 以下鉴权信息可在腾讯云控制台（https://console.cloud.tencent.com/httpdns/configure）开通服务后获取

/**
 * 初始化 HTTPDNS（默认为 DES 加密）：如果接入了 MSDK，建议初始化 MSDK 后再初始化 HTTPDNS
 *
 * @param context 应用上下文，最好传入 ApplicationContext
 * @param appkey 业务 appkey，即 SDK AppID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权id对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnsIp 由外部传入的dnsIp，可选："119.29.29.98"（仅支持 http 请求），"119.29.29.99"（仅支持 https 请求）以腾讯云文档（https://cloud.tencent.com/document/product/379/54976）提供的 IP 为准
 * @param debug 是否开启 debug 日志，true 为打开，false 为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, dnsIp, debug, timeout);
```

#### 自选加密方式（DesHttp, AesHttp, Https）
```Java
/**
 * 初始化 HTTPDNS（自选加密方式）：如果接入了 MSDK，建议初始化 MSDK 后再初始化 HTTPDNS
 *
 * @param context 应用上下文，最好传入 ApplicationContext
 * @param appkey 业务 appkey，即 SDK AppID，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于上报
 * @param dnsid dns解析id，即授权id，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnskey dns解析key，即授权id对应的 key（加密密钥），在申请 SDK 后的邮箱里，腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于域名解析鉴权
 * @param dnsIp 由外部传入的dnsIp，可选："119.29.29.98"（仅支持 http 请求），"119.29.29.99"（仅支持 https 请求）以腾讯云文档（https://cloud.tencent.com/document/product/379/54976）提供的 IP 为准
 * @param debug 是否开启 debug 日志，true 为打开，false 为关闭，建议测试阶段打开，正式上线时关闭
 * @param timeout dns请求超时时间，单位ms，建议设置1000
 * @param channel 设置 channel，可选：DesHttp（默认）, AesHttp, Https
 * @param token 腾讯云官网（https://console.cloud.tencent.com/httpdns）申请获得，用于 HTTPS 校验
 */
MSDKDnsResolver.getInstance().init(MainActivity.this, appkey, dnsid, dnskey, dnsIp, debug, timeout, channel, token);
```

### 接口调用
```Java

/**
 * HTTPDNS 同步解析接口
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成返回最新解析结果
 * 返回值字符串以“;”分隔，“;”前为解析得到的 IPv4 地址（解析失败填“0”），“;”后为解析得到的 IPv6 地址（解析失败填“0”）
 * 返回示例：121.14.77.221;2402:4e00:1020:1404:0:9227:71a3:83d2
 * @param domain 域名（如www.qq.com）
 * @return 域名对应的解析 IP 结果集合
 */
String ips = MSDKDnsResolver.getInstance().getAddrByName(domain);

/**
 * HTTPDNS 同步解析接口（批量查询）
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成返回最新解析结果
 * 返回值 ipSet 即解析得到的 IP 集合
 * ipSet.v4Ips 为解析得到 IPv4 集合, 可能为 null
 * ipSet.v6Ips 为解析得到 IPv6 集合, 可能为 null
 * 单独域名返回结果示例：IpSet{v4Ips=[121.14.77.201, 121.14.77.221], v6Ips=[2402:4e00:1020:1404:0:9227:71ab:2b74, 2402:4e00:1020:1404:0:9227:71a3:83d2], ips=null}
 * 多域名返回结果示例：IpSet{v4Ips=[www.baidu.com:14.215.177.39, www.baidu.com:14.215.177.38, www.youtube.com:104.244.45.246], v6Ips=[www.youtube.com.:2001::1f0:5610], ips=null}
 * @param domain 支持多域名，域名以“,”分割，例如：qq.com,baidu.com
 * @return 域名对应的解析 IP 结果集合
 */
Ipset ips = MSDKDnsResolver.getInstance().getAddrsByName(domain);


//  异步回调，注意所有异步请求需配合异步回调使用
MSDKDnsResolver.getInstance().setHttpDnsResponseObserver(new HttpDnsResponseObserver() {
    @Override
    public void onHttpDnsResponse(String tag, String domain, Object ipResultSemicolonSep) {
        long elapse = (System.currentTimeMillis() - Long.parseLong(tag));
        String lookedUpResult = "[[getAddrByNameAsync]]:ASYNC:::" + ipResultSemicolonSep +
                ", domain:" + domain +  ", tag:" + tag +
                ", elapse:" + elapse;
    }
});

/**
 * HTTPDNS 异步解析接口（需配合异步回调使用）
 * 首先查询缓存，若存在则返回结果，若不存在则进行异步域名解析请求
 * 解析完成会在异步回调返回最新解析结果
 * @param domain 域名（如www.qq.com）
 */
MSDKDnsResolver.getInstance()
    .getAddrByNameAsync(hostname, String.valueOf(System.currentTimeMillis()))

/**
 * HTTPDNS 异步解析接口（批量查询，需配合异步回调使用）
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成会在异步回调返回最新解析结果
 * @param domain 支持多域名，域名以“,”分割，例如：qq.com,baidu.com
 */
MSDKDnsResolver.getInstance()
    .getAddrsByNameAsync(hostname, String.valueOf(System.currentTimeMillis()))
```

### 接入验证

#### 日志验证

当 init 接口中 debug 参数传入 true，过滤 TAG 为 “HTTPDNS” 的日志，并查看到 LocalDns（日志上为 ldns_ip）和 HTTPDNS（日志上为 hdns_ip）相关日志时，可以确认接入无误。
- key 为 ldns_ip 的是 LocalDNS 的解析结果。
- key 为 hdns_ip 的是 HTTPDNS A 记录的解析结果。
- key 为 hdns_4a_ips 的是 HTTPDNS AAAA 记录的解析结果。
- key 为 a_ips 的是域名解析接口返回的 IPv4 集合。
- key 为 4a_ips 的是域名解析接口返回的 IPv6 集合。

#### 模拟 LocalDNS 劫持

模拟 LocalDNS 劫持情况下，如果 App 能够正常工作，可以证明 HTTPDNS 已经成功接入。
>!由于 LocalDNS 存在缓存机制，模拟 LocalDNS 进行接入验证时，请尽量保证 LocalDNS 的缓存已经被清理，您可以通过重启机器，切换网络等方式，尽量清除 LocalDNS 的解析缓存；验证时，请注意对照启用 LocalDNS 和启用 HTTPDNS 的效果。
>
- 修改机器 Hosts 文件。
  - LocalDNS 优先通过读取机器 Hosts 文件方式获取解析结果。
  - 通过修改 Hosts 文件，将对应域名指向错误的 IP，可以模拟 LocalDNS 劫持。
  - Root 机器可以直接修改机器 Hosts 文件。
- 修改 DNS 服务器配置。
  - 通过修改 DNS 服务器配置，将 DNS 服务器指向一个不可用的 IP（如局域网内的另一个 IP），可以模拟 LocalDNS 劫持。
  - 机器连接 Wi-Fi 情况下，在当前连接的 Wi-Fi 的高级设置选项中修改 IP 设置为静态设置，可以修改 DNS 服务器设置（不同机器具体的操作路径可能略有不同）。
  - 借助修改 DNS 的 App 来修改 DNS 服务器配置（通常是通过 VPN 篡改 DNS 包的方式来修改 DNS 服务器配置）。

#### 抓包验证

以下以接入 HTTP 网络访问为例进行说明：
- 使用 **tcpdump** 进行抓包。
>!常用的移动端 HTTP/HTTPS 抓包工具（例如 Charles/Fiddler），是通过 HTTP 代理方式进行抓包，不适用于抓包验证 HTTPDNS 服务是否生效，相关说明请参见 [本地使用 HTTP 代理](#local)。
>
  - Root 机器可以通过 tcpdump 命令抓包。
  - 非 Root 机器上，系统可能内置有相关的调试工具，可以获取抓包结果（不同机器具体的启用方式不同）。
- 通过 **WireShark** 观察抓包结果。
  - 对于 HTTP 请求，我们可以观察到明文信息，通过对照日志和具体的抓包记录，可以确认最终发起请求时使用的 IP 是否和 SDK 返回的一致。如下图所示： 
![](https://main.qcloudimg.com/raw/63464903e3861007c1c9cb2130781701.png)
从抓包上看，`xw.qq.com` 的请求最终发往了 IP 为 `183.3.226.35` 的服务器。
  - 对于 HTTPS 请求，TLS 的握手包实际上是明文包，在设置了 SNI 扩展（请参见 [HTTPS 兼容](#HTTPS)）情况下，通过对照日志和具体的抓包记录，可以确认最终发起请求时使用的 IP 是否和 SDK 返回的一致。如下图所示：
![](https://main.qcloudimg.com/raw/544370c87fb2d09029699fb1f0db30d9.png)
    从抓包上看，`xw.qq.com` 的请求最终发往了 IP 为 `183.3.226.35` 的服务器。


### 注意事项
- getAddrByName 是耗时同步接口，应当在子线程调用。
- 如果客户端的业务与 HOST 绑定，例如，客户端的业务绑定了 HOST 的 HTTP 服务或者是 CDN 的服务，那么您将 URL 中的域名替换成 HTTPDNS 返回的 IP 之后，还需要指定下 HTTP 头的 HOST 字段。
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
 - 以 curl 为例，假设您想要访问 `www.qq.com`，通过 HTTPDNS 解析出来的 IP 为 `192.168.0.111`，那么您可以这么访问：
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

## HTTPDNS SDK 接入 HTTP 网络访问实践

将 HTTPDNS SDK 的域名解析能力接入到业务的 HTTP（HTTPS）网络访问流程中，总的来说可以分为两种方式：

- 替换 URL 中的 Host 部分得到新的 URL，并使用新的 URL 进行网络访问。
  这种实现方案下，URL 丢掉了域名的信息，对于需要使用到域名信息的网络请求，需要做比较多的兼容性工作。
- 将 HTTPDNS 的域名解析能力注入到网络访问流程中，替换掉原本网络访问流程中的 LocalDNS 来实现。
  - 这种实现方案下，不需要逐个对请求的 URL 进行修改，同时由于没有修改 URL，不需要做额外的兼容性工作，但需要业务侧使用的网络库支持 DNS 实现替换。
  - 单纯针对 DNS 替换这个思路，也可以通过 Hook 系统域名解析函数的方式来实现，但是 HTTPDNS SDK 内部已经使用系统的域名解析函数，Hook 系统域名解析函数可能会造成递归调用直到栈溢出。

不同网络库具体的接入方式，可以参见对应的接入文档（当前目录下）及参考使用 Sample（HttpDnsSample 目录）。

### 替换 URL 接入方式兼容
如前文所述，对于需要使用到域名信息的网络请求（一般是多个域名映射到同一个 IP 的情况），我们需要进行额外兼容。以下从协议层面阐述具体的兼容方式，具体的实现方式需要视网络库的实现而定。

#### HTTP 兼容
对于 HTTP 请求，我们需要通过指定报文头中的 Host 字段来告知服务器域名信息。Host 字段详细介绍参见 [Host](https://tools.ietf.org/html/rfc2616#page-128)。

#### HTTPS 兼容[](id:HTTPS)
- HTTPS 是基于 TLS 协议之上的 HTTP 协议的统称，因此对于 HTTPS 请求，我们同样需要设置 Host 字段。
- 在 HTTPS 请求中，我们需要先进行 TLS 的握手。TLS 握手过程中，服务器会将自己的数字证书发给我们用于身份认证，因此，在 TLS 握手过程中，我们也需要告知服务器相关的域名信息；在 TLS 协议中，我们通过 SNI 扩展来指明域名信息。SNI 扩展的详细介绍参见 [Server Name Indication](https://tools.ietf.org/html/rfc6066#page-6)。

### 本地使用 HTTP 代理[](id:local)
本地使用 HTTP 代理情况下，建议**不要使用 HTTPDNS** 进行域名解析。
以下区分两种接入方式并进行分析：

#### 替换 URL 接入方式
根据 HTTP/1.1 协议规定，在使用 HTTP 代理情况下，客户端侧将在请求行中带上完整的服务器地址信息。详细介绍可以参见 [origin-form](https://tools.ietf.org/html/rfc7230#page-42)。
这种情况下（本地使用了 HTTP 代理，业务侧使用替换 URL 方式接入了 HTTPDNS SDK，且已经正确设置了 Host 字段），HTTP 代理接收到的 HTTP 请求中会包含服务器的 IP 信息（请求行中）以及域名信息（Host 字段中），但具体 HTTP 代理会如何向真正的目标服务器发起 HTTP 请求，则取决于 HTTP 代理的实现，可能会直接丢掉我们设置的 Host 字段使得网络请求失败。

#### 替换 DNS 实现方式
以 OkHttp 网络库为例，在本地启用 HTTP 代理情况下，OkHttp 网络库不会对一个 HTTP 请求 URL 中的 Host 字段进行域名解析，而只会对设置的 HTTP 代理的 Host 进行域名解析。在这种情况下，启用 HTTPDNS 没有意义。

#### 判断本地是否使用 HTTP 代理
判断代码如下：

```kotlin
val host = System.getProperty("http.proxyHost")
val port = System.getProperty("http.proxyPort")
if (null != host && null != port) {
    // 本地使用了 HTTP 代理
}
```

## 实践场景

### OkHttp

OkHttp 提供了 DNS 接口，用于向 OkHttp 注入 DNS 实现。得益于 OkHttp 的良好设计，使用 OkHttp 进行网络访问时，实现 DNS 接口即可接入 HTTPDNS 进行域名解析，在较复杂场景（HTTP/HTTPS + SNI）下也不需要做额外处理，侵入性极小。示例如下：

```Java
mOkHttpClient =
    new OkHttpClient.Builder()
        .dns(new Dns() {
            @NonNull
            @Override
            public List<InetAddress> lookup(String hostname) {
                Utils.checkNotNull(hostname, "hostname can not be null");
                String ips = MSDKDnsResolver.getInstance().getAddrByName(hostname);
                String[] ipArr = ips.split(";");
                if (0 == ipArr.length) {
                    return Collections.emptyList();
                }
                List<InetAddress> inetAddressList = new ArrayList<>(ipArr.length);
                for (String ip : ipArr) {
                    if ("0".equals(ip)) {
                        continue;
                    }
                    try {
                        InetAddress inetAddress = InetAddress.getByName(ip);
                        inetAddressList.add(inetAddress);
                    } catch (UnknownHostException ignored) {
                    }
                }
                return inetAddressList;
            }
        })
        .build();
```

>! 实现 DNS 接口，即表示所有经由当前 OkHttpClient 实例处理的网络请求都会经过 HTTPDNS。如果您只有少部分域名是需要通过 HTTPDNS 进行解析，建议您在调用 HTTPDNS 域名解析接口之前先进行过滤。

### Retrofit + OkHttp
Retrofit 实际上是一个基于 OkHttp，对接口做了一层封装桥接的 lib。因此只需要仿 OkHttp 的接入方式，定制 Retrofit 中的 OkHttpClient，即可方便地接入 HTTPDNS。示例如下：
```Java
mRetrofit =
    new Retrofit.Builder()
        .client(mOkHttpClient)
        .baseUrl(baseUrl)
        .build();
```

### WebView

Android 系统提供了 API 以实现 WebView 中的网络请求拦截与自定义逻辑注入。我们可以通过该 API 拦截 WebView 的各类网络请求，截取 URL 请求的 HOST，调用 HTTPDNS 解析该 HOST，通过得到的 IP 组成新的 URL 来进行网络请求。示例如下：
```Java
mWebView.setWebViewClient(new WebViewClient() {
    // API 21及之后使用此方法
    @SuppressLint("NewApi")
    @Override
    public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
        if (request != null && request.getUrl() != null && request.getMethod().equalsIgnoreCase("get")) {
            String scheme = request.getUrl().getScheme().trim();
            String url = request.getUrl().toString();
            Log.d(TAG, "url:" + url);
            // HTTPDNS 解析 css 文件的网络请求及图片请求
            if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
            && (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url .endsWith(".gif"))) {
                try {
                    URL oldUrl = new URL(url);
                    URLConnection connection = oldUrl.openConnection();
                    // 获取 HTTPDNS 域名解析结果
                    String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
                    String[] ipArr = ips.split(";");
                    if (2 == ipArr.length && !"0".equals(ipArr[0])) { // 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
                        String ip = ipArr[0];
                        String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
                        connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置 HTTP 请求头 Host 域名
                        connection.setRequestProperty("Host", oldUrl.getHost());
                    }
                    Log.d(TAG, "contentType:" + connection.getContentType());
                    return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    // API 11至 API20使用此方法
    public WebResourceResponse shouldInterceptRequest(WebView view, String url) {
        if (!TextUtils.isEmpty(url) && Uri.parse(url).getScheme() != null) {
            String scheme = Uri.parse(url).getScheme().trim();
            Log.d(TAG, "url:" + url);
            // HTTPDNS 解析 css 文件的网络请求及图片请求
            if ((scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
            && (url.contains(".css") || url.endsWith(".png") || url.endsWith(".jpg") || url.endsWith(".gif"))) {
                try {
                    URL oldUrl = new URL(url);
                    URLConnection connection = oldUrl.openConnection();
                    // 获取 HTTPDNS 域名解析结果
                    String ips = MSDKDnsResolver.getInstance().getAddrByName(oldUrl.getHost());
                    String[] ipArr = ips.split(";");
                    if (2 == ipArr.length && !"0".equals(ipArr[0])) { // 通过 HTTPDNS 获取 IP 成功，进行 URL 替换和 HOST 头设置
                        String ip = ipArr[0];
                        String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
                        connection = (HttpURLConnection) new URL(newUrl).openConnection(); // 设置 HTTP 请求头 Host 域名
                        connection.setRequestProperty("Host", oldUrl.getHost());
                    }
                    Log.d(TAG, "contentType:" + connection.getContentType());
                    return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                }
            }
        }
        return null;
    }});
// 加载web资源
mWebView.loadUrl(targetUrl);
```

### HttpURLConnection

- HTTPS 示例如下：
```Java
 // 以域名为 www.qq.com，HTTPDNS 解析得到的 IP 为192.168.0.1为例
String url = "https://192.168.0.1/"; // 业务自己的请求连接
 HttpsURLConnection connection = (HttpsURLConnection) new URL(url).openConnection();
 connection.setRequestProperty("Host", "www.qq.com");
 connection.setHostnameVerifier(new HostnameVerifier() {
 	@Override
 	public boolean verify(String hostname, SSLSession session) {
 		return HttpsURLConnection.getDefaultHostnameVerifier().verify("www.qq.com", session);
 	}
 });
 connection.setConnectTimeout(mTimeOut); // 设置连接超时
 connection.setReadTimeout(mTimeOut); // 设置读流超时
 connection.connect();
```
- HTTPS + SNI 示例如下：
```Java
 // 以域名为 www.qq.com，HttpDNS 解析得到的 IP 为192.168.0.1为例
 String url = "https://192.168.0.1/"; // 用 HTTPDNS 解析得到的 IP 封装业务的请求 URL
 HttpsURLConnection sniConn = null;
 try {
 	sniConn = (HttpsURLConnection) new URL(url).openConnection();
 	// 设置HTTP请求头Host域
 	sniConn.setRequestProperty("Host", "www.qq.com");
 	sniConn.setConnectTimeout(3000);
 	sniConn.setReadTimeout(3000);
 	sniConn.setInstanceFollowRedirects(false);
 	// 定制SSLSocketFactory来带上请求域名 ***关键步骤
 	SniSSLSocketFactory sslSocketFactory = new SniSSLSocketFactory(sniConn);
 	sniConn.setSSLSocketFactory(sslSocketFactory);
 	// 验证主机名和服务器验证方案是否匹配
 	HostnameVerifier hostnameVerifier = new HostnameVerifier() {
 		@Override
 		public boolean verify(String hostname, SSLSession session) {
 			return HttpsURLConnection.getDefaultHostnameVerifier().verify("原解析的域名", session);
 		}
 	};
 	sniConn.setHostnameVerifier(hostnameVerifier);
 	...
 } catch (Exception e) {
 	Log.w(TAG, "Request failed", e);
 } finally {
 	if (sniConn != null) {
 		sniConn.disconnect();
 	}
 }

 class SniSSLSocketFactory extends SSLSocketFactory {
 
 	private HttpsURLConnection mConn;

 	public SniSSLSocketFactory(HttpsURLConnection conn) {
 		mConn = conn;
 	}

 	@Override
 	public Socket createSocket() throws IOException {
 		return null;
 	}

 	@Override
 	public Socket createSocket(String host, int port) throws IOException, UnknownHostException {
 		return null;
 	}

 	@Override
 	public Socket createSocket(String host, int port, InetAddress localHost, int localPort) throws IOException, UnknownHostException {
 		return null;
 	}

 	@Override
 	public Socket createSocket(InetAddress host, int port) throws IOException {
 		return null;
 	}

 	@Override
 	public Socket createSocket(InetAddress address, int port, InetAddress localAddress, int localPort) throws IOException {
 		return null;
 	}

 	@Override
 	public String[] getDefaultCipherSuites() {
 		return new String[0];
 	}

 	@Override
 	public String[] getSupportedCipherSuites() {
 		return new String[0];
 	}

 	@Override
 	public Socket createSocket(Socket socket, String host, int port, boolean autoClose) throws IOException {
 		String realHost = mConn.getRequestProperty("Host");
 		if (realHost == null) {
 			realHost = host;
 		}
 		Log.i(TAG, "customized createSocket host is: " + realHost);
 		InetAddress address = socket.getInetAddress();
 		if (autoClose) {
 			socket.close();
 		}
 		SSLCertificateSocketFactory sslSocketFactory = (SSLCertificateSocketFactory) SSLCertificateSocketFactory.getDefault(0);
 		SSLSocket ssl = (SSLSocket) sslSocketFactory.createSocket(address, port);
 		ssl.setEnabledProtocols(ssl.getSupportedProtocols());
 		if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
 			Log.i(TAG, "Setting SNI hostname");
 			sslSocketFactory.setHostname(ssl, realHost);
 		} else {
 			Log.d(TAG, "No documented SNI support on Android < 4.2, trying with reflection");
 			try {
 				Method setHostnameMethod = ssl.getClass().getMethod("setHostname", String.class);
 				setHostnameMethod.invoke(ssl, realHost);
 			} catch (Exception e) {
 				Log.w(TAG, "SNI not useable", e);
 			}
 		}
 		// verify hostname and certificate
 		SSLSession session = ssl.getSession();
 		HostnameVerifier hostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();
 		if (!hostnameVerifier.verify(realHost, session)) {
 			throw new SSLPeerUnverifiedException("Cannot verify hostname: " + realHost);
 		}			
 		Log.i(TAG, "Established " + session.getProtocol() + " connection with " + session.getPeerHost() + " using " + session.getCipherSuite());
 		return ssl;
 	}
 }
```

### Unity

- 初始化 HTTPDNS 和灯塔接口
>! 若已接入 msdk 或者单独接入了腾讯灯塔则不用初始化灯塔。
>
	示例如下：
```C#
 private static AndroidJavaObject sHttpDnsObj;
 public static void Init() {
 	AndroidJavaClass unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
 	if (unityPlayerClass == null) {
 		return;
 	}	
 	AndroidJavaObject activityObj = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
 	if (activityObj == null) {
 		return;
 	}
 	AndroidJavaObject contextObj = activityObj.Call<AndroidJavaObject>("getApplicationContext");
 	// 初始化 HTTPDNS
 	AndroidJavaObject httpDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
 	if (httpDnsClass == null) {
 		return;
 	}
 	sHttpDnsObj = httpDnsClass.CallStatic<AndroidJavaObject>("getInstance");
 	if (sHttpDnsObj == null) {
 		return;
 	}
 	sHttpDnsObj.Call("init", contextObj, appkey, dnsid, dnskey, debug, timeout);
 }
```
- 调用 getAddrByName 接口解析域名。示例如下：
```C#
// 该操作建议在子线程中或使用 Coroutine 处理
// 注意在子线程中调用需要在调用前后做 AttachCurrentThread 和 DetachCurrentThread 处理 
public static string GetHttpDnsIP(string url) {
	string ip = string.Empty;
	AndroidJNI.AttachCurrentThread(); // 子线程中调用需要加上
	// 解析得到 IP 配置集合
	string ips = sHttpDnsObj.Call<string>("getAddrByName", url);
	AndroidJNI.DetachCurrentThread(); // 子线程中调用需要加上
	if (null != ips) {
		string[] ipArr = ips.Split(';');
        if (2 == ipArr.Length && !"0".Equals(ipArr[0]))
		ip = ipArr[0];
	}
	return ip;
}
```
	
	
