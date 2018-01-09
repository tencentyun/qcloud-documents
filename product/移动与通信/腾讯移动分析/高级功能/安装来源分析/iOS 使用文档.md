### 工程配置
1. 统计安装来源（URL Scheme）
XCode 中的 URL Types 中增加一条 URL Scheme 配置，Role 是 Viewer，URL Schemes 的配置后续在 JS SDK 的初始化会用到。
2. 如果已安装 App，直接打开（非必需，通过 Universal Links 技术）。
i. 首先你需要有一个 https 的域名，例如 domain.com；
ii. Uninversal Links 需要的 json 文件：apple-app-site-association，可以从 MTA 管理台生成；
iii. 把 apple-app-site-association 上传到 domain.com 根目录（iOS 系统会自动从`https://domain.com/apple-app-site-association`进行访问）；
iiii. XCode 的 capabilities 增加 Domains 的配置，例如 applinks:domain.com。
3. 下载页面的修改
具体请参考 MTA 管理台中关于 JS SDK 的说明。
4. 备注
因为用到了 keychain，如果遇到相关编译不过的问题，请在项目中引用 Security.framework。

### 接口调用
1.AppDelegate 中的改动
在 MTA 的初始化之后增加[Installtracker getInstance]

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    
    [[MTAConfig getInstance] setSmartReporting:YES];
    [[MTAConfig getInstance] setReportStrategy:MTA_STRATEGY_INSTANT];
    
    [[MTAConfig getInstance] setDebugEnable:YES];
    
    [MTA startWithAppkey:@"I2E3KXDU1E2W"];
    
    [Installtracker getInstance];
    
    return YES;
}
```

在 handleOpenURL 中增加调用
```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    
    [[Installtracker getInstance] handleOpenURL:url];
    
    return true;
}
```

通用链接，如果 App 已经安装，直接打开
```
- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler
{
    BOOL result = [[Installtracker getInstance] checkIsFromMTARefer:userActivity];
    return result;
}
```

2.在 App 进入的第一个 ViewController 的修改

viewDidLoad 中添加以下代码
```
- (void)viewDidLoad {
    [super viewDidLoad];
    
    [[Installtracker getInstance] startByViewDidload];
    
}
```
3.如果有自己的中间页，不使用 MTA 管理台生成的话，需要单独接入 JS SDK 并设置中间页的地址，didFinishLaunchingWithOptions 的初始化修改如下：
```objective-c
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    
    [[MTAConfig getInstance] setSmartReporting:YES];
    [[MTAConfig getInstance] setReportStrategy:MTA_STRATEGY_INSTANT];
    
    [[MTAConfig getInstance] setDebugEnable:YES];
    
    [MTA startWithAppkey:@"I2E3KXDU1E2W"];
    
    [[Installtracker getInstance] setChannelUrl:@"http://domain.com/test/download.html"];
    
    return YES;
}
```
>**说明：**
>i. 注意`http://domain.com/test/download.html` 这代表着你投放的网址可能是`http://domain.com/test/download.html?ADTAG=youradtag` 、`http://domain.com/test/download.html?ADTAG=youradtag2`、`http://domain.com/test/download.html?ADTAG=youradtag3 `等。 
>ii. 请替换`http://domain.com/test/download.html `为实际的中间页地址。
>iii. JS SDK 的使用参考 MTA 管理台相关页面。

### iOS 落地页 JS SDK 配置

以下为嵌入落地页的 JS SDK 格式，必须填写替换参数：
$download_btn_id：下载按钮的 ID
$app_key：MTA 管理台中 iOS 的 APP KEY
$URL_Scheme：ios app的URL Scheme

```js
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
使用示例：
```js
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