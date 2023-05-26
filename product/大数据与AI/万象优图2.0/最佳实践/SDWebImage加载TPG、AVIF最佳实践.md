## SDWebImage加载TPG、AVIF最佳实践

### 通过 SDWebImage + 自定义网络层 + HTTPDNS + QUIC + 失败重试 + 原图保护 加载TPG、AVIF图

>! SDK 版本需要大于等于 v1.5.0。

##### 一、添加依赖
podfile文件中添加
```
pod 'CloudInfinite/CIDownloader' // 自定义网络层 + SDWebImage
pod 'CloudInfinite/CIDNS' // DNS模块，内部已封装腾讯HTTPDNS
pod 'CloudInfinite/Quic' // QUIC模块
pod 'CloudInfinite/TPG' // TPG解码器，根据实际需求 选择TPG或AVIF
pod 'CloudInfinite/AVIF' // AVIF解码器
```
##### 二、导入头文件

```
#import "CIDNSLoader.h"
#import "CIImageDownloader.h"
#import "SDWebImage-CloudInfinite.h"
#import "QCloudQuicConfig.h"
```

##### 二、初始化

```
@property (nonatomic,strong)CIDNSLoader * dnsloader;
```

```


{
    // 配置CIImageDownloader，指定哪些场景使用CIImageDownloader进行下载解码图片，
    // return YES;表示用CIImageDownloader，return NO;表示不用CIImageDownloader，用SDWebImage默认下载器。
    // 默认所有图片都使用CIImageDownloader。
    [CIImageDownloader sharedDownloader].canUseCIImageDownloader = ^BOOL(NSURL * _Nonnull url, SDWebImageOptions options, SDWebImageContext * _Nonnull context) {
        return YES;
    };

    // 配置HTTPDNS
    [self setupCIDNS];

    // 配置重试 ，sdk内部已默认重试3次间隔1s。
    [CIImageDownloader sharedDownloader].retryCount = 2;
    [CIImageDownloader sharedDownloader].sleepTime = 2;
    // 可选配置，sdk内部已有默认筛选
    [CIImageDownloader sharedDownloader].canUseRetryWhenError = ^BOOL(QCloudURLSessionTaskData * _Nonnull task, NSError * _Nonnull error) {
        // 指定哪些错误需要重试
        return YES;
    };

    //配置QUIC
    // 开启quic
    [CIImageDownloader sharedDownloader].enableQuic = YES;
    // 配置quic白名单，指定哪些host可用quic,不指定并开启 则表示全部使用quic
    [CIImageDownloader sharedDownloader].quicWhiteList = @[@"examples-1251000004.cos.ap-shanghai.myqcloud.com"];
    [QCloudQuicConfig shareConfig].race_type = QCloudRaceTypeQUICHTTP;

    // 开启原图保护
    // 开启请求TPG,AVIF加载失败时请求原图 
    [UIView setLoadOriginalImageWhenError:YES];
    // 可选配置，sdk内部将图片链接中format/tpg 或者 format/avif删除，如果不满足业务，则需自定义tpg、avif链接转换原图链接策略。
    [UIView setLoadTPGAVIFImageErrorHandler:^NSString *(NSString * _Nonnull url) {
        NSString * newUrl = @"";/// 将tpg、avif转换为原格式链接
        return url;
    }];

    // 配置并发量
    // 可选配置，sdk内默认并发3，最大并发6。
    [CIImageDownloader sharedDownloader].customConcurrentCount = 5;
    [CIImageDownloader sharedDownloader].maxConcurrentCount = 10;
}

-(void)setupCIDNS{
    DnsConfig config;
    config.appId = @"appId";
    config.dnsIp = @"1.1.1.1";
    config.dnsId = 000000;
    config.dnsKey = @"dnsKey";//des的密钥
    config.encryptType = HttpDnsEncryptTypeDES;
    config.debug = YES;
    config.timeout = 5000;
    self.dnsloader = [[CIDNSLoader alloc] initWithConfig:config];
    [QCloudHttpDNS shareDNS].delegate = self.dnsloader;
    
}
```
>? 使用QUIC需开启白名单

到这里所有配置完成，加载图片方式和SDWebImage用法一致，不用修改业务已有代码。

##### 三、TPG、AVIF原图保护错误收集。
原图保护方案主要用于提升用户体验，但是TPG、AVIF加载失败错误信息还是需要收集，并根据错误信息来分析排查问题，解决问题。

```
[UIView setTPGAVIFImageErrorObserver:^(NSString * _Nonnull url, NSError * _Nonnull error) {
    error 为解码失败的错误信息 可以在这里统一处理TPG、AVIF加载失败的错误信息。
}];
```

