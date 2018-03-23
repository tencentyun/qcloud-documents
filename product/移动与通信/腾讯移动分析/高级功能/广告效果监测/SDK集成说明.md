要使用 MTA 广告效果监测与分析，您需要先在 App中集成 MTA 的 SDK，集成步骤如下：
1. 集成 MTA 的基础 SDK （[Android快速集成入口](/document/product/549/12862) | [iOS快速集成入口](/document/product/549/12857)），如果您已集成过 MTA 的基础 SDK ，可跳过该步骤；
2. 集成广告监测模块（[Android集成代码]() | [iOS集成代码]()），并上报广告监测标准事件；
3. 若您的推广目标是 H5 页面（简称“落地页”），最终通过落地页下载应用统计，您可以在落地页嵌入 MTA 的 JS 代码，可以做到一个落地页多渠道、多平台的统计，适用于微信内、分享、地推、二维码等各场景（[Android集成配置]() | [iOS集成配置]() | [落地页多渠道多平台配置]()）

## Android SDK广告监测模块集成指南
### 接口调用

**注册事件**
通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化。

**接口说明：**
```
tatService.trackRegAccountEvent(Context context,String user ，AccountType type);
```
**参数说明：**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|context	|是	|当前上下文
|user|	是	|用户名，最多64个字符|
|type|	是	|目前支持手机号(" mobile ")、邮箱(" mail ")、微信ID(" WX")、QQ号("QQ").<br> 如：StatConfig.AccountType.WX

**付费事件**
通过上报付费事件，您可以统计到每一次投放的LTV值从而衡量您的投资回报率。

**接口说明：**
```
StatService.trackPayEvent(Context context, String cy, String id, double money, CurrencyType type);
```
**参数说明：**

|参数名|	是否必要	|参数描述|
| :-----: | :------: | :--------:|
|context	|是	|当前上下文|
|cy	|是	|支付方式（最多64个字符）.如（"wx"、"Alipay"）等|
|id	|是	|订单号等（最多64个字符）.如（"88888999955542"）等|
|money	|是|	金额.如（88.8）|
|type|	是	|目前支持两种：CNY人民币("CNY")、USD美金("USD")。如StatConfig.CurrencyType.CNY|

**其他自定义事件**
若您希望上报其他自定义的用户行为，您可以参考MTA自定义事件： [自定义事件介绍](/document/product/549/13057) | [Android接口](/document/product/549/13066) | [iOS接口](/document/product/549/13067)
## iOS SDK广告监测模块集成指南
### 工程配置
引入 adtracker 文件夹下的 .a 文件和头文件,以及 idfa 文件夹下的 libidfa.a 到 Xcode 工程之中。

### 接口调用
>注意：
>激活后的活跃事件的上报, 请在主线程中调用。

**注册事件 **
通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化

**接口说明**

```
 (void)trackRegAccountEvent:(MTAADAccountType)accountType account:(NSString *)account
```
 
**参数说明**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|accountType|	是|	账号类型|
|account|	是	|具体的账号|
**付费事件 **

通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化。

**接口说明**
```
(void)trackUserPayEvent:(MTAADPayMoneyType)moneyType orderID:(NSString *)orderID
                   payNum:(double)payNum
                  payType:(NSString *)payType; 
```

**参数说明**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|moneyType|	是	|货币种类，支持两种：人民币、美金|
|orderID	|是|	订单ID， 或交易流水号|
|payNum	|是	|订单金额|
|payType	|是	|支付类型，如微信、支付宝、银联等|

**其他自定义事件**
若您希望上报其他自定义的用户行为，您可以参考MTA自定义事件： [自定义事件介绍](/document/product/549/13057) | [Android接口](/document/product/549/13066) | [iOS接口](/document/product/549/13067)

## Android JS SDK配置
### 工程配置
1. 【必选】要在 MTA 前台开通并配置相关的推广计划；
2. 【必选】在 App 的入口处，一般为 Application 或 MainActivity 的 onCreate() 调用`StatConfig.setTLinkStatus(true);`
3. 【可选】若有接入腾讯 TBS 浏览服务 SDK ，请在主线程调用`QbSdk.initX5Environment()`方法后面添加<br>&emsp;&emsp;&emsp;&nbsp;`StatConfig.invokeTBSSdkOnUiThread(context);`

### 落地页 JS 配置
以下为嵌入落地页的 js sdk 格式，必须填写替换参数：

|参数名|参数描述|
| :---: | :---:|
|$download_btn_id | 下载按钮的id
|$app_key|MTA 管理台中 Android 的 App KEY

```
<script>
var _mta_btn_id = '$download_btn_id';
 (function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "$app_key");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```

**使用示例**
```
<a id="download_app">下载应用</a>

<script>
var _mta_btn_id = 'download_app';
(function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "IB7ZRJ6V8S1T");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```

## iOS JS SDK配置
### 工程配置
**1. 统计安装来源( URL Scheme )**
&emsp;&emsp;XCode 中的 URL Types 中增加一条 URL Scheme 配置，Role 是 Viewer 。URL Schemes 的配置后续在 JS SDK 的初始化会用到。
**2. 如果已安装 App ，直接打开(非必需，通过 Universal Links 技术 )**
&emsp;&emsp;i. 首先你需要有一个https的域名，例如domain.com。
&emsp;&emsp;ii. Uninversal Links 需要的 json 文件的【 apple-app-site-association 】，可以从MTA管理台生成。
&emsp;&emsp;iii. 把apple-app-site-association上传到domain.com根目录(iOS系统会自动从https://domain.com/apple-app-site-association 进行访问)
&emsp;&emsp;iiii. XCode的capabilities增加Domains的配置，例如applinks:domain.com
**3.下载页面的修改**
&emsp;&emsp;请参考MTA管理台中关于JS SDK的说明。
>注意：
>因为用到了keychain，如果遇到相关编译不过的问题，请在项目中引用Security.framework。

### 接口调用
AppDelegate中的改动
 1. 在MTA的初始化之后增加[ADTracker getInstance]
 ```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    [[MTAConfig getInstance] setSmartReporting:YES];
    [[MTAConfig getInstance] setReportStrategy:MTA_STRATEGY_INSTANT];
    [[MTAConfig getInstance] setDebugEnable:YES];
    [MTA startWithAppkey:@"I2E3KXDU1E2W"];
    [ADTracker getInstance];
    return YES;
}
```
 2. 在 handleOpenURL 中增加调用
 ```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [[ADTracker getInstance] handleOpenURL:url];
    return true;
}
``` 
 3. 在 App 进入的第一个 ViewController 的修改
&emsp;viewDidLoad中添加以下代码
```
(void)viewDidLoad {
    [super viewDidLoad];
    [[ADTracker getInstance] startByViewDidload];
}
```

 4. 如果有自己的中间页，不使用 MTA 管理台生成的话。需要单独接入JS SDK，并设置中间页的地址.
didFinishLaunchingWithOptions 的初始化修改如下

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    [[MTAConfig getInstance] setSmartReporting:YES];
    [[MTAConfig getInstance] setReportStrategy:MTA_STRATEGY_INSTANT];
    [[MTAConfig getInstance] setDebugEnable:YES];
    [MTA startWithAppkey:@"I2E3KXDU1E2W"];
    [[ADTracker getInstance] setChannelUrl:@"http://domain.com/test/download.html"];
    return YES;
}
```

>注意： 
>1. http://domain.com/test/download.html 这代表着你投放的网址可能是
>http://domain.com/test/download.html?ADTAG=youradtag ;
>http://domain.com/test/download.html?ADTAG=youradtag2;
>http://domain.com/test/download.html?ADTAG=youradtag3 等等。
>2. 请替换 http://domain.com/test/download.html 为实际的中间页地址。
>3. JS SDK的使用参考MTA管理台相关页面。

### 落地页JS配置
以下为嵌入落地页的 js sdk 格式，必须填写替换参数：

|参数名	|	参数描述|
| :----: | :----: |
|$download_btn_id | 下载按钮的 id|
|$app_key |MTA 管理台中 iOS 的 App KEY|
|$URL_Scheme| iOS App 的 URL Scheme|
```
<script>
var _mta_btn_id = '$download_btn_id';
 (function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "$app_key");
  mta.setAttribute("app_flag", "$URL_Scheme");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```
**使用示例**
```
<a id="download_app">下载应用</a>
<script>
var _mta_btn_id = 'download_app';
(function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "IB7ZRJ6V8S1T");
  mta.setAttribute("app_flag", "mtaApp");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```

## 落地页多渠道多平台配置
若您需要在微信、朋友圈、二维码、短信等场景下进行推广，且推广地址为活动页面，可以使用以下方案：
在落地页（活动页面）嵌入 JS SDK 时，可以在代码中根据当前访问页面的设备系统(参考 HTTP Useragent )将$adtag设置成您在 MTA 获得的 TLink 中的后缀 ADTAG值，同时将 $app_key 也设置成在 MTA 中获得的不同平台的 Appkey 即可。
```
<script>
var _mta_btn_id = '$download_btn_id';
 var _mta_adtag = '$adtag';
 (function() {
      var mta = document.createElement("script");
      mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
      mta.setAttribute("name", "MTA_CHANNEL");
      mta.setAttribute("app_key", "$app_key");
      mta.setAttribute("app_flag", "$URL_Scheme"); (Android不需要该行)
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(mta, s);
    })();
</script>
```
**使用示例**
在MTA管理台Android和iOS中各配置两个推广链接： iOS: http://xxxxx.com?ADTAG=111 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;Android: http://xxxx.com?ADTAG=222 
其中iOS的 Appkey 为 AAAAAAAA，Android 的 Appkey 为 BBBBBBB（见管理台 -> 配置管理 -> 应用信息页面） 则在活动页面中判断，若当前设备为 iOS，将 $adtag 设置成 111，同时 $app_key 设置为 AAAAAAAA；若当前设备为Android, 将 $adtag 设置成 222，同时 $app_key 设置为 BBBBBBB。
>注意:
>如果需要多个链接跳转同一个落地页，同时每个链接都需要统计Android和iOS，则可以在跳转至落地页前将ADTAG附在URL的参数中