### How to Activate TLink Feature

1. [Required] Activate and configure the relevant promotion program on MTA frontend.
2. [Required] Activate TLink feature at the entry of App (generally, "StatConfig.setTLinkStatus(true);" is called by onCreate() of Application or MainActivity).
3. [Optional] If SDK accessing Tencent TBS browsing service is available, add "StatConfig.invokeTBSSdkOnUiThread(context);" after "QbSdk.initX5Environment()" to be called by the main thread.


### JS SDK Configuration of Android Landing Page
The following is the JS SDK format of the embedded landing page and replacement parameters must be filled in:
$download_btn_id: The ID of the download button
$app_key: Android APP KEY in MTA management console

```js
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
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```
