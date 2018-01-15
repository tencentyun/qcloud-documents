### 如何启用 TLink 功能

1. 【必选】要在 MTA 前台开通并配置相关的推广计划；
2. 【必选】在 App 的入口处，一般为 Application 或 MainActivity 的 onCreate() 调用“StatConfig.setTLinkStatus(true);”开启TLink功能；
3. 【可选】若有接入腾讯 TBS 浏览服务 SDK，请在主线程调用“QbSdk.initX5Environment()”方法后面添加“StatConfig.invokeTBSSdkOnUiThread(context);”。


### Android落地页 JS SDK 配置
以下为嵌入落地页的 JS SDK 格式，必须填写替换参数：
$download_btn_id：下载按钮的 ID
$app_key：MTA 管理台中 Android 的 APP KEY

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
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```