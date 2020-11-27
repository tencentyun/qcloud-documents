腾讯云 X-P2P 解决方案，可帮助用户直接使用经过大规模验证的直播、点播、文件分发服务，通过经商用验证的 P2P 服务大幅节省带宽成本，提供更优质的用户体验。开发者可通过 SDK 中简洁的接口快速同自有应用集成，实现 Android 设备上的 P2P 加速功能。

传统 CDN 加速服务中，客户端向 CDN 发送 HTTP 请求获取数据。在腾讯云 X-P2P 服务中，SDK 可以视为下载代理模块，客户端应用将 HTTP 请求发送至 SDK，SDK 从 CDN 或其他 P2P 节点获取数据，并将数据返回至上层应用。SDK 通过互相分享数据降低 CDN 流量，并通过 CDN 的参与，确保了下载的可靠性。

> ? SDK 支持多实例，即支持同时开启多个不同资源的直播 P2P。

## 支持的 ABI
当前 Android SDK 支持的 ABI 架构如下：
- armeabi-v7a
- arm64-v8a
- x86
- x86_64

## 添加依赖

### aar 接入
1. 将 `xnet-release.aar` 文件拷贝到 libs 目录下。
2. 在应用模块的 `build.gradle` 中加入代码：
``` gradle
dependencies {
    implementation fileTree(include: ['*.jar'], dir: 'libs')
    implementation (name: 'xnet-release', ext: 'aar')
}
```

### gradle 组件包接入
通过 bintray 获取我们的 gradle 最新 SDK 包：
``` gradle
implementation 'com.tencent.qcloud:xnet:release-1.0.2'
```

## 混淆配置
由于 native 层代码需要反射调回 java，需要确保 SDK 内的代码都不被混淆，请在 proguard 中添加以下配置：
```
-keep public class com.tencent.qcloud.** {
    *;
}
```

## SDK 接入步骤
### 步骤1：初始化
初始化 `XP2PModule` 后启动 App，并初始化 P2P SDK。

``` java
// 初始化APP_ID等关键客户信息
final String APP_ID = "$your_app_id";
final String APP_KEY = "$your_app_key";
final String APP_SECRET = "$your_app_secret";

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    // 返回值ok可用于统计p2p成功与失败
    // 无论成功与失败，都可以使用XNet.proxyOf与XNet.proxyOf
    // 失败时，XNet.proxyOf是""
    // 成功时，XNet.proxyOf是127.0.0.1:16080/${domain}
    bool ok = XNet.create(this, APP_ID, APP_KEY, APP_SECRET);

    //开启调试日志(发布可关闭)
    XNet.enableDebug();
}
```

### 步骤2：接入直播 Live 

#### 播放控制（start/stop）
启动直播 P2P：
``` java
// 初始化appId等关键客户信息
final String APP_ID = "$your_app_id";
final String APP_KEY = "$your_app_key";
final String APP_SECRET = "$your_app_secret";

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    // 返回值ok可用于统计p2p成功与失败
    // 无论成功与失败，都可以使用XNet.proxyOf与XNet.proxyOf
    // 失败时，XNet.proxyOf是""
    // 成功时，XNet.proxyOf是127.0.0.1:16080/${domain}
    bool ok = XNet.create(this, APP_ID, APP_KEY, APP_SECRET);

    //开启调试日志(发布可关闭)
    XNet.enableDebug();
}
```

由于后台监听限制的问题，resume 的情况下需要调用 resume 接口：
``` java
    // 返回值ok代表着是否恢复成功
    bool ok = XNet.resume();
```

###  步骤3：接入 P2P 文件下载
``` java
// 例如：http://domain/path/to/some.file?params=xxx
// 变成：http://{XNet.proxyOf(file.p2p.com)}/file=http://domain/path/to/some.file?params=xxx
// 要改的仅仅是在://后插入XNET.proxyOf
    String rawUrl = "http://domain/path/to/some.file?params=xxx"
    String p2pURl = XNet.proxyOf("file.p2p.com") + "/file?channel=" + URLEncoder.encode(rawUrl);

// 通过p2purl使用其他http接口下载文件
    URL url = new URL(p2pURl);
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
```
