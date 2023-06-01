
本文主要介绍如何在使用 Glide 时集成 QCloud 网络库。

QCloud 网络库 SDK 自定义了 GlideUrl 的 ModelLoader，接管图片加载网络层，并新增了如下功能

1. 在网络层新增了 HTTPDNS，有效避免由于运营商传统 LocalDNS 解析导致的无法访问最佳接入点的方案。原理为使用 HTTP 加密协议替代传统的 DNS 协议，整个过程不使用域名，大大减少劫持的可能性。
2. 在网络层接入 QUIC，提升弱网加载图片成功率，增强用户体验。
3. SDK 内部增加了重试机制，并支持自定义重试次数以及重试间隔时间，用于降低因为网络波动造成图片加载失败的风险。
4. 自定义加载图片并发数。

### 安装 Glide 和 QCloud 网络库

Glide 是一个知名开源的图片缓存库。更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
implementation 'com.qcloud.cos:qcloud-decoder-network:1.1.0'
implementation 'com.github.bumptech.glide:glide:version'
```

### 注册 ModelLoader

通过 AppGlideModule 注册相关 ModelLoader 实现相应功能。
```
 // 注册自定义 GlideModule
 // 类库开发者可以继承 LibraryGlideModule 创建类似的注册类
@GlideModule
public class MyAppGlideModule extends AppGlideModule {
    @Override
    public void registerComponents(@NonNull Context context, @NonNull Glide glide, Registry registry) {
        // 使用QCloudHttpUrlLoader加载GlideUrl
        // 此处使用prepend 而不是replace是因为QCloudHttpUrlLoader可以根据url设置只接管部分网络请求(例如 只接管tpg或avif)，其他的还是走默认网络层

        QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder().builder();
        QCloudGlideUrlCallback glideUrlCallback = new QCloudGlideUrlCallback() {
            @Override
            public boolean handles(@NonNull GlideUrl url) {
                // 返回需要处理什么类型的url，例如tpg或avif格式的url
                // 处理方式可以参考QCloudFormatUtils中默认的方式
                return false;
            }
        };
        registry.prepend(GlideUrl.class, InputStream.class,
                new QCloudHttpUrlLoader.Factory(context.getApplicationContext(), qCloudHttpConfig, glideUrlCallback)
        );

        // QCloudHttpConfig和QCloudGlideUrlCallback也支持不传，即默认值，QCloudGlideUrlCallback的默认值是只处理标准的数据万象tpg和avif格式url
        //registry.prepend(GlideUrl.class, InputStream.class, new QCloudHttpUrlLoader.Factory(context.getApplicationContext()));
    }
}
```
注册完毕后，通过 Glide 加载网络图片时的网络请求就会由 QCloud 网络库接管。
QCloud 网络库的配置和功能主要是通过 QCloudHttpConfig 进行设置，详情见以下功能和配置。

### 接入 HTTPDNS

通过 QCloudHttpConfig 的 setDnsFetch 方法进行 DNS 设置。

```
QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder()
        .setDnsFetch(new QCloudHttpClient.QCloudDnsFetch() {
            @Override
            public List<InetAddress> fetch(String hostname) throws UnknownHostException {
                //根据hostname获取对应的IP列表
                //返回对应的InetAddress列表
                return inetAddressList;
            }
        })
        .builder();
```

以下用腾讯云 HTTP DNS 作为示例。更多信息，请参见 [腾讯云 HTTP DNS 官方文档](https://cloud.tencent.com/product/httpdns)。

```
QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder()
        .setDnsFetch(new QCloudHttpClient.QCloudDnsFetch() {
            @Override
            public List<InetAddress> fetch(String hostname) throws UnknownHostException {
                //使用MSDKDnsResolver之前需要在合适的地方初始化HTTP DNS SDK，例如在Application中
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
        .builder();
```

### 接入 QUIC
>?若使用 QUIC，请点击[这里](https://cloud.tencent.com/document/product/436/37708)联系联系相关同学开白名单

1. 接入 QUIC，首先需要在 Gradle 文件中添加 QUIC 库依赖。
    ```
    implementation 'com.qcloud.cos:quic:1.5.39'
    ```

2. 开启 QUIC。
    ```
    QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder()
        .enableQuic(false)
        .builder();
    ```

### 配置超时时间和重试策略
通过 QCloudHttpConfig 的 setConnectionTimeout 和 setSocketTimeout 方法设置超时时间，
通过 QCloudHttpConfig 的 setRetryStrategy 设置重试策略。

```
QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder()
                .setConnectionTimeout(15 * 1000)
                .setSocketTimeout(30 * 1000)
                .setRetryStrategy(RetryStrategy.DEFAULT)
                .builder();
```

### 设置请求图片最大并发数
通过 QCloudHttpConfig 的 setDownloadMaxThreadCount 方法进行请求图片最大并发数设置。
SDK 内部会根据网络状况自动增加或降低并发数量，最小为1，最大为 setDownloadMaxThreadCount 设置的值，默认为 5。

```
QCloudHttpConfig qCloudHttpConfig = new QCloudHttpConfig.Builder()
        .setDownloadMaxThreadCount(5)
        .builder();
```