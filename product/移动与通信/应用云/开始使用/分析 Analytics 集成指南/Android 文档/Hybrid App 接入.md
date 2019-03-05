## Hybrid App 简介

Hybrid App 指包含原生页面和 html5 页面的 App。MTA hybrid 支持统计 Android/iOS + webview 开发的应用数据。


### 功能介绍

MTA 提供 Hybrid App 接入服务，为用户提供更完善的数据服务，用户接入后可实现：

- 统一统计 App 内全部数据，无需跳转查看，打破 App 与 H5 的边界。
- 连接 App 与 H5 之间的关键路径，事件漏斗更完整。
- 可统计 H5 页面数据，访问路径更完整。

### 实现原理

H5 使用 JavaScript SDK ，采集到数据后，发往 App，App SDK 收到 JavaScript SDK 发送的数据后，会把默认采集的属性加上，最后如果 App 端设置了公共属性，也会把公共属性加上。使用了混合统计功能以后，在 App 内加载的 html5 页面也能通过 Native 的方式上报页面访问事件和自定义 kv 事件。

使用混合统计功能时，需要在 iOS、Android 以及 HTML 端同时接入对应的 SDK。


## Android 侧接入

### 准备工作

Hybrid 统计是在原生统计基础上进行的，在开始之前，请确保已按照 [MTA Android 快速入门](https://cloud.tencent.com/document/product/666/14313) 接入我们原生统计 SDK。


### 设置监控 WebView

```
WebView webView = findViewById(R.id.webview);

// 这里必须使能运行 js 脚本
WebSettings webSettings = webView.getSettings();
webSettings.setJavaScriptEnabled(true);

// 给 webview 添加监控
TACAnalyticsService.getInstance().monitorWebViewEvent(webView);
```

### 配置 WebViewClient

MTA 需要在 WebViewClient 的 shouldOverrideUrlLoading 方法调用 SDK 接口，进行 URL 拦截。

```
webView.setWebViewClient(new WebViewClient() {

    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        // 尽量保证放在第一行
        if(TACAnalyticsService.getInstance().handleWebViewUrl(view, url)){
            return true;
        }
        super.shouldOverrideUrlLoading(view, url);
        return true;
    }
});

// 如果不能保证放在第一行处理，请按照以下方式处理
webView.setWebViewClient(new WebViewClient() {

	@Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        try {
            String decodedURL = java.net.URLDecoder.decode(url, "UTF-8");
            if (!TextUtils.isEmpty(decodedURL) &&
                    url.toLowerCase().startsWith("tencentMtaHyb:".toLowerCase())){
                TACAnalyticsService.getInstance().handleWebViewUrl(view, url);
                return true;
            } else{
                // 其它url的处理逻辑
            }
        } catch (UnsupportedEncodingException ex){
        }
        return super.shouldOverrideUrlLoading(view, url);
    }
});

```
## iOS 侧接入
### 准备工作

Hybrid 统计是在原生统计基础上进行的，在开始之前，请确保已按照 [MTA iOS 快速入门](https://cloud.tencent.com/document/product/666/14315) 接入我们原生统计 SDK。


### 设置监控 UIWebView

```
//给指定的webView引入Hybrid的功能，请保证该行代码在设置代理之前调用，方能保证相关逻辑被注入到代理中
[TACAnalyticsService catchExceptionForUIWebView:_webView];
 _webView.delegate = self;
```

### 设置监控 WKWebView

```
//给指定的wkWebView加入Hybrid的功能，请保证该行代码在设置代理之前调用，方能保证相关逻辑被注入到代理中
[TACAnalyticsService catchExceptionForWKWebView:_wkWebView];
_wkWebView.navigationDelegate = self;
```

## JavaScript SDK 使用说明

### App&H5 联动分析接入

需要统计 App Webview 的基础访问、点击事件时，请在 webview 里加入以下 JS 代码：

```
<script src="//pingjs.qq.com/mta/app_link_h5_stats.js" name="MtaLinkH5"></script>
```
 后续的方法上报都必须保证已加载以上 JS SDK。

### 手动上报页面访问统计

访问页面时，上报页面访问情况：

```
MtaLinkH5.pageBasicStats({
  'title': '必填-每页要求不重复'
});
```

> - 确定联动分析 JS SDK 已载入，并且设置了 title 名称；
> - title 为必填项目，并且每页的 title 都要求不重复，重复影响统计。

### 设置登录帐号

用于设置用户登录帐号信息：

```
MtaLinkH5.setLoginUin(uin);
```

> - 确定联动分析 JS SDK 已载入；
> - uin 为设置的用户帐号，String 类型。


### 自定义事件

用于页面自定义事件埋点上报：

```
MtaLinkH5.eventStats(event_id, param_json);
```

> - 确定联动分析 JS SDK 已载入；
> - event_id 为事件 ID，在事件中添加后拷贝过来；
> - param_json 为事件参数以及事件参数值，每个参数对应一个参数值，为 json 格式。

示例：

```
<button onclick="MtaLinkH5.eventStats('test_event')">事件-不带参数</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1'})">事件-单个参数</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1','param2':'value2'})">事件-多个参数-参数建议最多不超过5个</button>
```

### 注意事项

- 只统计 App 内的 H5 数据，不统计 App 外的 H5 数据；
- 集成之后事件中 H5 页面的事件会标记展示；
- 页面统计中的 H5 页面会进行标记展示；
- H5 事件添加后需要进行事件上报后才有数据，具体请参见【自定义事件】；
- 本地安装 JS SDK（[npm 包链接](https://www.npmjs.com/package/mta-hybird-analysis)）；
- 不支持 x5 内核。
