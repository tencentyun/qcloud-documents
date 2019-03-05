如果您需要在微信、朋友圈、二维码、短信等场景下进行推广，且推广地址为活动页面，可以使用以下方案：

在落地页（活动页面）嵌入 JS SDK 时，可以在代码中根据当前访问页面的设备系统( 参考 HTTP Useragent )将 $adtag 设置成您在 MTA 获得的 TLink 中的后缀 ADTAG 值，同时将 $app_key 也设置成在 MTA 中获得的不同平台的 Appkey 即可。

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

**使用示例：**
在 MTA 管理台 Android 和 iOS 中各配置两个 Tlink：
- iOS: `http://xxxxx.com?ADTAG=111 `
- Android:  `http://xxxx.com?ADTAG=222 `

其中 iOS 的 Appkey 为 AAAAAAAA，Android 的 Appkey 为 BBBBBBB（见[管理台](http://mta.qq.com/mta/overview/ctr_all_app_new)->配置管理->应用信息页面） 则在活动页面中判断，若当前设备为 iOS，将 $adtag 设置成 111，同时 $app_key 设置为 AAAAAAAA；若当前设备为 Android, 将 $adtag 设置成 222，同时 $app_key 设置为BBBBBBB。

（如果需要多个链接跳转同一个落地页，同时每个链接都需要统计 Android 和 iOS，则可以在跳转至落地页前将 ADTAG 附在 URL 的参数中）
