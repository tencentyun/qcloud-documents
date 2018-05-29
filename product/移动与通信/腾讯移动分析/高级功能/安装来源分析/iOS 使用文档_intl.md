### Configuring Projects
1. Statistics on installation source (URL Scheme)
The configuration of URL Scheme is added to URL Types in XCode, and Role is Viewer. This configuration will be used in the initialization of JS SDK afterwards.
2. If the App has been installed, open it directly (using the Universal Links technology; optional).
i. A https domain name is required, such as domain.com.
ii. The json file (apple-app-site-association) used by Uninversal Links can be generated from MTA console.
iii. Upload apple-app-site-association to the root directory of domain.com (iOS system will automatically access it from `https://domain.com/apple-app-site-association`).
iiii. The configuration of Domains is added to capabilities of XCode, such as applinks:domain.com.
3. Modification of the download page
For more information, please see JS SDK description on MTA console.
4. Note
As keychain is used, if the relevant compiling failed, reference Security.framework in the project.

### Calling API
1. Modification in AppDelegate
Add [Installtracker getInstance] after MTA is initialized.

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

Call it in handleOpenURL.
```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    
    [[Installtracker getInstance] handleOpenURL:url];
    
    return true;
}
```

A general link. If the App has been installed, open it directly.
```
- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler
{
    BOOL result = [[Installtracker getInstance] checkIsFromMTARefer:userActivity];
    return result;
}
```

2. Modification of the first ViewController after the App is opened.

The following codes are added to viewDidLoad:
```
- (void)viewDidLoad {
    [super viewDidLoad];
    
    [[Installtracker getInstance] startByViewDidload];
    
}
```
3. If you have your own intermediate page and do not use MTA console for generation, you need to access JS SDK and set the address of the intermediate page. The initialization of didFinishLaunchingWithOptions is modified as follows:
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
>**Notes:**
>i. Note that `http://domain.com/test/download.html` means that the delivery websites may be `http://domain.com/test/download.html?ADTAG=youradtag`, `http://domain.com/test/download.html?ADTAG=youradtag2` or `http://domain.com/test/download.html?ADTAG=youradtag3 `. 
>ii. Please replace `http://domain.com/test/download.html ` with the actual intermediate page address.
>iii. For more information on how to use JS SDK, please see the related pages on MTA console.

### JS SDK Configuration of iOS Landing Page

The following is the JS SDK format of the embedded landing page and replacement parameters must be filled in:
$download_btn_id: The ID of the download button
$app_key: iOS APP KEY in MTA console.
$URL_Scheme: URL Scheme of iOS App.

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
Example:
```js
<a id="download_app">Download App</a>

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
