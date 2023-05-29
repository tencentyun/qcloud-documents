## 接管SDWebImage网络层

>! SDK 版本需要大于等于 v1.5.0。

万象SDK自定义了CIDownloader嵌入SDWebImage中，接管图片加载网络层，并新增了如下功能

1. 在网络层新增了HTTPDNS，有效避免由于运营商传统 LocalDNS 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。
2. 在网络层接入QUIC，提升弱网加载图片成功率，增强用户体验。
3. SDK内部增加了重试机制，并支持自定义重试次数以及重试间隔时间，用于降低因为网络波动造成图片加载失败的风险。
4. 若项目中使用到TPG或AVIF图片，可开启原图保护策略，若TPG、AVIF图加载失败，可自动加载原格式图片，从而不影响用户使用。并将解错误收集用于排查解码失败原因及时修复。
5. 自定义加载图片并发数。
>?

接下来逐一介绍每个功能的详细使用，以及示例代码。

### 一、接入CIDownloader
接入CIDownloader只需在Podfile新增CIDownloader的依赖即可。
```
pod 'CloudInfinite/CIDownloader'
```
SDK内部自动检测是否有该类，并加入到SDWebImage loader管理器中。

* 动态配置是否使用CIDownloader；
```
[CIImageDownloader sharedDownloader].canUseCIImageDownloader = ^BOOL(NSURL * _Nonnull url, SDWebImageOptions options, SDWebImageContext * _Nonnull context) {
/// 业务判断是否使用CIImageDownloader 加载图片，还是SDWebImage 自带loader加载图片
    return YES;
};
```
 
### 二、接入HTTPDNS

万象SDK提供两种方式接入HTTPDNS：
1. 使用自定义HTTPDNS解析

    使用自定义HTTPDNS解析，需要自定义类并实现`QCloudHTTPDNSProtocol`协议。
    ```
    @interface MyHTTPDNSHandler ()<QCloudHTTPDNSProtocol>
    @end

    @implementation MyHTTPDNSHandler
    -(NSString *)resolveDomain:(NSString *)domain{
        NSString * ipString = ... // 自己实现dns解析。
        return ipString;
    }
    @end
    ```
    将该类对象设置给`[QCloudHttpDNS shareDNS].delegate`。
    ```
    self.handler = [MyHTTPDNSHandler new];
    [QCloudHttpDNS shareDNS].delegate = self.handler;
    ```

2. 使用万象自带的 CIDNS

    接入CIDNS首先需要在Podfile中添加
    ```
    pod 'CloudInfinite/CIDNS'
    ```

    >?CIDNS封装了腾讯HTTPDNS，接入CIDNS需要在腾讯HTTPDNS申请密钥相关信息，具体请查[HTTPDNS接入](https://cloud.tencent.com/document/product/379/77755)
    ```
    /// 配置Dnsconfig。
    /// 参数含义请查看https://cloud.tencent.com/document/product/379/77755。
    DnsConfig config;
    config.appId = @"appid";
    config.dnsIp = @"dnsIp";
    config.dnsId = dnsId;
    config.dnsKey = @"dnsKey";//des的密钥
    config.encryptType = HttpDnsEncryptTypeDES;
    config.debug = YES;
    config.timeout = 5000;
    /// 实例化CIDNSLoader 。注意[QCloudHttpDNS shareDNS].delegate为弱引用，dnsloader需一个强引用持有，否则dnsloader会提前释放。
    self.dnsloader = [[CIDNSLoader alloc] initWithConfig:config];
    /// 将代理dnsloader设置给[QCloudHttpDNS shareDNS].delegate。
    [QCloudHttpDNS shareDNS].delegate = self;
    ```

### 三、接入QUIC
>?若使用QUIC，请点击[这里](https://cloud.tencent.com/document/product/436/37708)联系联系相关同学开白名单

1. 接入QUIC，首先需要在Podfile文件中添加Quic。
    ```
    pod 'CloudInfinite/Quic'
    ```

2. 开启QUIC以及配置。
    ```
    /// 启用QUIC
    [CIImageDownloader sharedDownloader].enableQuic = YES;

    /// 配置QUIC白名单，指定那些host使用QUIC，若不配置，则认为CIImageDownloader全部请求都走QUIC
    [CIImageDownloader sharedDownloader].quicWhiteList = @[@"test.***.com"];

    /// quic高级配置，具体查看QCloudQuicConfig类。
    [QCloudQuicConfig shareConfig].race_type = QCloudRaceTypeQUICHTTP;
    ...
    ```
### 四、配置重试策略
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

### 五、设置请求图片并发数
CIImageDownloader 支持设置请求图片并发数量。
customConcurrentCount 为当前并发数量，SDK内部根据网络状况自动增加或降低并发数量，最小为1，最大为maxConcurrentCount。

```
[CIImageDownloader sharedDownloader].customConcurrentCount = 3;
[CIImageDownloader sharedDownloader].maxConcurrentCount = 10;
```

### 六、开启TPG、AVIF原图保护例代码
原图保护为TPG、AVIF模块所独有功能，适用于 使用`CloudInfinite/SDWebImage-CloudInfinite`加载TPG、AVIF图片。
功能描述：当TPG、AVIF图片加载失败时，自动请求原格式图片，提升用户体验。并将TPG、AVIF加载失败原因返回，用于排查失败原因及时修复。

* 开启原图保护
    ```
    [UIView setLoadOriginalImageWhenError:YES];
    ```

* 自定义TPG、AVIF链接转换原格式图片链接
    ```
    [UIView setLoadTPGAVIFImageErrorHandler:^NSString * _Nullable(NSString * _Nonnull url) {
        // 将TPG、AVIF图片链接装换位原格式图片。
        return url;
    }];
    ```

* 添加tpg、avif加载失败监听，获取url以及错误信息，可以用于日志上报以及排查原因。

    ```
    [UIView setTPGAVIFImageErrorObserver:^(NSString * _Nonnull url, NSError * _Nonnull error) {
    // 加载tpg、avif 图片报错时回调，返回链接以及对应的错误信息 
    }];
    ```

