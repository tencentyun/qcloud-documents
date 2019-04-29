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