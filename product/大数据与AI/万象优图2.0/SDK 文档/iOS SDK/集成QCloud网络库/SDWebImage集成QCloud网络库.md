>! SDK 版本需要大于等于 v1.5.0。

万象SDK自定义了 CIDownloader 嵌入 SDWebImage 中，接管图片加载网络层，并新增了如下功能：

1. 在网络层新增了 HTTPDNS，有效避免由于运营商传统 LocalDNS 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。
2. 在网络层接入 QUIC，提升弱网加载图片成功率，增强用户体验。
3. SDK内部增加了重试机制，并支持自定义重试次数以及重试间隔时间，用于降低因为网络波动造成图片加载失败的风险。
4. 若项目中使用到 TPG 或 AVIF 图片，可开启原图保护策略，若 TPG、AVIF 图加载失败，可自动加载原格式图片，从而不影响用户使用。并将错误信息收集用于排查失败原因并及时修复。
5. 自定义加载图片并发数。

接下来逐一介绍每个功能的详细使用，以及示例代码：

### 接入CIDownloader

接入 CIDownloader 只需在 Podfile 新增 CIDownloader 的依赖即可。
```
pod 'CloudInfinite/CIDownloader'
```
SDK 内部自动检测是否有该类，并加入到 SDWebImage loader 管理器中。

动态配置是否使用 CIDownloader，默认只接管 TPG、AVIF 图片请求。
```
[CIImageDownloader sharedDownloader].canUseCIImageDownloader = ^BOOL(NSURL * _Nonnull url, SDWebImageOptions options, SDWebImageContext * _Nonnull context) {
/// 业务判断是否使用 CIImageDownloader 加载图片，还是 SDWebImage 自带 loader 加载图片
    return YES;
};
```
 
### 接入HTTPDNS

万象SDK提供两种方式接入HTTPDNS：
1. 使用自定义HTTPDNS解析。

    使用自定义HTTPDNS解析，需要自定义类并实现 `QCloudHTTPDNSProtocol` 协议。
    ```
    @interface MyHTTPDNSHandler ()<QCloudHTTPDNSProtocol>
    @end

    @implementation MyHTTPDNSHandler
    -(NSString *)resolveDomain:(NSString *)domain{
        NSString * ipString = ... // 自己实现 dns 解析。
        return ipString;
    }
    @end
    ```
    将该类对象设置给 `[QCloudHttpDNS shareDNS].delegate`。
    ```
    self.handler = [MyHTTPDNSHandler new];
    [QCloudHttpDNS shareDNS].delegate = self.handler;
    ```

2. 使用万象自带的 CIDNS。

    接入 CIDNS 首先需要在 Podfile 中添加：
    ```
    pod 'CloudInfinite/CIDNS'
    ```

    >? CIDNS 封装了腾讯 HTTPDNS，接入 CIDNS 需要在腾讯 HTTPDNS 申请密钥相关信息，具体请查[HTTPDNS 接入文档](https://cloud.tencent.com/document/product/379/77755)。
    ```
    /// 配置 Dnsconfig。
    /// 参数含义请查看https://cloud.tencent.com/document/product/379/77755。
    DnsConfig config;
    config.appId = @"appid";
    config.dnsIp = @"dnsIp";
    config.dnsId = dnsId;
    config.dnsKey = @"dnsKey";//des 的密钥
    config.encryptType = HttpDnsEncryptTypeDES;
    config.debug = YES;
    config.timeout = 5000;
    /// 实例化 CIDNSLoader 。注意 [QCloudHttpDNS shareDNS].delegate 为弱引用，dnsloader 需一个强引用持有，否则 dnsloader 会提前释放。
    self.dnsloader = [[CIDNSLoader alloc] initWithConfig:config];
    /// 将代理 dnsloader 设置给 [QCloudHttpDNS shareDNS].delegate。
    [QCloudHttpDNS shareDNS].delegate = self;
    ```

### 接入 QUIC
>?若使用 QUIC，请点击[这里](https://cloud.tencent.com/document/product/436/37708)联系技术人员添加白名单。

1. 接入 QUIC，首先需要在 Podfile 文件中添加 Quic。
    ```
    pod 'CloudInfinite/Quic'
    ```

2. 开启 QUIC 以及配置。
    ```
    /// 启用 QUIC
    [CIImageDownloader sharedDownloader].enableQuic = YES;

    /// 配置 QUIC 白名单，指定那些 host 使用 QUIC，若不配置，则认为CIImageDownloader 全部请求都走 QUIC。
    [CIImageDownloader sharedDownloader].quicWhiteList = @[@"test.***.com"];

    /// QUIC 高级配置，具体查看 QCloudQuicConfig 类。
    [QCloudQuicConfig shareConfig].race_type = QCloudRaceTypeQUICHTTP;
    ```

### 配置重试策略
CIImageDownloader 支持重试，默认重试次数3，间隔1s。
1. 配置重试次数以及间隔时间。
    ```
    /// 设置重试2次。
    [CIImageDownloader sharedDownloader].retryCount = 2;
    /// 每次重试间隔时间2s。
    [CIImageDownloader sharedDownloader].sleepTime = 2;
    ```

2. 自定义是否重试策略。
    ```
    [CIImageDownloader sharedDownloader].canUseRetryWhenError = ^BOOL(QCloudURLSessionTaskData * _Nonnull task, NSError * _Nonnull error) {
        return YES;
    };
    ```

### 设置请求图片并发数
CIImageDownloader 支持设置请求图片并发数量。
customConcurrentCount 为当前并发数量，SDK内部根据网络状况自动增加或降低并发数量，最小为1，最大为 maxConcurrentCount。

```
[CIImageDownloader sharedDownloader].customConcurrentCount = 3;
[CIImageDownloader sharedDownloader].maxConcurrentCount = 10;
```

### 加载 TPG、AVIF 失败后请求原图重试
当 TPG、AVIF 图片加载失败时，自动请求原格式图片，提升用户体验。并将 TPG、AVIF 加载失败原因返回，用于排查失败原因及时修复。

1. 开启失败后原图重试功能。
    ```
    [UIView setLoadOriginalImageWhenError:YES];
    ```

2. 自定义 TPG、AVIF 链接转换原格式图片链接。
    ```
    [UIView setLoadTPGAVIFImageErrorHandler:^NSString * _Nullable(NSString * _Nonnull url) {
        // 将 TPG、AVIF 图片链接装换位原格式图片。
        return url;
    }];
    ```

3. 添加 TPG、AVIF 加载失败监听，获取 url 以及错误信息，可以用于日志上报以及排查原因。

    ```
    [UIView setTPGAVIFImageErrorObserver:^(NSString * _Nonnull url, NSError * _Nonnull error) {
    // 加载 TPG、AVIF 图片报错时回调，返回链接以及对应的错误信息 
    }];
    ```

